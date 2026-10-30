# Template — HUMAN-ACTION-QUEUE.md

> Copy to the business root. **Maintained continuously.** Blocking first, newest at the
> top of each section. Mirror it into `data/queue.json` for the ops-health dashboard.

---

```markdown
# Human Action Queue — [business]

## Blocking — work is stopped until these are done

- [ ] **[Action]** (cost, time estimate)
      *Unblocks:* [what cannot happen without it]
      *Lead time:* [if any]
      *Requested:* [date]

## High-leverage — not blocking, but each is worth weeks

- [ ] **[Action]** (time estimate)
      *Worth:* [what it saves or produces]
      *Requested:* [date]

## Waiting on you — asked, no response yet
- [ ] [item] — *asked [date], [n] days ago*

## Done
- [x] [item] — [date]. *Effect:* [what it changed]
```

---

## Filled example

```markdown
## Blocking

- [ ] **Buy sending domain** (~$12, 10 min) — Namecheap or Cloudflare, then DNS access.
      *Unblocks:* all outreach. Warmup is 3 weeks after purchase, so this is the critical
      path — every day of delay adds a day to first revenue.
      *Requested:* 2026-09-03

- [ ] **Confirm PayPal invoicing as an individual** (5 min) — I need to walk the whole
      money path with you once.
      *Unblocks:* receiving any revenue at all.
      *Requested:* 2026-09-03

## High-leverage

- [ ] **Intro to your contact at Meridian Freight** (5 min)
      *Worth:* roughly 2 weeks of cold outreach, and a calibration call on pricing before
      I send 40 emails at the wrong number.
      *Requested:* 2026-09-04

## Waiting on you
- [ ] DNS records for getdatacleaned.com — *asked 2026-09-03, 9 days ago.* Warmup has not
      started; first send is slipping day for day.

## Done
- [x] Confirmed no EU customers initially — 2026-09-03. *Effect:* GDPR obligations
      deferred. **Revisit before any EU prospect enters the list.**
```

---

## Rules

- **Every item states what it unblocks or what it is worth.** That is what turns a task
  list into something an operator acts on.
- **Ask specifically.** "Do you have social media?" produces nothing. "Do you have an X
  account with 300+ developer followers, and will you publish two posts a week I draft?"
  produces an answer you can plan around.
- **Batch and order.** Five specific asks with an order get done. Twenty do not.
- **Re-raise anything over five days** with what the delay is costing.
- **Populate Sella's `needs_human`** from the blocking section — the operator sees it
  before deciding to fund.
- **Never simulate a blocked action** (G9). Do everything that does not depend on it, and
  say the business is not stalled.
