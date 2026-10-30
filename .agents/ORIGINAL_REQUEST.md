# Original User Request

## 2026-09-05T06:34:47Z

Build a comprehensive, publication-grade 50-page equivalent Master Handbook for JEE Main & Advanced Classical Mechanics & Rotational Dynamics. The handbook must be formatted as an elegant, readable web book with a soft warm paper/yellow background theme, rich embedded diagrams, rigorous formula sheets with validity conditions, NTA/JEE negative-marking trap alerts, worked JEE Advanced PYQs, and challenge practice problems.

Working directory: `/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook`
Integrity mode: development

## Requirements

### R1. Complete 6-Chapter Mechanics Curriculum
Cover the entire classical mechanics & rotational dynamics syllabus across 6 in-depth chapters:
1. Vectors, Calculus & Advanced 2D Kinematics (River-swimmer, rain-man, projectile on inclined planes, radius of curvature)
2. Newton's Laws & Complex Friction Dynamics (Non-inertial frames, multi-block friction thresholding, wedge-pulley constraints)
3. Work, Energy & Power (Potential energy curves, equilibrium stability, vertical circular motion boundary conditions)
4. Center of Mass, Linear Momentum & Collisions (Continuous body COM, oblique collisions with restitution, variable mass systems)
5. Rotational Mechanics & Toppling (Torque about arbitrary points, IAOR, pure rolling dynamics, toppling vs sliding, angular momentum about moving axes)
6. Gravitation & Oscillatory Motion / SHM (Orbital mechanics, Kepler's laws, compound pendulums, two-block oscillators, damping & resonance)

Each chapter must contain:
- First-principles conceptual theory & derivations.
- Master formula summary table with strict domain-of-validity rules.
- Minimum 10 NTA/JEE trap alerts highlighting common calculation blunders and negative-mark pitfalls.
- Minimum 3 fully dissected JEE Advanced previous year problems (PYQs) with step-by-step reasoning.
- Minimum 5 practice challenge problems with detailed solution keys.

### R2. Book Reader Layout with Soft Warm Yellow Aesthetic
- Rendered as an interactive standalone web book with a soft warm yellow / cream paper aesthetic (`#fcfaf2` background, `#f7f3e8` card tints, `#e8dec8` borders, and rich ink typography `#1e293b`).
- Responsive table of contents with smooth navigation, chapter progress indicators, and collapsible subsections.
- Distinct styling cards for Trap Alerts (crimson tint), Formula Tables (monospace math), and IIT Professor Tips (amber/green).

### R3. Visual Physics Diagrams
- Clear, publication-grade vector diagrams (clean inline SVGs or stored web images in `assets/`) for key physical systems:
  - Free Body Diagrams (FBDs) with resolved components.
  - Multi-block friction configurations.
  - Potential energy wells with equilibrium points.
  - Oblique collision velocity vectors.
  - Pure rolling contact point velocities and friction vectors.
  - Gravitational orbits and SHM reference circle phasor diagrams.

### R4. Mathematical Typesetting & Print/Export Readiness
- Formatted with KaTeX/MathJax for crisp LaTeX mathematical notation.
- Comprehensive `@media print` CSS rules so printing (`Cmd + P` or headless export) produces a seamless ~50-page book with clean page breaks, running headers, and no broken equation blocks.
- Ready for local viewing (`open index.html`) and single-command deployment to Vercel or GitHub Pages.

## Acceptance Criteria

### Content Completeness & Rigor
- [ ] All 6 chapters fully written with complete prose, rigorous formulas, and verified physics explanations (no placeholder text or summaries).
- [ ] Each chapter contains at least 10 specific, numbered trap alerts based on real JEE failure patterns.
- [ ] Each chapter contains at least 3 worked JEE Advanced PYQs with complete solution steps.
- [ ] Each chapter contains at least 5 challenge practice problems with full solution keys.

### Design & Reader Experience
- [ ] Book theme applied: soft warm yellow paper palette (`#fcfaf2`), elegant literary serif font stack, high-contrast readable text.
- [ ] Responsive navigation sidebar allows instant jumping between chapters and sections.
- [ ] Embedded physics diagrams render crisply across all sections.

### Offline & Print Verification
- [ ] Standalone HTML opens cleanly in any standard browser without local server requirements.
- [ ] Print preview (`@media print`) formats cleanly into a 50+ page PDF book with appropriate chapter breaks.
- [ ] Validated with programmatic checks for broken links, syntax errors, or unrendered LaTeX.
