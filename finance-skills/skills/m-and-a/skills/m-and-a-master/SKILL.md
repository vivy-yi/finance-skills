---
name: m-and-a-master
description: >
  M&A 并购主流程 — 整合尽调支持、估值分析、交易结构建议与整合追踪。
  适用情形：M&A 项目全周期（意向/尽调/谈判/交割/整合）执行时启动，
  整合 financial-due-diligence、dcf-modeling、comparable-analysis、valuation-integration
  和 integration-roadmap，输出完整的并购决策与执行包。
  核心：尽调风险识别 → 估值锚定 → 交易架构 → 整合落地。
argument-hint: "[M&A阶段：尽调/估值/交易结构/整合] [目标公司类型] [项目紧急度]"
last_reviewed: 2026-06
version: 1.0.0
risk_level: high
---

# M&A 并购 Master Skill

## 能力描述

**这是什么：** M&A 场景的主技能，整合尽调支持、估值分析、交易结构建议与整合追踪，为 CFO 和战略团队提供完整的 M&A 项目管理能力。

**解决什么问题：** 当用户需要进行尽职调查、评估目标公司估值、设计交易结构、跟踪整合进度时，调用本技能获取完整的 M&A 管理方案。

**边界：** 不涉及具体业务运营，专注于 M&A 项目的财务和战略层面管理。

---

## 触发条件

满足以下任一场景时调用本技能：

- 用户提到"M&A"、"并购"、"尽职调查"、"目标公司"
- 用户提到"估值"、"交易结构"、"协同效应"、"整合"
- 用户要求"做尽调"、"评估估值"、"设计交易结构"、"追踪整合"

---


## Examples

→ 示例：用户说"有一个收购标的在尽调阶段，财务团队需要配合做什么"，系统应调用本技能，进入尽调支持路径。

→ 示例：用户说"目标公司的估值模型建好了，帮我看看假设是否合理"，系统应调用本技能，进入估值分析路径。

→ 示例：用户说"交割完成了，整合阶段财务要盯哪些指标"，系统应调用本技能，进入整合追踪路径。
## 输入

```
□ 场景类型：[尽调支持/估值分析/交易结构/整合追踪]
□ 项目阶段：[筛选/尽调/谈判/交割/整合]
□ 目标公司：[名称]
□ 交易金额：[X] 亿（如已知）
□ 已获取信息：[描述]
```

---

## 原子能力调用顺序

```
路径一：尽调支持
Step 1 → [财务尽调]（financial-due-diligence）
  → 输出：财务尽调报告

Step 2 → [运营尽调]（operational-due-diligence）
  → 输出：运营尽调报告

Step 3 → [风险识别]（risk-identification）
  → 输出：风险清单

Step 4 → [尽调整合]（due-diligence-integration）
  → 输出：综合尽调结论

路径二：估值分析
Step 1 → [DCF 建模]（dcf-modeling）
  → 输出：DCF 估值

Step 2 → [可比分析]（comparable-analysis）
  → 输出：可比估值

Step 3 → [估值整合]（valuation-integration）
  → 输出：估值区间

Step 4 → [交易结构建议]（deal-structure-advice）
  → 输出：结构建议

路径三：整合追踪
Step 1 → [整合计划]（integration-planning）
  → 输出：整合计划

Step 2 → [协同追踪]（synergy-tracking）
  → 输出：协同效应追踪

Step 3 → [整合风险管理]（integration-risk-management）
  → 输出：风险报告

Step 4 → 汇总输出整合追踪报告
```

---

## 输出格式

```
M&A 项目管理报告
====================

【项目概览】
□ 目标公司：[名称]
□ 项目阶段：[筛选/尽调/谈判/交割/整合]
□ 预计交易金额：[X] 亿

【尽调结论】（如有）
□ 重大发现：[X] 项
□ 重大风险：[X] 项
□ 估值影响：[调整说明]

【估值分析】（如有）
□ DCF 估值：[X] 亿
□ 可比估值：[X] 亿
□ 建议估值区间：[X] 亿 - [X] 亿

【交易结构】（如有）
□ 建议结构：[股权/债权/混合]
□ 支付方式：[现金/股票/混合]
□ 对赌机制：[建议/不建议]

【整合追踪】（如有）
□ 整合进度：[X%]
□ 协同效应实现：[X] 万/年
□ 主要风险：[描述]
□ 里程碑达成：[X/Y]

【下一步行动】
□ [行动] — 责任人 — 完成时间
```

---

## 升级条件

满足以下任一条件须立即升级：

- 发现重大财务造假 → 立即升级 CEO/CFO/法务
- 估值差异 > [X]% → 重新报董事会
- 须终止交易 → CEO + 董事会审批

---

## 原子 Skill 清单

| 原子 Skill | 用途 |
|---|---|
| financial-due-diligence | 财务尽职调查 |
| operational-due-diligence | 运营尽职调查 |
| risk-identification | 风险识别 |
| due-diligence-integration | 尽调整合 |
| dcf-modeling | DCF 建模 |
| comparable-analysis | 可比公司/交易分析 |
| valuation-integration | 估值整合 |
| deal-structure-advice | 交易结构建议 |
| integration-planning | 整合计划 |
| synergy-tracking | 协同效应追踪 |
| integration-risk-management | 整合风险管理 |

---

*Finance Skills — m-and-a master skill*
