---
name: esg-reporting-master
description: >
  ESG 报告主流程 — 整合环境/社会/治理数据收集、ESG 评级管理、重大事件应对与报告编制。
  适用情形：年度 ESG 报告披露或评级机构（MSCI/Sustainalytics）评估时执行，
  整合 esg-data-integration、esg-materiality-assessment、esg-rating-tracking 和 esg-reporting，
  输出符合监管要求的 ESG 报告。
  核心：数据完整性 → 重要性评估 → 评级管理 → 合规披露。
argument-hint: "[ESG数据类型：E/S/G] [报告用途：披露/评级/内部] [数据期间]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# ESG 报告 Master Skill

## 能力描述

**这是什么：** ESG 报告场景的主技能，整合环境/社会/治理数据收集、ESG 评级管理、重大事件应对与报告编制，为 CFO 和可持续发展团队提供完整的 ESG 管理能力。

**解决什么问题：** 当用户需要收集 ESG 数据、管理 ESG 评级、应对重大 ESG 事件、或编制 ESG 报告时，调用本技能获取完整的 ESG 管理方案。

**边界：** 不涉及具体业务运营，专注于 ESG 数据管理和披露合规。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"ESG"、"碳排放"、" sustainability"、"社会责任"
- 用户提到"ESG 评级"、"ESG 报告"、"GRI"、"TCFD"
- 用户要求"编制 ESG 报告"、"提升 ESG 评级"、"应对 ESG 事件"

---


## Examples

→ 示例：用户说"MSCI要来做ESG评级访谈，财务需要准备哪些数据"，系统应调用本技能，进入评级管理路径。

→ 示例：用户说" regulators要求披露Scope 3碳排放，我们还没有完整的核算体系"，系统应调用本技能，进入数据收集路径。

→ 示例：用户说"年度ESG报告马上要交了，需要财务确认碳成本数据的准确性"，系统应调用本技能，进入报告编制路径。
## 输入

```
□ 场景类型：[数据收集/评级管理/事件应对/报告编制]
□ 报告周期：[年度/季度]
□ 框架标准：[GRI/SASB/TCFD/CSRD]
□ 涉及范围：[E/S/G]
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
路径一：ESG 报告编制
Step 1 → [E 指标收集]（environmental-data-collection）
  → 输出：环境数据

Step 2 → [S 指标收集]（social-data-collection）
  → 输出：社会数据

Step 3 → [G 指标收集]（governance-data-collection）
  → 输出：治理数据

Step 4 → [ESG 数据整合]（esg-data-integration）
  → 输出：整合数据

Step 5 → [ESG 报告撰写]（esg-report-writing）
  → 输出：ESG 报告

路径二：评级管理
Step 1 → [ESG 评级追踪]（esg-rating-tracking）
  → 输出：评级状态

Step 2 → [评级差距分析]（rating-gap-analysis）
  → 输出：差距报告

Step 3 → [评级提升建议]（rating-improvement-advice）
  → 输出：提升方案

Step 4 → 汇总输出评级管理报告

路径三：重大事件应对
Step 1 → [ESG 事件评估]（esg-event-assessment）
  → 输出：事件评估

Step 2 → [事件即时响应]（event-immediate-response）
  → 输出：响应方案

Step 3 → [ESG 披露评估]（esg-disclosure-assessment）
  → 输出：披露要求

Step 4 → 汇总输出事件应对报告
```

---

## 输出格式

```
ESG 管理报告
====================

【ESG 概览】
□ 框架标准：[GRI/SASB/TCFD]
□ 数据完整度：[X%]
□ 重大事件：[X] 起

【E（环境）指标】
| 指标 | 目标 | 实际 | 完成率 |
|---|---|---|---|
| 碳排放（范围1+2） | [X] tCO2e | [X] tCO2e | [X%] |
| 能耗 | [X] MWh | [X] MWh | [X%] |

【S（社会）指标】
| 指标 | 目标 | 实际 | 完成率 |
|---|---|---|---|
| 员工培训时长 | [X]h/人 | [X]h/人 | [X%] |
| 工伤率 | [X]% | [X]% | [X%] |

【G（治理）指标】
| 指标 | 目标 | 实际 | 完成率 |
|---|---|---|---|
| 独立董事比例 | [X]% | [X]% | [X%] |

【ESG 评级】（如有）
□ MSCI 评级：[X]
□ 评级机构：[名称]
□ 评级变动：[上调/维持/下调]

【报告状态】
□ 编制进度：[X%]
□ 审批状态：[草稿/审阅中/已发布]
□ 发布预期：[YYYY-MM-DD]
```

---

## 升级条件

满足以下任一条件须立即升级：

- 重大 ESG 事件 → 立即升级 CEO/CFO
- ESG 评级下调 → CEO 关注
- 须即时披露事件 → CEO/CFO/董秘审批

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| environmental-data-collection | 环境指标收集 |
| social-data-collection | 社会指标收集 |
| governance-data-collection | 治理指标收集 |
| esg-data-integration | ESG 数据整合 |
| esg-report-writing | ESG 报告撰写 |
| esg-rating-tracking | ESG 评级追踪 |
| rating-gap-analysis | 评级差距分析 |
| rating-improvement-advice | 评级提升建议 |
| esg-event-assessment | ESG 事件评估 |
| event-immediate-response | 事件即时响应 |
| esg-disclosure-assessment | ESG 披露评估 |

---

*Finance Skills — esg-reporting master skill*
