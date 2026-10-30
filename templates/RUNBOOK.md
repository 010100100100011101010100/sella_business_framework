# Template — RUNBOOK.md

> Copy to the business root. **The actual steps to deliver one unit of work.** Updated
> every time they change. This is the compounding asset in an operations business (G11) —
> every delivery should make the next one cheaper.

---

```markdown
# Runbook — [deliverable]

Last updated [date] · last run [date] · avg cycle time [n]

## Inputs required
- [ ]                                       ← from the client
- [ ]                                       ← from us

## Steps
1.
2.
…

## The quality gate
**Check:**
**Pass condition:**
**On fail:**                                ← do NOT deliver
**Signed off by:**                          ← named human for C9

## Delivery
Format:
Message template: see below
Where it goes:

## Post-delivery
- [ ] Log revenue and COGS in transactions.json
- [ ] Set data_delete_due (+30 days)
- [ ] Ask for the referral                  ← at delivery. Later never comes
- [ ] Offer the recurring version, with an honest reason to defer it
- [ ] Update this runbook if anything changed

## Known failure modes
| Symptom | Cause | Fix |

## Estimate vs actual
| Date | Estimated | Actual | Multiplier |
```

---

## Filled example — extract

> **Steps.** 1. Receive export, confirm format and row count. 2. **Sample 100 rows and
> run the margin arithmetic — never quote before this.** 3. Normalize company names and
> domains. 4. Dedup on domain + normalized name; write the match rule to tab 2. 5. Verify
> emails. 6. Enrich company-level. 7. Enrich person-level *if in scope*. 8. Compute the
> change summary. 9. **Gate.** 10. Deliver.
>
> **Gate.** Check: control total. Pass: matched + unmatched + flagged = source row count,
> exactly. **On fail: do not deliver.** Investigate — a mismatch means a row was dropped
> or double-counted, and either is a wrong number in a spreadsheet the client will trust.
>
> **Known failure modes.**
> | Enrichment hit rate far below model | Unfamiliar vertical | Sampled the wrong subset — sample the actual mix, weighted |
> | Control total off by a small number | Blank rows in source | Strip and record the count in the summary |
>
> **Estimate vs actual.** 2026-09-20 · est 4h · actual 6.5h · **1.63×** — European records
> needed manual review.

---

## Rules

- **Write it after the first delivery, not before.** A runbook written in advance is a
  guess; one written after is a record.
- **Every support question becomes a runbook or docs edit the same day.** Support that
  does not reduce future support is a treadmill.
- **Log estimate vs actual every time.** Most people need a 1.4–1.8× multiplier on their
  instinct and cannot know theirs without the data.
- **The gate is not optional and not a vibe.** A named check with a pass condition, run
  every time (`20-systems/delivery-and-qa.md`).
- **One runbook per deliverable type.** Client-specific quirks go in a client profile,
  not here.
