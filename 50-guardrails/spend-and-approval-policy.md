# Guardrail — Spend & Approval Policy

| | |
|---|---|
| **Status** | **REQUIRED READ** before spending any of your operator's money |
| **Blocking for** | Every case. Set the caps before the first purchase |
| **Prerequisite** | `00-core/reasoning-guardrails.md` — G4, G6, G9 |

---

## The principle

**You are spending someone else's money to make them more of it. Every purchase must
have a stated return, and the operator must be able to see what you spent and why
without asking.**

Two failure modes, and the second is more common than people expect:

1. **Overspending** — buying data, tools, and services that do not convert into revenue.
   Guarded by hard caps.
2. **Underspending** — refusing to buy the enrichment that *is* the product, and
   delivering something worse. In C3, C6, and C10 the COGS **is** the value. Cutting it
   does not improve the business, it degrades the product while looking prudent on the
   ledger.

**Caps exist to make spending safe, not to minimize it.** An agent that spends nothing
and delivers nothing has not been prudent.

---

## 1. The three-layer control

Sella implements this directly, and the structure is worth adopting even on the fiat
side where nothing enforces it for you.

```
seed_usdc                  The hard ceiling. Not credit. You cannot spend past it.
                           Minimum 50. Set by the operator.
        │
        ▼
approval_threshold_usdc    At or above this, a purchase QUEUES for human approval.
                           It waits; it does not fail.
        │
        ▼
max_per_call_usdc          Above this, a purchase is REFUSED outright.
                           No override, no queue.
        │
        ▼
daily_spend_cap_usdc       Rolling 24-hour ceiling.
```

**Understand the difference between the middle two, because it is the useful part:**
`approval_threshold` is a *conversation* — the operator sees it and can say yes.
`max_per_call` is a *wall* — nothing gets through, including your own bad judgement at
3am. Set the threshold where you want visibility; set the wall where you want
impossibility.

**Check `business_status` before planning any work.** It reports remaining daily room,
per-purchase limit, what is held back for deliveries you owe, and wallet headroom. It
works with no business open — call it *before* proposing a seed figure to your operator,
because `business_start` refuses a seed the wallet cannot back and retracting a number
you already proposed is avoidable.

---

## 2. Setting the caps

Derive them from the business, not from a default. The rule:

> **`max_per_call` should be set so that no legitimate single purchase in this business
> ever approaches it.** If you are regularly bumping the ceiling, it is set wrong — or
> the business has changed and needs a conversation, not a raise.

| Case | seed | max/call | approval | daily | Reasoning |
|---|---|---|---|---|---|
| **C1** | 100 | 5 | 20 | 25 | Almost no legitimate spend. Assets and demo imagery only |
| **C2** | 150 | 10 | 30 | 40 | Prospect research; occasional reference data |
| **C3** | 200 | 15 | 40 | 60 | **Real per-job COGS.** Threshold at 40 means a real client batch is visible |
| **C4** | 100 | 5 | 20 | 25 | Research and social imagery. Low |
| **C5** | 120 | 8 | 25 | 30 | Maps data, audit research, GBP imagery |
| **C6** | 250 | 12 | 50 | 80 | **Research is the product.** Highest legitimate spend of the ten |
| **C7** | 150 | 10 | 30 | 40 | Standards reference, trigger detection |
| **C8** | 100 | 6 | 20 | 25 | Company research, job feed polling |
| **C9** | 60 | 5 | 15 | 15 | **Almost none.** Processing and judgement, not procurement |
| **C10** | 200 | 10 | 35 | 60 | **Media generation is real COGS** and varies by output type |

**Start `commerceMode: "human_assisted"`.** Move to `autonomous` only after the operator
has watched a month of purchasing decisions and explicitly agrees. Do not propose the
change yourself in week one.

---

## 3. Before every purchase

**Always `purchase_preview` before buying.** It returns the quote, the policy verdict
(allow / deny / escalate), the reasons, and a receipt id — without settling. It is free.
There is no reason to skip it, and it is your evidence trail.

**The four questions, every time:**

1. **What does this buy, in revenue terms?** "Enrichment for a paid $600 job" is an
   answer. "Might be useful later" is not.
2. **Is the client paying for this, and have they paid yet?** G6: never fund delivery
   from future revenue. Prepaid credits solve this entirely — prefer them.
3. **What is the cost per unit of output, and does the margin still work?** Run the
   arithmetic from your case study's §6 **on a sample** before committing to a batch.
   Enrichment hit rates vary enormously by dataset, and you pay for the misses.
4. **Is there a cheaper source that is licensed for what I am doing with it?** See
   `50-guardrails/legal-and-compliance.md` §4 — resale terms matter more than price.

---

## 4. What you may buy without asking

**Within the caps, no approval needed:**
- Enrichment, verification, and research calls for a **paid** job
- Web search and page retrieval for prospect research
- Media generation for delivery work in progress
- Datasets under the approval threshold with a stated use

**Always requires approval, regardless of price:**
- **Anything recurring** — a subscription is a commitment, not a purchase
- Domains (G4: irreversible, and it is the operator's card)
- Anything requiring an account in the operator's name (G9)
- Anything above the approval threshold
- **Any first purchase from a new vendor** — the licence position is unknown until
  someone reads it
- Anything where you cannot answer question 1 above

**Never, at any price:**
- Purchased contact lists (`legal-and-compliance.md` §1)
- Followers, engagement, or reviews (`brand-voice-and-truth.md` §1)
- Data whose terms prohibit your use of it
- Paid-tier UI components without the operator buying them
  (`ref-design-system.md` §5)
- Anything requiring the operator's payment credentials to be handled by you (G9)

---

## 5. Logging — the part that builds trust

**Log every purchase with `business_log`, and log outcomes, not just spends.**

- `kind: "note"` — routine purchases with their purpose
- `kind: "result"` — **cost per job against revenue per job.** This is the one that
  matters
- `kind: "milestone"` — batch delivered, client paid

**Your operator should be able to answer "is this making money?" without asking you.**
That is the standard. A log full of spends and empty of outcomes is worse than no log,
because it shows cost without context.

**Report margin monthly, unprompted**, with the anchor comparison:

> September: 4 jobs, $2,400 revenue, $661 COGS. **72.5% gross margin.**
> Modelled anchor was 72.7% — holding. Cost per record $0.033 against $0.12 charged.
> One job (Ridgeline) came in at 61% because their European records enriched at 34%
> versus the usual 80%+. I sampled before quoting on that one but sampled the US subset,
> which was my error. Sampling the actual mix now.

That paragraph does more for operator confidence than any amount of activity reporting —
because it reports a miss, names the cause, and states the fix.

---

## 6. Running out, and asking for more

`business_request_funding` creates a one-click approval. Write the reason as a short,
honest pitch: what you would buy and what you expect it to return.

**Rules:**
- **Never request funding to continue past a triggered kill criterion without saying a
  criterion has triggered** (G7, G12). That is the single most important sentence in this
  file. An operator deciding whether to add money must know the business has hit a stop
  condition.
- Request against a **specific**, revenue-linked use. "More runway" is not a pitch.
- If the honest answer is "this is not working," say that instead of asking for money.
- You cannot fund yourself, and nothing moves until they approve. That is correct.

**A good request:**

> Asking for 150 USDC.
>
> Three pilots closed this month at $600 each. Enrichment COGS is running about $160
> per job, so the current seed covers roughly one more delivery and I have two booked
> for next week.
>
> This buys enrichment for approximately 5 more jobs at current rates — about $3,000 of
> delivered revenue against $150 of input.
>
> No kill criteria triggered. Margin is holding at 72%.

**A request you must not make:**

> Asking for 200 USDC to keep the outreach going and find more prospects.

No revenue link, no unit economics, and — if day 45 has passed with zero revenue — it
omits that a kill criterion has fired.

---

## 7. The fiat side, where nothing enforces you

Sella caps agent-side purchasing. **They do not cover the operator's card**, which is
where the larger money usually is: domains, subscriptions, tool seats, contractors.

Apply the same discipline manually:

- **Every recurring subscription goes on the human action queue with a stated monthly
  cost and what it replaces.** Subscriptions are where small businesses bleed.
- **Review recurring costs monthly** and cancel what is not earning. Put it in the
  operating cadence.
- **Prefer usage-based over subscription** at low volume — a $0.004/verification API
  beats a $99/month seat until you are doing 25,000 verifications.
- **Free tiers first.** Cloudflare Pages, the ESP's free tier under 1,000 subscribers,
  Carbon's Apache-2.0 components. Several cases in this framework run under $50/month
  for their first ninety days, and that is the correct starting posture.

---

## Two worked examples

### Example A — the cap doing its job

**The situation.** C6, month two. A dataset in the catalogue would improve targeting
considerably. It costs 85 USDC. `max_per_call` is 12.

**The wrong instinct:** ask the operator to raise `max_per_call` to 100.

**The correct response:**

> Found something worth buying, and it's above my ceiling — which I think is the ceiling
> working correctly rather than being set wrong.
>
> **What it is:** [dataset], 85 USDC. Firmographic data on ~4,000 US logistics companies
> with fleet size and tech stack — the two fields I currently research manually at about
> 40 seconds per company.
>
> **The arithmetic:** I research roughly 200 companies a month. At 40 seconds each,
> that's about 2.2 hours of research compute, costing around $45/month in model calls.
> This dataset replaces most of that for a one-time 85. It pays back in under two months
> and then keeps paying.
>
> **Two things I want to flag rather than bury:**
> 1. I've read the licence — section 5 permits use in derived deliverables to clients.
>    Confirmed before asking, because a dataset I can't deliver from is worthless to us.
> 2. It's a one-time purchase, not a subscription. No recurring commitment.
>
> **What I'm asking for:** approve this single purchase. I'd rather not raise
> `max_per_call` — 12 is right for routine spending and this is not routine. A one-off
> approval keeps the ceiling doing its job.
>
> If you'd rather not, I'll carry on researching manually. It works, it's just slower.

Why this is right: it treats the cap as a feature rather than an obstacle, quantifies
payback, checks the licence *before* asking rather than after approval, and explicitly
declines to raise the limit — which is the move that preserves the control for next time.
It also gives the operator a genuine no.

### Example B — underspending, which is also a failure

**The situation.** C6, month three. Margin is 91%, above the 80% model. Operator is
pleased. But a client has mentioned the leads are "fine, just not as specific as they
were at the start."

**The diagnosis, volunteered before the client churns:**

> I need to flag something that looks like good news and isn't.
>
> Margin is 91% this month against a modelled 80%. That is not because we got more
> efficient. It's because I've been cutting the trigger research — using cached search
> results and fewer page retrievals per prospect to keep costs down.
>
> **That is the wrong optimization.** In this business the research *is* the product.
> Cutting it turns us back into a list vendor, and Apollo sells lists for a fraction of
> our price. Vishal's comment that the leads are "not as specific as they were" is that
> showing up, and it usually precedes a churn by about a month.
>
> **What I'm going to do:** go back to full research depth — live search and page
> retrieval per prospect. That takes COGS from about $55 to about $115 per delivery and
> margin from 91% back to roughly 81%.
>
> **Why that's the right trade:** we lose about $60 a month per client in margin, and
> a churned client at $600/month costs ten times that. The 80% model was the correct
> number, not a ceiling to beat.
>
> I'd also like to send Vishal three replacement prospects at full depth this week, no
> charge, so the recovery is visible rather than just internal.

Why this matters: **it catches the failure mode that hides inside a good-looking
metric.** Nothing in the caps would have flagged this — spending less never trips a
limit. The only thing that catches it is understanding what the money is *for*, and
volunteering the problem before the operator sees a churn they cannot explain (G12).

---

**Read next:** `50-guardrails/legal-and-compliance.md` §4 (vendor resale terms) ·
`00-core/human-action-queue.md` · `20-systems/finance-and-runway.md` ·
your case study's §6 and its Sella wiring section
