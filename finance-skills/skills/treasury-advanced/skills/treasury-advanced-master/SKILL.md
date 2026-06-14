---
name: treasury-advanced-master
description: >
  高级司库主流程 — 整合现金池管理、流动性风险管控（LCR/NSFR）、投资合规与银行关系维护。
  适用情形：日终流动性监控、季度监管报送或重大资金架构调整时执行，
  整合 cash-pool-configuration、lcr-assessment、investment-compliance-check
  和 bank-relationship-assessment，输出符合监管要求的司库管理报告。
  核心：资金归集 → 流动性计量 → 监管合规 → 渠道维护。
argument-hint: "[司库任务类型：现金池/LCR/投资/银行关系] [涉及账户/金额]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# 高级司库 Master Skill

## 能力描述

**这是什么：** 高级司库场景的主技能，整合现金池管理、流动性风险管控（LCR/NSFR）、投资管理与银行关系维护，为 CFO 和司库团队提供完整的司库管理能力。

**解决什么问题：** 当用户需要管理现金池、应对流动性预警、处理银行关系变化、或管理投资组合时，调用本技能获取完整的司库管理方案。

**边界：** 不涉及具体业务运营资金调动，专注于流动性安全和收益管理。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"司库"、"现金池"、"LCR"、"流动性"
- 用户提到"投资理财"、"银行授信"、"银行关系"
- 用户要求"管理现金池"、"应对流动性预警"、"管理投资组合"

---

## 输入

```
□ 场景类型：[现金池管理/流动性管理/投资管理/银行关系]
□ 涉及账户：[列表]
□ 涉及金额：[X] 万
□ 紧迫程度：[紧急/一般/规划性]
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
路径一：现金池管理
Step 1 → [现金池配置]（cash-pool-configuration）
  → 输出：池配置

Step 2 → [资金调拨]（fund-transfer）
  → 输出：调拨确认

Step 3 → [池余额监控]（pool-balance-monitoring）
  → 输出：监控报告

Step 4 → 汇总输出现金池管理报告

路径二：流动性预警处理
Step 1 → [LCR 评估]（lcr-assessment）
  → 输出：LCR 状态

Step 2 → [流动性应急处理]（liquidity-emergency-handling）
  → 输出：应急方案

Step 3 → [银行授信激活]（bank-credit-activation）
  → 输出：授信启用

Step 4 → 汇总输出流动性应对报告

路径三：投资管理
Step 1 → [投资合规检查]（investment-compliance-check）
  → 输出：合规确认

Step 2 → [投资执行]（investment-execution）
  → 输出：执行确认

Step 3 → [投资绩效追踪]（investment-performance-tracking）
  → 输出：绩效报告

Step 4 → [投资风险管理]（investment-risk-management）
  → 输出：风险报告

Step 5 → 汇总输出投资管理报告
```

---

## 输出格式

```
高级司库管理报告
====================

【现金头寸】
□ 总可用现金：[X] 万
□ 分布：境内 [X] 万 / 境外 [X] 万
□ 现金池状态：[正常/预警/紧张]

【LCR/NSFR】
□ LCR：[X%]（监管 [X%]）
□ HQLA：[X] 万
□ 30 天净流出：[X] 万
□ NSFR：[X%]

【现金池】
□ 池类型：[实体现金池/虚拟现金池]
□ 主账户余额：[X] 万
□ 子账户余额：[X] 万
□ 昨日调拨：[X] 笔，[X] 万

【银行关系】
□ 合作银行：[X] 家
□ 授信总额：[X] 万
□ 可用额度：[X] 万
□ 须关注事项：[描述]

【投资组合】
□ 投资总额：[X] 万
□ 产品类型：存款 [X%]/国债 [X%]/货币基金 [X%]/理财 [X%]
□ 本月收益：[X] 万
□ 浮盈/亏：[±X] 万

【流动性预警】（如有）
□ 预警级别：[黄/红]
□ 预警原因：[描述]
□ 应急措施：[描述]
□ 预计恢复：[YYYY-MM-DD]
```

---

## 升级条件

满足以下任一条件须立即升级：

- LCR < 监管要求 → 立即升级 CFO/CEO
- 银行授信突然收紧 → 立即升级 CFO
- 投资亏损 > [X] 万 → CFO + CEO 审批
- 跨境资金调动受限 → CFO + CEO 知悉

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| cash-pool-configuration | 现金池配置 |
| fund-transfer | 资金调拨 |
| pool-balance-monitoring | 池余额监控 |
| lcr-assessment | LCR 评估 |
| liquidity-emergency-handling | 流动性应急处理 |
| bank-credit-activation | 银行授信激活 |
| investment-compliance-check | 投资合规检查 |
| investment-execution | 投资执行 |
| investment-performance-tracking | 投资绩效追踪 |
| investment-risk-management | 投资风险管理 |

---

*Finance Skills — treasury-advanced master skill*
