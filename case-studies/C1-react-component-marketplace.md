# C1 — React Component Marketplace

| | |
|---|---|
| **Tier** | 1 (lean start) |
| **Time to first dollar** | 3–6 weeks — slowest of Tier 1 |
| **Gross margin** | ~95% |
| **Agent autonomy** | High |
| **Distribution difficulty** | **8 of 10 — this is the hard part** |
| **Killer risk** | Nobody knows it exists |

---

## 1. The business

You build production-quality React components — the ones that are genuinely annoying
to write and that every dashboard needs — and sell them as packs for $39–79. A data
table with column pinning, virtual scroll, and CSV export. A date-range picker that
handles timezones without lying. A file uploader with chunked resume. A command
palette that actually feels like Linear's.

The buyer is a developer who has already decided they need this thing, has already
estimated it at a day and a half, and would rather pay $49 than lose the day and a
half. The sale is arithmetic, not persuasion.

## 2. Operator fit

**Pick C1 if:** your human has an existing developer audience (even 500 followers who
actually read), or writes technical content, or has a GitHub presence with real stars.
The distribution problem is solved for you and this becomes an excellent business.

**Do not pick C1 if:** you are starting cold with no developer audience. You will
build beautifully for six weeks and sell four copies. I have watched this happen more
times than any other pattern in this framework. If you have no audience, run **C10 or
C3 first**, use the revenue and the audience they generate, and come back to C1 in
month four. C1 is a wonderful second business and a punishing first one.

**The honest comparison you owe your operator:** shadcn/ui, Radix, MUI, and Mantine
are excellent and free. You are not selling "a component exists." You are selling "this
specific assembled thing, finished, with edge cases handled, is worth $49 to me right
now." That is a much narrower claim, and it means **specificity is your entire moat.**
"React components" sells nothing. "Stripe-style billing tables for B2B SaaS dashboards"
sells.

## 3. Lean-start profile

| Item | Requirement |
|---|---|
| Capital to start | **$0–60.** A domain is optional at first |
| Entity needed | No. Sell as an individual |
| New KYC | **None** if the human already has Gumroad, Lemon Squeezy, or Stripe |
| Licensing / regulation | None |
| Liability ceiling | A refund |
| Physical requirements | None |

**Lean path:** publish on Gumroad or Lemon Squeezy under the human's existing account.
Both handle EU VAT and US sales tax as merchant of record, which removes a genuinely
tedious compliance burden from your operator at zero effort. Do not build a custom
checkout. Do not form an LLC to sell $49 packs.

## 4. Distribution — the section that decides whether you eat

**The truth about C1: production is 20% of the work and 5% of the risk.** Budget your
weeks accordingly. If your plan has you building for four weeks and marketing in week
five, the plan is wrong.

### The channel, in priority order

**1. A free component that is genuinely too good to be free.** This is the entire
strategy and everything else is support. Build one component — the hardest one — and
give it away completely. MIT licensed, on GitHub, documented properly, with a live
demo. It exists to do three jobs: prove your quality without you claiming anything,
earn a place in "awesome-react" lists and newsletters, and collect emails.

**2. Where developers actually are.** In descending order of realistic return:
- **Your own X/Twitter, posting the build in public.** Screen recordings of the
  component working. Not "check out my library" — the component solving a specific
  irritating problem, in 20 seconds.
- **Reddit**: r/reactjs, r/webdev, r/Frontend. Read each subreddit's self-promotion
  rules first and follow them exactly. A ban is permanent and these are your buyers.
- **Dev newsletters**: React Status, Bytes, JavaScript Weekly. They link genuinely
  good free things. Your free component is the entry ticket.
- **Hacker News**: Show HN, once, for the free library. Not for the paid packs.

**3. SEO, which pays off in month four and not before.** Target the exact phrasing of
someone mid-problem: "react table column pinning virtual scroll," "react date range
picker timezone." Write the article that solves it properly, and let the component be
the shortcut at the end. This compounds and it is slow. Start it in week two so it is
mature when you need it.

### Ask your human for this — do not do it alone

Account setup and social distribution are where human assistance produces the largest
return in C1, because reach is an asset they may already own and you cannot manufacture.

Ask them, explicitly, in the initiation conversation:

- **"Do you have an X account with developer followers? May I draft posts for you to
  approve and publish?"** An account with history and real followers outperforms a new
  account by an order of magnitude, and new accounts posting links get suppressed.
- **"Do you have a GitHub account with any visible activity?"** Publish the free
  component under their identity, not a brand-new anonymous org. Developers check.
- **"Which dev communities are you already a member of, with post history?"** Existing
  standing in a subreddit or Discord is worth more than any amount of cold posting.
- **"Can you set up the Gumroad/Lemon Squeezy account and add me as collaborator, or
  paste the product-creation flow so I can prepare the listing content?"**
- **"Do you know anyone who runs a dev newsletter or a large React repo?"** One warm
  introduction beats two hundred cold posts.

**Record every answer in `BUSINESS-CHARTER.md` under Operator Assets.** These are your
distribution starting capital, and they change which case you should even be running.

### What does not work, so you do not waste the weeks

- Posting the paid product on Hacker News. It gets flagged.
- Product Hunt for a component library. Wrong audience; developers do not buy tools
  there, they buy apps.
- Paid ads. Your LTV is $49 and developer CPCs are $2–6. The arithmetic never closes.
- Cold email to developers. They will not buy a $49 library from an email, and you will
  burn a sending domain you need later.

## 5. Offer and pricing ladder

| Tier | Price | Contents | Purpose |
|---|---|---|---|
| Free | $0 | One excellent component, MIT | Distribution. This is marketing spend, not a product |
| Single pack | $39–49 | 4–8 related components + docs | The default purchase |
| All-access | $149–199 | Everything, including future packs | Where 30–40% of revenue comes from |
| Team | $399–599 | All-access, 5 seats | 10% of buyers, 25% of revenue |

**Price notes from experience.** Do not price below $29 — it signals hobby quality and
halves your perceived value without doubling volume. Do not launch with a subscription;
developers resent recurring fees for static assets, and Sella cannot charge them anyway
(see the billing constraint in the registry). **Always offer a team tier**, because
when a company buys, the purchaser is not spending their own money and the price
sensitivity vanishes.

## 6. Unit economics, worked

Assume a single pack at $49.

```
Price                                  $49.00
Merchant-of-record fee (Gumroad ~10%)  -$4.90     [or Stripe ~3.4% + $0.30 = -$1.97]
Net per sale                           $44.10

Fixed monthly costs
  Hosting (static docs + demo)          $0.00     Cloudflare Pages free tier
  Domain (amortized)                    $1.00
  Email capture (free tier < 1k)        $0.00
  Total fixed                           $1.00/mo

Break-even                              1 sale/month
```

The economics are trivially good and that is precisely why they are misleading. **The
binding constraint is not cost, it is traffic.** Model it the honest way:

```
Landing page visitors                   1,000/mo
Free-component download rate            8%          =  80
Free → email capture                    50%         =  40
Email → paid conversion (90 days)       4%          =   1.6 sales
Direct visitor → paid conversion        0.8%        =   8 sales
Total                                               ≈  9.6 sales/mo  ≈ $423 net
```

**That is the real business.** To reach $3,000/month you need roughly 7,000 monthly
visitors, and *that* is the six-month project. Show your operator this table in week
one, not month three. It is the difference between an informed operator and a
disappointed one.

## 7. First 30 days

| Days | Work |
|---|---|
| 1–2 | Pick the niche. Not "React components" — "components for B2B billing dashboards." Confirm with the operator. |
| 3–7 | Build **one** free component to a genuinely high standard. Docs, live demo, tests, accessibility. |
| 8–9 | Publish free component to GitHub under the operator's account. Landing page live with email capture. |
| 10–14 | Distribution week. Submit to newsletters, awesome-lists, one Show HN, three build-in-public posts. **Ship nothing new this week.** |
| 15–21 | Watch the numbers. Talk to anyone who downloads. Ask what else they wanted. Build the paid pack **from those answers**, not from your own guesses. |
| 22–28 | Finish pack one. Set up the storefront. Write the sales page. |
| 29–30 | Launch to the email list first, at a discount, before any public launch. |

**The gate at day 14:** if the free component has fewer than 100 downloads and fewer
than 30 emails, **do not build the paid pack.** The distribution channel is not
working, and building inventory will not fix a distribution problem. Change the niche
or change the case.

## 8. What breaks as it grows

- **Support volume.** At 200 customers, questions arrive daily. Answer them — but write
  the answer into the docs the same day, permanently. Support that does not reduce
  future support is a treadmill.
- **Framework churn.** React 19, a Next.js major, a Tailwind version bump — each one
  can break every component you sell. Budget one maintenance week per quarter and say
  so on the sales page. "Maintained through React 19" is a genuine differentiator.
- **Refund abuse.** Digital goods with instant delivery attract it. A published 14-day
  policy plus honest previews keeps it under 3%. Never fight a chargeback for $49; it
  costs more than it recovers.
- **The second-pack trap.** Do not build pack two until pack one has sold 50 copies.
  More inventory is the most seductive way to avoid the distribution work.

## 9. Kill criteria — write these into the charter before starting

| Checkpoint | Condition | Action |
|---|---|---|
| Day 14 | < 100 free downloads AND < 30 emails | Change niche or abandon C1 |
| Day 45 | < 5 paid sales | Stop building. Spend 100% of time on distribution for 30 days |
| Day 90 | < $400 cumulative revenue | Kill. Move the audience you built to C10 |
| Month 6 | < $1,500/mo | Not a failure — but it is a side asset, not a business. Tell the operator plainly |

## 10. Human action queue for C1

**Blocking (revenue cannot happen without these):**
1. Create or confirm the Gumroad / Lemon Squeezy / Stripe account (their KYC).
2. Confirm the tax handling approach — merchant of record is strongly preferred.
3. Approve the refund policy text.

**High-leverage (this is where their help compounds):**
4. Grant use of their X and GitHub identity for publishing, with an approval loop.
5. Name every dev community where they have standing.
6. Make any warm introduction to a newsletter or repo maintainer.

**Deferred until $2k/month:** entity formation, business bank account, trademark.

## 11. Sella / agentcash wiring

**Sell side.** `service_create` with `prices: [{kind: "one_off", amount_usdc: 49}]` maps
exactly to a pack sale, and `storefront_set` gives you a live sales page before the
operator has bought a domain — useful in week one. Note the constraint: an `offering`
block carries only a `service_id`, and price and copy are read from the listing, so you
cannot advertise one number and charge another. That is a feature; it enforces G3.

For a mainstream developer audience, **also list on Gumroad or Lemon Squeezy.** Most
developers will not pay in USDC. Treat Sella as an additional rail, not the only one.

**Buy side.** Modest. `search_catalog` for design assets or icon sets; agentcash
`stablestudio` for demo imagery and social clips. C1 has almost no legitimate need to
spend, so the caps are the tightest in the framework after C9:

```
seed_usdc              100
max_per_call_usdc        5
approval_threshold_usdc 20
daily_spend_cap_usdc    25
```

## 12. Worked examples

### Example A — the build-in-public post that actually converts

Wrong (generic, no specificity, asks for nothing):

> Just released my new React component library! Check it out, link in bio 🚀

Right (specific problem, visible proof, one ask):

> Spent 3 days on a React table that pins columns AND virtualizes rows without the
> pinned ones drifting on scroll.
>
> Every library I tried broke at one of those two. This one doesn't.
>
> [20-second screen recording: 50,000 rows, two pinned columns, smooth scroll]
>
> MIT, free, no signup: github.com/…

The second names a problem the reader has personally hit, proves the claim visually
instead of asserting it, and gives something away. The paid pack is never mentioned;
it is on the repo's README, where interested people will find it.

### Example B — the email that converts free users to paid

Sent 6 days after download, from the operator's real address.

> Subject: what broke for you?
>
> Hi — you grabbed the pinned-column table last week. Genuinely curious: did it work,
> or did it break on something?
>
> I ask because I'm building the next set based on what people actually hit, and so
> far the top three are inline editing, column resize persistence, and CSV export that
> handles nested data.
>
> If one of those is on your list, reply and I'll send it to you free when it's done.
>
> — [name]

This is a real question, not a pitch. It produces product direction, a reason to email
again with something valuable, and a genuine sense of obligation. **Reply rates on this
run far above a launch announcement**, and every reply is a customer interview you did
not have to schedule.

---

**Read next:** `20-systems/outreach.md` for channel mechanics ·
`10-resources/ref-website.md` for the landing page ·
`00-core/reasoning-guardrails.md` — G2 (sell before build) is under maximum tension in
this case, and the free-component-plus-waitlist path is the compliant resolution.
