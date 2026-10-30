# Dashboard — Outreach

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Build when 50+ prospects are in flight |
| **Prerequisite** | `30-dashboards/dashboard-spec.md`, `20-systems/outreach.md` |
| **Reads** | `prospects.json` · `touches.json` · `metrics.json` |
| **Primary for** | C3, C6 · secondary C2, C7 |

---

## The question it answers

**"Is outreach working, and if not, where exactly is it failing?"**

Each failure point has a different fix, and applying the wrong one wastes weeks. The
dashboard's job is to make the failure point obvious at a glance.

```
Sent  →  Delivered  →  Replied  →  Call booked  →  Won
   ↑          ↑           ↑            ↑
 bounce   deliverability  message    offer/price
 = bad      = domain      = trigger   = too big a step
  data
```

---

## Layout

**Row 1 — the funnel, with evidence rungs (G1).** Five tiles, left to right, matching the
diagram. Each shows the count, the conversion from the previous stage, and the rung.

```
SENT        DELIVERED     REPLIED       CALL BOOKED   WON
184         181  98.4%    31  17.1%     8  25.8%      2  25.0%
            rung —        rung 4        rung 5        rung 8
```

**Row 2 — health, with thresholds shown.** Bounce, complaint, opt-out, reply rate. Each
with its window, its raw counts, and its model anchor. **Colour only on threshold breach**,
never as encouragement.

**Row 3 — reply rate by trigger tier.** The single most useful cut in the dashboard, and
the one that tells you what to research more of.

```
TIER A    24 sent   7 replied   29.2%
TIER B    91 sent  19 replied   20.9%
TIER C    69 sent   5 replied    7.2%
```

**Row 4 — the prospect table.** Filterable records table (Beautiful UI). Columns: company,
contact, title, tier, status, last touch, days since. Sortable. **Rows missing a
`trigger_source_url` are flagged** — that is a G3 compliance view, not a data-quality
nicety.

**Row 5 — sequence position.** How many prospects sit at each step, and how many are
overdue for their next touch.

---

## Rules specific to this dashboard

- **Never show open rate as a headline.** Opens are increasingly unmeasurable, and
  tracking pixels cost deliverability and create a GDPR problem (`ref-email-domain.md`).
  If shown at all, label it unreliable
- **Bounce rate above 5% renders as a full-width stop banner**, not a tile. It is an
  emergency, not a metric
- **`opted_out` prospects are excluded from every count** and shown only in a separate
  compliance view
- **Show days-since-last-touch** so stalled sequences are visible
- **Raw counts under every rate.** 2/48 and 21/500 are different kinds of 4%

---

## Ten-case notes

| Case | The cut that matters most |
|---|---|
| **C3** | Reply rate by **vertical**, not just tier — hit rates and receptiveness vary hugely |
| **C6** | **Trigger-tier percentage over time.** The month it drops from 84% to 41% is the month before churn |
| **C2** | Trigger type → call-booked rate. Which signals actually produce scoping calls |
| **C7** | Time from gap-assessment send to reply. This buyer is slow; a 3-week lag is normal |
| **C5** | **Not this dashboard.** Calls are the channel — use the pipeline dashboard |

---

## Worked example — the dashboard doing its job

**What the operator sees on a Tuesday:**

```
SENT 184   DELIVERED 181 (98.4%)   REPLIED 31 (17.1%)   CALLS 8 (25.8%)   WON 2

BOUNCE 1.6% ✓        COMPLAINTS 0.0% ✓       OPT-OUT 0.5% ✓
REPLY (30d) 17.1%  ·  model 8–15%  ·  31/181

REPLY BY TIER    A 29.2% (7/24)    B 20.9% (19/91)    C 7.2% (5/69)

⚠ 12 prospects have no trigger_source_url — compliance view
```

**The reading, in fifteen seconds:** deliverability is healthy, the message works (17.1%
against a 8–15% model), and the funnel is fine until calls-to-won.

**The two findings the layout surfaces without anyone hunting:**

1. **Tier C is dragging the average.** 69 sends at 7.2% versus tier A at 29.2%. Nearly
   40% of sends are going to prospects with weak triggers. Cutting tier C entirely would
   raise the blended rate and reduce cost — the tier ladder is doing real work and we are
   ignoring it.
2. **12 rows with no source URL.** Those triggers were not verified against an opened,
   dated page. That is a G3 exposure — if any of those triggers is wrong, we have asserted
   something we did not check to a stranger, in the operator's name. **These do not get
   sent until verified or dropped.**

**The decision it produces:** stop researching tier C, verify or drop the 12, and redirect
that research time into finding more tier-A triggers. That is a `change X because Y`
outcome for the weekly review — which is what a dashboard is for.

**What it deliberately does not do:** celebrate 17.1%. It is above model, which is worth
knowing, but the dashboard shows it beside the model and lets the operator conclude that
themselves.

---

**Read next:** `20-systems/outreach.md` · `30-dashboards/pipeline-crm-dashboard.md` ·
`50-guardrails/legal-and-compliance.md` §1
