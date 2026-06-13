# Finance Skills

> AI-Ready Financial Intelligence — 覆盖 CFO 全部工作域的智能体 Skill 体系

[![Agent Framework](https://img.shields.io/badge/Agent-Hermes%20%7C%20OpenClaw-6366f1)](https://github.com/vivy-yi)
[![Financial Scenes](https://img.shields.io/badge/Scenes-34-22d3ee)](./finance-skills/skills)
[![Skill Files](https://img.shields.io/badge/Skills-152-4ade80)](./finance-skills/skills)
[![MCP Connectors](https://img.shields.io/badge/Connectors-34-818cf8)](./finance-skills/CONNECTORS.md)
[![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

---

## 是什么

Finance Skills 是一套面向 AI Agent 的**财务职能 Skill 系统**。每个 Skill 对应一个财务场景中的具体任务，Agent 加载后可以自主完成从数据读取、判断到输出的完整工作流。

**解决问题**：让 AI Agent 具备财务专业能力——不是通用聊天，而是能真正执行"内控测试""KPI 根因分析""IFRS 9 信用风险评估"这类任务的财务助手。

---

## 架构总览

```
finance-skills/
├── FINANCE-SKILLS-OVERVIEW.html   ← 可视化图谱（浏览器直接打开）
├── finance-skills/
│   ├── ARCHITECTURE.md            ← 工程架构说明
│   ├── CLAUDE.md                  ← 全局配置模板
│   ├── CONNECTORS.md              ← 9 个 Connector 定义（SAP/Power BI/BlackLine/Bloomberg...）
│   ├── PROJECT_WORKSPACE.md       ← 项目空间规范
│   ├── cold-start/                ← 首次配置向导
│   └── skills/                    ← 34 个财务场景
│       ├── internal-control/
│       ├── kpi-management/
│       └── ...
└── diagram/
    ├── FINANCE-SKILLS-OVERVIEW.html
    └── 财务职能体系全览.html           ← 早期设计稿（参考保留）
```

**三层架构**：

| Layer | 内容 | 状态 |
|-------|------|------|
| Layer 0 — Hub | 全局配置、冷启动、Connector 注册 | ✅ |
| Layer 1 — 场景 | 34 个场景 × (references/ + skills/ + CLAUDE.md) | ✅ |
| Layer 2 — 项目 | 项目空间（跨 Session 记住上下文） | ✅ 规范已定义 |

---

## 核心概念

### Skill 类型

每个场景下有两种 Skill：

| 类型 | 定位 | 数量/场景 |
|------|------|-----------|
| **Master Skill** | 场景主技能，识别用户意图并分发给 Atomic | 1 个/场景（30 个） |
| **Atomic Skill** | 原子技能，执行具体财务任务 | 3~6 个/场景（122 个） |

### 场景知识后端

每个场景目录下包含三个知识文件，供 Skill 运行时读取：

- **判断框架.md** — 财务判断规则（YAML/表格），如内控缺陷分级标准、KPI 选择逻辑
- **数据源清单.md** — 场景所需数据 → Connector → 系统/表/字段 映射
- **查询路径.md** — 无 Connector 时的手动 SOP，引导用户完成数据收集

### Connector 生态

9 个 Connector，覆盖 5 层架构：

```
L1 ERP      SAP S/4HANA, Oracle EBS/Fusion, 用友 NC/U8, 金蝶 K3
L2 BI       Power BI, Tableau, FineReport（帆软）
L3 执行     BlackLine, SAP Concur, Expensify, Kyriba, GTreasury, Bloomberg TSOX, Refinitiv Eikon, Capital IQ, Wind, AuditBoard
L4 合规     SharePoint, Google Drive, Workday Adaptive, Anaplan, Tagetik, CCH Tagetik, Workiva
L5 HR/税务  Workday HCM, BambooHR, ADP, TaxDome, Vertex/Sovos
L5 ESG/IR   Sustainalytics, MSCI ESG, Bloomberg ESG, Diligent, Q4
```

---

## 场景全景（34 个）

### 战略级（A 级）— 17 个

| 场景 | 简介 | Atomic Skills |
|------|------|--------------|
| [internal-control](./finance-skills/skills/internal-control/) | 内部控制与 SOX 合规 | 控制测试/缺陷评估/审批矩阵/内控设计 |
| [kpi-management](./finance-skills/skills/kpi-management/) | KPI 选择·追踪·根因分析 | 指标设定/追踪/预警处理/根因分析 |
| [board-reporting](./finance-skills/skills/board-reporting/) | 董事会材料准备与分发 | 董事会材料/会议管理/审计委员会支持 |
| [management-report](./finance-skills/skills/management-report/) | 管理报告生成与发布 | 财务报告生成/管理层评论写作/指标预警 |
| [business-insight](./finance-skills/skills/business-insight/) | 业务洞察生成与验证 | 洞察生成/验证/趋势分析/调查分析 |
| [strategic-planning](./finance-skills/skills/strategic-planning/) | 战略规划与执行追踪 | 战略目标设定/假设评估/风险评估/执行追踪 |
| [financing-structure](./finance-skills/skills/financing-structure/) | 融资结构设计与成本计算 | 融资成本计算/银行关系/契约监控/债务重组 |
| [m-and-a](./finance-skills/skills/m-and-a/) | 收购与并购全流程 | 财务尽调/DCF 建模/可比分析/整合路线图 |
| [fx-risk](./finance-skills/skills/fx-risk/) | 外汇风险识别与对冲 | 敞口计算/预测分析/对冲策略/交易执行 |
| [esg-reporting](./finance-skills/skills/esg-reporting/) | ESG 数据整合与披露 | 数据整合/实质性评估/评级追踪/报告生成 |
| [investor-relations](./finance-skills/skills/investor-relations/) | 投资者关系管理 | 路演材料/业绩电话准备/信息披露/反馈追踪 |
| [treasury-management](./finance-skills/skills/treasury-management/) | 司库管理与资金预测 | 日间头寸/资金预测/付款授权审批 |
| [capital-allocation](./finance-skills/skills/capital-allocation/) | 资本配置与 ROIC 分析 | 投资评估/ROIC vs WACC 比较/情景分析/WACC 计算 |
| [transfer-pricing-documentation](./finance-skills/skills/transfer-pricing-documentation/) | 转让定价文档与 BEPS 合规 | 主文档/本地文档/CbCR/APA 管理 |
| [internal-audit](./finance-skills/skills/internal-audit/) | 内部审计管理全流程 | 年度审计计划/合规性审计/舞弊调查/整改跟踪 |
| [project-valuation](./finance-skills/skills/project-valuation/) | 项目估值与投资决策 | NPV-IRR 计算/实物期权分析/可比参照/投资决策报告 |
| [ifrs9-credit-risk](./finance-skills/skills/ifrs9-credit-risk/) | IFRS 9 信用风险敞口评估 | 三阶段分类/ECL 计量/宏观前瞻调整/监管披露 |

### 运营级（B 级）— 17 个

| 场景 | 简介 | Atomic Skills |
|------|------|--------------|
| [accounts-payable](./finance-skills/skills/accounts-payable/) | 应付账款与付款调度 | 三单匹配自动化/付款调度/供应商付款审查 |
| [accounts-receivable](./finance-skills/skills/accounts-receivable/) | 应收账款与催收 | 账龄分析/信用评估/催收自动化 |
| [audit-support](./finance-skills/skills/audit-support/) | 审计配合与证据收集 | 审计调整审查/证据收集/函证管理 |
| [budget-management](./finance-skills/skills/budget-management/) | 预算编制与执行监控 | 年度预算编制/预算调整审查/执行监控/差异分析 |
| [cash-management](./finance-skills/skills/cash-management/) | 现金流管理与预测 | 头寸监控/预测/付款调度 |
| [compliance-reporting](./finance-skills/skills/compliance-reporting/) | 合规报告与监管披露 | 税务申报/监管报告/披露管理 |
| [cost-control](./finance-skills/skills/cost-control/) | 成本控制与差异分析 | 成本中心绩效/费用比率分析/标准成本差异 |
| [expense-review](./finance-skills/skills/expense-review/) | 费用报销审查 | 发票验证/三单匹配/政策合规检查/争议识别 |
| [financial-analysis](./finance-skills/skills/financial-analysis/) | 财务分析与报告 | 预算执行分析/盈利分析/KPI 仪表盘 |
| [fixed-assets](./finance-skills/skills/fixed-assets/) | 固定资产管理 | 资产购置审查/资产处置审查/折旧分析 |
| [intercompany-accounting](./finance-skills/skills/intercompany-accounting/) | 关联方交易与转让定价 | 公司间对账/转让定价审查/担保审查 |
| [investment-management](./finance-skills/skills/investment-management/) | 投资组合管理 | 组合审查/流动性评估/融资成本分析 |
| [month-end-close](./finance-skills/skills/month-end-close/) | 月结自动化 | 月结检查清单执行/验证/跨期调整/对账自动化 |
| [payroll-accounting](./finance-skills/skills/payroll-accounting/) | 薪酬会计与社保 | 薪酬计算/社保审查/代扣代缴审查 |
| [tax-filing](./finance-skills/skills/tax-filing/) | 税务申报（企税/增值税/个税） | 企税申报/增值税申报/个税申报/税务风险评估 |
| [treasury-advanced](./finance-skills/skills/treasury-advanced/) | 高级司库（银行关系/流动性） | 银行关系评估/现金池配置/投资合规检查/LCR 评估 |
| [working-capital](./finance-skills/skills/working-capital/) | 营运资本优化 | 现金转换周期/库存优化/应付账款策略/供应链金融 |

> 注：部分运营场景（budget-management、expense-review、month-end-close 等）为纯 Atomic 编排，无 Master Skill。

---

## 快速开始

### 1. 安装 Skill

```bash
# 方式一：软链接到 Hermes
ln -s /path/to/finance-skills/finance-skills ~/.hermes/skills/finance

# 方式二：在 SOUL.md 中配置引用路径
```

### 2. 首次配置（冷启动）

```
/hermes
> /finance:cold-start
```

或直接触发关键词：`开始配置财务技能`、`初始化 finance`、`cold start`

冷启动流程：
1. **连接器检测** — 验证 SAP / Power BI / BlackLine 等系统可达性
2. **公司配置** — 收集 ERP 类型 / 审计周期 / 财务职能结构
3. **场景选择** — 选择相关场景（可多选）
4. **阈值设置** — 配置内控缺陷分级标准、KPI 基准值等
5. **持久化** — 写入 `~/.config/finance-skills/CLAUDE.md`

### 3. 使用场景 Skill

```
Hermes/Agent: 加载场景 Skill
    ↓
Master Skill: 识别用户意图
    ↓
Atomic Skill: 执行具体任务
    ↓
references/: 读取判断框架 + 数据源映射
    ↓
Connector: 调用外部系统
    ↓
输出结果（报告/判断/建议）
```

---

## Skill 文件结构

```
skills/[场景]/
├── CLAUDE.md                 ← 用户配置（公司名称/阈值/联系人）
├── references/
│   ├── 判断框架.md            ← 财务判断规则（YAML/表格）
│   ├── 数据源清单.md          ← 数据 → Connector → 字段 映射
│   └── 查询路径.md            ← SOP（无 Connector 时的手动流程）
└── skills/
    ├── [scene]-master/       ← 场景主技能
    │   └── SKILL.md
    └── [atomic-skill]/       ← 原子技能
        └── SKILL.md
```

每个 SKILL.md 包含：

```yaml
---
name: [skill-name]
description: [能力描述]
argument-hint: "[参数格式]"
risk_level: [low|medium|high]
version: "1.0.0"
---

## Examples
> 用户说"...", 调用本技能

## 加载上下文
首次使用时读取 `../../CLAUDE.md` 获取场景级配置

## 第一步 / 第二步 / ...
[可执行步骤：判断 → 工具调用 → 输出]
```

---

## 与 Legal Skill 体系的关系

Finance Skills 与 [Greater China Legal](https://github.com/vivy-yi/Greater-China-Legal)（大中华区法律 Agent Skill 体系）同源，遵循相同的工程规范：

| 维度 | Greater China Legal | Finance Skills |
|------|---------------------|----------------|
| 场景数 | 12 个法律域 | 34 个财务场景 |
| 架构 | Layer 0 Hub + Layer 1 域 + Layer 2 项目 | Layer 0 Hub + Layer 1 场景 + Layer 2 项目 |
| 知识后端 | 判断框架 + 数据源清单 + 查询路径 | 判断框架 + 数据源清单 + 查询路径 |
| Connector | Westlaw / 企查查 / MCP Server | SAP / Power BI / BlackLine / Bloomberg |
| 定位 | 律师业务流（审查/谈判/诉讼） | CFO 工作流（控制/分析/决策/披露） |

两者可同时加载于同一 Agent，会话中按意图自动路由。

---

## 文件统计

| 指标 | 数量 |
|------|------|
| 场景总数 | 34 |
| 战略级（A 级） | 17 |
| 运营级（B 级） | 17 |
| Skill 文件（SKILL.md） | 152 |
| Master Skill | 30 |
| Atomic Skill | 122 |
| references 文件 | 102 |
| 场景级配置文件（CLAUDE.md） | 34 |
| Connector 类型 | 34（覆盖 L1~L5） |

**质量状态**：所有 SKILL.md 文件 frontmatter ✅ + Examples ✅ 100%

---

## 技术栈

- **Agent 框架**：Hermes Agent / OpenClaw
- **Skill 格式**：Markdown（SKILL.md + YAML frontmatter）
- **知识后端**：Markdown 表格/YAML（判断框架、数据源清单、查询路径）
- **系统集成**：MCP（Model Context Protocol）Connector
- **可视化**：HTML5 + CSS3（FINANCE-SKILLS-OVERVIEW.html）

---

## 目录深度

```
finance-skills/finance-skills/skills/[scene]/skills/[skill]/SKILL.md
         1           2       3        4         5         6
```

共 6 层。相对路径 `../../CLAUDE.md` 从 Skill 文件指向场景根目录（路径深度不变）。

---

## License

MIT License — 可自由用于个人和商业项目。

---

## 作者

**vivy-yi** · GitHub: [@vivy-yi](https://github.com/vivyyi)
