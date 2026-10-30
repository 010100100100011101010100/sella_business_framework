# Dashboard — Marketing

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Build only when running more than one channel |
| **Prerequisite** | `30-dashboards/dashboard-spec.md`, `20-systems/marketing.md` |
| **Reads** | `content.json` · `clients.json` · `touches.json` · `metrics.json` |
| **Primary for** | C4, C8 · secondary C1, C10 |

---

## The question it answers

**"Which channels produced customers, and which are costing time for nothing?"**

**Most marketing effort produces nothing.** Without a scheduled look you will keep doing it
because it feels productive. This dashboard exists to make killing a channel easy.

---

## Layout

**Row 1 — customers by source.** The most useful marketing data you will ever have, and
the most under-collected.

```
SOURCE            CLIENTS   REVENUE (90d)
cold_email            4        $2,400
referral              2        $1,800
public_work           1          $800
linkedin              0             $0
content               0             $0
```

**Ask every customer where they came from and record it in `clients.json`.** Three months
of this beats any framework's channel ranking, because it is *your* market.

**Row 2 — cost per outcome.** The only thing that makes channels comparable.

```
CHANNEL        TIME (30d)   OUTCOMES        COST PER BOOKED CALL
cold_email        11 hrs    8 calls, 2 won         ~1.4 hrs
linkedin          12 hrs    0 calls, 0 won              —
```

**Count time, not just money.** For most cases here time is the scarce input, and a
channel consuming 12 hours for zero outcomes is expensive even at $0 spend.

**Row 3 — the compounding funnel** (only once it exists). Content published → traffic →
email captures → customers. Do not build this before month three; there is nothing to show.

**Row 4 — content log.** Date, channel, title, and `approved_by` where published in
someone's name. **The `approved_by` column is a compliance view for C10 and C4**, not
bookkeeping.

**Row 5 — audience** (C4, C8 only). Subscribers, **open rate**, growth rate.

> **Open rate is the real health metric, not subscriber count.** 900 subscribers at 55%
> is worth more than 4,000 at 20%, and sponsors know it. Show open rate larger.

---

## Rules specific to this dashboard

- **Attribution is asked, not inferred.** Do not guess a source from timing
- **Track time per channel.** The main cost is not money
- **Show zero-outcome channels prominently.** The purpose is to make cutting easy
- **Never report activity as achievement** (G12). "18 posts" is an input; "0 replies" is
  the result
- **Audience metrics carry their window** — "58% open rate over the last 30 days." A
  media-kit number without a window is a G3 problem waiting to happen

---

## Ten-case notes

| Case | The cut that matters |
|---|---|
| **C1** | Free-component downloads → email → paid. The whole funnel is this |
| **C4** | **Open rate over time.** Below 25% for three weeks = fix before growing |
| **C8** | Subscriber growth **and** listing decay together |
| **C10** | Free public repurposes → inbound enquiries. Direct and measurable |
| **C2, C5, C9** | **Referral source per client.** These businesses become referral-driven |
| **C3, C6, C7** | Minimal. The outreach dashboard covers the real channel |

---

## Worked example — the review that kills a channel

**C3, week 8:**

```
SOURCE          CLIENTS   REVENUE (90d)      CHANNEL      TIME   OUTCOMES
cold_email          2        $1,200          cold_email   11 hr  4 calls, 2 won
linkedin            0             $0         linkedin     12 hr  0 calls, 0 won
```

**The reading:** roughly equal time, wildly unequal outcomes. Six weeks is enough to know.

**The decision — cut LinkedIn.** Not because posting is worthless in general, but because
we are posting into a network of 90 connections with no reach, to a buyer who is not
browsing LinkedIn for data services.

**What the 12 hours becomes:** at ~2 hours per sample and a 21% reply rate, that is 6 more
samples ≈ 1.3 more replies ≈ a meaningful fraction of a pilot. A direct trade that favours
samples heavily.

**What is kept:** one piece of compounding work per week, rewritten as a **search-targeted
article** rather than a LinkedIn post — same underlying activity, a surface where the buyer
actually looks, and it can still be posted to LinkedIn afterwards at no extra cost.

**What would reopen it:** the operator's connections growing into the RevOps world, or a
client sharing a post. Neither has happened, and naming the condition means the decision
can be revisited on evidence rather than on restlessness.

---

**Read next:** `20-systems/marketing.md` · `20-systems/content-and-writing.md` ·
`50-guardrails/brand-voice-and-truth.md`
