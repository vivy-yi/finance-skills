---
name: fx-risk-master
description: >
  外汇风险管理主流程 — 整合外汇敞口管理、对冲策略执行、敞口超限处理与模型失效应对。
  适用情形：外汇敞口监控周期（每日/每周）或重大汇率波动事件触发时执行，
  整合 fx-exposure-calculation、fx-forecast-analysis、fx-hedging-strategy 和 fx-deal-execution，
  输出完整的外汇风险管理报告与对冲执行清单。
  核心：敞口测算 → 情景分析 → 对冲策略 → 执行监控 → 模型校准。
argument-hint: "[外汇敞口类型：交易/换算/经济] [涉及币种] [敞口金额] [对冲状态]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# 外汇风险 Master Skill

## 能力描述

**这是什么：** 外汇风险场景的主技能，整合外汇敞口管理、对冲策略执行、敞口超限处理与模型失效应对，为司库团队提供完整的外汇风险管理能力。

**解决什么问题：** 当用户需要管理外汇敞口、执行对冲策略、处理敞口超限、或应对汇率预测失效时，调用本技能获取完整的外汇风险管理方案。

**边界：** 不涉及具体进出口业务执行，专注于外汇风险的对冲与管理。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"外汇敞口"、"对冲策略"、"远期外汇"、"汇率风险"
- 用户提到"敞口超限"、"对冲亏损"、"外汇预警"
- 用户要求"管理外汇风险"、"执行对冲"、"分析敞口"

---


## Examples

→ 示例：用户说"人民币近期波动很大，需要评估一下我们的外汇敞口和对冲方案"，系统应调用本技能，进入敞口管理路径。

→ 示例：用户说"欧元收款对冲合约快到期了，需要决策是否展期"，系统应调用本技能，进入对冲执行路径。

→ 示例：用户说"对冲亏损超过了预警线，需要向CFO解释原因并提出调整建议"，系统应调用本技能，进入超限处理路径。
## 输入

```
□ 场景类型：[敞口管理/对冲执行/超限处理/模型失效]
□ 涉及币种：[USD/EUR/其他]
□ 敞口金额：[X] 万美元等值
□ 当前汇率：[X.XX]
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
路径一：日常敞口管理
Step 1 → [外汇敞口计算]（fx-exposure-calculation）
  → 输出：敞口报告

Step 2 → [对冲比例建议]（hedge-ratio-advice）
  → 输出：对冲建议

Step 3 → [对冲工具选择]（hedge-instrument-selection）
  → 输出：工具建议

Step 4 → [对冲执行]（hedge-execution）
  → 输出：执行确认

路径二：敞口超限处理
Step 1 → [外汇敞口计算]（fx-exposure-calculation）
  → 输出：超限确认

Step 2 → [超限应急处理]（exposure-exceed-handling）
  → 输出：应急方案

Step 3 → [对冲执行]（hedge-execution）
  → 输出：新增对冲

Step 4 → [政策调整建议]（policy-adjustment-advice）
  → 输出：限额调整建议

路径三：模型失效应对
Step 1 → [模型失效识别]（model-failure-identification）
  → 输出：失效确认

Step 2 → [对冲策略临时调整]（hedge-temp-adjustment）
  → 输出：临时策略

Step 3 → [模型改进]（model-improvement）
  → 输出：改进方案

Step 4 → 汇总输出模型失效应对报告
```

---

## 输出格式

```
外汇风险管理报告
====================

【敞口概览】
□ 币种：[USD/EUR/其他]
□ 总敞口：[X] 万美元等值
□ 已对冲：[X] 万美元等值
□ 未对冲：[X] 万美元等值
□ 对冲比例：[X%]

【敞口明细】
| 敞口类型 | 金额 | 对冲金额 | 未对冲 |
|---|---|---|---|
| 贸易敞口 | [X]万 | [X]万 | [X]万 |
| 金融敞口 | [X]万 | [X]万 | [X]万 |

【对冲现状】
□ 工具类型：[远期/期权/掉期]
□ 在手合约：[X] 份
□ 合约金额：[X] 万
□ 平均汇率：[X.XX]
□ 账面盈亏：[±XXX万]

【VaR 分析】
□ 置信水平：[95%/99%]
□ VaR：[XXX万]
□ 压力测试损失：[XXX万]（汇率±10%）

【超限处理】（如有）
□ 超限金额：[X] 万
□ 超限原因：[描述]
□ 应急措施：[描述]
□ 执行时间：[YYYY-MM-DD]

【对冲建议】
□ 建议对冲量：[X] 万
□ 建议工具：[描述]
□ 预计成本：[X] 万
```

---

## 升级条件

满足以下任一条件须立即升级：

- 敞口超限 → 立即升级 CFO
- 对冲亏损 > [X] 万 → CFO + CEO 审批
- 模型连续失效 → CFO 审批更换

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| fx-exposure-calculation | 外汇敞口计算 |
| hedge-ratio-advice | 对冲比例建议 |
| hedge-instrument-selection | 对冲工具选择 |
| hedge-execution | 对冲执行 |
| exposure-exceed-handling | 敞口超限应急处理 |
| policy-adjustment-advice | 政策调整建议 |
| model-failure-identification | 模型失效识别 |
| hedge-temp-adjustment | 对冲策略临时调整 |
| model-improvement | 模型改进 |

---

*Finance Skills — fx-risk master skill*
