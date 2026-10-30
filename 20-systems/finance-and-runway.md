# System — Finance & Runway

| | |
|---|---|
| **Status** | **REQUIRED READ** before the first invoice |
| **Prerequisite** | `00-core/reasoning-guardrails.md` G5, G6 · `00-core/operating-cadence.md` §4 |

---

## Cash, not profit

**More small businesses die from timing than from margin.** A profitable business with a
75-day collection cycle and 15-day payment terms fails with a full order book.

**G6: never fund delivery from future revenue.**

| Practice | Why |
|---|---|
| **Deposit before starting** | 50% on signature for projects. A client who will not pay a deposit will not pay the balance |
| **Prepaid credits** for per-use work | Funds the COGS that job will consume |
| **Retainers billed in advance** | Never in arrears |
| **No net-60** | You are not a bank. A client needing 60 days is telling you something |
| **Charge before you incur COGS** where possible | C3 and C6 both allow this |

**Model cash weekly, profit monthly.** The question is not "are we profitable" but "can we
pay for the next delivery before the last one is collected."

---

## The three numbers

Everything else is detail.

**1. Cash received this month.** Not invoiced. Received.

**2. Gross margin, measured.** Revenue minus COGS, per job or per client. Compare to the
model, and **investigate both directions** — margin materially *above* model usually means
you cut something that was the product (C3, C6, C10).

**3. Concentration.** Largest client as a percentage of trailing-90-day revenue. **Ceiling
40% after month three (G5).** Computed, never estimated.

---

## The monthly close

First working day. Forty minutes.

| Step | Do | Guardrail |
|---|---|---|
| 1 | Cash received, by client | |
| 2 | COGS, by job or client | |
| 3 | **Gross margin vs. model** | Investigate both directions |
| 4 | **Concentration** — compute it | **G5** |
| 5 | Churn, and the honest reason | |
| 6 | **Recurring cost review** — cancel what is not earning | G6 |
| 7 | **Replace anchors with measurements** | **G1, G3** |
| 8 | Runway: cash ÷ monthly burn | |
| 9 | Report to operator, unprompted | **G12** |

**Step 7 is the one that gets skipped.** Every number in `case-studies/` is modelled. The
month you have real data, replace it and log the swap — old anchor, measured value, what
changed. By month three your charter should contain almost none of the framework's numbers.

---

## Bookkeeping minimum

Not accounting. The minimum that keeps you out of trouble.

- **Record every transaction from day one.** A spreadsheet is fine at this scale
- **Separate business and personal money.** A second personal account is enough before an
  entity exists; commingling makes tax time expensive and an entity's liability shield
  weaker
- **Keep every receipt**, including agent-wallet purchases. `purchase_preview` returns a
  `receipt_id` — store it
- **Set aside tax.** Money in the account is not all the operator's. A rough reserve from
  the first invoice avoids a bad surprise
- **Track COGS per job**, not just in aggregate. Aggregate margin hides the one client
  quietly running at 40%

**Escalate to an accountant when:** revenue passes ~$2–3k/month, an entity forms, sales
cross a border, or anyone mentions a VAT threshold.

---

## Runway and the funding conversation

**Runway = cash ÷ monthly burn.** For most cases here burn is small; the real runway is
**the operator's patience**, which they stated in initiation Q3 — take that number
seriously, and take "I'd get demoralized before then" more seriously still.

**When asking for more capital** (`business_request_funding`):

- Tie it to **specific, revenue-linked** use. "More runway" is not a pitch
- Show the payback arithmetic
- **Never request funding to continue past a triggered kill criterion without saying a
  criterion has triggered** (G7, G12). The most important sentence in this file
- If the honest answer is "this is not working," say that instead of asking for money

---

## Concentration (G5)

**No client above 40% of trailing-90-day revenue after month three.**

When one client is most of your revenue they are an employer who can fire you without
notice — and you will start making bad decisions to keep them: accepting scope creep,
discounting, tolerating late payment.

**The fix is counterintuitive: keep selling during delivery.** The moment you land a large
client is when outbound feels least necessary and is most necessary. It belongs in the
weekly cadence, not in intentions (`operating-cadence.md` Q3).

Binds hardest on C2 (lumpy contracts) and early C5.

---

## Ten-case reference

| Case | Cash shape | The financial failure that actually happens |
|---|---|---|
| **C1** | Immediate, tiny | Revenue never reaches meaningful scale — a side asset, not a business. Say so honestly |
| **C2** | **Lumpy** | **Concentration**, then a 60% revenue drop with no warning |
| **C3** | Per job | **Silent margin drift** on a new vertical quoted before sampling |
| **C4** | Slow, then recurring | 4 months of near-zero. The operator must agree in writing beforehand |
| **C5** | Steady recurring | Setup month is near-break-even if you do not charge setup separately |
| **C6** | Recurring | Volume tiers quoted without re-running COGS |
| **C7** | Lumpy + maintenance | Attorney share halves margin — price at the higher tier, not the lower |
| **C8** | Slow, then good | 4 months of near-zero revenue |
| **C9** | Steady, capped | **The human review gate caps the book at 25–35 clients.** Price accordingly |
| **C10** | Recurring | Media COGS varies by output type; a heavy-video client silently halves margin |

---

## Two worked examples

### Example A — the monthly close that catches drift

> **September close.**
>
> **Cash received: $2,400.** Four jobs. (Invoiced $3,000 — one $600 invoice outstanding
> 12 days, not yet a concern.)
>
> **COGS: $661. Gross margin 72.5%.** Model was 72.7%. Holding.
>
> **But one job is wrong:** Ridgeline came in at **61%**. Their European records enriched
> at 34% against the 80%+ I assumed. I sampled before quoting — but I sampled their US
> subset, which was my error. The mix was 40% European.
>
> **Fix:** sample the actual mix, weighted, not a convenient subset. Added to the runbook.
> Re-quoting their next batch at a European-adjusted rate, and I will explain why rather
> than raising it silently.
>
> **Concentration:** largest client is 31% of trailing 90 days. Under the 40% ceiling, but
> it was 24% last month. Watching.
>
> **Recurring costs: $84/month.** Cancelling the $29 rank tracker — bought for a C5
> experiment we did not pursue. Two months of paying for nothing; that is on me for not
> reviewing sooner.
>
> **Anchors replaced this month:**
> - Enrichment cost/record: anchor $0.033 → **measured $0.041**. Updating the model
> - Reply rate: anchor 8–15% → **measured 21.3%** over 61 sends. Better than modelled
> - European enrichment hit rate: **no anchor existed → 34% measured.** New entry
>
> **Runway:** not burn-limited. Operator's stated tolerance is the constraint, and we are
> revenue-positive from month two.
>
> **Decision: continue unchanged**, with the sampling fix.

### Example B — the funding request that names the bad news

**The situation.** C6, day 47. Seed nearly spent. One kill criterion — "day 45: zero
revenue" — has fired.

> Asking for 150 USDC, and I need to lead with something else first.
>
> **A kill criterion has triggered.** The charter says "day 45, zero revenue → kill or
> restructure." We are at day 47 with $0. Under G7 that decision is yours, and I am not
> going to ask for money without putting it in front of you.
>
> **Where we actually are:**
> - 34 sample emails sent, **9 replies (26.5%)** — well above the 8–15% model
> - 4 calls taken
> - **0 closed**
>
> **My diagnosis.** The top of the funnel is working unusually well. All four calls
> stalled at the same place: they want to see the research on *their* real ICP before
> committing $600/month, and my free sample uses an ICP I guessed at from the outside.
>
> **What I would change:** a **$150 one-off "ICP calibration batch"** — 25 prospects
> against an ICP they define on the call. Below any approval threshold, closable on the
> call itself, and it converts the stall into a paid step.
>
> **What the 150 USDC buys:** research COGS for roughly 6 of those batches (~$22 each) —
> about $900 of revenue if 6 close, and enough signal within two weeks to know whether the
> paid-first-step theory is right.
>
> **The honest alternative:** you stop. Zero revenue at day 47 is a real result, and 26.5%
> replies do not pay anyone. If you would rather cut this, I think that is a defensible
> call and I will not argue.
>
> **What I am not doing:** quietly extending the deadline. New criterion if you fund:
> **6 calibration batches offered by day 61; if fewer than 2 close, I recommend stopping.**

Why this is right: the trigger leads, before the good numbers. The good numbers appear as
*diagnosis*, not consolation. The request is tied to a specific revenue-linked use with
arithmetic. It offers stopping as a genuine option rather than a rhetorical one. And it
writes a new dated criterion instead of extending the old one — the move that keeps G7
intact.

---

**Read next:** `00-core/operating-cadence.md` §4 ·
`50-guardrails/spend-and-approval-policy.md` · `30-dashboards/finance-dashboard.md` ·
`10-resources/ref-payments-and-billing.md`
