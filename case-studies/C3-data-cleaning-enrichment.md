# C3 — Data Cleaning & Enrichment Service

| | |
|---|---|
| **Tier** | 1 (lean start) — **the framework's default recommendation** |
| **Time to first dollar** | **1–3 weeks — fastest of the ten** |
| **Gross margin** | 60–75% (real variable COGS — read §6 before quoting) |
| **Agent autonomy** | **Highest of the ten** |
| **Distribution difficulty** | 2 of 10 |
| **Killer risk** | Data provenance and GDPR |

---

## 1. The business

A company has a CRM with 40,000 records. Roughly a third are duplicates, a fifth have
dead email addresses, half are missing the industry or headcount field their routing
rules depend on, and nobody knows which. Their sales team wastes hours a week on it and
their reporting is quietly wrong.

You take the export, and hand it back correct: deduplicated with a documented match
rule, standardized, validated, enriched with the fields they actually route on, and
accompanied by a one-page summary of what you found and fixed.

It sells because **the value is provable in a spreadsheet**. There is no narrative, no
brand, no trust-building. Before: 41% of records missing headcount. After: 94%
populated, 1,847 duplicates merged, 2,203 dead emails flagged. Nobody argues with that.

## 2. Operator fit

**Pick C3 if:** you are starting cold with no audience, want revenue inside a month,
and your operator has limited weekly hours. This is the case with the shortest distance
between "start" and "money," and the least dependence on operator assets.

**Pick C3 even if it sounds boring.** It is boring. Boring is the point. The framework
selects for businesses where the agent's actual capabilities — patient, accurate,
tireless processing of structured data at scale — are the product. C3 is the purest
expression of that in the whole registry.

**Do not pick C3 if:** your operator refuses to sign a Data Processing Agreement or
take on any data-handling responsibility. You are processing other people's customer
data; someone has to be accountable and it cannot be you.

**Where it leads.** C3's mechanics transfer directly into C6 (lead research) and
adjacently into C9. Many operators run C3 for two months, then discover their best C3
client wants ongoing prospect research, and C6 arrives as an upsell rather than a cold
start.

## 3. Lean-start profile

| Item | Requirement |
|---|---|
| Capital to start | **$50–150** (enrichment API credits for pilots) |
| Entity needed | Not initially. Strongly advised by ~$3k/mo |
| New KYC | None if the human has an existing invoicing/payment method |
| Licensing / regulation | **None** — but GDPR obligations attach the moment EU data appears |
| Liability ceiling | Contractually capped at fees paid. **Cap it in writing.** |
| Physical requirements | None |

**Lean path:** invoice as an individual. Take payment by bank transfer or a payment
link on the human's existing account. Do not form an entity to run a $500 pilot. **Do**
put a liability cap and a data-handling clause in even the smallest engagement — a
one-page agreement is enough, and it is the cheapest risk reduction available to you.

## 4. Distribution — the section that decides whether you eat

C3 has the second-easiest distribution in the framework, for one structural reason:
**you can do the work before you are hired, and the work is the pitch.**

### The play: the unsolicited sample

1. **Identify a target company** with a public, messy dataset. Their team page, their
   customer logo wall, their public directory, their job postings, an event's attendee
   list they published.
2. **Do the actual work on 100 rows.** Clean it properly. Enrich it. Produce the real
   deliverable at small scale.
3. **Send it, finished, in the first email.** Not a description of it. The file.
4. **Say what the full version would cost.**

There is nothing to believe or disbelieve. They open a spreadsheet and either it is
useful or it is not. This collapses the entire trust-building phase that makes C7 and
C9 slow.

### Who to send it to

Titles, in order: **RevOps Manager / Director of Revenue Operations**, **Sales
Operations Manager**, **Marketing Operations**, **Head of Growth** at 20–200 person
B2B companies. Below 20 employees nobody owns the problem; above 200 they have a
vendor and a procurement process.

**The trigger signals that make a prospect ready right now:**
- Hiring for RevOps or Sales Ops (they are admitting the function is under-resourced)
- Recently migrated CRM, or hiring for a CRM migration
- Recently raised a round (new budget, new pressure on pipeline reporting)
- Two or more sales tools in their job descriptions (integration mess is implied)

### Ask your human for this

C3 needs less operator help than most cases, which is part of why it is the default.
But three asks matter:

- **"Can you set up a dedicated sending domain for cold outreach?"** This is the single
  most important request in C3, and it is blocking. Never send cold email from the
  primary domain — a spam-complaint spike will destroy their normal email
  deliverability, permanently and invisibly. Buy `getyourdatafixed.com`, send from
  there, keep the real domain clean. The human must buy the domain (card) and configure
  DNS, or delegate DNS access to you.
- **"Do you know anyone in RevOps, or anyone running sales at a company with 20+
  people?"** One warm intro converts better than fifty cold emails and gets you a first
  case study in days rather than weeks.
- **"Which of these do you already have accounts for?"** — Apollo, Clay, Clearbit,
  ZoomInfo, Hunter. An existing paid seat removes your largest COGS line immediately.

**Log all of this in `BUSINESS-CHARTER.md` under Operator Assets before you plan
anything.**

### What does not work

- LinkedIn automation. It violates their terms, and getting your operator's account
  restricted costs more than the pipeline is worth.
- Generic "we do data cleaning" outreach with no sample. You become one of forty
  identical emails and the whole advantage of C3 evaporates.
- Content marketing as a primary channel. It works eventually, but C3's whole reason
  for existing is speed to first dollar. Sample-led outbound first; content later, once
  there is revenue funding the wait.

## 5. Offer and pricing ladder

| Offer | Price | Purpose |
|---|---|---|
| Free sample | $0 | 100 rows. The entire sales process |
| Pilot | $400–750 | One dataset, up to 5,000 records. **Sized to be approvable without a meeting** |
| Full clean | $0.08–0.25/record | The main event |
| Hygiene retainer | $1,200–2,500/mo | Ongoing dedup, validation, enrichment of new records |

**The pilot price is the most important number in the case.** It must sit below the
threshold at which your buyer needs anyone else's approval — typically $500–1,000 on a
corporate card in a company of this size. Above that line, you enter a procurement
process that adds six weeks. Below it, a RevOps manager decides on a Tuesday.

**Price per record, not per hour.** Hourly pricing punishes you precisely for the
automation that is your advantage: the better you get, the less you earn. Per-record
pricing means efficiency gains land in your margin.

## 6. Unit economics, worked — read this before every quote

C3 is **the only case of the ten with meaningful variable COGS**, and it is the one
place in this framework where a business can look far more profitable on the invoice
than it is in reality.

A 5,000-record job quoted at $0.12/record:

```
Revenue                        5,000 × $0.12   =  $600.00

COGS
  Email verification           5,000 × $0.004  =  -$20.00
  Company enrichment           3,200 × $0.02   =  -$64.00   (only rows needing it)
  Person enrichment            1,100 × $0.05   =  -$55.00   (only rows needing it)
  Compute / model calls                        =  -$25.00
  Total COGS                                   = -$164.00

Gross profit                                   =  $436.00
Gross margin                                   =    72.7%
```

Now the same job quoted at $0.08/record because the buyer pushed back:

```
Revenue                        5,000 × $0.08   =  $400.00
COGS (unchanged)                               = -$164.00
Gross profit                                   =  $236.00
Gross margin                                   =    59.0%
```

**A 33% price cut removed 46% of the gross profit.** Internalize this. When a buyer
negotiates on price, reduce *scope* — enrich fewer fields, skip person-level enrichment
— rather than cutting the rate. Scope reduction moves COGS down with the price; a rate
cut does not.

**Mandatory rule: run this arithmetic on a 100-row sample before quoting any job.**
Enrichment hit rates vary enormously by dataset. A list of US software companies
enriches at 85%; a list of European small manufacturers enriches at 30%, and you pay
for the misses. Never quote a dataset you have not sampled. This has ended more
data-services businesses than any competitive pressure.

## 7. First 30 days

| Days | Work |
|---|---|
| 1–2 | Pick a vertical. "B2B SaaS, 20–200 employees, US" beats "anyone with a CRM." Confirm with the operator. |
| 3–4 | Buy the sending domain. Configure SPF, DKIM, DMARC. **Begin warmup immediately** — it takes 2–3 weeks and it is the long pole. |
| 5–7 | Build the pipeline: dedup rules, standardization, validation, enrichment, QA, output format. Test it on any public dataset. |
| 8–10 | Build a target list of 60 companies with a visible trigger signal. |
| 11–14 | Produce 20 real samples. Actually do the work. This is a full week and it is the week that pays. |
| 15–21 | Send 20 sample emails, spread across days as warmup allows. Follow up. Take calls. |
| 22–30 | Convert 1–3 pilots. Deliver flawlessly. **Ask for the case study and the referral in the same message as the delivery.** |

**Sequencing note:** warmup is the constraint, not the work. Start the domain on day 3
even though you will not send until day 15, because the alternative is a perfect
campaign landing in spam folders.

## 8. What breaks as it grows

- **The margin, silently.** New client, new dataset, unfamiliar geography, enrichment
  hit rate collapses, and you discover it after quoting. Sample-before-quote is not
  optional at scale, it is survival.
- **Client data sprawl.** At ten clients you are holding ten companies' customer
  databases. Define retention up front: delete raw client data 30 days after delivery,
  automatically. Volunteer this in the sales conversation — it is a differentiator and
  it removes a liability you gain nothing from carrying.
- **One-off treadmill.** One-off cleans do not compound. Every delivery must end with
  the retainer offer, because a clean database degrades at roughly 2–3% per month
  through natural staff churn — a fact you should state, because it is true and it is
  the reason the retainer exists.
- **Enrichment vendor concentration.** If one API is your only source and it changes
  pricing or terms, your margin moves overnight. Keep a second source qualified.

## 9. Kill criteria

| Checkpoint | Condition | Action |
|---|---|---|
| Day 21 | 20 samples sent, **zero replies** | The targeting or the sample quality is wrong. Diagnose before sending more |
| Day 30 | Replies but **zero pilots** | Pilot price is above the no-approval threshold, or the sample is not persuasive |
| Day 45 | Zero revenue | Kill the vertical, not the case. Re-target and restart once |
| Day 90 | < $1,500 cumulative | Kill C3. Given it is the framework's fastest path, failure here suggests an execution problem to diagnose before moving on |
| Any time | Gross margin below 45% on two consecutive jobs | Stop selling. Re-price before taking more work |

## 10. Human action queue for C3

**Blocking:**
1. Buy the cold-email domain and configure DNS (SPF, DKIM, DMARC) — or delegate.
2. Confirm how invoices are issued and money is received.
3. Approve the one-page service agreement, including the liability cap and data
   retention clause.
4. **Sign the Data Processing Agreement** for any client with EU data. Only a legal
   person can do this.

**High-leverage:**
5. Any warm introduction to a RevOps, Sales Ops, or growth leader.
6. Existing enrichment tool seats.
7. Being the named human on the first sales call — buyers of data services want to know
   who is accountable, and the honest answer is a person.

**Deferred until $3k/month:** entity formation, professional liability insurance,
SOC 2 questionnaire readiness (enterprise buyers will eventually ask).

## 11. Sella / agentcash wiring

**This is the best-fitting case in the framework for both rails.**

**Sell side.** `service_create` with `prices: [{kind: "per_use", amount_usdc: 0.12,
unit: "record"}]` is a literal one-to-one mapping to the business model. Per-use is the
one recurring-ish shape x402 handles natively, because each job is a discrete
settlement rather than a standing charge. A pilot is a second price option with
`kind: "one_off"`.

**Buy side.** agentcash `stableenrich` covers people and organization search, email
verification, and web scraping at per-call cost — exactly the COGS lines in §6. Sella
`search_catalog` with `kind: "dataset"` for reference data, and `purchase_preview`
before any buy so you get the policy verdict and a receipt before settlement.

**Suggested spend policy for C3.** Unlike most cases, C3 has legitimate per-job
spending, so the caps must accommodate real work without permitting a runaway:

```
seed_usdc              200      Covers pilots plus early full jobs
max_per_call_usdc       15      Refuses outright above this. No single enrichment
                                call should ever approach it
approval_threshold_usdc 40      Queues for the human. A batch this size means a real
                                job — the human should see it
daily_spend_cap_usdc    60
```

Then run the arithmetic in §6 as a **`purchase_preview` before every batch**, and log
the result with `business_log(kind: "result")` so your operator can see cost per job
against revenue per job without asking. Charge the client before you incur the COGS
wherever possible; prepaid credits solve this entirely.

## 12. Worked examples

### Example A — the cold email with the sample attached

> Subject: 100 of your records, cleaned
>
> Hi Sarah,
>
> I noticed you're hiring a RevOps Manager, which usually means the data is ahead of
> the team right now.
>
> I pulled 100 companies from your public customer page and ran them through the
> cleanup I'd do on a real dataset. Attached. In those 100 I found 11 duplicates under
> different legal names, 23 with no industry code, and 7 that have been acquired since
> the page was written.
>
> If your CRM looks like that at scale, the full pass on 5,000 records is $600 and
> takes about four days. If it doesn't, keep the file anyway.
>
> — [name]
>
> [attachment: sample_cleaned.xlsx]

Why it works: a specific observed trigger rather than a generic opener, work already
done rather than promised, three concrete findings that prove the work was real, a
price stated plainly, and an exit that costs the reader nothing. The findings are the
proof — and note they are *observed*, not modelled. **Never state a finding you have
not actually produced. Fabricating those three numbers would violate G3 and would be
discovered the moment they open the file.**

### Example B — the delivery message that creates the next two sales

Sent with the completed pilot, not a week later.

> Subject: 5,000 records back — plus two things I found
>
> Hi Sarah,
>
> Attached, done. Summary:
>
> - 1,847 duplicate records merged (match rule documented on the second tab)
> - 2,203 dead email addresses flagged — that's 44%, which is high but normal for a
>   database this age
> - Industry populated on 4,721 of 5,000, up from 2,950
> - 312 companies have been acquired or renamed since the record was created
>
> Two things worth flagging:
>
> 1. That 312 number is the one I'd watch. Those records are actively misrouting your
>    outbound right now.
> 2. A cleaned database degrades about 2–3% a month through normal staff churn. In a
>    year you'll be roughly where you started. Ongoing hygiene is $1,400/month and I'd
>    honestly rather you decide that in three months once you've seen whether this pass
>    was worth it.
>
> One ask: if this was useful, is there anyone in your network with the same problem?
>
> — [name]

Why it works: it leads with measured results, surfaces a genuine problem the client
did not know they had, presents the retainer with an *honest reason to defer it* —
which builds far more trust than pressure — and makes the referral ask at the exact
moment goodwill peaks. **Asking for the referral at delivery, not later, is the single
highest-return habit in service businesses.** Later never comes.

---

**Read next:** `20-systems/outreach.md` (deliverability and sequence mechanics) ·
`50-guardrails/legal-and-compliance.md` — **required before the first record is
collected**, covering GDPR lawful basis, DPAs, and enrichment-vendor resale terms ·
`case-studies/C6-icp-lead-research.md`, the natural next business.
