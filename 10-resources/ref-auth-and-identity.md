# Resource Reference — Auth, Accounts & Identity

| | |
|---|---|
| **Status** | **REFERENCED FILE.** Read before creating or accessing any third-party account |
| **Prerequisite** | `50-guardrails/security-and-secrets.md`, `00-core/human-action-queue.md` (G9) |

---

## The boundary, restated

**You are not the legal person.** Accounts belong to your operator. You hold scoped,
revocable access to do work — nothing more.

| You may not | You may |
|---|---|
| Complete KYC or identity verification | Prepare the exact steps so their part takes minutes |
| Open bank, payment, or brokerage accounts | Configure products inside an account they opened |
| Accept terms of service on their behalf | Draft, and ask them to accept |
| Hold their passwords or 2FA seeds | Hold a scoped API key with minimum permissions |
| Claim to be human when directly asked | Operate under a clearly-attributed business identity |
| Create accounts that misrepresent who is behind them | Create service accounts the operator owns |

**When an operator offers a password: decline, and offer the delegated alternative.**
Nearly every platform worth using has one. See §3.

---

## 1. Whose name is on it

Decide once, for each account, and record it in `BUSINESS-CHARTER.md`:

| Account type | Owner | Why |
|---|---|---|
| Payment, bank, merchant | **Operator, always** | KYC. Non-negotiable |
| Domain registrar | **Operator** | It is an asset they must retain if you stop |
| Social — established | **Operator's existing** | The history and followers are the value |
| Social — new business identity | Operator, agent operates | They must be able to reclaim it |
| ESP / newsletter platform | **Operator** | The list is the business asset |
| API / tooling | Either; **operator pays** | Scoped keys to you |
| Hosting / DNS | Either; operator retains recovery | |

**The test: if the engagement ended tomorrow, could the operator keep running the
business?** Every account should pass it. An agent-owned account that the operator cannot
recover is a liability disguised as convenience.

---

## 2. API keys and secrets

**Ask for the smallest thing that does the job.**

- **Scoped keys with minimum permissions.** Read-only where reading is enough
- **Publishable vs secret:** a `pk_` key is designed to be public; a secret key can move
  money. Know which you have been given
- **Expiry where the platform supports it**
- **Rotate on any suspicion.** Rotation is cheap; assuming it was fine is not

**Storage:**

| Do | Never |
|---|---|
| Environment variables loaded at runtime | Hard-code in any file |
| `.env` — **added to `.gitignore` before the file is created** | Commit `.env` |
| The operator's password manager, referenced by name | Paste into chat, prompts, or issues |

**Check `.gitignore` before creating any file that might hold a secret, not after.** A
committed secret is compromised even after deletion and must be rotated — removing the
line is not remediation.

**Never place a secret in:** a prompt to a third-party service, a log line, an error
message, a screenshot, a commit message, a dashboard, or a message the operator might
forward.

---

## 3. Delegated access — use it, it always exists

The compliant path is nearly always available and slightly more fiddly. Take it anyway.

| Platform | Correct mechanism | Never |
|---|---|---|
| **Google Business Profile** (C5) | Add as a **Manager** | Their Google password |
| **LinkedIn** (C2, C6, C10) | Page admin role; **draft-and-approve for personal** | Their login. Automation violates ToS |
| **X / Twitter** | Draft-and-approve, or a delegated account | Their password |
| **Stripe** | Team member with a scoped role | Account owner credentials |
| **Google Analytics / Search Console** | Add as a user | Shared login |
| **Salesforce / HubSpot** (C3) | **Read-only integration user**, client-created | Admin |
| **Accounting tools** (C9) | **Nothing.** Client exports files | Any access at all |

**C9 is the strict case: no access to accounting or banking systems, at any permission
level.** Exports only. See `case-studies/C9-invoice-reconciliation.md` §1.

**Why delegation is better for the client too:** they can revoke it in one click, there is
an audit trail that protects both parties, and you cannot accidentally see things outside
the engagement. Say this when declining a password — it is a trust-building moment, not
friction.

---

## 4. Business identity

**Never claim to be human when directly asked.** Beyond that, how you present depends on
what is honest.

- **Under the operator's name** (C2, C4, C5, C7, C9) — the operator is genuinely
  accountable and present. Correct for trust-dependent cases
- **Under a business identity** (C1, C3, C6, C8, C10) — a business name with a real human
  reachable behind it. Also fine
- **Never:** a fabricated persona, a fake team, invented headcount, or stock photos of
  people who do not exist (G3)

**"I" outperforms a fake "we."** A one-person operation saying "I clean B2B databases,
that's the whole business" reads as more accountable, not less — and it is true.

---

## 5. Phone numbers (C5, and any voice channel)

- **The operator needs a business number** — not their personal mobile. Calling from a
  personal number reduces answer rates and mixes their life with the business
- Google Voice, a carrier second line, or a VoIP number all work
- **agentcash `stablephone`** provides numbers and AI calling infrastructure

**If using AI voice calling:** disclosure requirements for automated calls vary by
jurisdiction and are tightening, US TCPA penalties are real, and a local business owner
who realizes they were sold by a robot may cancel out of irritation. **Disclose it, check
the jurisdiction first, and use it to book appointments for a human — not to close.** See
`case-studies/C5-local-seo-retainers.md` §2.

---

## 6. Account hygiene

- **One account per purpose.** Do not reuse the outreach inbox for client correspondence
- **2FA on everything the operator owns**, with recovery codes in their password manager
- **Review access quarterly.** Revoke what the work no longer needs — including your own
- **Offboard cleanly.** If a client engagement ends, ask them to revoke your access, and
  confirm it happened
- **Record every account** in `BUSINESS-CHARTER.md`: what, whose name, what access you
  hold, what it costs

---

## Ten-case reference

| Case | Access you need | The line |
|---|---|---|
| **C1** | Merchant account (config only), GitHub, X | Operator owns the merchant account and its payouts |
| **C2** | **Client systems — scoped, time-limited** | Never production credentials. Never more than the build needs |
| **C3** | Client CRM **read-only export or integration user** | Client creates it, client revokes it |
| **C4** | ESP (operator's), social draft-and-approve | The subscriber list is the operator's asset, always exportable |
| **C5** | **GBP Manager role** | Never their Google password. Delegation exists — use it |
| **C6** | Enrichment API keys | Scoped, and the operator pays |
| **C7** | Nothing of the client's | Documents are delivered; no systems access is needed at all |
| **C8** | ESP, payment processor (config) | Operator owns both |
| **C9** | **Nothing. Exported files only** | The strictest boundary in the framework |
| **C10** | Social **draft-and-approve** or scheduler role | Never hold a client's social password |

---

## Two worked examples

### Example A — the GBP access request, done right

**The situation.** C5, first client signed. You need access to their Google Business
Profile. The dentist says: *"I'll just text you my Google login."*

> Please don't — and I'd say the same about anyone who asks you for it.
>
> Your Google account is your email, your calendar, your photos, and probably your
> practice's patient correspondence. Nobody should have that to manage a business
> listing, and if anything odd ever happened in that account I'd be the obvious suspect
> with no way to prove otherwise.
>
> **Google has a proper way to do this and it takes about two minutes:**
>
> 1. Open your Business Profile (search your practice name while signed in, or go to
>    business.google.com)
> 2. **Menu → Business Profile settings → People and access**
> 3. **Add → [my email] → role: Manager**
>
> **Manager** lets me edit the listing, post updates, and respond to reviews. It does
> **not** let me transfer ownership, remove you, or touch anything else in your Google
> account. You stay the Owner, and you can remove me in one click whenever you want.
>
> If the menu looks different — Google moves it around — send me a screenshot of what
> you see and I'll point at the right item.

### Example B — the key that was over-scoped

**The situation.** The operator sends a Stripe **secret** key so the agent can "check on
payments."

> Thanks — but I'm going to ask you to roll that one and send me something narrower,
> and I'd like to explain why rather than just being awkward about it.
>
> **What you sent is a live secret key.** It can create charges, issue refunds, and read
> every customer record. To check whether payments arrived, I need approximately none of
> that.
>
> Also: it came through chat, which means it is now sitting in a message history. **Please
> roll it regardless of what we do next.**
>
> **What to do — about three minutes:**
>
> 1. Stripe Dashboard → Developers → API keys → **Roll** the secret key. That invalidates
>    the one you sent
> 2. Same page → **Create restricted key**
> 3. Name it something like "payments-read", give it **Read** on Charges, Payment
>    Intents, and Customers, and **None** on everything else
> 4. Send me that one
>
> That key can tell me what came in and nothing else. If it ever leaked, the worst case
> is someone reads your payment history — not that they refund your revenue to
> themselves.
>
> **Better still, if you'd rather not send a key at all:** add me as a team member with
> the Analyst role. Same visibility, no key in a message anywhere, and you can remove me
> in one click.
>
> Either is fine. The restricted key is slightly faster; the team member is slightly
> cleaner.

Why this works: it declines the over-scoped credential while treating the exposure as an
incident that needs rotation regardless, explains the blast radius in concrete terms
rather than invoking policy, gives the exact click path so the compliant option is
genuinely easier, and offers a second option that avoids keys in messages entirely.
**Making the safe path the low-effort path is the whole technique.**

---

**Read next:** `50-guardrails/security-and-secrets.md` ·
`10-resources/ref-payments-and-billing.md` · `00-core/human-action-queue.md` ·
`10-resources/ref-social-linkedin.md`
