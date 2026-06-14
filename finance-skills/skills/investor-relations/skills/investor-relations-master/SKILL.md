---
name: investor-relations-master
description: >
  投资者关系主流程 — 整合信息披露管理、分析师关系维护、投资者沟通与重大事件 IR 应对。
  适用情形：定期业绩发布、路演筹备、分析师问询回复或重大资本市场事件时执行，
  整合 ir-disclosure-management、earnings-call-preparation、roadshow-material-preparation
  和 investor-feedback-tracking，输出符合监管披露要求的 IR 沟通材料。
  核心：信息披露合规 → 投资者沟通 → 反馈跟踪 → 关系维护。
argument-hint: "[IR任务类型：信息披露/路演/分析师沟通/业绩发布] [时间节点]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# 投资者关系 Master Skill

## 能力描述

**这是什么：** 投资者关系场景的主技能，整合信息披露管理、分析师关系维护、投资者沟通与重大事件 IR 应对，为 CFO 和 IR 团队提供完整的投资者关系管理能力。

**解决什么问题：** 当用户需要管理信息披露、处理分析师问询、组织业绩路演、或应对投资者重大关切时，调用本技能获取完整的 IR 管理方案。

**边界：** 不涉及具体业务运营，专注于投资者沟通与信息披露管理。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"投资者关系"、"IR"、"分析师"、"路演"
- 用户提到"信息披露"、"机构投资者"、"股东"
- 用户要求"管理 IR"、"组织路演"、"处理投资者问询"

---


## Examples

→ 示例：用户说"下个月有业绩路演，帮我准备一下Q&A里可能被问到的财务问题"，系统应调用本技能，进入投资者沟通路径。

→ 示例：用户说"有分析师发了份负面报告，我们需要准备一个官方回应"，系统应调用本技能，进入分析师关系路径。

→ 示例：用户说"有重大收购要公告，需要确保信息披露合规，不出现选择性披露"，系统应调用本技能，进入信息披露管理路径。
## 输入

```
□ 场景类型：[信息披露/分析师关系/投资者沟通/事件应对]
□ 活动类型：[业绩发布/路演/NDR/股东大会]
□ 涉及对象：[机构投资者/分析师/散户/监管]
□ 时间：[YYYY-MM-DD]
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
路径一：信息披露管理
Step 1 → [披露合规检查]（disclosure-compliance-check）
  → 输出：合规清单

Step 2 → [披露内容准备]（disclosure-content-preparation）
  → 输出：披露草稿

Step 3 → [披露审批]（disclosure-approval）
  → 输出：审批记录

Step 4 → [披露发布]（disclosure-publishing）
  → 输出：发布确认

路径二：业绩路演
Step 1 → [路演材料准备]（roadshow-material-preparation）
  → 输出：路演 Deck

Step 2 → [投资者名单确认]（investor-list-confirmation）
  → 输出：投资者清单

Step 3 → [路演执行]（roadshow-execution）
  → 输出：路演纪要

Step 4 → [路演后跟进]（roadshow-follow-up）
  → 输出：跟进清单

路径三：投资者关切处理
Step 1 → [投资者问询分类]（investor-query-classification）
  → 输出：问询分类

Step 2 → [敏感信息评估]（sensitive-information-assessment）
  → 输出：披露评估

Step 3 → [问询回应准备]（query-response-preparation）
  → 输出：回复材料

Step 4 → [问询记录归档]（query-record-filing）
  → 输出：归档记录

路径四：重大事件应对
Step 1 → [事件IR影响评估]（event-ir-impact-assessment）
  → 输出：影响评估

Step 2 → [IR应对方案]（ir-response-plan）
  → 输出：应对方案

Step 3 → [沟通材料准备]（communication-material-preparation）
  → 输出：沟通材料

Step 4 → 汇总输出事件 IR 应对报告
```

---

## 输出格式

```
投资者关系管理报告
====================

【投资者结构】
□ 机构投资者：[X] 家 — 持股 [X]%
□ 公募基金：[X] 家 — 持股 [X]%
□ 散户：[X]% — 持股 [X]%

【分析师覆盖】
□ 覆盖分析师：[X] 家
□ 评级分布：买入 [X]/持有 [X]/卖出 [X]
□ 目标价区间：[X] 元 - [X] 元

【近期 IR 活动】
| 活动 | 日期 | 对象 | 反馈 |
|---|---|---|---|
| [路演/业绩发布] | [日期] | [投资者类型] | [反馈摘要] |

【信息披露】（近期）
□ 披露数量：[X] 份
□ 类型：定期报告 [X]/临时公告 [X]

【投资者关切】（如有）
□ 关切事项：[描述]
□ 关切程度：[高/中/低]
□ 处理措施：[描述]
□ 跟进状态：[处理中/已解决]

【升级事项】（如有）
□ 疑似泄露事件：[描述] — 状态 [处理中]
□ 负面分析师报告：[描述] — 应对 [已回应/不回应]
```

---

## 升级条件

满足以下任一条件须立即升级：

- 疑似内幕信息泄露 → 立即升级 CEO/CFO/董秘
- 机构投资者威胁大幅减持 → CEO/CFO 关注
- 媒体负面报道广泛传播 → IR + CEO 联合应对

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| disclosure-compliance-check | 披露合规检查 |
| disclosure-content-preparation | 披露内容准备 |
| disclosure-approval | 披露审批 |
| disclosure-publishing | 披露发布 |
| roadshow-material-preparation | 路演材料准备 |
| investor-list-confirmation | 投资者名单确认 |
| roadshow-execution | 路演执行 |
| roadshow-follow-up | 路演后跟进 |
| investor-query-classification | 投资者问询分类 |
| sensitive-information-assessment | 敏感信息评估 |
| query-response-preparation | 问询回应准备 |
| query-record-filing | 问询记录归档 |
| event-ir-impact-assessment | 事件 IR 影响评估 |
| ir-response-plan | IR 应对方案 |
| communication-material-preparation | 沟通材料准备 |

---

*Finance Skills — investor-relations master skill*
