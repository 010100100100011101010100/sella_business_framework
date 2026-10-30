# Template — ASSETS-AND-LICENCES.md

> Copy to the business root. **Records every third-party thing you use and whether you are
> allowed to use it that way.** This file prevents the two failures that end businesses
> quietly: a vendor termination notice, and shipping a paid component nobody bought.

---

```markdown
# Assets & Licences — [business]

Last reviewed [date]

## Data sources
| Source | Used for | Resale/redistribution permitted? | Clause | Checked | Verdict |

## Code and UI components
| Component | Source | Licence | Tier (free/paid) | Checked | Where used |

## Fonts and media
| Asset | Source | Licence | Where used |

## Client-permissioned material
| Item | Client | Permission granted | Date | Scope |
```

---

## Filled example

```markdown
## Data sources
| Source | Used for | Resale permitted? | Clause | Checked | Verdict |
| Provider A | contact discovery | **NO** — "internal business purposes only" | §4.3 | 2026-09-05 | **REJECTED.** Our product redistributes |
| Provider B | contact discovery | **YES** — permits inclusion in deliverables to customer's clients | §6 | 2026-09-05 | In use. Primary |
| Provider C | email verification | Yes — verification results, no redistribution restriction | §3.1 | 2026-09-05 | In use |
| stableenrich | org search, web research | Per-call; output usable in deliverables | ToS | 2026-09-05 | In use |

## Code and UI components
| Component | Source | Licence | Tier | Checked | Where used |
| Data table, tokens | IBM Carbon | Apache 2.0 | free | 2026-09-14 | site + dashboards |
| Records table | Beautiful UI | MIT | free | 2026-09-14 | outreach dashboard |
| IBM Plex Sans | Google Fonts | OFL | free | 2026-09-14 | everywhere |

## Client-permissioned material
| Item | Client | Permission | Date | Scope |
| "1,847 duplicates in 5,000 records" | Meridian | Written, email | 2026-09-22 | Website + outreach. **Company name may NOT be used** |
```

---

## Rules

- **Check before the first delivery from any new source**, not after. Search the terms for
  "resale," "redistribution," "derivative," "end user."
- **Any first purchase from a new vendor needs operator approval regardless of price** —
  the licence position is unknown until someone reads it.
- **Qualify a second source for anything load-bearing.** Single-source dependency means one
  terms change moves your margin or ends your product.
- **Record the clause reference and the date**, not just "yes." A future agent needs to
  know what was actually read.
- **Never ship a paid-tier component without the operator buying it** — the real risk on
  mixed free/paid component libraries (`ref-design-system.md` §5).
- **Client permission is scoped.** "You may quote the result" is not "you may name us."
  Record the scope, and honour it (G3).
- **Re-review quarterly.** Terms change.
