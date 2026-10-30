# Resource Reference — LinkedIn

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Read when LinkedIn is a channel — **and before any LinkedIn data use** |
| **Relevant to** | C2, C4, C6, C7, C10 · data-source implications for **C6** |
| **Prerequisite** | `50-guardrails/legal-and-compliance.md` §3, `10-resources/ref-auth-and-identity.md` |

---

## Read this first: the automation boundary · **HARD**

**LinkedIn's user agreement prohibits scraping and automated activity. Enforcement is
real** — account restriction or permanent ban, and LinkedIn has litigated against
scrapers.

**Never run scrapers, connection automation, or automated messaging on your operator's
LinkedIn account.**

The trade is one-sided and worth stating plainly: the downside is the **permanent loss of
their professional identity** — a decade of connections, their employment history, their
recommendations. The upside is saving a few dollars in API cost. That is never worth
taking, and no volume target changes it.

**What is compliant:**
- LinkedIn as a **research surface a human reads**
- **Draft-and-approve**: you write, the operator posts and connects at human pace
- Sourcing contact data from providers who carry **their own lawful basis and their own
  relationship with the source** (agentcash `stableenrich` routes LinkedIn data this way)
- Company Page admin roles for organizational posting

**What is not:**
- Any tool that logs into their account and acts
- Bulk connection requests or auto-DMs
- Scraping profiles or search results
- Anything sold as "LinkedIn automation," regardless of how it is marketed

**For C6 specifically:** this is your killer risk. Source contact data from providers,
not from your own scraper. See `case-studies/C6-icp-lead-research.md` §5.

---

## Step 0 — Is LinkedIn your channel?

**Use it when:** the buyer is a B2B professional and your operator has genuine standing —
a real profile, a real history, real connections in the field.

**Do not use it when:** the buyer is a developer (they are on X and GitHub), a local
business owner (they are on the phone), or a consumer.

| Case | Verdict |
|---|---|
| **C2** | **Strong** — case studies after each project generate inbound for a year |
| **C4** | **Strong** for professional niches. Daily insight clips |
| **C6** | **Strong for publishing**; **hard boundary on data** |
| **C7** | **Strong** — compliance content performs with this buyer |
| **C10** | **Primary** for B2B creators; the free repurpose is posted here |
| **C1** | Weak. Developers are elsewhere |
| **C3** | Marginal. Outbound works better; revisit once there is revenue |
| **C5, C8, C9** | **No.** Wrong buyer or wrong channel |

---

## Personal profile beats Company Page — by a lot

Company Pages get very little organic reach. **Publish from the operator's personal
profile.** Their name, their face, their history.

A Company Page is worth having as a credibility artifact — prospects check that it exists
— but do not expect it to distribute anything.

**Ask specifically:**

> "Will you publish two posts a week that I draft, from your personal profile? About ten
> minutes of your time, and it reaches people a new page never would."

---

## What works

**Write like a person who knows something, not like marketing.** The register on
LinkedIn rewards plain, direct, specific writing far more than most people assume.

- **Lead with a claim or an observation**, not a hook question. Never open with "Most
  people think…"
- **One idea per post.** Short paragraphs, generous line breaks
- **Specific numbers from real work.** "1,847 duplicates in 5,000 records" outperforms any
  adjective
- **Native content.** No links in the post body where reach matters — put them in the
  first comment
- **Documents (carousels)** perform well for frameworks and checklists
- **Reply to every comment.** Early comment velocity drives distribution
- **Post Tuesday–Thursday, mornings** in the audience's timezone

**What does not work:** engagement bait, "Agree?" endings, humblebrag origin stories,
reposting the same content weekly, and anything that reads as written by a content agency.

---

## Prohibited (G3)

- Fabricated case studies or client results
- Client logos or names without written permission
- Invented metrics or milestones
- Buying engagement or using pods
- Automated posting, commenting, or connecting
- Publishing an opinion in the operator's name they have not expressed

---

## Ten-case reference

| Case | Use | The one thing that works |
|---|---|---|
| **C2** | Post-project case study | "What was broken, what I built, 4 weeks, fixed price" — with the client's permission |
| **C4** | Daily insight clip | The sharpest single judgement from each issue, standalone |
| **C6** | Redacted research sample | Show the depth of one prospect row. It sells the whole service |
| **C7** | Compliance explainer | "What an enterprise buyer will ask for" — the gap list, free |
| **C10** | **The free public repurpose** | Tagged to the creator, crediting them generously |
| **C3** | Occasional | Data-quality findings from anonymized work |

---

## Two worked examples

### Example A — the C2 post-project case study

> Finished a four-week build for a 3PL company last month. Writing it up because the
> problem is common.
>
> **The problem:** they reconciled Shopify orders against their 3PL's exports by hand.
> One person, one day a week, in a spreadsheet. It broke whenever either export format
> changed.
>
> **What I built:** an internal tool that ingests both exports and produces four lists —
> matched, missing from the 3PL, missing from Shopify, and quantity mismatches. Four
> weeks, fixed price.
>
> **What surprised me:** 312 orders had been silently mismatched over eight months.
> Nobody knew, because nobody had ever reconciled a full year at once.
>
> **The general point:** if a person spends a day a week on a spreadsheet that breaks,
> that is usually a three-to-six week build. The reason it does not get built is that it
> is never the most important thing on the engineering roadmap — not that it is hard.
>
> Posted with the client's permission.

Specific, useful to a reader who has the same problem, and the last line is a G3
requirement rather than a courtesy.

### Example B — refusing the automation tool

**The situation.** Operator: *"My friend uses a tool that sends 50 connection requests a
day with a personalized note. Should we set that up?"*

> No — and this is one of the few things I'd push back on even if you told me to proceed,
> so let me give you the full reason.
>
> **It violates LinkedIn's user agreement**, and enforcement is not theoretical. The
> penalty is restriction or permanent loss of the account. Your LinkedIn is a decade of
> connections, your employment history, and your recommendations. It is not recoverable
> and there is no appeal worth relying on.
>
> **The asymmetry:** we would be risking your professional identity to save maybe $40 a
> month in research costs. Your friend has not been caught *yet* — that is the only
> information his experience contains.
>
> **What I'd do instead, which is compliant and works better:**
>
> - **You post twice a week**, I draft. Ten minutes of your time. Reaches your existing
>   network, which already trusts you
> - **You send 5–10 personal connection requests a week**, manually, to people I've
>   researched — with a real reason in each note. A 10% acceptance on 50 automated
>   requests is worse than 60% on 8 researched ones, and it does not put the account at
>   risk
> - **Contact data comes from providers** who have their own licence for it, not from
>   scraping. That is what `stableenrich` is for and it costs cents
>
> The compliant version is slower per action and considerably better per outcome. The
> automated version is faster right up until the day it is not.

---

**Read next:** `50-guardrails/legal-and-compliance.md` §3 · `20-systems/outreach.md` ·
`case-studies/C6-icp-lead-research.md` §5 · `20-systems/content-and-writing.md`
