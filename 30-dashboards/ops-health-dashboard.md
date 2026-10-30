# Dashboard — Ops Health

| | |
|---|---|
| **Status** | **REFERENCED FILE. Build this one first for five of the ten cases** |
| **Prerequisite** | `30-dashboards/dashboard-spec.md`, `20-systems/delivery-and-qa.md` |
| **Reads** | `deliveries.json` · `queue.json` · `clients.json` · `metrics.json` |
| **Primary for** | **C4, C6, C8, C9, C10** |

---

## Why this one matters most

**The dominant failures in this framework are gradual, not acute.**

Margin drift. Trigger-tier regression. Voice drift to generic. Listing decay. Open-rate
decline. Review-gate skipping.

**None of them announce themselves on any single delivery.** Each one looks fine in
isolation and only exists as a trend. Delivery gets done because a client is waiting;
quality gets done because something is watching. **Vigilance does not catch these. An
instrument does.**

That is what this dashboard is.

---

## Layout

**Row 1 — the quality gate, per case.** The single most important tile, and it shows a
**streak**, not a snapshot.

```
QA GATE — control_total           LAST 12 DELIVERIES
✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓          12/12 passed
```

For C9 this shows the **human reviewer's name** on every delivery. A delivery without a
named reviewer renders as a failure, not a blank — the gate not running is the incident.

**Row 2 — the drift trend.** One chart, the metric that regresses in *your* case, over
6–12 periods, with the model line drawn across it.

| Case | The metric that drifts |
|---|---|
| **C4** | Open rate |
| **C6** | Trigger tier A/B percentage |
| **C8** | Live-listing percentage |
| **C10** | Voice-guide validation pass rate |
| **C3** | Margin per job |
| **C9** | Review-gate compliance (must be 100%) |

**Draw the model line.** A number is only drifting relative to something.

**Row 3 — cadence streak** (C4, C8). Consecutive publishing days or weeks, and any misses.
For a publication, **cadence is the product** — a missed day is a defect, not a scheduling
detail.

**Row 4 — the human action queue.** From `queue.json`, blocking items first, sorted by
days waiting. Use Beautiful UI's **approval card** — this is the most actionable content
on the page and it maps directly onto Sella's approval threshold.

```
⚠ BLOCKED 9 DAYS   Buy sending domain and provide DNS access
                   Unblocks: all outreach. 3-week warmup starts on purchase.
```

**Row 5 — obligations with dates.** Data-deletion due dates (`data_delete_due`),
retainer renewal dates, contract end dates, listing expiry. **Anything with a date that
will embarrass you if missed.**

**Row 6 — WIP.** Deliveries in flight against the case's limit. Over the limit renders as
a warning: quality drops before throughput rises.

---

## Rules specific to this dashboard

- **Streaks, not snapshots.** A single passing gate says nothing; twelve says the process
  runs
- **A missing gate result is a failure, not a blank.** Silence is the failure mode
- **Draw the model line on every drift chart**
- **Blocked items sort by age, and age is displayed** — that is what makes staleness
  visible
- **Never hide an overdue obligation** because it is uncomfortable (G12)

---

## Ten-case notes

| Case | Build first? | The tile that earns the dashboard |
|---|---|---|
| **C4** | **Yes** | Cadence streak + open-rate trend |
| **C6** | **Yes** | Trigger-tier percentage over time |
| **C8** | **Yes** | Live-listing percentage + cadence streak |
| **C9** | **Yes** | **Review-gate compliance with reviewer names. Must be 100%** |
| **C10** | **Yes** | Voice-validation pass rate + pending client approvals |
| **C3** | Second | Margin per job; data-deletion due dates |
| **C1** | Later | Support-ticket volume; framework-version compatibility |
| **C2** | Later | Estimate vs. actual per project |
| **C5** | Later | Report-sent streak per client |
| **C7** | Later | Regulatory-sweep date; document staleness |

---

## Worked example — the tile that catches drift before the client does

**C6, month four. What the operator sees:**

```
QA GATE — trigger_verification      LAST 12 BATCHES
✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓            12/12 passed

TRIGGER TIER A/B %                              model: ≥80%
  M1  84% ────────────────────────────
  M2  79% ──────────────────────────
  M3  62% ────────────────────  ⚠
  M4  41% ─────────────  ⚠⚠

WIP  3 of 4 batches
BLOCKED  none
```

**The gate says everything passed. It is still the wrong reading, and the chart is why.**

The gate checks that every row *has* a verified trigger. It does not check that the
trigger is any *good*. Tier A/B has fallen from 84% to 41% over four months — more than
half of delivered rows now carry tier-C triggers, which are true but weak, and true-but-
weak is what a list vendor delivers.

**What happened:** COGS optimization. Cached search results, fewer page retrievals. Margin
went up. The finance dashboard showed 91% against an 80% model and flagged it; this
dashboard shows *what it cost*.

**The two dashboards together tell the whole story, and neither tells it alone.** Finance
says the margin moved; ops health says the product moved. That is the argument for
building both.

**The decision:** restore full research depth, add trigger-tier percentage to the monthly
close, and send the affected client three replacement prospects at full depth, unprompted.

**The counterfactual:** without this chart, the first signal is a client saying "not as
specific as it was" — which typically precedes cancellation by about a month, and by then
the fix is a recovery rather than a correction.

---

**Read next:** `20-systems/delivery-and-qa.md` · `20-systems/support-and-retention.md` ·
`00-core/operating-cadence.md` · `40-automation/periodic-jobs.md`
