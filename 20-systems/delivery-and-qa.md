# System — Delivery & QA

| | |
|---|---|
| **Status** | **REQUIRED READ** before the first delivery |
| **Prerequisite** | `00-core/delivery-model-selector.md`, your case study's §7–§8 |

---

## The asymmetry that governs everything here

**Delivery quality does not win you customers. It stops you losing them.**

Nobody refers you because a file arrived correctly. Everybody leaves when one does not.
Delivery is insurance, and the return on it is invisible right up until the moment it is
catastrophic.

Two consequences:

1. **Do not over-invest in polish** the customer did not ask for and will not notice.
2. **Do not under-invest in correctness.** In C9 one wrong number ends the relationship,
   and the client does not complain — they leave, and they tell people.

---

## The quality gate

**Every case in this framework needs one explicit gate before anything reaches a
customer.** Not a vibe — a named check with a pass/fail condition, run every time.

| Case | The gate | Pass condition |
|---|---|---|
| **C1** | Component works in a clean install | Fresh project, install, render, no console errors |
| **C2** | **Signed acceptance criteria** | Every AC verified by its stated method |
| **C3** | **Control total** | Matched + unmatched + disputed = source row count |
| **C4** | Fact check + source link on every claim | Every assertion traceable to a primary source |
| **C5** | Report figures match the platform | Numbers pulled fresh, not carried forward |
| **C6** | **Trigger verification** | Every row has a dated URL that was actually opened |
| **C7** | **Cross-document consistency** | No contradictions in dates, retention, role names |
| **C8** | Link health | Every listing resolves and is still open |
| **C9** | **Human review** | A named person signed off. **No exceptions, ever** |
| **C10** | Voice guide validation | No never-use vocabulary; no unexpressed opinions |

**The gate is not part of the delivery model — it is bolted on top of it** because some
failures are unrecoverable. See `delivery-model-selector.md` §"the three overrides."

---

## WIP limits

**Concurrency is the enemy of a small operation.** For a solo operator plus an agent, the
practical limit is **one to two client deliveries in flight.**

Beyond that: quality drops before throughput rises, and the operator's review gate becomes
a bottleneck that fails silently — they start skimming instead of reviewing, and nobody
notices until something wrong ships.

| Case | WIP limit | Bound by |
|---|---|---|
| C2 | **1 project** | Depth of attention |
| C3 | 2 jobs | QA gate |
| C5 | Unlimited clients, one monthly cycle | Sales throughput, not delivery |
| C6 | 3–4 batches | Research depth |
| C9 | **25–35 clients per reviewer** | The human review gate |
| C10 | 8–10 clients | Voice validation + approval loops |

**If you are exceeding the limit, the answer is not to work faster.** It is to stop
selling until capacity exists, or to raise prices so fewer clients produce the same
revenue.

---

## The delivery message

**The moment of delivery is the highest-leverage communication in the entire
relationship.** Goodwill peaks here and decays immediately. What you do with that window
determines renewal, referral, and expansion.

**The structure:**

```
1. The result, first          The number they care about. Not methodology
2. What you did               Specific, brief
3. What you could not resolve  Flagged, never guessed
4. Any correction             Volunteered before they find it
5. What you need from them     One thing, if any
6. The next step               The retainer, the next batch — with an honest reason
7. The referral ask            Here. Not later. Later never comes
```

**Sections 3 and 4 build more trust than section 1.** Flagging ambiguity instead of
guessing, and volunteering a correction before anyone noticed, are the two strongest
trust signals available to a small business — see C9's monthly report.

**Section 7 is the single highest-return habit in service businesses.** Ask at delivery,
when they are most pleased. A week later the feeling has faded and the ask feels
transactional.

---

## Scope discipline

**Iterate on the *how*, never on the *what*** without a change order.

| Freely negotiable | Needs a change order |
|---|---|
| Implementation detail | What is being delivered |
| Visual and interaction choices | The acceptance criteria |
| Order of work | The delivery date |
| Internal process | The price |

**The script, verbatim:**

> That's a good addition and I'd like to include it. It's outside the signed criteria, so
> it's a change order — about $1,400 and three days, which moves delivery to the 22nd.
> Want me to write it up?

**Never refuse. Always price.** Refusing makes you difficult; pricing makes you
professional and makes clients thoughtful about what they ask for.

---

## When you get it wrong

You will. What happens next decides whether the relationship survives.

1. **Tell them before they find it.** Always. A volunteered error is a process working; a
   discovered one is a trust failure.
2. **State what was wrong, what is right, and what changed** in the process. Once,
   plainly, without extended apology.
3. **Fix it at your cost**, without negotiation.
4. **Never silently correct a prior delivery.** C9's volunteered July correction is the
   model — restate, explain, and flag it so the trend line makes sense.
5. **Log it** in `DECISION-LOG.md`, with the process change.

**Do not over-apologize.** One clear acknowledgment plus a fix reads as competence.
Three paragraphs of contrition reads as instability and makes the client wonder what else
is wrong.

---

## Documentation and repeatability

**Every delivery should make the next one cheaper.** That is the compounding asset in an
operations business (G11).

- **A runbook per case** — the actual steps, updated when they change
  (`templates/RUNBOOK.md`)
- **A client profile** — their format quirks, their preferences, their voice guide
- **Answer support questions into the docs the same day.** Support that does not reduce
  future support is a treadmill
- **Log estimate versus actual** on every project. Most people need a 1.4–1.8× multiplier
  on their instinct, and you cannot know yours without the data

---

## Ten-case reference

| Case | Cycle | The failure that actually happens |
|---|---|---|
| **C1** | Per pack | Framework version breaks every component at once. Budget a maintenance week per quarter |
| **C2** | Per project, V-model | Scope creep via six small reasonable additions |
| **C3** | Per job | **Margin drift** — new vertical, unfamiliar hit rate, quoted before sampling |
| **C4** | Daily, fixed | Missing a day. Cadence *is* the product |
| **C5** | Monthly | Reporting lagging indicators only, so the client sees nothing happening |
| **C6** | Monthly batch | **Quality regression to the mean** by month four. Client says "not as specific as it was" |
| **C7** | Per pack, V-model | **Internal inconsistency** across documents. An auditor finds it in ten minutes |
| **C8** | Weekly issue | **Decay.** Dead listings destroy candidate trust faster than good ones build it |
| **C9** | Monthly + mid-month chase | **One wrong number.** Binary trust loss |
| **C10** | Weekly batch | **Generic voice.** They will not tell you; they will say "bringing it in-house" |

**Six of ten failure modes are gradual, not acute** — margin drift, quality regression,
decay, voice drift. Those are the ones a gate catches and vigilance does not, because they
never announce themselves on any single delivery.

---

## Two worked examples

### Example A — the gate catching something before it shipped

**The situation.** C7. Compliance pack for a 45-person company, ready to deliver.

> Cross-document consistency check before delivery — found three contradictions. Holding
> the pack.
>
> 1. **Data retention.** Retention Policy §2 says financial records 7 years. The Privacy
>    Notice says "up to 5 years." The questionnaire answer bank says 7. Two of three
>    agree, but the Privacy Notice is the one their customers actually read.
> 2. **Incident notification.** IR Plan §5.1 says notify affected parties within 72
>    hours. The DPA template says "without undue delay and in any event within 48 hours."
>    We have committed them to a stricter deadline in one document than another — which
>    is worse than either alone.
> 3. **Role naming.** "Security Officer" in four documents, "Information Security Lead"
>    in two. Same person, and an auditor will ask whether these are two roles.
>
> **Why this matters more than it looks:** the most common real defect in a compliance
> pack is not a missing document, it is internal contradiction. An auditor finds it in
> ten minutes and the client's credibility is gone in the room — and they will
> reasonably blame us.
>
> **Fixing all three**, then re-running the check. Half a day.
>
> **Process change:** the consistency check currently runs at the end. Moving it to run
> after each document is drafted as well, so contradictions surface while the reasoning is
> fresh rather than at the gate.
>
> Delivery moves from Thursday to Friday. Telling the client today rather than letting a
> date slip silently.

### Example B — the delivery message that generates the next two sales

C3, pilot complete.

> **Subject: 5,000 records back — plus two things I found**
>
> Hi Sarah,
>
> Attached, done.
>
> - **1,847 duplicate records merged** (match rule documented on tab 2, so you can audit
>   it)
> - **2,203 dead email addresses flagged** — 44%, which is high but normal for a database
>   this age
> - **Industry populated on 4,721 of 5,000**, up from 2,950
> - **312 companies acquired or renamed** since their record was created
>
> **Control check:** matched + unmatched + flagged = 5,000. Balanced.
>
> **Two things worth flagging:**
>
> 1. **That 312 is the number I'd watch.** Those records are actively misrouting your
>    outbound right now — that is not a data-hygiene issue, it is a pipeline issue.
> 2. **One I couldn't resolve:** 47 records have two plausible parent companies after a
>    merger. I've listed them on tab 4 rather than picking one. Someone who knows the
>    accounts should decide.
>
> **What I'd suggest next, honestly:** a cleaned database degrades about 2–3% a month
> through normal staff churn, so in a year you're roughly back where you started. Ongoing
> hygiene is $1,400/month — but I'd rather you decide that in three months once you've
> seen whether this pass actually changed anything for the team.
>
> **One ask:** if this was useful, is there anyone in your network with the same problem?
>
> — [name]

Why this works: measured results first with the control check proving the arithmetic
closes; a finding they did not know about and did not ask for; **47 records flagged rather
than guessed**, which is the trust move; the retainer presented *with a reason to defer
it*, which builds far more credibility than pressure; and the referral ask at the exact
moment goodwill peaks.

---

**Read next:** `20-systems/support-and-retention.md` ·
`00-core/delivery-model-selector.md` · `templates/RUNBOOK.md` ·
`50-guardrails/security-and-secrets.md` §3 (client data retention)
