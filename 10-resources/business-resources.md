# Business Resources — Routing Index

| | |
|---|---|
| **Status** | **REQUIRED READ** before acquiring or setting up anything |
| **Prerequisite** | `00-core/viability-screen.md` (T1 money path), `00-core/human-action-queue.md` |
| **Output** | The Resources section of `BUSINESS-CHARTER.md` + blocking items on the human action queue + `.claude/required-reads.md` |

---

## How this file works

This is the **index**. It does not tell you how to set anything up. It tells you
**what your business actually needs, in what order**, and routes you to the referenced
file for each one.

**The referenced-file mechanic:**

1. You decide the business needs a website.
2. You read `ref-website.md`.
3. **That file is now a compulsory read for this business.** Record it in
   `.claude/required-reads.md` so any agent picking this work up later reads it too.

Files you do not need remain unread. That is the point — an agent that reads all twelve
resource files has spent its context on infrastructure it will never build.

---

## The principle: reuse, then defer, then acquire

**Every resource has four costs**, and the first is the only one people count:

| Cost | Example |
|---|---|
| Money | $12/year domain, $49/month ESP |
| Setup time | Three weeks of domain warmup |
| **Maintenance** | Every account is a thing that breaks, expires, or gets suspended |
| **Liability surface** | Every account holds data, has a login, can be compromised |

So the order is always:

**1. Reuse what the operator has.** Their Gumroad, their X account with real followers,
their existing Clay seat, their domain. This is free, instant, and usually better —
an established account outperforms a new one by an order of magnitude, and new accounts
posting links get algorithmically suppressed.

**2. Defer what is not blocking.** You do not need a logo, a brand system, a company
email signature, or a LinkedIn company page to make your first sale. You need a way to
be paid and a way to reach a buyer.

**3. Acquire only what the next two weeks require.**

**Run the asset inventory from `initiation.md` Section 2 before acquiring anything.**
The most expensive mistake in this file is discovering in week four that the operator
already had the thing you spent a week building.

---

## The universal minimum

Nearly every business needs exactly these to start. Nothing else is blocking.

| # | Resource | Route to | Lead time |
|---|---|---|---|
| 1 | **A way to receive money** | `ref-payments-and-billing.md` | 1 day · **hard blocker** |
| 2 | **A way to reach the buyer** | the channel's file, per your case | varies |
| 3 | A place to put the offer | `ref-website.md` — *often not needed week one* | hours |

**That is the list.** Everything else in this index is conditional.

**Resource #1 is a hard stop.** The T1 money-path test exists because agents build for
three weeks and then discover the operator cannot be paid. Walk it end to end on day
one: customer decides → pays by what method → lands where → operator can access it.

---

## The full resource map

Read the routing question. If the answer is no, do not read the file.

### Identity and communication

| Resource | Read the file when | Route to |
|---|---|---|
| **Sending domain** | Any cold email at all | `ref-email-domain.md` · **3-week lead time — decide day one** |
| **Business email** | Any client correspondence | `ref-email-domain.md` |
| **Auth / accounts / secrets** | Any third-party account or API key | `ref-auth-and-identity.md` |
| **Phone number** | C5, or any voice channel | `ref-auth-and-identity.md` §phone |

### Presence

| Resource | Read the file when | Route to |
|---|---|---|
| **Website** | Prospects will check you exist, or you sell to strangers | `ref-website.md` |
| **Design system** | **Any** site or dashboard is being built | `ref-design-system.md` |
| **Hosting** | You have a website | `ref-hosting-and-infra.md` |
| **X / Twitter** | Developer or founder audience (C1, C2, C10) | `ref-social-x.md` |
| **LinkedIn** | B2B professional audience (C2, C4, C6, C7, C10) | `ref-social-linkedin.md` |
| **YouTube** | Video is a primary channel (C10, some C4) | `ref-social-youtube.md` |

### Commerce

| Resource | Read the file when | Route to |
|---|---|---|
| **Payments and billing** | **Always.** Resource #1 | `ref-payments-and-billing.md` |
| **Procurement / buying** | You will spend money on inputs (C3, C6, C10) | `ref-procurement-marketplaces.md` |

### Delivery artifacts

| Resource | Read the file when | Route to |
|---|---|---|
| **Documents and decks** | Deliverables are documents (C7, C9), or you pitch with a deck | `ref-docs-and-decks.md` |
| **Dashboards** | You need to see the business, or a client does | `30-dashboards/dashboard-spec.md` |

---

## Sequencing — what to acquire, and when

The mistake is acquiring everything in week one. The correct order is driven by **lead
time and blocking status**, not by importance.

**Day 1 — the long-lead and hard-blocking items only**
- Payment rail (blocking, and it is the operator's action)
- **Sending domain, if there will be any cold email.** Warmup is 2–3 weeks and it is the
  critical path. Buy it before the pipeline exists, before the list exists, before you
  know your exact offer. It warms while you build.

**Week 1 — what the first outreach needs**
- Business email address
- Whatever the demonstration artifact requires (usually nothing)
- The operator's existing social accounts, confirmed and permissioned

**Week 2–3 — what the first sale needs**
- A one-page site, *if* the buyer will check (`ref-website.md` Step 0 decides this)
- A one-page service agreement
- Invoicing mechanics

**After first revenue**
- Better website, real brand, dashboards, additional socials, company pages

**Deferred to ~$2–3k/month**
- Entity, business banking, insurance, trademark
- **Exceptions: C2, C7, and C9 need the entity and (for C7/C9) insurance *first*.** That
  is not lean, it is the price of those cases.

---

## Ask the human before acquiring anything

Nine questions, from `initiation.md` §2, that most often eliminate an acquisition:

1. Do you already have a way to receive money?
2. Do you own any domains?
3. Do you have a social account with a real following — which platform, roughly how many,
   who are they?
4. Do you have an email list?
5. Which tools do you already pay for? *(Apollo, Clay, Canva, an ESP, hosting)*
6. Do you have a business email address and phone number?
7. Do you have a GitHub, portfolio, or public body of work?
8. Will you approve and publish content I draft, from your accounts?
9. Do you have brand colours, a logo, or a look you want this to match?

**Log every answer under Operator Assets in `BUSINESS-CHARTER.md`.**

**Ask specifically, not generally.** "Do you have social media?" produces nothing. "Do
you have an X account with 300+ developer followers, and will you publish two posts a
week that I draft?" produces something you can plan around.

---

## What you may not acquire (G9)

Only your operator can:

- Open a payment processor, bank, or merchant account (KYC)
- Buy a domain (card)
- Register an entity
- Accept terms of service on their own behalf
- Complete identity verification anywhere

**Everything in this index that requires one of those goes on the human action queue as
a blocking item, with what it unblocks and its lead time.** See
`00-core/human-action-queue.md` for how to ask well.

---

## Ten-case reference — the minimum viable resource set

Only what is genuinely blocking. Everything else is deferred.

| Case | Day-1 blocking | Week 1–3 | Deferred |
|---|---|---|---|
| **C1** | Merchant account (Gumroad/LS) | GitHub + X (operator's), storefront page | Domain, real site, LinkedIn |
| **C2** | Payment rail, **entity** | Business email, credibility site, MSA | Socials, brand, dashboards |
| **C3** | Payment rail, **sending domain** | Business email, one-page site, agreement + DPA | Brand, socials, entity |
| **C4** | ESP account, physical address | Landing page (ESP-hosted is fine), operator's social | Own domain, custom site, paid tier |
| **C5** | Payment rail, **business phone** | Credibility site, GBP access process | Socials, brand |
| **C6** | Payment rail, **sending domain** | Business email, one-page site + sample, DPA | Brand, socials |
| **C7** | **Entity + E&O**, payment rail | Business email, credibility site, disclaimer language | Socials, dashboards |
| **C8** | ESP account, payment for posts | Landing page, community presence | Job board site, own domain |
| **C9** | Payment rail, **entity** | Business email, minimal site, agreement | Socials, brand, dashboards |
| **C10** | Payment rail (or prepaid) | Operator's or studio social account, portfolio page | Domain, custom site, LinkedIn page |

**Read the pattern in the last column.** Brand, socials, and dashboards are deferred in
almost every case. They feel like setup; they are not blocking, and time spent on them
in week one is time not spent finding out whether anyone will pay.

---

## Recording required reads

Whenever you read a referenced file, append it to `.claude/required-reads.md`:

```markdown
# Required reads for this business

## Core (always)
- 00-core/reasoning-guardrails.md
- 00-core/initiation.md
- 00-core/case-registry.md
- 00-core/viability-screen.md
- 00-core/human-action-queue.md
- 00-core/delivery-model-selector.md
- 00-core/operating-cadence.md
- case-studies/C3-data-cleaning-enrichment.md

## Systems in use
- 20-systems/outreach.md
- 20-systems/delivery-and-qa.md

## Resources acquired — read because we built this
- 10-resources/business-resources.md
- 10-resources/ref-payments-and-billing.md   (Gumroad, 2026-09-03)
- 10-resources/ref-email-domain.md           (sending domain, 2026-09-03)
- 10-resources/ref-website.md                (one-page offer, 2026-09-10)
- 10-resources/ref-design-system.md          (Carbon, restrained, 2026-09-10)

## Guardrails triggered by this business
- 50-guardrails/legal-and-compliance.md      (GDPR, vendor resale terms)
- 50-guardrails/security-and-secrets.md      (client data handling)

## NOT read — not needed
- ref-social-youtube.md, ref-social-linkedin.md, ref-docs-and-decks.md
```

**Keep the "NOT read" section.** It tells a future agent that the omission was a
decision, not an oversight — which stops it re-litigating a resolved question.

See `40-automation/agent-state-files.md` for generating the `.claude/`, `.cursor/`, and
`.antigravity/` manifests.

---

## Two worked examples

### Example A — the resource plan that stays small

**The situation.** C3 selected, viability screen passed, day 1.

> **Resource plan — deliberately short.**
>
> **Blocking today, both yours:**
>
> 1. **Sending domain** (~$12, 10 min). This is the critical path and I want it done
>    before anything else, including before I know our exact pricing. Warmup takes 2–3
>    weeks and nothing can be sent until it is done, so every day of delay is a day added
>    to first revenue. It warms in the background while I build.
> 2. **Confirm the payment rail.** You have PayPal from freelancing. I need to walk the
>    whole path with you once: a client agrees → you invoice → they pay how → it lands
>    where → you can spend it. Five minutes, and it is the test that catches the problem
>    that would otherwise surface in week four.
>
> **Week 1, mine:**
> - Business email on the new domain
> - The cleaning pipeline and 20 real samples
>
> **What I am deliberately NOT doing, and why:**
>
> - **No website yet.** `ref-website.md` Step 0: our first outreach attaches a file. The
>   buyer opens a spreadsheet, not a homepage. A site becomes worth building once someone
>   replies and checks us out — probably week 3.
> - **No logo, no brand, no colours.** Nothing in the first sale depends on it.
> - **No LinkedIn company page, no X account.** Wrong channel for RevOps cold outreach,
>   and a new account with no history is worth roughly nothing.
> - **No dashboard.** With zero prospects there is nothing to display. Building one now
>   is building a UI for an empty file.
> - **No entity.** Invoicing as an individual is legal in your jurisdiction and a $600
>   pilot does not justify formation costs. Revisit at ~$3k/month.
>
> **Total spend to start: $12.** Total setup on your side: about 15 minutes.
>
> Files I'm reading for this: `ref-payments-and-billing.md` and `ref-email-domain.md`.
> Recording both in `.claude/required-reads.md`, along with the list above of what we
> chose not to build — so if someone picks this up in a month they know those were
> decisions.

Why this works: it separates blocking from everything else, gives lead-time reasoning for
why the domain comes before the strategy, and — most valuably — **states what it is not
building and why.** That list is the real output. An operator seeing "$12 and 15 minutes"
understands the posture immediately.

### Example B — the operator who wants the setup first

**The situation.** Operator: *"Before we start selling, let's get the branding sorted, get
a proper website up, and set up the LinkedIn company page and Twitter. I want it to look
legitimate."*

> I understand the instinct and I want to redirect it rather than just disagree, because
> the underlying worry is real.
>
> **The worry is: will a stranger take us seriously?** That is a fair question. The
> answer for this business is that our credibility comes from the attached spreadsheet,
> not from the letterhead. When a RevOps manager opens a file and sees 11 duplicates in
> their own data that they did not know about, the branding is not what they are
> assessing.
>
> **The cost of doing it first is specific, not abstract:**
>
> Branding, a full site, and two social accounts is realistically two weeks. Our whole
> runway is eight. And it happens *before* we know anything — before we know whether
> RevOps managers reply, whether $600 is approvable, whether logistics data enriches well
> enough for the margin to work. If any of those is wrong, we rebuild the branding around
> a different offer anyway.
>
> There is also a channel point: a brand-new X and LinkedIn with no history and no
> followers does not read as legitimate. It reads as a company founded last Tuesday,
> which is worse than having no accounts at all. Those channels need months of activity
> to be assets, and neither is where RevOps buyers are.
>
> **What I'd do instead — same goal, two days instead of two weeks:**
>
> - A one-page site once we have our first reply. One clear promise, the price, your
>   name and photo, a real physical address. That reads as more legitimate to a B2B
>   buyer than a polished brand with no person behind it.
> - Business email on our own domain — that one genuinely matters and it is already in
>   flight.
> - A real result on the page as soon as we have one. "1,847 duplicates found in 5,000
>   records" is worth more than any amount of design.
>
> **My suggestion: revisit branding at first revenue.** By then we will know what we
> actually sell, who buys it, and what language they use — and the brand will be built
> around something true instead of a guess.
>
> If you'd still rather do it now, it's your business and I'll build it. I just want the
> two weeks to be a decision rather than a default.

Why this works: it names the operator's real concern instead of arguing with the surface
request, quantifies the cost against the actual runway, adds the non-obvious point that
empty social accounts *reduce* credibility, offers a two-day version that serves the same
goal, and hands the decision back explicitly. **The redirect is more useful than a
refusal because it solves the thing they were actually worried about.**

---

**Read next:** whichever referenced file this index routed you to · then record it in
`.claude/required-reads.md` · `00-core/human-action-queue.md` for the blocking items
