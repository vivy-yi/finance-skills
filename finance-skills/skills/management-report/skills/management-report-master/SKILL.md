---
name: management-report-master
description: >
  管理报告主流程 — 整合月度财务报告编制、业务分析整合、指标预警处理与管理报告发布。
  适用情形：月度/季度管理报告编制（每月固定时间）时执行，
  整合 financial-report-generation、management-commentary-writing、metric-alert-handling
  和 management-report-publishing，输出完整的管理报告包。
  核心：财务数据 → 业务解读 → 指标预警 → 报告编排 → 分发归档。
argument-hint: "[报告期间 YYYY-MM] [报告类型：月度/季度/年度] [是否有预警数据]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: medium
---

# 管理报告 Master Skill

## 能力描述

**这是什么：** 管理报告场景的主技能，整合月度财务报告编制、业务分析整合、指标预警处理与管理报告发布，为 CFO 和财务分析团队提供完整的管理报告生产能力。

**解决什么问题：** 当用户需要编制月度管理报告、处理报告中的指标预警、整合业务分析到财务报告、或发布管理报告时，调用本技能获取完整的管理报告生产方案。

**边界：** 不涉及具体业务运营分析，专注于报告生产流程和财务与业务的整合分析。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"管理报告"、"月度报告"、"财务分析报告"
- 用户提到"报告预警"、"指标异常"、"数据不一致"
- 用户要求"编制管理报告"、"整合业务分析"、"发布报告"

---


## Examples

→ 示例：用户说"月度管理报告到截止日期了，数据都拿齐了，帮我看一下结构有没有问题"，系统应调用本技能，进入报告编制路径。

→ 示例：用户说"业务和财务对收入的数字对不上，管理报告发不出去"，系统应调用本技能，进入数据协调路径。

→ 示例：用户说"几个指标触发了预警，需要在管理报告里重点说明一下"，系统应调用本技能，进入预警处理路径。
## 输入

```
□ 场景类型：[报告编制/预警处理/数据协调/报告发布]
□ 报告期间：[YYYY-MM]
□ 报告范围：[公司整体/业务线/部门]
□ 截止日期：[YYYY-MM-DD]
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
路径一：月度管理报告编制
Step 1 → [管理报告数据提取]（management-report-data）
  → 输出：基础数据

Step 2 → [指标预警处理]（kpi-alert-handling）
  → 输出：预警处理方案

Step 3 → [业务分析整合]（business-analysis-integration）
  → 输出：业务分析内容

Step 4 → [管理报告撰写]（management-report-writing）
  → 输出：完整报告

Step 5 → [管理报告审阅]（management-report-review）
  → 输出：审阅意见

路径二：报告预警处理
Step 1 → [指标预警处理]（kpi-alert-handling）
  → 输出：预警分析

Step 2 → [业务分析整合]（business-analysis-integration）
  → 输出：根因分析

Step 3 → [管理报告撰写]（management-report-writing）
  → 输出：预警说明

Step 4 → 汇总输出预警处理报告
```

---

## 输出格式

```
管理报告生产报告
====================

【报告概览】
□ 报告期间：[YYYY-MM]
□ 报告页数：[X] 页
□ 数据完整度：[X%]
□ 预警数量：[X] 个（黄 [X] / 红 [X]）

【核心指标】
| 指标 | 目标 | 实际 | 达成率 | 状态 |
|---|---|---|---|---|
| [名称] | [X] | [X] | [X%] | ✅/⚠️/🔴 |

【预警处理】（如有）
□ 预警指标：[名称]
□ 原因：[描述]
□ 影响：[描述]
□ 建议：[描述]

【业务分析整合】（如有）
□ 分析主题：[描述]
□ 关键洞察：[X] 点
□ 建议行动：[X] 项

【报告审阅】
□ 审阅意见：[X] 条
□ 须修改项：[列表]
□ 发布状态：[草稿/审阅中/已发布]

【下一步】
□ 报告发布：[YYYY-MM-DD]
□ 下月报告启动：[YYYY-MM-DD]
```

---

## 升级条件

满足以下任一条件须升级：

- 关键指标跌破红线 → 立即升级 CEO
- 数据跨系统不一致 → 升级 CFO
- 报告须跨部门协调 → 升级 CFO 协调

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| management-report-data | 管理报告数据提取 |
| kpi-alert-handling | 指标预警处理 |
| business-analysis-integration | 业务分析整合 |
| management-report-writing | 管理报告撰写 |
| management-report-review | 管理报告审阅 |

---

*Finance Skills — management-report master skill*
