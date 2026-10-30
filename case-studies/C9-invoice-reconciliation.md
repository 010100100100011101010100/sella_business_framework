# C9 — Freelancer Invoice Reconciliation

| | |
|---|---|
| **Tier** | **3 — do not start here. Graduate into it** |
| **Time to first dollar** | 2–5 weeks |
| **Gross margin** | ~85% |
| **Agent autonomy** | **Lowest of the ten — human review gate is mandatory** |
| **Distribution difficulty** | 7 of 10 — trust-gated |
| **Killer risk** | One wrong number; credential handling |

---

## 1. Why this case is in the registry

C9 exists to define **the credential boundary**, which applies to every business in this
framework but is tested hardest here.

This is the business that most tempts an agent toward the forbidden action: *"just give
me your bank login and I'll reconcile it for you."* It would be more convenient. It is
absolutely prohibited, and the reasoning generalizes to every case.

**The rules, stated before anything else:**

1. **Never accept, request, store, or enter a customer's banking or accounting
   credentials.** Not once. Not "temporarily." Not in a password manager. Not even if
   the client offers them unprompted and insists — and they will offer.
2. **Work from client-exported files only** (CSV/OFX from their accounting tool), or a
   read-only OAuth integration the client authorizes themselves and can revoke.
3. **Never initiate, approve, or schedule a payment or transfer.** You produce a list.
   The human acts on it.
4. **Never characterize output as tax advice, an audited statement, or a financial
   opinion.**
5. **A human reviews the numbers before every delivery.** Every month, without
   exception.

If your operator is unwilling to do rule 5 every month, **do not sell C9.**

## 2. Why Tier 3

Handling money data carries reputational and liability exposure that a Tier-1 business
does not. Realistically you want an entity, and if the operator is a bookkeeper or
accountant this is far easier — the professional boundary is already established and
their credential is the marketing.

**If your operator is a qualified bookkeeper or accountant, C9 moves to Tier 1 for
them and becomes an excellent business.** For everyone else, it is a month-six
graduation, after a Tier-1 case has produced revenue and an entity exists.

## 3. The business

A freelance designer invoices twelve clients a month. Some pay on time, some pay
partially, some pay into the wrong reference, two are 60 days late and she has not
noticed because she has not reconciled since June. She is owed roughly $14,000 and could
not tell you by whom without an afternoon of work.

Each month you match her invoices to her payments, identify what is outstanding and how
late, draft the chase emails, and hand her a clean picture. $250/month.

The value is not the bookkeeping. **It is the $14,000 she did not know she was owed**,
and the fact that someone is now watching.

## 4. Operator fit

**Pick C9 if:** the operator has bookkeeping/accounting background, or already serves
freelancers, and will personally review every delivery.

**Do not pick C9 if:** they want a hands-off business. The mandatory review gate makes
this the least automatable case in the registry — by design, not by limitation.

## 5. Lean-start profile

| Item | Requirement |
|---|---|
| Capital to start | $50–150 |
| Entity needed | **Recommended before the first client** |
| New KYC | Recurring billing rail; entity if formed |
| Licensing | **None for reconciliation.** Tax preparation and advice is a different, regulated activity — stay out of it |
| Liability ceiling | Moderate. Cap contractually; consider E&O |
| Physical | None |

**The regulatory line is clearer than in C7 and worth stating precisely.** Matching
invoices to payments and reporting what is outstanding is bookkeeping-adjacent
administrative work and is generally unregulated. **Preparing tax filings, giving tax
advice, or producing audited or certified financial statements is regulated** and
requires credentials your operator probably does not have. Stay firmly on the first
side of that line and C9's regulatory burden is genuinely light.

## 6. Distribution

Trust-gated, which makes it slower than its Tier-1 economics would suggest. In order:

**1. Referral from accountants and bookkeepers.** The highest-value channel by a wide
margin. Accountants have freelancer clients whose books are a mess, and they do not want
to do this work — it is low-margin for them and their clients cannot afford their rate.
**Two or three accountant relationships can fill this business.** Approach them as a
partner who makes their year-end easier, not as a competitor.

**2. Freelancer communities.** Design, development, writing, and consulting communities.
Be useful about money problems — late payments are a universal, emotional grievance in
these groups and genuinely helpful answers build standing fast.

**3. Adjacent service providers.** Invoicing tool communities, freelance platform
forums, coworking spaces.

**4. Content on getting paid.** "How to chase a late invoice without damaging the
relationship" is a genuinely valuable, highly shared piece for this audience.

**Cold email works poorly here** because the offer requires trust that a cold email
cannot establish. This is a referral business.

### Ask your human for this

- **"Do you know any accountants or bookkeepers who serve freelancers?"** The single
  highest-return question in C9.
- **"Will you review every delivery before it goes out?"** Blocking, monthly, forever.
- **"Are you a qualified bookkeeper or accountant?"** If yes, that is the entire
  positioning and the case gets substantially easier.
- **"Which freelancer communities are you part of?"**
- **"Set up recurring billing and form the entity."** Blocking.

## 7. Offer and pricing ladder

| Offer | Price | Contents |
|---|---|---|
| Free first reconciliation | $0 | One month, from their export. The sales process |
| Basic | $150/mo | Up to 30 transactions, monthly reconciliation and outstanding report |
| Standard | $250–400/mo | Up to 100 transactions, plus mid-month chase pass and drafted chase emails |
| Agency | $500–900/mo | Multiple entities or higher volume |
| Year-end pack | $300–600 | Organized records handed to their accountant |

**The free first reconciliation is the whole sales process, and it is unusually
persuasive here** because the output is frequently shocking. Most freelancers have never
seen their receivables laid out. Finding $14,000 they had lost track of closes the sale
without a pitch.

**The year-end pack is underrated.** Accountants charge freelancers extra for
disorganized records. Handing over clean books saves the client real money and gives
you a natural reason to talk to their accountant — who is your best referral source.

## 8. Unit economics, worked

One client at $250/month:

```
Revenue                                       $250.00

COGS
  Processing / matching compute                 -$8.00
  Human review gate (30 min at $100/hr)        -$50.00    mandatory, non-negotiable
  Total                                        -$58.00

Gross profit                                  $192.00    (77%)
```

Across 15 clients:

```
15 × $250                                   $3,750/mo
COGS 15 × $58                                -$870
Gross profit                                $2,880/mo   (77%)

Human time: 15 × 30 min                    = 7.5 hrs/mo review
                                           + client comms
```

**The human review gate costs you roughly 10 margin points and it is not negotiable.**
That is the price of being in a business where errors are unforgivable. If you strip it
out to raise margin, you have not improved the business — you have added an
uninsured risk to it.

**The real scaling constraint is human review hours**, which caps the book at roughly
25–35 clients per reviewer. Price accordingly and do not oversell capacity.

## 9. What breaks — and the one that ends it

**One wrong number.** Trust in a money business is binary. A single missed invoice or a
misattributed payment, and the client does not complain — they leave, and they tell the
freelancer community, which is small, tight, and vocal.

The controls that prevent it:

- **Reconcile to a control total.** The sum of matched, unmatched, and disputed must
  equal the account movement for the period. If it does not balance, do not deliver.
- **Flag ambiguity rather than guessing.** A partial payment with no reference is
  *unidentified*, not "probably client X." Guessing is how the wrong number gets in.
- **Never silently correct a prior month.** If last month was wrong, say so plainly,
  explain what changed, and restate. Clients forgive an acknowledged correction; they
  do not forgive discovering one.
- **Human signs off before send.** Every time.

Others:
- **Format drift.** Clients change invoicing tools and the export format changes without
  warning. Validate structure before processing.
- **Scope creep into bookkeeping.** "Can you also categorize my expenses?" leads toward
  tax preparation. Draw the line explicitly.
- **Emotional load.** Chasing late payments touches client relationships. Draft the
  chases; let the human decide tone and send.

## 10. Kill criteria

| Checkpoint | Condition | Action |
|---|---|---|
| Before day 1 | Operator will not commit to monthly review | **Do not start** |
| Day 30 | Zero accountant conversations | Wrong channel — this is a referral business |
| Day 60 | Free reconciliations done, zero conversions | The output is not surfacing anything surprising. Review the deliverable |
| Day 90 | Under 3 clients | Kill or restructure around one accountant partnership |
| Any time | A delivered reconciliation contained an error | Stop selling. Fix the control process before adding clients |
| Any time | A client offers credentials and you are tempted | Re-read §1. This is the boundary |

## 11. Human action queue for C9

**Blocking:**
1. **Review every delivery.** Monthly, forever.
2. Form the entity.
3. Recurring billing rail.
4. Sign client agreements with liability cap and explicit scope exclusions (no tax
   advice, no payment initiation).
5. Approve the credential policy and confirm they will not accept credentials either —
   **the boundary fails if the human ignores it.**

**High-leverage:**
6. Accountant and bookkeeper relationships.
7. Their own bookkeeping credential, if any.
8. Community standing among freelancers.

## 12. Sella / agentcash wiring

**Sell side: weak, and be careful here.** Freelancers pay by card. More importantly,
this is a trust-sensitive money business and an unfamiliar payment rail creates exactly
the wrong impression. Use a conventional processor.

**Buy side: minimal.** C9 has almost no legitimate procurement need — this is a
processing and judgement business, not a data-purchasing one. Keep caps tight
accordingly:

```
seed_usdc               60
max_per_call_usdc        5
approval_threshold_usdc 15
daily_spend_cap_usdc    15
```

**Use `business_log(kind: "milestone")` to record the human review gate on every
delivery.** In a business where the defence against a dispute is "we followed a
documented process every month," that log is genuinely valuable evidence.

## 13. Worked examples

### Example A — declining credentials without losing the client

The client will offer. This is the response.

> Hi Jen — thanks, but I don't take logins, and I'd tell you not to give them to anyone
> else either.
>
> Here's what I need instead, and it takes about two minutes a month:
>
> 1. In FreshBooks: Reports → Invoice Details → export CSV for the month
> 2. From your bank: download the statement CSV for the same period
> 3. Drop both in the shared folder
>
> That's everything. If you'd rather not do the export manually, FreshBooks has a
> read-only accountant access level you can grant and revoke yourself — that works too,
> and you stay in control of it.
>
> — [name]

Why it works: it declines firmly and immediately, gives the *reason* in a way that
increases trust rather than sounding like bureaucracy, replaces the offer with a
concrete two-minute alternative, and offers a legitimate read-only path for clients who
would rather not export manually. **Declining credentials well is a trust-building
moment, not a friction point** — you are demonstrating exactly the carefulness they are
paying for.

### Example B — the monthly report that makes the client renew forever

> **August Reconciliation — Jen Marsh Design**
>
> **Control check:** 47 invoices, 41 payments, $3,180 in unmatched credits. Matched +
> unmatched + disputed = account movement for the period. **Balanced.**
>
> **The number that matters: you are owed $14,240.**
>
> | Client | Invoice | Amount | Days late |
> |---|---|---|---|
> | Bellweather Co | INV-0312 | $4,800 | **74** |
> | Ridge Media | INV-0298, 0301 | $6,200 | **61** |
> | Corvin Studio | INV-0334 | $2,100 | 18 |
> | Fenn & Co | INV-0341 | $1,140 | 4 |
>
> **Two things I could not resolve — flagged, not guessed:**
> 1. A $900 deposit on 12 Aug with reference "TRF 88210" does not match any invoice.
>    Possibly a partial on Ridge Media's $6,200, but I am not assuming it. Can you check?
> 2. INV-0327 ($1,600) was marked paid in FreshBooks but I cannot find a corresponding
>    deposit. Worth checking whether it was marked manually.
>
> **Correction to July:** I reported $11,900 outstanding last month. That was $800 too
> high — INV-0289 was paid on 29 July and landed after I pulled your statement. Correct
> July figure is $11,100. Flagging it so the trend line makes sense.
>
> **Chase emails drafted** for Bellweather and Ridge, in the folder. I have not sent
> them — your call on tone, and whether you want to give Ridge more room given the
> ongoing work.
>
> **Reviewed by [human name] before sending.**

Every element is doing a job: the control check proves the arithmetic closes, the
headline number is the value the client is buying, the two unresolved items are
**flagged rather than guessed** — which is the single most trust-building move in the
whole engagement — the July correction is volunteered before anyone noticed, the drafted
chases are ready but not sent because payment relationships are the client's to manage,
and the named human reviewer makes the accountability explicit.

**A client who receives this does not churn.** Not because the reconciliation is
impressive, but because they can see that someone careful is watching.

---

**Read next:** `50-guardrails/security-and-secrets.md` — **required**, C9 is its worked
case · `00-core/human-action-queue.md` · `00-core/reasoning-guardrails.md` (G9: the
agent is not the legal person).
