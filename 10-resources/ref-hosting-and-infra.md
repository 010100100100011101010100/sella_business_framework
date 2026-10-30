# Resource Reference — Hosting & Infrastructure

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Read when you have a website or dashboard to deploy |
| **Prerequisite** | `10-resources/ref-website.md`, `10-resources/ref-design-system.md` |

---

## The rule: you operate nothing

**No server, no database, no authentication, no background process you are responsible
for keeping alive.**

This is not minimalism for its own sake. A server is a thing that breaks at 3am, costs
money monthly whether or not it earns any, accrues security patches, and creates a breach
surface holding data you did not need to store. **A small business that has to operate
infrastructure has taken on a second job it is not paid for.**

Everything in this framework is achievable with static files plus somebody else's managed
service.

**The constraint is about operating, not about build steps.** Astro, Eleventy, and a
Next.js static export all emit static files and satisfy it completely — see
`ref-design-system.md` §"The static constraint, resolved."

---

## The stack

| Layer | Use | Cost |
|---|---|---|
| **Static host** | Cloudflare Pages, Netlify, or GitHub Pages | **Free** at this scale |
| **DNS** | Cloudflare, or the registrar's | Free |
| **Domain** | Namecheap, Cloudflare Registrar | ~$12/yr · **operator buys it (G9)** |
| **Forms** | The payment provider's hosted checkout, or a form service free tier | Free |
| **Analytics** | Plausible, Fathom, or Cloudflare Web Analytics | Free–$9/mo |
| **Email (transactional)** | The ESP or agentcash `stableemail` | Usage-based |
| **File delivery** | The merchant of record, or signed expiring URLs | Included |
| **Asset hosting** | agentcash `stableupload` for permanent URLs | Per-use |

**Recommended default: Cloudflare Pages.** Free, global, automatic HTTPS, deploys from a
git push, and DNS lives in the same place. There is no meaningful reason to pay for
hosting at this stage.

---

## What you must not build

| Do not build | Use instead | Why |
|---|---|---|
| A login system | Nothing — gate via the payment provider | Credentials you store are credentials you can lose |
| A payment form | Hosted checkout redirect | PCI scope you cannot satisfy |
| A database | Flat JSON/CSV in the repo | Nothing at this scale needs one |
| A file upload endpoint | `stableupload`, or the client sends files | An unauthenticated upload is an attack surface |
| An admin panel | Edit the files | You are the only admin |
| A cron server | The platform's scheduler (`40-automation/periodic-jobs.md`) | Another thing to keep alive |
| A custom analytics pipeline | Plausible / Fathom | Solved, cheaply |

**Gating paid content without auth:** the merchant of record delivers the file (Gumroad,
Lemon Squeezy do this natively), or you issue a signed URL that expires. Both are
standard, neither stores a password.

---

## Performance and reliability baseline

Non-negotiable, and all are easy on a static site:

- **Under 1.5s load on 4G. Under 500KB total page weight.** Measure, do not assume —
  Framer Motion plus three animated components exceeds this on its own
- **Works without JavaScript** for content, navigation, and the CTA
- **HTTPS everywhere**, automatic on every recommended host
- **Custom 404** pointing back to the offer
- **Uptime monitoring** on the one page that matters — a free checker is sufficient

**Backups:** the site lives in git. That is the backup. **Client data is different** —
see `50-guardrails/security-and-secrets.md` §3, and note that the correct posture there
is deletion at 30 days, not backup.

---

## Cost discipline

**Most cases in this framework should run under $50/month for the first ninety days.**

| Case | Realistic month-one infrastructure cost |
|---|---|
| C1 | ~$1 (domain amortized; MoR takes a % of sales, not a fee) |
| C2 | ~$1 |
| C3 | ~$1 + enrichment COGS |
| C4 | $0–49 (ESP free tier under 1,000 subscribers) |
| C5 | ~$35 (rank tracking) |
| C6 | ~$1 + enrichment COGS |
| C7 | ~$1 |
| C8 | $0–49 (ESP free tier) |
| C9 | ~$1 |
| C10 | ~$1 + media generation COGS |

**Every recurring subscription goes on the human action queue with its monthly cost and
what it replaces**, and gets reviewed at the monthly close (G6). Subscriptions are where
small businesses bleed — not through one bad decision, but through six reasonable ones
nobody revisits.

**Free tiers first, always.** Cloudflare Pages, the ESP under 1,000 subscribers,
Carbon's Apache-2.0 components. Prefer usage-based over subscription at low volume: a
$0.004/verification API beats a $99/month seat until you are doing 25,000 verifications.

---

## Ten-case reference

| Case | Hosting need | Notes |
|---|---|---|
| **C1** | Static site + docs + live demos | Demos matter more than copy. MoR handles file delivery |
| **C2** | Static credibility site | Client project infra is **the client's**, provisioned in their accounts |
| **C3** | One static page | Deliverables go via email or a signed link, never a portal |
| **C4** | **ESP-hosted initially**, own archive later | The archive becomes the SEO asset — plan the URL structure early |
| **C5** | Static site | Client GBP is theirs; you hold delegated access, never their password |
| **C6** | One static page + sample | Same as C3 |
| **C7** | Static credibility site | Documents delivered directly. **Do not build a client portal** |
| **C8** | Static board + ESP | Board is generated from data files at build time |
| **C9** | Minimal static site | **No client data anywhere near the website** |
| **C10** | Static portfolio | `stableupload` for delivered media assets |

**Note the recurring pattern in C2, C5, and C7: the client's infrastructure stays in the
client's accounts.** You get scoped, revocable access. You never host their production
anything — that converts a service engagement into an operational dependency you are not
priced for and cannot exit cleanly.

---

## Two worked examples

### Example A — declining to build the portal

**The situation.** C7, second client. *"Can we have a portal to log in and see all our
compliance documents?"*

> I'd rather not build that, and I think you'll prefer the alternative.
>
> A portal means user accounts, passwords, session handling, and your compliance
> documents sitting on a server I operate. Those documents describe your security
> posture — they are among the more sensitive things you own. Putting them behind a
> login I built and maintain adds risk to *you* without adding much convenience.
>
> There is also a compliance irony: a security questionnaire will ask you about your
> vendors' controls. "Our compliance documents are stored in a bespoke portal built by a
> one-person consultancy" is a worse answer than "we hold them ourselves."
>
> **What I'd do instead:**
>
> - **The pack is delivered as files you own** — your Drive, your SharePoint, wherever
>   your policies already live. That is where an auditor will expect to find them.
> - **A version index** as the pack's first page: every document, its version, its date,
>   and what changed. That is the actual thing a portal would give you.
> - **Under the maintenance retainer**, I send updated documents when something changes,
>   with a changelog.
>
> You get the visibility without either of us taking on custody of your security
> documentation. If you'd still like something browsable, I can generate a static index
> page you host yourself — no login, no server, and it lives inside your own perimeter.

### Example B — the free tier that runs out mid-growth

**The situation.** C4, month 5. 980 subscribers, ESP free tier caps at 1,000.

> Heads up on a cost that arrives in about two weeks, so it is not a surprise.
>
> We are at 980 subscribers and the ESP's free tier stops at 1,000. At current growth
> (~70/week) we cross it around the 18th.
>
> **The cost:** $49/month at our tier. **Against:** $2,400/month in current sponsor
> revenue. It is 2% of revenue for the thing that delivers the product, so this is not a
> decision, it is a bill — I am flagging it so it does not look like a surprise charge.
>
> **What I checked before accepting it:**
>
> - **Alternatives.** Two cheaper options exist, but both would mean migrating the list.
>   List migration costs deliverability — the new sending infrastructure has no
>   reputation with our subscribers' providers and open rates typically dip for a few
>   weeks. Open rate is our entire sponsor pitch. Not worth $20/month.
> - **The annual plan** saves about 15%. Worth taking now that revenue is predictable.
> - **The next threshold** is 5,000 subscribers at $99/month. At current growth that is
>   roughly month 12, and revenue at 5,000 subscribers should be several times that.
>
> **Recommendation:** take the annual plan. Adding it to the recurring-cost review so we
> revisit it at each monthly close rather than letting it become invisible.

Why this is right: it surfaces the cost before it lands, sizes it against revenue rather
than in isolation, shows the alternatives were genuinely considered, and gives the
non-obvious reason not to optimize — migration costs deliverability, and deliverability
is the product. It also puts the cost into a review cycle instead of letting it become
one of the six reasonable subscriptions nobody revisits.

---

**Read next:** `10-resources/ref-website.md` · `10-resources/ref-design-system.md` ·
`40-automation/periodic-jobs.md` · `50-guardrails/security-and-secrets.md`
