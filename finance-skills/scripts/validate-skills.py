#!/usr/bin/env python3
"""
validate-skills.py — Finance Skills frontmatter/spec 校验器

校验所有 SKILL.md / CLAUDE.md 的合规性：
  - YAML frontmatter 必须是 --- 关闭（不能是 ...）
  - 必填：name / description
  - 推荐：risk_level / version / last_reviewed / argument-hint
  - description ≤ 1024 字符
  - body ≤ 500 行
  - name slug 合规（小写/数字/-）
  - risk_level 必须是 low/medium/high/critical

支持 --auto-fix 自动修两个最常见 bug：
  1. frontmatter 用 ... 关闭 → 改成 ---
  2. 表格行 || 开头 → 改成 |

用法：
  python3 scripts/validate-skills.py
  python3 scripts/validate-skills.py --auto-fix
  python3 scripts/validate-skills.py --scene tax-filing
  python3 scripts/validate-skills.py --strict

退出码：
  0 = 全部通过
  1 = 有 error
  2 = 有 warning（仅 --strict 下）
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("需要 pyyaml：pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent

# --- Constants ---
# SKILL.md 文件必须满足 spec；CLAUDE.md 和 references/*.md 是配置/知识文件，不强求 frontmatter
SKILL_FILE_PATTERNS = ["skills/*/skills/*/SKILL.md", "skills/*/SKILL.md"]  # atomic + master
CONFIG_FILE_PATTERNS = ["skills/*/CLAUDE.md", "skills/cold-start/SKILL.md", "skills/*/skills/*/AGENTS.md"]

REQUIRED_FIELDS = ["name", "description"]
RECOMMENDED_FIELDS = ["risk_level", "version", "last_reviewed", "argument-hint"]
VALID_RISK_LEVELS = {"low", "medium", "high", "critical"}
NAME_PATTERN = re.compile(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$")


def _is_skill_file(path: Path) -> bool:
    """判断是否需要 frontmatter 的 skill 文件"""
    rel = str(path.relative_to(ROOT))
    if rel.endswith("/SKILL.md") and "/skills/" in rel:
        # 场景下 skills/{x}/SKILL.md 是 atomic
        # skills/cold-start/SKILL.md 是顶层 SKILL.md
        return True
    return False


def _load_frontmatter(path: Path) -> tuple[dict | None, list[str]]:
    """读 frontmatter，返回 (data_dict, body_lines) 或 (None, [])"""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, []
    end = None
    for i in range(1, min(40, len(lines))):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, []
    fm_text = "\n".join(lines[1:end])
    try:
        data = yaml.safe_load(fm_text)
    except yaml.YAMLError:
        return None, []
    if not isinstance(data, dict):
        return None, []
    body_lines = lines[end + 1:]
    return data, body_lines


def validate_one(path: Path) -> tuple[list[str], list[str], bool]:
    """返回 (errors, warnings, fixable)"""
    errors, warnings = [], []
    fixable = False

    is_skill = _is_skill_file(path)
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    if not lines or lines[0].strip() != "---":
        if is_skill:
            errors.append("首行不是 ---")
        else:
            warnings.append("CLAUDE.md / references 无 frontmatter（配置文件，正常）")
        return errors, warnings, fixable

    # 找结束 — 检测 ... 是可修复的 bug
    end = None
    ellipsis_line_idx = None
    for i in range(1, min(40, len(lines))):
        if lines[i].strip() == "---":
            end = i
            break
        if lines[i].strip() == "...":
            ellipsis_line_idx = i
            fixable = True
            break
    if end is None and ellipsis_line_idx is None:
        errors.append("frontmatter 未在 40 行内关闭")
        return errors, warnings, fixable

    # 如果有 ... 且未找到 ---，自动修复后重读
    if ellipsis_line_idx is not None:
        lines[ellipsis_line_idx] = "---"
        text = "\n".join(lines)
        # 重新找 end
        for i in range(1, min(40, len(lines))):
            if lines[i].strip() == "---":
                end = i
                break

    fm_text = "\n".join(lines[1:end])
    try:
        data = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:
        errors.append(f"YAML 解析失败: {e}")
        return errors, warnings, fixable

    if not isinstance(data, dict):
        errors.append("frontmatter 不是 dict")
        return errors, warnings, fixable

    # 必填
    for f in REQUIRED_FIELDS:
        if f not in data or not data[f]:
            errors.append(f"缺必填字段: {f}")

    # name 校验
    if "name" in data:
        n = str(data["name"])
        if not NAME_PATTERN.match(n):
            errors.append(f"name '{n}' 不合法（仅小写字母/数字/-）")
        if len(n) > 64:
            errors.append(f"name 长度 {len(n)} > 64")
        if n.endswith("-"):
            errors.append("name 不能以 - 结尾")

    # description 长度
    if "description" in data:
        d = str(data["description"]).strip()
        if len(d) > 1024:
            errors.append(f"description 长度 {len(d)} > 1024")
        if len(d) < 60:
            warnings.append(f"description 过短 ({len(d)} 字符，建议 ≥ 60)")

    # risk_level
    if "risk_level" in data:
        rl = str(data["risk_level"]).lower()
        if rl not in VALID_RISK_LEVELS:
            errors.append(f"risk_level '{rl}' 不在 {VALID_RISK_LEVELS}")
    else:
        warnings.append("缺推荐字段: risk_level")

    # 推荐字段
    for f in RECOMMENDED_FIELDS:
        if f not in data:
            warnings.append(f"缺推荐字段: {f}")

    # body 长度
    body = "\n".join(lines[end + 1:])
    body_line_count = len([l for l in body.split("\n") if l.strip()])
    if body_line_count > 500:
        warnings.append(f"body {body_line_count} 行 > 500（应拆分到 references/）")

    return errors, warnings, fixable


def fix_ellipsis(path: Path) -> bool:
    """把 frontmatter 的 ... 关闭符改成 ---"""
    if not _is_skill_file(path):
        return False
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return False
    for i in range(1, min(40, len(lines))):
        if lines[i].strip() == "...":
            lines[i] = "---"
            path.write_text("\n".join(lines), encoding="utf-8")
            return True
    return False


def fix_broken_tables(path: Path) -> int:
    """把 || 开头的多行表格改成 |（去掉一个前导 |）"""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    fixed = 0
    new_lines = []
    for line in lines:
        if line.startswith("||") and (len(line) < 3 or line[2] != "|"):
            new_lines.append(line[1:])  # 去掉第一个 |
            fixed += 1
        else:
            new_lines.append(line)
    if fixed > 0:
        path.write_text("\n".join(new_lines), encoding="utf-8")
    return fixed


def main() -> int:
    parser = argparse.ArgumentParser(description="Finance Skills 校验器")
    parser.add_argument("--scene", help="只校验指定场景（按目录名）")
    parser.add_argument("--auto-fix", action="store_true", help="自动修复已知 bug（... 关闭符、|| 表格）")
    parser.add_argument("--strict", action="store_true", help="warning 也算失败")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式报告")
    args = parser.parse_args()

    if args.scene:
        # 场景模式：校验整个场景目录
        pattern = f"skills/{args.scene}/**/*.md"
    else:
        # 全局模式：只校验 SKILL.md（CLAUDE.md/references 是配置文件不强求）
        pattern = "skills/**/SKILL.md"
    files = sorted(ROOT.glob(pattern))

    if args.auto_fix:
        ellipsis_fixed = 0
        table_fixed = 0
        for f in files:
            if fix_ellipsis(f):
                ellipsis_fixed += 1
            n = fix_broken_tables(f)
            table_fixed += n
        print(f"🔧 auto-fix 完成: frontmatter ... 修复 {ellipsis_fixed} 个，表格 || 修复 {table_fixed} 行\n")

    # 校验
    total_errors = 0
    total_warnings = 0
    file_results = []
    for f in files:
        errs, warns, _ = validate_one(f)
        file_results.append((f, errs, warns))
        total_errors += len(errs)
        total_warnings += len(warns)

    if args.json:
        import json
        out = {
            "total_files": len(files),
            "errors": total_errors,
            "warnings": total_warnings,
            "files": [
                {
                    "path": str(f.relative_to(ROOT)),
                    "errors": errs,
                    "warnings": warns,
                }
                for f, errs, warns in file_results
                if errs or warns
            ],
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(f"扫描 {len(files)} 个文件（pattern={pattern}）\n")
        for f, errs, warns in file_results:
            if errs or warns:
                rel = f.relative_to(ROOT)
                print(f"📄 {rel}")
                for e in errs:
                    print(f"  ❌ {e}")
                for w in warns:
                    print(f"  ⚠️  {w}")
        if not any(errs or warns for _, errs, warns in file_results):
            print("✅ 所有文件合规")
        print(f"\n=== 汇总 ===")
        print(f"文件: {len(files)}")
        print(f"Errors: {total_errors}")
        print(f"Warnings: {total_warnings}")

    if total_errors > 0:
        return 1
    if args.strict and total_warnings > 0:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())