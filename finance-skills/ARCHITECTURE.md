# Finance Skills — 工程架构

*对照 Legal（claude-for-legal）设计，补充 Finance 缺失的工程层。*

---

## 三层架构对比

```
┌─────────────────────────────────────────────────────────────┐
│                    LEGAL (claude-for-legal)                  │
├─────────────────────────────────────────────────────────────┤
│  Layer 0: legal-builder-hub                                  │
│           ├── cold-start-interview                           │
│           ├── skill-installer                               │
│           └── .mcp.json  (Connector 注册表)                   │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: corporate-legal 等 12 个域                         │
│           ├── CLAUDE.md  (用户配置)                         │
│           ├── skills/  (领域 skill)                         │
│           ├── agents/  (专项 agent)                         │
│           └── .mcp.json  (域级 connector)                   │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: deals/[code]/  (项目空间)                         │
│           ├── matter.md  (项目上下文)                       │
│           └── documents/                                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                  FINANCE (finance-skills) — 当前状态          │
├─────────────────────────────────────────────────────────────┤
│  Layer 0: [缺失]                                            │
│           cold-start ❌  skill-installer ❌  .mcp.json ❌     │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: skills/  (29 个场景)                              │
│           ├── references/  (知识文档) ← 知识后端 ✅          │
│           ├── skills/  (66 个 skill) ✅                    │
│           └── CLAUDE.md  (缺失 — 用户配置) ❌               │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: [缺失]                                            │
│           projects/ ❌  project.md ❌                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                  FINANCE — 补全目标状态                      │
├─────────────────────────────────────────────────────────────┤
│  Layer 0: finance-builder-hub/                              │
│           ├── cold-start ✅ (已写 skills/cold-start/)       │
│           ├── skill-installer (待实现)                      │
│           └── .mcp.json ✅ (已写 CONNECTORS.md)            │
├─────────────────────────────────────────────────────────────┤
│  Layer 1: skills/                                             │
│           ├── CLAUDE.md ✅ (用户配置模板)                   │
│           ├── references/                                   │
│           │   ├── 判断框架.md  ✅ 知识沉淀                  │
│           │   ├── 数据源清单.md ✅ 含 connector 映射       │
│           │   └── 查询路径.md  ✅ SOP                      │
│           └── skills/                                       │
│               ├── scene-master/  ✅ 编排层                  │
│               └── atomic/  ✅ 执行层                        │
├─────────────────────────────────────────────────────────────┤
│  Layer 2: projects/                                         │
│           ├── 2026-annual-audit/ ✅ (PROJECT_WORKSPACE.md)  │
│           └── *.md  (项目上下文) ✅                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 已完成文件

| 文件 | 作用 | 状态 |
|------|------|------|
| `CONNECTORS.md` | 全局 Connector 规范（SAP/Power BI/BlackLine/Bloomberg 等） | ✅ |
| `PROJECT_WORKSPACE.md` | 项目空间规范（目录结构 + project.md 格式） | ✅ |
| `skills/cold-start/SKILL.md` | 首次配置向导（Part 0-4：连接器检测 + 公司配置 + 场景选择 + 阈值设置） | ✅ |
| `CLAUDE.md` | 用户配置模板（含 PLACEHOLDER 提示） | ✅ |

---

## 待实现工程组件

### 高优先级

| 组件 | 说明 | 依赖 |
|------|------|------|
| `.mcp.json` | MCP Server 配置声明（对应 Legal 的 connector 注册） | 工程实现 |
| `skill-installer` | 从 registry 安装 skill 包（参考 Legal 的 `skill-installer`） | Layer 0 |
| 各场景 `references/数据源清单.md` 的 connector 映射表 | 当前只有占位符，需填入真实 connector → 字段映射 | CONNECTORS.md |

### 中优先级

| 组件 | 说明 |
|------|------|
| `projects/` 目录创建 + `project.md` 模板 | 工程实现 |
| `/finance:project-list` skill | 项目列表 |
| `/finance:project-switch <code>` skill | 切换项目上下文 |
| `/finance:project-new` skill | 创建新项目 |

### 低优先级（长期）

| 组件 | 说明 |
|------|------|
| SAP/Oracle/Power BI/BlackLine MCP Server 实现 | 实际的连接器工程 |
| 各连接器的 fallback 机制实现 | 当 Connector 不可用时的降级逻辑 |
| 与日历系统集成 | 关键日期提醒 |

---

## 与 Legal 的设计差异（由领域特性决定）

| 维度 | Legal | Finance | 差异原因 |
|------|-------|---------|---------|
| **Connector 类型** | VDR/日历/Slack | ERP/BI/司库系统 | 法律是文档协作，财务是数字执行 |
| **项目周期** | M&A deal（几周～几年） | 年度审计（12个月固定周期） | 财务有法规强制的固定周期 |
| **跨期关联** | 通常一次性 | 每年重复，需关联历史 | 财务审计连续性 |
| **阈值数量** | 少（格式偏好） | 多（金额/比率/天数） | 财务判断依赖量化阈值 |
| **Offline 模式** | 读本地文档即可 | 必须有手动输入 fallback | 财务数据在系统里，不在文档里 |

---

## 配置路径设计（与 Legal 一致）

```
~/.config/finance-skills/              ← Finance Skills 用户配置根目录
├── CLAUDE.md                          ← 公司级配置（ERP/阈值/团队）
├── credentials/                       ← API 密钥（不对 Agent 暴露）
│   ├── sap.env
│   ├── powerbi.env
│   └── blackline.env
├── audit.log                          ← 操作审计
├── .mcp.json                          ← 全局 Connector 声明
└── projects/                          ← 项目空间
    ├── 2026-annual-audit/
    │   └── project.md
    └── m-and-a-deal-alpha/
        └── project.md
```

与 Legal 的路径设计原则一致：
- 配置与代码分离（`~/.config/` vs plugin code）
- 版本独立（更新 plugin 不覆盖用户配置）
- 凭证不进入 plugin 代码
