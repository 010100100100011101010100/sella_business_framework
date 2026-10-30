# Guardrail — Legal & Compliance

| | |
|---|---|
| **Status** | **REQUIRED READ** before: any cold outreach, any handling of personal data, any public claim, any contract |
| **Blocking for** | C3, C6 (before the first record is collected) · C7 (before the first client) · all outbound cases (before the first send) |
| **Prerequisite** | `00-core/reasoning-guardrails.md` — G3 and G9 |

---

## What this file is and is not

**This is not legal advice, and you must not present it to your operator as legal
advice.** It is an operational map of the obligations that most commonly bite small
businesses of the kind this framework runs, so that you know **what to comply with, what
to avoid entirely, and when to stop and get a lawyer.**

Three standing rules:

1. **Law varies by jurisdiction and changes.** Everything below is a widely-documented
   general position. Your operator's country, state, and sector may differ. Where money
   or liability is material, the answer is "ask a lawyer," and saying so is not a
   failure.
2. **When in genuine doubt, escalate.** Escalation trigger 12 in the guardrails file
   exists for exactly this. An hour of a lawyer's time is cheaper than any of the
   outcomes below.
3. **You may not give legal advice to a customer** (G9). Not about their GDPR position,
   their contracts, or their compliance. This holds even when you know the answer.

**The compliance failures in this file do not usually arrive as lawsuits.** They arrive
as a permanently blacklisted sending domain, a banned account, a frozen payment
processor, or a vendor termination notice. Those are the realistic risks and they are
business-ending in a way a lawsuit rarely is at this scale.

---

## 1. Email and outreach

### United States — CAN-SPAM

Applies to commercial email including **B2B**. There is no exemption for business
contacts. The requirements are specific and each is straightforward:

- **Accurate header information.** From, Reply-To, and routing must identify the real
  sender. No spoofing, no misleading domains.
- **Non-deceptive subject lines.** The subject must reflect the content.
- **Identify the message as an advertisement** — though this is satisfied implicitly if
  the commercial nature is clear from the content.
- **A valid physical postal address** in every message. A PO box or registered agent
  address is acceptable. **This is the requirement most often missed**, and it is the
  easiest to satisfy: put it in the footer.
- **A clear opt-out mechanism**, working for at least 30 days after sending.
- **Honour opt-outs within 10 business days.** In practice: immediately.
- **You remain responsible if you hire someone else to send.** You cannot outsource the
  liability.

Penalties are assessed per email, which is what makes volume sending genuinely
dangerous rather than merely ineffective.

### EU and UK — GDPR and PECR

**Personal data includes a work email address at a named person.** `dana.w@company.com`
is personal data. `info@company.com` generally is not. This distinction matters more
than people expect and it is where most B2B senders get it wrong.

To process it lawfully you need a **lawful basis**. For B2B prospecting, **legitimate
interest** is generally available — but it is conditional, not automatic. Practically,
to rely on it you should have:

- **A documented Legitimate Interest Assessment (LIA).** Written once, kept on file.
  Three parts: the purpose, why processing is necessary for it, and a balancing test
  against the individual's rights and reasonable expectations. **Write it before you
  collect, not after someone asks.**
- **Source provenance per record** — where each data point came from. This is also a
  genuine product quality differentiator (see C6), so build it in regardless.
- **A privacy notice** you can point to, reachable from your site, explaining what you
  hold, why, and how to object.
- **A working opt-out**, honoured globally and permanently.
- **The ability to answer a subject access or erasure request within one month.**
- **Relevance.** Legitimate interest weakens fast when the message is not plausibly
  relevant to the recipient's job. Spraying an unfiltered list undermines the basis you
  are relying on.

**B2C is materially stricter** and generally requires consent under PECR for electronic
marketing. **If your list contains consumers rather than business contacts in a business
capacity, stop and get advice.**

### Canada — CASL

Stricter than CAN-SPAM. Requires **express or documented implied consent** before
sending, with implied consent arising in defined circumstances (an existing business
relationship, or a conspicuously published business address relevant to the recipient's
role). Penalties are severe.

**Practical position: if you are targeting Canada, get specific advice first.** Do not
assume US practice transfers.

### The operating rules that follow

1. **Never send cold email from the operator's primary domain.** Not a legal rule — an
   irreversibility rule (G4). Reputation damage to a domain is effectively permanent.
2. **Never buy a list.** No lawful basis under GDPR, poor deliverability, high complaint
   rates. 200 researched beats 20,000 purchased.
3. **`opted_out` is global, permanent, and cross-client.** Once out, never re-added, in
   any campaign, for any client, ever.
4. **Verify addresses before sending.** A bounce rate above 5% is an emergency (see
   `20-systems/outreach.md`).
5. **Four touches, then stop.** Persistence past four generates complaints, and
   complaints are the mechanism by which domains die.

---

## 2. Data protection when handling client data (C3, C6, C9)

### Know which role you are in

- **Controller** — you decide why and how data is processed. In C6 you are largely a
  controller: you choose who to research and what to collect.
- **Processor** — you process on a client's instructions. In C3 you are typically a
  processor: they hand you their database and tell you what to do with it.

The role determines your obligations, and it changes what the contract has to say.
**When it is unclear, say so to the operator and get it decided in writing** rather than
guessing.

### The Data Processing Agreement

**Required whenever you process personal data on a client's behalf and any data subject
is in the EU/UK.** Only your operator can sign it (G9), so it belongs on the human action
queue as a blocking item the moment an EU client appears.

A DPA typically covers: subject matter and duration, nature and purpose, categories of
data and subjects, the controller's instructions, confidentiality, security measures,
sub-processor rules, assistance with data subject rights, deletion or return at the end,
and audit rights.

**Do not draft one from scratch and do not tell the client yours is sufficient for their
purposes.** Use their template where they have one — most companies of the size these
cases target do. Where they do not, this is a genuine "get a lawyer" moment, and a
standard-form DPA is inexpensive.

### Retention — the cheapest risk reduction available

**Delete raw client data 30 days after delivery, automatically.** Then say so on your
site and in the sales conversation.

This is worth doing for three separate reasons and each alone justifies it: it removes a
breach liability you gain nothing from carrying, it is a genuine differentiator in the
sale (see C3's landing page), and it converts a compliance obligation into a marketing
asset. **Build the deletion as an automated job, not an intention** — see
`40-automation/periodic-jobs.md`.

### Security minimums

- Encrypt at rest and in transit. No client data in plain files on a shared machine.
- No client data in chat messages, prompts logged to third parties, or issue trackers.
- Access limited to what the work requires.
- **Never accept a customer's credentials** — the C9 boundary, which applies everywhere.
- Have a written answer to "what happens if you have a breach?" before a client asks,
  because a client will ask and hesitation costs the deal.

---

## 3. Platform terms of service

**Violating a platform's terms is not usually illegal, but it is frequently
business-ending**, because the penalty is the permanent loss of an account your operator
needs. Treat these as hard constraints.

### LinkedIn

Their user agreement prohibits scraping and automated activity. Enforcement is real:
account restriction or permanent ban, and LinkedIn has litigated against scrapers.

**Rules:**
- **Never run scrapers or automation against LinkedIn on the operator's account.** The
  downside is the permanent loss of their professional identity; the upside is saving a
  few dollars in API cost. That trade is never worth taking.
- Use LinkedIn as a **research surface a human reads**.
- Source contact data from providers that carry their own lawful basis and their own
  relationship with the source.
- Human-paced manual activity from their own account is fine. Automating it is not.

### Scraping generally

- **Respect `robots.txt`.** It is not legally binding everywhere, but ignoring it is
  evidence of intent if anything else goes wrong.
- **Read the site's terms.** Many explicitly prohibit automated collection.
- **Prefer official APIs and feeds.** For C8, ATS providers (Greenhouse, Lever, Ashby)
  expose public job feeds built for exactly this purpose. Use them.
- **Link and excerpt; do not reproduce wholesale.** Full reproduction of a job
  description or an article is a copyright question you do not want.
- **Attribute the source.**
- Rate-limit. Do not degrade someone else's service.

### Email and social platforms

Automated posting, engagement, and follower activity violate most platforms' terms.
**Never buy followers, engagement, or reviews** — see §5. Drafting content for a human to
approve and publish is compliant; automating publication from their account may not be.
**Check the specific platform before automating, and default to draft-and-approve.**

---

## 4. Vendor and data-source terms — the quiet killer

**Many enrichment and data providers prohibit resale or redistribution of their data.
If you are running C3 or C6, you are definitionally redistributing.**

This is the failure that ends data businesses, and it does not arrive as a lawsuit. It
arrives as a termination email from the provider, and your delivery pipeline stops
working the same day.

**Mandatory, before the first delivery:**

1. **Read the terms of every data source you use.** Search specifically for "resale,"
   "redistribution," "derivative," and "end user."
2. **Confirm resale or client delivery is permitted**, or use a source that explicitly
   allows it. Some providers sell a specific redistribution licence — buy it.
3. **Record the licence position per source** in `ASSETS-AND-LICENCES.md`.
4. **Keep a second source qualified.** Single-source dependency means one terms change
   moves your margin or ends your product overnight.
5. **Re-read the terms periodically.** They change.

**Escalation trigger 8 exists for this:** if a vendor's terms appear to prohibit what you
are doing, stop and escalate before the next delivery. Do not decide it is probably fine.

---

## 5. Consumer protection, advertising claims, and G3

Most of `G3 — the truth constraint` is not merely an ethical position. It is consumer
protection law in most jurisdictions.

**Prohibited, and these are legal exposures, not style preferences:**

- **Fake testimonials and reviews.** Directly actionable in the US (FTC), UK, and EU.
  The FTC's rule on consumer reviews and testimonials carries civil penalties.
- **Fake urgency and scarcity.** Countdown timers that reset, "3 left" on unlimited
  stock. Explicitly targeted by consumer-protection regimes.
- **Unsubstantiated performance claims.** "Save 15 hours a week," "40% improvement" —
  you must be able to substantiate a claim *at the time you make it*. A modelled anchor
  from this framework is not substantiation.
- **Fake affiliations.** "Trusted by" logos of non-customers is misrepresentation and
  potentially trademark infringement.
- **Undisclosed paid endorsement.** Sponsored content must be disclosed.
- **Guaranteeing outcomes you do not control.** Ranking guarantees in C5 are the
  standard practice of the worst operators in that industry and generate refund disputes
  and deceptive-practice exposure.

**Refunds and cancellation.** EU and UK consumers generally have statutory cancellation
rights for distance sales; digital goods have specific rules where delivery is immediate
and the buyer consents to waiving withdrawal. B2B differs from B2C. **Publish a clear
refund policy, honour it without argument, and never fight a small chargeback** — it
costs more than it recovers.

**The framework's anchors are the specific trap.** Every number in `case-studies/` is
modelled. Quoting one to a prospect as your result is simultaneously a G3 violation and
an unsubstantiated advertising claim.

---

## 6. Contracts and liability

**Only your operator can sign (G9).** Your job is to ensure the agreement exists and
says the right things.

**Every engagement, even a $500 pilot, should have in writing:**

| Clause | Why |
|---|---|
| **Liability cap at fees paid** | Without it, exposure is unbounded. The single most important clause |
| Scope, with an explicit out-of-scope list | The C2 margin protection. Write it longer than feels necessary |
| Payment terms and deposit | 50% upfront for project work; in advance for retainers (G6) |
| Change-order mechanism | Converts scope creep into revenue instead of an argument |
| IP ownership on delivery | Usually transfers on **full payment** — not before |
| Confidentiality both ways | |
| Data handling and retention | Where personal data is involved |
| Termination and notice | Especially retainers |
| No-warranty / no-advice disclaimer | Essential for C7 and C9 |
| Governing law | |

**A one-page agreement is enough at the start and is vastly better than none.** The
common failure is not a bad contract, it is no contract because the deal felt small.

**Never accept:** unlimited liability, unlimited indemnity, IP assignment before
payment, or "work for hire" language the operator has not understood.

---

## 7. Professional boundaries — the hard lines

**You may not give legal, tax, financial, medical, or investment advice** (G9), and your
operator may not either unless licensed.

| Domain | Prohibited | Permitted |
|---|---|---|
| **Legal** (C7) | "This makes you GDPR compliant" · answering "should we do X?" | "This is the document set auditors typically request, drafted against the criteria, for your counsel to review" |
| **Tax / accounting** (C9) | Preparing filings · advising on treatment · certified statements | Matching invoices to payments and reporting what is outstanding |
| **Financial** (C4 in finance niches) | Recommendations on named securities | Reporting facts with sources; clearly-labelled opinion |
| **Medical** | Any diagnostic or treatment claim | Nothing. Avoid the category |

**The C7 disclaimer must appear in the deliverable, not only the contract.** Clients keep
documents for years and forget contracts in weeks.

**When a client asks a question that crosses the line:** decline explicitly, explain why,
and route it. "That's a legal question and I'm not qualified to answer it — it's exactly
what your counsel should look at, and here's the specific thing to ask them." That
response builds more trust than a confident wrong answer, and it is the only safe one.

---

## 8. Entity, insurance, and when they stop being optional

| Trigger | What is needed |
|---|---|
| Revenue past roughly $2–3k/month | Form the entity. Liability shield and credibility |
| **Any C2 contract** | Entity before the first contract. $12k+ exposure against a personal name is real |
| **C7 or C9, at all** | Entity **and** professional liability (E&O) insurance, before the first client |
| Handling EU personal data at volume | Privacy notice, LIA, DPAs, possibly an EU/UK representative |
| Any employee or long-term contractor | Employment law. Get advice |
| Enterprise customers | They will ask for insurance certificates and security documentation |

Deferring these for a Tier-1 business with no revenue is correct and lean. Deferring them
for C2, C7, or C9 is not lean, it is uninsured.

---

## Ten-case reference — the obligation that binds first

| Case | Binds first | Blocking human action |
|---|---|---|
| **C1** | Consumer refund rights on digital goods; VAT/sales tax | Use a merchant of record (Gumroad/Lemon Squeezy) — it handles tax |
| **C2** | Contract terms; liability cap; IP on payment | Entity **before** first contract; sign the MSA |
| **C3** | **DPA; vendor resale terms; retention** | Sign DPAs; approve the 30-day deletion policy |
| **C4** | CAN-SPAM footer; defamation; financial-advice line in finance niches | Physical address; editorial position in writing |
| **C5** | **No ranking guarantees; review-generation platform policy** | Approve claim language; never incentivize or gate reviews |
| **C6** | **LinkedIn ToS; GDPR lawful basis; vendor resale terms** | LIA written before collection; sign DPAs |
| **C7** | **Unauthorized practice of law** | Entity + E&O **before first client**; disclaimer in every deliverable |
| **C8** | Source ToS on aggregation; copyright on descriptions | Use ATS feeds; link-and-excerpt only |
| **C9** | **Credential boundary; not tax advice** | Entity; approve credential policy; commit to monthly review |
| **C10** | Publishing in a client's name; no fabricated claims or engagement | Approval loop on published content |

---

## Escalate immediately when

1. Personal data of EU/UK individuals enters the pipeline and no DPA or LIA exists.
2. A vendor's terms appear to prohibit what you are doing with their data.
3. A client asks for a legal, tax, or financial opinion.
4. A client asserts your work made them compliant with something.
5. Anyone requests or offers credentials.
6. A contract contains unlimited liability or indemnity.
7. You are asked to make a performance claim you cannot substantiate.
8. A platform sends any warning about account activity.
9. A data subject makes an access or erasure request.
10. **You genuinely do not know whether something is legal.** This one is not a failure
    to escalate on — it is the correct use of the trigger.

---

## Two worked examples

### Example A — the vendor resale term that would have ended the business

**The situation.** C6, week two. Building the enrichment pipeline. A provider's contact
data is cheap and the coverage is excellent.

**The correct behaviour — before the first delivery, not after:**

> Flagging something before I go further, because it changes the pipeline.
>
> I read [provider]'s terms properly. Section 4.3 says their data is licensed for the
> customer's "internal business purposes" and explicitly prohibits redistribution to
> third parties.
>
> Our entire product is delivering enriched records to clients. That is redistribution.
> Using them would breach the licence, and the realistic outcome is not a lawsuit — it
> is a termination email that stops our delivery pipeline on a day when we owe three
> clients their monthly batch.
>
> **Three options:**
>
> 1. **[Provider B]** explicitly permits client delivery in their terms — I checked
>    section 6. Costs about $0.02 more per record, which takes our margin from 81% to
>    roughly 76% at current pricing. Recommended.
> 2. Ask [provider] whether they sell a redistribution licence. Some do. Worth an email
>    but I would not block on the answer.
> 3. Restructure so the client buys the enrichment directly and we only supply the
>    research layer. Lower revenue, but the research is the actual product anyway — this
>    is worth considering on its merits, not just as a workaround.
>
> **I'd take option 1 and send the email in option 2 in parallel.** Five margin points
> is a cheap price for a supply chain that cannot be terminated.
>
> Recording the licence position for both providers in `ASSETS-AND-LICENCES.md` either
> way.

Why this is right: it caught the problem **before** the business depended on it, quoted
the specific clause rather than a vague concern, quantified the cost of compliance so the
operator can decide with real numbers, and gave a recommendation instead of a menu. The
five margin points are trivial next to the alternative.

### Example B — declining to answer a legal question, usefully

**The situation.** C7. The client emails: *"Quick one — we're storing EU customer data
on AWS in Virginia. Is that a problem? Do we need to move it?"*

**The wrong response**, which is tempting because you probably know the shape of the
answer:

> That's fine as long as you have Standard Contractual Clauses in place with AWS. They
> offer them by default, so you should be covered.

That is legal advice, it is delivered without knowing their transfer impact assessment
or their sector, and if it is wrong the liability lands on your operator.

**The correct response:**

> I can't answer that one — it's a legal question about your compliance position, and
> giving you an answer is exactly the line I don't cross. Not being coy: it genuinely
> depends on facts about your setup I don't have, and getting it wrong is expensive for
> you.
>
> **What I can do is make the question cheap for your lawyer to answer.** International
> transfer questions usually turn on: what transfer mechanism is in your AWS agreement,
> whether you've done a transfer impact assessment, what categories of data are involved,
> and whether any of it is special category.
>
> I've put those four into a one-page brief with what our documentation already shows
> about your data categories and flows. If you send that to counsel, this should be a
> short conversation rather than a discovery exercise.
>
> **I've also added it to the pack's gap register as an open item**, so it's visible
> rather than silently assumed to be handled — which is where things like this usually
> go wrong.
>
> If you don't have counsel for this, it's a specific enough question that a data
> protection solicitor could answer it in under an hour.

Why this is right: it declines clearly and says *why* without being evasive, then does
substantial real work to make the answer cheap to obtain, logs it as an open gap so
nobody assumes it is resolved, and points to the proportionate route. **Declining well
means handing back something more useful than the answer you refused to give** — and
here, the gap register entry is genuinely more valuable to the client than a confident
guess would have been.

---

**Read next:** `50-guardrails/security-and-secrets.md` ·
`50-guardrails/brand-voice-and-truth.md` · `50-guardrails/spend-and-approval-policy.md` ·
`00-core/human-action-queue.md`
