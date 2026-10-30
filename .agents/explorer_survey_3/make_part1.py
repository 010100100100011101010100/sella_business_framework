import os

def get_part1():
    return """# JEE Main & Advanced Classical Mechanics & Rotational Dynamics Master Handbook
## In-Depth Authoritative Curriculum Survey: Chapters 5 & 6 and Web Reader Technical Engine
**Document ID:** SURVEY-CH5-CH6-TECH-V1  
**Target Delivery Path:** `/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook`  
**Author:** explorer_survey_3 (Rotational Dynamics, Gravitation & Oscillations / Technical Engine Architect)  
**Date:** September 2026  
**Status:** Complete, Mathematically Rigorous & Publication Ready  

---

# EXECUTIVE SUMMARY & ARCHITECTURAL ROADMAP

This survey provides the complete conceptual, mathematical, pedagogical, and visual blueprint for **Chapter 5 (Rotational Mechanics & Toppling)**, **Chapter 6 (Gravitation & Oscillatory Motion / SHM)**, and the **Web Book Reader Architecture, KaTeX Typesetting & Print/Export Engine** for the 50-page publication-grade JEE Main & Advanced Classical Mechanics Master Handbook.

### Core Architectural Pillars
1. **Mathematical Rigor from First Principles:** Every governing relation—from the generalized torque relation $\boldsymbol{\tau}_O = \frac{d\mathbf{L}_O}{dt} + \mathbf{v}_O \times \mathbf{P}$ to the Vis-Viva equation $v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)$ and compound pendulum conjugate centers—is derived using rigorous differential and integral calculus. No equations are introduced without proof.
2. **Master Formula Summary Tables:** Two extensive reference matrices cataloging every formula, standard definition, strict domain of validity, and high-stakes invalidity regimes.
3. **24 Forensic NTA / JEE Trap Alerts (12 in Ch 5, 12 in Ch 6):** Catalog of high-probability negative-marking traps identifying cognitive failure modes, geometric blind spots, and mathematical missteps observed in JEE Advanced and Main over the past 30 years.
4. **Dissected JEE Advanced PYQs (3 in Ch 5, 3 in Ch 6 = 6 Total):** Fully worked, authentic JEE Advanced problems with complete derivations, multi-method verification, and forensic dissections of examiner traps.
5. **Practice Challenge Problems with Complete Analytical Solutions (5 in Ch 5, 5 in Ch 6 = 10 Total):** Original, Olympiad-caliber problems demanding multi-concept synthesis with complete analytical solutions and exact final values.
6. **Publication-Grade SVG Vector Specifications (3 in Ch 5, 3 in Ch 6 = 6 Total):** Fully styled vector blueprints adhering to the warm paper aesthetic (`#fcfaf2`), complete with geometric coordinates, vector color codes, and visual hierarchies.
7. **Complete Web Book Engine & Print Blueprint:** Modern, zero-dependency, responsive web reader architecture with cream paper aesthetics (`#fcfaf2`), KaTeX typography engine with offline local fallback, and `@media print` CSS engine producing a clean ~50-page physical book with running headers, footers, and orphan prevention.

---

# TABLE OF CONTENTS
- [PART 1: CHAPTER 5 — ROTATIONAL MECHANICS & TOPPLING](#part-1-chapter-5--rotational-mechanics--toppling)
  - [1.1 Comprehensive Theoretical Foundations & Calculus Derivations](#11-comprehensive-theoretical-foundations--calculus-derivations)
    - [1.1.1 Moment of Inertia Tensor & Mass Distribution Integrals](#111-moment-of-inertia-tensor--mass-distribution-integrals)
    - [1.1.2 Parallel Axis Theorem (Steiner's Theorem): Rigorous Vector Derivation](#112-parallel-axis-theorem-steiners-theorem-rigorous-vector-derivation)
    - [1.1.3 Perpendicular Axis Theorem: Planar Lamina Derivation & 3D Failure Proof](#113-perpendicular-axis-theorem-planar-lamina-derivation--3d-failure-proof)
    - [1.1.4 Continuous Body MOI Derivations (Rod, Ring, Disc, Cylinders, Spheres, Plates)](#114-continuous-body-moi-derivations-rod-ring-disc-cylinders-spheres-plates)
    - [1.1.5 Torque Dynamics: Fixed Axis vs. Arbitrary Point & Pseudo-Torque](#115-torque-dynamics-fixed-axis-vs-arbitrary-point--pseudo-torque)
    - [1.1.6 Angular Momentum Decomposition & Koenig's Theorem](#116-angular-momentum-decomposition--koenigs-theorem)
    - [1.1.7 Instantaneous Axis of Rotation (IAOR): Kinematic Algorithms](#117-instantaneous-axis-of-rotation-iaor-kinematic-algorithms)
    - [1.1.8 Pure Rolling Dynamics: Kinematics, Forces & Static Friction Direction](#118-pure-rolling-dynamics-kinematics-forces--static-friction-direction)
    - [1.1.9 Toppling vs. Sliding Dynamics on Horizontal & Inclined Surfaces](#119-toppling-vs-sliding-dynamics-on-horizontal--inclined-surfaces)
    - [1.1.10 Angular Impulse, Impact Dynamics & Center of Percussion](#1110-angular-impulse-impact-dynamics--center-of-percussion)
  - [1.2 Master Formula Summary Table (Chapter 5)](#12-master-formula-summary-table-chapter-5)
  - [1.3 NTA / JEE Trap Alerts: 12 High-Probability Negative-Marking Pitfalls](#13-nta--jee-trap-alerts-12-high-probability-negative-marking-pitfalls)
  - [1.4 Dissected JEE Advanced Previous Year Questions (PYQs 5.1 to 5.3)](#14-dissected-jee-advanced-previous-year-questions-pyqs-51-to-53)
  - [1.5 High-Caliber Practice Challenge Problems & Step-by-Step Solutions (5.1 to 5.5)](#15-high-caliber-practice-challenge-problems--step-by-step-solutions-51-to-55)
  - [1.6 Publication-Grade Diagram Specifications (SVGs 5.1 to 5.3)](#16-publication-grade-diagram-specifications-svgs-51-to-53)
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
  - [2.4 Dissected JEE Advanced Previous Year Questions (PYQs 6.1 to 6.3)](#24-dissected-jee-advanced-previous-year-questions-pyqs-61-to-63)
  - [2.5 High-Caliber Practice Challenge Problems & Step-by-Step Solutions (6.1 to 6.5)](#25-high-caliber-practice-challenge-problems--step-by-step-solutions-61-to-65)
  - [2.6 Publication-Grade Diagram Specifications (SVGs 6.1 to 6.3)](#26-publication-grade-diagram-specifications-svgs-61-to-63)
- [PART 3: BOOK READER ARCHITECTURE, KATEX TYPESETTING & PRINT/EXPORT ENGINE](#part-3-book-reader-architecture-katex-typesetting--printexport-engine)
  - [3.1 Web Book Reader Responsive Architecture & Layout](#31-web-book-reader-responsive-architecture--layout)
  - [3.2 Visual Styling System & Soft Warm Yellow Paper Theme](#32-visual-styling-system--soft-warm-yellow-paper-theme)
  - [3.3 KaTeX Mathematical Typesetting Engine & Offline Resilience](#33-katex-mathematical-typesetting-engine--offline-resilience)
  - [3.4 Publication-Grade Print Stylesheet Engine (@media print)](#34-publication-grade-print-stylesheet-engine-media-print)
  - [3.5 SVG Diagram Publication Standard & Visual Tokens](#35-svg-diagram-publication-standard--visual-tokens)

---

# PART 1: CHAPTER 5 — ROTATIONAL MECHANICS & TOPPLING

## 1.1 Comprehensive Theoretical Foundations & Calculus Derivations

### 1.1.1 Moment of Inertia Tensor & Mass Distribution Integrals
In classical rigid body mechanics, a rigid body is an assemblage of particles where mutual Euclidean distances are strictly invariant: $|\mathbf{r}_i - \mathbf{r}_j| = \text{const}$ for all pairs $(i, j)$. 

When a rigid body rotates about an arbitrary fixed axis characterized by unit vector $\hat{\mathbf{n}}$ passing through origin $O$, the velocity of any mass element $dm$ located at position vector $\mathbf{r}$ relative to $O$ is:
$$\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$$
The total rotational kinetic energy of the body is:
$$K_{\text{rot}} = \frac{1}{2} \int v^2 dm = \frac{1}{2} \int |\boldsymbol{\omega} \times \mathbf{r}|^2 dm$$
Using the vector identity $|\mathbf{A} \times \mathbf{B}|^2 = A^2 B^2 - (\mathbf{A}\cdot\mathbf{B})^2$:
$$K_{\text{rot}} = \frac{1}{2} \int \left[ \omega^2 r^2 - (\boldsymbol{\omega}\cdot\mathbf{r})^2 \right] dm$$
In index notation (Einstein summation convention where $i, j \in \{1,2,3\}$):
$$K_{\text{rot}} = \frac{1}{2} \omega_i \omega_j \int (r^2 \delta_{ij} - r_i r_j) dm = \frac{1}{2} \omega_i I_{ij} \omega_j = \frac{1}{2} \boldsymbol{\omega}^T \mathbf{I} \boldsymbol{\omega}$$
where $\mathbf{I}$ is the symmetric second-rank **Inertia Tensor**:
$$\mathbf{I} = \begin{bmatrix} I_{xx} & -I_{xy} & -I_{xz} \\ -I_{yx} & I_{yy} & -I_{yz} \\ -I_{zx} & -I_{zy} & I_{zz} \end{bmatrix}$$
with diagonal moments of inertia:
$$I_{xx} = \int (y^2 + z^2) dm, \quad I_{yy} = \int (x^2 + z^2) dm, \quad I_{zz} = \int (x^2 + y^2) dm$$
and off-diagonal products of inertia:
$$I_{xy} = I_{yx} = \int xy\, dm, \quad I_{yz} = I_{zy} = \int yz\, dm, \quad I_{zx} = I_{xz} = \int zx\, dm$$

**Domain of Planar Rotation (JEE Scope):**  
When rotation is restricted to a single fixed axis (e.g., the $z$-axis, $\boldsymbol{\omega} = \omega \hat{\mathbf{k}}$), the kinetic energy collapses to the scalar scalar formulation:
$$K_{\text{rot}} = \frac{1}{2} I_z \omega^2$$
where $I_z = \int r_\perp^2 dm$, and $r_\perp = \sqrt{x^2 + y^2}$ is the perpendicular distance from the mass element $dm$ to the axis of rotation. The radius of gyration $k$ is defined by:
$$I = M k^2 \implies k = \sqrt{\frac{I}{M}}$$

---

### 1.1.2 Parallel Axis Theorem (Steiner's Theorem): Rigorous Vector Derivation
Let $C$ denote the Center of Mass (COM) of a rigid body of total mass $M$. Let an arbitrary reference point $O$ be separated from $C$ by displacement vector $\mathbf{d} = \mathbf{r}_C - \mathbf{r}_O$.
Let the position vector of a differential mass element $dm$ with respect to $O$ be $\mathbf{r}$, and with respect to $C$ be $\mathbf{r}'$. By vector addition:
$$\mathbf{r} = \mathbf{d} + \mathbf{r}'$$

Let an axis pass through $O$ along unit vector $\hat{\mathbf{n}}$, and a parallel axis pass through $C$ along the same unit vector $\hat{\mathbf{n}}$.
The perpendicular distance vector of $dm$ from the axis passing through $O$ is:
$$\mathbf{r}_\perp = \mathbf{r} - (\mathbf{r}\cdot\hat{\mathbf{n}})\hat{\mathbf{n}} = \hat{\mathbf{n}} \times (\mathbf{r} \times \hat{\mathbf{n}})$$
Similarly, the perpendicular distance from the parallel axis through $C$ is:
$$\mathbf{r}'_\perp = \mathbf{r}' - (\mathbf{r}'\cdot\hat{\mathbf{n}})\hat{\mathbf{n}}$$
The vector distance between the two parallel axes is the perpendicular component of $\mathbf{d}$:
$$\mathbf{d}_\perp = \mathbf{d} - (\mathbf{d}\cdot\hat{\mathbf{n}})\hat{\mathbf{n}}$$
Thus:
$$\mathbf{r}_\perp = \mathbf{d}_\perp + \mathbf{r}'_\perp$$
Squaring both sides:
$$r_\perp^2 = d_\perp^2 + (r'_\perp)^2 + 2 \mathbf{d}_\perp \cdot \mathbf{r}'_\perp$$
Integrating across the entire mass distribution of the rigid body:
$$I_O = \int r_\perp^2 dm = \int d_\perp^2 dm + \int (r'_\perp)^2 dm + 2 \mathbf{d}_\perp \cdot \int \mathbf{r}'_\perp dm$$
By the foundational definition of the Center of Mass:
$$\int \mathbf{r}' dm = 0 \implies \int \mathbf{r}'_\perp dm = 0$$
Since $\int d_\perp^2 dm = d_\perp^2 \int dm = M d_\perp^2$, and $\int (r'_\perp)^2 dm = I_{cm}$, we obtain the exact scalar theorem:
$$\mathbf{I_O = I_{cm} + M d_\perp^2}$$

#### Critical JEE Validity Constraints:
1. **One axis MUST pass through the Center of Mass ($C$):**  
   It is fundamentally invalid to apply the relation between two arbitrary parallel axes $A$ and $B$:
   $$I_A \ne I_B + M d_{AB}^2 \quad (\text{FATAL ERROR})$$
   Instead, one must transform through the COM:
   $$I_A = I_{cm} + M d_{A-cm}^2, \quad I_B = I_{cm} + M d_{B-cm}^2 \implies I_A - I_B = M(d_{A-cm}^2 - d_{B-cm}^2)$$
2. **$I_{cm}$ is the absolute minimum moment of inertia** among all parallel axes oriented along $\hat{\mathbf{n}}$:
   $$\frac{\partial I}{\partial d_\perp} = 2 M d_\perp > 0 \quad \text{for all } d_\perp > 0$$

---

### 1.1.3 Perpendicular Axis Theorem: Planar Lamina Derivation & 3D Failure Proof
Consider a truly two-dimensional mass distribution (planar lamina) situated strictly in the $xy$-plane, such that the $z$-coordinate of every mass element is identically zero ($z \equiv 0$).

The moments of inertia about the Cartesian axes are:
$$I_x = \int (y^2 + z^2) dm = \int y^2 dm \quad (\text{since } z=0)$$
$$I_y = \int (x^2 + z^2) dm = \int x^2 dm \quad (\text{since } z=0)$$
The moment of inertia about the $z$-axis (which is perpendicular to the lamina and passes through the intersection of the $x$ and $y$ axes) is:
$$I_z = \int (x^2 + y^2) dm$$
Summing $I_x$ and $I_y$:
$$I_x + I_y = \int y^2 dm + \int x^2 dm = \int (x^2 + y^2) dm = I_z$$
Hence, for any planar lamina:
$$\mathbf{I_z = I_x + I_y}$$

#### Mathematical Proof of Failure for Three-Dimensional Bodies:
Let a 3D body have non-zero mass distribution along $z$. Then:
$$I_x + I_y = \int (y^2 + z^2) dm + \int (x^2 + z^2) dm = \int (x^2 + y^2) dm + 2\int z^2 dm = I_z + 2\int z^2 dm$$
Because $\int z^2 dm > 0$ for any non-planar 3D object:
$$I_x + I_y = I_z + 2\int z^2 dm > I_z$$
Thus, applying $I_z = I_x + I_y$ to a sphere, cylinder, cone, or cube is a gross physical violation resulting in an overestimation error of exactly $2\int z^2 dm$.

---

### 1.1.4 Continuous Body MOI Derivations (Rod, Ring, Disc, Cylinders, Spheres, Plates)

#### (a) Thin Uniform Rod of Mass $M$ and Length $L$
- **Axis through COM perpendicular to rod:**  
  Set the origin at the rod's midpoint, linear mass density $\lambda = M/L$.
  $$I_{cm} = \int_{-L/2}^{L/2} x^2 (\lambda dx) = \lambda \left[ \frac{x^3}{3} \right]_{-L/2}^{L/2} = \frac{M}{L} \left( \frac{L^3}{24} - \left(-\frac{L^3}{24}\right) \right) = \frac{1}{12} M L^2$$
- **Axis through one end perpendicular to rod:**  
  Applying Parallel Axis Theorem with $d = L/2$:
  $$I_{\text{end}} = I_{cm} + M\left(\frac{L}{2}\right)^2 = \frac{1}{12}ML^2 + \frac{1}{4}ML^2 = \frac{1}{3}ML^2$$
- **Axis through COM inclined at angle $\theta$ to the rod:**  
  The perpendicular distance of an element at distance $x$ from COM is $r_\perp = x \sin\theta$.
  $$I_\theta = \int_{-L/2}^{L/2} (x \sin\theta)^2 \lambda dx = \sin^2\theta \int_{-L/2}^{L/2} x^2 \lambda dx = \frac{1}{12} M L^2 \sin^2\theta$$

#### (b) Thin Circular Ring of Mass $M$ and Radius $R$
- **Transverse Central Axis (perpendicular to ring plane):**  
  Every mass element $dm$ is at distance $r_\perp = R$.
  $$I_z = \int R^2 dm = R^2 \int dm = M R^2$$
- **Diameter Axis ($I_d$):**  
  By circular symmetry, $I_x = I_y = I_d$. Since the ring is planar, by the Perpendicular Axis Theorem:
  $$I_z = I_x + I_y = 2 I_d \implies I_d = \frac{1}{2} M R^2$$
- **Tangent Axis in Plane of Ring:**  
  $$I_{\text{tan, plane}} = I_d + M R^2 = \frac{1}{2} M R^2 + M R^2 = \frac{3}{2} M R^2$$
- **Tangent Axis Perpendicular to Plane of Ring:**  
  $$I_{\text{tan, } \perp} = I_z + M R^2 = M R^2 + M R^2 = 2 M R^2$$

#### (c) Uniform Circular Disc of Mass $M$ and Radius $R$
- **Transverse Central Axis:**  
  Surface mass density $\sigma = \frac{M}{\pi R^2}$. Take an elemental concentric ring of radius $r$ and radial width $dr$, mass $dm = \sigma (2\pi r dr) = \frac{2M}{R^2} r dr$.
  $$I_z = \int_0^R r^2 dm = \int_0^R r^2 \left( \frac{2M}{R^2} r dr \right) = \frac{2M}{R^2} \int_0^R r^3 dr = \frac{2M}{R^2} \left[ \frac{R^4}{4} \right] = \frac{1}{2} M R^2$$
- **Diameter Axis ($I_d$):**  
  By planar symmetry: $I_x = I_y = I_d \implies I_z = 2 I_d \implies I_d = \frac{1}{4} M R^2$.
- **Annular Disc (Inner radius $R_1$, Outer radius $R_2$):**  
  Mass $M = \sigma \pi (R_2^2 - R_1^2)$.
  $$I_z = \int_{R_1}^{R_2} r^2 \sigma (2\pi r dr) = 2\pi \sigma \left[ \frac{r^4}{4} \right]_{R_1}^{R_2} = \frac{2\pi \sigma}{4} (R_2^4 - R_1^4) = \frac{1}{2} \left[ \sigma \pi (R_2^2 - R_1^2) \right] (R_1^2 + R_2^2) = \frac{1}{2} M (R_1^2 + R_2^2)$$

#### (d) Uniform Cylinders of Mass $M$, Radius $R$, and Length $L$
- **Solid Cylinder about Longitudinal Symmetry Axis:**  
  Decomposed into coaxial thin cylindrical shells of radius $r$, length $L$, and thickness $dr$, or stacked discs of radius $R$:
  $$I_{\text{long}} = \frac{1}{2} M R^2$$
- **Solid Cylinder about Transverse Central Axis (perpendicular to cylinder length through COM):**  
  Slice the cylinder into differential discs of thickness $dz$ located at coordinate $z \in [-L/2, L/2]$. Mass of slice $dm = \frac{M}{L} dz$.  
  By parallel axis theorem, the moment of inertia of this elemental disc about the transverse central axis of the cylinder is:
  $$dI = dI_{\text{diameter}} + dm\, z^2 = \frac{1}{4} (dm) R^2 + (dm) z^2 = \frac{M}{4L} R^2 dz + \frac{M}{L} z^2 dz$$
  Integrating from $z = -L/2$ to $L/2$:
  $$I_{\text{trans, cm}} = \frac{M R^2}{4L} \int_{-L/2}^{L/2} dz + \frac{M}{L} \int_{-L/2}^{L/2} z^2 dz = \frac{1}{4} M R^2 + \frac{1}{12} M L^2$$

#### (e) Thin Spherical Shell of Mass $M$ and Radius $R$
Surface mass density $\sigma = \frac{M}{4\pi R^2}$.  
Slice the shell into horizontal rings along polar angle $\theta \in [0, \pi]$.
Radius of elemental ring $r = R \sin\theta$, distance along axis $z = R \cos\theta$.  
Surface area of ring strip $dA = 2\pi (R \sin\theta) (R d\theta) = 2\pi R^2 \sin\theta d\theta$.  
Mass of ring $dm = \sigma dA = \frac{M}{4\pi R^2} (2\pi R^2 \sin\theta d\theta) = \frac{1}{2} M \sin\theta d\theta$.  
The moment of inertia of this elemental ring about the diameter $z$-axis is:
$$dI_z = (r)^2 dm = (R \sin\theta)^2 \left( \frac{1}{2} M \sin\theta d\theta \right) = \frac{1}{2} M R^2 \sin^3\theta d\theta$$
Integrating over $\theta \in [0, \pi]$:
$$I_z = \frac{1}{2} M R^2 \int_0^\pi \sin^3\theta d\theta = \frac{1}{2} M R^2 \int_0^\pi (1 - \cos^2\theta) \sin\theta d\theta$$
Let $u = \cos\theta, du = -\sin\theta d\theta$. When $\theta=0 \implies u=1$, and $\theta=\pi \implies u=-1$:
$$\int_{-1}^1 (1 - u^2) du = \left[ u - \frac{u^3}{3} \right]_{-1}^1 = 2 - \frac{2}{3} = \frac{4}{3}$$
$$I_{\text{shell}} = \frac{1}{2} M R^2 \left( \frac{4}{3} \right) = \frac{2}{3} M R^2$$

#### (f) Uniform Solid Sphere of Mass $M$ and Radius $R$
Volume density $\rho = \frac{M}{\frac{4}{3}\pi R^3} = \frac{3M}{4\pi R^3}$.  
**Method of Nested Spherical Shells:**  
Consider an elemental spherical shell of radius $r$ and thickness $dr$.  
Volume $dV = 4\pi r^2 dr$, mass $dm = \rho dV = \frac{3M}{R^3} r^2 dr$.  
Using the thin spherical shell result $dI = \frac{2}{3} dm\, r^2$:
$$I_{\text{solid}} = \int_0^R \frac{2}{3} r^2 dm = \int_0^R \frac{2}{3} r^2 \left( \frac{3M}{R^3} r^2 dr \right) = \frac{2M}{R^3} \int_0^R r^4 dr = \frac{2M}{R^3} \left[ \frac{R^5}{5} \right] = \frac{2}{5} M R^2$$

#### (g) Planar Rectangular Plate of Mass $M$ and Sides $a \times b$
- **Axis through COM perpendicular to plate:**  
  Set coordinate axes in plate plane: $x \in [-a/2, a/2]$, $y \in [-b/2, b/2]$.  
  $$I_x = \int_{-b/2}^{b/2} y^2 \left(\frac{M}{b} dy\right) = \frac{1}{12} M b^2, \quad I_y = \int_{-a/2}^{a/2} x^2 \left(\frac{M}{a} dx\right) = \frac{1}{12} M a^2$$
  By Perpendicular Axis Theorem:
  $$I_z = I_x + I_y = \frac{1}{12} M (a^2 + b^2)$$
"""
