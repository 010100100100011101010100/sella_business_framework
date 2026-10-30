# System — Outreach

> **Status: REQUIRED READ before sending a single message to a stranger.**
>
> Prerequisites: `00-core/reasoning-guardrails.md`, your chosen case study.
> **Also required before your first send:** `50-guardrails/legal-and-compliance.md`.

---

## The doctrine

**Outreach is a research problem, not a volume problem.**

The instinct — yours especially, because you can execute it — is to send more. Two
hundred emails instead of twenty. It is the wrong instinct, and acting on it is how
sending domains die.

The arithmetic that should govern every decision here:

```
Volume approach:   500 generic emails × 0.8% reply  =  4 replies
                   Cost: a burned domain, spam complaints, no learning

Research approach:  40 researched emails × 12% reply =  5 replies
                   Cost: two days of research, a clean domain, and you now know
                   which trigger worked
```

Fewer replies is not the outcome. **More replies, a surviving domain, and a learned
signal** is the outcome. Volume is what you do *after* you know which specific research
angle produces replies — and even then, you scale the research, not the template.

**Channel precedes offer.** Decide how you will reach the buyer before you finalize what
you are selling. C5 is the framework's proof: local business owners do not read email,
so a beautiful email-based local SEO offer is not a business. If you cannot name the
channel, you do not have a business yet.

---

## Step 1 — Pick the channel, honestly

| Channel | Works for | Fails for | Operator dependency |
|---|---|---|---|
| **Cold email** | C2, C3, C6, C7 | C5, C1 | Needs a separate domain |
| **Free public work** | **C10**, C1 | C7, C9 | Wants their account |
| **Phone** | **C5** | Everything else | **Requires a willing human** |
| **Referral partnership** | C5, C7, **C9** | Slow to start | Requires their network |
| **Community participation** | C1, C4, C8, C10 | Slow | Requires existing standing |
| **Audience building** | **C4, C8** | Anything needing money in 60 days | Requires their name and patience |

**The disqualifying question for each case:** if the channel it needs is unavailable to
your operator, the case is unavailable. Go back to `00-core/initiation.md`.

---

## Step 2 — Deliverability: the physics you cannot argue with

Ignore this section and everything after it is wasted. Email deliverability is not a
best practice; it is an infrastructure constraint with hard failure modes, and the
failures are **invisible** — your emails go to spam, nobody tells you, and you conclude
the market does not want your product.

### The non-negotiables

**1. Never send cold email from the operator's primary domain.**
This is the single most important rule in this file. Spam complaints against a domain
damage its reputation permanently and invisibly. If your operator's business runs on
`theircompany.com`, a cold campaign from that domain can degrade their ability to email
customers, invoices, and their own accountant — and they will not connect the two events.

Buy a separate domain. `getdatacleaned.com`, `[brand]-hq.com`, a `.co` variant of the
main brand. Cost: about $12. **Put this on the human action queue as a blocking item on
day one**, because of the warmup lead time below.

**2. Configure SPF, DKIM, and DMARC before the first send.**
Without all three, major providers treat you as unauthenticated and route accordingly.
DMARC should start at `p=none` for monitoring, then tighten.

**3. Warm the domain for 2–3 weeks before real sending.**
A brand-new domain that starts sending 50 emails a day looks exactly like a spam
operation, because that is what spam operations do. Ramp:

| Week | Daily volume per inbox |
|---|---|
| 1 | 5–10 |
| 2 | 10–20 |
| 3 | 20–35 |
| 4+ | 35–50 **maximum** |

**Warmup is the long pole in every outbound case.** Start it on day one of the
engagement, before the pipeline is built, before the list exists. C3's 30-day plan buys
the domain on day 3 and does not send until day 15 for exactly this reason.

**4. Cap at 50/day per inbox. Permanently.**
Not a ramp target — a ceiling. To send more, add inboxes, not volume per inbox.

**5. Plain text, or nearly.**
No tracking pixels on cold email — they hurt deliverability and, under GDPR, tracking
without consent is its own problem. No images, no HTML templates, one link at most.
Cold email should look like a person wrote it, because a person should have.

### The health metrics, and what they mean

| Metric | Healthy | Warning | Stop immediately |
|---|---|---|---|
| Bounce rate | < 2% | 3–5% | **> 5%** — your list is bad; verify before sending more |
| Spam complaint rate | < 0.1% | 0.1–0.3% | **> 0.3%** — stop the campaign entirely |
| Reply rate | > 5% | 2–5% | **< 1%** — the message or the targeting is wrong |
| Open rate *(if measured at all)* | > 40% | 25–40% | < 20% — subject or sender reputation |

**Reply rate is the metric that matters.** Opens are increasingly unmeasurable and
tracking them costs you deliverability. **Bounce rate above 5% is an emergency** — it
means you are sending to unverified addresses, which is the fastest way to be
blacklisted. Verify every address before sending. It costs about $0.004 each.

**Planning anchors, not promises:** cold B2B email typically replies at 1–5%; a tight
ICP with a strong, specific trigger and a free artifact can reach 8–15%. These are
inferred ranges. **Replace them with your measured numbers after your first 100 sends
and log the replacement in `DECISION-LOG.md`** (G1, G3).

---

## Step 3 — The legal boundary

**Read `50-guardrails/legal-and-compliance.md` in full before your first send.** The
summary:

**US — CAN-SPAM.** Accurate From and Subject lines, a valid physical postal address in
every message, a working opt-out, and opt-outs honoured within 10 business days.
Applies to B2B. Penalties are per-email.

**EU/UK — GDPR and PECR.** Personal data of EU/UK individuals requires a lawful basis.
For B2B prospecting, legitimate interest is generally available but is **conditional,
not automatic**: you need a documented legitimate-interest assessment, a record of where
each contact came from, a privacy notice you can point to, a working opt-out, and the
ability to honour erasure requests. **B2C is far stricter and generally requires
consent** — if your list contains consumers rather than business contacts, stop.

**Canada — CASL.** Stricter than CAN-SPAM: requires express or documented implied
consent. Penalties are severe. If targeting Canada, get specific advice.

**LinkedIn.** Their user agreement prohibits scraping and automated activity.
Enforcement is real — restriction or permanent ban. **Do not run automation on your
operator's LinkedIn account.** The downside is losing their professional identity
permanently; the upside is saving a few dollars. Never worth it. Use LinkedIn as a
research surface a human reads, and source contact data from providers with their own
lawful basis.

**Purchased lists.** Do not use them. Poor deliverability, no lawful basis under GDPR,
and high complaint rates. Building a researched list of 200 beats buying 20,000.

---

## Step 4 — Research: the part that is actually the product

**A trigger is a dated, verifiable, recent fact about this specific company that makes
them ready now.**

### Trigger quality ladder

| Tier | Trigger | Why it works |
|---|---|---|
| **A** | Hiring for the exact role that owns your problem | Budget exists, pain is admitted, and hiring takes months while you take weeks |
| **A** | Public complaint naming the thing you fix (G2 review, forum, support thread) | They said it themselves |
| **A** | A tooling change visible in job posts or their stack | Mid-migration is the buying window |
| **B** | Funding round, 3–9 months old | Money landed, scaling pain arrived |
| **B** | New executive in the relevant function | New leaders buy; they are establishing a mandate |
| **B** | Announced move upmarket or first enterprise customer | Predictable new requirements |
| **C** | Company growth, headcount changes | Weak — true of everyone |
| **D** | "I saw your website" / "I love what you're building" | **Not a trigger.** This is filler |

**Aim for tier A or B on every prospect.** If you cannot find one, that prospect is not
ready — remove them from the list rather than sending a weaker email. A list of 40 with
tier-A triggers outperforms 400 with tier C.

### The verification rule · **G3, and it is not negotiable**

**Never state a trigger you have not verified.** Writing "I noticed you're hiring three
SDRs" when you did not check is a fabrication, and it is discovered the instant they
reply "we're not." Every trigger must have a URL you actually opened, with a date. Store
both alongside the prospect record.

This is also why researched outreach beats generic: the specificity is only persuasive
*because* it is real, and recipients can tell.

### Tooling

- **agentcash `stableenrich`** — people and organization search, Exa web search for
  trigger research, Firecrawl for page retrieval, email verification, LinkedIn data
  through a compliant provider. This covers most of the research pipeline.
- **agentcash `stableemail`** — sending. Use for cold outreach only; subscriber lists
  belong on a real ESP with list management and one-click unsubscribe.
- **Sella `search_catalog`** (`kind: "dataset"`) — industry-specific company lists.
- **Always `purchase_preview` before a research batch**, and log cost per batch with
  `business_log(kind: "result")`. Research is your largest variable cost in C3 and C6.

---

## Step 5 — The sequence

Four touches over 12 days. Then stop.

| # | Day | Purpose | Length |
|---|---|---|---|
| 1 | 0 | Trigger + free artifact + one ask | 90–130 words |
| 2 | 3 | One new piece of value. **Not "just bumping this"** | 40–60 words |
| 3 | 7 | Different angle — a different problem or a different person's perspective | 60–80 words |
| 4 | 12 | The close-out. Explicitly the last one | 30–40 words |

### Rules that decide whether it works

- **One ask per email.** Two asks halve the response rate.
- **The ask should be small.** "Worth 20 minutes?" beats "let's schedule a demo." "Want
  the other 190?" beats "let me send you a proposal."
- **Lead with the trigger, not with yourself.** The first sentence must be about them.
  If it starts with "I" or "We," rewrite it.
- **Give something in email one.** The sample, the audit, the ten leads, the repurposed
  clip. C3, C6, C10, C5 all work on this mechanic and it is the framework's single
  strongest outreach pattern.
- **State the price.** Withholding it to force a call reads as evasive and filters out
  precisely the buyers who move fast.
- **Give a real exit.** "If this isn't relevant, keep the file anyway" outperforms
  pressure, and it is honest.
- **Four touches, then stop.** After the close-out, remove them. Persistence past four
  generates complaints, and complaints are what kill domains.

### The close-out email, which outperforms every follow-up

> Subject: closing the loop
>
> Hi Sarah — I'll stop here, I don't want to keep landing in your inbox.
>
> If the duplicate problem ever becomes the thing that's annoying you, the sample I sent
> is still good and my door's open.
>
> — [name]

This gets replies at a surprisingly high rate. It removes pressure entirely, which is
often the only thing that was blocking a response.

---

## Step 6 — The data contract

All dashboards read these files. Keep the shape; the outreach dashboard depends on it.
See `30-dashboards/dashboard-spec.md`.

`data/prospects.json`
```json
{
  "id": "p_0142",
  "company": "Northwind Freight Systems",
  "domain": "northwindfreight.com",
  "contact_name": "Dana Whitfield",
  "title": "VP Revenue Operations",
  "email": "dana.w@northwindfreight.com",
  "email_verified": true,
  "email_verified_at": "2026-09-01",
  "trigger_tier": "A",
  "trigger": "Posted 'RevOps Manager — CRM Migration' naming a HubSpot→Salesforce move in Q4",
  "trigger_source_url": "https://northwindfreight.com/careers/revops-manager",
  "trigger_verified_at": "2026-09-02",
  "data_source": "stableenrich/people-search",
  "lawful_basis": "legitimate_interest",
  "status": "sequenced",
  "sequence_id": "seq_003",
  "opted_out": false
}
```

`data/touches.json`
```json
{
  "id": "t_0891",
  "prospect_id": "p_0142",
  "sequence_id": "seq_003",
  "step": 1,
  "channel": "email",
  "sent_at": "2026-09-03T09:14:00Z",
  "subject": "100 of your records, cleaned",
  "outcome": "replied",
  "outcome_at": "2026-09-03T16:02:00Z",
  "sentiment": "positive"
}
```

**`opted_out` is honoured globally and permanently, across every campaign and every
client.** Never re-add an opted-out contact. This is both a legal requirement and the
minimum standard of decency.

---

## Step 7 — Reading the results

Diagnose by *where* it fails. Each failure has a different fix, and applying the wrong
one wastes weeks.

| Symptom | Diagnosis | Fix |
|---|---|---|
| High bounce | Bad data | Verify before sending. **Stop until fixed** |
| Delivered, no opens, no replies | Deliverability or subject | Check spam placement. Simplify the subject |
| Opens, no replies | The message | Weak trigger, or the ask is too big |
| Replies, all "not now" | Timing/trigger quality | Move up the trigger ladder |
| Replies, no calls | The offer or the price | Lower the first step. Try a paid pilot below the approval threshold |
| Calls, no closes | Positioning or trust | Add proof. Reduce the first commitment |

**Do not change more than one variable at a time**, and do not judge on fewer than 30
sends. With 20 sends and one reply you know nothing; the noise dominates.

**Log every diagnosis in `DECISION-LOG.md`.** Six weeks in, the log of what you changed
and what happened is worth more than any playbook.

---

## Ten-case reference

| Case | Channel | Trigger | Free artifact | Ask |
|---|---|---|---|---|
| **C1** | Community + free component | n/a — inbound | The free component | "Join the list" |
| **C2** | Cold email | Hiring an ops/internal-tools role | Named-process diagnosis | "20 minutes?" |
| **C3** | Cold email | Hiring RevOps; CRM migration | **100 cleaned rows, attached** | "$600 for the full pass?" |
| **C4** | Social clips + sponsor email | For sponsors: they sell to your readers | Recent issues | "One slot, $600/wk" |
| **C5** | **Phone** | Map-pack position + review gap | One-page audit | "Can I email you the page?" |
| **C6** | Cold email | They are hiring AEs/SDRs | **Ten researched leads, in the email** | "200/mo for $600?" |
| **C7** | Cold email | Series A; first enterprise deal; SOC 2 in job posts | Public-gap assessment | "Full pack, $2,200?" |
| **C8** | Community, then employer email | Their role has been open 40+ days | Salary data report | "$299, refund under 3 applicants" |
| **C9** | **Referral via accountants** | n/a — warm | Free first reconciliation | "Can I do one month?" |
| **C10** | **Free public work** | They publish long-form and don't repurpose | **The repurposed content itself, published** | **None. The work is the ask** |

Note the pattern: every case leads with something free, but in **three of them — C3, C6,
C10 (bolded above) — the demonstration and the deliverable are the same object.** You do a
small piece of the actual paid work, and that artifact is the entire pitch. Those three
are also ranks 1–3 on the distribution-difficulty ranking in `00-core/case-registry.md`.
That is not a coincidence — it is the mechanic.

---

## Two worked examples

### Example A — C3, the four-touch sequence in full

**Touch 1, day 0** — trigger, artifact, price, exit:

> Subject: 100 of your records, cleaned
>
> Hi Sarah,
>
> I noticed you're hiring a RevOps Manager and the posting mentions a Salesforce
> migration in Q4. That's usually when the data problems become everyone's problem.
>
> I pulled 100 companies from your public customer page and ran them through the
> cleanup I'd do on a real dataset. It's attached. In those 100: 11 duplicates under
> different legal names, 23 with no industry code, 7 acquired since the page was
> written.
>
> If your CRM looks like that at scale, the full pass on 5,000 records is $600 and takes
> about four days. Worth doing before a migration rather than after.
>
> If not, keep the file.
>
> — [name]

**Touch 2, day 3** — new value, not a bump:

> Subject: re: 100 of your records, cleaned
>
> One thing I should have added: of the 7 acquired companies, 3 still have active
> contacts in the parent org under a different domain. Those are recoverable rather than
> dead — list attached.
>
> — [name]

**Touch 3, day 7** — different angle:

> Subject: the migration angle
>
> Hi Sarah — different thought.
>
> The reason I'd do this before the Salesforce cutover rather than after: duplicates
> migrate too, and once they're in the new system with new record IDs, deduplicating
> them is considerably harder. Most teams discover this about three weeks post-cutover.
>
> Four days, $600, and it happens before the migration rather than becoming a Q1
> project.
>
> — [name]

**Touch 4, day 12** — close-out:

> Subject: closing the loop
>
> Hi Sarah — I'll stop here rather than keep landing in your inbox. The sample's still
> good if the duplicate problem ever becomes the annoying one.
>
> — [name]

Each touch adds something. None says "just following up." Touch 3 does the real work of
the sequence — it reframes the timing as urgent using a genuine technical fact, not
manufactured scarcity. **Note that nothing in this sequence is a claim that cannot be
checked**: the eleven duplicates are in the attached file, and the migration argument is
verifiable reasoning rather than a statistic.

### Example B — the same prospect, done badly

For contrast, because this is what an unguided agent produces:

> Subject: Quick question
>
> Hi Sarah,
>
> Hope you're doing well! I came across Meridian and was really impressed by what you're
> building in the logistics space.
>
> We help companies like yours with data quality solutions. Our clients typically see a
> 40% improvement in data accuracy and save 15 hours per week on manual processes.
>
> Would you be open to a quick 15-minute call next week to explore how we might be able
> to help Meridian achieve similar results?
>
> Best,
> [name]

Everything wrong with it, in order of severity:

1. **"40% improvement" and "15 hours per week" are fabricated.** No such measurement
   exists. This is a G3 violation and it is the most common one in outreach.
2. **"We" implies a team that does not exist.** Also G3.
3. **No trigger.** "I came across Meridian" is not a reason to be emailing today.
4. **Nothing given.** The entire email asks and gives nothing.
5. **"Quick question" is not the subject.** There is no question.
6. **The ask is a call**, which is a much larger commitment than the relationship
   supports.
7. **"Companies like yours"** tells her you do not know what her company is.

This email will reply at well under 1%, generate complaints, and contribute to the
domain's decline. It is also faster to write, which is precisely why the discipline in
this file has to be explicit.

---

**Read next:** `50-guardrails/legal-and-compliance.md` — **required before sending** ·
`10-resources/ref-email-domain.md` for the DNS and warmup mechanics ·
`30-dashboards/outreach-dashboard.md` · `20-systems/sales-and-pricing.md` for what
happens after a reply.
