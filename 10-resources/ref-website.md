# Resource Reference — Website

> **Status: REFERENCED FILE.** Read this only when `business-resources.md` routes you
> here — i.e. when you have decided the business needs a website. **Once you read it,
> it becomes a required read for this business**: record that in
> `.claude/required-reads.md` so any agent picking this up later knows.
>
> Prerequisite: `00-core/reasoning-guardrails.md` (G3 governs every claim on the page).

---

## Step 0 — Decide whether you need one at all

**Most businesses in this framework do not need a website in week one, and building one
early is the most common way G2 gets violated.** A website is a building activity that
feels like distribution. It is not. Nobody visits a website that nothing links to.

Run the decision table before writing a line of HTML:

| Situation | Verdict |
|---|---|
| Cold outbound, no traffic source yet | **No site.** A one-page proof doc is enough |
| Prospects will Google you before replying (C2, C7, C9) | **Yes — a credibility site.** Minimal, one page |
| Selling a digital product to strangers (C1) | **Yes — a storefront.** But a Gumroad/Lemon Squeezy page may be sufficient at first |
| Building an audience (C4, C8) | **Yes — but the *email platform's* hosted page is fine to start** |
| Local business services (C5) | **Yes.** Local buyers check that you exist |
| Referral-driven, warm only (C9 early) | **No.** Referral does the trust work |
| Delivering via free public work (C10) | **Not initially.** The published work *is* the portfolio |

**The honest sequence for most cases:** no site → a Sella `storefront_set` or a hosted
product page → a single static landing page → a real site. Move to the next stage only
when the current one is the actual constraint.

**The Sella zero-build option is genuinely useful in week one.** `storefront_set`
publishes a page your operator and prospects can read — heading, text, metrics, tables,
offerings, links — before a domain exists. Because an `offering` block carries only a
`service_id` and reads price and copy from the listing, you cannot advertise one number
and charge another. Use it as the interim site while you find out whether anyone wants
the thing.

---

## Step 0.5 — Pick the design system

**Before writing markup, read `10-resources/ref-design-system.md`.**

If the operator has brand colours, a logo, an existing site, or a stated look — use
theirs and skip the rest. Ask once, specifically.

If they have no preference, the choice is **determined by what the buyer is risking**,
not by taste. High-trust purchases (compliance, money, their customer data) want
restraint and density; taste purchases (components, creative services) want polish,
because there the page is a live demonstration of the product.

The default sources, when nothing is specified: **IBM Carbon** (restrained base,
Apache 2.0), **Beautiful UI** (data and approval components, MIT), **Aceternity**
(expressive hero, check licence per component), **Rare UI** (one distinctive accent,
open source), **neobrutalism** (expressive at near-zero page weight).

**The rule: one restrained base plus at most one expressive accent.** Never two
expressive sources. Full reasoning, the per-case table, and the mandatory licence check
are in `ref-design-system.md`.

---

## Hard constraints — these are not preferences

**1. Static only. No server, no database, no backend you operate.**
Same rule as the dashboards. A server is an operational liability, a security surface,
and a monthly cost, and it can break while nobody is watching. Everything in this
framework is achievable with static files.

**2. No authentication. No user accounts. Ever.**
The moment you store credentials you have taken on a breach liability that no business
at this stage should carry. If something needs to be gated, use the payment provider's
own delivery (Gumroad delivers files; Stripe sends a link) or a signed URL that expires.

**3. Payments go through a hosted checkout redirect.**
Stripe Checkout, Lemon Squeezy, Gumroad, Paddle. **Never build a payment form.** Card
data must not touch a page you wrote; that is PCI scope you cannot satisfy and do not
want. The button links out, the provider handles everything, the customer comes back.

**4. No cookies you do not need — then you need no cookie banner.**
Use privacy-friendly analytics that do not set cookies (Plausible, Fathom, Cloudflare
Web Analytics, or a simple server-log approach). This removes the consent banner
entirely, which improves conversion and removes a compliance surface. **This is a
genuine advantage of building small; take it.**

**5. Every claim on the page must be true and verifiable (G3).**
No invented testimonials, no "trusted by" logos without written permission, no customer
counts you have not reached, no fake scarcity timers, no stock photos of a team that
does not exist. If the business is one person and an agent, the page may say "I" — and
it converts better than a fake "we."

---

## The five archetypes

Pick one. Do not blend them; a page trying to be two things converts as neither.

### A — The one-page offer
**For:** C3, C6, C10 early. **Purpose:** a place the cold email links to.
One scroll. What it is, who it is for, what it costs, one button. No navigation.

### B — The credibility site
**For:** C2, C7, C9. **Purpose:** survive the Google check before a reply.
Home, work/proof, about (with a real name and face), contact. Its job is to make a
prospect think "this is a real person who does this," not to convert cold traffic.

### C — The storefront
**For:** C1, C8. **Purpose:** sell a catalogued thing.
Product list, product detail, docs, checkout redirect. Live demos matter more than copy
for a developer audience.

### D — The content engine
**For:** C4, C8. **Purpose:** SEO and the archive.
Article/issue pages, a good archive index, subscribe form on every page. Every issue is
a permanent page and the compounding asset (G11).

### E — The proof portfolio
**For:** C10, C2. **Purpose:** show the work.
Case pages with before/after. For C10, the free public repurposes go here.

---

## Structure and copy

### Above the fold — the four-line formula

Every landing page, every archetype:

1. **What it is, in the buyer's words.** Not your category — their problem.
2. **Who it is for**, specifically enough that the wrong person self-excludes.
3. **The proof** — one concrete, real, verifiable thing.
4. **One button.**

Worked, for C3:

> # Your CRM has more duplicates than you think
> Deduplication, validation, and enrichment for B2B sales teams with 5,000–100,000
> records. Send an export, get it back correct in four days.
>
> Last job: 1,847 duplicates merged and 2,203 dead addresses flagged in a 5,000-record
> database.
>
> **[Get 100 rows cleaned free →]**

Note that the proof line is a **real, measured** result from a real job, and the CTA is
the free sample — the same mechanic as the outreach. The page and the email make the
same offer, which is why the page converts: the visitor arrives already primed.

**Before you have a real result, say so:** "New — taking the first three clients at a
founding rate" outperforms a fabricated number, and it is the only honest option (G3).

### Specificity over adjectives

| Weak | Strong |
|---|---|
| "High-quality data cleaning" | "1,847 duplicates found in 5,000 records" |
| "Fast turnaround" | "Four days, or you don't pay" |
| "Trusted by businesses" | "Currently working with three B2B SaaS teams" |
| "Affordable pricing" | "$600 for 5,000 records" |

**Put the price on the page.** Hiding it to force a conversation filters out fast movers
— exactly the buyers you want early — and reads as evasive.

### One CTA

Every page has one primary action. Repeat it; do not diversify it. A page offering
"book a call OR download the guide OR join the newsletter" converts worse than any one
of them alone.

---

## Stack

**Recommended:** hand-written HTML + CSS for one to five pages, borrowing Carbon's
spacing and type tokens. Astro or Eleventy from about ten pages, or when there is a
content archive. **Do not reach for a React SPA for a marketing site** — it is slower,
worse for SEO, and solves a problem you do not have.

**The no-server constraint is not a ban on build steps.** Astro, Eleventy, and a Next.js
static export all emit static files and satisfy it fully, so React component libraries
are available when a component genuinely earns it (C1, C10). What still binds: the 500KB
weight budget, working without JavaScript, and the accessibility floor. See
`ref-design-system.md` §"The static constraint, resolved".

**Hosting:** Cloudflare Pages, Netlify, or GitHub Pages. All free at this scale, all
serve static files globally, none require you to operate anything.

**Domain:** the human buys it (it needs a card — G9). About $12/year. **Put it on the
action queue early**, especially if outbound is involved, because the sending domain
warmup has a three-week lead time.

**Baseline requirements**, all easy and all worth doing:
- Loads in under 1.5s on 4G; total page weight under 500KB
- Real HTML semantics; works without JavaScript
- Responsive from 320px; tap targets 44px minimum
- Contrast ratio 4.5:1 minimum; visible focus states; alt text on meaningful images
- One `<h1>`, honest `<title>` and meta description, Open Graph tags for link previews

---

## Ten-case reference

*(Design system per case is a separate table in `ref-design-system.md` — it keys off
buyer risk, not archetype.)*

| Case | Archetype | Pages | H1 | Primary CTA |
|---|---|---|---|---|
| **C1** | C — Storefront | Home, packs, docs, free component | "Components you'd have spent two days building" | Get the free one |
| **C2** | B — Credibility | Home, work, about, contact | "Fixed-price internal tools in 3–6 weeks" | Book a scoping call |
| **C3** | A — One-page offer | One page | "Your CRM has more duplicates than you think" | Get 100 rows cleaned free |
| **C4** | D — Content engine | Home, archive, issue pages, about | "The 5 things in [niche] you can't miss, daily" | Subscribe free |
| **C5** | B — Credibility + local | Home, service, results, contact | "Get found when someone searches '[trade] [city]'" | Get your free audit |
| **C6** | A — One-page offer | One page + sample | "200 prospects a month, with a reason to call each one" | See ten free |
| **C7** | B — Credibility | Home, packs, about, contact | "The document set your enterprise buyer will ask for" | Free gap assessment |
| **C8** | D — Content engine | Board, issues, salary data, post-a-job | "[Role] jobs and the weekly brief" | Subscribe free |
| **C9** | B — Credibility, minimal | Home, how it works, about | "Know exactly who owes you what" | Free first month |
| **C10** | E — Proof portfolio | Home, work, pricing | "One episode. Twelve posts. Every week." | See what we did with [name]'s episode |

**Note C10's CTA.** It points at a real published artifact rather than a form, which is
the same free-work mechanic that makes its distribution the easiest in the framework.
The site is a portfolio of things already done, not a promise of things to come.

---

## Two worked examples

### Example A — the C3 one-page offer, in full

The entire page. One scroll, one CTA, nothing else.

> **[H1]** Your CRM has more duplicates than you think
>
> **[Sub]** Deduplication, validation, and enrichment for B2B sales teams with
> 5,000–100,000 records. Send an export, get it back correct in four days.
>
> **[CTA]** Get 100 rows cleaned, free →
>
> ---
>
> **What you get back**
> - Duplicates merged, with the match rule documented so you can audit it
> - Dead email addresses flagged and verified
> - Industry, headcount, and location populated where they were missing
> - Companies that have been acquired or renamed, identified
> - A one-page summary of what was wrong and what changed
>
> ---
>
> **What it costs**
> Free sample — 100 records, no commitment.
> Pilot — $600 for up to 5,000 records, four days.
> Full — $0.12 per record above that.
> Ongoing hygiene — from $1,400/month.
>
> ---
>
> **How it works**
> 1. Send a CSV export. No system access, no credentials, no integration.
> 2. Four days.
> 3. You get a cleaned file and a summary of what changed.
>
> Your raw data is deleted 30 days after delivery.
>
> ---
>
> **Who I am**
> I'm [name]. I clean B2B databases. That's the whole business.
> [photo] · [email] · [physical address, for CAN-SPAM compliance]
>
> **[CTA]** Get 100 rows cleaned, free →

Every section is doing work. **"No system access, no credentials, no integration" is the
line that closes** — it removes the buyer's largest objection before they voice it, and
it is a direct application of the credential boundary from C9. The 30-day deletion
promise is volunteered rather than buried, because it converts. The single "I" instead
of "we" is honest (G3) and reads as more accountable, not less.

Note also: **no testimonials.** There are none yet, and inventing them is prohibited.
The page works without them because the free sample removes the need for social proof
entirely — the visitor can just try it.

### Example B — the same page, done badly

> **[H1]** Enterprise-Grade Data Quality Solutions
>
> **[Sub]** We leverage cutting-edge AI to transform your data into actionable insights,
> empowering your revenue team to unlock their full potential.
>
> **[Trusted by]** [six logos of companies that are not customers]
>
> **[Testimonial]** "Working with them transformed our data operations. A game-changer
> for our team." — Sarah M., VP Sales
>
> **[Stats]** 500+ Happy Clients · 99.9% Accuracy · 10M+ Records Processed
>
> **[CTA]** Book a Demo · Download our Whitepaper · Start Free Trial

What is wrong, worst first:

1. **The logos are not customers. That is fraud**, and if any of those companies notices,
   your operator has a legal problem, not a marketing one.
2. **The testimonial is invented**, and "Sarah M., VP Sales" is the shape a fabricated
   attribution takes.
3. **"500+ clients, 10M+ records, 99.9% accuracy"** — none measured. G3, three times.
4. **The H1 says nothing.** "Enterprise-grade" and "solutions" are category words, not
   problems.
5. **Three CTAs**, so there is effectively none.
6. **"We"** implies a team.
7. **No price**, so serious buyers bounce.

The failure is not aesthetic. Items 1–3 are the kind that end businesses, and they are
the default output of an agent asked to "write a landing page" without guardrails. **The
honest version above converts better anyway**, which is worth saying plainly: G3 is not
a tax on effectiveness here, it is the reason the good page works.

---

**Read next:** `10-resources/ref-design-system.md` — **required before writing markup** ·
`10-resources/business-resources.md` (the routing index) ·
`10-resources/ref-payments-and-billing.md` before adding any checkout ·
`10-resources/ref-hosting-and-infra.md` · `30-dashboards/dashboard-spec.md`, which
shares this file's static-only constraint.
