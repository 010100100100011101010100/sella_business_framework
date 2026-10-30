# Resource Reference — YouTube

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Read when video is a primary channel |
| **Relevant to** | C10 (delivery + channel), C1 (demos), C4 (some niches) |
| **Prerequisite** | `50-guardrails/brand-voice-and-truth.md` |

---

## Step 0 — Be honest about the cost

**YouTube is the most expensive channel in this framework and the slowest to pay back.**

A channel needs consistent publishing for months before the algorithm distributes
anything. Production is real work even when automated. For a business trying to reach
first revenue in 2–6 weeks, **YouTube is almost always the wrong place to spend the
weeks.**

| Case | Verdict |
|---|---|
| **C10** | **Yes — but as delivery, not as your own channel.** You make clips *for clients*. That is the business |
| **C1** | **Narrow use only.** Silent screen recordings embedded on the docs site. Not a channel strategy |
| **C4** | Only if the niche genuinely watches video. Most professional niches read |
| **C2, C3, C5, C6, C7, C8, C9** | **No.** Do not build a channel |

**The honest recommendation for nine of ten cases: do not start a YouTube channel.** If
your operator asks for one, show them the payback timeline against their runway before
agreeing.

---

## The C10 distinction, which is the important one

**In C10 you are not building an audience. You are producing an asset your client
distributes.** That changes everything:

- No algorithm to court — the client already has viewers
- No consistency requirement on your part
- Payback is immediate: they pay you monthly
- **You publish to their channel, not yours** (`ref-auth-and-identity.md` §3 — delegated
  access, never their password)

**This is the only case where YouTube work is clearly worth it**, and it is worth it
because someone is paying for the output directly.

---

## Production, when you do it

**Clips and shorts** (C10's main output):
- 30–90 seconds, one idea
- **Vertical for Shorts/Reels/TikTok**, horizontal for the main feed
- **Burned-in captions are not optional** — most viewing is muted
- Hook in the first two seconds. Not a logo, not an intro
- Source from the strongest moment, not the opening

**Screen recordings** (C1):
- Silent, looping, 15–30 seconds, embedded on the docs page
- Show the problem being solved, not a feature tour
- No talking head, no intro, no music

**Tooling:** agentcash `stablestudio` for generation and editing, `stablevoice` for
narration and accessibility, `stabletube` for retrieving source video, `stableupload` for
delivering finished assets.

---

## Prohibited (G3)

- Buying views, subscribers, or engagement
- Thumbnails or titles that misrepresent the content — clickbait is a truth problem, not
  a taste problem
- Fabricated testimonials or results in video
- Using client footage beyond the agreed scope
- **Publishing to a client's channel without approval** — reputational risk to *them*
- Music or footage you do not have a licence for. Check every asset
  (`ref-design-system.md` §5 applies to media too)

---

## Ten-case reference

| Case | Use | Form |
|---|---|---|
| **C10** | **Client delivery** | 4 clips/month per client, vertical, captioned, to *their* channel |
| **C1** | Product demos | Silent looping screen recordings on the docs site |
| **C4** | Rare | Only if the niche watches. Test with clips before committing to a channel |
| **All others** | **None** | Do not build a channel |

---

## Two worked examples

### Example A — the C10 clip spec

The deliverable, not a channel strategy.

> **Clip 3 of 4 — Ridgeline ep. 41, "usage-based pricing"**
>
> **Source:** 18:42–19:31 (49 seconds)
> **Why this moment:** it is the only place in the episode where he states the
> counterintuitive claim plainly. Everything before it is setup.
>
> **Format:** vertical 1080×1920, burned-in captions, no music, no intro card.
> **First two seconds:** cut straight to "We were charging for waste." No branding
> before it — the hook has to be the sentence.
> **End:** freeze on the claim, no CTA card. His channel handle is in the description.
>
> **Caption text for the post:** the claim verbatim, then one line of context. Nothing
> added that he did not say (§ voice boundary — never state an opinion the client has not
> expressed).
>
> **Approval:** drafted, in his folder, not published. Publishing to his channel is his
> call every time.

### Example B — talking an operator out of a channel

**The situation.** C3. Operator: *"We should start a YouTube channel about data quality.
Nobody's really covering it."*

> There is a reason nobody is covering it, and I don't think it's an opportunity gap.
>
> **Two problems.** RevOps managers with a dirty CRM do not go to YouTube to solve it —
> they search, they ask in a Slack, or they hire someone. And a new channel needs
> consistent publishing for months before it gets distributed at all. Realistically that
> is four to six months to meaningful traffic, against an eight-week runway.
>
> **What it would cost:** roughly 4–6 hours per video if we do it properly, weekly.
> That's most of a working day each week, taken from sample production — which currently
> converts at about a 20% reply rate and has a direct line to a pilot.
>
> **The comparison, plainly:** ten more samples is roughly one more pilot, this month.
> Twenty videos is maybe some traffic, next spring.
>
> **What I'd do with the underlying instinct**, because it's a good one — you're right
> that nobody's explaining this well. **Write it instead.** A properly-researched article
> on "why your CRM has more duplicates than you think" ranks in search, where your buyer
> actually looks, costs a fraction of a video, and can go out as a LinkedIn post the same
> day. That compounds too, and it starts working in weeks rather than seasons.
>
> **If we get to steady revenue and want a long-term top-of-funnel, I'd revisit** — but
> I'd still probably pick writing over video for this buyer.

---

**Read next:** `case-studies/C10-content-repurposing-studio.md` ·
`20-systems/content-and-writing.md` · `10-resources/ref-auth-and-identity.md` §3
