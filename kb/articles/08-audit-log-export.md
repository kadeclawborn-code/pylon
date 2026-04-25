# Audit log export

Pylon's audit log captures every administrative mutation: rule changes, config changes, permission changes, billing changes. Available on Business and Enterprise tiers.

This article covers the export workflow.

## Where to find the audit log

`app.pylon.dev/settings/audit-log`. Requires admin role on your Pylon org.

## Filtering

The audit log view supports filters:

- **Event type** — multi-select: rule_create, rule_update, rule_delete, config_change, permission_change, billing_change, etc. Full list at pylon.dev/docs/audit-event-types.
- **Actor** — multi-select user
- **Date range** — calendar pick

## In-page query window

The in-page query is capped at **30 days**. This is a deliberate cap — the audit log table grows large for active customers, and unbounded queries timeout. For windows beyond 30 days, use the export pipeline (described below).

## Export to CSV / JSON

For larger windows or for compliance-team handoffs:

1. Click **Export** on the audit log page
2. Select format: CSV or JSON
3. Set date range (no cap on the export window)
4. Submit

For exports under 10,000 rows, the file downloads directly.

For larger exports, the export runs as a background job. You'll receive an email when it's ready, with a signed link valid for 24 hours.

Typical export times:
- 10k rows: ~30 seconds
- 100k rows: ~3-5 minutes
- 500k rows: ~15-25 minutes

## CSV format

```
event_id,event_type,actor_id,actor_type,timestamp,entity_type,entity_id,details
01HX8K5Q...,rule_create,user_north_002,user,2026-01-15T14:32:00Z,rule,rule_abc123,"{""rule_id"":""northwall.compliance-currency"",""severity"":""high""}"
```

The `details` column is a JSON string. Parse appropriately in your downstream tooling.

## JSON format

```json
[
  {
    "event_id": "01HX8K5Q...",
    "event_type": "rule_create",
    "actor": {"id": "user_north_002", "type": "user"},
    "timestamp": "2026-01-15T14:32:00Z",
    "entity": {"type": "rule", "id": "rule_abc123"},
    "details": {
      "rule_id": "northwall.compliance-currency",
      "severity": "high"
    }
  },
  ...
]
```

## Retention

- **Business tier** — 1 year retention
- **Enterprise tier** — 7 years retention

Older entries are deleted from your account. We do not provide retrieval of audit log entries beyond your tier's retention window. If you need longer retention, export periodically to your own warehouse.

## SOC 2 audit use

The audit log is structured to support SOC 2 control evidence. Specifically:

- **CC6.1, CC6.2 (logical access)** — permission_change events
- **CC6.6 (system change management)** — rule_create, rule_update, rule_delete, config_change events
- **CC7.2 (system monitoring)** — entity-level mutation history

For SOC 2 Type II audits, Enterprise customers can use the **Auditor Portal** (Q3 2026; pre-orders accepted now). The Auditor Portal lets your auditor pull current evidence directly via API, with audit trails of which controls they accessed.

## Common questions

**Why don't I see my own activity in the audit log?**

The audit log captures mutations, not queries. Reading the dashboard, viewing reports, etc. don't generate events. If you're looking for "did Bea log in last week?", that's not in the audit log — try the access log (separate feature, Enterprise tier only).

**Can I delete entries?**

No. The audit log is append-only by design (Postgres-level enforcement, not just app convention). This is a SOC 2 requirement.

**Can I edit details?**

No. Same reason.

**Why does the export take so long for 500k rows?**

We stream rows server-side rather than paginating, which is the right design for large exports but slower than a single-batch fetch. The trade-off: streaming doesn't time out at our end. The 15-25 minute mark for 500k rows is at the limit of acceptable; if you have an export workflow that needs it faster, talk to support — we have an Enterprise-tier accelerator option for very large exports (Q3 2026 ship target).
