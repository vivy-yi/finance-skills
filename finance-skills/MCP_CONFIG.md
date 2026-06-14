# MCP Connector 配置说明

Finance Skills 的能力边界由 MCP Connector 决定。本文档说明 `.mcp.json` 的分层结构和场景级覆盖机制。

---

## 分层结构

```
finance-skills/
├── .mcp.json                     ← 全局：所有场景共享的 connector
├── skills/
│   ├── {scene}/
│   │   ├── .mcp.json             ← 场景级：仅该场景用，覆盖全局
│   │   ├── references/
│   │   │   └── 数据源清单.md     ← connector → 系统/字段 映射（业务侧）
│   │   └── skills/
```

**合并规则**：场景级 `.mcp.json` 与全局 `.mcp.json` 合并（同 name 时场景级覆盖全局）。

---

## 全局 `.mcp.json`

位于仓库根目录 `finance-skills/.mcp.json`，包含 **Layer 1-5** 的核心 connector：

| Layer | 类型 | 示例 |
|-------|------|------|
| Layer 1 | ERP | SAP S/4HANA、Oracle EBS、用友 NC、金蝶 K3 |
| Layer 2 | BI | Power BI、Tableau、FineReport |
| Layer 3 | 财务工具 | BlackLine、SAP Concur、Kyriba、Bloomberg |
| Layer 4 | 合规文档 | SharePoint、Workiva、Tagetik |
| Layer 5 | HR/税务/ESG | Workday、Sustainalytics、MSCI ESG |

**全局 connector 的特点**：
- 跨场景共享（90% 的财务操作都需要 SAP 的 GL/AR/AP）
- 凭证统一管理（`~/.config/finance-skills/credentials/`）

详见 [CONNECTORS.md](CONNECTORS.md)。

---

## 场景级 `.mcp.json`

位于 `skills/{scene}/.mcp.json`，仅在**该场景被触发时加载**。

### 什么时候需要场景级 connector？

**场景 A**：某个数据源**只有特定场景用**（其他场景不会调用）

```
✅ 典型例子：tax-filing 需要电子税务局 API
   → 其他 33 个场景都不会申报纳税
   → 不应该放全局（污染其他场景的 connector 列表）
   → 放 tax-filing/.mcp.json
```

**场景 B**：场景需要**特定厂商的 connector**（用户用的不是默认厂商）

```
✅ 典型例子：fx-risk 默认用 Bloomberg，但某用户只有 Refinitiv 订阅
   → 全局 .mcp.json 仍提供 Bloomberg 作为默认
   → 用户在自己的 fx-risk/.mcp.json 里加 Refinitiv
   → 优先用 Refinitiv（场景级覆盖全局）
```

**场景 C**：场景需要**高频调用的特定工具**（避免污染全局工具列表）

```
✅ 典型例子：internal-audit 需要 AuditBoard
   → 但 80% 的财务用户没有 AuditBoard 订阅
   → 放 internal-audit/.mcp.json，按需加载
```

### 什么时候**不**需要场景级 .mcp.json？

```
❌ 场景只用全局 connector（SAP GL/AR/AP + Power BI）
❌ 场景只需要 "Excel/CSV 读" fallback（全局 .mcp.json 已有）
```

---

## 场景级 `.mcp.json` 模板

最小可用模板：

```json
{
  "mcpServers": {
    "{connector-name}": {
      "type": "http" | "stdio",
      "url": "https://...",
      "description": "...",
      "auth": {
        "type": "oauth2" | "api_key" | "sso" | "...",
        "..."
      },
      "tools": ["tool_1", "tool_2"],
      "scenarios": ["this-scene"]
    }
  }
}
```

字段说明：
- `type: stdio` → 本地进程，通过 `command` 启动（如 `npx @finance-mcp/sap-connector`）
- `type: http` → HTTP API，`url` 必填
- `auth.type`：
  - `oauth2` → `client_id`/`client_secret` 走环境变量 `${CLIENT_ID}`
  - `api_key` → `header` + `value`（value 走环境变量）
  - `sso` → `provider: azure-ad | okta | google`
- `tools` → 该 connector 暴露给 Agent 的工具列表
- `scenarios` → 哪些场景会用到（应该等于 `.mcp.json` 所在目录的场景名）
- `fallback`（可选）：connector 不可用时的降级方案
  - `type: manual_csv` → 读本地 CSV（path 是相对 finance-skills 根目录）
  - `type: erp` → 用全局 ERP connector 的某工具
  - `type: manual_api` → 提示用户用 curl 命令手动调

---

## 已实现的场景级 `.mcp.json`

| 场景 | connector | 用途 | 触发场景 |
|------|-----------|------|---------|
| `tax-filing/.mcp.json` | `tax-einvoicing` + `fa-assets-system` | 电子税务局 + 本地固资台账 | 税务申报/资产折旧 |
| `fx-risk/.mcp.json` | `bloomberg-tsux` + `refinitiv-eikon` | 实时外汇/利率数据 | 外汇敞口/对冲/估值 |
| `treasury-management/.mcp.json` | `kyriba-treasury` + `auditboard-grc` | 司库执行 + SOX 控制 | 资金管理/审计/内控 |

---

## 添加新场景级 connector 的流程

```
1. 复制模板到 skills/{your-scene}/.mcp.json
2. 修改 connector name / url / auth / tools
3. 在 skills/{your-scene}/references/数据源清单.md 加一行映射
   → "Connector: {name} | 工具: {tool} | 用途: ..."
4. 在 SKILL.md 的"加载上下文"段落引用 connector name
5. 测试：python3 scripts/validate-skills.py --scene {your-scene}
6. 验证场景加载时 connector 出现在工具列表
```

---

## 凭证管理

**绝不**在 `.mcp.json` 里 hardcode 凭证。所有凭证走环境变量：

```json
"auth": {
  "type": "oauth2",
  "client_id": "${SAP_CLIENT_ID}",   // ← 从环境变量读
  ...
}
```

环境变量由 `~/.config/finance-skills/credentials/{connector}.env` 加载：

```bash
# ~/.config/finance-skills/credentials/sap.env
SAP_CLIENT_ID=xxx
SAP_CLIENT_SECRET=xxx
```

加载机制在 Cold-Start SKILL.md 的 Part 0 中实现。

---

## Connector 故障排查

| 症状 | 原因 | 解决 |
|------|------|------|
| 场景不出现某工具 | 场景级 .mcp.json 未配置 | 复制对应场景模板 |
| 工具调用 401 | 凭证过期 | 重跑 cold-start Part 0 |
| 工具调用超时 | 网络/服务不可用 | fallback 模式降级到 CSV |
| 工具名与 SKILL.md 不一致 | tools 列表漏配 | 在 .mcp.json tools 数组里加 |

详见 [CONNECTORS.md](CONNECTORS.md) Layer 分层说明。