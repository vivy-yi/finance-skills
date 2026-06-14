---
name: capital-allocation-master
description: >
  资本配置主流程 — 整合投资评估、资本预算、WACC 测算与股东回报管理。
  适用情形：年度资本预算编制或重大投资项目评估时执行，整合 investment-evaluation、
  wacc-calculation、roic-vs-wacc-comparison 和 scenario-analysis，
  输出完整的资本配置决策包。
  核心：投资回报测算 → 风险加权 → 资本成本对照 → 配置优化。
argument-hint: "[决策类型：投资评估/资本预算/股东回报/WACC] [相关金额] [决策阶段]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# 资本配置 Master Skill

## 能力描述

**这是什么：** 资本配置场景的主技能，整合投资评估、资本预算、WACC 测算与股东回报管理，为 CFO 和战略团队提供完整的资本配置管理能力。

**解决什么问题：** 当用户需要评估投资项目、制定资本预算、测算 WACC、或管理股东回报时，调用本技能获取完整的资本配置管理方案。

**边界：** 不涉及具体业务运营投资决策，专注于资本层面的配置与回报管理。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"资本配置"、"投资评估"、"WACC"、"股东回报"
- 用户提到"资本预算"、"ROIC"、"IRR"、"股息"
- 用户要求"评估投资项目"、"制定资本预算"、"管理股东回报"

---


## Examples

→ 示例：用户说"今年有5个Capex项目在排队，总预算超了，需要按优先级排序"，系统应调用本技能，进入资本预算路径。

→ 示例：用户说"帮我测一下我们目前的WACC，明年的融资决策要用"，系统应调用本技能，进入WACC测算路径。

→ 示例：用户说"PE投资人问我们未来3年的股息政策，有什么建议"，系统应调用本技能，进入股东回报路径。
## 输入

```
□ 场景类型：[投资评估/资本预算/WACC 测算/股东回报]
□ 资本类型：[Capex/M&A/战略投资]
□ 涉及金额：[X] 万
□ 审批层级：[财务经理/CFO/CEO/董事会]
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
路径一：投资项目评估
Step 1 → [投资评估测算]（investment-evaluation）
  → 输出：IRR/NPV/ROIC

Step 2 → [ROIC vs WACC 比较]（roic-vs-wacc-comparison）
  → 输出：价值创造评估

Step 3 → [投资优先级排序]（investment-priority-ranking）
  → 输出：优先级列表

Step 4 → [投资审批支持]（investment-approval-support）
  → 输出：审批材料

路径二：资本预算
Step 1 → [资本需求测算]（capital-requirement-assessment）
  → 输出：需求规模

Step 2 → [资本来源规划]（capital-source-planning）
  → 输出：来源方案

Step 3 → [配置比例设计]（allocation-ratio-design）
  → 输出：配置比例

Step 4 → [预算执行追踪]（budget-execution-tracking）
  → 输出：执行报告

路径三：股东回报
Step 1 → [股息政策评估]（dividend-policy-assessment）
  → 输出：政策评估

Step 2 → [股息分配执行]（dividend-distribution-execution）
  → 输出：分配方案

Step 3 → [回购计划管理]（buyback-plan-management）
  → 输出：回购计划

Step 4 → 汇总输出股东回报报告

路径四：WACC 重大变化应对
Step 1 → [WACC 重新测算]（wacc-recalculation）
  → 输出：新 WACC

Step 2 → [对资本配置的影响]（impact-on-capital-allocation）
  → 输出：影响分析

Step 3 → [IRR 门槛调整]（irr-threshold-adjustment）
  → 输出：新门槛

Step 4 → 汇总输出 WACC 变化应对报告
```

---

## 输出格式

```
资本配置管理报告
====================

【WACC】
□ 当前 WACC：[X%]
□ 债务成本：[X%]
□ 股权成本：[X%]
□ D/E 结构：[X]/[X]
□ WACC 变化：[±X bp]

【投资组合】
□ 在执行项目：[X] 个
□ 总投资：[X] 亿
□ 平均 IRR：[X%]
□ IRR vs WACC：[X%] vs [X%]

【项目评估】（如有新项目）
| 项目 | IRR | NPV | ROIC | 优先级 |
|---|---|---|---|---|
| [名称] | [X%] | [X]万 | [X%] | [1/2/3] |

【资本配置】
□ 可用资本：[X] 亿
□ 已分配：[X] 亿
□ 待分配：[X] 亿
□ 配置比例：运营 [X%]/战略 [X%]/回报 [X%]

【股东回报】
□ 股息政策：派息比例 [X]%
□ 本期股息：[X] 万
□ 回购计划：[X] 万（如有）
□ 执行状态：[✅ 已批准 / ⚠️ 待审批]

【IRR 门槛】
□ 当前门槛：[X%]
□ 建议门槛：[X%]（如 WACC 变化 > ±[X] bp）
□ 审批状态：[✅ 已更新 / ⚠️ 待审批]

【升级事项】（如有）
□ ROIC 连续低于 WACC：[X] 年 — 须战略复盘
□ 单项投资超权限：[描述] — 须 [CFO/CEO/董事会] 审批
```

---

## 升级条件

满足以下任一条件须立即升级：

- 单项投资 > [X] 万 → 董事会审批
- ROIC 连续 2 年低于 WACC → CEO/CFO 战略复盘
- 资本配置政策重大调整 → 董事会审批

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| investment-evaluation | 投资评估测算 |
| roic-vs-wacc-comparison | ROIC vs WACC 比较 |
| investment-priority-ranking | 投资优先级排序 |
| investment-approval-support | 投资审批支持 |
| capital-requirement-assessment | 资本需求测算 |
| capital-source-planning | 资本来源规划 |
| allocation-ratio-design | 配置比例设计 |
| budget-execution-tracking | 预算执行追踪 |
| dividend-policy-assessment | 股息政策评估 |
| dividend-distribution-execution | 股息分配执行 |
| buyback-plan-management | 回购计划管理 |
| wacc-recalculation | WACC 重新测算 |
| impact-on-capital-allocation | 对资本配置的影响 |
| irr-threshold-adjustment | IRR 门槛调整 |

---

*Finance Skills — capital-allocation master skill*
