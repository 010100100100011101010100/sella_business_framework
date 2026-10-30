# Resource Reference — Documents & Decks

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Read when deliverables are documents, or you pitch with a deck |
| **Relevant to** | C7, C9 (deliverables) · C2, C4, C6 (proposals and media kits) |
| **Prerequisite** | `50-guardrails/brand-voice-and-truth.md`, `10-resources/ref-design-system.md` |

---

## Step 0 — Does this need to be a document at all?

Most things that get made into decks should have been an email.

| Situation | Use |
|---|---|
| Explaining an offer to one person | **An email.** Faster to read, faster to reply to |
| A deliverable the client keeps and refers back to | A document |
| Something an auditor or third party will read | **A document, with traceability** (C7) |
| A pitch you present live | A deck — sparse, you are the content |
| A pitch you send unattended | **A document, not a deck.** Sent decks are read as documents and fail as both |
| Recurring numbers for a client | A one-page report, same format every time |

**The most common waste in this file is building a 20-slide deck for something that
converts better as a six-paragraph email.** Before making a deck, ask whether anyone
asked for one.

---

## Documents as deliverables (C7, C9)

**The document is the product. Its structure carries the value.**

**Non-negotiables:**

1. **Lead with what the reader needs.** C9's report opens with "you are owed $14,240,"
   not with methodology. C7's pack opens with the coverage map, not the introduction.
2. **State what you could not determine.** Flag ambiguity rather than guessing — C9's
   "two things I could not resolve" is the most trust-building section in the whole
   engagement.
3. **Declare known gaps deliberately.** C7's "known gaps, stated deliberately" is what
   makes the rest credible. A document claiming completeness it lacks is worse than none.
4. **Carry the disclaimer in the deliverable**, not only the contract. Clients keep
   documents for years and forget contracts in weeks.
5. **Version and date everything.** Version, date, and what changed since last time.
6. **Consistency across documents.** The most common real defect in a multi-document pack
   is internal contradiction — retention says 7 years in one place and 3 in another. Build
   the cross-check as an explicit gate (`delivery-model-selector.md` §D).

**Format:** deliver PDF for anything final and referenceable; editable formats only when
the client will maintain it. Plain, dense, and precise beats designed —
`ref-design-system.md`'s buyer-risk axis applies: these are the highest-trust documents in
the framework and restraint *is* the signal.

---

## Proposals (C2, C7)

**A proposal is a decision document, not a brochure.** One to three pages.

```
1. The problem, in their words        — proves you listened
2. What you will deliver              — specific, with the out-of-scope list
3. How you will verify it is done     — acceptance criteria (C2's margin protection)
4. Timeline and milestones
5. Price and payment terms            — stated plainly, no ranges, no "starting from"
6. What you need from them
7. What happens if scope changes      — the change-order mechanism, named
```

**Section 3 is the one people omit and it is the one that protects you.** Section 7 turns
a future argument into a priced conversation.

**Never send a proposal without a price.** "Let's discuss investment" reads as evasive and
loses the buyers who move fast — the ones you want.

---

## Decks

**Only for live presentation.** If it will be read unattended, write a document.

- **One idea per slide.** If it needs paragraphs, it is a document
- **The slide supports you; it is not the script**
- **Numbers must be measured and labelled** with their window (G3). A media kit slide
  saying "1,240 subscribers, 58% open rate, last 30 days" is a claim; without the window
  it is a boast that invites a wrong reading
- **10–15 slides maximum**
- **No stock photos of people who do not work for you**

**The media kit (C4, C8)** is the main legitimate deck in this framework: audience size
and composition, measured engagement with the window, past issues, the offering, the
price. **Sella `storefront_set` does this natively** — heading, text, metric, table, and
`offering` blocks, where the offering reads price from the listing so you cannot advertise
one number and charge another.

---

## Prohibited (G3)

- Client logos or names without written permission
- Fabricated case studies, testimonials, or results
- Unlabelled modelled numbers presented as results
- **Framework anchors quoted as your own performance**
- Claiming completeness a document does not have
- Compliance or legal assertions beyond "drafts for your counsel to review" (C7)

---

## Ten-case reference

| Case | Main artifact | The thing that makes it work |
|---|---|---|
| **C1** | Docs site | Live demos beat prose. Not a document at all |
| **C2** | **Proposal + acceptance criteria** | The out-of-scope list. Write it longer than feels necessary |
| **C3** | One-page change summary with the file | Measured before/after; the control total balancing |
| **C4** | **Media kit** | Measured numbers with windows; audience composition over raw size |
| **C5** | Monthly client report | Leading indicators first, honest lagging ones, one ask of the client |
| **C6** | Per-row delivery format | Dated sourced trigger + suggested first line + confidence field |
| **C7** | **Compliance pack + coverage map** | Traceability table and the deliberate gap declaration |
| **C8** | Media kit + salary report | Methodology and sample size stated — omitting n is soft fabrication |
| **C9** | **Monthly reconciliation** | Control check, unresolved items flagged not guessed, volunteered corrections |
| **C10** | Voice guide + monthly performance report | The "never says" list does more work than the positive rules |

---

## Two worked examples

### Example A — the proposal that protects the margin

Two pages. Abbreviated to the structural parts.

> **Order reconciliation tool — Meridian Logistics**
> Prepared 2026-09-03 · valid 30 days
>
> **The problem.** Your team reconciles Shopify orders against Fulfil's exports manually,
> roughly one day per week, and it breaks when either export format changes. In our
> scoping call you estimated 312 orders may have been mismatched over the last eight
> months without anyone noticing.
>
> **What I'll deliver.** A tool that ingests both exports and produces four lists:
> matched, missing from Fulfil, missing from Shopify, and quantity mismatches on matched
> orders. Runs on demand; a date range is selected by the user.
>
> **Explicitly out of scope:** automatic correction of mismatches · writing back to
> Shopify · historical reconciliation before 2026-01-01 · any 3PL other than Fulfil ·
> scheduled/automatic runs · user accounts or permissions.
>
> **How we'll know it's done.** Seven acceptance criteria, attached, each with its
> verification method. AC-04, for example: running both exports for August produces four
> categories totalling the Shopify order count. You sign these before I start.
>
> **Timeline.** Four weeks from signature. Weekly demo each Thursday.
>
> **Price.** $11,000. 50% on signature, 50% on acceptance.
>
> **What I need from you.** Sample exports from both systems (week 1), one 30-minute
> call weekly, and a named person to sign off acceptance.
>
> **If scope changes.** Anything outside the signed criteria is a change order — I'll
> price it and tell you the schedule impact before doing it. I won't decline additions,
> and I won't absorb them silently either.

The out-of-scope list is the most valuable text on the page. Every line is a conversation
that becomes a priced change order instead of an argument in week five.

### Example B — the deck that should have been an email

**The situation.** C4, month four. Operator: *"Let's put together a proper sponsor deck —
maybe 15 slides, with our story, the audience, some design."*

> I'd send a short email instead, and here's why I think it converts better.
>
> **A sponsor deck arrives unattended.** Nobody presents it. So it gets read as a
> document — and as a document, 15 slides is worse than six paragraphs: slower to skim,
> harder to reply to, and it lands as an attachment people open later and forget.
>
> **What a sponsor actually needs to decide:** who reads it, how many, how engaged, do
> they buy what I sell, what does it cost. That is five facts. Our story is not one of
> them, and design is not either — a media-buying decision at $600 is made on numbers.
>
> **What I'd send instead** — this is the whole thing:
>
> > 1,240 subscribers, 61% average open rate over the last 30 days. Roughly 70% RA/QA
> > managers and directors at device manufacturers, mostly US.
> >
> > You sell submission management software to exactly these people.
> >
> > One slot per issue, $600/week for four issues. 40 words and a link at the top. Happy
> > to send the last two weeks of issues so you can see what you'd be next to.
>
> That is the deck. It is also repliable in one line, which matters more than it sounds
> — a deck asks for a meeting, an email asks for a yes.
>
> **Where I would build something:** `storefront_set` gives us a permanent sponsor-facing
> page with the metrics, past issues, and the offering, at no cost. Link it from the
> email for anyone who wants more. That covers the 20% who want detail without slowing
> down the 80% who don't.

---

**Read next:** `10-resources/ref-design-system.md` ·
`50-guardrails/brand-voice-and-truth.md` · `20-systems/sales-and-pricing.md` ·
`20-systems/delivery-and-qa.md`
