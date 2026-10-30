# Resource Reference — Design System Selection

> **Status: REFERENCED FILE.** Read when building **any** user-facing website
> (`ref-website.md`) or **any** dashboard (`30-dashboards/dashboard-spec.md`). Once
> read, it becomes a required read for this business — record it in
> `.claude/required-reads.md`.
>
> Prerequisites: `00-core/reasoning-guardrails.md` (G3 governs every claim rendered on
> a page), `10-resources/ref-website.md` (the static constraint).

---

## Step 0 — Does the operator have a style?

**If the operator specifies a style, brand, existing site, or set of colours, use
theirs. Stop reading here and follow it.** Their brand consistency is worth more than
any library's polish, and overriding it to use something you find nicer is not your
call.

Ask once, specifically:

> "Do you have brand colours, a logo, an existing site, or a look you want this to
> match? If not, I'll pick something appropriate for your buyer and show you before I
> build it."

**If they have no preference, this file governs.** Do not invent a house style from
scratch, and do not default to whatever you generated last time.

---

## The reasoning that matters: match the buyer, not your taste

**This is the whole file. Everything below is application.**

A design system is not a matter of preference. It is a signal about what kind of
operation the visitor is dealing with, and the correct signal is **determined by what
the buyer is risking.**

```
        Buyer's perceived risk of this purchase
        ↑
  HIGH  │  Compliance docs (C7)      →  Restraint, density, precision
        │  Money data (C9)              Expressive design ACTIVELY
        │  $12k contracts (C2)          DESTROYS TRUST here
        │  Their customer data (C3, C6)
        │
        │  Retainers (C5)            →  Plain, legible, fast
        │  Job posts (C8)               Neutral. Do not distract
        │
        │  Newsletters (C4)          →  Typography-first, reading-optimized
        │
   LOW  │  Components (C1)           →  Expressive, animated, polished
        │  Creative services (C10)      The polish IS the product demo
        ↓
```

**The two failure modes, and both are common:**

1. **Expressive design on a high-trust purchase.** A compliance-document business with
   animated gradient orbs and scroll-triggered reveals reads as a marketing site, not a
   professional service. The buyer is about to hand you their audit readiness. Flair
   costs you the deal, and they will not tell you why.

2. **Sterile design on a taste purchase.** A component marketplace with a plain
   Bootstrap-looking site tells a developer your components are plain. Here the site is
   a **live demonstration of the product**, and restraint is a negative signal.

**The test question:** *does the visitor's decision depend on believing I am careful, or
on believing I have taste?* Careful → restrained. Taste → expressive. When it is both
(C2, C10), lead with careful and let one element carry the taste.

---

## The five sources, and what each is actually for

All five are legitimate; they are not interchangeable.

### 1. IBM Carbon Design System — the restrained default
`carbondesignsystem.com` · **Apache 2.0** · React, Web Components, and plain CSS/vanilla

Enterprise-grade, data-dense, grid-disciplined. IBM Plex typography. Precise spacing
tokens, exhaustively documented, and a genuine accessibility baseline rather than an
afterthought.

**Use for:** every dashboard, and every high-trust business site (C2, C3, C6, C7, C9).
**Strengths:** looks like software built by adults; data tables and forms are excellent;
the vanilla/web-components path needs no React, which suits this framework's constraints
perfectly.
**Weakness:** it looks like IBM. Distinctive it is not — which is exactly why it works
where credibility beats memorability.

### 2. Beautiful UI — data and agent-native components
`beautifului.dev` · **MIT** · 20+ components, built by Turbo

Two clusters, both directly relevant here:
- **Data:** records table, diff table, filter table, charts, flowcharts, insight cards
- **AI-native:** thinking traces, streaming text, **approval cards**, **tool chips**,
  context cards, chat composer, code blocks

**Use for:** dashboards, above all others. **This is the best-fitting source in the
framework for an agent-run business**, and the reason is specific: your dashboards need
to show *what the agent did, what it spent, and what is waiting for human approval*.
The approval card maps directly onto Sella's `approval_threshold_usdc` queue and onto
`HUMAN-ACTION-QUEUE.md`. The tool chip maps onto logged agent actions. The diff table
maps onto C3's before/after deliverable.

Reach for this before building an approval or activity UI by hand.

### 3. Aceternity UI — expressive marketing surfaces
`ui.aceternity.com` · **check per component** · React + Next.js + Tailwind + Framer
Motion

Animated, high-polish marketing components: spotlights, background beams, card hover
effects, bento grids, infinite moving cards, text reveals.

**Use for:** hero sections and landing pages where taste is the purchase (C1, C10).
**Use sparingly.** These are heavy — Framer Motion plus several animated components will
blow the 500KB page-weight budget in `ref-website.md` on its own.
**Licensing: Aceternity has free components and a paid Pro tier. Check the licence on
each component you take.** See §5 — this is not optional.

### 4. Rare UI — distinctive single-purpose components
`rareui.com` · **free, open source** · React, shadcn CLI, Tailwind · 17+ components

Unusual, memorable, single-file components: Folder, Fluid Orb, Gravity Letters, Duration
Picker, OTP Input.

**Use for:** exactly one memorable moment on an expressive site. Their value is
scarcity — a page using six Rare UI components is a novelty demo, not a business. Use
one, well placed, and let the rest of the page be quiet.

### 5. Neobrutalism — a style, not a library
Thick black borders, hard offset shadows (no blur), saturated flat colour, chunky type,
no gradients, visible structure.

**Use for:** C10 and creator-facing work, or any business deliberately signalling
"independent, opinionated, not an agency."
**Strengths:** implementable in pure CSS with **zero dependencies and near-zero page
weight** — the most framework-compatible expressive option by a wide margin. Fast,
accessible if contrast is handled, and genuinely distinctive.
**Weakness:** polarizing, and it reads as unserious to a conservative B2B buyer. Never
for C7 or C9.
*(If you use `neobrutalism.dev` components rather than writing the CSS yourself, check
their licence separately — the style is free, a specific implementation may not be.)*

---

## Combining them — the rule

**One restrained base + at most one expressive accent.** Never blend two expressive
sources; the page stops having a point of view and starts looking like a component
gallery.

| Composition | Verdict |
|---|---|
| Carbon base + Beautiful UI data components | **Best dashboard combination.** Use by default |
| Carbon base + one Rare UI accent | Good. Restrained with one memorable moment |
| Aceternity hero + plain CSS body | Good for C1/C10. Keeps the weight budget |
| Neobrutalism throughout | Good, and cheapest. Commit fully or not at all |
| Aceternity + Rare UI + neobrutalism | **No.** Three voices, no identity |
| Carbon + neobrutalism | **No.** Directly contradictory signals |

---

## The static constraint, resolved

`ref-website.md` requires **no server, no database, no authentication**. That constraint
is about *operational liability* — things that break unattended, cost money monthly, or
create a breach surface.

**It is not a prohibition on a build step.** Astro, Eleventy, or a Next.js static export
produce static files and satisfy it completely. So React component libraries are
available to you.

What still binds, and is not negotiable:

1. **Page weight under 500KB, load under 1.5s on 4G.** Framer Motion plus three animated
   components exceeds this alone. Measure before shipping.
2. **The page must work without JavaScript** for anything that matters — content,
   navigation, the CTA link. Animation may degrade; the offer may not disappear.
3. **No auth, no server, no database.** Unchanged.
4. **Accessibility floor:** 4.5:1 contrast, visible focus states, 44px tap targets,
   `prefers-reduced-motion` respected. **Neobrutalism and Aceternity both fail contrast
   and motion accessibility by default** — fix it rather than shipping it.

**The honest default for most cases in this framework: hand-written HTML and CSS, with
Carbon's tokens and type scale copied in.** No build step at all, and it satisfies
everything. Reach for a framework when the component genuinely earns it — which for C1
and C10 it does, and for C3, C7, and C9 it does not.

---

## §5 — The licence check · mandatory before shipping any component

**Check the licence of every component you copy, and record it.** This framework asks
you to hold your operator to G3 on truthfulness; shipping code you have not verified you
are allowed to ship is the same category of failure.

| Source | Licence |
|---|---|
| IBM Carbon | Apache 2.0 — permissive, attribution in NOTICE |
| Beautiful UI | MIT — permissive |
| Rare UI | Free, open source — confirm the repo licence file |
| Aceternity UI | **Mixed. Free components and a paid Pro tier — check per component** |
| Neobrutalism (as a style) | Not licensable. A specific implementation may be |

Rules:

- **Never ship a paid-tier component without your operator buying it.** This is the one
  real risk in the list and it is on Aceternity's boundary.
- Keep `ASSETS-AND-LICENCES.md` recording each component, its source, and its licence.
- **Copy components, never marketing copy or imagery.** Lifting a design system's
  landing-page text is both a copyright problem and a G3 problem, because their claims
  are not your claims.
- Fonts have their own licences. IBM Plex is Open Font Licence; check anything else.

---

## Dashboards specifically

Dashboards in this framework are **client-side only, read from flat JSON, and are read
by your operator most days.** Design accordingly:

**Default stack: Carbon tokens + Beautiful UI data components, no build step where
possible.** Vanilla CSS with Carbon's spacing/type scale and IBM Plex covers most of it.

**Non-negotiables:**
- **Data density over whitespace.** This is an instrument panel, not a landing page.
- **The number that matters is the largest thing on screen.** Revenue, replies, cash —
  not a chart, not a logo.
- **Never animate data.** Animated counters and transitions on numbers make an operator
  distrust the numbers, and they are right to.
- **No dark-pattern framing.** Do not colour a bad number green because it improved.
  Show the number and the direction; let them judge (G12).
- **Show the evidence rung** (G1) wherever the dashboard reports pipeline. "4 replies
  (rung 4), 1 call booked (rung 5)" — not "strong interest."
- **Surface pending approvals prominently.** Use Beautiful UI's approval card. Anything
  waiting on the human is the most actionable thing on the page.

---

## Ten-case reference

| Case | Buyer risk | Recommended | Why |
|---|---|---|---|
| **C1** React components | Low / taste | **Aceternity hero + one Rare UI accent** | The site is a live demo of your component quality. Restraint here reads as "plain components" |
| **C2** Fixed-bid agency | High | **Carbon-leaning, restrained** | $12k buyer wants evidence of competence. One tasteful element, no more |
| **C3** Data cleaning | High | **Carbon, plain HTML/CSS** | They are handing you their customer database. Look like software, not marketing |
| **C4** News brief | Medium | **Typography-first — none of the five as primary** | Reading experience is the product. Borrow Carbon's type scale; skip the component libraries entirely |
| **C5** Local SEO | Medium | **Plain, legible, mobile-first** | A dentist on a phone. Neobrutalism confuses this buyer; Carbon-lite or plain CSS |
| **C6** Lead research | High | **Carbon + Beautiful UI tables** | Show the sample in a records table — the data display *is* the pitch |
| **C7** Compliance docs | **Highest** | **Carbon, maximum restraint** | Expressive design actively destroys this sale. No animation at all |
| **C8** Job board | Medium | **Carbon for the board, light accent on the subscribe page** | Listings are dense data; the newsletter landing may carry one expressive element |
| **C9** Reconciliation | **Highest** | **Carbon, maximum restraint** | Money business. Every visual decision should say "careful" |
| **C10** Repurposing studio | Low / taste | **Neobrutalism, or Aceternity** | Taste is the product being sold. Neobrutalism preferred — near-zero weight, genuinely distinctive |
| **All dashboards** | n/a — internal | **Carbon tokens + Beautiful UI data + approval cards** | Density, honesty, and the approval queue front and centre |

Note **C4 is deliberately "none of the above."** A reading publication wants a long-form
typography stack, generous measure, and almost no components. Forcing a component
library onto it makes it worse. Say so to the operator rather than using one because it
was on the list.

---

## Two worked examples

### Example A — C1, where expressive is correct

**The reasoning, written into `DECISION-LOG.md`:**

> **Design system for the component marketplace site.**
>
> Buyer is a developer deciding whether $49 of components is worth it. They will judge
> component quality by looking at my site, because my site is built from the same kind
> of thing I am selling. This is the one case in the registry where the page is a live
> product demo, so polish is not decoration — it is evidence.
>
> **Chosen:** Aceternity for the hero (spotlight + bento grid for the pack listing),
> **one** Rare UI component as the memorable moment, plain Tailwind everywhere else.
>
> **Rejected:** Carbon. It would signal "enterprise tooling," which is not what a solo
> developer buying a $49 pack is looking for, and it would make my components look
> plain by association.
>
> **Weight budget:** Framer Motion is ~90KB gzipped. Two animated components plus the
> hero puts me around 340KB, inside the 500KB budget with room. Verified with a build,
> not estimated.
>
> **Licence check:** hero spotlight and bento grid are Aceternity free-tier — confirmed
> on the component page, recorded in `ASSETS-AND-LICENCES.md`. **Did not use the Pro
> templates.** Rare UI is open source, repo licence confirmed.
>
> **Accessibility:** `prefers-reduced-motion` disables all animation. Hero text contrast
> raised to 5.1:1 from Aceternity's default, which failed at 3.2:1.

Note the last two paragraphs. **Verifying the licence tier and fixing the default
contrast are the two things that get skipped**, and they are exactly the ones that
matter — one is a legal exposure for your operator, the other excludes real users.

### Example B — C7, where expressive loses the deal

**The situation.** The operator sees a competitor's compliance site with animated
gradients and says: *"Ours looks boring next to theirs. Can you make it look more
modern?"*

**The response:**

> I can, and I want to push back once before I do — then it's your call.
>
> Your buyer is a founder about to hand you their audit readiness before an enterprise
> deal worth six figures to them. What they are buying is the belief that you are
> careful and precise. Every animated gradient spends a little of that.
>
> There is a real asymmetry here: a boring compliance site costs you nothing, because
> nobody has ever declined to buy a policy pack because the site was too plain. A
> flashy one costs you the buyers who conclude you are a marketing operation rather
> than a practice — and they will not tell you that, they will just not reply.
>
> The competitor may be getting deals despite that site, not because of it.
>
> **What I'd do instead — this is what "modern" actually means to this buyer:**
>
> - Tighten the type scale and spacing. Carbon's grid discipline reads as precise, and
>   precision is the message
> - IBM Plex Sans instead of the system font — it looks considered without looking
>   designed
> - Put the **control coverage map** on the homepage. A real traceability table is the
>   single most persuasive thing we own, and no competitor with a gradient hero is
>   showing one
> - One accent colour, used only on the CTA
> - Faster. Their site takes 2.8s to load; ours can be under 1s, and enterprise buyers
>   check on bad hotel wifi
>
> That reads as more expensive than animation does, to this specific buyer.
>
> If you still want the gradients after that, say so and I'll build it — it's your
> business and your name on it. But I'd want to test it against the plain version
> rather than switch on the assumption.

Why this is the right shape: it states the disagreement once with a concrete reason,
gives the **asymmetry argument** (the downside is one-sided), reframes "modern" into
things that genuinely signal quality to *this* buyer, offers a specific alternative
rather than just refusing, and explicitly hands the decision back. **A design opinion
delivered without a testable alternative is just taste, and taste is not an argument.**

---

**Read next:** `10-resources/ref-website.md` · `30-dashboards/dashboard-spec.md` ·
`50-guardrails/brand-voice-and-truth.md` (nothing rendered on a page may be a claim you
have not verified — G3)
