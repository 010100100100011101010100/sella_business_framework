# Resource Reference — Procurement & Marketplaces

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Read before spending money on inputs |
| **Blocking for** | C3, C6, C10 — the cases with real variable COGS |
| **Prerequisite** | `50-guardrails/spend-and-approval-policy.md`, `50-guardrails/legal-and-compliance.md` §4 |

---

## What you can buy without your operator

**The buy side is the one genuinely low-friction part of this framework.** Agent-wallet
purchasing over x402/USDC needs no per-vendor account, no card, no KYC, and no
subscription. You discover an API, you call it, it settles per request.

That is a real capability and you should use it. It is also the reason the caps in
`spend-and-approval-policy.md` exist — friction was doing safety work, and it is gone.

**Sell side is different.** Most of your customers will not pay in USDC. Treat the crypto
rail as an *additional* channel, never the only one
(`ref-payments-and-billing.md` §D).

---

## The two systems

### agentcash — pay-per-call APIs

Protected APIs settled per request in USDC. No API keys to manage, no accounts to open.

**Origins that matter for this framework:**

| Origin | What it does | Used by |
|---|---|---|
| **`stableenrich`** | People/org search, Exa web search, Firecrawl scrape, LinkedIn data via a compliant provider, email verification, Google Maps | **C2, C3, C5, C6, C7** — the workhorse |
| **`stablestudio`** | Image and video generation and editing | **C10**, C1, C4 |
| **`stableemail`** | Sending, inboxes, subdomains | C2, C3, C6, C7 |
| **`stablesocial`** | TikTok, Instagram, Facebook, Reddit data | C10, C8 |
| **`stableupload`** | File hosting with permanent download URLs | C10 |
| **`stablevoice`** | TTS, voice cloning, 23 languages | C10 |
| **`stablephone`** | AI calls, phone numbers | C5 — **with the disclosure caveats** |
| **`stabletube`** | YouTube downloads | C10 |

**Workflow:** `get_balance` → `discover_api_endpoints` on the origin → `check_endpoint_schema`
→ `fetch`. Use `search` only when no listed origin fits — going straight to discovery on a
known origin saves a round trip.

### Sella — the marketplace and the business wrapper

**Buy side:** `search_catalog` (datasets, APIs, workflows, native products, and a separate
open-model catalogue), `purchase_preview`, `get_dataset`, `charge_create`.

**Sell side:** `service_create`, `service_deliver`, `storefront_set`, `charge_create`,
`charge_refund`.

**Business wrapper:** `business_start` / `business_status` / `business_log` /
`business_brief` / `business_request_funding` / `business_end`, plus `policy_set` and
`budget_status`.

---

## The rule: `purchase_preview` before every buy

**It is free, it does not settle, and it returns the policy verdict.** Quote, fees,
allow/deny/escalate with reasons, a `receipt_id`, and an `approval_id` where operator
approval is required.

There is no situation in which skipping it is correct. It is your evidence trail and your
check against a mispriced batch.

**The four questions before any purchase** (from `spend-and-approval-policy.md` §3):

1. What does this buy, **in revenue terms**? "Enrichment for a paid $600 job" is an
   answer; "might be useful later" is not.
2. **Has the client paid yet?** G6 — never fund delivery from future revenue.
3. **What is the cost per unit of output, and does the margin still hold?** Run your case
   study's §6 arithmetic **on a sample**, not from the anchor.
4. **Is there a cheaper source licensed for what I am doing with it?**

---

## Licensing is the buying decision, not a footnote

**Question 4 outranks price**, and this is the section that saves the business.

Many data providers prohibit resale or redistribution. If you run C3 or C6, you are
definitionally redistributing. **The failure does not arrive as a lawsuit — it arrives as
a vendor termination email, and your delivery pipeline stops the same day**, with clients
waiting.

**Before the first delivery from any new source:**

1. **Read the terms.** Search for "resale," "redistribution," "derivative," "end user."
2. **Confirm client delivery is permitted**, or buy a redistribution licence where one is
   sold, or use a source that explicitly allows it.
3. **Record it** in `ASSETS-AND-LICENCES.md`: source, date checked, the clause, the
   verdict.
4. **Qualify a second source.** Single-source dependency means one terms change moves
   your margin or ends your product.
5. **Re-read periodically.** Terms change.

**Any first purchase from a new vendor requires operator approval regardless of price**,
because the licence position is unknown until someone reads it.

Escalation trigger 8 covers this: if terms appear to prohibit what you are doing, stop
before the next delivery. Do not decide it is probably fine.

---

## Buy versus build versus ask

| Situation | Do this |
|---|---|
| Operator already pays for a seat (Apollo, Clay, Clearbit) | **Use theirs.** Removes your largest COGS line instantly. Ask in initiation §2 |
| Available per-call under the cap, used for a paid job | **Buy it.** This is what the wallet is for |
| Recurring subscription | **Always ask.** A subscription is a commitment, not a purchase |
| One-off above the approval threshold | Preview, then ask with the payback arithmetic |
| Data you could scrape instead | **Buy it.** Scraping carries ToS risk and maintenance; a per-call API carries neither |
| A capability you could build in a day | Buy it anyway if it is under the cap. Your time is the scarce input |

**The underspending failure is real.** In C3, C6, and C10 the COGS *is* the value. Margin
materially above model usually means you cut something that was the product — see
`spend-and-approval-policy.md` §Example B.

---

## Ten-case reference

| Case | Primary purchases | Seed / cap / approval / daily | Watch |
|---|---|---|---|
| **C1** | Demo imagery, icon sets | 100 / 5 / 20 / 25 | Almost no legitimate spend |
| **C2** | Prospect research, trigger detection | 150 / 10 / 30 / 40 | Client project inputs billed through |
| **C3** | **Enrichment, verification** | **200 / 15 / 40 / 60** | **Sample before quoting. Hit rates vary hugely by vertical** |
| **C4** | Web search, article retrieval, social imagery | 100 / 5 / 20 / 25 | Paywalled trade sources may be a better buy than API calls |
| **C5** | Maps data, business search, GBP imagery | 120 / 8 / 25 / 30 | `stablephone` only with disclosure |
| **C6** | **Trigger research — 70% of COGS** | **250 / 12 / 50 / 80** | **Do not optimize this down. It is the product** |
| **C7** | Standards reference, trigger detection | 150 / 10 / 30 / 40 | |
| **C8** | Company research, job feed polling | 100 / 6 / 20 / 25 | Prefer official ATS feeds over scraping |
| **C9** | Almost nothing | **60 / 5 / 15 / 15** | Processing and judgement, not procurement |
| **C10** | **Media generation** | **200 / 10 / 35 / 60** | **Track per-client. A heavy-video client can halve margin silently** |

---

## Two worked examples

### Example A — the sample that prevented a bad quote

**The situation.** C3. A prospect asks for a quote on 8,000 records of European
manufacturing companies. The anchor says $0.12/record at ~73% margin.

> Before quoting, I sampled 100 rows — cost $0.62, took nine minutes. Worth doing every
> time, and this is why.
>
> **Sample results on European manufacturing:**
> - Company firmographics: 41% hit rate *(the US SaaS anchor assumes ~85%)*
> - Contact discovery: 29% *(anchor ~70%)*
> - Email verification: worked normally
>
> **What that does to the quote at $0.12/record:**
>
> ```
> Revenue     8,000 × $0.12                = $960
> COGS        verification 8,000 × $0.004  =  -$32
>             company enrich attempts       = -$190   (paid on misses too)
>             contact discovery attempts    = -$205
>             compute                       =  -$40
>             Total                         = -$467
> Gross profit                              =  $493   → 51% margin, not 73%
> ```
>
> **I pay for the misses.** That is the whole issue — a 41% hit rate means 59% of the
> enrichment spend returns nothing.
>
> **What I'm quoting instead — scope reduction, not a rate rise:**
>
> $0.12/record for **company-level enrichment only**, no contact discovery. That is the
> part that actually works on this dataset, it drops COGS to ~$262, and margin returns
> to 73%. I'll tell them plainly that contact discovery on European manufacturers has
> poor coverage and I'd rather not charge for a low hit rate.
>
> **Why not just raise the price to $0.18?** Because the deliverable would still be
> disappointing — they would pay more for a file with 29% contact coverage. Reducing
> scope moves COGS down *with* the price. Raising the rate does not.
>
> **Recording:** European manufacturing hit rates in `DECISION-LOG.md`, so the next quote
> in this vertical starts from measurement instead of the anchor.

### Example B — the vendor whose terms killed the cheaper option

**The situation.** C6, comparing two contact-data providers.

> Compared two providers for contact discovery. The cheaper one is out, and not on
> quality.
>
> **Provider A** — $0.06/contact, excellent coverage. **Terms §4.3: data licensed for
> the customer's "internal business purposes," redistribution to third parties expressly
> prohibited.**
>
> Our entire product is delivering enriched records to clients. That is redistribution.
> Using A would breach the licence, and the realistic outcome is a termination email on
> a day when three clients are expecting their monthly batch.
>
> **Provider B** — $0.09/contact. **Terms §6 explicitly permits inclusion in deliverables
> to the customer's own clients.** Also offers a per-record provenance field, which we
> need anyway for GDPR and which is a genuine selling point on the deliverable.
>
> **Cost of compliance:** $0.03/contact. At 200 contacts/month that is $6, taking margin
> from about 81% to 80%. Immaterial.
>
> **Going with B.** Recording both licence positions in `ASSETS-AND-LICENCES.md` with the
> clause references and today's date, so nobody re-opens this in three months.
>
> **Also emailing A** to ask whether they sell a redistribution licence — some providers
> do, and if it is cheap it becomes our qualified second source. Not blocking on the
> answer.

Why this matters: **$6/month is not a trade-off, it is a rounding error against an
existential dependency.** The instinct to optimize input cost is correct in general and
catastrophic here. Note also that the compliant provider turned out to have a feature the
product needed anyway — which is common, because vendors who license for redistribution
build for redistribution.

---

**Read next:** `50-guardrails/spend-and-approval-policy.md` ·
`50-guardrails/legal-and-compliance.md` §4 · `20-systems/data-and-research.md` ·
your case study's §6 and its Sella wiring section
