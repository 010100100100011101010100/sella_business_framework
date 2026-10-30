# Dashboards — Shared Specification

| | |
|---|---|
| **Status** | **REQUIRED READ** before building any dashboard |
| **Prerequisite** | `10-resources/ref-design-system.md`, `10-resources/ref-hosting-and-infra.md` |
| **Governs** | Every file in `30-dashboards/`. The data contract is binding |

---

## The constraints

**Client-side only. No server, no database, no authentication, no build-time API calls.**

A dashboard reads flat JSON files from the same directory and renders them in the browser.
That is the entire architecture, and it is deliberate: a dashboard is a *window*, not a
system. It must never be something that can break while nobody is watching, hold data you
did not need to store, or cost money monthly.

**Consequences:**

- **No login.** If a dashboard should not be public, it is not deployed publicly — keep it
  local, or behind the host's static access control. **Never build auth**
- **No writes.** Dashboards read. Data is written by your jobs and your work, not by
  clicking
- **Interactions are local only** — filter, sort, expand, switch date range. All in-memory
- **Works offline** from the JSON files. No external requests at runtime

---

## Step 0 — Do you need one yet?

**Almost certainly not in week one.** A dashboard over an empty file is a UI for nothing.

| Situation | Verdict |
|---|---|
| Zero prospects, zero clients | **No.** Read the JSON directly |
| Under ~30 prospects | **No.** The files are readable as text |
| Active outreach, 50+ prospects | Outreach dashboard |
| 3+ clients or recurring revenue | Finance + ops health |
| Client-facing reporting (C5, C10) | A per-client report, not a dashboard |

**Build the data files from day one. Build the dashboard when reading them stops being
easy.** The contract below matters more than any dashboard — it is what makes every later
dashboard possible without rework.

---

## The data contract · binding

All files live in `data/`. UTF-8 JSON arrays. **ISO 8601 dates.** Stable ids. Money in
minor units where possible, or explicit decimal with a stated currency.

### `data/prospects.json`
Defined in `20-systems/outreach.md`. Do not change the shape.

```json
{
  "id": "p_0142",
  "company": "Northwind Freight Systems",
  "domain": "northwindfreight.com",
  "contact_name": "Dana Whitfield",
  "title": "VP Revenue Operations",
  "email": "dana.w@northwindfreight.com",
  "email_verified": true,
  "email_verified_at": "2026-09-01",
  "trigger_tier": "A",
  "trigger": "Posted 'RevOps Manager — CRM Migration' naming a HubSpot→Salesforce move",
  "trigger_source_url": "https://northwindfreight.com/careers/revops-manager",
  "trigger_verified_at": "2026-09-02",
  "data_source": "stableenrich/people-search",
  "lawful_basis": "legitimate_interest",
  "status": "sequenced",
  "sequence_id": "seq_003",
  "opted_out": false
}
```

`status`: `researched` · `sequenced` · `replied` · `call_booked` · `won` · `lost` · `dropped`

### `data/touches.json`
```json
{
  "id": "t_0891",
  "prospect_id": "p_0142",
  "sequence_id": "seq_003",
  "step": 1,
  "channel": "email",
  "sent_at": "2026-09-03T09:14:00Z",
  "subject": "100 of your records, cleaned",
  "outcome": "replied",
  "outcome_at": "2026-09-03T16:02:00Z",
  "sentiment": "positive"
}
```

`channel`: `email` · `phone` · `linkedin` · `public_work` · `referral`
`outcome`: `sent` · `bounced` · `replied` · `opted_out` · `no_response`

### `data/clients.json`
```json
{
  "id": "c_004",
  "name": "Meridian Logistics",
  "prospect_id": "p_0089",
  "won_at": "2026-09-14",
  "source": "cold_email",
  "offer": "pilot",
  "mrr_usd": 0,
  "status": "active",
  "churned_at": null,
  "churn_reason": null,
  "dpa_signed": true,
  "data_delete_due": "2026-10-14"
}
```

`source` is the **most under-tracked and most useful field in the contract**
(`marketing.md`). Record it for every client, always.

### `data/deliveries.json`
```json
{
  "id": "d_0031",
  "client_id": "c_004",
  "kind": "pilot",
  "units": 5000,
  "unit_label": "record",
  "started_at": "2026-09-16",
  "delivered_at": "2026-09-20",
  "qa_gate": "control_total",
  "qa_passed": true,
  "qa_passed_by": "human:operator",
  "revenue_usd": 600.00,
  "cogs_usd": 164.20,
  "notes": "European subset enriched at 34%"
}
```

**`qa_passed` and `qa_passed_by` are mandatory.** For C9 the reviewer's name is the record
that the gate ran (`delivery-and-qa.md`).

### `data/transactions.json`
Append-only. Signed amounts: revenue positive, costs negative.

```json
{
  "id": "tx_0210",
  "date": "2026-09-20",
  "type": "revenue",
  "amount_usd": 600.00,
  "client_id": "c_004",
  "delivery_id": "d_0031",
  "method": "invoice_transfer",
  "received": true,
  "received_at": "2026-09-27",
  "category": null,
  "receipt_id": null
}
```

`type`: `revenue` · `cogs` · `subscription` · `one_off_cost`
**`received` distinguishes invoiced from collected. Cash is what counts (G6).**
`receipt_id` carries the Sella `purchase_preview` receipt for agent purchases.

### `data/content.json`
```json
{
  "id": "ct_0044",
  "published_at": "2026-09-12",
  "channel": "linkedin",
  "kind": "post",
  "title": "Why your CRM has more duplicates than you think",
  "url": "https://…",
  "for_client_id": null,
  "approved_by": "human:operator"
}
```

`approved_by` is mandatory for anything published in someone's name (C10, C4).

### `data/queue.json`
Machine-readable mirror of `HUMAN-ACTION-QUEUE.md`.
```json
{
  "id": "q_012",
  "title": "Buy sending domain and provide DNS access",
  "blocking": true,
  "unblocks": "All outreach. 3-week warmup starts on purchase",
  "requested_at": "2026-09-03",
  "done_at": null
}
```

### `data/metrics.json`
**Generated, never hand-edited.** Written by a scheduled job
(`40-automation/periodic-jobs.md`).

```json
{
  "generated_at": "2026-10-01T06:00:00Z",
  "window_days": 30,
  "evidence": { "sent": 61, "replied": 13, "calls_booked": 4, "won": 2 },
  "rates": { "reply_rate": 0.213, "bounce_rate": 0.016, "optout_rate": 0.000 },
  "money": {
    "revenue_invoiced_usd": 3000.00,
    "revenue_received_usd": 2400.00,
    "cogs_usd": 661.00,
    "gross_margin": 0.725,
    "gross_margin_model": 0.727
  },
  "concentration": { "largest_client_pct": 0.31, "ceiling": 0.40, "breach": false },
  "quality": { "trigger_tier_ab_pct": 0.84, "sourced_rows_pct": 1.0 },
  "blocked": { "open_items": 1, "oldest_days": 9 }
}
```

**Rules:**
- **No PII in `metrics.json`.** It must be safe to show anyone
- Every rate carries its window
- `gross_margin_model` sits beside the measured value so drift is visible in both
  directions

---

## Design

**Default stack: IBM Carbon tokens + Beautiful UI data components**
(`ref-design-system.md`). Vanilla CSS with Carbon's spacing and type scale plus IBM Plex
covers most of it with no build step.

**Beautiful UI is the best fit in the framework for an agent-run business**, specifically:
its **approval card** maps onto `queue.json` and Sella's approval threshold, its **tool
chip** maps onto logged agent actions, its **diff table** maps onto C3's before/after, and
its records/filter tables map onto `prospects.json`.

**Non-negotiables:**

| Rule | Why |
|---|---|
| **Density over whitespace** | An instrument panel, not a landing page |
| **The number that matters is the largest thing on screen** | Revenue, replies, cash |
| **Never animate data** | Animated counters make an operator distrust the numbers, correctly |
| **No dark-pattern framing** | Never colour a bad number green because it improved (G12) |
| **Show the evidence rung** | "4 replies (rung 4), 1 call (rung 5)" — not "strong interest" (G1) |
| **Pending approvals prominent** | Anything waiting on the human is the most actionable thing on the page |
| **Model beside measured** | Every rate shows its anchor, so drift is visible |
| **Windows on every rate** | "21.3% over 61 sends, last 30 days" |
| Theme-aware, responsive, tables scroll in their own container | |

---

## Ten-case reference

| Case | Build first | Then | Skip |
|---|---|---|---|
| **C1** | None — sales come from the merchant dashboard | Ops health at 200+ customers | Outreach, pipeline |
| **C2** | **Pipeline** (concentration risk) | Finance | Outreach at 1 project WIP |
| **C3** | **Outreach** | Finance (margin per job) | Marketing |
| **C4** | **Ops health** (open rate, cadence streak) | Marketing (growth) | Outreach, pipeline |
| **C5** | **Pipeline** (calls are the constraint) | Per-client reports | Marketing |
| **C6** | **Outreach + ops health** (trigger-tier quality) | Finance | Marketing |
| **C7** | Pipeline | Finance | Outreach volume |
| **C8** | **Ops health** (listing decay, open rate) | Marketing | Outreach |
| **C9** | **Ops health** (the review gate) | Finance | Outreach, marketing |
| **C10** | **Ops health** (voice validation, approvals) | Finance (COGS per client) | Outreach |

**Ops health is first for five of ten**, because the dominant failures in this framework
are gradual quality regressions — trigger tier, voice drift, listing decay, open rate,
review-gate compliance. Those need a scheduled instrument, not vigilance.

---

## Two worked examples

### Example A — declining to build one yet

**The situation.** C3, day 4. Operator: *"Can you build me a dashboard so I can see how
it's going?"*

> Not yet — and I want to give you something better in the meantime.
>
> Right now `prospects.json` has 6 rows and `touches.json` has 0. A dashboard over that is
> a UI for an empty file, and building it would cost a day I would rather spend making
> samples.
>
> **What I'm doing instead, starting today:** writing the data files properly from the
> first prospect, in the shape the dashboard will need. That is the part that would be
> expensive to retrofit. The dashboard becomes about two hours' work whenever we want it.
>
> **What you get this week:** the Friday report — evidence rung counts, spend, what is
> blocked on you, and the decision. Five lines. At this volume that is genuinely more
> useful than a chart, because with 6 prospects a chart is noise.
>
> **When I'd build it:** around 50 prospects in flight, which at current pace is week 3.
> At that point reading the raw file stops being easy and the reply-rate-by-trigger-tier
> cut starts telling us something we cannot see by eye.
>
> Flag it sooner if you'd rather have it — it is your call, I just do not think it earns
> the day yet.

### Example B — the honest metric tile

**The situation.** Building the outreach dashboard. Reply rate this week is 4.2%, down
from 21.3% last month.

**The wrong tile** — technically accurate, materially misleading:

```
REPLY RATE
21.3% ↑
```

Using the all-time figure because it looks better, with an up-arrow from an earlier
period.

**The right tile:**

```
REPLY RATE (last 7 days)          REPLY RATE (last 30 days)
4.2%  ▼ from 21.3%                 16.8%
2 replies / 48 sent                31 replies / 184 sent
model: 8–15%                       model: 8–15%
```

Both windows, both labelled. The recent drop is shown with its direction and its
comparison, not buried in a longer average. Raw counts appear beneath every rate, because
2/48 and 21/500 are different kinds of 4%. The model sits beside the measurement so drift
is visible in both directions.

**Note there is no green.** The 30-day number is above model and the 7-day number is
below; colouring either would be editorialising a number the operator can read for
themselves. **The dashboard's job is to show, not to reassure** (G12) — and an operator
who catches you flattering a number once will distrust every number afterwards.

---

**Read next:** `10-resources/ref-design-system.md` · `40-automation/periodic-jobs.md`
(generating `metrics.json`) · the individual dashboard files in this directory
