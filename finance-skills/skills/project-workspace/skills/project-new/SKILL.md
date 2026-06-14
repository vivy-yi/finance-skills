---
name: project-new
description: >-
  新建项目 — 创建项目目录 + project.md 模板，引导填写项目信息。
  适用情形：开始一个新的财务周期项目（年度审计启动、Q2 预算审查立项、税务申报周期开启）。
  触发词：新建项目、创建项目、立项、新财年审计、Q2 预算立项、税务申报周期。
  核心：项目类型选择 → 代码生成 → project.md 模板填充 → 关联场景激活。
argument-hint: "[--type <类型>] [--code <代码>] [--name <名称>] [--owner <负责人>]"
risk_level: medium
last_reviewed: 2026-06-14
version: 1.0.0
---

## 加载上下文

读取 `../references/项目空间结构.md` 了解目录规范和 project.md 模板。

---

# /finance:project-new — 新建项目

创建 `~/.config/finance-skills/projects/{code}/` 目录和 project.md 文件。

## 命令格式

```
/finance:project-new [--type <类型>] [--code <代码>]
```

可选参数跳过交互直接创建。

## 项目类型

| 类型 | 用途 | 默认代码格式 |
|------|------|------------|
| `annual-audit` | 年度审计（内控/财务） | `{YYYY}-audit-ic` |
| `budget-review` | 季度/年度预算审查 | `{Q}{YYYY}-budget` |
| `tax-filing` | 税务申报周期 | `tax-filing-{YYYY}` |
| `m-and-a` | M&A 尽调/估值/整合 | `m-and-a-{deal-code}` |
| `financing` | 融资项目（银团/债券/股权） | `financing-{YYYY-MM}` |
| `internal-control` | 内控设计/整改 | `ic-{scope}-{YYYY}` |
| `other` | 其他（自定义） | `{name}-{YYYY-Q}` |

## 交互流程

### 步骤 1：选择项目类型

```
选择项目类型：
1. annual-audit   - 年度审计（内控/财务）
2. budget-review  - 季度/年度预算审查
3. tax-filing     - 税务申报周期
4. m-and-a        - M&A 尽调/估值/整合
5. financing      - 融资项目
6. internal-control - 内控设计/整改
7. other          - 其他（自定义）
```

### 步骤 2：输入项目代码

```
请输入项目代码（或回车使用默认）：
默认: {自动按类型生成}

代码必须：
- 全小写字母/数字/-
- 不含空格和特殊字符
- 1-32 字符
- 同一类型内唯一

示例：2026-audit-ic / Q3-2026-budget / m-and-a-deal-alpha
```

**冲突检查**：如果代码已存在，报错并要求重新输入。

### 步骤 3：填写项目基础信息

按 [references/项目空间结构.md](../references/项目空间结构.md) 的 project.md 模板，依次询问：

```
Q1: 项目名称（用于显示）？
    > 2026 年度内部控制审计

Q2: 项目负责人？
    > CFO 张三

Q3: 项目周期？
    起始日期 (YYYY-MM-DD): 2026-01-01
    结束日期 (YYYY-MM-DD): 2026-12-31

Q4: 初始阶段？
    1. planning   - 规划
    2. active     - 启动
    3. fieldwork  - 现场执行
    默认: planning

Q5: 项目范围描述（可空）？
    > 总部 + 华东区域（工厂/仓库）

Q6: 排除范围（可空）？
    > 海外子公司（独立审计）
```

### 步骤 4：选择激活场景

```
选择该项目涉及的财务场景（可多选）：

☑ annual-audit      - 年度审计
☐ budget-review     - 预算审查
☐ tax-filing        - 税务申报
☐ internal-audit    - 内部审计
☐ internal-control  - 内部控制
☐ m-and-a           - 并购
☐ fx-risk           - 外汇
☐ treasury-management - 资金
☐ board-reporting   - 董事会汇报
☐ ... 其他场景

默认根据项目类型自动勾选（如 annual-audit 自动勾选 internal-audit + internal-control）
```

场景选择会写入 project.md 的 `关联场景` 字段，影响后续 skill 自动激活哪些。

### 步骤 5：设置关键阈值

按项目类型显示必填阈值：

**annual-audit 类型必填**：
```
重大缺陷门槛：[默认 500 万元]
重要缺陷门槛：[默认 100 万元]
SOX 控制总数：[可空]
```

**budget-review 类型必填**：
```
预算偏差预警阈值：[默认 ±5%]
超支审批层级：[默认 财务总监]
```

**m-and-a 类型必填**：
```
交易规模：[必填，万元]
目标公司：[必填]
```

**其他类型**：可跳过此步。

### 步骤 6：创建目录 + 文件

```
项目根目录: ~/.config/finance-skills/projects/{code}/

创建以下结构：
{code}/
├── project.md                  ← 写入用户填写的信息
├── scope.md                    ← 空模板（用户后续填）
├── timeline.md                 ← 空模板
├── findings/                   ← 空目录
├── control-testing/            ← 空目录（仅 annual-audit/internal-audit）
├── documents/                  ← 空目录
└── audit-trail.log             ← 空文件，记录所有 skill 操作
```

### 步骤 7：输出创建结果

```
════════════════════════════════════════
✅ 项目创建成功！

代码: {code}
类型: {type}
名称: {name}
负责人: {owner}
周期: {start} ~ {end}
当前阶段: {status}
关联场景: {N} 个

项目目录: ~/.config/finance-skills/projects/{code}/
════════════════════════════════════════

下一步：
  输入 /finance:project-switch {code} 切换到该项目
  输入 /finance:project-status {code} 查看详情
  输入 /finance:project-list 看所有项目
════════════════════════════════════════
```

---

## 实现机制

### project.md 模板（写入项目根目录）

参考 [references/项目空间结构.md](../references/项目空间结构.md) 的完整模板。

最小必填结构：

```markdown
---
code: {code}
type: {type}
created: {YYYY-MM-DD}
status: {status}
owner: {owner}
---

# Project: {name}

## 基本信息
- **项目类型**: {type}
- **项目代码**: {code}
- **负责人**: {owner}
- **项目周期**: {start} ~ {end}
- **当前阶段**: {status}

## 关联场景
{勾选场景列表}

## 关键阈值
{按类型填充}

## 关联产出物
（暂无）

## 历史上下文
（首次创建，无）

## Agent 备注
（Agent 在项目执行过程中记录的临时状态）
```

---

## Examples

→ 示例：用户说"启动 2026 年度内控审计"，系统应选择 annual-audit 类型，代码默认 `2026-audit-ic`，询问负责人/周期/范围，生成 project.md。

→ 示例：用户说"我们有个 M&A 项目代号 alpha，开始尽调"，系统应选择 m-and-a 类型，代码 `m-and-a-deal-alpha`，询问交易规模和目标公司。

→ 示例：用户说"用命令行直接创建：/finance:project-new --type budget-review --code Q3-2026-budget --name 'Q3 2026 预算审查' --owner '财务经理王五'"，跳过交互直接创建。

---

## 注意事项

- **覆盖保护**：如果代码已存在，**拒绝覆盖**，要求用户用 `--force` 或换代码
- **凭证隔离**：项目目录**不存放** API 凭证（统一在 `~/.config/finance-skills/credentials/`）
- **跨平台路径**：使用 `~/.config/` 跨平台路径，不要 hardcode `/Users/xxx`
- **删除项目**：不提供删除入口（防止误删历史项目）。如需"删除"，建议用 `project-archive` 归档