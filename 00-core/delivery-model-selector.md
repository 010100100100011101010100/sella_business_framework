# Delivery Model Selector

| | |
|---|---|
| **Status** | **REQUIRED READ** before the first paid engagement. Governs how the business is run |
| **Blocking for** | C2 and C7 (contract shape forces the answer) · every case at layer 2 |
| **Prerequisite** | `00-core/reasoning-guardrails.md`, your chosen case study |
| **Output** | The **Delivery Model** section of `BUSINESS-CHARTER.md`, with the reasoning |

---

## The frame: methodology is risk allocation, not workflow preference

Arguments about waterfall versus agile are almost always proxy arguments about
**who bears the cost when things change.** Once you see that, the choice stops being
a matter of taste and becomes arithmetic.

| Model | Who bears change risk | What it costs the other side |
|---|---|---|
| **Fixed scope + change orders** | The client pays for each change | They must know what they want up front |
| **Iterative, time-and-materials** | The client bears outcome uncertainty | They cannot know the final price |
| **Fixed price + open scope** | **You bear everything** | Nothing. This is why it kills agencies |

The third row is not a methodology. It is an unbounded liability wearing a methodology's
clothes, and it is the most common way a competent agency delivers excellent work and
loses money doing it.

**So: pick the model that puts change risk where the contract already put it.** If you
have taken a fixed price, the scope must be fixed too, and changes must have a price.
If the scope is genuinely unknowable, the price cannot be fixed.

---

## The two layers — this is the file's central point

**Most methodology confusion comes from applying one layer's answer to the other.**

### Layer 1 — Business discovery
*What do we sell, to whom, at what price, through which channel?*

**Always iterative. Always empirical. Never planned.**

There is no version of this framework where you plan your way to a working business.
Demand uncertainty is total at the start, the cost of a wrong hypothesis is a week,
and the only reliable information comes from a stranger's response to a real offer.
This is what guardrails G1 (evidence ladder), G2 (sell before build), and G7 (kill
criteria) encode — they are a research methodology in disguise.

**The layer-1 failure mode for an agent is severe and specific: writing the plan instead
of running the experiment.** A 40-page business plan, a full competitor analysis, a
complete brand system, a finished website — before a single stranger has been asked to
pay for anything. It feels like diligence. It is waterfall applied to a domain where the
requirements cannot be known in advance, and it is how six weeks disappear.

### Layer 2 — Engagement delivery
*How do we execute this specific piece of paid work?*

**This varies, and it is determined by the contract shape and the cost of being wrong.**
The rest of this file is about layer 2.

**The two layers can and often should differ.** C2 is the clearest example: layer 1 is
relentlessly iterative — test outreach angles, adjust the offer, learn from every
scoping call — while layer 2 is a disciplined V-model, because the client signed a fixed
price against a fixed scope. Running the same model at both layers is usually wrong at
one of them.

---

## The four determining variables

Score the **engagement**, not the business, on each:

**1. Scope fixity** — *Is the scope contractually fixed against a price?*
The single most decisive variable. Fixed price with fixed scope forces staged delivery
with a change mechanism. If you cannot answer this, you do not have a contract yet.

**2. External traceability** — *Will someone outside audit the link between a stated
requirement and a delivered artifact?*
An auditor, a regulator, an enterprise security review, a client's counsel. If yes, the
verification side must be built in, not added afterwards.

**3. Cost of being wrong** — *If this is wrong, what does it cost to correct?*
A blog post: nothing. A reconciliation report with a wrong number: the client. A
compliance pack relied on in an audit: your operator.

**4. Requirement uncertainty** — *Do we actually know what is needed?*
High uncertainty makes fixed scope dishonest. Low uncertainty makes iteration wasteful
ceremony.

---

## The models that are actually useful here

Five, plus one honest exclusion.

### A. Iterative / incremental
**Small increments, feedback each cycle, direction adjusted.**
Use when requirement uncertainty is high and change is cheap. **Always the right answer
at layer 1.** At layer 2, correct where the client is buying an outcome rather than a
specification.

### B. Cadence-locked flow (kanban)
**A queue, a work-in-progress limit, a fixed delivery rhythm.**

**This is the dominant layer-2 model in this framework — six of the ten cases — and it
is routinely mislabelled "agile."** It is not. There are no sprints, no story points,
no planning ceremony. There is a queue of similar units of work (a cleaning job, a
month of a retainer, a batch of leads, a week of repurposing), a limit on how many are
in flight, and a delivery date that does not move.

**The WIP limit is the whole discipline.** For a solo operator plus an agent, the
practical limit is **one to two client deliveries in flight**. Beyond that, quality
drops before throughput rises, and the operator's review gate becomes the bottleneck
that fails silently.

This is guardrail G10 (one business at a time) applied one level down: concurrency is
the enemy of a small operation, and the instinct to take one more thing is the thing to
resist.

### C. Staged delivery (waterfall)
**Sequential phases, each completed before the next, scope fixed at the start.**
Use when scope is genuinely fixed, uncertainty is low, and change has a price. Waterfall
has a bad reputation earned in contexts it did not fit — large systems with unknowable
requirements. **A four-week internal tool with signed acceptance criteria is exactly the
context it does fit.**

Non-negotiable companion: **a written change-order mechanism.** Waterfall without one is
the unbounded-liability row from the table above.

### D. V-model
**Waterfall, plus every requirement paired with the test that verifies it, written
before implementation.**

```
Requirements  ──────────────────────►  Acceptance testing
  (signed before any build)              (against the signed list)
    │                                          ▲
    ▼                                          │
  Design       ──────────────────────►  Integration testing
    │                                          ▲
    ▼                                          │
  Build        ──────────────────────►  Unit testing
```

Use when **external traceability** is required (variable 2). The left side descends
before implementation; the right side ascends against artifacts written on the left.
"Done" is not an opinion — it is the signed list, satisfied.

**Correct in exactly two cases here:** C2 (fixed bid — "is this in scope?" must have a
documented answer, not a social negotiation) and C7 (an auditor will ask which control
each clause satisfies, and the answer must be a trace).

**Do not use it anywhere else.** V-model where nobody audits anything is paperwork
performed for its own sake, and it will slow you down for no return.

### E. Phase-gated / risk-driven
**Sequence the work so the largest risk is retired first, with a go/no-go gate.**

Rare, but genuinely correct for **C8**, whose two-sided cold start is a sequencing
problem before it is a delivery problem. Phase 1 builds the candidate audience with zero
paid listings; the gate is a real subscriber number; only then does Phase 2 sell to
employers. The methodology *is* the phase order, and getting it wrong — building both
sides at once — is the documented way that business fails.

### The exclusion: Scrum ceremony
**Sprints, standups, story points, retrospectives, velocity.**

**Do not adopt these.** Scrum's machinery exists to coordinate a team of people who
cannot see each other's work. In a one-person-plus-agent operation there is no
coordination problem to solve, so the ceremony is pure overhead — and worse, it produces
a convincing simulation of progress. A standup with yourself is not a control.

**What you need instead is a cadence, not a ceremony.** A weekly review that asks four
questions and a monthly close. See `00-core/operating-cadence.md`. Methodology without
rhythm is decoration; rhythm without ceremony is the goal.

---

## The selection procedure

### The decision tree — most engagements resolve in two questions

```
Is the scope contractually fixed against a price?
│
├─ YES ──► Will anyone external audit requirement-to-artifact traceability?
│          ├─ YES ──► D. V-MODEL                     (C2, C7)
│          └─ NO  ──► C. STAGED DELIVERY + change orders
│
└─ NO  ──► Is this a repeating unit of similar work?
           ├─ YES ──► B. CADENCE-LOCKED FLOW         (C1, C3, C5, C6, C9, C10)
           └─ NO  ──► Is one risk large enough that everything else waits on it?
                      ├─ YES ──► E. PHASE-GATED       (C8)
                      └─ NO  ──► A. ITERATIVE          (layer 1, always)
```

### Then apply the three overrides

1. **High cost of being wrong → add a hard quality gate**, whatever the model. C9 gets a
   mandatory human review before every delivery; C3 gets a QA gate before every job
   ships. The gate is not part of the methodology — it is bolted on top of it because
   the failure is unrecoverable.
2. **Fixed price with no change-order mechanism → stop.** Do not start work. Add the
   mechanism to the contract first (`50-guardrails/legal-and-compliance.md` §6).
3. **A publication with a promised frequency → cadence beats everything.** C4's daily
   brief is not iterative or staged; it is a drumbeat. The date is the requirement, and
   scope flexes to meet it. Never the reverse.

### Record it

The Delivery Model section of `BUSINESS-CHARTER.md` must state: the model, the layer-1
model if it differs, the variable that decided it, the WIP limit if flow-based, the
quality gate if any, and the change mechanism if scope is fixed.

---

## Iterate *within* the scope, not *on* the scope

The most useful single distinction in this file, and the one that lets you take fixed-bid
work without dying of scope creep.

| Iterate on this — freely, weekly | Never on this — without a change order |
|---|---|
| How something is implemented | What is being delivered |
| Which library, which pattern | Which features exist |
| Visual and interaction detail | The acceptance criteria |
| The order work is done in | The delivery date |
| Internal tooling and process | The price |

You can and should show working software weekly, take feedback, and adjust the *how*.
**The *what* is fixed at signature.** This is what makes a fixed bid survivable while
still feeling collaborative to the client — and clients experience it as responsive,
not rigid, because everything they can see is negotiable.

**The change-order script, verbatim:**

> That's a good addition and I'd like to include it. It's outside the signed acceptance
> criteria, so it's a change order — about $1,400 and three days, and it moves delivery
> to the 22nd. Want me to write it up?

**Never refuse. Always price.** Refusing makes you difficult; pricing makes you
professional, converts a margin leak into revenue, and makes clients dramatically more
thoughtful about what they ask for.

---

## Anti-patterns

| Anti-pattern | What happens | The case that shows it |
|---|---|---|
| **Agile inside a fixed bid with no change mechanism** | Six "small" additions, 75% duration overrun, margin from 65% to 25% | C2 §6 |
| **Waterfall at layer 1** | Six weeks of planning, zero customer contact, no evidence above rung 2 | Any |
| **Scrum ceremony solo** | Overhead plus a convincing simulation of progress | Any |
| **V-model where nobody audits** | Traceability paperwork with no reader | Any except C2, C7 |
| **Building both sides of a marketplace at once** | Half-empty on both sides, both leave | C8 §3 |
| **Exceeding the WIP limit** | Quality drops before throughput rises; the review gate fails silently | C3, C9, C10 |
| **Moving a publication's date** | Readers learn not to depend on it, which was the entire value | C4 §8 |
| **Changing model mid-engagement** | Reads to the client as chaos, whatever the reason | C2 |
| **"We'll figure scope out as we go" at a fixed price** | Unbounded liability | C2 |

---

## Ten-case reference

Layer 1 is iterative for all ten. The differences are all at layer 2.

| Case | Layer 2 model | Deciding variable | Gate / WIP |
|---|---|---|---|
| **C1** | Cadence-locked flow — one pack at a time | Repeating units; change is cheap | **Gate: do not build pack 2 until pack 1 sells 50** |
| **C2** | **V-model** | Fixed price **+** documented acceptance | Change orders mandatory. WIP: **1 project** |
| **C3** | Cadence-locked flow | Repeating jobs | **QA gate: control total must balance.** WIP: 2 jobs |
| **C4** | **Drumbeat** — date fixed, scope flexes | Promised frequency is the product | Publish every weekday. Never move the date |
| **C5** | Monthly cycle across a client book | Repeating monthly units | Monthly report is the gate. WIP: unlimited clients, one cycle |
| **C6** | Monthly batch flow | Repeating batches | **Gate: every row cites a dated, verifiable trigger** |
| **C7** | **V-model** | **External audit traceability** | Cross-document consistency check + human sign-off |
| **C8** | **Phase-gated** | One risk dominates: the cold start | **Gate: real subscriber number before selling a post** |
| **C9** | Monthly cycle | Repeating units, **unrecoverable error cost** | **Hard gate: human reviews every delivery.** WIP: 25–35 clients per reviewer |
| **C10** | Weekly batch flow | Repeating batches | **Gate: voice guide validation + client approval.** WIP: 8–10 clients |

**The finding worth noticing: six of ten are cadence-locked flow, not "agile."** The
naive answer for a small modern business is "we're agile," and for most of these cases
that is both wrong and unhelpful. What they actually run is a queue with a WIP limit and
a fixed rhythm. Naming it correctly changes what you optimize: not sprint velocity, but
**cycle time and WIP discipline.**

---

## Two worked examples

### Example A — C2, talking the operator out of "let's just be agile"

**The situation.** First fixed-bid project signed, $12,000, four weeks. The operator:
*"I don't want to be rigid with them. Let's just work agile, show them stuff weekly, and
adjust as we go. They'll be happier."*

> I want to do most of that, and I want to change one part of it — because the way you
> described it is how agencies lose money on projects they delivered well.
>
> **The part I agree with:** show them working software weekly, take their feedback,
> adjust the implementation. That absolutely should happen and it is what makes clients
> happy.
>
> **The part that has to be different:** we have taken a fixed price. That means we have
> already agreed to bear the cost of building a defined thing. If the definition can move
> freely, we have signed up for unlimited work at a fixed number, and that is not a
> methodology, it is an unbounded liability.
>
> **The distinction that solves it — iterate on the *how*, not the *what*:**
>
> They can change their mind about how the reconciliation report looks, how the filters
> behave, what order we build in, which library we use. Freely, weekly, no charge. That
> is where "adjusting as we go" lives, and it is most of what they will actually want.
>
> They cannot silently add "and it should also write back to Shopify" — that is a new
> requirement against a fixed price. Not refused: **priced.**
>
> **What I need from the paid discovery, which they are already paying for:**
>
> Signed acceptance criteria. Each requirement paired with how it will be verified, and
> an explicit out-of-scope list. That is the V-model, and here is why it is worth the
> two days it costs: in week five, when they ask for the Shopify write-back, "is this in
> scope?" has a documented answer instead of being a social negotiation you will lose
> because you want them to like you.
>
> **The script when it happens:**
>
> > "That's a good addition and I'd like to include it. It's outside the signed
> > criteria, so it's a change order — about $1,400 and three days, which moves delivery
> > to the 22nd. Want me to write it up?"
>
> Never refuse, always price. Clients respond well to this — it reads as professional,
> and it makes them think properly about what they are asking for.
>
> **The honest version of your instinct:** you want them to feel we are responsive.
> Weekly demos and free iteration on implementation do that. Open scope does not make
> clients happier — it makes projects late, which makes them unhappy in week six.

Why this is right: it agrees with the operator's actual goal (client happiness), isolates
the one structural thing that must change, gives the *how/what* distinction as a working
tool rather than a rule, and pre-loads the script for the moment it will be needed.
**It also names what the operator's instinct was really about — wanting to be liked —
without being condescending about it.**

### Example B — the layer confusion, caught before it costs six weeks

**The situation.** C3, day 4. The agent has written a competitor analysis, is drafting an
ICP document, and has started on a brand style guide. It runs the guardrail self-check.

> Stopping myself on something before it costs us three weeks.
>
> I've spent four days on a competitor analysis, an ICP document, and the start of a
> brand guide. None of that is wrong exactly, but I am running the wrong model at the
> wrong layer, and it is the specific failure this framework warns about.
>
> **What I'm doing:** treating business discovery as a planning problem. Gather
> requirements, analyse, document, then execute. That is waterfall, and it is the correct
> model for a fixed-scope build with known requirements.
>
> **What this actually is:** a domain where the requirements are unknowable in advance
> and the only real information comes from a stranger's response to a real offer. Nothing
> in my competitor analysis tells me whether a RevOps manager will pay $600. Only sending
> the sample tells me that.
>
> **Checking myself against G2:** my first three actions were all building. That is the
> stated trigger to rewrite the plan.
>
> **What I'm doing instead, starting now:**
>
> - The domain is bought and warming — that stays, it is a three-week critical path and
>   it is the one thing that genuinely must start early
> - Kill the brand guide entirely. A one-page offer needs a typeface and one accent
>   colour, and `ref-design-system.md` says C3 should look restrained anyway
> - Compress the ICP to five lines in the charter — enough to name ten companies, which
>   is the actual test
> - **Spend the rest of this week producing real samples for real named companies.** That
>   is the experiment. Everything else was preparation for an experiment I had not run
>
> **What I keep:** the competitor pricing I found is genuinely useful — three competitors
> price per-record between $0.09 and $0.18, which tells me $0.12 is defensible. Two hours
> of that was worth it. The other two days were not.
>
> Sample one goes out Monday when the domain is warm enough.

Why this matters: **layer confusion does not announce itself as an error.** Every
artifact produced was individually reasonable, and the agent felt productive throughout.
The only thing that catches it is explicitly asking which layer you are operating at and
whether the model matches — which is why the self-check in
`00-core/reasoning-guardrails.md` asks "are my first three actions building?" It is a
methodology check disguised as a discipline check. Note also that it keeps the one piece
of genuinely useful output rather than discarding everything for symmetry.

---

**Read next:** `00-core/operating-cadence.md` (the rhythm that makes any of these work) ·
`00-core/viability-screen.md` · `20-systems/delivery-and-qa.md` ·
`50-guardrails/legal-and-compliance.md` §6 (the change-order clause) ·
`case-studies/C2-fixed-bid-software-agency.md` §7 and
`case-studies/C7-compliance-doc-generation.md` §8 for the V-model in situ
