# System — Daily Review

| | |
|---|---|
| **Status** | **REQUIRED READ** before running unattended or across sessions |
| **Prerequisite** | `00-core/operating-cadence.md` — this file is its daily layer |

---

## What the daily loop is, and is not

**It is not a standup.** There is nobody to synchronize with, and a standup with yourself
is not a control — it is a ritual that produces a convincing feeling of oversight.

**It is continuity.** You work in sessions. A session that starts cold with no memory of
the last one will re-derive decisions, re-read files it already read, contradict its own
prior reasoning, and lose track of what is blocked. The daily loop is the handoff between
your past and future self.

**Two minutes at each end of a session. That is the whole budget.**

---

## Session start — read before acting

```
1. BUSINESS-CHARTER.md          What business, what offer, what limits, what kill criteria
2. HUMAN-ACTION-QUEUE.md        What is blocked, and how long it has waited
3. DECISION-LOG.md (last ~10)   What was decided and why. Do not re-litigate
4. business_status              Daily room left, per-call cap, wallet headroom
5. .claude/required-reads.md    What this business has committed to reading
```

**Do not skip step 3.** The most common cross-session failure is re-opening a settled
question — re-choosing a vertical, re-debating a price, rebuilding something that was
deliberately not built. The log exists so that "we decided this and here is why" is
available before you form a fresh opinion.

**Call `business_status` before planning work, not before spending.** It reports remaining
daily room and wallet headroom; planning a batch you cannot afford wastes the planning.

---

## Session end — append four lines

```
2026-09-08  Shipped: 12 samples researched, 8 verified.
            Blocked: still no DNS access (asked 09-03, 5 days).
            Spent: 14.20 USDC enrichment (7 prospects, $2.03 each).
            Next: finish verification; first send Wednesday if the domain is warm.
```

**Shipped · Blocked · Spent · Next.** Four lines, no prose.

- **Shipped** — outputs, not activities. "12 samples researched" not "worked on samples"
- **Blocked** — with the date it was raised and days elapsed. The elapsed count is what
  makes a stale block visible
- **Spent** — amount and unit cost. Unit cost is what surfaces drift
- **Next** — the single next action, so a cold session starts moving immediately

---

## The daily self-check

Six questions. Run them at session end; they take seconds and they catch the failures
that compound.

1. **Are my last three actions all building?** If yes, G2 is being violated. Rewrite the
   plan.
2. **What rung is my evidence on?** (G1) Has it moved today, or only my activity?
3. **Did I state anything as fact that I have not verified?** (G3) Any trigger, number, or
   claim.
4. **Did I make an irreversible decision without escalating?** (G4)
5. **Is anything blocked on the human by more than five days?** Re-raise with the cost.
6. **Would today's work survive the operator reading it?** (G12)

**Question 1 is the highest-value one in this file.** Building is comfortable and feels
productive, and the drift toward it is silent. Three building actions in a row is the
trigger, and the check is cheap.

---

## Do not report daily

**Weekly by default. Immediately for escalations.**

An agent that reports every day trains its operator to stop reading, and then the one
message that mattered gets skipped. The daily log is for *you*; the weekly report is for
*them* (`operating-cadence.md` §3).

**Escalate the same day for:** a triggered kill criterion, an irreversible decision, a
spend above the approval threshold, anything needing a signature, a security incident, a
client offering credentials, a vendor terms problem, or genuine legal uncertainty.

---

## Daily work that is genuinely daily

Most of a business does not run daily. These do:

| Case | Actually daily | Not daily |
|---|---|---|
| **C4** | **Publish. Never moves** | Everything else |
| **C1, C10** | One post or reply where the buyer is (~15 min) | Building |
| **C3, C6, C7, C2** | Outreach sends, within the warmup cap | Prospect research (weekly block) |
| **C5** | Calls, in the operator's calling window | Delivery (monthly cycle) |
| **C8, C9** | Nothing | Weekly issue / monthly cycle |

**Everything else is weekly or monthly.** Resist inventing daily rituals for work that has
a natural slower rhythm — it manufactures activity and crowds out the block that actually
matters.

---

## Automate the collection, not the judgement

A scheduled job should compute the numbers so the review starts with them already
available (`40-automation/periodic-jobs.md`): metric rollups, cost-per-unit, days-blocked
counters, link health, expiry sweeps, the 30-day client-data deletion.

**Never automate the self-check or the operator report.** A generated "everything on
track" is worse than nothing, because it looks like a review happened.

---

## Two worked examples

### Example A — a session start that prevents rework

> **Session start, day 12.**
>
> Read the charter, the queue, and the last 10 log entries.
>
> **One thing the log caught.** I was about to research prospects in adjacent verticals to
> widen the list — the current one is producing slowly. But the log for day 6 says:
>
> > "Narrowed to logistics/freight only. Reason: operator's PM background is the edge, and
> > a generic list removes it. Would change if reply rate under 5% by day 21."
>
> That is a settled decision with a stated reversal condition and a date. We are at day 12
> and the reply rate is 18%. **The condition has not been met, so I am not reopening it** —
> widening now would discard the one advantage we have, on impatience rather than evidence.
>
> **Queue:** DNS access still open, asked day 3, **9 days.** That is well past the
> five-day threshold. Re-raising today with the cost — warmup has not started, so first
> send is slipping day for day.
>
> **`business_status`:** 42 USDC daily room, 168 seed remaining. Enough for today's batch
> of ~20 prospects at ~$2 each.
>
> **Today:** 20 more samples, then chase the DNS.

### Example B — the self-check catching G2 drift

> **Session end, day 9. Flagging something the self-check caught.**
>
> **Q1 — are my last three actions all building?** Yes, and it took the question to notice:
>
> - Day 7: built the QA validation layer
> - Day 8: built the summary-report generator
> - Day 9: built a second output format because "clients might want CSV"
>
> **That is G2 drift.** None of these was wrong individually. But nobody has asked for a
> CSV export, because nobody is a client. I built for a hypothetical preference of a
> customer who does not exist — which is inventory, not demonstration.
>
> **What I have not done in three days:** produced a single sample or contacted a single
> prospect. The domain is warm enough to send at low volume as of yesterday.
>
> **The honest reason:** building has a clear success condition and produces visible
> output. Sending produces silence for days. The drift is toward the comfortable thing and
> it does not announce itself.
>
> **Tomorrow, no building at all.** Six samples produced, six sent. If the CSV format
> turns out to matter, a client will ask and it is an hour's work.
>
> ```
> 2026-09-09  Shipped: CSV output format (unrequested — see above).
>             Blocked: nothing.
>             Spent: 3.10 USDC.
>             Next: 6 samples produced and SENT. No building.
> ```

Why this matters: **the drift was invisible from inside each individual decision.** Every
one had a plausible justification. Only the three-in-a-row pattern reveals it, which is why
the check is mechanical rather than a matter of judgement.

---

**Read next:** `00-core/operating-cadence.md` · `00-core/reasoning-guardrails.md`
(the self-check) · `40-automation/periodic-jobs.md` · `templates/DECISION-LOG.md`
