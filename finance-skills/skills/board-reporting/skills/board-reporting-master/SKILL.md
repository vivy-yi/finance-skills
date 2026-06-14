---
name: board-reporting-master
description: >
  董事会汇报主流程 — 整合 Board Deck 编制、审计委员会支持、董事会议程管理与重大事项汇报。
  适用情形：年度/季度董事会与审计委员会会议前执行，整合 board-deck-preparation、
  audit-committee-support、board-meeting-management 和 board-material-distribution，
  输出完整的董事会汇报材料包。
  核心：会议准备 → 材料编制 → 委员会协同 → 重大事项汇报。
argument-hint: "[会议类型：Board/审计委员会/专门委员会] [报告期间] [是否紧急] [主要议题]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# 董事会汇报 Master Skill

## 能力描述

**这是什么：** 董事会汇报场景的主技能，整合 Board Deck 编制、审计委员会支持、董事会议程管理与重大事项汇报，为 CFO 和董秘提供完整的董事会支持能力。

**解决什么问题：** 当用户需要准备 Board Deck、处理审计委员会问询、管理董事会议程、或向董事会汇报重大事项时，调用本技能获取完整的董事会汇报方案。

**边界：** 不涉及具体业务决策（投资/融资本身），专注于汇报材料准备与流程管理。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"Board Deck"、"董事会"、"审计委员会"、"董事会议程"
- 用户提到"Board 汇报材料"、"董事会演示"、"高管汇报"
- 用户要求"准备 Board Deck"、"管理议程"、"处理审计委员会问询"

---


## Examples

→ 示例：用户说"下周三董事会，要准备Q1的Board Deck，时间很紧"，系统应调用本技能，进入Board Deck编制路径。

→ 示例：用户说"审计委员会对内控缺陷整改进度有疑问，需要准备一份专项汇报"，系统应调用本技能，进入审计委员会支持路径。

→ 示例：用户说"CEO要求在董事会上解释一下我们最新的ESG评级变化"，系统应调用本技能，进入重大事项汇报路径。
## 输入

```
□ 场景类型：[Deck 编制/审计委员会支持/议程管理/重大事项汇报]
□ 会议类型：[董事会/审计委员会/战略委员会/薪酬委员会]
□ 涉及议题：[列出议题]
□ 会议时间：[YYYY-MM-DD]
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
路径一：Board Deck 编制
Step 1 → [Board Deck 编制]（board-deck-preparation）
  → 输出：Board Deck 草稿

Step 2 → [财务数据协调]（financial-data-coordination）
  → 输出：数据核对报告

Step 3 → [Board 演示支持]（board-presentation-support）
  → 输出：Q&A 准备材料

Step 4 → 汇总输出完整 Board Deck

路径二：审计委员会支持
Step 1 → [审计发现响应]（audit-finding-response）
  → 输出：审计问询回复

Step 2 → [内控缺陷汇报]（control-deficiency-reporting）
  → 输出：缺陷整改进度

Step 3 → [审计委员会材料]（audit-committee-material）
  → 输出：审计委员会专项材料

Step 4 → 汇总输出审计委员会支持包
```

---

## 输出格式

```
董事会汇报支持报告
====================

【会议信息】
□ 会议类型：[董事会/审计委员会]
□ 会议时间：[YYYY-MM-DD HH:MM]
□ 参会人员：[列表]

【议程】
| 序号 | 议题 | 汇报人 | 时长 | 资料 |
|---|---|---|---|---|
| 1 | [议题] | [姓名] | [X]min | [Deck 名称] |

【Board Deck 概览】
□ Deck 页数：[X] 页
□ 核心内容：[摘要]

【数据核对】
□ 审计数据 vs Board Deck：[✅ 一致 / ⚠️ 存在差异]
□ 差异项：[列表]

【Q&A 准备】
□ 预计问题：[X] 个
□ 敏感问题：[X] 个
□ 准备状态：[✅ 已准备 / ⚠️ 部分准备]

【升级事项】
□ 须 CEO 关注事项：[描述]
□ 须董事会决策事项：[描述]
```

---

## 升级条件

满足以下任一条件须立即升级：

- 须披露重大信息 → CEO/董秘确认
- 涉及关联交易 → 独立董事审批
- 审计委员会提出重大质疑 → CEO/CFO 回应

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| board-deck-preparation | Board Deck 编制 |
| financial-data-coordination | 财务数据协调与核对 |
| board-presentation-support | Board 演示支持与 Q&A 准备 |
| audit-finding-response | 审计发现响应 |
| control-deficiency-reporting | 内控缺陷汇报 |
| audit-committee-material | 审计委员会专项材料 |

---

*Finance Skills — board-reporting master skill*
