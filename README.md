# Autonomous Business Framework

A set of instruction files you hand to your coding agent so it can choose and run a
small, sustainable business for you.

**What it is for:** boring, proven, cash-generating businesses — a software agency,
a data-cleaning service, a productized component library, a paid newsletter, a local
SEO retainer book. Sustainable revenue, not venture growth.

**What it is not for:** venture-scale startups. Those are non-standardized and this
framework deliberately excludes them.

## How to use it

1. Put this directory where your agent can read it.
2. Tell your agent: *"Read SKILL.md and run the initiation."*
3. Answer its questions. **Especially the asset inventory** — what accounts, contacts,
   and credibility you already have changes which business it should pick.
4. Approve the business it proposes, or push back. It will show you its scoring.
5. Work through the human action queue it gives you. Some items only you can do.

## What it will produce

- `BUSINESS-CHARTER.md` — the business, the buyer, the offer, the channel, the limits,
  and the kill criteria
- `HUMAN-ACTION-QUEUE.md` — what it needs from you, ordered, with what each unblocks
- `DECISION-LOG.md` — every significant decision and why

## Structure — 60 files

```
SKILL.md                  Entry point — tells the agent what to read, in order
00-core/         7        Guardrails, initiation, case index, viability, cadence,
                          delivery-model selection, human action boundary
case-studies/   10        The ten canonical businesses, in depth
10-resources/   12        Routing index → website, design system, payments, email
                          domain, hosting, auth, procurement, socials, docs
20-systems/      9        Outreach, marketing, sales, delivery/QA, content,
                          support, data & research, finance, daily review
30-dashboards/   6        Shared data contract + five dashboards (no servers)
40-automation/   2        Periodic jobs, agent state manifests
50-guardrails/   4        Legal & compliance, security, brand truth, spend
templates/       8        Artifacts the agent fills in
```

**The agent is instructed not to read all of it.** `10-resources/business-resources.md`
routes to only the resource files this particular business needs, and records what was
read — and what was deliberately skipped — in `.claude/required-reads.md`.

## The ten businesses

React component marketplace · fixed-bid software agency · data cleaning and enrichment ·
vertical news brief · local SEO retainers · ICP lead research · SMB compliance docs ·
niche job board · invoice reconciliation · content repurposing studio.

Full detail in `case-studies/`. Start with `00-core/case-registry.md`.

## Two things to know before you start

**Every number in this framework is a planning anchor, not a promise.** They are
modelled ranges to build a first plan against and replace with your own measurements.
The agent is instructed never to quote them to a customer as if they were results.

**There is no zero-KYC path to real revenue.** Every payment rail that touches money
verifies a legal person. "Lean" here means reusing accounts you already have and
deferring entity formation — not avoiding identity verification, which is not
avoidable.
