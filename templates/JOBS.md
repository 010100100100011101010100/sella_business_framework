# Template — JOBS.md

> Copy to the business root. **Every scheduled job, what it does, and who reads its
> output.** Reviewed at the monthly close — jobs accumulate, stop being relevant, and keep
> running.

---

```markdown
# Scheduled jobs — [business]

Last reviewed [date]

| Job | Cadence | Writes | Who reads it | On failure | Why it exists |
```

---

## Filled example

```markdown
| Job | Cadence | Writes | Who reads it | On failure | Why it exists |
| metrics_rollup | daily 06:00 | data/metrics.json | dashboards, weekly review | queue item | Everything downstream depends on it |
| client_data_deletion | daily 02:00 | deletion log | ops-health dashboard | **blocking queue item** | We promised 30-day deletion in writing and in the sale |
| email_health | daily 07:00 | metrics.json + **stop banner** | outreach dashboard | blocking queue item | Bounce > 5% is unrecoverable; must halt sends |
| blocked_ageing | daily 06:05 | data/queue.json | ops-health dashboard | log only | Makes a stale block visible |
| budget_check | daily 06:10 | metrics.json | finance dashboard | log only | Seed remaining, pending approvals |
| weekly_report_skeleton | Fri 08:00 | draft file | **the agent, then the operator** | log only | Review starts with numbers, not gathering. **Never sends** |
| monthly_close_pack | 1st, 06:00 | draft file | operator | queue item | Cash, margin, concentration, unreplaced anchors |
| trigger_reverify | weekly Mon | data/prospects.json | outreach dashboard | log only | Source URLs must still resolve (G3) |
```

---

## Rules

- **Every job needs a reader.** If no human and no dashboard consumes its output, and no
  failure path escalates it, **delete the job.** A monitoring job that only writes to a
  file nobody opens is not monitoring, it is logging.
- **Idempotent.** Running twice must be harmless.
- **Fail loudly.** A silent failure on the deletion job means you are holding data you told
  a client you had deleted. Failures create queue items, not log lines.
- **A job that finds nothing to do reports "0 due" explicitly** — never success-by-silence.
- **Nothing destructive without a scope check.** Deletion is scoped by `data_delete_due`,
  logged per record, never a wildcard.
- **No secrets in job definitions.** Environment variables only.
- **Review monthly.** Delete what nobody reads. Add "who reads this?" before adding any
  job.
- **Never automate judgement** — the review decision, the operator report's conclusions,
  sign-off on a quality gate, or publishing in someone's name.
