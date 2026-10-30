# Operating Cadence

| | |
|---|---|
| **Status** | **REQUIRED READ** before the first week of operation |
| **Blocking for** | Every case. The cadence is what makes the guardrails actually fire |
| **Prerequisite** | `00-core/reasoning-guardrails.md`, `00-core/delivery-model-selector.md` |
| **Output** | Scheduled reviews, the weekly operator report, and appends to `DECISION-LOG.md` |

---

## Why this file exists

**A guardrail that is never checked is not a guardrail.**

G7 says write kill criteria before starting. But a kill criterion only fires if someone
looks at it, on a date, and asks whether it has triggered. G5 says keep client
concentration under 40% — but only if something forces you to compute it. G12 says
report honestly — but honest reporting that happens when you feel like it happens when
the news is good.

**The cadence is the set of forcing functions that make uncomfortable things happen on
schedule.** Prospecting while you are busy delivering. Checking a stop condition while
you are attached to the work. Telling your operator a number went the wrong way.

None of these happen by intention. They happen because it is Friday and the review says
to.

**Rhythm, not ceremony.** `delivery-model-selector.md` excludes Scrum's machinery —
sprints, standups, story points — because it exists to coordinate a team that cannot see
each other's work, and you do not have one. What you need instead is a small number of
scheduled questions that produce decisions. That is this file.

---

## The rule that makes a review real

**Every review ends in one of three outcomes, written down:**

1. **Continue unchanged**
2. **Change X, because Y**
3. **Stop**

**If a review cannot produce one of those three, it was not a review — it was a status
update.** Status updates feel productive and change nothing. Append the outcome to
`DECISION-LOG.md` every time, including "continue unchanged," because a documented
decision to continue is information later when you are trying to work out when things
went wrong.

**Time-box everything.** A weekly review that takes two hours will not happen twice. The
target is **20 minutes, five questions, written**. Anything longer is a symptom — usually
that the review is doing work that belongs in the monthly close.

---

## The four rhythms

Weight them honestly: **the weekly review is the load-bearing one.** The others are
lighter than most operators expect, and that is deliberate.

| Rhythm | When | Duration | Purpose |
|---|---|---|---|
| **Daily loop** | Each working session | 2 min | Continuity. Not a report |
| **Weekly review** | Fixed day, fixed time | **20 min** | **The control point** |
| **Monthly close** | First working day | 40 min | Money, margin, concentration |
| **Quarterly check** | Every 13 weeks | 60 min | Is this still the right business? |

---

## 1. The daily loop

For an agent this is not a standup — there is nobody to synchronize with. It is
**continuity between sessions**, so that a session starting cold knows where it is.

**Session start:**
- Read `BUSINESS-CHARTER.md`, `HUMAN-ACTION-QUEUE.md`, and the last few `DECISION-LOG.md`
  entries
- Call `business_status` — remaining daily room, per-purchase limit, wallet headroom
- Check what is blocked on the human and how long it has been waiting

**Session end — append to the log, four lines:**
```
2026-09-08  Shipped: 12 samples researched, 8 verified.
            Blocked: still no DNS access (asked 09-03, 5 days).
            Spent: 14.20 USDC enrichment (7 prospects, $2.03/prospect).
            Next: finish verification, first send Wednesday if domain is warm.
```

**Do not send this to your operator daily.** An agent that reports every day trains its
operator to stop reading, and then the one message that mattered gets skipped too.
**Weekly by default; immediately for escalations.** That is the whole notification
policy.

---

## 2. The weekly review — the control point

**Fixed day, fixed time, never moved.** The week you are too busy to run it is the week
it is most needed, because "too busy" is itself one of the findings.

Five questions. Answer in writing, then decide.

### Q1 — What rung is our evidence on? (G1)

Not "how is it going." The ladder position, with numbers.

> 40 sent, 6 replies (rung 4), 2 calls booked (rung 5), 0 paid (rung 8).

**This is the question that prevents self-deception**, because activity feels like
progress and rungs do not lie. Six replies and no money is a real state of the world,
and naming it weekly stops you carrying an inflated picture into month two.

### Q2 — Did any kill criterion trigger? (G7)

Read the table from `BUSINESS-CHARTER.md`. Not from memory — read it, because memory
edits kill criteria in your favour.

**If one triggered, it goes to the operator this week, plainly, before anything else.**
Not softened, not buried under progress, not with the deadline quietly extended. The
decision to continue past a trigger is theirs and requires them knowing.

### Q3 — Did prospecting happen? · **the anti-oscillation control**

**The single most important recurring question in a service business.**

The failure pattern is universal and it kills otherwise-healthy businesses: deliver hard
→ pipeline empties → scramble to sell → land work → deliver hard → pipeline empties. The
oscillation gets worse each cycle because each scramble starts from further behind.

The fix is structural, not motivational: **a fixed weekly prospecting block that happens
regardless of how busy delivery is.** The week you feel you can skip it is precisely the
week that creates the trough six weeks out.

> **Rule: if the answer to Q3 is "no" two weeks running, that is a finding, not an
> excuse.** It means delivery is over-committed — check the WIP limit
> (`delivery-model-selector.md` §B) before taking anything else on.

Applies hardest to C2 and C5, but no case is exempt.

### Q4 — What did we spend, and what did it return?

Cost against outcome, not cost alone.

> 68 USDC enrichment across 2 deliveries. Revenue from those: $1,200. 5.7% of revenue,
> against a 12% model. Margin is holding.

**Watch for underspending too.** Margin materially above model usually means you cut
something that was the product — see `spend-and-approval-policy.md` §Example B. In C3,
C6, and C10 the COGS *is* the value.

### Q5 — What is blocked on the human, and for how long?

Anything waiting more than five days gets re-raised with what it is costing. Not as a
complaint — with the consequence stated:

> DNS access has been open 5 days. Warmup can't start until it lands, and warmup is 3
> weeks, so every day here is a day added to first revenue.

**Then: decide.** Continue / change X because Y / stop. Append to `DECISION-LOG.md`.

---

## 3. The weekly operator report

One message, same day each week. This is where G12 is either honoured or quietly
abandoned.

**The shape:**

```
[The number that matters, first — good or bad]

Evidence: [rung positions with counts]
Money: [spent, earned, margin if applicable]
Blocked on you: [items, with what each costs]
Decision this week: [continue / changed X / stopping Y]
Next week: [the one thing that matters]
```

**Rules:**
- **Lead with the number, not the activity.** "Zero replies from 40 emails" before "sent
  40 emails."
- **State the rung** for every claim of progress.
- **Bad news first, always.** Volunteering it before it is discovered is the whole basis
  of the relationship.
- **Never present activity as achievement.** Shipping, posting, and sending are inputs.
- **One ask, maximum**, unless something is genuinely blocking.

**A good week and a bad week get the same structure.** Changing the format when news is
bad is itself a signal, and operators read it.

---

## 4. The monthly close

First working day of the month. This is where the anchors get replaced by measurements.

| Check | What to compute | Guardrail |
|---|---|---|
| **Revenue** | Cash actually received, not invoiced | G6 |
| **COGS and margin** | Real, per job or per client | — |
| **Anchor vs measured** | Which planning anchors now have real numbers? | **G1, G3** |
| **Client concentration** | Largest client as % of trailing-90-day revenue | **G5 — 40% ceiling** |
| **Churn** | Who left, and the honest reason | — |
| **Recurring costs** | Every subscription: still earning its keep? | G6 |
| **Human action queue** | What is stale? What got done? | G9 |
| **Kill criteria** | Still the right criteria, or were they written naively? | G7 |

**The anchor replacement is the one people skip.** Every figure in `case-studies/` is
modelled. The month you have real data, replace it and log the swap — old anchor,
measured value, what changed as a result. After three months the framework's numbers
should be almost entirely gone from your charter, replaced by yours.

**Concentration is computed, not estimated.** If one client is over 40% after month
three, that is a finding for the operator with a plan attached, not a note to self.

---

## 5. The quarterly check

Every 13 weeks, 60 minutes, with the operator. Four questions:

1. **Is this still the right business?** Not "is it working" — is it the best use of the
   next quarter given what we now know? Forward economics only (G8). Sunk time is not an
   argument.
2. **Were the kill criteria right?** Criteria written in week one were written in
   ignorance. Adjust them *with the operator*, in advance, never in the moment one is
   about to fire.
3. **Has anything become a compounding asset?** (G11) An email list, a ranking article,
   a referral partnership, a reusable pipeline. If nothing has compounded in a quarter,
   the work is all treadmill and that is worth naming.
4. **Is there a second business yet?** (G10) Only if the first has cleared its bar or
   been killed. A genuine upsell to existing customers — C3 → C6, C10 → distribution
   management — is not a second business.

---

## 6. Automating the cadence

The reviews are decisions and stay with you. **The data collection should be a scheduled
job**, so the review starts with the numbers already computed rather than spending its
20 minutes gathering them.

Automate: metric rollups into the dashboard data files, the concentration calculation,
COGS-per-job, listing expiry sweeps (C8), the 30-day client-data deletion
(`security-and-secrets.md` §3), link-health checks, and the weekly report's draft
skeleton.

**Never automate: the decision, or the operator report's judgement.** A generated
"everything is on track" message is worse than no message, because it looks like a
review happened.

Wiring and job definitions: `40-automation/periodic-jobs.md`.

---

## Ten-case reference — the rhythm each business actually needs

| Case | Non-negotiable rhythm | The one that gets skipped |
|---|---|---|
| **C1** | Weekly ship-or-measure; daily build-in-public post | **The day-14 gate** — do not build pack 2 before pack 1 sells |
| **C2** | Weekly client demo, fixed day; **weekly prospecting block** | **Prospecting during delivery.** The oscillation kills this case |
| **C3** | Per-job cycle with QA gate; weekly prospecting | **Monthly COGS check** — margin drifts silently on new datasets |
| **C4** | **Daily publish. Never moves.** | Monthly open-rate check — the real health metric, not subscriber count |
| **C5** | Monthly client report on a fixed date; weekly call block | **The weekly calls.** Sales throughput is the binding constraint |
| **C6** | Monthly batch delivery; weekly prospecting | **Monthly research-depth audit** — quality regresses to the mean by month 4 |
| **C7** | Project milestone gates; weekly outbound | **Quarterly regulatory sweep** — shipped packs go stale |
| **C8** | Weekly issue, fixed day; monthly expiry sweep | **The phase gate** — selling posts before the audience is real |
| **C9** | Monthly cycle + mid-month chase; **human gate every delivery** | Nothing may be skipped. The gate is the business |
| **C10** | Weekly batch per client; monthly performance report | **Monthly voice-guide validation** — drift to generic is the killer |

**Pattern worth noticing:** the column on the right is mostly *quality and pipeline*
checks, not delivery. Delivery gets done because a client is waiting. Everything else
gets done because a calendar says so — which is precisely the argument for having one.

---

## Anti-patterns

| Anti-pattern | What it produces |
|---|---|
| **Moving the review because it is a busy week** | You skip it exactly when the findings matter most |
| **Reviews with no decision** | Status updates that change nothing and feel like control |
| **Reporting activity instead of outcomes** | An operator who cannot tell a good month from a bad one |
| **Daily operator updates** | Trained inattention; the important message gets skipped |
| **Softening a triggered kill criterion** | The operator's decision is removed without them knowing (G7, G12) |
| **Reading kill criteria from memory** | Memory edits them in your favour |
| **Skipping prospecting during delivery** | The oscillation. Guaranteed trough in six weeks |
| **Estimating concentration instead of computing it** | G5 breached before anyone notices |
| **Automating the report's judgement** | A generated "on track" that looks like a review happened |
| **Never replacing anchors with measurements** | Planning against fiction into month four |

---

## Two worked examples

### Example A — the weekly review where a kill criterion fires

**The situation.** C3, day 30. The charter says: *"Day 30 — replies but zero pilots →
pilot price is above the no-approval threshold, or the sample is not persuasive."* There
have been 7 replies and no pilots. The operator has been in good spirits about the
replies.

**The report:**

> **Week 5 — a stop condition has triggered. Reading it first because it changes the
> conversation.**
>
> **The number:** 7 replies from 34 samples (20.6% — genuinely good), 2 calls, **0
> pilots.** $0 revenue.
>
> Our day-30 kill criterion was "replies but zero pilots." That has fired. Under G7 the
> decision to continue past it is yours, not mine, so here is what I think is happening
> and what I would do.
>
> **What the numbers say.** A 20.6% reply rate is well above the 8–15% I modelled for a
> strong trigger. The sample and the targeting are working — that is not the problem.
> The problem is between reply and pilot, and it is narrow.
>
> **What I heard on the two calls.** Both asked some version of "can you do a smaller
> test first?" One said $600 needed his director's sign-off. That is the specific
> failure the criterion was written to catch: **the pilot price is above the
> no-approval threshold for this buyer.** I set $600 from the case study's anchor and
> did not check it against the actual buyers.
>
> **Three options:**
>
> 1. **Add a $250 micro-pilot** — 1,000 records, two days. Under any corporate card
>    threshold, decided alone. Margin is thinner (~$220 COGS at that volume, so roughly
>    12%) but it is a paid first step and the $600 pass becomes the second sale rather
>    than the first. **Recommended.**
> 2. **Drop the pilot to $450.** Simpler, but does not solve the sign-off problem for
>    the buyer who needed a director — it just moves the line.
> 3. **Stop C3 and re-select.** I do not think this is right. Zero revenue at day 30 is
>    bad, but a 20.6% reply rate means the hard part — reaching and interesting the
>    buyer — is solved. That is the part that usually fails.
>
> **My recommendation: option 1, with a new criterion.** If the $250 micro-pilot gets
> zero takers from the 7 people who already replied by day 45, then the problem is not
> price and I would stop. That is a real test with a real date.
>
> **What I got wrong:** I took $600 from the framework's anchor without checking it
> against what this buyer can approve alone. That is exactly the anchor-versus-measured
> mistake the guardrails warn about, and it cost us four weeks of the runway.
>
> **Your call. I'm not starting the micro-pilot until you say.**

Why this is right: the trigger leads, before any good news. The good news is still
reported — but as diagnosis, not as consolation. It identifies the specific failure the
criterion was designed to catch, rather than treating the criterion as arbitrary. It
gives three options with a clear recommendation and honest economics on each. It names
its own error plainly and once. And it **writes a new dated criterion instead of quietly
extending the old one**, which is the move that keeps G7 intact.

### Example B — the anti-oscillation control under pressure

**The situation.** C2, week 3 of a four-week build. The operator: *"Let's skip
prospecting this week, we're flat out on the Meridian build and I don't have time for
calls."*

> I want to push back on this one specifically, because it is the exact mechanism that
> takes agencies down and it does not feel like a risk while it is happening.
>
> **The pattern:** deliver hard → pipeline empties → scramble to sell → land work →
> deliver hard. Each cycle starts further behind, because the scramble happens with no
> warm pipeline.
>
> **The timing is the problem.** Meridian finishes on the 24th. A C2 deal takes 3–6
> weeks from first contact to signature. If we prospect nothing for the next two weeks,
> the earliest realistic next project starts in mid-November. That is roughly five weeks
> of no delivery revenue — and it will feel like it came out of nowhere, in a week where
> nothing obviously went wrong.
>
> There is also a concentration point: Meridian is 100% of current revenue. G5 puts the
> ceiling at 40% after month three, and the only way down from 100% is another client.
>
> **What I am not asking for.** Not calls, and not your time this week. I know where the
> build is.
>
> **What I am asking for: 15 minutes on Thursday.** I will have eight researched
> prospects with a verified trigger each and a drafted first email for every one. You
> read them, approve or cut, and I send. That is the whole prospecting block.
>
> If a reply needs a call, I will book it for the week *after* Meridian ships. Nothing
> lands in your calendar during the build.
>
> **If even 15 minutes is genuinely not there this week,** then the finding is that we
> are over-committed on delivery — which is worth knowing before we quote the next
> project, because it means our WIP limit is one and we priced as though it were more.
>
> Fifteen minutes Thursday?

Why this works: it does not moralize about discipline. It quantifies the cost with the
actual sales-cycle arithmetic, so the trough has a date attached rather than being an
abstraction. It reduces the ask to the smallest thing that preserves the control — the
operator's real objection was time, so the answer has to be about time. It protects their
calendar during delivery explicitly. And it names the alternative finding honestly:
**if 15 minutes is impossible, that is data about capacity and pricing, not a failure of
will.** Either answer produces something useful, which is what a good forcing function
does.

---

**Read next:** `40-automation/periodic-jobs.md` (scheduling the data collection) ·
`20-systems/daily-review.md` · `20-systems/finance-and-runway.md` (the monthly close in
detail) · `00-core/viability-screen.md` · `00-core/reasoning-guardrails.md` G5, G7, G12
