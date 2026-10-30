# Project: JEE Main & Advanced Classical Mechanics & Rotational Dynamics Master Handbook

## Architecture
The handbook is a publication-grade, 50-page equivalent standalone interactive web book designed for JEE Main & Advanced aspirants.
- **Visual Design**: Soft warm yellow/cream paper aesthetic (`#fcfaf2` background, `#f7f3e8` card tint, `#e8dec8` borders, `#1e293b` ink typography, crimson trap callouts, emerald/gold professor tips).
- **Navigation**: Responsive sidebar with smooth scrolling, chapter section trees, reading progress indicator, and mobile collapsible drawer.
- **Math Engine**: KaTeX typesetting with physics macros and resilient local offline fallback (`assets/katex/`).
- **Print & Export Engine**: High-fidelity `@media print` CSS engine supporting A4 printing (`Cmd + P`), forced chapter page breaks, dynamic running headers/footers with page counters, orphan/widow suppression, and unbreakable equation/diagram blocks.
- **Visual Assets**: Publication-grade vector inline SVGs for Free Body Diagrams, multi-block friction, potential wells, oblique collisions, pure rolling velocity/friction vectors, and orbital/SHM phasors.
- **Testing Architecture**: Independent opaque-box test runner validating all 4 tiers (Feature Coverage, Boundary & Corner Cases, Cross-Feature Combinations, Real-World Application Scenarios), followed by white-box adversarial stress testing (Tier 5).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Web Reader Shell | Standalone HTML5 layout, `#fcfaf2` palette, responsive sidebar, reading progress bar | M1 | ORIGINAL_REQUEST §R2 |
| 2 | KaTeX Typography & Offline Fallback | Mathematical notation typesetting with offline fallback | M1 | ORIGINAL_REQUEST §R4 |
| 3 | Print CSS Engine | `@media print` stylesheet for clean 50+ page book export with headers & no split math | M1 | ORIGINAL_REQUEST §R4 |
| 4 | E2E Testing Infrastructure | Automated test runner, DOM/syntax/LaTeX validation, 4-tier test suite | M1 | ORIGINAL_REQUEST §Acceptance |
| 5 | Chapter 1: Kinematics | Cartesian/polar/tangential coordinates, river-swimmer, rain-man, incline projectile, curvature | M2 | ORIGINAL_REQUEST §R1.1 |
| 6 | Chapter 1 Formula Table & Traps | Formula validity table, >=10 NTA trap alerts (1.1-1.12), 3 PYQs, 5 challenge problems | M2 | ORIGINAL_REQUEST §R1 |
| 7 | Chapter 1 SVG Diagrams | Incline projectile geometry, curvilinear acceleration vectors | M2 | ORIGINAL_REQUEST §R3 |
| 8 | Chapter 2: Newton's Laws & Friction | Non-inertial frames, pseudo-forces, wedge constraints, multi-block friction thresholding | M2 | ORIGINAL_REQUEST §R1.2 |
| 9 | Chapter 2 Formula Table & Traps | Formula validity table, >=10 NTA trap alerts (2.1-2.12), 3 PYQs, 5 challenge problems | M2 | ORIGINAL_REQUEST §R1 |
| 10 | Chapter 2 SVG Diagrams | Multi-block friction FBD with resolved components, wedge-pulley constraint | M2 | ORIGINAL_REQUEST §R3 |
| 11 | Chapter 3: Work, Energy & Power | Work-KE theorem, conservative fields, curl test, potential wells U(x), stability, VCM regimes | M3 | ORIGINAL_REQUEST §R1.3 |
| 12 | Chapter 3 Formula Table & Traps | Formula validity table, >=10 NTA trap alerts (3.1-3.12), 3 PYQs, 5 challenge problems | M3 | ORIGINAL_REQUEST §R1 |
| 13 | Chapter 3 SVG Diagrams | Potential energy well with equilibrium points, VCM string vs rod tension regimes | M3 | ORIGINAL_REQUEST §R3 |
| 14 | Chapter 4: Center of Mass & Collisions | Continuous COM calculus, Koenig's theorem, oblique restitution, variable mass rocket & conveyor | M3 | ORIGINAL_REQUEST §R1.4 |
| 15 | Chapter 4 Formula Table & Traps | Formula validity table, >=10 NTA trap alerts (4.1-4.12), 3 PYQs, 5 challenge problems | M3 | ORIGINAL_REQUEST §R1 |
| 16 | Chapter 4 SVG Diagrams | Oblique collision velocity decomposition along LOI, variable mass control volume | M3 | ORIGINAL_REQUEST §R3 |
| 17 | Chapter 5: Rotational Mechanics | MOI tensor, Steiner/perpendicular proofs, generalized torque, IAOR, pure rolling, toppling, percussion | M4 | ORIGINAL_REQUEST §R1.5 |
| 18 | Chapter 5 Formula Table & Traps | Formula validity table, >=10 NTA trap alerts (5.1-5.12), 3 PYQs, 5 challenge problems | M4 | ORIGINAL_REQUEST §R1 |
| 19 | Chapter 5 SVG Diagrams | Pure rolling IAOR acceleration field, normal force shift during toppling, sweet spot | M4 | ORIGINAL_REQUEST §R3 |
| 20 | Chapter 6: Gravitation & SHM | Shell theorems, self-energy, Vis-Viva, Hohmann, SHM phasors, two-block, compound pendulum, damping | M4 | ORIGINAL_REQUEST §R1.6 |
| 21 | Chapter 6 Formula Table & Traps | Formula validity table, >=10 NTA trap alerts (6.1-6.12), 3 PYQs, 5 challenge problems | M4 | ORIGINAL_REQUEST §R1 |
| 22 | Chapter 6 SVG Diagrams | Gravitational field/potential profile, Hohmann transfer ellipse, compound pendulum T(d) | M4 | ORIGINAL_REQUEST §R3 |
| 23 | E2E Testing Pass (Tiers 1-4) | 100% pass of all automated test cases across all 6 chapters | M5 | ORIGINAL_REQUEST §Acceptance |
| 24 | Adversarial Hardening (Tier 5) | White-box edge case testing, unrendered LaTeX checks, broken link checks | M5 | ORIGINAL_REQUEST §Acceptance |
| 25 | Forensic Integrity Verification | Full forensic audit verifying authentic implementations and zero facade/cheating | M5 | System Instructions |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | UI Shell, KaTeX & Test Harness | Reader shell, styling, KaTeX setup, print CSS, test suite harness | none | PLANNED |
| M2 | Chapters 1 & 2 Integration | Full text, theory, formula tables, 24 traps, 6 PYQs, 10 challenges, SVGs | M1 | PLANNED |
| M3 | Chapters 3 & 4 Integration | Full text, theory, formula tables, 24 traps, 6 PYQs, 10 challenges, SVGs | M1 | PLANNED |
| M4 | Chapters 5 & 6 Integration | Full text, theory, formula tables, 24 traps, 6 PYQs, 10 challenges, SVGs | M1 | PLANNED |
| M5 | E2E Verification & Audit | 100% test pass (Tiers 1-4), Tier 5 adversarial stress, forensic audit | M2, M3, M4 | PLANNED |

## Interface Contracts
### Content HTML ↔ Reader Shell & CSS
- Every chapter is contained in an `<article class="chapter" id="chapter-N">`.
- Section headings use `<h2 class="section-title" id="chN-secM">`.
- Master Formula Tables use `<div class="table-container"><table class="formula-table">`.
- NTA Trap Alerts use `<div class="callout callout-trap"><div class="callout-badge">NTA TRAP ALERT N.M</div>...</div>`.
- JEE Advanced PYQs use `<div class="card card-pyq"><div class="card-header">JEE Advanced PYQ N.M</div>...</div>`.
- Challenge Practice Problems use `<div class="card card-challenge"><div class="card-header">Challenge Problem N.M</div><details class="solution-details"><summary>View Complete Analytical Solution</summary>...</div>`.
- SVGs use `<figure class="diagram-figure"><svg class="physics-diagram" viewBox="..." role="img">...`.

### Test Runner ↔ Content & Book Delivery
- Target directory: `/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook`
- Test Runner: `python3 tests/run_tests.py`
- Exit code 0 indicates all assertions pass; non-zero output details failing assertions.

## Code Layout
```
/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook/
├── index.html                   # Master single-page web book reader with all 6 chapters
├── css/
│   ├── style.css                # Warm yellow theme (#fcfaf2), typography, cards, callouts
│   └── print.css                # Publication-grade @media print stylesheet
├── js/
│   ├── app.js                   # Navigation, reading progress bar, drawer toggle
│   └── katex-render.js          # KaTeX auto-render & fallback
├── assets/
│   └── katex/                   # Local offline KaTeX JS/CSS/fonts fallback
└── tests/
    ├── run_tests.py             # Master test runner (Tiers 1-4 & Tier 5)
    ├── test_curriculum.py       # Validates formula tables, traps, PYQs, challenges
    ├── test_design.py           # Validates theme colors, typography, responsiveness
    └── test_print.py            # Validates @media print rules, page-breaks, equations
```
