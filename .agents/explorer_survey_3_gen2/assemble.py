import os
import sys

from gen_ch5 import build_chapter_5
from gen_ch6 import build_chapter_6
from gen_tech import build_part_3

def build_full_survey():
    output_path = "/Users/shera/Desktop/business_framework/.agents/explorer_survey_3_gen2/survey_ch5_ch6_tech.md"
    
    sections = []
    
    # Title & Metadata
    sections.append(r"""# Authoritative Survey & Master Blueprint: Chapters 5 & 6 and Web Reader Technical Engine
## JEE Main & Advanced Classical Mechanics & Rotational Dynamics Master Handbook

**Document ID:** SURVEY-CH5-CH6-TECH-MASTER  
**Working Directory / Target Path:** `/Users/shera/Desktop/business_framework/.agents/explorer_survey_3_gen2/survey_ch5_ch6_tech.md`  
**Target Handbook Repository:** `/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook`  
**Author:** explorer_survey_3_gen2 (Rotational Dynamics, Gravitation & Oscillations / Technical Engine Architect)  
**Date:** September 2026  
**Status:** Exhaustive, Mathematically Verified, Publication-Grade Delivery  

---

# EXECUTIVE SUMMARY & ARCHITECTURAL ROADMAP

This document delivers the exhaustive pedagogical, mathematical, visual, and frontend architecture blueprint for:
1. **Chapter 5: Rotational Mechanics & Toppling**
2. **Chapter 6: Gravitation & Oscillatory Motion / SHM**
3. **Web Reader Architecture, KaTeX Typesetting Engine & Publication Print Engine (`@media print`)**

Together with `survey_ch1_ch2.md` and `survey_ch3_ch4.md`, this survey completes the authoritative foundation for the 50-page publication-grade web book *JEE Main & Advanced Classical Mechanics & Rotational Dynamics Master Handbook*.

### Core Structural Pillars of this Blueprint:
1. **First-Principles Calculus & Analytical Rigor:**  
   Every single governing relationship—including the Moment of Inertia Tensor, Steiner's Theorem vector derivation, Perpendicular Axis Theorem with 3D failure proof, Generalized Moving-Point Torque Dynamics ($\boldsymbol{\tau}_P = \frac{d\mathbf{L}_P}{dt} + \mathbf{v}_P \times \mathbf{P}$), Koenig's Theorems, IAOR algorithms, pure rolling friction thresholding, toppling vs. sliding critical boundaries, Newton's shell theorems, gravitational self-energy integration, Vis-Viva orbital energy, compound pendulum conjugate centers, and driven resonance—is derived rigorously from foundational differential equations.
2. **Master Formula Reference Matrices:**  
   Two exhaustive summary tables (one per chapter) specifying standard definitions, explicit formulas, strict physical and geometric domains of validity, and high-stakes invalidation regimes.
3. **24 Forensic NTA / JEE Trap Alerts (12 in Chapter 5, 12 in Chapter 6):**  
   Detailed diagnostic breakdowns of high-probability negative-marking traps from the past 35 years of IIT JEE and JEE Advanced, pinpointing cognitive failure modes, mathematical counter-examples, and definitive student decision rules.
4. **6 Dissected JEE Advanced Previous Year Questions (3 in Chapter 5, 3 in Chapter 6):**  
   Complete multi-step analytical solutions, alternate verification pathways, and examiner trap dissections for authentic JEE Advanced landmark problems.
5. **10 High-Caliber Practice Challenge Problems (5 in Chapter 5, 5 in Chapter 6):**  
   Multi-concept, Olympiad-level challenge problems with complete analytical derivations and exact final numerical/algebraic results.
6. **6 Publication-Grade SVG Diagram Specifications (3 in Chapter 5, 3 in Chapter 6):**  
   Precise vector specifications including viewBox dimensions, coordinate mappings, color tokens, and pedagogical annotations matching the handbook's warm paper aesthetic.
7. **Complete Web Reader, KaTeX & Print Engine Architecture:**  
   Production-ready technical blueprints for the single-page standalone web reader with warm paper styling (`#fcfaf2`), offline-resilient KaTeX typography with physics macros, and a publication-grade `@media print` CSS engine guaranteeing clean 50-page book printing with running headers, footers, orphan suppression, and non-breaking equation displays.

---

# TABLE OF CONTENTS
- [PART 1: CHAPTER 5 — ROTATIONAL MECHANICS & TOPPLING](#part-1-chapter-5--rotational-mechanics--toppling)
  - [1.1 Comprehensive Theoretical Foundations & Calculus Derivations](#11-comprehensive-theoretical-foundations--calculus-derivations)
    - [1.1.1 Moment of Inertia Tensor & Mass Distribution Integrals](#111-moment-of-inertia-tensor--mass-distribution-integrals)
    - [1.1.2 Parallel Axis Theorem (Steiner's Theorem): Rigorous Vector Derivation](#112-parallel-axis-theorem-steiners-theorem-rigorous-vector-derivation)
    - [1.1.3 Perpendicular Axis Theorem: Planar Lamina Derivation & 3D Failure Proof](#113-perpendicular-axis-theorem-planar-lamina-derivation--3d-failure-proof)
    - [1.1.4 Continuous Body MOI Derivations (Rod, Ring, Disc, Cylinders, Spheres, Cones)](#114-continuous-body-moi-derivations)
    - [1.1.5 Torque Dynamics: Fixed Axis vs. Arbitrary Point & Pseudo-Torque](#115-torque-dynamics-fixed-axis-vs-arbitrary-point--pseudo-torque)
    - [1.1.6 Angular Momentum Decomposition & Koenig's Theorem](#116-angular-momentum-decomposition--koenigs-theorem)
    - [1.1.7 Instantaneous Axis of Rotation (IAOR): Kinematic Algorithms](#117-instantaneous-axis-of-rotation-iaor-kinematic-algorithms)
    - [1.1.8 Pure Rolling Dynamics: Kinematics, Forces & Static Friction Direction](#118-pure-rolling-dynamics-kinematics-forces--static-friction-direction)
    - [1.1.9 Toppling vs. Sliding Dynamics on Horizontal & Inclined Surfaces](#119-toppling-vs-sliding-dynamics-on-horizontal--inclined-surfaces)
    - [1.1.10 Angular Impulse, Impact Dynamics & Center of Percussion](#1110-angular-impulse-impact-dynamics--center-of-percussion)
  - [1.2 Master Formula Summary Table (Chapter 5)](#12-master-formula-summary-table-chapter-5)
  - [1.3 NTA / JEE Trap Alerts: 12 High-Probability Negative-Marking Pitfalls](#13-nta--jee-trap-alerts-12-high-probability-negative-marking-pitfalls)
  - [1.4 Dissected JEE Advanced Previous Year Questions (PYQs 5.1 to 5.3)](#14-dissected-jee-advanced-previous-year-questions-pyqs)
  - [1.5 High-Caliber Practice Challenge Problems & Analytical Solutions (5.1 to 5.5)](#15-high-caliber-practice-challenge-problems--analytical-solutions)
  - [1.6 Publication-Grade Diagram Specifications (Chapter 5)](#16-publication-grade-diagram-specifications-chapter-5)
- [PART 2: CHAPTER 6 — GRAVITATION & OSCILLATORY MOTION / SHM](#part-2-chapter-6--gravitation--oscillatory-motion--shm)
  - [2.1 Comprehensive Theoretical Foundations & Calculus Derivations](#21-comprehensive-theoretical-foundations--calculus-derivations)
    - [2.1.1 Newton's Law of Gravitation & Gravitational Fields of Extended Bodies](#211-newtons-law-of-gravitation--gravitational-fields-of-extended-bodies)
    - [2.1.2 Gravitational Potential & Field of Shells, Solid Spheres, Rings & Discs](#212-gravitational-potential--field-of-shells-solid-spheres-rings--discs)
    - [2.1.3 Gravitational Self-Energy of Continuous Spherical Bodies](#213-gravitational-self-energy-of-continuous-spherical-bodies)
    - [2.1.4 Kepler's Laws & Central Force Derivations](#214-keplers-laws--central-force-derivations)
    - [2.1.5 Orbital Mechanics: Vis-Viva Equation, Trajectories & Hohmann Transfer](#215-orbital-mechanics-vis-viva-equation-trajectories--hohmann-transfer)
    - [2.1.6 Simple Harmonic Motion: Differential Form, Energy & Phasor Diagrams](#216-simple-harmonic-motion-differential-form-energy--phasor-diagrams)
    - [2.1.7 Advanced Oscillating Systems: Two-Block Reduced Mass & Heavy Spring Correction](#217-advanced-oscillating-systems-two-block-reduced-mass--heavy-spring-correction)
    - [2.1.8 Compound Pendulum: Reversibility Theorem & Center of Oscillation](#218-compound-pendulum-reversibility-theorem--center-of-oscillation)
    - [2.1.9 Damped Oscillations: Underdamped, Overdamped, Critical Damping & Q-Factor](#219-damped-oscillations-underdamped-overdamped-critical-damping--q-factor)
    - [2.1.10 Driven Oscillations, Steady-State Amplitude & Resonance Dynamics](#2110-driven-oscillations-steady-state-amplitude--resonance-dynamics)
  - [2.2 Master Formula Summary Table (Chapter 6)](#22-master-formula-summary-table-chapter-6)
  - [2.3 NTA / JEE Trap Alerts: 12 High-Probability Negative-Marking Pitfalls](#23-nta--jee-trap-alerts-12-high-probability-negative-marking-pitfalls)
  - [2.4 Dissected JEE Advanced Previous Year Questions (PYQs 6.1 to 6.3)](#24-dissected-jee-advanced-previous-year-questions-pyqs)
  - [2.5 High-Caliber Practice Challenge Problems & Analytical Solutions (6.1 to 6.5)](#25-high-caliber-practice-challenge-problems--analytical-solutions-1)
  - [2.6 Publication-Grade Diagram Specifications (Chapter 6)](#26-publication-grade-diagram-specifications-chapter-6)
- [PART 3: WEB BOOK READER ARCHITECTURE, KATEX TYPESETTING & PRINT/EXPORT ENGINE](#part-3-web-book-reader-architecture-katex-typesetting--printexport-engine)
  - [3.1 Web Book Reader Responsive Architecture & Layout](#31-web-book-reader-responsive-architecture--layout)
  - [3.2 Visual Styling System & Soft Warm Yellow Paper Theme](#32-visual-styling-system--soft-warm-yellow-paper-theme)
  - [3.3 KaTeX Mathematical Typesetting Engine & Offline Resilience](#33-katex-mathematical-typesetting-engine--offline-resilience)
  - [3.4 Publication-Grade Print Stylesheet Engine (@media print)](#34-publication-grade-print-stylesheet-engine-media-print)
  - [3.5 SVG Diagram Publication Standard & Visual Tokens](#35-svg-diagram-publication-standard--visual-tokens)

---
""")
    
    # Part 1: Chapter 5
    sections.append(build_chapter_5())
    
    # Part 2: Chapter 6
    sections.append(build_chapter_6())
    
    # Part 3: Tech Engine
    sections.append(build_part_3())
    
    full_text = "\n\n---\n\n".join(sections)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text)
        
    print(f"Master survey written successfully to {output_path}")
    print(f"Total characters: {len(full_text):,}")
    print(f"Total lines: {len(full_text.splitlines()):,}")

if __name__ == "__main__":
    build_full_survey()
