---
name: financing-structure-master
description: >
  融资结构主流程 — 整合融资成本分析、信用评级管理、融资渠道维护与融资方案设计。
  适用情形：年度融资规划或重大融资决策（银团/债券/股权融资）时执行，
  整合 financing-cost-calculation、bank-relationship-management、
  covenant-compliance-monitoring 和 debt-restructuring，输出完整的融资方案。
  核心：成本测算 → 渠道维护 → 契约合规 → 结构优化。
argument-hint: "[融资需求类型：新增/置换/优化] [融资金额] [期限要求] [是否有评级]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# 融资结构 Master Skill

## 能力描述

**这是什么：** 融资结构场景的主技能，整合融资成本分析、信用评级管理、融资渠道维护与融资方案设计，为 CFO 和司库团队提供完整的融资结构管理能力。

**解决什么问题：** 当用户需要分析融资成本、管理信用评级、维护银行关系、或设计新融资方案时，调用本技能获取完整的融资结构管理方案。

**边界：** 不涉及具体投资决策，专注于融资端的结构设计与成本管理。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"融资成本"、"信用评级"、"授信额度"、"融资渠道"
- 用户提到"WACC"、"债务结构"、"银行关系"
- 用户要求"分析融资成本"、"管理评级"、"设计融资方案"

---


## Examples

→ 示例：用户说"子公司要在境外发美元债，帮我评估一下融资成本和汇率风险"，系统应调用本技能，进入融资方案设计路径。

→ 示例：用户说"评级公司刚下调了我们的评级，CFO要求分析对现有债务的影响"，系统应调用本技能，进入评级管理路径。

→ 示例：用户说"银行给我们的授信额度下个月到期，需要准备续授信的材料"，系统应调用本技能，进入渠道维护路径。
## 输入

```
□ 场景类型：[成本分析/评级管理/渠道维护/方案设计]
□ 融资工具类型：[银行贷款/债券/租赁/其他]
□ 涉及金额：[X] 万
□ 期限：[X] 年
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
路径一：融资成本分析
Step 1 → [融资成本核算]（financing-cost-calculation）
  → 输出：成本分析报告

Step 2 → [评级变动追踪]（rating-change-tracking）
  → 输出：评级状态

Step 3 → [融资渠道评估]（financing-channel-assessment）
  → 输出：渠道对比

Step 4 → 汇总输出融资成本分析报告

路径二：融资方案设计
Step 1 → [融资需求测算]（financing-need-assessment）
  → 输出：融资需求

Step 2 → [融资工具选择]（financing-instrument-selection）
  → 输出：工具建议

Step 3 → [融资成本核算]（financing-cost-calculation）
  → 输出：成本测算

Step 4 → [融资渠道维护]（financing-channel-maintenance）
  → 输出：渠道关系

Step 5 → 汇总输出融资方案建议
```

---

## 输出格式

```
融资结构管理报告
====================

【融资概览】
□ 现有融资总额：[X] 亿
□ 加权平均成本：[X%]
□ 授信总额：[X] 亿
□ 可用额度：[X] 亿

【融资明细】
| 工具 | 金额 | 利率 | 到期日 | 成本 |
|---|---|---|---|---|
| [类型] | [X]亿 | [X%] | [YYYY] | [X%] |

【成本分析】
□ 当前 WACC：[X%]
□ 债务成本：[X%]
□ 股权成本：[X%]
□ 成本变化：[±X bp]

【评级状态】（如有变化）
□ 最新评级：[AAA/AA/A]
□ 评级机构：[名称]
□ 评级变动：[上调/维持/下调] — 原因 [描述]

【融资方案建议】（如有）
□ 建议工具：[描述]
□ 建议规模：[X] 亿
□ 预计成本：[X%]
□ 实施路径：[描述]

【银行关系】
□ 合作银行：[X] 家
□ 主结算银行：[名称]
□ 须关注事项：[描述]
```

---

## 升级条件

满足以下任一条件须立即升级：

- 融资成本上升 > [X] bp → CFO 审批
- 信用评级下调 → 立即升级 CEO/CFO
- 须新增融资渠道 → CFO + CEO 审批

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| financing-cost-calculation | 融资成本核算 |
| rating-change-tracking | 信用评级变动追踪 |
| financing-channel-assessment | 融资渠道评估 |
| financing-need-assessment | 融资需求测算 |
| financing-instrument-selection | 融资工具选择 |
| financing-channel-maintenance | 融资渠道维护 |

---

*Finance Skills — financing-structure master skill*
