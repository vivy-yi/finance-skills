---
name: project-list
description: >-
  项目列表 — 扫描 ~/.config/finance-skills/projects/ 列出所有项目，标注状态、阶段、关键日期。
  适用情形：开始工作时查看活跃项目、做周报时盘点所有项目状态、切换前确认项目代码。
  触发词：项目列表、有哪些项目、活跃项目、项目状态总览。
  核心：自动扫描 + 按状态分组（活跃/规划/报告/已关闭）+ 高亮下次关键日期。
argument-hint: "[--status <status>] [--type <type>] [--upcoming <N>]"
risk_level: low
last_reviewed: 2026-06-14
version: 1.0.0
---

## 加载上下文

读取 `../references/项目空间结构.md` 了解 project.md 字段。

---

# /finance:project-list — 项目列表

扫描 `~/.config/finance-skills/projects/` 目录，列出所有项目并按状态分组。

## 命令格式

```
/finance:project-list [--status <状态>] [--type <类型>] [--upcoming <N>]
```

参数：
- `--status` 过滤状态：`planning` / `active` / `fieldwork` / `reporting` / `closed`
- `--type` 过滤类型：`annual-audit` / `budget-review` / `tax-filing` / `m-and-a` / `other`
- `--upcoming <N>` 只显示未来 N 天内有里程碑的项目

## 输出格式

```
════════════════════════════════════════
📋 项目列表（按状态分组）
扫描时间: {YYYY-MM-DD HH:MM}
项目总数: {N}
════════════════════════════════════════

【活跃 / 执行中】
 1. 2026-audit-ic                  [fieldwork]
    年度内部控制审计
    负责人: CFO 张三 | 周期: 2026-01-01 ~ 2026-12-31
    下次关键日期: 2026-06-30 管理层评审会 (5 天后)
    完成度: 31/72 控制测试 (43%)

 2. tax-filing-2026                [active]
    2026 年度税务申报
    负责人: 税务经理李四 | 周期: 2026-01-01 ~ 2026-12-31
    下次关键日期: 2026-07-15 增值税申报 (20 天后)

【规划中】
 3. m-and-a-deal-alpha             [planning]
    M&A 项目 Alpha 尽调
    负责人: CFO 张三 | 周期: 2026-07-01 ~ 2026-09-30
    开始: 2026-07-01 (7 天后)

【报告阶段】
 4. Q2-2026-budget                 [reporting]
    Q2 2026 预算审查
    负责人: 财务经理王五 | 完成: 2026-06-10
    待审: CFO/CEO 审批

【已关闭】
 5. 2025-audit-ic                  [closed]
    2025 年度内部控制审计
    完成: 2026-03-15 | 缺陷: 重大 0 / 重要 3 / 一般 12
    整改完成率: 100%

════════════════════════════════════════
当前激活项目: {current-project-code}（如有）
════════════════════════════════════════

输入 /finance:project-switch <code> 切换项目
输入 /finance:project-new 创建新项目
════════════════════════════════════════
```

## 字段提取

每个项目的展示信息从 `project.md` 提取：

| 展示字段 | project.md 来源 |
|---------|-----------------|
| 状态 | `状态` 或 `当前阶段` |
| 类型 | `项目类型` |
| 负责人 | `负责人` |
| 周期 | `审计周期` 或 `项目周期` |
| 下次关键日期 | `下次关键日期` 或从 `关键日期` 段第一个未来日期 |
| 完成度 | `关联产出物` 数量 / `关键阈值.总数`（如 SOX 控制测试 31/72） |

## 实现机制

扫描逻辑：

```bash
PROJECTS_ROOT=~/.config/finance-skills/projects
for dir in $PROJECTS_ROOT/*/; do
  project_md=$dir/project.md
  if [ -f "$project_md" ]; then
    # 解析 project.md 提取字段
    code=$(basename "$dir")
    status=$(grep "^状态" "$project_md" | head -1)
    # ...
  fi
done
```

按状态分组排序：`fieldwork` > `active` > `reporting` > `planning` > `closed`。

## Examples

→ 示例：用户说"看看当前有哪些项目"，系统扫描 projects/ 目录并按状态分组输出。

→ 示例：用户说"列出未来 30 天内有截止的项目"，系统用 `--upcoming 30` 过滤。

→ 示例：用户说"所有 M&A 项目状态"，系统用 `--type m-and-a` 过滤。

---

## 注意事项

- **空目录扫描**：如果 `~/.config/finance-skills/projects/` 不存在或为空，输出"暂无项目"，并提示运行 `/finance:project-new` 创建
- **project.md 损坏**：用 ⚠️ 标注，跳过该项目的字段提取，仍显示 code + 目录路径
- **不修改任何文件**：纯只读 skill