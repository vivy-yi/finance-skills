---
name: project-switch
description: >-
  项目切换 — 加载指定项目的 project.md 上下文到当前会话。后续所有 skill 操作
  都在该项目上下文中执行（产出物写到 projects/{code}/，引用项目阈值）。
  适用情形：开始/恢复一个财务项目（年度审计、Q2 预算审查、税务申报周期、M&A 尽调）时执行。
  触发词：切换项目、进入项目、恢复项目、加载项目上下文、switch to project。
  核心：单例项目上下文（同时只能激活一个项目），所有 skill 引用 ~/.config/finance-skills/projects/{code}/project.md。
argument-hint: "[<project-code>] [--show]"
risk_level: low
last_reviewed: 2026-06-14
version: 1.0.0
---

## 加载上下文

**首次执行：** 读取 `../references/项目空间结构.md` 了解 project.md 字段规范。

**本 skill 本身不读项目内容**，只设置 `current_project_code` 上下文变量。后续 skill 通过此变量定位项目目录。

---

# /finance:project-switch — 切换项目上下文

把当前会话的"项目上下文"切到指定项目。所有后续 skill 操作都基于该项目的 `project.md` 中的阈值/范围/历史上下文。

## 命令格式

```
/finance:project-switch <project-code> [--show]
```

参数：
- `<project-code>`：项目代码（如 `2026-audit-ic` / `Q2-2026-budget` / `tax-filing-2026` / `m-and-a-deal-alpha`）
- `--show`：只显示当前激活项目，不切换

## 操作步骤

### 步骤 1：定位项目目录

```
项目根目录 = ~/.config/finance-skills/projects/{project-code}/
```

如果目录不存在：

```
❌ 项目不存在: {project-code}

请使用 /finance:project-list 查看现有项目
或 /finance:project-new 创建新项目
```

### 步骤 2：校验 project.md

读取 `{project-root}/project.md`，校验：
- 必填字段齐全（项目类型/代码/负责人/周期/状态）
- YAML frontmatter 解析正确
- `状态` 字段是合法值（`planning` / `active` / `fieldwork` / `reporting` / `closed`）

如果 project.md 损坏或缺字段：

```
⚠️ project.md 损坏或缺必填字段

请运行 /finance:project-repair {project-code} 自动修复
或手动编辑 ~/.config/finance-skills/projects/{project-code}/project.md
```

### 步骤 3：检查项目状态

读取 `状态` 字段：

| 状态 | 是否允许切换 | 警告 |
|------|-------------|------|
| `planning` | ✅ | "项目仍在规划阶段，未开始执行" |
| `active` | ✅ | 无 |
| `fieldwork` | ✅ | 无 |
| `reporting` | ✅ | "项目在报告阶段，新发现可能不影响最终结论" |
| `closed` | ⚠️ | "项目已关闭，切换为只读模式" |
| `archived` | ❌ | "项目已归档，不可切换" |

`closed` 状态允许切换但提示只读。

### 步骤 4：写入会话上下文

将以下信息注入会话上下文：

```
current_project = {
    code: "{project-code}",
    type: "{project-type}",
    root: "~/.config/finance-skills/projects/{project-code}/",
    status: "{状态}",
    started: "{开始日期}",
    next_milestone: "{下次关键日期}",
}
```

**关键约束**：同时只能激活一个项目。如果已激活另一个项目：

```
⚠️ 当前已激活项目: {old-code}

切换到 {new-code} 将丢弃 {old-code} 的会话状态（包括未保存的临时笔记）
确认切换吗？[y/N]
```

### 步骤 5：输出切换结果

成功切换时输出：

```
════════════════════════════════════════
✅ 已切换到项目: {project-code}

项目类型: {type}
负责人: {name}
周期: {period}
当前阶段: {stage}
上次活动: {last-activity}
下次关键日期: {next-milestone}
════════════════════════════════════════

项目根目录: ~/.config/finance-skills/projects/{project-code}/
所有 skill 操作的产出物将记录到此项目。

输入 /finance:project-status 查看项目详情
输入 /finance:project-list 切换到其他项目
════════════════════════════════════════
```

---

## Examples

→ 示例：用户说"切换到 2026 年度内部控制审计项目"，系统应切换到 `2026-audit-ic`，加载该项目的 project.md，输出项目摘要。

→ 示例：用户说"我要开始做 Q2 预算审查"，系统应先检查 `Q2-2026-budget` 是否存在，存在则切换，不存在则提示用 `/finance:project-new` 创建。

→ 示例：用户说"现在做的是哪个项目"，系统应使用 `--show` 模式，只输出当前激活项目信息。

---

## 与其他 skill 的协作

切换项目后，以下 skill 会自动使用项目上下文：

| Skill | 项目上下文的用途 |
|-------|------------------|
| `/internal-audit:control-testing` | 把控制测试底稿写入 `projects/{code}/control-testing/` |
| `/month-end-close:*` | 把月度关账报告写入 `projects/{code}/close-{YYYY-MM}/` |
| `/m-and-a:*` | 把尽调材料写入 `projects/{code}/due-diligence/` |
| `/board-reporting:*` | 把董事会材料写入 `projects/{code}/board-{YYYY-Q}/` |

**未切换项目时调用**：上述 skill 仍可执行（不强制依赖项目），但会提示"未指定项目上下文，产出物将写入默认目录 `~/.config/finance-skills/scratch/`"。

---

## 关闭项目

要关闭当前项目，使用 `/finance:project-archive {project-code}` 或修改 `project.md` 的 `状态` 字段。

切换到 `closed` 状态后：
- 项目目录变为只读
- 不再出现在 `/finance:project-list` 的"活跃"列表
- 可通过 `/finance:project-switch {code}` 重新打开（会自动恢复 `closed` 状态）

---

## 注意事项

- **无项目 ≠ 不能用 skill**。基础 skill（如 `/tax-filing:vat-monthly-declare`）可不依赖项目上下文运行
- **切换不影响数据**：所有项目文件独立保存，切换只是"激活焦点"
- **多任务并发**：项目是单例的。如果同时跟踪多个项目（如年度审计 + Q2 预算），在两个会话窗口分别切换，不要在同一会话混用
- **凭证不在项目目录**：API 凭证统一在 `~/.config/finance-skills/credentials/`，不在项目目录内（避免泄露）