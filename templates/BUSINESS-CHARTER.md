# Template — BUSINESS-CHARTER.md

> Copy this to the business root as `BUSINESS-CHARTER.md`. **Written at the end of
> initiation, before any other work.** It is the single source of truth; every other
> artifact defers to it.
>
> Filled example throughout in blockquotes, using C3.

---

```markdown
# BUSINESS CHARTER — [name]

Created [date] · last updated [date] · case [C#]

## 1. The business
One paragraph. What we sell, to whom, and why it works.
```
> Cleaning and enriching B2B CRM databases for logistics and freight companies of
> 20–200 people. They export, we return it deduplicated, validated, and enriched in four
> days. It works because the value is provable in a spreadsheet and the buyer can approve
> the entry price alone.

```markdown
## 2. The buyer
Specific enough to name ten. Then name ten.

Title(s):
Company profile:
Trigger signals:
The ten:  1. … 10.
```

```markdown
## 3. The offer
| Tier | Price | Contents |
Free demonstration:
Paid first step (must sit below the buyer's no-approval threshold):
Main offer:
Recurring version:
```

```markdown
## 4. Distribution
Primary channel:
The specific play:
Why this channel reaches this buyer:
What we are NOT doing, and why:
```

```markdown
## 5. Operator assets  (from initiation §2 — only what we will actually use)
Audience:
Relationships / introductions:
Credibility:
Existing accounts and tool seats:
Committed behaviours:      e.g. will take calls / will review monthly / will publish
```

```markdown
## 6. Money path   (walked end to end — T1)
Customer decides →  pays by …  →  lands in …  →  operator accesses via …  →  tax handled by …
Recurring billing available?  yes / no / prepaid blocks instead
```

```markdown
## 7. Spend limits
seed __ · max per call __ · approval threshold __ · daily cap __  (USDC)
commerceMode: human_assisted
Fiat spend requiring approval: any recurring subscription; anything over $__
```

```markdown
## 8. Delivery model
Layer 1 (discovery):   iterative — always
Layer 2 (engagement):  [model]
Deciding variable:
WIP limit:
Quality gate:                         pass condition:
Change mechanism (if scope is fixed):
```

```markdown
## 9. Kill criteria   (G7 — dated and numbered, written BEFORE starting)
| Checkpoint | Condition | Action |
```
> | Day 21 | 20 samples sent, zero replies | Diagnose targeting before sending more |
> | Day 30 | Replies but zero pilots | Price is above the approval threshold, or the sample is not persuasive |
> | Day 45 | Zero revenue | Kill the vertical, re-target, restart once |
> | Day 90 | Under $1,500 cumulative | Kill C3 |
> | Any time | Gross margin under 45% on two consecutive jobs | Stop selling; re-price |

```markdown
## 10. The 90-day target
One number:

## 11. Selection reasoning
Chosen: [case] — score __
Runner-up: [case] — score __
The factor that decided it:
Disqualified, and why:

## 12. Viability screen
T1 money path __ · T2 reachability __ · T3 unit economics __ · T4 demonstration __ · T5 survival __
Confidence: low / medium / high        Why:
Red flags:
What would change confidence, and by when:
```

---

## Rules

- **Kill criteria are written before starting and read, not recalled** (G7). Re-read at
  every weekly review.
- **Every number is labelled measured or modelled** (G3). When an anchor is replaced by a
  measurement, update here and log the swap in `DECISION-LOG.md`.
- **Section 2 must contain ten actual names.** If it cannot, the viability screen has not
  passed and work should not start.
- **Update at the monthly close.** A charter that no longer describes the business is
  worse than none.
