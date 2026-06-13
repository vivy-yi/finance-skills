# Finance Project Workspace

财务工作不是单次任务，而是有明确周期和范围的**项目**。Legal 用 `deals/[code]/` 管理 M&A 项目，Finance 需要等价设计。

---

## 核心概念

**Project = 一个财务工作周期 + 范围 + 产出物集合**

- 年度审计是一个 Project
- Q2 预算审查是一个 Project
- 一次 M&A 尽职调查是一个 Project
- 一个税务申报周期是一个 Project

Project Workspace 让 Agent 能够：
1. **跨 Session 记住上下文**（上次审计发现哪些缺陷）
2. **关联产出物**（控制测试底稿 → 缺陷评估 → 整改计划）
3. **区分"当前项目"和"历史项目"**（不说去年审计的事当今年审计的输入）

---

## 目录结构

```
~/.config/finance-skills/
├── CLAUDE.md                    ← 公司级配置（ERP类型/阈值/团队）
├── credentials/                 ← API 密钥（不对 Agent 暴露路径）
│   ├── sap.env
│   ├── powerbi.env
│   └── concur.env
├── audit.log                    ← 操作审计日志
│
└── projects/                    ← 所有财务项目
    ├── 2026-annual-audit/       ← 年度审计
    │   ├── project.md           ← 项目上下文（核心）
    │   ├── scope.md             ← 审计范围
    │   ├── timeline.md          ← 关键时间节点
    │   ├── findings/            ← 缺陷评估输出
    │   │   ├── C-01-重大.md
    │   │   └── C-02-重要.md
    │   ├── control-testing/     ← 控制测试底稿
    │   │   ├── C-01-test.md
    │   │   └── C-02-test.md
    │   └── documents/           ← 相关文档
    │
    ├── Q2-budget-review/        ← 季度预算审查
    │   ├── project.md
    │   ├── department-budgets/
    │   ├── variance-analysis/
    │   └── management-approval/
    │
    ├── tax-filing-2026/         ← 年度税务申报
    │   ├── project.md
    │   ├── tax-computation/     ← 税额计算
    │   ├── supporting-docs/     ← 证明文件
    │   └── compliance-checklist/
    │
    └── m-and-a-deal-alpha/      ← M&A 项目（按 deal code）
        ├── project.md
        ├── financial-model/     ← DCF 模型
        ├── due-diligence/      ← 尽职调查
        │   ├── control-dd.md
        │   └── tax-dd.md
        └── integration-plan/    ← 整合计划
```

---

## project.md 结构（核心文件）

每个 Project 的 `project.md` 是项目的单一真相来源：

```markdown
# Project：2026 年度内部控制审计

## 基本信息

- **项目类型**：`annual-audit`
- **项目代码**：`2026-audit-ic`
- **负责人**：[CFO 姓名]
- **审计周期**：2026-01-01 ~ 2026-12-31
- **项目状态**：`active` | `planning` | `fieldwork` | `reporting` | `closed`

## 当前阶段

- **阶段**：`fieldwork`
- **上次活动**：2026-06-10（控制测试 C-01）
- **下次关键日期**：2026-06-30（管理层评审会）

## 范围

- **纳入范围**：总部 + 华东区域（工厂/仓库）
- **排除范围**：海外子公司（独立审计）
- **关注领域**：收入确认、采购付款、存货管理

## 相关系统

| 系统 | Connector | 数据可用性 |
|------|-----------|-----------|
| SAP S/4HANA | `sap_gl_query` | ✅ |
| Power BI | `pbi_datasets_refresh` | ✅ |
| BlackLine | `bl_account_recon` | ⚠️ 部分可用 |

## 关键阈值

- **重大缺陷门槛**：RMB 500 万
- **重要缺陷门槛**：RMB 100 万
- **SOX 覆盖控制**：72 个
- **已完成测试**：31 个

## 关联产出物

- `findings/C-01-重大.md`（已确认）
- `control-testing/C-01-test.md`（测试底稿）

## 历史上下文

- **2025 年审计发现**：重大缺陷 0 个，重要缺陷 3 个，一般缺陷 12 个
- **整改状态**：3 个重要缺陷中 2 个已整改，1 个持续到本期

## Agent 备注

（Agent 在项目执行过程中记录的临时状态）
```

---

## Workspace 操作 Skill（待实现）

### `/finance:project-list`

列出所有项目，标注状态和关键日期：

```
当前活跃项目：
1. 2026 年度内部控制审计 [fieldwork] — 下次：06-30 管理层评审
2. Q2 预算审查 [planning] — 开始：07-01
3. 税务申报 2026 [planning] — 截止：08-15

已完成：
4. 2025 年度内部控制审计 [closed]
```

### `/finance:project-switch <code>`

切换到指定项目，后续所有 Skill 操作都在该项目上下文中：

```
已切换到：2026 年度内部控制审计 [fieldwork]
所有操作将记录到 ~/.config/finance-skills/projects/2026-audit-ic/
```

### `/finance:project-new`

创建新项目并引导配置：

```
项目类型：
1. 年度审计（内控/财务）
2. 季度预算审查
3. 税务申报
4. M&A 尽职调查
5. 其他

选择类型后询问：项目代码、负责人、关键日期、范围
```

---

## 与 Legal Workspace 的关键差异

| 维度 | Legal deals/[code]/ | Finance projects/ |
|------|---------------------|------------------|
| **核心文件** | `matter.md` | `project.md` |
| **时间跨度** | M&A：几周到几个月 | 年度审计：12 个月周期 |
| **产出物类型** | 合同/备忘录/尽调报告 | 控制测试底稿/缺陷评估/整改计划 |
| **跨期关联** | 通常一次性 | 每年重复，关联历史数据 |
| **Agent 上下文** | 多 Agent 共享同一 matter | 多 Audit 周期需隔离但可追溯 |

---

## 实现优先级

**Phase 1（必须）**：
- `projects/` 目录结构
- `project.md` 格式规范
- `/finance:project-switch` skill

**Phase 2（应该）**：
- `/finance:project-list` 自动扫描
- `/finance:project-new` 创建向导
- 与 references/ 的关联（缺陷 → 项目 → 场景）

**Phase 3（可以）**：
- 与日历系统集成（关键日期提醒）
- 产出物自动归档
- 历史项目查询
