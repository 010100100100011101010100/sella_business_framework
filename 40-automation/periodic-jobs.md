# Automation — Periodic Jobs

| | |
|---|---|
| **Status** | **REQUIRED READ** before scheduling anything |
| **Prerequisite** | `00-core/operating-cadence.md`, `30-dashboards/dashboard-spec.md` |
| **Output** | Scheduled jobs + `JOBS.md` recording what runs, when, and why |

---

## The dividing line

**Automate the collection. Never automate the judgement.**

| Automate | Never automate |
|---|---|
| Computing `metrics.json` | The weekly review's decision |
| Link-health checks | The operator report's judgement |
| Listing expiry sweeps | Deciding a kill criterion has fired |
| **Client-data deletion at 30 days** | Approving spend above the threshold |
| Days-blocked counters | Publishing in someone's name |
| Cost-per-unit rollups | Quality gate sign-off (C9 especially) |
| Draft skeletons for reports | Sending a draft without review |

**A generated "everything on track" message is worse than no message**, because it looks
like a review happened. The job prepares the numbers; a person or a reasoning pass decides
what they mean.

---

## Design rules

**1. Idempotent.** Running a job twice must be harmless. Assume it will happen.

**2. Fail loudly, into the human queue.** A silent failure on the data-deletion job is a
compliance problem nobody knows about. Every job writes a result; a failure creates a
`queue.json` entry.

**3. Never destructive without a check.** The deletion job deletes *raw client data past
30 days* — scoped, logged, and never a wildcard.

**4. Log every run.** Timestamp, outcome, what changed. Append to `DECISION-LOG.md` for
anything that alters state.

**5. Cheap and infrequent.** Nothing here needs to run every minute. Most are daily or
weekly; a few are monthly.

**6. No secrets in job definitions.** Environment variables only
(`security-and-secrets.md`).

---

## The job catalogue

### Universal — every case

| Job | Cadence | Does |
|---|---|---|
| **Metrics rollup** | Daily, early | Recompute `metrics.json` from the source files |
| **Blocked-item ageing** | Daily | Update days-waiting on `queue.json`; flag anything over 5 days |
| **Weekly report skeleton** | Weekly, before review | Draft the five sections with numbers filled. **Never sends** |
| **Monthly close pack** | 1st of month | Cash received, COGS, margin, **concentration**, churn, recurring costs, unreplaced anchors |
| **Budget check** | Daily | `business_status` / `budget_status` → seed remaining, daily room, pending approvals |

### Conditional — only if the case needs it

| Job | Cadence | For | Does |
|---|---|---|---|
| **Client-data deletion** | Daily | **C3, C6, C9** | Delete raw client data past `data_delete_due`. **Log every deletion** |
| Email health check | Daily | Outbound cases | Bounce/complaint rates; **stop banner over threshold** |
| Sequence advance | Daily | Outbound cases | Which prospects are due their next touch. **Drafts; does not send unreviewed** |
| Trigger re-verification | Weekly | C6 | Re-check source URLs still resolve |
| **Listing expiry sweep** | Daily | **C8** | Expire listings past 30 days; flag dead links |
| Link health | Weekly | C4, C8 | Every published link still resolves |
| **Cadence streak** | Daily | **C4, C8** | Consecutive publish count; **alert on a miss immediately** |
| Rank + profile pull | Weekly | C5 | Fresh map-pack position, review count, profile calls |
| Voice-guide validation | Per batch | C10 | Check output against the never-use list. **Blocks the batch on fail** |
| Framework-compat check | Monthly | C1 | Install components in a clean project; flag breakage |
| Regulatory sweep | Quarterly | C7 | Check for changes affecting shipped packs |
| Renewal + obligation dates | Weekly | Recurring cases | Anything with a date that will embarrass you if missed |

---

## Scheduling

Use the platform's scheduler — **do not build a cron server**
(`ref-hosting-and-infra.md`).

- **Scheduled tasks / cron** for recurring work
- **Sella `business_log`** for anything an operator should be able to follow without asking
- **`JOBS.md`** records every scheduled job: name, cadence, what it does, what it writes,
  what happens on failure, and **why it exists**

**Review `JOBS.md` at the monthly close.** Jobs accumulate, stop being relevant, and keep
running. A job nobody reads the output of is a job to delete.

---

## The two jobs that matter most

**1. Client-data deletion (C3, C6, C9).**

This is the one where automation is genuinely load-bearing. Manual deletion does not
happen — not through negligence, but because there is never a moment when deleting old
data is the most urgent thing.

- Runs daily, deletes raw client data past `data_delete_due`
- **Logs every deletion**: client, what, when
- **Failure creates a blocking queue item**, because a silent failure means you are
  holding data you promised to delete and told a client you had deleted
- Say so on your site and in the sales conversation — it converts (C3)

**2. Cadence streak alerting (C4, C8).**

For a publication, **cadence is the product.** A missed day teaches readers not to depend
on it, and dependence is the entire value proposition. The alert must fire the same day,
not at the weekly review.

---

## Ten-case reference

| Case | The job that earns its keep |
|---|---|
| **C1** | Framework-compatibility check — a React or Tailwind major can break every component at once |
| **C2** | Renewal/milestone dates + estimate-vs-actual logging |
| **C3** | **Client-data deletion** + margin-per-job rollup |
| **C4** | **Cadence streak alert** + open-rate trend |
| **C5** | Weekly rank/profile pull so the monthly report writes itself |
| **C6** | **Trigger-tier rollup** — the drift metric — + source-URL re-verification |
| **C7** | Quarterly regulatory sweep + document-staleness flags |
| **C8** | **Listing expiry sweep.** Decay is the documented killer |
| **C9** | **Review-gate compliance check** — flag any delivery without a named reviewer |
| **C10** | **Voice-guide validation, blocking** + COGS-per-client rollup |

---

## Two worked examples

### Example A — the deletion job that failed quietly

**The situation.** The daily deletion job has been failing for six days — a path changed
after a directory reorganization. Nobody noticed because it exited 0.

**What should have happened, and the fix:**

> The client-data deletion job has not deleted anything since 2026-09-14. Six days.
>
> **Impact:** we are holding raw data for two clients past the 30-day window we committed
> to in writing, and told them about in the sales conversation. Northwind's was due
> 2026-09-16, Corvin's 2026-09-19.
>
> **Cause:** I reorganized `data/` on the 14th and the job's path was not updated. It
> exited 0 with nothing to do, so it looked like a clean run.
>
> **Fixed:** path corrected, both deletions run, logged. Verified the files are gone
> rather than assuming.
>
> **The real fix — the job was wrong, not just the path.** A deletion job that finds
> nothing to delete should not report success silently. It now:
> - Asserts the source directory exists, and **fails loudly if not**
> - Writes a run record every time, including "0 due" as an explicit result
> - **Creates a blocking `queue.json` item on any failure**
>
> **Do we need to tell the clients?** My read: no. The data was held six days longer than
> promised, not disclosed or breached, and is now deleted. But it is your call and I would
> rather you decide with the facts than have me decide for you.
>
> Logged in `DECISION-LOG.md`.

Why this is the right shape: it reports before being asked, states the exact exposure
including client names and dates, distinguishes the *path bug* from the deeper *design
bug*, and puts the disclosure judgement where it belongs — with the operator (G9, G12).

### Example B — the job that should not exist

**The situation.** Monthly `JOBS.md` review. C3, month four.

> Reviewing scheduled jobs. Deleting one and changing another.
>
> **`competitor_price_check` — daily, deleting.** I set this up in week two to watch three
> competitors' pricing pages. It has run 89 times and detected two changes, neither of
> which we acted on, and I have not read its output since week three. It is producing a
> file nobody opens.
>
> **What I'm replacing it with:** a quarterly manual check as part of the operating
> cadence review. Competitor pricing changes on a quarterly rhythm, not a daily one — the
> cadence was wrong, not the idea.
>
> **`email_health_check` — daily, changing.** Currently logs bounce and complaint rates to
> a file. It caught nothing during the day-17 bounce incident because **nobody was reading
> the file** — I caught that by checking manually.
>
> **Change:** above threshold, it now writes a blocking item to `queue.json` and surfaces
> a stop banner on the outreach dashboard. A monitoring job that only writes to a file
> nobody reads is not monitoring, it is logging.
>
> **The general lesson I'm taking:** a job needs a *reader*. If no human and no dashboard
> consumes its output, and no failure path escalates it, it should not run. Adding "who
> reads this?" to `JOBS.md` as a required field for every job.

---

**Read next:** `40-automation/agent-state-files.md` · `00-core/operating-cadence.md` ·
`30-dashboards/dashboard-spec.md` · `50-guardrails/security-and-secrets.md`
