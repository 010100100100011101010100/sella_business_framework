# System — Data & Research

| | |
|---|---|
| **Status** | **REQUIRED READ** before collecting any data about any person or company |
| **Blocking for** | **C3, C6** (data *is* the product) · C2, C5, C7 (prospect research) |
| **Prerequisite** | `50-guardrails/legal-and-compliance.md` §§2–4 — **read it first, not after** |

---

## The one thing that ends data businesses

**It is not a regulator. It is a vendor termination email.**

Many enrichment and data providers prohibit resale or redistribution. If you run C3 or C6,
you are definitionally redistributing. The failure arrives as a terse notice, your
pipeline stops the same day, and three clients are expecting their monthly batch.

**Before the first delivery from any new source:**

1. **Read the terms.** Search for "resale," "redistribution," "derivative," "end user"
2. **Confirm client delivery is permitted**, or buy a redistribution licence where one is
   sold, or use a source that explicitly allows it
3. **Record it** in `ASSETS-AND-LICENCES.md`: source, date checked, the clause, the verdict
4. **Qualify a second source.** Single-source dependency means one terms change moves your
   margin or ends your product
5. **Re-read periodically**

**Any first purchase from a new vendor needs operator approval regardless of price**,
because the licence position is unknown until someone reads it. Escalation trigger 8.

---

## Lawful basis, in practice

**A work email at a named person is personal data.** `dana.w@company.com` is;
`info@company.com` generally is not.

For B2B prospecting in the EU/UK, **legitimate interest is generally available but
conditional.** To rely on it you need, in practice:

- **A written Legitimate Interest Assessment** — purpose, necessity, balancing test.
  Written **before** collection, kept on file
- **Source provenance per record.** Where each data point came from. Also a genuine
  product differentiator — clients ask
- **A privacy notice** reachable from your site
- **A global, permanent opt-out**
- **The ability to answer access or erasure requests within one month**
- **Relevance.** Legitimate interest weakens fast when the message is not plausibly
  relevant to the person's job

**B2C is materially stricter and generally requires consent.** If your list contains
consumers rather than business contacts in a business capacity, stop and get advice.

---

## Collection: what is allowed

| Method | Verdict |
|---|---|
| **Licensed data providers** | **Preferred.** They carry their own lawful basis |
| **Official APIs and feeds** | **Preferred.** ATS job feeds (Greenhouse, Lever, Ashby) exist for this |
| Public pages, rate-limited, `robots.txt` respected | Acceptable — check the site's terms |
| **Scraping LinkedIn** | **Never.** ToS violation; permanent account loss |
| Scraping sites whose terms prohibit it | Never |
| **Purchased lists** | **Never.** No lawful basis, poor deliverability, high complaints |
| Bypassing paywalls or auth | Never |

**Link and excerpt; do not reproduce wholesale.** Full reproduction of a job description
or article is a copyright question you do not want (C8).

**Attribute the source.** Rate-limit. Do not degrade someone else's service.

---

## The research layer — where the value is

For C6 especially: **you are not selling records, you are selling the researched trigger.**
Apollo sells contacts cheaply. If you deliver a list, you are a worse Apollo at ten times
the price.

### Trigger quality ladder

| Tier | Trigger | Why |
|---|---|---|
| **A** | Hiring for the exact role that owns your problem | Budget exists, pain admitted, hiring takes months |
| **A** | Public complaint naming the thing you fix | They said it themselves |
| **A** | Tooling change visible in postings or stack | Mid-migration is the buying window |
| **B** | Funding round, 3–9 months old | Money landed, scaling pain arrived |
| **B** | New executive in the relevant function | New leaders buy |
| **C** | Growth, headcount changes | True of everyone |
| **D** | "I saw your website" | **Not a trigger** |

**Aim for A or B on every prospect. If you cannot find one, remove them from the list** —
a list of 40 with tier-A triggers beats 400 with tier C.

### The verification rule · G3, non-negotiable

**Never state a trigger you have not verified.** "I noticed you're hiring three SDRs" when
you did not check is fabrication, discovered the moment they reply "we're not." Every
trigger needs a **URL you actually opened, with a date**, stored on the record.

The specificity is only persuasive *because* it is real. Recipients can tell.

---

## Quality standards

**Define them, then gate against them every cycle** (`delivery-and-qa.md`). Quality
regression to the mean by month four is the documented failure in C6.

| Standard | Threshold |
|---|---|
| Email verification | 100% before send. Bounce > 5% is an emergency |
| Trigger tier | ≥ 80% tier A or B |
| Dated source URL | **100% of rows** |
| Provenance recorded | 100% |
| Confidence stated | Per row, honestly |

**Track these monthly and report them.** The month tier-A drops from 84% to 41% is the
month before a client churns.

---

## The per-record format

The difference between $3/prospect and $0.30/prospect:

```
Company · size · location · sector
Contact · title · email · verified date
TRIGGER  · what · dated source URL · verified date
WHY THEY BUY · the judgement a database cannot supply
SUGGESTED FIRST LINE · saves the rep the hardest ten minutes
DATA SOURCE · per field
CONFIDENCE · high/medium/low, honestly
```

**Provenance and confidence serve compliance and honesty simultaneously.** They are not
overhead — they are why the row is worth $3.

---

## Handling client data (C3, C9)

- **Encrypt at rest and in transit**
- **Segregate clients.** A cross-mix is an incident you must disclose
- **Delete raw client data 30 days after delivery, automatically.** Build it as a
  scheduled job, then say so on your site — it converts
- **Never put client data in a prompt to a third-party service** without confirming the
  agreement covers it. Frequently missed
- **Never accept a customer's credentials.** Exports or a client-authorized read-only
  integration only

---

## Ten-case reference

| Case | Data role | The boundary that binds |
|---|---|---|
| **C1** | None | — |
| **C2** | Prospect research | Verify triggers before writing them |
| **C3** | **Client data processing** | **DPA, retention, vendor resale terms** |
| **C4** | Source research | **Primary documents over coverage.** Cite everything |
| **C5** | Maps and profile data | Public data only. Never fabricate audit findings |
| **C6** | **Research is the product** | **LinkedIn ToS, GDPR basis, resale terms.** All three |
| **C7** | Public-gap assessment | Only claim what is *publicly absent*, never internal |
| **C8** | Job aggregation | **Official ATS feeds. Link-and-excerpt. Expire listings** |
| **C9** | Client financial data | **Exports only. No credentials, at any permission level** |
| **C10** | Source content | Client's own material. Never invent a statistic to improve a post |

---

## Two worked examples

### Example A — the trigger that was almost fabricated

**The situation.** C6. Building a batch. One prospect looks perfect but the research turns
up nothing recent.

> Removing Halden Logistics from this batch rather than sending a weak row.
>
> **What I have:** they fit the ICP exactly — 180 employees, freight software, US, and the
> client sells to precisely this profile. Tempting.
>
> **What I do not have:** a trigger. No hiring in the relevant function in 90 days, no
> funding, no visible tooling change, no public complaints. Their careers page has two
> engineering roles unrelated to revenue ops.
>
> **What I was about to write:** "Growing quickly and likely scaling their revenue
> operations." That is tier D — it is a guess dressed as an observation, it is true of
> nearly every company, and if the rep leads with it the prospect will hear a generic
> email.
>
> Worse: it edges toward fabrication. I would be implying I observed something I did not.
>
> **Removing them.** The batch is 197 instead of 200, and I would rather deliver 197 rows
> where every trigger is real than 200 where three are padding. If the client counts, I
> will tell them why.
>
> **Logging them for re-check next month.** Trigger absence is a timing fact, not a
> permanent one.

### Example B — the vendor terms that killed the cheaper source

**The situation.** C3. Comparing enrichment providers for a new vertical.

> Provider comparison. The cheaper one is out, and not on quality.
>
> **Provider A** — $0.04/record, strong coverage on logistics. **Terms §4.3: licensed for
> the customer's "internal business purposes"; redistribution to third parties expressly
> prohibited.**
>
> Our product is handing enriched records to clients. That is redistribution. Using A
> means operating in breach until someone notices — and the realistic outcome is a
> termination email on a day when a client is waiting for a batch.
>
> **Provider B** — $0.065/record. **§6 explicitly permits inclusion in deliverables to the
> customer's own clients.** Also exposes a per-field provenance value, which we need for
> GDPR anyway and which strengthens the deliverable.
>
> **Cost of compliance:** $0.025/record. On a 5,000-record job that is $125, taking margin
> from about 73% to 71%.
>
> **Taking B.** Two points is not a trade-off against an existential dependency.
>
> **Also:** emailing A to ask whether they sell a redistribution licence — several
> providers do, and if it is reasonable they become our qualified second source, which we
> need regardless. Not blocking on the answer.
>
> Recording both licence positions with clause references and today's date in
> `ASSETS-AND-LICENCES.md`.

Note that the compliant provider turned out to have a feature the product needed anyway.
**That is common — vendors who license for redistribution build for redistribution.**

---

**Read next:** `50-guardrails/legal-and-compliance.md` §§2–4 ·
`10-resources/ref-procurement-marketplaces.md` · `20-systems/outreach.md` ·
`50-guardrails/security-and-secrets.md`
