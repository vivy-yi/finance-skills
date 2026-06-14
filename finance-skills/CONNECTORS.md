# Finance MCP Connectors

财务 Agent 的能力边界由 Connector 决定。没有连接器的 skill 只能在"知识查询"层面工作；有了连接器，Agent 才能执行真实的财务操作。

---

## 核心原则

1. **MCP over direct API** — 所有连接器通过 MCP 协议接入，不直接在 Skill 里 hardcode API 密钥
2. **Read-heavy, Write-confirm** — 读操作直接执行，写操作（过账/审批/发送）需要显式用户确认
3. **财务边界清晰** — 每个 Connector 对应一个系统域，不跨系统事务（跨系统事务由业务层处理）
4. **容错降级** — 连接器不可用时，Skill 必须有 fallback（读本地文件/让用户手动输入）

---

## Connector 分层

```
finance-skills/
├── .mcp.json                    ← Finance 全局连接器（所有场景共享）
│
skills/
├── .mcp.json                   ← 场景级连接器覆盖（如 tax-filing 额外需要税局系统）
└── {scene}/
    └── references/
        └── 数据源清单.md        ← 连接器 → 系统/字段 映射
```

---

## 全局连接器（finance-skills/.mcp.json）

### Layer 1：ERP 核心（财务数据的唯一真相来源）

| 连接器 | 用途 | 核心工具 | 适用场景 |
|--------|------|---------|---------|
| **SAP S/4HANA** | 总账/AR/AP/资产 | `sap_gl_query`, `sap_ar_age`, `sap_ap_payment`, `sap_fixed_assets` | 几乎所有 |
| **Oracle EBS / Fusion** | 总账/AR/AP/资产 | `ora_gl_query`, `ora_ar_age`, `ora_ap_payment` | 几乎所有 |
| **用友 NC/U8/Cloud** | 总账/AR/AP | `yonyou_gl_query`, `yonyou_ar`, `yonyou_ap` | 国内企业 |
| **金蝶 K3/Cloud** | 总账/AR/AP | `kingdee_gl_query`, `kingdee_ar`, `kingdee_ap` | 国内企业 |

### Layer 2：BI & 分析层（从 ERP 拉数据做分析）

| 连接器 | 用途 | 核心工具 | 适用场景 |
|--------|------|---------|---------|
| **Power BI** | 管理报表/仪表板 | `pbi_datasets_refresh`, `pbi_report_export`, `pbi_data_query` | 管理报告/董事会/KPI |
| **Tableau** | 可视化分析 | `tableau_views_query`, `tableau_workbook_export` | 分析/商业洞察 |
| **FineReport / 帆软** | 国内 BI | `finereport_query`, `finereport_export` | 国内企业 |
| **Excel / CSV** | 本地数据 | `excel_read`, `excel_write` | 所有场景的 fallback |

### Layer 3：财务工具层（执行层）

| 连接器 | 用途 | 核心工具 | 适用场景 |
|--------|------|---------|---------|
| **BlackLine** | 账户对账/关账 | `bl_account_recon`, `bl_task_status`, `bl_variance_query` | 月结/内控 |
| **SAP Concur** | 差旅报销 | `concur_expense_list`, `concur_approval_submit`, `concur_policy_check` | 费用审查 |
| **Expensify** | 费用报销 | `expensify_report_list`, `expensify_policy_check` | 费用审查 |
| **Kyriba** | 司库/现金流 | `kyriba_cash_positions`, `kyriba_forecast`, `kyriba_bank_statements` | 司库/外汇 |
| **GTreasury (Finastra)** | 司库 | `gt_cash_query`, `gt_fx_deals`, `gt_forecast` | 司库 |
| **Bloomberg (TSOX)** | 外汇/市场数据 | `bloomberg_fx_rate`, `bloomberg_equity_quote`, `bloomberg_bond_analytics` | 外汇/融资 |
| **Refinitiv Eikon** | 市场数据 | `refinitiv_fx_rate`, `refinitiv_company_data` | 外汇/ESG/投资 |
| **Capital IQ (LSEG)** | M&A/股权数据 | `ciq_company_profile`, `ciq_transaction_search`, `ciq_valuation_metrics` | M&A/投资/可比分析 |
| **Wind (万得)** | 国内金融数据 | `wind_equity_quote`, `wind_bond_analytics`, `wind_macro_data` | 国内M&A/投资/宏观 |
| **AuditBoard** | SOX/内控管理 | `ab_control_testing`, `ab_finding_tracker`, `ab_audit_plan_status` | 内部控制/内部审计 |

### Layer 4：合规 & 文档层

| 连接器 | 用途 | 核心工具 | 适用场景 |
|--------|------|---------|---------|
| **SharePoint** | 财务文档库 | `sp_finance_library_read`, `sp_finance_library_write` | 所有文档管理 |
| **Google Drive** | 财务文档库 | `gdrive_finance_folder_read`, `gdrive_finance_folder_write` | 所有文档管理 |
| **Workday Adaptive Planning** | 预算/预测 | `workday_budget_query`, `workday_forecast_upload` | 预算管理 |
| **Anaplan** | 企业计划 | `anaplan_model_run`, `anaplan_data_export` | 预算/资本配置 |
| **Tagetik / CCH Tagetik** | 合并报表/关账 | `tagetik_close_status`, `tagetik_journal_entry`, `tagetik_intercompany_elimination` | 合并报表/财务关账 |
| **Workiva** | SOX/披露管理 | `workiva_control_docs`, `workiva_disclosure_checklist`, `workiva_workflow_status` | SOX合规/监管披露 |

### Layer 5：HR & 税务（边界系统）

| 连接器 | 用途 | 核心工具 | 适用场景 |
|--------|------|---------|---------|
| **Workday HCM** | 薪酬/人力成本 | `workday_payroll_query`, `workday_headcount_export` | 薪酬/预算 |
| **BambooHR** | 中小HR | `bamboohr_employee_list`, `bamboohr_time_off` | 薪酬 |
| **ADP** | 薪资 | `adp_payroll_report`, `adp_tax_withholding` | 薪酬 |
| **TaxDome** | 税务文档 | `taxdome_client_portal`, `taxdome_document_upload` | 税务 |
| **Vertex / Sovos** | 税务计算 | `vertex_quote_request`, `vertex_jurisdiction_lookup` | 税务 |

### Layer 5 扩展：ESG & 投资者关系

| 连接器 | 用途 | 核心工具 | 适用场景 |
|--------|------|---------|---------|
| **Sustainalytics** | ESG 评级/风险 | `sust_ESG_rating`, `sust_controversy_alert`, `sust_benchmark_rank` | ESG 报告/投资者关系 |
| **MSCI ESG Research** | ESG 数据 | `msci_ESG_score`, `msci_ISSgovernance`, `msci_climate_metric` | ESG 报告/合规披露 |
| **Bloomberg ESG** | ESG 数据集成 | `bloomberg_ESG_excel`, `bloomberg_ESG_score`, `bloomberg_sustainability_analytics` | ESG 报告/资本配置 |
| **Diligent (Board Portal)** | 董事会管理 | `diligent_board_meeting`, `diligent_resolution_vote`, `diligent_document_signoff` | 投资者关系/董事会 |
| **Q4 (IR Platform)** | 投资者关系 | `q4_earnings_calendar`, `q4_press_release`, `q4_analytics_dashboard` | 投资者关系 |

---

## 场景级连接器（skills/{scene}/.mcp.json）

### tax-filing 额外需要

```json
{
  "mcpServers": {
    "TaxDome": {
      "type": "http",
      "url": "https://api.taxdome.com/api/mcp",
      "description": "Tax document management — client portals, filing status, document exchange"
    },
    "Vertex-O系列": {
      "type": "http",
      "url": "https://vertex-corporate.company.com/api/mcp",
      "description": "Indirect tax calculation — sales tax, VAT, goods & services tax"
    }
  }
}
```

### treasury-management / treasury-advanced 额外需要

```json
{
  "mcpServers": {
    "Bloomberg TSOX": {
      "type": "stdio",
      "command": "python -m bloomberg_connector",
      "description": "Real-time FX rates, interest rates, market data for treasury"
    },
    "Kyriba": {
      "type": "http",
      "url": "https://{company}.kyriba.com/mcp",
      "description": "Cash visibility, forecasting, bank account management, payment factory"
    }
  }
}
```

---

## 数据源清单.md 中的 Connector 映射

每个场景的 `references/数据源清单.md` 必须包含 **Connector 映射表**：

```markdown
## 系统连接状态

| 优先级 | 系统 | Connector | 状态 | 说明 |
|--------|------|-----------|------|------|
| 1 | SAP S/4HANA | `sap_*` | ✅ 已配置 | GL/AR/AP/FA |
| 2 | Power BI | `pbi_*` | ⚪ 未配置 | Board 视图 |
| 3 | BlackLine | `bl_*` | ❌ 不可用 | 月结对账 |
| 4 | Concur | `concur_*` | ⚪ 未配置 | 差旅报销 |

## Connector → 字段映射

| 数据需求 | Connector | 工具 | 字段 |
|---------|-----------|------|------|
| 总账余额 | SAP | `sap_gl_query` | `RACCT`, `HSLVT`, `KUNNR` |
| 应收账款账龄 | SAP | `sap_ar_age` | `KUNNR`, `NAME1`, `DATAB`, `DATAS` |
| 预算执行 | Power BI | `pbi_datasets_refresh` | `Budget vs Actual` dataset |
```

---

## 连接器不可用时的 Fallback 策略

每个 Skill 必须声明当 Connector 不可用时的降级路径：

```markdown
## Fallback

如果 `sap_gl_query` 不可用：
1. 尝试 `yonyou_gl_query`（国内 ERP 备选）
2. 让用户提供 CSV/Excel 导出
3. 提示用户手动输入金额

如果 `pbi_report_export` 不可用：
1. 尝试 `tableau_views_query`
2. 手动从 BI 系统截图/导出
3. 用上一次缓存的数据，标注"数据时间戳"
```

---

## 连接器安全规范

- **凭证存储**：所有 API 密钥存储在 `~/.config/finance-skills/credentials/`（不对外暴露）
- **只读优先**：连接器默认配置为只读；写操作（过账/审批）需要额外确认步骤
- **审计日志**：所有连接器调用记录到 `~/.config/finance-skills/audit.log`
- **幂等性**：读操作天然幂等；写操作必须 idempotency key 防止重复执行
