# E2E Test Infra: JEE Mechanics & Rotational Dynamics Master Handbook

## Test Philosophy
- Opaque-box, requirement-driven, validating against user-facing specifications in `ORIGINAL_REQUEST.md`.
- Methodology: Category-Partition + Boundary Value Analysis + Pairwise Combinatorial + Real-World Workload Testing.

## Feature Inventory
| # | Feature | Source | Tier 1 | Tier 2 | Tier 3 |
|---|---------|--------|:------:|:------:|:------:|
| 1 | Book Reader Shell & Aesthetics | ORIGINAL_REQUEST §R2 | 5 | 5 | ✓ |
| 2 | KaTeX Typography & Math Rendering | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ |
| 3 | Print CSS Engine (@media print) | ORIGINAL_REQUEST §R4 | 5 | 5 | ✓ |
| 4 | Ch 1: Kinematics (Theory, Traps, PYQs, Challenges, SVGs) | ORIGINAL_REQUEST §R1.1 | 5 | 5 | ✓ |
| 5 | Ch 2: Newton's Laws & Friction (Theory, Traps, PYQs, Challenges, SVGs) | ORIGINAL_REQUEST §R1.2 | 5 | 5 | ✓ |
| 6 | Ch 3: Work, Energy & Power (Theory, Traps, PYQs, Challenges, SVGs) | ORIGINAL_REQUEST §R1.3 | 5 | 5 | ✓ |
| 7 | Ch 4: Center of Mass & Collisions (Theory, Traps, PYQs, Challenges, SVGs) | ORIGINAL_REQUEST §R1.4 | 5 | 5 | ✓ |
| 8 | Ch 5: Rotational Mechanics (Theory, Traps, PYQs, Challenges, SVGs) | ORIGINAL_REQUEST §R1.5 | 5 | 5 | ✓ |
| 9 | Ch 6: Gravitation & SHM (Theory, Traps, PYQs, Challenges, SVGs) | ORIGINAL_REQUEST §R1.6 | 5 | 5 | ✓ |

## Test Architecture
- **Runner**: `python3 tests/run_tests.py`
- **Output**: JSON report and standard TAP/terminal summary with exit code 0 on 100% pass.
- **Directory Layout**:
  * `tests/run_tests.py`: Master test suite orchestrating Tiers 1-4.
  * `tests/test_tier1_features.py`: Verifies existence and completeness of all features (6 chapters, formula tables, >=10 traps/ch, >=3 PYQs/ch, >=5 challenges/ch, SVGs).
  * `tests/test_tier2_boundaries.py`: Verifies boundaries: word count >= 50-page equivalent (>25,000 words), trap numbering continuity, formula validity columns, solution keys completeness.
  * `tests/test_tier3_cross_features.py`: Verifies cross-feature consistency: navigation anchors link to actual section IDs, KaTeX delimiters match macros, CSS classes link to styling tokens, print CSS rules cover all chapters.
  * `tests/test_tier4_real_world.py`: Verifies real-world browser and print rendering: standalone open without server, zero missing local assets, valid SVG syntax, print page break rules.

## Real-World Application Scenarios (Tier 4)
| # | Scenario | Features Exercised | Complexity |
|---|----------|--------------------|------------|
| 1 | Student Local Offline Browser Session | Standalone HTML, local assets, KaTeX fallback, sidebar navigation | High |
| 2 | Teacher Headless Print / PDF Export | @media print, page-break-inside avoid, running headers, orphan prevention | High |
| 3 | JEE Aspirant Trap & Formula Quick Review | NTA Trap callouts, formula validity tables, responsive drawer | Medium |
| 4 | Deep-Dive PYQ & Challenge Self-Study | Dissected PYQs, collapsible challenge solutions, inline SVG diagrams | High |
| 5 | Mobile Device Responsive Reading | Viewport meta, responsive layout, sidebar toggle, touch scrolling | Medium |

## Coverage Thresholds
- Tier 1: >=5 test cases per feature (>= 45 tests)
- Tier 2: >=5 test cases per feature (>= 45 tests)
- Tier 3: Pairwise feature combination tests (>= 15 tests)
- Tier 4: Real-world workload tests (>= 5 scenarios)
- Total minimum test count: >= 110 automated tests.
