# C8 — Niche Job Board + Hiring Newsletter

| | |
|---|---|
| **Tier** | 2 (slow to money; needs a transactional billing rail) |
| **Time to first dollar** | 6–12 weeks |
| **Gross margin** | ~95% |
| **Agent autonomy** | High |
| **Distribution difficulty** | **10 of 10 — hardest in the framework** |
| **Killer risk** | Two-sided cold start, then listing decay |

---

## 1. Why this case is in the registry

C8 teaches the **two-sided cold start**, which is the most common way an otherwise
sensible business plan fails. Even if you never run C8, read this file before building
anything with two distinct user groups. The reasoning transfers to marketplaces,
directories, communities, and any product where one group's value depends on another
group's presence.

**The trap:** a job board is worthless to employers with no candidates, and worthless
to candidates with no jobs. The instinctive plan is to build both simultaneously. That
plan fails, because you end up with a half-empty board that convinces neither side, and
both sides leave and do not come back.

## 2. The business

A job board for **one specific role in one specific industry** — not "tech jobs," but
"clinical data managers in pharma," "RevOps roles at Series A–C SaaS," "restaurant GMs
in the Southeast." Plus a weekly email that is the actual product.

Employers pay $299 per post or sponsor the newsletter. Candidates never pay.

## 3. The correct sequencing — this is the whole case

**Own the candidate side first. Always. Without exception.**

Candidates are free to acquire and their attention is what employers buy. The sequence:

**Phase 1 (weeks 1–8): build a candidate audience with zero paid listings.**
The weekly email must be valuable when it contains no paid jobs at all. Fill it with:
- Salary data you compile from public postings — genuinely scarce and highly shared
- Analysis of who is hiring and who is quietly not
- Aggregated public postings (**respecting each source's terms** — see §5)
- Career-relevant analysis specific to that role: what skills are appearing in
  postings, which tools are showing up, which are disappearing

**Phase 2 (weeks 8–14): prove the audience, then sell to employers.**
When the list is real — 800–1,500 engaged subscribers in a narrow role — employers will
pay to reach it. Not before.

**Phase 3: the board follows the newsletter, not the reverse.**
The board is an archive and an SEO asset. The newsletter is the product.

**The rule that matters most: do not sell a job post until you can state a real
subscriber number.** Inflating it violates G3, and it is self-punishing — the first
employer who pays $299 and gets zero applicants will say so publicly in a small
industry where everyone knows everyone. In a niche job board, one bad employer
experience is a meaningful fraction of your addressable market.

## 4. Operator fit

**Pick C8 if:** the operator has standing in a specific professional niche, can fund a
quiet quarter, and ideally has recruiting or hiring experience in that field.

**Do not pick C8 if:** revenue is needed inside 90 days, or the niche is not genuinely
narrow. "Tech jobs" competes with LinkedIn and you will lose. "Clinical data managers"
does not compete with anything, and that is the entire opportunity.

**The niche test:** could you name 200 companies that hire this exact role, and would a
person in that role recognize the publication as *for them* within five seconds? If
either answer is no, narrow further.

## 5. Lean-start profile and the legal boundary

| Item | Requirement |
|---|---|
| Capital to start | **$0–50/mo** |
| Entity needed | Not initially |
| New KYC | **Required** — you are taking payments from employers |
| Licensing | None |
| Liability ceiling | Low |
| Physical | None |

**The aggregation boundary.** Republishing job postings sits in genuinely mixed legal
territory and the honest position is: it depends on the source and the method.

- **Respect `robots.txt` and each site's terms.** Many job boards explicitly prohibit
  scraping their listings.
- **Prefer official feeds.** Many companies publish an XML/JSON careers feed
  specifically for aggregators. Greenhouse, Lever, Ashby and similar ATSs expose public
  APIs. Use them.
- **Link, do not copy.** Post the title, company, location, and a short excerpt with a
  link to the original. Wholesale reproduction of the full description is a copyright
  question you do not want.
- **Attribute the source.**
- **Remove filled listings promptly** — see decay in §9.

The safe path is not hard: official ATS feeds plus link-and-excerpt covers most of what
you need, and it is defensible.

## 6. Distribution

Hardest in the framework. Candidate-side growth, in order of what actually works:

**1. The salary data.** Compile compensation ranges from public postings in the niche
and publish quarterly. This is the single most shared artifact in any professional
community and it will do more for growth than everything else combined. It is also
genuinely useful, which is why it works.

**2. Being present where the role gathers.** Every profession has its places — a
subreddit, a Slack, a LinkedIn group, a conference, a certification body's forum. Be a
useful participant for weeks before mentioning the publication.

**3. The "who's hiring" post.** Monthly, in the community, free, with no gate. It is
useful on its own and it introduces the newsletter naturally.

**4. SEO on "[role] jobs" and "[role] salary."** Slow, compounding, and it eventually
becomes the largest channel. Start in week two.

**5. Recruiter relationships.** Recruiters in the niche want candidate reach. They will
promote you to candidates in exchange for visibility. This is an underused channel.

### Employer-side, only after Phase 1

Direct outreach to companies already posting the role publicly. The pitch is
straightforward once the audience is real: "1,400 clinical data managers read this
weekly. Your posting has been on LinkedIn for 40 days."

### Ask your human for this

- **"What niche do you actually know, and are you known in it?"** C8 without niche
  credibility is very hard.
- **"Which communities are you in?"** These are your first 200 subscribers.
- **"Do you know any recruiters in the field?"** Both a distribution channel and a
  future customer.
- **"Set up the email platform and payment processing."** Blocking.
- **"Will you be publicly named as the editor?"** Anonymous job boards read as scrapers.

## 7. Offer and pricing ladder

| Offer | Price | When |
|---|---|---|
| Candidate access | Free, forever | Always |
| Single post | $249–399 | Phase 2 |
| 3-post pack | $600–900 | Phase 2 |
| Newsletter sponsorship | $800–2,000/issue | Phase 2, at 1,000+ subscribers |
| Featured / pinned listing | +$150 | Phase 2 |
| Recruiter subscription | $300–600/mo | Phase 3 — unlimited posts |

**Do not charge candidates for anything.** Resume reviews, "premium" access, early
listings — all of it damages the audience you are actually selling. The candidate side
is inventory, and you do not charge your inventory.

## 8. Unit economics, worked

At 1,400 subscribers, month 5:

```
Revenue
  6 job posts × $299                            $1,794
  2 sponsorships × $900                         $1,800
  Total                                         $3,594/mo

COGS
  Email platform                                   -$49
  Hosting (static board)                            -$0
  ATS feed polling / research compute              -$35
  Total                                            -$84

Gross profit                                    $3,510/mo   (97.7%)
```

Superb — **and it arrives in month five.** The honest path:

```
Month 1     0 →   200 subscribers      $0
Month 2   200 →   500                  $0
Month 3   500 →   850                  $0    (maybe a first $299 post)
Month 4   850 → 1,150                  ~$600
Month 5 1,150 → 1,400                  ~$3,600
```

**Four months of near-zero revenue.** Your operator must agree to this in writing
before week one. C8 has the widest gap in the framework between eventual economics and
early experience, and that gap is where operators quit.

## 9. What breaks as it grows

- **Decay — the specific killer of job boards.** Filled and expired listings destroy
  candidate trust faster than good listings build it. A candidate who applies to three
  dead roles never opens the email again. **Automatic expiry at 30 days is mandatory**,
  plus a link-health check before every send. This is not optional maintenance; it is
  the product's integrity.
- **The empty-board problem in month one.** Do not launch a board with four listings.
  Launch the *newsletter* with analysis and aggregated postings; add the board when
  there is enough to fill it.
- **Employer churn from bad outcomes.** If a $299 post gets two applicants, that
  employer is gone and they will mention it. Manage expectations explicitly: state your
  subscriber count and typical applicant range honestly, and refund without argument
  when it underperforms badly. In a small niche, reputation is the entire asset.
- **Niche too small.** Some niches genuinely cannot support this — if only 40 companies
  hire the role and each hires once a year, the ceiling is real. Estimate the annual
  hiring volume of the niche *before* starting.

## 10. Kill criteria

| Checkpoint | Condition | Action |
|---|---|---|
| Day 30 | < 150 subscribers | Niche too narrow, or the distribution channel is wrong |
| Day 60 | < 400 subscribers, or open rate < 35% | Diagnose growth vs. content separately |
| Day 90 | < 800 subscribers | Kill or re-niche once |
| Day 120 | 1,000+ subscribers but zero employer interest | The niche does not have a hiring budget problem. Reconsider the buyer |
| Any time | Open rate below 25% for 3 weeks | Fix the product before growing the list |
| Any time | Employer reports fewer than 3 applicants | Refund, and re-examine whether the audience is genuinely engaged |

## 11. Human action queue for C8

**Blocking:**
1. Email platform account.
2. Payment processing for employer posts.
3. Physical address for email compliance.
4. Consent to be publicly named as editor.

**High-leverage:**
5. Niche credibility and community memberships.
6. Recruiter relationships.
7. Personal outreach to the first 50 subscribers.

## 12. Sella / agentcash wiring

**Sell side: genuinely good fit for the job-post transaction.** A single job post is a
discrete purchase — `service_create` with `prices: [{kind: "one_off", amount_usdc:
299}]` — and unlike C4's subscriptions, this needs no recurring authority. Sponsorships
are also `one_off`. `storefront_set` works as an employer-facing media kit.

The caveat: many employers pay by corporate card through procurement. Offer a
conventional processor alongside. **The recruiter subscription cannot be charged on this
rail** — sell it as a prepaid quarter instead.

**Buy side.** agentcash `stableenrich` for company research and job-posting discovery;
`stablesocial` for community distribution research.

```
seed_usdc              100
max_per_call_usdc        6
approval_threshold_usdc 20
daily_spend_cap_usdc    25
```

## 13. Worked examples

### Example A — the phase-1 newsletter with zero paid listings

The issue that has to be valuable before you have anything to sell.

> **Clinical Data Manager Weekly — Issue 7**
>
> **Salary data update.** I tracked 61 CDM postings with disclosed ranges over the last
> 90 days. Median base for Senior CDM in the US is $128k, up from $121k in the previous
> quarter's sample. The rise is concentrated in postings that mention decentralized
> trials — those pay a median $9k above equivalent roles that do not.
> [full data, methodology, and n for each cut]
>
> **What's appearing in postings.** "Medidata Rave" appeared in 38 of 61. "Veeva CDB"
> appeared in 14 — up from 4 a year ago. If you have not touched Veeva, that trend is
> now worth a weekend.
>
> **Who's hiring** (public postings, linked to source):
> - Parexel — 3 CDM roles, Remote US
> - IQVIA — Senior CDM, Durham NC
> - Medpace — CDM II, Cincinnati
> …[12 more, each linked to the original posting]
>
> **One thing worth reading:** [link + two sentences on why it matters]

There are no paid listings and no advertisers, and it is still worth a subscriber's
time — because the salary analysis and the tooling trend are genuinely scarce. **Note
the methodology disclosure and the sample size.** Publishing a salary median without
stating n and the collection window is the kind of soft fabrication G3 exists to
prevent; stating it also makes the data more credible, not less.

### Example B — the employer pitch, sent only once the audience is real

> Subject: your CDM role has been open 40 days
>
> Hi Rachel,
>
> Your Senior Clinical Data Manager posting went up on LinkedIn on 24 July — 41 days.
> For that role, that usually means it is not reaching the right people rather than
> that the right people said no.
>
> I publish Clinical Data Manager Weekly: 1,412 subscribers, 58% open rate over the
> last 30 days, roughly 70% currently in CDM or Senior CDM roles at CROs and sponsors.
>
> A post is $299 and goes into Thursday's issue plus the board. Typical range is 8–20
> applicants, though I'll be straight with you that it varies a lot by location and
> whether the range is disclosed — posts with a disclosed salary do roughly twice as
> well.
>
> If it gets fewer than 3 applicants I'll refund it, no discussion.
>
> — [name]

Why it works: a specific observed fact about *their* situation, measured audience
numbers with a stated window and composition, an honest range rather than a promise, a
genuinely useful piece of advice (disclose the salary) that costs them nothing and
improves their outcome, and a refund guarantee that makes $299 a trivial decision. The
guarantee is affordable precisely because you only send this once the audience is real.

---

**Read next:** `00-core/reasoning-guardrails.md` — G2 (evidence before build) and G3
(no inflated audience metrics) are both under maximum tension here ·
`case-studies/C4-vertical-news-brief.md`, which shares the audience-first structure ·
`20-systems/content-and-writing.md`.
