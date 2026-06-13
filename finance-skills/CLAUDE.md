# Finance Skills — 全局配置

*首次运行时，若此文件包含 `[PLACEHOLDER]`，运行 `/finance:cold-start` 完成配置。*

---

## 公司级配置

**公司名称**：`[PLACEHOLDER]`
**所属行业**：`[PLACEHOLDER]`
**财务职能结构**：`[PLACEHOLDER] — 共享中心 SSC / 分散型 / 混合型`
**主要 ERP 系统**：`[PLACEHOLDER] — SAP / Oracle EBS / 用友 / 金蝶 / 其他`
**当前审计周期**：自然年 / 财年（起始月：`[PLACEHOLDER]`）

---

## 已安装场景

| 场景 | 状态 | 最后使用 |
|------|------|---------|
| internal-control | 未配置 | — |
| kpi-management | 未配置 | — |
| board-reporting | 未配置 | — |
| ... | ... | ... |

运行 `/finance:cold-start` 添加更多场景。

---

## 连接器状态

| Connector | 系统 | 状态 | 说明 |
|-----------|------|------|------|
| `sap_*` | SAP S/4HANA | ⚪ 未检测 | 需要配置凭证 |
| `pbi_*` | Power BI | ⚪ 未检测 | 需要配置凭证 |
| `bl_*` | BlackLine | ⚪ 未检测 | 需要配置凭证 |
| `concur_*` | SAP Concur | ⚪ 未检测 | 需要配置凭证 |

运行 `/finance:cold-start --check-connections` 检测连接器状态。

---

## 操作日志

- 审计日志：`~/.config/finance-skills/audit.log`
- 凭证目录：`~/.config/finance-skills/credentials/`（不暴露给 Agent）

---

## 项目空间

当前活跃项目：`[无]`（运行 `/finance:project-switch` 切换）

---

*Finance Skills 需要完成 cold-start 配置才能执行真实任务。*
