---
name: project-archive
description: >-
  项目归档 — 把项目状态改为 archived，目录变为只读，标记完成日期。
  适用情形：项目完结（年度审计出具报告、税务申报周期结束、M&A 交易完成）后保留历史记录。
  触发词：归档项目、关闭项目、项目完结、项目封存。
  核心：状态流转 closed → archived，目录权限改为只读，保留所有产出物供历史查询。
argument-hint: "<project-code> [--force]"
risk_level: medium
last_reviewed: 2026-06-14
version: 1.0.0
---

# /finance:project-archive — 项目归档

把已关闭的项目标记为归档状态，目录只读。

## 命令格式

```
/finance:project-archive <project-code> [--force]
```

参数：
- `<project-code>`：项目代码
- `--force`：跳过状态检查（强制归档 `active` 项目）

## 状态流转

```
planning → active → fieldwork → reporting → closed → archived
                                                  ↑
                                              此处开始只读
```

**只能在 `closed` 状态下归档**（除非 `--force`）。

## 操作步骤

### 步骤 1：校验状态

读取 `project.md` 的 `状态` 字段：

| 当前状态 | 是否可归档 | 处理 |
|---------|----------|------|
| `closed` | ✅ | 直接归档 |
| `reporting` | ⚠️ | 提示"项目仍在报告阶段，确认归档吗？" |
| `active` / `fieldwork` / `planning` | ❌ | 拒绝，要求先 close（修改状态为 closed） |
| `archived` | ✅ | 幂等操作，输出"项目已是归档状态" |

### 步骤 2：校验完整性

检查项目目录是否完整：
- `project.md` 存在
- 关键产出物存在（按类型）：
  - annual-audit：`findings/` 至少 1 个
  - m-and-a：`due-diligence/` 至少 1 个
  - budget-review：`variance-analysis/` 至少 1 个
  - 其他：跳过

不完整时输出警告但不阻止归档。

### 步骤 3：写入归档信息

修改 `project.md`：
- `状态`: `closed` → `archived`
- 添加 `归档时间`: `{YYYY-MM-DD HH:MM}`
- 添加 `归档人`: `{current-user}`

可选：把目录移至 `~/.config/finance-skills/projects/_archive/{code}-{YYYY}/`（推荐）

### 步骤 4：标记只读

```
chmod -R 555 ~/.config/finance-skills/projects/{code}/
```

仅 `~/.config/finance-skills/projects/{code}/project.md` 保持可写（允许 reopen）。

### 步骤 5：输出归档结果

```
════════════════════════════════════════
📦 项目已归档

代码: {code}
名称: {name}
原始周期: {start} ~ {end}
关闭时间: {closed_date}
归档时间: {archive_date}
归档人: {user}

项目目录: ~/.config/finance-skills/projects/_archive/{code}-{YYYY}/
权限: 只读

历史保留 5 年（{archive_date} + 5 年后自动清理）
════════════════════════════════════════

恢复项目：/finance:project-switch {code}（会自动 reopen 到 closed 状态）
════════════════════════════════════════
```

---

## 历史保留策略

```
归档后保留时间：5 年
├── 0-1 年：完整保留，可随时 reopen
├── 1-3 年：压缩归档（tar.gz），reopen 需手动解压缩
└── 3-5 年：标记为"待清理"，到期自动提示用户
> 5 年：自动清理（除非用户标记"永久保留"）
```

永久保留：在 project.md 添加 `永久保留: true` 字段。

---

## Examples

→ 示例：用户说"归档 2025 年度审计项目"，系统校验状态 closed（如果未 closed 则要求先 close），执行归档。

→ 示例：用户说"强制归档 M&A alpha 项目"，系统用 `--force` 跳过状态检查。

---

## 注意事项

- **归档不可逆（除非 reopen）**：归档后目录只读，修改产出物会被权限拒绝
- **凭证已清除**：归档前自动检查 `~/.config/finance-skills/credentials/` 是否引用该项目 ID，如有则提示清理
- **跨年度审计关联**：归档 2025-audit 时，询问"是否将本期发现自动同步到 2026-audit 的'历史上下文'段？"（年度审计连续性需求）