# Resource Reference — Email & Sending Domain

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Read when any cold email is planned |
| **Blocking for** | C2, C3, C6, C7 · any outbound case |
| **Lead time** | **2–3 weeks.** The longest in the framework — decide on day one |
| **Prerequisite** | `20-systems/outreach.md`, `50-guardrails/legal-and-compliance.md` §1 |

---

## The one rule that matters most

**Never send cold email from the operator's primary domain.**

Spam complaints against a domain damage its reputation **permanently and invisibly**. If
your operator's normal life runs on `theircompany.com`, a cold campaign from that domain
can degrade their ability to email clients, invoices, and their own accountant — and they
will never connect the two events, because nothing bounces. Mail just quietly starts
landing in spam folders.

This is a G4 irreversibility problem, not a best practice. **Buy a separate domain. It
costs about $12.**

**And buy it on day one**, before the pipeline exists, before the list exists, before the
offer is final. Warmup takes 2–3 weeks and it is the critical path for every outbound
case. It warms in the background while you build everything else.

---

## Choosing the sending domain

**Good patterns:**
- A close variant: `getdatacleaned.com`, `datacleaned.co`
- A brand-adjacent alternate TLD: `[brand].co` if the primary is `[brand].com`
- A descriptive phrase the buyer would recognize

**Avoid:**
- Free TLDs (`.tk`, `.xyz` at the cheap end) — many filters penalize them by default
- Hyphens and numbers — they read as throwaway
- Anything deceptively similar to a known company — that is impersonation
- Reusing a previously-burned domain. Reputation attaches to the domain, and buying a
  cheap expired one inherits whatever it did before

**Buy fresh, not aged.** "Aged domain" sellers in the cold-email space are usually selling
domains with history you cannot audit.

---

## DNS: the three records, before the first send

All three, or major providers treat you as unauthenticated and route accordingly.

**SPF** — declares which servers may send as your domain. One record. Multiple SPF
records is a common misconfiguration and invalidates both.

**DKIM** — cryptographically signs outgoing mail so the recipient can verify it was not
altered. Your sending provider gives you the record.

**DMARC** — tells receivers what to do when SPF or DKIM fails, and where to send reports.

```
Start at:   v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com
After 2wks: v=DMARC1; p=quarantine; pct=25; rua=...
Mature:     v=DMARC1; p=reject; rua=...
```

Start at `p=none` so you get reports without breaking delivery while you configure. Tighten
once the reports are clean.

**Also worth setting:** a custom tracking domain if your tool uses one (shared tracking
domains carry other senders' reputation), and a real MX record so replies arrive.

**The operator buys the domain (card — G9).** They either configure DNS or delegate
access to you. Delegation is usually faster and is a reasonable ask.

---

## Warmup — the schedule and why it is not optional

A brand-new domain sending 50 emails a day looks exactly like a spam operation, because
that is what spam operations do.

| Week | Daily volume per inbox | What you are doing |
|---|---|---|
| 1 | 5–10 | Real conversations. Warmup tooling, or genuine correspondence |
| 2 | 10–20 | Ramp. Prioritize getting replies |
| 3 | 20–35 | Begin real outreach at low volume |
| 4+ | 35–50 **ceiling** | Steady state |

**50/day per inbox is a permanent ceiling, not a ramp target.** To send more, add
inboxes — never volume per inbox.

**Replies are the strongest warmup signal.** A domain whose mail gets replied to builds
reputation far faster than one that only sends. This is another argument for the
framework's sample-led outreach: emails that give something get replies, and replies build
the domain.

**Sequencing note.** C3's 30-day plan buys the domain on day 3 and does not send until day
15. That gap is not slack — it is the warmup, and the pipeline gets built inside it.

---

## Sending volume architecture

| Need | Setup |
|---|---|
| Up to 50/day | 1 domain, 1 inbox |
| Up to 150/day | 1 domain, 3 inboxes |
| More | Additional domains — **but see below** |

**Before adding capacity, ask whether you should.** `20-systems/outreach.md` is explicit:
outreach is a research problem, not a volume problem. 40 researched emails at a 12% reply
rate beat 500 generic ones at 0.8%, and the generic version costs you the domain.

**If you are reaching for a second sending domain in month one, the strategy is probably
wrong.**

---

## Deliverability health

| Metric | Healthy | Warning | Stop |
|---|---|---|---|
| Bounce rate | < 2% | 3–5% | **> 5% — emergency.** Verify before sending again |
| Spam complaints | < 0.1% | 0.1–0.3% | **> 0.3% — stop the campaign** |
| Reply rate | > 5% | 2–5% | < 1% — message or targeting is wrong |

**Verify every address before sending** (~$0.004 each). Bounce rate is the fastest route
to a blacklist and it is entirely preventable.

**Content rules that protect deliverability:**
- Plain text, or very nearly. No HTML templates
- **No tracking pixels on cold email** — they hurt deliverability, and under GDPR
  tracking without consent is its own problem
- One link maximum, and none at all in the first email where possible
- No attachments in email one *unless the attachment is the value* — C3 and C6 attach the
  sample deliberately, and that is a considered trade
- Avoid spam-trigger formatting: ALL CAPS subjects, multiple exclamation marks, "FREE"
- **Physical postal address in the footer** — CAN-SPAM requires it
- Working unsubscribe, honoured permanently and globally

---

## Business email versus sending email

**Two different addresses, and do not confuse them.**

| | Business email | Sending email |
|---|---|---|
| **Domain** | Primary, or the operator's | The separate sending domain |
| **Used for** | Clients, invoices, replies, contracts | Cold outreach only |
| **Volume** | Low | Capped at 50/day/inbox |
| **Risk** | Must stay clean | Expendable if it burns |

**Once a prospect replies, move the conversation to the business address.** The sending
domain has done its job; the relationship belongs on an address that will still exist in
two years.

---

## Agent-mail and automation

Sending infrastructure: agentcash `stableemail` handles outbound and inboxes and is
appropriate for cold outreach.

**Do not use it for subscriber lists.** C4 and C8 send to people who signed up, which
needs real list management, one-click unsubscribe, preference handling, and bounce
processing. That belongs on a proper ESP (Beehiiv, Ghost, ConvertKit, Buttondown) under
the operator's account. Mixing the two is how a newsletter ends up with compliance
problems and a burned domain simultaneously.

**Automation boundary:** you may draft, sequence, and send cold outreach within the
volume caps. You may not send anything binding, accept terms by email, or represent
yourself as human if directly asked (G9).

---

## Ten-case reference

| Case | Sending domain? | Notes |
|---|---|---|
| **C1** | **No** | Developer audience via community and free component. Cold email does not sell $49 libraries |
| **C2** | **Yes** | Trigger-driven outbound to ops leads |
| **C3** | **Yes — day-one blocker** | The critical path. Sample attached in email one |
| **C4** | Business email only; **ESP for the brief** | Sending domain only if prospecting sponsors |
| **C5** | **No** | Phone business. Email is for sending the audit *after* the call |
| **C6** | **Yes — day-one blocker** | Ten researched leads in the email body |
| **C7** | **Yes** | Gap assessment to trigger-matched prospects |
| **C8** | ESP for issues; light sending domain for employers | Employer outreach only after the audience is real |
| **C9** | **No** | Referral-gated. Cold email does not sell money services |
| **C10** | **No** | Free public work is the channel. Email would underperform badly |

**Only four of ten need a sending domain.** Do not buy one reflexively — if your case is
in the No column, that is a week of setup and $12 you should not spend, and a channel
that would have underperformed anyway.

---

## Two worked examples

### Example A — the day-one ask that protects the critical path

> **One thing today, and it is the only thing blocking us.**
>
> **Buy a sending domain — ~$12, about 10 minutes.**
>
> Something like `getdatacleaned.com`. Namecheap or Cloudflare, then either give me DNS
> access or add three records I'll send you.
>
> **Why today, before I've even finished the pricing.** Two reasons:
>
> 1. **We can't send from your main domain.** Cold email generates spam complaints even
>    when it's done well, and those permanently damage a domain's reputation. If your
>    normal email started landing in clients' spam folders you'd never work out why —
>    nothing bounces, mail just quietly stops arriving. Not worth risking for $12.
> 2. **Warmup takes 2–3 weeks and it's our critical path.** A new domain sending at
>    volume looks like spam to every major provider, so we ramp: 5–10/day in week one,
>    up to 35–50 by week four. The clock starts the day you buy it, not the day I finish
>    the pipeline. Every day of delay is a day added to first revenue.
>
> **What I'll do while it warms:** build the cleaning pipeline, research 60 target
> companies, and produce 20 real samples. First send is day 15 if the domain lands today.
>
> One thing to avoid: don't buy an "aged" domain from a marketplace even if it's offered.
> Reputation attaches to the domain and you inherit whatever it did before.

### Example B — the bounce-rate emergency

**The situation.** Day 17. 30 emails sent, 4 bounced — 13.3%.

> Stopping sends immediately. This one is urgent and it is my error.
>
> **13.3% bounce rate against a healthy threshold of 2%.** Above 5% is the level where
> mailbox providers start treating the sender as a list-scraper, and we are nearly triple
> that. Continuing would put a domain we have spent 17 days warming onto a blocklist,
> and that is not recoverable — we would buy a new domain and start the three weeks
> again.
>
> **What went wrong:** I verified the addresses on day 8 when I built the list, then
> added 12 more prospects on day 15 from a different source and did not re-run
> verification on those. All four bounces are in that batch of 12.
>
> **What I'm doing now:**
> 1. Sends paused — done.
> 2. Re-verifying all 34 remaining addresses (~$0.14 total, about ten minutes).
> 3. Removing anything that does not verify clean rather than risking it.
> 4. Resuming at reduced volume — 10/day for three days — to let the domain settle
>    before returning to the ramp.
>
> **Process change:** verification now runs as the last step before send, on every batch,
> not once when the list is built. Adding it to the runbook.
>
> **Cost of the mistake:** about four days of sending. **Cost if I had not checked:** the
> domain, and three weeks.
>
> No action needed from you — flagging it because you should see the misses as well as
> the wins.

Why this matters: the bounce rate is a **leading** indicator of an unrecoverable failure.
The response is right because it stops first and diagnoses second, identifies the specific
process gap rather than blaming the data, fixes the process not just the instance, and
states the counterfactual cost — which is what makes the four lost days obviously worth
it. It also reports an error the operator would never otherwise have seen (G12).

---

**Read next:** `20-systems/outreach.md` · `50-guardrails/legal-and-compliance.md` §1 ·
`00-core/human-action-queue.md` · `10-resources/ref-auth-and-identity.md`
