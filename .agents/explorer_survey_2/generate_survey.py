import sys
import os

survey_path = "/Users/shera/Desktop/business_framework/.agents/explorer_survey_2/survey_ch3_ch4.md"

with open(survey_path, "w", encoding="utf-8") as f:
    f.write("""# JEE Main & Advanced Classical Mechanics & Rotational Dynamics Master Handbook
## In-Depth Authoritative Curriculum Survey: Chapters 3 & 4
**Document ID:** SURVEY-CH3-CH4-V1  
**Target Delivery Target:** `/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook`  
**Authors:** explorer_survey_2 (Classical Mechanics & High-Stakes Physics Curriculum Specialist)  
**Date:** September 2026  
**Status:** Complete & Mathematically Rigorous  

---

# EXECUTIVE SUMMARY & ARCHITECTURAL ROADMAP

This survey provides the complete conceptual, mathematical, pedagogical, and visual blueprint for **Chapter 3 (Work, Energy & Power)** and **Chapter 4 (Center of Mass, Linear Momentum & Collisions)** of the 50-page publication-grade JEE Advanced Master Handbook. 

Each chapter has been designed from first principles to meet the dual standards of **absolute mathematical rigor** and **ruthless exam effectiveness**:
1. **First-Principles Calculus Derivations:** Every core formula is derived from fundamental definitions without hand-waving. Frame-dependent work, non-inertial pseudo-work, curl criteria for conservative fields, non-linear equilibrium stability, vertical circular motion boundary transitions, continuous COM volume integrals, oblique restitution along the line of impact, and control-volume variable-mass dynamics are explicitly formulated.
2. **Master Formula Summary Tables:** Comprehensive reference matrices detailing every governing equation alongside strict domains of validity, physical boundary conditions, and catastrophic error regimes.
3. **NTA / JEE Trap Alerts (12 per chapter = 24 total):** Exhaustively cataloged psychological and conceptual failure modes responsible for negative marks in JEE Main and JEE Advanced over the past 25 years.
4. **Dissected JEE Advanced PYQs (3 per chapter = 6 total):** Complete, unedited problem statements from historical JEE Advanced exams with first-principles solutions, alternative methods, and forensic autopsy of examiner traps.
5. **Practice Challenge Problems with Complete Solutions (5 per chapter = 10 total):** Original, high-caliber multi-concept Olympiad/JEE Advanced level problems complete with analytical step-by-step solutions and exact answer keys.
6. **Publication-Grade Diagram Specifications (3 per chapter = 6 total):** Precise geometric layouts, coordinate systems, visual hierarchy, color tokens, and SVG structure ready for direct compilation into the reader shell.

---

# TABLE OF CONTENTS
- [PART 1: CHAPTER 3 — WORK, ENERGY & POWER](#part-1-chapter-3--work-energy--power)
  - [1.1 Comprehensive Theoretical Foundations & Calculus Derivations](#11-comprehensive-theoretical-foundations--calculus-derivations)
    - [1.1.1 Work-Kinetic Energy Theorem in Inertial Reference Frames](#111-work-kinetic-energy-theorem-in-inertial-reference-frames)
    - [1.1.2 Work-Kinetic Energy Theorem in Non-Inertial Reference Frames & Pseudo-Work](#112-work-kinetic-energy-theorem-in-non-inertial-reference-frames--pseudo-work)
    - [1.1.3 Conservative Vector Fields, Potential Energy & The Curl Condition](#113-conservative-vector-fields-potential-energy--the-curl-condition)
    - [1.1.4 Potential Energy Curves U(x), Equilibrium Stability & Higher-Order Tests](#114-potential-energy-curves-ux-equilibrium-stability--higher-order-tests)
    - [1.1.5 Small Oscillations About Stable Equilibrium: Effective Spring Constant](#115-small-oscillations-about-stable-equilibrium-effective-spring-constant)
    - [1.1.6 Vertical Circular Motion (VCM): Light Inextensible String Boundary Regimes](#116-vertical-circular-motion-vcm-light-inextensible-string-boundary-regimes)
    - [1.1.7 Vertical Circular Motion: Light Rigid Rod & Constrained Double Track](#117-vertical-circular-motion-light-rigid-rod--constrained-double-track)
    - [1.1.8 Power Dynamics: Instantaneous, Average & Engine Mechanics Under Power Constraints](#118-power-dynamics-instantaneous-average--engine-mechanics-under-power-constraints)
  - [1.2 Master Formula Summary Table (Work, Energy & Power)](#12-master-formula-summary-table-work-energy--power)
  - [1.3 NTA / JEE Trap Alerts: 12 High-Probability Negative-Marking Pitfalls](#13-nta--jee-trap-alerts-12-high-probability-negative-marking-pitfalls)
  - [1.4 Dissected JEE Advanced Previous Year Questions (PYQs 3.1 to 3.3)](#14-dissected-jee-advanced-previous-year-questions-pyqs-31-to-33)
  - [1.5 High-Caliber Practice Challenge Problems & Step-by-Step Solutions (Problems 3.1 to 3.5)](#15-high-caliber-practice-challenge-problems--step-by-step-solutions-problems-31-to-35)
  - [1.6 Publication-Grade Diagram Specifications (SVGs 3.1 to 3.3)](#16-publication-grade-diagram-specifications-svgs-31-to-33)
- [PART 2: CHAPTER 4 — CENTER OF MASS, LINEAR MOMENTUM & COLLISIONS](#part-2-chapter-4--center-of-mass-linear-momentum--collisions)
  - [2.1 Comprehensive Theoretical Foundations & Calculus Derivations](#21-comprehensive-theoretical-foundations--calculus-derivations)
    - [2.1.1 Discrete vs. Continuous Formulations of Center of Mass](#211-discrete-vs-continuous-formulations-of-center-of-mass)
    - [2.1.2 Rigorous Calculus Derivations for Continuous Classical Bodies](#212-rigorous-calculus-derivations-for-continuous-classical-bodies)
    - [2.1.3 Center of Mass Frame (C-Frame) & Koenig's Kinetic Energy Decomposition](#213-center-of-mass-frame-c-frame--koenigs-kinetic-energy-decomposition)
    - [2.1.4 Dynamics of Center of Mass & Directional Momentum Conservation](#214-dynamics-of-center-of-mass--directional-momentum-conservation)
    - [2.1.5 Oblique Collisions: Line of Impact vs. Common Tangent & Restitution](#215-oblique-collisions-line-of-impact-vs-common-tangent--restitution)
    - [2.1.6 Kinetic Energy Loss in Oblique & Inelastic Collisions](#216-kinetic-energy-loss-in-oblique--inelastic-collisions)
    - [2.1.7 Variable Mass Mechanics: First-Principles Rocket Equation](#217-variable-mass-mechanics-first-principles-rocket-equation)
    - [2.1.8 Variable Mass Systems: Conveyor Belts, Leaking Freight Carts & The 50% Paradox](#218-variable-mass-systems-conveyor-belts-leaking-freight-carts--the-50-paradox)
  - [2.2 Master Formula Summary Table (Center of Mass, Momentum & Collisions)](#22-master-formula-summary-table-center-of-mass-momentum--collisions)
  - [2.3 NTA / JEE Trap Alerts: 12 High-Probability Negative-Marking Pitfalls](#23-nta--jee-trap-alerts-12-high-probability-negative-marking-pitfalls)
  - [2.4 Dissected JEE Advanced Previous Year Questions (PYQs 4.1 to 4.3)](#24-dissected-jee-advanced-previous-year-questions-pyqs-41-to-43)
  - [2.5 High-Caliber Practice Challenge Problems & Step-by-Step Solutions (Problems 4.1 to 4.5)](#25-high-caliber-practice-challenge-problems--step-by-step-solutions-problems-41-to-45)
  - [2.6 Publication-Grade Diagram Specifications (SVGs 4.1 to 4.3)](#26-publication-grade-diagram-specifications-svgs-41-to-43)
- [PART 3: HANDBOOK INTEGRATION & METRIC STANDARDS](#part-3-handbook-integration--metric-standards)

---
""")
print("Header written successfully.")
