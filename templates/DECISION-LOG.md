# Template — DECISION-LOG.md

> Copy to the business root. **Append-only.** This is the artifact that stops a future
> session — or a different agent — re-litigating settled questions.

---

## Two kinds of entry

**Decisions** — anything that shapes the business. **Daily log lines** — session
continuity.

```markdown
## [date] — [decision title]
**Decided:** what
**Because:** the reasoning, and the evidence rung (G1)
**Alternatives considered:** and why not
**Would reverse if:** the condition, with a date
```

```markdown
[date]  Shipped: [outputs, not activities]
        Blocked: [item] (asked [date], [n] days)
        Spent: [amount] ([unit cost])
        Next: [the single next action]
```

---

## Filled example

```markdown
## 2026-09-09 — Narrowed targeting to logistics and freight only
**Decided:** Target logistics/freight exclusively, not B2B SaaS generally.
**Because:** The operator spent 5 years as a logistics PM. They can talk to an ops
manager in that manager's language, which a generic data cleaner cannot. This is the only
real differentiator we have. Evidence: rung 2 — no market validation yet, this is a bet
on a stated asset.
**Alternatives considered:** Broad B2B SaaS (larger pool, no edge); adjacent verticals
alongside (dilutes the edge and the messaging).
**Would reverse if:** reply rate under 5% by day 21.

## 2026-09-20 — Replaced enrichment cost anchor with measurement
**Decided:** Model cost per record moves from $0.033 (framework anchor) to $0.041
(measured across 4 jobs, 14,200 records).
**Because:** 30 days of real data. G1/G3 — anchors must be replaced once measured.
**Effect:** Modelled margin at $0.12/record moves from 72.7% to 71.2%. Still above the
45% floor. No price change.

## 2026-09-24 — Kill criterion fired: day 30, replies but zero pilots
**Decided:** Escalated to operator. Recommended a $250 micro-pilot rather than stopping.
**Because:** 20.6% reply rate is well above the 8–15% model, so the top of the funnel
works. Both calls asked for a smaller first test; one needed director sign-off at $600.
That is the T3 approval-threshold failure, not a demand failure.
**Alternatives considered:** Drop the pilot to $450 (moves the line, does not solve
sign-off); stop and re-select (discards a working funnel).
**Would reverse if:** zero takers on the $250 micro-pilot from the 7 who already replied,
by day 45. **New criterion written; old one not extended.**

2026-09-25  Shipped: 6 samples produced and sent. Micro-pilot offer added to sequence.
            Blocked: nothing.
            Spent: 12.40 USDC (6 prospects, $2.07 each).
            Next: follow up with the 7 prior repliers on the new price.
```

---

## Rules

- **Append-only. Never edit or delete a past entry.** Correct it with a new one.
- **Log "continue unchanged" too.** A documented decision to continue is information later
  when you are working out when things went wrong.
- **Every decision carries its reversal condition, with a date.** Without one it is a
  preference, not a decision — and it will be reopened on impatience rather than evidence.
- **Log anchor→measurement swaps** (G1, G3). By month three the framework's numbers should
  be almost entirely gone from the charter.
- **Log fired kill criteria and what was decided**, including when the operator chose to
  continue past one.
- **Read the last ~10 entries at session start** (`20-systems/daily-review.md`). Do not
  re-litigate.
