# Case Registry — Index to the Ten Canonical Businesses

> **Status: REQUIRED READ.** Every file in this framework refers to these ten
> businesses by ID (C1–C10). This file is the **index**: summary tables, the
> lean-start tiering, and the selection logic.
>
> **The full narrative for each case lives in `case-studies/`.** Read the index here,
> pick your two or three candidates, then read only those case files. Do not read all
> ten case studies — you will burn your context and learn nothing you can act on.

---

## How to read the numbers

Every figure in this framework is a **planning anchor**, not a promise. Anchors come
from common market ranges and exist so you can build a first model and detect when
reality disagrees with it. They are **inferred**, not measured.

1. **Replace every anchor with your own measured value after 30 days of operation.**
2. **Record the replacement in `DECISION-LOG.md`**: old anchor, measured value, what
   you changed as a result.
3. **Never quote an anchor to a customer or prospect as if it were your result.** That
   violates guardrail G3 (Truth Constraint). If you have not measured it, say
   "modelled," or say nothing.

An anchor being wrong is normal. An anchor being *presented as evidence* is a
framework violation.

---

## Master table

| ID | Business | First $ | Margin | Money shape | Agent autonomy | Killer risk |
|---|---|---|---|---|---|---|
| **C1** | React Component Marketplace | 3–6 wk | ~95% | One-off, instant | High | Discovery |
| **C2** | Fixed-Bid Software Agency | 2–6 wk | 55–70% | Lumpy, milestone | Medium | Scope creep + concentration |
| **C3** | Data Cleaning & Enrichment | **1–3 wk** | 60–75% | Per-use or retainer | **Highest** | Data provenance / GDPR |
| **C4** | Vertical News Brief | 8–16 wk | ~90% | Sponsor + subscription | High prod, low judgement | Aggregation without a view |
| **C5** | Local SEO Retainers | 2–4 wk | 70–85% | Monthly recurring | Low sales, high delivery | Channel mismatch; day-90 churn |
| **C6** | ICP Lead Research | 2–4 wk | 75–90% | Monthly recurring | High | Source legality |
| **C7** | Compliance Doc Generation | 3–6 wk | ~90% | One-off + maintenance | Medium, human sign-off | Unauthorized practice of law |
| **C8** | Niche Job Board | 6–12 wk | ~95% | Per-post + sponsorship | High | Two-sided cold start; decay |
| **C9** | Invoice Reconciliation | 2–5 wk | ~85% | Monthly recurring | **Lowest** | One wrong number; credentials |
| **C10** | Content Repurposing Studio | 2–4 wk | 80–90% | Monthly recurring | High prod, medium voice | Generic voice |

---

## Lean-start tiering — read this before choosing

Your operator wants to start lean, with as few regulatory boundaries as possible in
the first ninety days. That is correct instinct. Here is the honest version of it.

### The KYC reality, stated plainly

**There is no path to real revenue with zero identity verification.** Every rail that
converts work into spendable money — Stripe, PayPal, Gumroad, Lemon Squeezy, a bank
account — verifies a legal person. That is not a rule you can route around, and any
plan that assumes otherwise is a plan that ends with frozen funds.

What you *can* do, and what "lean" actually means here:

| Lean move | Why it works |
|---|---|
| **Reuse the human's existing accounts** | Their personal Stripe/PayPal/Gumroad/Dodopayments is already verified. Zero new KYC. |
| **Sell as a sole proprietor first** | In most jurisdictions, invoicing under a personal name is legal without forming anything. |
| **Defer the entity until ~$2–3k/mo** | An LLC costs money and annual filings. Form it when revenue or liability justifies it, not before. |
| **Use the agent wallet for buying** | Sella/x402 purchasing settles in USDC with no per-vendor KYC. This is genuinely boundary-free — **on the buy side only**. |
| **Prepaid blocks over subscriptions** | Avoids the recurring-billing rail entirely at the start. See the billing constraint below. |
| **Avoid regulated categories at day one** | Not a workaround — a selection criterion. See Tier 3. |

**Tell your human this explicitly in the initiation conversation.** Do not quietly
assume they have a Stripe account, and do not build a business whose money path you
have not confirmed exists.

### The three tiers

**Tier 1 — Lean start. Begin here unless there is a specific reason not to.**
`C1` `C3` `C6` `C10`

- Under $150 to start. No entity required. No professional licensing.
- The human's existing personal payment account is sufficient.
- Liability is bounded: worst realistic case is a refund.
- Delivery is asynchronous and digital — no phone calls, no premises, no inventory.
- **C3 is the single best cold-start in the framework**: fastest to first dollar,
  provable value before payment, and the highest agent autonomy of the ten.

**Tier 2 — Lean, but with one blocking dependency.**
`C2` `C4` `C5` `C8`

- `C4`, `C5` and `C8` need a **recurring or transactional billing rail** before they can
  scale, which means the human must own a processor account.
- `C2` needs a **human who will take the scoping call and sign the contract**, and an
  entity before the first engagement — a $12k liability against a personal name is a real
  exposure. The delivery is otherwise lean.
- `C5` additionally needs a **human willing to make sales calls**. If that is absent,
  C5 is unavailable regardless of how good the delivery would be.
- `C4` and `C8` are slow to money (8–16 and 6–12 weeks). Only viable if the operator
  can fund a quiet quarter.

**Tier 3 — Do not start here. Graduate into these.**
`C7` `C9`

- `C7` risks unauthorized practice of law. `C9` handles other people's money data.
- Both realistically want professional liability insurance, an entity for the
  liability shield, and in C7's case an attorney relationship.
- Both are excellent businesses with high margins — **after** you have revenue,
  an entity, and insurance. Revisit at month six.
- If your operator is *already* a lawyer, accountant, or bookkeeper, these move to
  Tier 1 for them, because the professional boundary is already satisfied.

**Default recommendation: start in Tier 1, and default to C3 unless the operator's
existing assets point elsewhere.**

### The ≈$0 exception — check this before applying the default

Tier 1 means "under $150," not "free." Three of the four Tier-1 cases have a hard minimum
that a genuinely zero-capital operator cannot meet:

| Case | Real minimum before the first sample | Runs at ≈$0? |
|---|---|---|
| C1 | $0 (free tiers throughout) | ✅ — but needs a developer audience |
| **C3** | $12 domain **+ $80–200 enrichment credits** | ❌ |
| **C6** | $12 domain **+ ~$115 research per delivery** | ❌ |
| **C10** | **$0 if text-first** — drop clips and generated media | ✅ |

**At ≈$0, the default flips from C3 to C10**, run text-first: LinkedIn posts only, no
clips, no audiograms, no generated media. That takes COGS to roughly nothing while keeping
the framework's easiest distribution channel (rank 1 of 10), because the free public
repurpose needs no domain, no list, and no sending reputation.

**Say this to the operator explicitly**, because it is a real trade: text-first C10 has a
lower price ceiling (~$1,200/mo vs ~$1,600) and a weaker demonstration than a clip would
be. **C3 is the better business at any non-zero budget** — roughly $200 unlocks it, which
is worth naming as a decision rather than absorbing as a constraint.

---

## Distribution difficulty — the ranking that actually decides outcomes

You will not fail at production. You are good at production. **You will fail at
distribution.** Rank the cases by how hard it is to reach a paying buyer, and weight
this above every other factor in your selection:

| Rank | Case | Why | The channel that works |
|---|---|---|---|
| 1 (easiest) | **C10** | Delivery *is* the marketing — do the work publicly, unpaid, tagged to the target | Public proof-of-work |
| 2 | **C3** | You can prove value before payment: clean 100 of their rows free | Cold email with the sample attached |
| 3 | **C6** | The medium is the product: send them ten researched leads about their own business | Cold email that demonstrates itself |
| 4 | **C2** | Buyer already knows they have the problem; you capture demand, not create it | Outbound + referral (referral dominates by month 4) |
| 5 | **C5** | Buyer is easy to convince but hard to *reach* — they answer phones, not email | Phone and in-person only |
| 6 | **C7** | Trigger-driven outbound works, but the sale needs trust you have not built yet | Outbound on hiring/enterprise-deal signals |
| 7 | **C9** | Trust-gated; nobody hands money data to a stranger | Referral and accountant partnerships |
| 8 | **C1** | Nobody is searching for your specific pack; free alternatives are excellent | Developer social, then SEO — slow |
| 9 | **C4** | You must build an audience before anyone pays anything | Clips of the brief itself; referral loop |
| 10 (hardest) | **C8** | Two-sided cold start: worthless to each side without the other | Candidate side first, always |

**The pattern in the top three is not an accident.** C10, C3, and C6 all share one
property: **the demonstration and the deliverable are the same object.** You do a
small piece of the actual work, for free, for a specific named prospect, and that
artifact is your entire pitch. No claims to substantiate, no trust to build in the
abstract, no portfolio required.

**When ideating a business outside these ten, ask: can I do a small piece of the real
work for free, and will that artifact sell the rest?** If yes, you have a Tier-1
distribution profile. If no, you are signing up for months of audience building —
which is legitimate, but you must budget for it and tell your operator.

---

## Recurring-revenue billing constraint (C4, C5, C6, C9, C10)

Five cases depend on monthly recurring revenue. **Sella cannot charge a subscription.**
`service_create` accepts a `subscription` price kind for definition, but it cannot be
charged: x402 settles one request at a time and grants no standing authority to charge
the same payer again later.

Design around it from day one:

1. Recurring billing requires a conventional processor — Stripe, Paddle, Lemon Squeezy
   — opened by the **human**, under their legal identity. This is a **blocking item on
   the human action queue**, not a later task.
2. Until it exists, price recurring work as a **prepaid block** ("three months, paid
   upfront") which settles cleanly as a `one_off`. This is frequently better anyway:
   cash arrives earlier and churn drops.
3. **Never promise a customer an automatic renewal you cannot technically execute.**

---

## Selection procedure

Do not pick by preference. Run the procedure in `00-core/initiation.md`, which scores
the ten against your operator's actual constraints — capital, weekly hours, existing
audience, domain credibility, willingness to appear on calls, and tolerance for slow
money. The full self-selection algorithm, including the disqualifying conditions that
remove a case from consideration entirely, is in that file.

Shortcut heuristics, in priority order:

1. **Does the operator already have an audience or a network in some niche?** If yes,
   that niche's version of C10, C6, or C4 beats a cold start in anything else. An
   existing audience is worth more than a better business model.
2. **Will the operator make phone calls?** If no, delete C5.
3. **Can the operator fund 90 days with no revenue?** If no, delete C4 and C8.
4. **Does the operator have a professional license relevant to C7 or C9?** If yes,
   promote that case to Tier 1. If no, defer both to month six.
5. **Otherwise, default to C3.** Fastest to cash, highest autonomy, provable before
   payment, and the mechanics transfer to C6 and C10 later.

---

## Case files

| ID | File |
|---|---|
| C1 | `case-studies/C1-react-component-marketplace.md` |
| C2 | `case-studies/C2-fixed-bid-software-agency.md` |
| C3 | `case-studies/C3-data-cleaning-enrichment.md` |
| C4 | `case-studies/C4-vertical-news-brief.md` |
| C5 | `case-studies/C5-local-seo-retainers.md` |
| C6 | `case-studies/C6-icp-lead-research.md` |
| C7 | `case-studies/C7-compliance-doc-generation.md` |
| C8 | `case-studies/C8-niche-job-board.md` |
| C9 | `case-studies/C9-invoice-reconciliation.md` |
| C10 | `case-studies/C10-content-repurposing-studio.md` |

## Read next

- Choosing among the ten → `00-core/initiation.md`
- The rules constraining every decision → `00-core/reasoning-guardrails.md`
- What only your human can do → `00-core/human-action-queue.md`
- Reaching the buyer → `20-systems/outreach.md`
- Whether you need a website → `10-resources/ref-website.md`
