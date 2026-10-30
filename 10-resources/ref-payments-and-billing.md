# Resource Reference — Payments & Billing

| | |
|---|---|
| **Status** | **REFERENCED FILE — but effectively universal.** Resource #1 |
| **Blocking for** | Every case. The T1 money-path test fails without this |
| **Prerequisite** | `00-core/viability-screen.md` T1, `00-core/reasoning-guardrails.md` G6, G9 |

---

## Walk the money path before anything else

**Five steps. Confirm each one with the operator, out loud, on day one.**

```
1. Customer decides to buy
        ↓
2. Pays by WHAT method        ← the rail
        ↓
3. Lands WHERE                ← the account
        ↓
4. Operator can ACCESS it     ← withdrawal, hold periods, thresholds
        ↓
5. Tax is handled HOW         ← VAT/sales tax, and who is liable
```

**The failure this prevents:** an agent builds for three weeks, closes a client, and then
discovers the operator has no way to take the money. It is not a hypothetical — it is the
single most-skipped item in this framework, precisely because it feels like an
administrative detail rather than a design constraint.

**Step 4 is the one people miss even when they check the others.** "It lands in Stripe"
is not the end of the path. Stripe holds new-account funds, has payout schedules, and
freezes accounts for identity mismatch or unexpected volume. Confirm the operator can
actually get the money out, and when.

---

## The KYC reality, stated plainly

**There is no path to real revenue without identity verification.** Every rail that
converts work into spendable fiat verifies a legal person. That is not a rule you can
route around, and any plan assuming otherwise ends with frozen funds.

**What "lean" actually means here:**

| Lean move | Why it works |
|---|---|
| **Reuse the operator's existing account** | Their personal Stripe/PayPal/Gumroad is already verified. Zero new KYC |
| **Sell as a sole proprietor** | In most jurisdictions, invoicing under a personal name needs no entity |
| **Defer the entity to ~$2–3k/mo** | Formation costs money and creates annual filings |
| **Use a merchant of record** | They become liable for sales tax and VAT. See below — this is the biggest lean win available |
| **Prepaid blocks instead of subscriptions** | Avoids the recurring rail entirely at the start |
| **Agent wallet for the buy side** | x402/USDC purchasing needs no per-vendor KYC. Genuinely boundary-free — **buy side only** |

**Tell the operator this explicitly.** Do not quietly assume they have a processor, and
do not build a business whose money path you have not confirmed.

---

## The four rails

### A. Merchant of record — **the lean default for digital goods**
*Gumroad, Lemon Squeezy, Paddle*

They are the legal seller. The customer buys from them; they pay you.

**Why this matters more than the fee:** **they are liable for EU VAT and US sales tax,
not your operator.** Digital-goods tax is genuinely burdensome — EU VAT is charged at the
buyer's rate across 27 countries with registration obligations, and US economic-nexus
rules vary by state. A merchant of record makes that entirely someone else's problem for
a few percent.

- **Fee:** ~5–10% all-in — higher than a raw processor, and usually worth it
- **Best for:** C1, and any productized digital sale
- **Weakness:** less control, payout delays, not suitable for large B2B invoices

### B. Payment processor
*Stripe, PayPal, Square*

Your operator is the seller; the processor moves money and they carry tax liability.

- **Fee:** ~2.9% + $0.30 typical
- **Best for:** recurring billing (Stripe Billing), and anything needing card-on-file
- **Weakness:** **tax is now the operator's problem.** Also: new accounts get held funds
  and reviews — a first $12k payment into a fresh account frequently triggers one

### C. Invoice and bank transfer
*Direct, with a written agreement*

- **Fee:** near zero
- **Best for:** **C2, C7 — any B2B engagement above ~$2,000.** A corporate finance team
  expects an invoice and pays by transfer. Asking them to enter a card costs you deals
- **Weakness:** collection risk. Mitigate with deposits (G6)

### D. Crypto rail — Sella / x402 / USDC
*`service_create`, `charge_create`*

- **Fee:** platform fee deducted, remainder credits the operator's payable balance
- **Best for:** the **buy side** (procurement without per-vendor KYC), and per-use or
  one-off sales to crypto-comfortable buyers
- **Weaknesses, both important:**
  1. **Cannot charge subscriptions.** x402 settles one request at a time and grants no
     standing authority to charge a payer again
  2. **Most buyers will not use it.** A dentist, a RevOps manager, and a corporate
     finance team will all decline. Treat it as an *additional* rail, never the only one

---

## The subscription constraint (C4, C5, C6, C9, C10)

**Five of the ten cases depend on monthly recurring revenue, and Sella cannot charge
it.** `service_create` accepts a `subscription` price kind for *definition*, but it
cannot be charged.

Three consequences to design around from day one:

1. **Recurring billing requires a conventional processor** — Stripe Billing, Paddle,
   Lemon Squeezy — opened by the **human** under their identity. Blocking human action,
   not a later task.
2. **Until it exists, sell prepaid blocks.** "Three months, paid upfront" settles cleanly
   as a `one_off`. This is frequently *better anyway*: cash arrives earlier, churn drops,
   and the commitment conversation happens once instead of monthly.
3. **Never promise an automatic renewal you cannot technically execute.** That is a G3
   violation and it produces an angry customer at exactly the wrong moment.

---

## Payment terms — G6 in practice

**Never fund delivery from future revenue.**

| Work type | Terms | Why |
|---|---|---|
| Digital goods (C1) | Paid before delivery | Trivial |
| Project work (C2, C7) | **50% on signature, 50% on acceptance** | A client who will not pay a deposit will not pay the balance |
| Large projects (>$15k) | Three milestones | Limits exposure at any point |
| Per-use (C3, C6) | **Prepaid credits** | Removes collection risk entirely and funds COGS |
| Retainers (C5, C9, C10) | **Billed in advance, monthly** | Never in arrears |

**Do not extend net-60 as a small business.** You are not a bank, and a client who needs
60 days is telling you something about their own cash position.

**The deposit is not negotiable, and asking for it is not awkward.** It is standard
practice in every professional service. An operator who feels uncomfortable asking should
know that the discomfort is theirs alone — the client expects it.

---

## Tax, briefly and honestly

**This is not tax advice.** It varies enormously by jurisdiction and it is a genuine
"ask an accountant" domain.

What you need to know structurally:

- **Digital goods sold internationally trigger VAT/sales-tax obligations** that are
  disproportionately burdensome at small scale. **A merchant of record removes this
  entirely** and is the single strongest argument for rail A on C1.
- **B2B services** are generally simpler — often reverse-charge within the EU, and
  usually no sales tax on services in most US states, though this varies.
- **The operator owes income tax on profit** regardless of rail. Set expectations early:
  money in the account is not all theirs.
- **Keep records from transaction one.** Every invoice, every receipt, every COGS line.
  `20-systems/finance-and-runway.md` covers the bookkeeping cadence.

**Escalate to an accountant when:** revenue passes roughly $2–3k/month, the operator
forms an entity, sales cross a border, or anyone mentions a VAT threshold.

---

## Refunds, chargebacks, disputes

- **Publish a clear refund policy and honour it without argument.** A 14-day policy on
  digital goods keeps abuse under ~3%.
- **Never fight a small chargeback.** A $49 dispute costs more in time and fees than it
  recovers, and losing raises your dispute ratio anyway.
- **A dispute ratio above ~1% risks processor termination.** That is an
  account-ending event, not a cost line.
- **Refund generously when you have underdelivered.** C8's "fewer than 3 applicants and
  I refund it" is a sales tool precisely because it is real.

---

## What you may not do (G9) · **HARD**

You may not:
- Open a payment processor, merchant, or bank account
- Complete KYC or identity verification
- **Enter or handle card numbers, bank details, or financial credentials** — the
  operator's or a customer's
- Initiate, approve, or schedule a payment or transfer
- Build a payment form. **Hosted checkout redirect only** — card data must never touch a
  page you wrote (`ref-website.md` §3)

**You may:** hold publishable keys (`pk_`), draft invoices for the operator to send,
configure products and prices inside an account they opened, and prepare the exact
setup steps so their part takes minutes.

**If an operator offers to send you their ID, SSN, or card details: decline, and tell
them not to put it in chat.** See `00-core/human-action-queue.md` §Example B for the
script.

---

## Ten-case reference

| Case | Primary rail | Terms | The specific trap |
|---|---|---|---|
| **C1** | **Merchant of record** | Paid upfront | Building custom checkout instead of using MoR, and inheriting EU VAT |
| **C2** | **Invoice + transfer** | 50/50 | Starting work before the deposit lands |
| **C3** | Invoice or Stripe; **prepaid credits** | Prepaid | Buying enrichment before the client has paid (G6) |
| **C4** | Stripe/ESP for subs; `one_off` for reports | Monthly / upfront | Promising renewal on a rail that cannot renew |
| **C5** | **Stripe card-on-file** | Advance, 6-mo term | Billing in arrears, then chasing a dentist for $900 |
| **C6** | Stripe, or **prepaid quarters** | Advance | Quoting a volume tier without re-running COGS |
| **C7** | **Invoice + transfer** | Upfront for the pack | Putting a compliance engagement on a crypto rail |
| **C8** | Stripe/MoR for posts | Immediate | Recruiter subscription — cannot charge on Sella; sell prepaid |
| **C9** | Stripe card-on-file | Advance | **Never touching client bank credentials.** The C9 boundary |
| **C10** | Stripe, or **prepaid pilot** | Advance | Selling a monthly retainer with no recurring rail in place |

---

## Two worked examples

### Example A — walking the money path and finding the break

**The situation.** C10 selected. Operator has Stripe from a previous project. Looks fine.

> Walked the money path with you and found one break. Better now than in week four.
>
> 1. **Customer decides** — a creator agrees to $1,400/month. Fine.
> 2. **Pays by what method** — card. Fine.
> 3. **Lands where** — your Stripe. Fine.
> 4. **You can access it** — **here is the break.** Your Stripe is set up as a one-off
>    payment link from the 2024 project. It has no Billing product configured, which
>    means it can take a single payment but cannot charge the same card next month.
>    Right now we can sell a one-off, not a retainer.
> 5. **Tax** — B2B services, your jurisdiction, likely no sales tax on services. Worth
>    one question to your accountant before invoice three, not before invoice one.
>
> **Two options:**
>
> 1. **Set up Stripe Billing** (~20 min, yours). Proper subscriptions, card on file,
>    automatic renewal, failed-payment retries. This is where we end up eventually.
> 2. **Sell a prepaid pilot instead** — $800 for one month, one-off, using what already
>    works. **This is what I'd do first**, and not just because it avoids the setup.
>
> **Why the pilot is better anyway:** a creator who has never worked with us is being
> asked to commit to a recurring charge on the strength of a free sample. That is a
> bigger ask than $800 once. The pilot converts better, the cash arrives sooner, and a
> client who has seen a month of output renews far more readily than one committing
> cold.
>
> **My recommendation:** sell pilots now, and set up Billing in week three when we have
> a client who has already seen a month and wants to continue. That way the setup
> happens against a real renewal instead of a hypothetical one.
>
> Nothing is blocked either way — I just wanted the constraint visible before I write
> pricing into the offer.

Why this works: it walks all five steps rather than stopping at "there's a Stripe
account," locates the break precisely, and turns a constraint into a better commercial
decision. The recommendation is not a workaround — it is genuinely the stronger first
offer, and the reasoning says why.

### Example B — the operator who wants to skip the merchant of record

**The situation.** C1. Operator: *"Gumroad takes 10%? That's a lot. Let's just use
Stripe, it's 3%."*

> The 7-point difference is real and I want to show you what it is buying, because it is
> not just convenience.
>
> **What Gumroad's fee covers that Stripe's does not: they become the merchant of
> record.** That means they are the legal seller and they carry the sales-tax liability.
>
> **Concretely, on digital goods:** the moment someone in Germany buys your $49 pack, EU
> VAT is due at the German rate. Same for France, Spain, and 24 others, each at their own
> rate. There are registration schemes to handle this, and they involve filings. On the
> US side, economic-nexus rules mean sales tax obligations can arise in states you have
> never been to, and the thresholds vary by state.
>
> With Stripe, all of that is yours. With Gumroad, none of it is.
>
> **The arithmetic at our modelled volume:** roughly 10 sales/month at $49 is $490.
> The fee difference is about $32/month. Handling EU VAT registration and filings
> yourself costs either a chunk of your time every quarter or a few hundred a year to an
> accountant — and it costs it *whether or not* the volume justifies it.
>
> **Where the trade flips:** at maybe $8–10k/month in digital sales, the fee difference
> becomes large enough that proper tax handling on Stripe is worth setting up. That is a
> good problem and we should revisit it there.
>
> **One more thing that is not on the invoice:** Gumroad handles VAT-inclusive display
> pricing for EU buyers automatically. Getting that wrong — showing $49 and charging $58
> at checkout — is a conversion problem *and* a consumer-protection problem in several
> jurisdictions.
>
> **My recommendation: Gumroad now, revisit at $8k/month.** The 7% is buying you the
> right to not think about international tax while we find out whether anyone buys.

Why this works: it does not dismiss a legitimate cost concern. It identifies what the fee
actually purchases, quantifies both sides at *our* modelled volume rather than in the
abstract, names the threshold at which the answer flips, and adds a non-obvious point
about VAT-inclusive display pricing. **The operator can now make this decision themselves
next time.**

---

**Read next:** `10-resources/ref-website.md` §3 (hosted checkout redirect) ·
`20-systems/finance-and-runway.md` · `50-guardrails/security-and-secrets.md` §4 ·
`00-core/human-action-queue.md` (all of this is blocking and theirs)
