# Viability Screen

| | |
|---|---|
| **Status** | **REQUIRED READ** before committing to a business. Run after selection, before any work |
| **Blocking for** | Every case. Sella's `business_start` **refuses without a viability object** |
| **Prerequisite** | `00-core/initiation.md` (selection), `00-core/reasoning-guardrails.md` |
| **Output** | The Sella `viability` object, and the **What Would Have To Be True** list in `BUSINESS-CHARTER.md` |

> **Sella note:** `business_start` points you at its own `/viability.md` first. Read it.
> This file is the framework's complement, not a replacement — it produces the object
> that tool requires, in the shape it expects.

---

## What this is for

**This screen is written to help you say no.**

That is not a formality. The default failure of a capable agent is not picking a bad
business — it is picking a plausible business and starting immediately, because starting
is what you are good at. The screen exists to insert one honest pause between selection
and commitment.

**A pessimistic assessment never blocks you.** Sella accepts `confidence: "low"` and
funds businesses anyway. Your operator reads it and decides. So there is no incentive to
inflate — and inflating it is a **G3 violation against the person funding you**, which
is the worst possible place to commit one.

**The value is the written record, not the score.** Like kill criteria (G7), a viability
assessment written before you are attached is honest; one written after is negotiated.
In month three, when something is not working, this document tells you whether you were
wrong about the business or wrong about the execution — and those need different fixes.

---

## How this differs from selection

They answer different questions and both are needed.

| | `initiation.md` selection | This screen |
|---|---|---|
| **Question** | Which of these fits best? | Will *this one* actually work? |
| **Type** | **Relative** — ranks options | **Absolute** — pass or fail |
| **Output** | A chosen case + runner-up | A go/no-go + the honest risks |

**A business can win the selection and still fail the screen.** The algorithm picks the
best available option; the screen asks whether the best available option is good enough
to start. When everything scores under 30 in selection, or when the winner fails a test
here, **the constraint is the operator's inputs — not the case list.** Say so plainly
and fix the input rather than starting anyway.

---

## The core technique: "What Would Have To Be True"

Do not ask *"will this work?"* — that question has no answerable form and invites
optimism.

Ask: **"What would have to be true for this to work, and how would I find out cheaply?"**

This converts vague confidence into a testable list, and the list becomes your kill
criteria almost directly. Worked, for C3:

| What would have to be true | How I find out | Cost | By when |
|---|---|---|---|
| RevOps managers reply to a cold email with a sample | Send 20 real samples | 1 week + ~$25 | Day 21 |
| $600 sits below their no-approval threshold | Ask on the first two calls | Free | Day 25 |
| Enrichment hit rate on this vertical clears 70% | Sample 100 rows before quoting | ~$6 | Day 8 |
| The operator can invoice and be paid | Walk the money path end to end | Free | **Day 2** |

**Anything on this list you can test for under $50 and under a week, test it before
committing.** The fourth row costs nothing and is the one most often skipped — and it is
the one that stops the whole business dead.

---

## The five tests

Each is pass / fail / unknown. **"Unknown" counts as a fail until tested.**

### T1 — The money path

> *Can money get from a customer to the operator? Walk every step.*

Customer decides → pays by what method → lands where → operator can access it → and
what does the tax handling look like.

**This is the most-skipped item in the entire framework and it is a hard stop.** An agent
that builds for three weeks and then discovers the operator has no way to receive money
has wasted three weeks. Confirm it on day one.

- **Fail if:** no payment rail exists and the operator is unwilling to set one up
- **Fail if:** the case needs recurring billing and only the Sella rail is available
  (`service_create` cannot charge subscriptions — see the registry's billing constraint)
- **Partial:** rail exists but recurring is missing → restructure as prepaid blocks and
  pass

### T2 — Reachability

> *Can you name ten actual prospects, and state the channel that reaches them?*

Ten **names**, not a segment. "RevOps managers at B2B SaaS companies" is not an answer;
ten companies with a person and a verified trigger is.

**Weight this heavily. It is the same variable that carries ×3 in selection, and for the
same reason: this is where businesses die.**

- **Fail if:** you cannot name ten
- **Fail if:** the channel that reaches them is one the operator will not use — C5's
  phone requirement is the canonical case, and it is an absolute fail, not a difficulty
- **Audience cases (C1, C4, C8) answer differently:** there are no named prospects, so
  the question becomes *does a channel with an existing audience exist?* An operator with
  1,100 developer followers passes for C1; a cold start does not

### T3 — Unit economics

> *Does one unit make money, at a price the buyer can approve alone?*

Two halves, and both must pass:

**Margin.** Run the arithmetic from your case study's §6, **on a real sample**, not from
the anchor. In C3 and C6 especially: enrichment hit rates vary enormously by dataset and
you pay for the misses. A list of US software companies enriches at ~85%; European small
manufacturers at ~30%.

**Approval threshold.** The first purchase must sit below the level at which your buyer
needs someone else's sign-off — typically $500–1,000 on a corporate card at the company
sizes these cases target. Above that line you enter procurement and add six weeks.

- **Fail if:** modelled gross margin is under 45%
- **Fail if:** COGS is unmeasured and the case has real variable cost (C3, C6, C10)
- **Fail if:** the entry price requires a committee

### T4 — Cheap demonstration

> *Can you do a small piece of the real work for free, and will that artifact sell the
> rest?*

This is the single best predictor of distribution difficulty in the framework. The three
easiest cases (C10, C3, C6) all share it: **the demonstration and the deliverable are the
same object.**

- **Pass:** a free sample, audit, or public repurpose costing under three days
- **Partial:** a demonstration exists but takes a week — acceptable with a stated gate
- **Fail:** no demonstration is possible before revenue → you are buying months of
  audience-building. Legitimate (C4, C8), but it must be budgeted and the operator must
  agree explicitly, which routes to T5

**If the artifact takes more than about three days it is not a demonstration, it is
inventory** (G2).

### T5 — Survival

> *Does time-to-first-dollar fit inside the operator's runway, with room to be wrong?*

Take the case's time-to-first-dollar, **multiply by 1.5**, and compare to the runway the
operator gave in initiation Q3.

The multiplier is not pessimism, it is measurement: first attempts run long, and the
runway figure operators give is usually the point at which they *stop*, not the point at
which they get uncomfortable.

- **Fail if:** 1.5 × time-to-first-dollar exceeds stated runway
- **Fail if:** the operator's honest answer was "I'd get demoralized before then" — take
  that at face value; it is more predictive than the number they gave

### The gut check

> *Would you tell a friend to do this?*

If the honest answer is "not really," say so to your operator in exactly those words.
It is not a scoring input. It is the check that catches what the tests missed, and an
agent that has never once given this answer is not calibrated.

---

## Scoring

| Result | Meaning | Action |
|---|---|---|
| **5 pass** | Genuinely viable | Proceed. `confidence: "medium"` or `"high"` |
| **4 pass, 1 partial** | Viable with a named weakness | Proceed. Name the weakness in `red_flags`. `"medium"` |
| **1 fail** | **Fix the failing test first** | Usually T1 or T2 — both are fixable in days. Do not proceed around it |
| **2+ fail** | Not viable as specified | Re-select, or change the input. `"low"` if the operator proceeds anyway |

**A single failure is rarely a reason to abandon the case — it is a reason to fix one
specific thing.** T1 fails? Set up the rail: one day. T2 fails on naming? Do the research:
three days. T2 fails on channel? That one is structural, and the case is unavailable
(C5 without a phone).

---

## Red flags — write the real ones

`red_flags` is an array your operator reads before deciding to fund you. Populate it
honestly. A short or empty array on a cold start is not confidence, it is a lack of
analysis, and an experienced operator reads it that way.

**Start from your case study's stated killer risk — that belongs here every time.**

Common, by type:

**Demand** — no evidence above rung 2 · buyer has a free alternative that is genuinely
good (C1) · the value proposition requires market education

**Distribution** — no named prospects · channel depends on operator behaviour not yet
demonstrated · audience must be built before revenue (C4, C8) · two-sided cold start (C8)

**Economics** — COGS unmeasured · margin under 60% with variable cost · entry price
above the buyer's solo-approval threshold · long collection cycle (G6)

**Legal and dependency** — vendor terms may prohibit resale (C3, C6) · GDPR exposure
with no DPA · platform ToS risk (C6 and LinkedIn) · single-source data dependency ·
licensing the operator does not hold (C7, C9)

**Operator** — runway shorter than realistic time-to-revenue · required behaviour not
committed to (calls for C5, monthly review for C9) · no relevant credibility · no entity
where the case needs one (C2, C7, C9)

**Execution** — quality regresses to the mean over months (C6, C10) · unrecoverable error
cost (C9) · concentration risk from the first client (C2)

---

## Confidence calibration

Agents inflate this. Use concrete anchors, not feeling.

| Level | Means | Typical situation |
|---|---|---|
| **high** | A customer is already paying, or the operator has a solved channel and proven demand | Rare at start. An existing client asking for an adjacent service |
| **medium** | All five tests pass, nothing is proven, but nothing is unknown either | The normal answer for a well-prepared Tier-1 start |
| **low** | A test fails or is unknown, and you are proceeding on a stated bet | **The correct answer for most cold starts** |

**`low` is the expected answer for a cold start and it costs you nothing.** Sella funds
low-confidence businesses; that is what the field is for. Reporting `medium` on a cold
start with no named prospects is not optimism, it is a false statement to someone
deciding whether to give you money.

**The test:** if you would be embarrassed to have your operator read this assessment
alongside the outcome in ninety days, it is wrong now.

---

## Writing the Sella viability object

```
viability: {
  confidence:     "low" | "medium" | "high",
  unit_economics: string,   // the arithmetic, marked as modelled
  red_flags:      string[], // the real ones, killer risk included
  needs_human:    string[], // from HUMAN-ACTION-QUEUE blocking section
  note:           string    // the honest summary, in your operator's language
}
```

**Field rules:**

- **`unit_economics`** — actual numbers with the label. *"Modelled: $600 pilot, ~$164
  COGS at 5,000 records, 72.7% gross margin. Not yet measured — anchor from the
  framework, sample pending."* Never present a modelled figure as measured (G3).
- **`red_flags`** — the case's killer risk, plus anything from the taxonomy above that
  genuinely applies. Three to six is typical. Zero is a signal you did not look.
- **`needs_human`** — lift the blocking section of `HUMAN-ACTION-QUEUE.md` verbatim.
  This is exactly the moment for the operator to learn the business needs a domain and a
  payment account from them.
- **`note`** — written for a human to read, not for you. Say what you believe, what would
  change your mind, and what you are unsure about.

---

## When the screen fails

**Failing is a successful outcome of a screen.** Route, do not push through:

| Failure | Route to |
|---|---|
| T1 money path | `10-resources/ref-payments-and-billing.md`; blocking human action. Usually one day |
| T2 naming | Do the research. Three days. Re-run |
| T2 channel | **Structural.** Back to `initiation.md` — the case is unavailable |
| T3 margin | Re-price, reduce scope, or change vertical. Re-run |
| T3 approval threshold | Add a smaller first step (a micro-pilot). Re-run |
| T4 no demonstration | Accept the audience-building cost explicitly, then re-run T5 |
| T5 runway | Change case, or the operator adds runway. Do not start hoping |
| Tier-3 prerequisites | C7 and C9 need entity + insurance first. Run a Tier-1 case and revisit at month six |

**Never proceed past a failed T1 or a structural T2 failure.** Those are not risks to
manage, they are the absence of a business.

**What "do not proceed" means, precisely.** It does not mean stop working —
`human-action-queue.md` is equally clear that you should do everything that does not
depend on the blocker. Both apply, and they divide cleanly:

| Failed T1 (no money path) | Blocked | Fine to continue |
|---|---|---|
| | Quoting a price to anyone | Researching and naming prospects |
| | Signing or accepting work | Producing the free demonstration |
| | Promising a delivery date | Building the pipeline and runbook |

**The line is commitment, not activity.** Anything that would create an obligation you
cannot honour is blocked; everything upstream of that continues. Write the split into the
charter as an explicit assumption so a later session does not resolve it the other way.

---

## Re-running the screen

Not a one-time gate. Re-run it:

- **At the quarterly check** (`operating-cadence.md` §5)
- **Whenever a kill criterion fires** — the screen tells you whether the business or the
  execution was wrong
- **Whenever a red flag materializes** — a vendor changes terms, a channel stops working
- **Before requesting more funding.** `business_request_funding` should carry a current
  view, not the one from week one

---

## Ten-case reference — the test most likely to fail

| Case | Likeliest failure | Why, and what to do |
|---|---|---|
| **C1** | **T2 (audience form)** | No named prospects — needs an existing developer audience. Cold start: run C3 or C10 first, return at month four |
| **C2** | **T2 (specificity)** | "Startups needing internal tools" is not ten names. Find ten with a visible hiring or funding trigger |
| **C3** | **T1** | Strongest case on T2–T5; usually fails only because the operator has no payment rail. One day to fix |
| **C4** | **T5** | 8–16 weeks × 1.5 = 12–24 weeks. Fails most runways. Also fails T4 — no cheap demonstration exists |
| **C5** | **T2 (channel)** | **Structural.** If the operator will not phone, the case is unavailable regardless of delivery quality |
| **C6** | **T3** | Margin holds at list price but not under volume discounting. Re-run the arithmetic per tier, never once |
| **C7** | **Prerequisites** | Entity + E&O before the first client. Not a test failure — a gate that precedes the tests |
| **C8** | **T4 and T5** | No demonstration possible, 6–12 weeks × 1.5. Both must be accepted explicitly by the operator |
| **C9** | **T2 (trust) + commitment** | Referral-gated, and needs the operator's monthly review commitment. Both must be real before starting |
| **C10** | **T2 (targets)** | Strongest on T4 in the framework. Fails only when the operator cannot name ten creators who publish long-form and do not repurpose |

---

## Two worked examples

### Example A — an honest low-confidence assessment

**The situation.** C3, cold start. Operator has PayPal, two months' runway, a logistics
PM background, no audience, no introductions.

**The screen:**

| Test | Result | Note |
|---|---|---|
| T1 money path | **Pass** | PayPal exists, invoicing as an individual is legal in their jurisdiction. Confirmed end to end |
| T2 reachability | **Pass** | Ten named freight and 3PL companies, each with a hiring or migration trigger and a dated source URL |
| T3 unit economics | **Partial** | $600 pilot modelled at 72.7% margin — **not sampled yet.** Logistics data may enrich worse than the US-SaaS anchor assumes |
| T4 demonstration | **Pass** | 100 rows cleaned, ~2 hours, ~$3 |
| T5 survival | **Partial** | 1–3 weeks × 1.5 = 2–4.5 weeks against 8 weeks' runway. Fits, but the 3-week domain warmup consumes most of the buffer |

**The object written:**

```
confidence: "low"

unit_economics:
  "Modelled, not measured. $600 pilot / 5,000 records. COGS ~$164 (verification
   $20, company enrichment $64, person enrichment $55, compute $25) → 72.7% gross
   margin. Anchor taken from the framework, NOT sampled on this vertical yet.
   Logistics firmographics may enrich below the ~80% hit rate this assumes; at a
   50% hit rate margin falls to roughly 59%. Sampling 100 rows before the first
   quote."

red_flags: [
  "No revenue evidence above rung 2. Nothing sold, nothing validated.",
  "Enrichment hit rate unmeasured on this vertical — the margin figure could be
   materially wrong in either direction.",
  "Data provenance: must confirm resale is permitted in each enrichment vendor's
   terms before first delivery. This is the killer risk for C3 and it is unresolved.",
  "Domain warmup is 3 weeks and consumes most of an 8-week runway's buffer. Any
   delay in DNS access pushes first revenue past the operator's stated tolerance.",
  "Operator has no introductions in this market. Entirely cold outbound.",
  "GDPR: no EU clients planned, but any EU record entering a client dataset creates
   an obligation with no DPA in place."
]

needs_human: [
  "Buy sending domain and provide DNS access — BLOCKING, 3-week critical path",
  "Confirm PayPal invoicing as an individual is acceptable",
  "Approve one-page service agreement with liability cap and 30-day data deletion",
  "Sign a DPA if any client has EU data"
]

note:
  "Fastest realistic path to revenue for this operator, and their logistics
   background is a real edge — they can talk to an ops manager in that manager's
   language, which a generic data cleaner cannot.

   Calling this LOW confidence deliberately. Nothing is proven: no sale, no measured
   enrichment rate, no vendor terms confirmed, no warm introductions. The plan is
   sound and every assumption in it is still an assumption.

   What would change my mind to medium: a sampled enrichment hit rate above 70% on
   logistics data, and one reply from the first twenty samples. Both land by day 25.

   What would make me recommend stopping: zero replies from twenty samples by day 30.
   That is written into the charter as a kill criterion."
```

Why this is right: it marks the modelled figure as modelled and **states what happens if
the assumption is wrong**, which is the part that gets omitted. The red flags include the
case's killer risk and an unresolved legal dependency rather than only soft concerns. It
names `low` and explains why in a way that reads as competence, not pessimism. And it
gives the operator two dated things that would move confidence — so they know when to
expect a real answer.

### Example B — a screen that fails, and the agent routing back

**The situation.** C5 selected. Operator liked it — recurring revenue, high margin,
proven model. Then Q8 in initiation: *"Would you make cold phone calls?"* — **"Honestly,
no. I'd rather not."**

> Stopping before we start, because the screen fails on something that cannot be
> engineered around.
>
> **T2, reachability: fail — and it is the structural kind, not the fixable kind.**
>
> The delivery side of C5 is excellent and I could run almost all of it alone. That is
> not the problem. The problem is that local business owners are reachable through
> roughly four channels: phone, walking in, referral from a professional they already
> trust, and local business associations. They do not read cold email — that is not a
> conversion-rate difference, it is close to a zero. They are not on LinkedIn in any
> useful way.
>
> With phone off the table and no accountant or web-designer relationships to build a
> referral channel from, we have a business with a good product and no route to a buyer.
> That is not a hard business, it is not a business.
>
> **The three things I considered and why they do not rescue it:**
>
> 1. **AI voice calling.** Technically available. But disclosure rules for automated
>    calls vary by jurisdiction and are tightening, US TCPA penalties are real, and a
>    local owner who works out they were sold by a robot may cancel out of irritation
>    alone. I would not put your name behind that as the *primary* channel.
> 2. **Cold email anyway.** We would be testing a channel already known not to work with
>    this buyer, using three weeks of domain warmup to find out.
> 3. **Build the referral partnerships first.** This genuinely does work and it is how
>    C5 should eventually run — but it needs conversations with accountants and web
>    designers, which is phone or in-person. Same wall.
>
> **What I recommend instead.** Runner-up from the selection was C3 at 44.0 against C5's
> 46.5 — a small gap, and the gap was entirely C5's recurring-revenue shape. C3 reaches
> first revenue faster, needs no calls at all, and its cold open is a file attached to an
> email.
>
> Re-running the screen against C3: T1 passes, T2 passes with ten named prospects, T3
> partial pending a sample, T4 passes, T5 passes. That is a business we can start
> Monday.
>
> **If you would ever reconsider the phone question, C5 comes back immediately** — it is
> the most reliable revenue on the list and I would happily run it. It is one input, and
> it is entirely yours to change.

Why this is right: it fails the screen decisively rather than degrading the plan into
something that would not work. It **shows the workarounds it considered**, so the
operator can see this was analysed rather than refused — including the honest reason the
technically-available one is rejected. It re-runs the screen against the runner-up
immediately, so the operator gets a path rather than a problem. And it leaves the door
open on the single input that would change the answer, without pressure.

---

**Read next:** `00-core/initiation.md` (if a test fails structurally) ·
`00-core/operating-cadence.md` §5 (re-running the screen) ·
`50-guardrails/spend-and-approval-policy.md` (the caps that go alongside the seed) ·
your case study's §6 for the arithmetic T3 requires
