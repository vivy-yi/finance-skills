---
name: cold-start
description: >
  Finance Skills 首次配置向导。检测连接器状态、收集公司配置、
  选择相关场景、设置关键阈值。首次使用 Finance Skills 时必须运行此向导。
  触发词："开始配置"、"初始化财务技能"、"财务助手设置"、
  "cold start"、"setup finance"
argument-hint: "[--check-connections] [--redo]"
---

# /finance:cold-start

## 流程概览

```
Part 0：连接器检测
Part 1：公司配置
Part 2：场景选择
Part 3：关键阈值设置
Part 4：写入配置
```

---

## Part 0：连接器检测

**目标：确认哪些 Connector 能够实际工作（不只是配置声明）。**

尝试调用每个候选 Connector 的轻量 API：
- SAP → 读取公司名称 `GET /sap/bc/rest/company`
- Power BI → 读取工作区列表 `GET /v1.0/myorg/groups`
- BlackLine → 读取账户列表 `GET /api/v2023.1/accounts`
- Concur → 读取用户档案 `GET /api/v4/user`

对每个 Connector：
- ✅ 成功响应 → 标记 `Operational`
- ⚠️ 配置存在但调用失败 → 标记 `Configured-unreachable` + 一行修复说明
- ❌ 未配置 → 标记 `Not configured`

输出连接器状态表：

```
| Connector | 系统 | 状态 | 说明 |
|-----------|------|------|------|
| sap_* | SAP S/4HANA | ✅ Operational | 公司代码: [CODE] |
| pbi_* | Power BI | ⚠️ Configured-unreachable | 检查 API 权限 |
| bl_* | BlackLine | ❌ Not configured | 运行 /finance:connector-setup bl |
```

---

## Part 1：公司配置

**目标：收集公司级财务信息，写入 `~/.config/finance-skills/CLAUDE.md`。**

依次询问：

### Q1：ERP 系统
```
你们公司用哪个 ERP 系统？
1. SAP S/4HANA
2. Oracle EBS / Fusion
3. 用友 NC / U8 / Cloud
4. 金蝶 K3 / Cloud
5. 其他（请说明）
```

### Q2：财务职能结构
```
财务团队结构是怎样的？
1. 共享中心 SSC（财务共享中心）
2. 分散型（每个业务单元有独立财务）
3. 混合型（共享中心 + 部分分散）
```

### Q3：审计周期
```
审计周期是什么？
1. 自然年（1月1日～12月31日）
2. 财年（请说明起始月，如 4月1日～次年3月31日）
```

### Q4：主要财务系统（多选）
```
除了 ERP，你们还用哪些财务系统？
□ Power BI / Tableau（管理报表）
□ BlackLine（账户对账/关账）
□ SAP Concur / Expensify（差旅报销）
□ Kyriba / GTreasury（司库管理）
□ Bloomberg（外汇/市场数据）
□ 其他（请说明）
```

---

## Part 2：场景选择

**目标：确认用户需要哪些财务场景的能力。**

展示 29 个场景的分类地图：

```
┌─────────────────────────────────────────────────────────────┐
│  交易级（Transaction）                                      │
│  AP / AR / GL / 固定资产 / 工资 / 集团内往来              │
├─────────────────────────────────────────────────────────────┤
│  报告级（Reporting）                                        │
│  管理报告 / 董事会汇报 / 月结 / KPI / 费用审查               │
├─────────────────────────────────────────────────────────────┤
│  分析级（Analysis）                                         │
│  财务分析 / 商业洞察 / 成本控制 / 预算管理                   │
├─────────────────────────────────────────────────────────────┤
│  战略级（Strategic）                                        │
│  融资结构 / M&A / 投资管理 / 外汇风险 / ESG / 司库         │
├─────────────────────────────────────────────────────────────┤
│  合规级（Compliance）                                       │
│  内控设计 / 内控测试 / 审计支持 / 税务申报                   │
├─────────────────────────────────────────────────────────────┤
│  投资者关系 / 战略规划 / 资本配置                            │
└─────────────────────────────────────────────────────────────┘
```

询问：
```
你目前最需要哪些场景？（可多选，例如 "内控 + 董事会汇报 + 税务"）
或者输入 "全部" 安装所有场景。
```

根据用户选择，在 `CLAUDE.md` 的场景表中标记已选场景。

---

## Part 3：关键阈值设置

**目标：设置各场景的关键阈值（影响判断框架的量化标准）。**

对已选场景，询问关键阈值：

### 内控场景（如果选择了）
```
【内控缺陷评级阈值】
重大缺陷（Material Weakness）金额门槛：RMB [  500 ] 万
重要缺陷（Significant Deficiency）金额门槛：RMB [  100 ] 万

（提示：参考 SOX 404 和公司财务重要性水平）
```

### 费用合规场景（如果选择了）
```
【差旅/费用超标阈值】
住宿费超标：超过标准 [  20 ]%
餐费超标：超过标准 [  15 ]%
单次超规审批层级：[部门负责人] 级
```

### 预算场景（如果选择了）
```
【预算偏差预警阈值】
收入偏差预警：低于预算 [  -5 ]%
成本偏差预警：超过预算 [   5 ]%
重大偏差需要：[CFO] 审批
```

阈值写入各场景的 `references/数据源清单.md`，在 `threshold:` 字段下。

---

## Part 4：写入配置

**输出目标：**

```
~/.config/finance-skills/           ← 用户配置根目录（与 Legal 一致）
├── CLAUDE.md                      ← 公司级配置
├── credentials/                   ← API 密钥（不暴露给 Agent）
│   ├── sap.env
│   ├── pbi.env
│   └── bl.env
├── audit.log                      ← 操作日志
└── projects/                      ← 项目空间
    └── README.md
```

**更新 `references/数据源清单.md` 中的 Connector 映射**，注入已检测到的系统连接状态。

---

## `--check-connections` 标志

只运行 Part 0（连接器检测），更新 `CLAUDE.md` 中的连接器状态表，不修改其他配置。

```
/finance:cold-start --check-connections
```

---

## `--redo` 标志

重置所有配置，重新运行完整流程。**会覆盖已有配置**。

```
/finance:cold-start --redo
```

---

## 依赖关系

此 Skill 依赖：
- `CONNECTORS.md`（第 0 部分连接器检测需要知道有哪些 Connector 可用）
- `PROJECT_WORKSPACE.md`（了解项目目录结构）
- 各场景的 `references/数据源清单.md`（写入阈值）

首次运行前检查这些文件是否存在，如不存在给出警告。

---

## Fallback

如果无法连接到任何财务系统：
1. 标记所有 Connector 为 `Offline mode`
2. 告知用户：Skill 将在手动输入模式下运行（用户提供数据，Agent 输出判断）
3. 这是可用状态，只是效率较低
