---
name: kpi-management-master
description: >
  KPI 管理主流程 — 整合 KPI 目标设定、数据追踪、预警处理与根因分析。
  适用情形：月度/季度经营分析会或 KPI 异常预警触发时执行，
  整合 kpi-target-setting、kpi-data-tracking、kpi-alert-handling 和 kpi-root-cause-analysis，
  输出完整的 KPI 监控与归因报告。
  核心：目标设定 → 数据采集 → 异常预警 → 根因归因 → 改善跟踪。
argument-hint: "[KPI操作类型：目标设定/追踪/预警处理/根因分析] [涉及部门/指标]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# KPI 管理 Master Skill

## 能力描述

**这是什么：** KPI 管理场景的主技能，整合 KPI 目标设定、数据追踪、预警处理与根因分析，为财务 BP 和管理层提供 KPI 全景管理能力。

**解决什么问题：** 当用户需要设定 KPI、追踪 KPI 执行、处理 KPI 预警、或分析 KPI 未达标原因时，调用本技能获取完整的 KPI 管理方案。

**边界：** 不涉及具体业务执行（销售/生产本身），专注于 KPI 体系设计与分析。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"KPI"、"绩效指标"、"目标追踪"、"未达标"
- 用户提到"KPI 预警"、"指标异常"、"绩效分析"
- 用户要求"设定 KPI"、"追踪 KPI"、"分析 KPI"

---


## Examples

→ 示例：用户说"下个季度要给销售团队设KPI，需要财务BP配合做目标分解"，系统应调用本技能，进入KPI设定路径。

→ 示例：用户说"毛利率连续3个月低于预算，是什么原因"，系统应调用本技能，进入根因分析路径。

→ 示例：用户说"月度运营KPI有个预警，库存周转天数比上个月多了20天"，系统应调用本技能，进入KPI预警处理路径。
## 输入

```
□ 场景类型：[KPI 设定/追踪/预警处理/未达标分析]
□ KPI 类型：[财务 KPI/运营 KPI/业务 KPI]
□ 涉及期间：[月度/季度/年度]
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
Step 1 → [KPI 目标设定]（kpi-target-setting）
  → 输出：KPI 目标值与分解

Step 2 → [KPI 数据追踪]（kpi-data-tracking）
  → 输出：KPI 实际值报告

Step 3 → [KPI 预警处理]（kpi-alert-handling）
  → 输出：预警处理方案（如触发预警）

Step 4 → [KPI 根因分析]（kpi-root-cause）
  → 输出：未达标原因分析

Step 5 → 汇总输出 KPI 管理报告
```

---

## 输出格式

```
KPI 管理报告
====================

【KPI 概览】
□ KPI 数量：[X] 个
□ 达标率：[X%]
□ 黄灯 KPI：[X] 个
□ 红灯 KPI：[X] 个

【KPI 明细】
| KPI 名称 | 目标值 | 实际值 | 达成率 | 状态 |
|---|---|---|---|---|
| [名称] | [X] | [X] | [X%] | ✅/⚠️/🔴 |

【预警处理】（如适用）
□ 预警 KPI：[名称]
□ 预警原因：[描述]
□ 处理措施：[描述]

【未达标分析】（如适用）
□ 未达标 KPI：[名称]
□ 原因分类：[可控/不可控]
□ 根因：[描述]
□ 改进措施：[描述]

【下一步行动】
□ [行动1] — 责任人 [X] — 完成 [YYYY-MM-DD]
□ [行动2] — 责任人 [X] — 完成 [YYYY-MM-DD]
```

---

## 升级条件

满足以下任一条件须升级：

- 关键 KPI 连续 3 个月未达标 → 升级 CFO
- 须调整年度 KPI 目标 → 升级 CEO
- KPI 数据系统性不一致 → 升级 CFO

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| kpi-target-setting | KPI 目标设定与分解 |
| kpi-data-tracking | KPI 数据追踪与报告 |
| kpi-alert-handling | KPI 预警处理 |
| kpi-root-cause | KPI 未达标根因分析 |

---

*Finance Skills — kpi-management master skill*
