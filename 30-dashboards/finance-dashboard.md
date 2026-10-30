# Dashboard — Finance

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Build once there is revenue from more than one client |
| **Prerequisite** | `30-dashboards/dashboard-spec.md`, `20-systems/finance-and-runway.md` |
| **Reads** | `transactions.json` · `deliveries.json` · `clients.json` · `metrics.json` |

---

## The question it answers

**"Did we get paid, did we keep any of it, and can we afford the next delivery?"**

Cash, not profit (G6). The distinction is the point of the dashboard.

---

## Layout

**Row 1 — cash, three tiles, in this order:**

```
RECEIVED (30d)      INVOICED, UNPAID       GROSS MARGIN
$2,400              $600  · 12 days        72.5%  · model 72.7%
```

**Received comes first, always.** Invoiced money is not money. The unpaid tile shows the
oldest outstanding age, because that is the number that predicts a collection problem.

**Row 2 — margin per delivery.** A table, not an average. Aggregate margin hides the one
job quietly running at 40%.

```
Delivery         Client        Revenue   COGS     Margin
d_0034           Ridgeline     $720      $281     61%  ⚠
d_0033           Northwind     $600      $151     75%
d_0031           Meridian      $600      $164     73%
```

**Flag any delivery more than 10 points below model, in either direction.** Above-model
margin is a warning too — in C3, C6, and C10 it usually means you cut something that was
the product (`support-and-retention.md` Example B).

**Row 3 — recurring costs.** Every subscription, its monthly cost, and when it was last
reviewed. **Sorted by last-reviewed, oldest first.** Subscriptions are where small
businesses bleed, not through one bad decision but through six reasonable ones nobody
revisits.

**Row 4 — agent spend.** Daily cap used, seed remaining, spend per delivery, and pending
approvals. Pull from `business_status` / `budget_status`.

**Row 5 — anchor vs. measured.** Every planning anchor still in use, its measured
replacement if one exists, and the date of replacement. **Unreplaced anchors after 60 days
are flagged** — planning against fiction into month four is a real failure mode (G1, G3).

---

## Rules specific to this dashboard

- **Received ≠ invoiced.** Never show a single "revenue" number that blurs them
- **Per-delivery margin, never only the average**
- **Flag margin drift in both directions**
- **Never colour a bad number green because it improved** (G12)
- **Show the tax reserve** if the operator is setting one aside. Money in the account is
  not all theirs
- **No forecasting.** This dashboard reports what happened. A weighted pipeline lives on
  the pipeline dashboard and is labelled an estimate

---

## Ten-case notes

| Case | The number that matters most |
|---|---|
| **C1** | Net per sale after merchant-of-record fees — not gross price |
| **C2** | **Concentration** (on pipeline) + estimate-vs-actual per project |
| **C3** | **Margin per job**, and per vertical. The drift is silent |
| **C4** | Sponsor revenue vs. subscription revenue, tracked separately |
| **C5** | Setup-month margin vs. steady-state. Setup is near break-even if not charged separately |
| **C6** | **COGS per delivery**, watched for downward drift as hard as upward |
| **C7** | Margin with and without the attorney share — they are different businesses |
| **C8** | Revenue per issue against subscriber count |
| **C9** | **Revenue per reviewer-hour.** The gate caps the book at 25–35 clients |
| **C10** | **COGS per client.** A heavy-video client silently halves margin |

---

## Worked example — the tile that catches silent drift

**Month three, C6. What the operator sees:**

```
RECEIVED (30d)     INVOICED, UNPAID     GROSS MARGIN
$1,800             $0                   91.2%  · model 80.9%  ⚠ +10.3

MARGIN PER DELIVERY
  d_0041   Vishal Media   $600   $52    91.3%  ⚠
  d_0040   Corvin Group   $600   $55    90.8%  ⚠
  d_0039   Halden         $600   $51    91.5%  ⚠
```

**An operator reading a normal dashboard sees three green numbers and a business
outperforming its model.** This one flags all three.

**Why the flag is correct:** COGS should be ~$115 per delivery, of which roughly 70% is
trigger research. At $52 the research is not happening at full depth — cached search
results, fewer page retrievals. Margin went up because **the product got worse.**

In C6 the research *is* the product. A list with a thin sentence attached is a worse
Apollo at ten times the price, and the client notices in month four with "not as specific
as it was" — about a month before they cancel.

**The arithmetic the flag forces:** restoring depth costs ~$63/delivery, so ~$189/month
across three clients. A churned client at $600/month costs three times that in the first
month alone.

**What makes this work is the `gross_margin_model` field in the contract.** Without a model
sitting beside the measurement, 91% is unambiguously good news. With it, the gap is a
question — and the question is the whole value of the dashboard.

---

**Read next:** `20-systems/finance-and-runway.md` ·
`50-guardrails/spend-and-approval-policy.md` · `00-core/operating-cadence.md` §4
