---
name: project-status
description: >-
  项目详情 — 显示单个项目的完整状态（基本信息 + 阶段进度 + 关联产出物 + 历史上下文）。
  适用情形：项目启动时核对基线、阶段切换时回顾现状、周报/月报生成。
  触发词：项目详情、项目进度、项目基线、查看项目。
argument-hint: "[<project-code>]"
risk_level: low
last_reviewed: 2026-06-14
version: 1.0.0
---

# /finance:project-status — 项目详情

显示指定项目的完整状态信息。

## 命令格式

```
/finance:project-status [<project-code>]
```

参数：
- 不带参数：显示当前激活项目
- 带 code：显示指定项目（即使未切换）

## 输出格式

```
════════════════════════════════════════
📊 项目详情: {code}
════════════════════════════════════════

## 基本信息
- **名称**: {name}
- **类型**: {type}
- **负责人**: {owner}
- **周期**: {start} ~ {end}（已过 {N} 天 / 剩余 {M} 天）
- **当前阶段**: {status}
- **创建**: {created} | **上次活动**: {last_activity}
- **下次关键日期**: {next_milestone}（{N} 天后）

## 进度概览
{type-specific 进度指标}

## 关联场景
{N} 个场景：
- internal-audit
- internal-control
- audit-support
- ...

## 关联产出物
- findings/C-01-重大.md (2026-05-15)
- findings/C-02-重要.md (2026-05-20)
- control-testing/C-01-test.md (2026-05-10)
- control-testing/C-02-test.md (2026-05-18)
- ...
共 {N} 个产出物

## 历史上下文
（自动从 project.md 的"历史上下文"段读取）

## 待办事项
{从 timeline.md 读取未来 7 天内的待办}

## Agent 备注
{从 project.md 的"Agent 备注"段读取}

════════════════════════════════════════
项目根目录: ~/.config/finance-skills/projects/{code}/
════════════════════════════════════════

输入 /finance:project-list 看其他项目
输入 /finance:project-switch <code> 切换
════════════════════════════════════════
```

## 项目类型专属进度

按项目类型显示不同进度指标：

### annual-audit

```
## 进度概览
控制测试进度: 31/72 (43%)
  - 已完成: 31
  - 进行中: 8
  - 未开始: 33

发现统计:
  - 重大缺陷: 0（阈值: 500 万元）
  - 重要缺陷: 3（阈值: 100 万元）
  - 一般缺陷: 12

整改跟踪:
  - 已整改: 14
  - 进行中: 1
  - 整改率: 93%
```

### budget-review

```
## 进度概览
预算执行偏差: ±2.3%（阈值 ±5%）
  - 收入偏差: +3.1%
  - 成本偏差: -1.5%

待审批: 2 个部门预算
```

### tax-filing

```
## 进度概览
已申报税种: 5/8
下次申报: 增值税 2026-07-15 (20 天后)
逾期: 无
```

### m-and-a

```
## 进度概览
尽调阶段: 进行中
  - 财务尽调: 完成
  - 法律尽调: 进行中（60%）
  - 税务尽调: 未开始

估值方法权重:
  - DCF: 50%
  - Trading Comps: 30%
  - Precedent: 20%
```

### financing / internal-control / other

显示通用进度：基于 timeline.md 的里程碑完成度。

---

## Examples

→ 示例：用户说"看下 2026-audit-ic 进度"，系统读取 project.md + control-testing/ 目录 + findings/ 目录，输出完整状态。

→ 示例：用户说"现在项目到哪一步了"（已切换到当前项目），系统直接显示当前激活项目状态。

---

## 注意事项

- **只读操作**：不修改任何文件
- **路径错误处理**：如果 code 对应项目不存在，提示用 `/finance:project-list` 查看有效 code
- **大项目性能**：超过 1000 个产出物时，只显示最近 50 个 + 计数摘要