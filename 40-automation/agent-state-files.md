# Automation — Agent State Files

| | |
|---|---|
| **Status** | **REQUIRED READ** at the end of initiation |
| **Prerequisite** | `00-core/initiation.md`, `10-resources/business-resources.md` |
| **Output** | `.claude/`, `.cursor/`, and `.antigravity/` manifests |

---

## The problem these solve

**A different agent — or you, in a fresh session — will pick this business up with no
memory of any of it.**

Without a manifest that agent will read the wrong files, miss the guardrails that apply,
re-open settled decisions, and re-litigate the vertical you chose in week one. It will
also read files that were deliberately *not* needed, burning context on infrastructure
this business will never build.

**The manifest is the handoff.** It says: read these, in this order, because of these
decisions.

**Generate it at the end of initiation, and update it whenever a referenced file becomes
required.**

---

## What goes in

Three things, and the third is the one people omit:

1. **What to read, in order** — core, case study, systems in use, resources acquired,
   guardrails triggered
2. **Where the live state is** — charter, queue, decision log, data files
3. **What was deliberately NOT read, and why** — so a future agent knows the omission was
   a decision, not an oversight, and does not go re-derive it

---

## The canonical file: `.claude/required-reads.md`

This is the source of truth. The other manifests point at it.

```markdown
# Required reads — Northwind Data Cleaning (C3)

Generated 2026-09-03 · updated 2026-09-14

## Read first, in this order
1. 00-core/reasoning-guardrails.md
2. 00-core/initiation.md
3. 00-core/case-registry.md
4. case-studies/C3-data-cleaning-enrichment.md
5. 00-core/viability-screen.md
6. 00-core/human-action-queue.md
7. 00-core/delivery-model-selector.md
8. 00-core/operating-cadence.md

## Systems in use
- 20-systems/outreach.md          primary channel
- 20-systems/delivery-and-qa.md   control-total gate
- 20-systems/sales-and-pricing.md
- 20-systems/finance-and-runway.md
- 20-systems/daily-review.md

## Resources acquired — read because we built or bought this
- 10-resources/business-resources.md
- 10-resources/ref-payments-and-billing.md    PayPal + invoice · 2026-09-03
- 10-resources/ref-email-domain.md            getdatacleaned.com · 2026-09-03
- 10-resources/ref-procurement-marketplaces.md  stableenrich · 2026-09-05
- 10-resources/ref-website.md                 one-page offer · 2026-09-14
- 10-resources/ref-design-system.md           Carbon, restrained · 2026-09-14

## Guardrails triggered by this business
- 50-guardrails/legal-and-compliance.md   GDPR, DPA, vendor resale terms
- 50-guardrails/security-and-secrets.md   client data, 30-day deletion
- 50-guardrails/brand-voice-and-truth.md  no anchors quoted as results
- 50-guardrails/spend-and-approval-policy.md

## Live state — read before acting
- BUSINESS-CHARTER.md
- HUMAN-ACTION-QUEUE.md
- DECISION-LOG.md          last ~10 entries. DO NOT re-litigate settled decisions
- ASSETS-AND-LICENCES.md
- JOBS.md
- data/*.json

## NOT read — decisions, not oversights
- ref-social-x.md, ref-social-linkedin.md, ref-social-youtube.md
  RevOps buyers are not reached through social. Decided 2026-09-03
- ref-docs-and-decks.md
  Deliverable is a spreadsheet + one-page summary. No decks
- 30-dashboards/*
  Under 50 prospects. Data files are readable directly. Revisit week 3
- case-studies/C1,C2,C4–C10
  Not our case. C6 is the planned upsell — read it only when that starts
```

**The "NOT read" section is the most valuable part.** It stops a future agent spending an
hour re-deciding something, and it makes the reasoning auditable.

---

## `.claude/CLAUDE.md`

Short. Points at the manifest and carries the non-negotiables.

```markdown
# Northwind Data Cleaning — agent instructions

This is a business run under the Autonomous Business Framework.

**Before doing anything, read `.claude/required-reads.md` and follow its order.**

## Non-negotiable
- Never fabricate testimonials, metrics, credentials, or triggers (G3)
- Sell before you build (G2)
- Check kill criteria in BUSINESS-CHARTER.md — read them, do not recall them (G7)
- You are not the legal person. Blocked items go in HUMAN-ACTION-QUEUE.md (G9)
- Report losses as loudly as wins (G12)
- Never accept a customer's credentials

## Spend
seed 200 · max/call 15 · approval 40 · daily 60 USDC
`purchase_preview` before every buy. `business_status` before planning work.

## Session protocol
Start: charter → queue → last 10 decision-log entries → business_status
End:   append Shipped / Blocked / Spent / Next to DECISION-LOG.md
Report weekly, not daily. Escalate immediately per guardrails §Escalation triggers.
```

---

## `.cursor/rules/business.mdc`

Cursor reads `.mdc` rule files. Same content, its format:

```markdown
---
description: Autonomous business operating rules — read before any work
alwaysApply: true
---

This repository runs a business under the Autonomous Business Framework.

Read `.claude/required-reads.md` first and follow its order. Live state is in
BUSINESS-CHARTER.md, HUMAN-ACTION-QUEUE.md, and DECISION-LOG.md.

Never fabricate testimonials, metrics, credentials, or outreach triggers. Sell before
building. Check kill criteria by reading them, not from memory. You cannot sign, verify
identity, or open accounts — those go to HUMAN-ACTION-QUEUE.md. Report losses as loudly
as wins. Never accept a customer's credentials.

Spend: seed 200 / max-per-call 15 / approval 40 / daily 60 USDC. `purchase_preview`
before every purchase.
```

---

## `.antigravity/rules.md`

```markdown
# Business operating rules

Entry point: `.claude/required-reads.md` — read it first, in order.

State: BUSINESS-CHARTER.md · HUMAN-ACTION-QUEUE.md · DECISION-LOG.md · data/*.json

Hard rules: no fabricated social proof or metrics · sell before building · kill criteria
are read, not recalled · the agent is not the legal person · report losses plainly ·
never accept customer credentials.

Spend caps: seed 200 · max/call 15 · approval 40 · daily 60 USDC.
```

---

## Keeping them current

| Trigger | Update |
|---|---|
| A referenced file is read | Add to "Resources acquired" with the date and reason |
| A guardrail becomes relevant | Add to "Guardrails triggered" |
| A resource is deliberately declined | Add to "NOT read" with the reason and date |
| Spend caps change | All three manifests |
| The case changes or a second business starts | Regenerate entirely |
| Monthly close | Sanity-check the manifest against reality |

**Do not let them drift.** A manifest that lists files nobody reads, or omits the guardrail
that now applies, is worse than none — it will be trusted and it will be wrong.

**One manifest per business.** If the operator eventually runs two (G10 — only after the
first clears its bar), they get separate directories and separate manifests. Never merge
them; the whole value is that a manifest describes *one* business's decisions.

---

## Ten-case reference — what the manifest most needs to carry

| Case | The thing a fresh agent must not miss |
|---|---|
| **C1** | The day-14 gate: do not build pack 2 before pack 1 sells 50 |
| **C2** | **V-model.** Acceptance criteria are signed before build; changes are priced |
| **C3** | **30-day client-data deletion** + vendor resale terms already verified |
| **C4** | **The date never moves.** Editorial position is the operator's, in writing |
| **C5** | The operator makes the calls. Delegated GBP access only, never a password |
| **C6** | **LinkedIn ToS boundary** + the trigger-tier minimum |
| **C7** | **Disclaimer in every deliverable.** Never answer a legal question |
| **C8** | **Phase gate:** no selling posts before the audience number is real |
| **C9** | **Human reviews every delivery. No credentials, at any permission level** |
| **C10** | Voice guide + never-say list; nothing publishes without client approval |

---

## Worked example — the manifest earning its keep

**The situation.** Month two. The operator opens a fresh session in a different tool and
asks the agent to "widen the prospect list, we're going slowly."

**Without a manifest:** the agent reads the repo, sees a slow-moving list, and widens into
adjacent verticals. It discards the operator's logistics background — the one real
advantage — because nothing told it that was a decision.

**With the manifest:**

> Read `.claude/required-reads.md` and the last decision-log entries before starting.
>
> **I'm not going to widen the list, and here is the entry that decided it:**
>
> > **2026-09-09** — Narrowed to logistics/freight only. Reason: operator's 5 years as a
> > logistics PM is the edge; they can talk to an ops manager in that manager's language.
> > A generic list removes the only differentiator we have. **Would reverse if reply rate
> > drops below 5% by day 21.**
>
> That is a settled decision with a stated reversal condition. We are at day 34 and the
> reply rate is **18.2%** — well above both the reversal threshold and the 8–15% model.
>
> **So "going slowly" is not a targeting problem.** Looking at the actual numbers: 61
> sent, 13 replied, 4 calls, **0 closed.** The funnel is excellent until the close.
>
> **That matches a kill criterion in the charter** — "day 30: replies but zero pilots →
> pilot price is above the buyer's no-approval threshold, or the sample is not
> persuasive." It fired four days ago and should have been reported.
>
> **What I'd do instead of widening:** add a $250 micro-pilot below the corporate-card
> threshold and offer it to the 13 people who already replied. That tests the actual
> constraint. Widening the list would add more replies to a funnel that already produces
> replies and not revenue — more of the thing that is working, none of the thing that is
> not.
>
> Want me to go that way?

**What the manifest and log prevented:** discarding the differentiator, on impatience,
against a documented condition that had not been met — and it surfaced a fired kill
criterion nobody had reported. **A fresh agent with no manifest would have confidently
done the wrong thing and had a good reason for it.**

---

**Read next:** `00-core/initiation.md` (outputs) · `templates/DECISION-LOG.md` ·
`templates/BUSINESS-CHARTER.md` · `10-resources/business-resources.md`
