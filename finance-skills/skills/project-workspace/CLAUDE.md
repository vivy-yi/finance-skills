# Project Workspace — Finance Skills Layer 2

财务工作按"项目"组织。本目录提供 Layer 2 项目管理能力。

---

## 包含的 Skill

| Skill | 触发词 | 用途 |
|-------|--------|------|
| `/finance:project-list` | 项目列表、有哪些项目 | 列出所有项目 |
| `/finance:project-new` | 新建项目、立项、启动项目 | 创建项目 + project.md |
| `/finance:project-switch` | 切换项目、进入项目 | 激活项目上下文 |
| `/finance:project-status` | 项目详情、项目进度 | 显示单个项目完整状态 |
| `/finance:project-archive` | 归档项目、关闭项目 | 项目封存（只读） |

---

## 项目目录

```
~/.config/finance-skills/projects/
├── {code}/                ← 项目目录
│   ├── project.md         ← 项目单一真相来源
│   ├── scope.md           ← 项目范围
│   ├── timeline.md        ← 关键时间节点
│   ├── findings/          ← 缺陷产出物
│   ├── documents/         ← 证据材料
│   ├── audit-trail.log    ← 操作审计日志
│   └── _meta/             ← Agent 内部元数据
└── _archive/              ← 已归档项目（只读）
```

详见 [references/项目空间结构.md](references/项目空间结构.md)。

---

## 项目类型

| 类型 | 适用 | 默认场景 |
|------|------|---------|
| `annual-audit` | 年度审计 | internal-audit, internal-control, audit-support |
| `budget-review` | 预算审查 | budget-management, kpi-management |
| `tax-filing` | 税务申报 | tax-filing, transfer-pricing-documentation |
| `m-and-a` | 并购尽调 | m-and-a, financial-analysis, tax-filing |
| `financing` | 融资项目 | financing-structure, treasury-management |
| `internal-control` | 内控整改 | internal-control, internal-audit |
| `other` | 其他 | 自定义 |

---

## 工作流

**首次使用：**
```
1. /finance:cold-start           ← 全局配置（公司/ERP/连接器）
2. /finance:project-new          ← 创建第一个项目
3. /finance:project-switch <code> ← 激活项目上下文
4. 执行项目内的 skill
5. /finance:project-status       ← 查看进度
6. /finance:project-archive      ← 完结后归档
```

**日常使用：**
```
/finance:project-list          ← 看看现在做哪个
/finance:project-switch <code> ← 切换到目标项目
执行 skill                     ← 操作记录到项目目录
```

---

## 项目状态流转

```
planning → active → fieldwork → reporting → closed → archived
```

| 状态 | 说明 | 可执行 skill |
|------|------|------------|
| planning | 规划阶段 | 仅 project-status / project-new |
| active | 启动执行 | 全部 |
| fieldwork | 现场执行（年度审计特有） | 全部 |
| reporting | 报告阶段 | 全部但产出物标"待审" |
| closed | 已关闭 | 仅 project-status（只读） |
| archived | 已归档 | 仅 project-status（只读） |

---

## 与 Layer 1 场景的协作

切换项目后，Layer 1 的 skill 自动使用项目上下文：

```
用户：/finance:project-switch 2026-audit-ic
  → 加载 project.md
  → 设定 current_project_code = 2026-audit-ic

用户：/internal-audit:control-testing
  → 检查 current_project_code
  → 读取 project.md 关键阈值（重大缺陷门槛等）
  → 执行控制测试
  → 把产出物写入 ~/.config/finance-skills/projects/2026-audit-ic/control-testing/
  → 追加日志到 audit-trail.log
```

**未切换项目时**：skill 仍可执行，但产出物写到 `~/.config/finance-skills/scratch/{timestamp}/`（一次性临时目录）。

---

## 详见 references/

- [references/项目空间结构.md](references/项目空间结构.md) — 完整目录规范 + project.md 字段说明