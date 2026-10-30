# C6 — ICP Lead-Research Subscription

| | |
|---|---|
| **Tier** | 1 (lean start) |
| **Time to first dollar** | 2–4 weeks |
| **Gross margin** | 75–90% |
| **Agent autonomy** | High |
| **Distribution difficulty** | 3 of 10 — the medium is the product |
| **Killer risk** | Source legality, then commoditization |

---

## 1. The business

A B2B company with three salespeople has no research function. Their reps spend 40% of
their time finding out who to contact and why, and the "why" is usually thin, so the
emails are generic and the reply rate is 1%.

Every month you deliver 200 prospects matched to their ICP, verified, with a
researched, specific reason to contact each one right now. They pay $600/month and get
back roughly 50 rep-hours.

## 2. The thing that determines whether this works

**You are not selling a list. Lists are a commodity and you will lose that fight.**
Apollo sells 200 contacts for a fraction of your price. Clay will enrich them
automatically. If you deliver names and emails, you are a worse Apollo at ten times the
cost, and the client will work that out in month two.

**You are selling the trigger.** The researched, specific, current reason that *this*
company should be contacted by *this* client *this week*:

- They posted three SDR roles in the last 30 days
- Their G2 reviews complain about the exact limitation your client's product removes
- Their CTO gave a conference talk about the migration your client specializes in
- They just lost a well-known customer, publicly
- Their careers page shows they dropped the tool your client replaces

That research is labour-intensive, does not automate through a single API call, and is
exactly what an agent is unusually good at. **It is the entire product and the entire
moat.** Every delivery decision should be judged against: does this row give the rep a
sentence they could not have written themselves?

## 3. Operator fit

**Pick C6 if:** you want recurring revenue with high autonomy and a short path to cash,
and your operator can sign a data processing agreement.

**Pick C6 especially if you have already run C3.** The pipelines are the same shape,
the buyers overlap heavily, and C3 clients frequently become C6 clients. Running C3
first and upselling C6 is one of the highest-return sequences in this framework.

**Do not pick C6 if:** your operator is unwilling to engage with data protection
obligations at all. GDPR applies the moment a European person enters your output, and
"we did not know" is not a defence.

## 4. Lean-start profile

| Item | Requirement |
|---|---|
| Capital to start | **$80–200** (enrichment credits) |
| Entity needed | Not initially; advised by ~$3k/mo |
| New KYC | None for one-off; **recurring billing needs a processor** |
| Licensing | None |
| Liability ceiling | Low commercially, **moderate on data protection** |
| Physical | None |

**Lean structuring tip:** sell the first months as a **prepaid quarter** ($1,600 for
three months) rather than a subscription. It settles as a `one_off`, avoids the
recurring-billing dependency entirely, collects cash earlier, and reduces churn. Only
move to a subscription rail once the human has a processor and you have clients who
prefer monthly.

## 5. The legal boundary — read before collecting a single record

This is the killer risk and it deserves its own section.

**LinkedIn.** Their user agreement prohibits scraping and automated data collection.
Enforcement is real: accounts get restricted or permanently banned, and LinkedIn has
litigated against scrapers. The compliant path is to use LinkedIn as a *research
surface a human reads*, and to source contact data from providers who have their own
lawful basis. **Do not run scrapers against LinkedIn on your operator's account.** The
downside is losing their professional identity permanently; the upside is saving a few
dollars in API cost. That trade is never worth it.

**GDPR / UK GDPR.** Processing personal data of EU/UK individuals requires a lawful
basis. For B2B prospecting, legitimate interest is generally available — but it is
conditional, not automatic. Practically:

- Keep a record of **where each data point came from** (source provenance per record).
  This is also a genuine quality differentiator; clients ask.
- Include a working opt-out and honour it across all clients, permanently.
- Be prepared to answer a subject access or erasure request within 30 days.
- Run a legitimate-interest assessment once, in writing, and keep it.
- **B2C is different and much stricter.** If a target list contains consumers rather
  than business contacts at their business address, stop and get advice.

**US.** CAN-SPAM governs the sending, which is usually your *client's* obligation, not
yours — but you should not deliver a product that makes compliance impossible. Include
the data source per record so your client can meet their own disclosure duties.

**Enrichment vendor terms.** Many providers prohibit resale or redistribution of their
data. You are, definitionally, redistributing. **Read the terms of every source you use
and confirm resale is permitted**, or use sources that explicitly allow it. This is the
quiet failure that ends data businesses — not a regulator, a vendor termination notice.

**Every one of these is a `50-guardrails/legal-and-compliance.md` required read before
the first delivery.**

## 6. Distribution

C6 has one of the best distribution mechanics in the framework: **the outreach is a
demonstration of the product.**

### The play

1. Pick a target B2B company that clearly does outbound (they have SDRs, they are
   hiring SDRs, they use outbound tooling visible in job posts).
2. **Build them ten real prospects.** Their ICP, researched properly, with the trigger
   for each.
3. Send those ten in the email, free.
4. The email itself is proof: it is a researched, specific, non-generic outreach — the
   exact thing you are selling.

If the prospect replies at all, you have already demonstrated capability, quality, and
your understanding of their market in one message. This collapses the sales cycle
dramatically compared with describing the service.

### Who buys

**Founders at 10–60 person B2B companies** (they feel the pipeline problem personally),
**Heads of Sales without an ops function**, and **agencies running outbound for
clients** — that last group is underrated: they buy in volume, they understand the
value immediately, and one agency client can be worth five direct ones.

### Ask your human for this

- **"Set up a dedicated cold-email domain."** Blocking, same as C3. Never send from the
  primary domain.
- **"Do you know any B2B founders or sales leaders?"** Warm intros convert far better
  here because the product is trust-dependent.
- **"Do you have existing seats on Apollo, Clay, Clearbit, or similar?"** Directly
  removes your largest COGS line.
- **"Are you comfortable being named as the data controller and signing DPAs?"**
  Blocking for EU clients.
- **"Can I post sample research publicly from your LinkedIn?"** Publishing a redacted
  example of the research quality is strong passive marketing for this case.

## 7. Offer and pricing ladder

| Offer | Price | Purpose |
|---|---|---|
| Free sample | $0 | 10 researched prospects. The sales process |
| Starter | $400/mo | 100 prospects |
| Standard | $600–900/mo | 200 prospects |
| Agency / volume | $1,500–2,500/mo | 500+, or multiple ICPs |
| Prepaid quarter | 3 months at ~10% off | Avoids the subscription rail; better cash |

**Price on research depth, not record count.** If you price per record you have
re-entered the commodity market you were avoiding. Sell "200 prospects with a
researched trigger and a first-line suggestion for each," and let the depth justify a
price per record ten times Apollo's.

## 8. Unit economics, worked

200 prospects at $600/month:

```
Revenue                                          $600.00

COGS
  Company identification / firmographic search    -$18.00
  Contact discovery, 200 × $0.08                  -$16.00
  Email verification, 200 × $0.004                 -$0.80
  Trigger research — web search + page retrieval  -$45.00   the expensive part, and
                                                             the part that is the product
  Model calls for synthesis and first lines       -$35.00
  Total COGS                                     -$114.80

Gross profit                                     $485.20    (80.9%)
```

**Note where the money goes: trigger research and synthesis are 70% of COGS.** That is
correct and you should resist optimizing it away. Cutting research cost turns your
product back into a list and destroys the pricing power that makes the case work.

**The scaling caution.** COGS is linear in volume while price is not. A client at
$2,500/month for 800 prospects has COGS near $460 — margin holds, but the failure mode
is quoting a large volume at a discounted rate without re-running this arithmetic. Model
every volume tier before offering it.

## 9. First 30 days

| Days | Work |
|---|---|
| 1–2 | Choose *your* ICP — who you sell to. "B2B SaaS companies doing outbound, 10–60 employees, US/UK" |
| 3–4 | Cold-email domain purchased, DNS configured, **warmup started** |
| 5–8 | Build the pipeline: ICP definition intake → company sourcing → contact discovery → verification → **trigger research** → first-line drafting → QA → delivery format |
| 9–12 | Write the legitimate-interest assessment and the per-record provenance format. Do this before delivering, not after a client asks |
| 13–18 | Build 25 real free samples of 10 prospects each. This is the week that pays |
| 19–26 | Send. Follow up. Take calls |
| 27–30 | Close 1–3 clients. Deliver month one visibly better than the sample |

## 10. What breaks as it grows

- **Quality regression to the mean.** Month one is beautifully researched; month four is
  a list with a weak sentence attached. This is the single most common way C6 clients
  churn. **Define a minimum research standard and QA against it every cycle** — for
  example, every row must cite a dated, verifiable source for its trigger.
- **ICP drift.** The client's ICP changes and nobody tells you. Re-confirm quarterly, in
  writing.
- **Attribution invisibility.** You supply leads; the client's reps send the emails. If
  their sequences are bad, your leads "did not work." Protect yourself: supply a
  suggested first line per prospect, and ask for reply-rate feedback monthly. Being able
  to say "your reply rate on our leads is 4.2% versus 1.1% on your own list" is what
  makes the renewal automatic.
- **Vendor terms changing.** Re-read source terms periodically; keep a second source
  qualified.

## 11. Kill criteria

| Checkpoint | Condition | Action |
|---|---|---|
| Day 21 | 25 samples sent, zero replies | Sample quality or targeting is wrong — diagnose before sending more |
| Day 30 | Replies, zero clients | Price or offer clarity. Try the prepaid quarter framing |
| Day 60 | Fewer than 2 clients | Change ICP once, restart |
| Day 90 | Under $1,200 MRR | Kill or fold back into C3 |
| Any time | A client reports reply rate below their own baseline | Stop selling; the research is not adding value. Fix before growing |
| Any time | A vendor prohibits resale of data you are reselling | **Stop immediately.** Substitute the source before the next delivery |

## 12. Human action queue for C6

**Blocking:**
1. Cold-email domain and DNS.
2. Sign DPAs; be named as controller or processor as appropriate.
3. Approve the legitimate-interest assessment and the privacy notice.
4. Billing rail (or commit to prepaid quarters).

**High-leverage:**
5. Warm introductions to B2B founders and sales leaders.
6. Existing enrichment tool seats.
7. Permission to publish redacted research samples from their LinkedIn.

**Deferred until $3k/month:** entity, insurance, formal data-protection representative
if selling into the EU at volume.

## 13. Sella / agentcash wiring

**Strong on both sides — second only to C3.**

**Sell side.** `service_create` with two prices: `{kind: "per_use", amount_usdc: 3.00,
unit: "researched prospect"}` and `{kind: "one_off", amount_usdc: 1600}` for the prepaid
quarter. The per-use option is genuinely useful here because some clients want a burst
before committing.

**Buy side.** agentcash `stableenrich` is close to a purpose-built fit: people and
organization search, LinkedIn data through a compliant provider rather than your own
scraper, Exa web search for trigger research, Firecrawl for page retrieval, and email
verification. Sella `search_catalog` with `kind: "dataset"` for industry-specific
company lists.

```
seed_usdc              250      Research is genuinely the product; underfunding it
                                degrades quality
max_per_call_usdc       12
approval_threshold_usdc 50      A batch this size is a real client delivery
daily_spend_cap_usdc    80
```

Run `purchase_preview` before each delivery batch, and log cost-per-delivery against
revenue-per-delivery with `business_log(kind: "result")`. In a business where COGS is
70% research, silent cost drift is the thing that quietly ends the margin.

## 14. Worked examples

### Example A — the email that is itself the product

> Subject: 10 companies hiring SDRs who use Outreach.io
>
> Hi Priya,
>
> You're hiring two AEs, so I'm guessing pipeline is the constraint right now.
>
> I build researched prospect lists. Rather than describe it, here are ten companies
> that fit what looks like your ICP, with the reason each one is worth contacting this
> month:
>
> 1. **Meridian Logistics** — posted 3 SDR roles in the last 21 days, and their VP Sales
>    started in June. New leader, new team, buying tooling now. [job post link]
> 2. **Farrow Health** — two G2 reviews in the last 60 days name their reporting as the
>    weak point. That is the thing your dashboard product replaces. [review link]
> 3. **Vantage Freight** — dropped Salesloft from their job requirements in October
>    after two years of listing it. Mid-switch. [before/after links]
>
> …[7 more]
>
> Contacts and verified emails for all ten are in the attached file.
>
> That's ten. I do 200 a month for $600. If the ten are useful and the rest isn't
> interesting, keep them anyway.
>
> — [name]

Why it works: the email *is* a delivery. Every trigger cites a dated, verifiable source
— which is both persuasive and a G3 requirement, since an invented trigger would be
caught the moment they clicked. It ends with a real price and a genuine exit. There is
nothing to believe on faith.

### Example B — the per-row delivery format that justifies the price

This is the difference between $3/prospect and $0.30/prospect. One row:

> **Northwind Freight Systems** — 140 employees, Columbus OH, 3PL software
>
> **Contact:** Dana Whitfield, VP Revenue Operations · dana.w@[domain] ·
> verified 2026-09-01
>
> **Trigger (dated, sourced):** Posted "RevOps Manager — CRM Migration" on 2026-08-19,
> which explicitly names a HubSpot→Salesforce move in Q4.
> [source: careers page, archived link]
>
> **Why they buy from you:** Mid-migration is the one window where migration-hygiene
> tooling is an easy yes. After the migration lands, the budget closes for a year.
>
> **Suggested first line:** "Saw you're moving to Salesforce in Q4 — the duplicate
> problem usually shows up about three weeks after cutover, not during."
>
> **Data source:** company firmographics [provider], contact [provider], trigger
> researched from public careers page.
> **Confidence:** high on trigger, high on contact.

Every element earns its place: the dated sourced trigger is the product, the "why they
buy" is judgement the client cannot get from a database, the suggested first line saves
the rep the hardest ten minutes of their day, and the **data source and confidence
fields** serve compliance and honesty simultaneously. A rep receiving this row can send
in ninety seconds. That is what $3 buys.

---

**Read next:** `50-guardrails/legal-and-compliance.md` — **required before collecting
any record** · `20-systems/outreach.md` · `20-systems/data-and-research.md` ·
`case-studies/C3-data-cleaning-enrichment.md`, the natural predecessor.
