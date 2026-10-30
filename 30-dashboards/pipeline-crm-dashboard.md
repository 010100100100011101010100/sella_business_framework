# Dashboard — Pipeline & CRM

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Build when deals need tracking beyond a list |
| **Prerequisite** | `30-dashboards/dashboard-spec.md`, `20-systems/sales-and-pricing.md` |
| **Reads** | `prospects.json` · `clients.json` · `deliveries.json` · `metrics.json` |
| **Primary for** | C2, C5, C7 · secondary C3, C6, C9 |

---

## The question it answers

**"What is actually going to close, when, and what happens to us if it does not?"**

For C2 there is a second question that matters more than the first: **"how exposed are we
to one client?"** (G5).

---

## Layout

**Row 1 — the concentration warning, if it applies.** For any case with lumpy or recurring
revenue, this goes **first**, above the pipeline. Not a tile at the bottom.

```
LARGEST CLIENT     31% of trailing-90-day revenue     ceiling 40%
```

Renders as a full-width banner when over 40%. This is G5 made visible, and it is the
number an operator will otherwise never compute.

**Row 2 — stage counts with weighted value.** Not a funnel — a list of what exists.

```
REPLIED        8    —
CALL BOOKED    4    $8,400 weighted
PROPOSAL OUT   2    $18,000 weighted
WON (90d)      3    $19,600 actual
```

**Weight honestly.** A booked call is not 50% likely to close. Use *your measured* stage
conversion once you have it, and show "unweighted, no data yet" until then rather than
inventing a probability (G3).

**Row 3 — the deal table.** Company, stage, value, days in stage, next action, next action
date. **Sorted by days-in-stage descending**, so the stalled ones surface rather than the
exciting ones.

**Row 4 — stage conversion, measured.** Reply→call, call→proposal, proposal→won, with raw
counts. This is what tells you which stage is broken.

**Row 5 — active clients.** Name, offer, MRR, start date, source, next delivery due.

---

## Rules specific to this dashboard

- **Days-in-stage is the primary sort.** A deal sitting 40 days in "proposal out" is dead
  and should be closed out, not hoped over
- **Every deal has a next action with a date.** A deal without one is not in the pipeline
- **Never show a forecast as a commitment.** Weighted pipeline is an estimate; label it
- **`source` on every won client.** Three months of this beats any framework's channel
  ranking, because it is your market (`marketing.md`)
- **Show lost reasons.** Aggregate them. Two losses for the same reason is a fixable
  system problem

---

## Ten-case notes

| Case | What this dashboard is really for |
|---|---|
| **C2** | **Concentration, above everything.** One client at 70% is the case's documented killer |
| **C5** | **Calls made this week.** Sales throughput is the binding constraint, not delivery |
| **C7** | Long cycles — days-in-stage matters more than count |
| **C3, C6** | Light use. The outreach dashboard covers most of it until deals get large |
| **C9** | Referral source tracking — which accountant sends which clients |

---

## Worked example — the banner that changes a decision

**What the operator sees, C2, month four:**

```
⚠ LARGEST CLIENT   68% of trailing-90-day revenue   ceiling 40%   BREACH

CALL BOOKED    1    $9,000 weighted (unweighted — no conversion data yet)
PROPOSAL OUT   0
WON (90d)      2    $23,000

DEALS
  Company            Stage         Value    Days in stage   Next action
  Halden Systems     call booked   $9,000   3               Scoping call Thu
  Corvin Group       replied       —        19  ⚠           No next action set
```

**The three things this surfaces:**

1. **68% concentration.** Meridian is more than two-thirds of revenue. When their project
   ends — which it will, because C2 is project work — revenue drops by two-thirds with no
   warning. This is not a future risk, it is a present state.
2. **One deal in the pipeline.** With a four-week delivery and a 3–6 week sales cycle,
   there is no realistic next project unless something starts now.
3. **Corvin has sat 19 days with no next action.** That is a deal that was replied to and
   then dropped during delivery — the oscillation, visible.

**The decision:** the weekly prospecting block is not optional this week, and Corvin gets
contacted today. Note that all three findings point at the *same* underlying cause —
prospecting stopped when delivery started (`operating-cadence.md` Q3).

**What makes the banner work:** the operator was not asking about concentration. They
opened the dashboard to check on Halden. **G5 only fires if something computes it and puts
it above the thing they came to look at.**

---

**Read next:** `20-systems/sales-and-pricing.md` · `00-core/operating-cadence.md` ·
`30-dashboards/finance-dashboard.md`
