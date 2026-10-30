# JEE Main & Advanced Classical Mechanics & Rotational Dynamics Master Handbook
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

# PART 1: CHAPTER 3 — WORK, ENERGY & POWER

## 1.1 Comprehensive Theoretical Foundations & Calculus Derivations

### 1.1.1 Work-Kinetic Energy Theorem in Inertial Reference Frames
The concept of mechanical work formalizes the action of a force field acting along a spatial trajectory. Let a particle of invariant mass $m$ traverse a smooth curve $C$ in $\mathbb{R}^3$ parameterized by arc length or time, $\mathbf{r}(t)$, from an initial configuration $\mathbf{r}_1 = \mathbf{r}(t_1)$ to a final configuration $\mathbf{r}_2 = \mathbf{r}(t_2)$.

#### Definition of Infinitesimal and Finite Work
The infinitesimal work $dW$ performed by a vector force $\mathbf{F}$ over an infinitesimal displacement $d\mathbf{r}$ is given by the differential 1-form:
$$dW = \mathbf{F} \cdot d\mathbf{r} = F_x dx + F_y dy + F_z dz$$
The total work accumulated along path $C$ is the line integral:
$$W = \int_{C} \mathbf{F} \cdot d\mathbf{r} = \int_{t_1}^{t_2} \mathbf{F}(t) \cdot \frac{d\mathbf{r}}{dt} \, dt = \int_{t_1}^{t_2} (\mathbf{F} \cdot \mathbf{v}) \, dt$$

#### Rigorous Calculus Derivation of the Theorem
From Newton's Second Law in an inertial frame, the net force acting on the particle is:
$$\mathbf{F}_{net} = \sum \mathbf{F} = m \mathbf{a} = m \frac{d\mathbf{v}}{dt}$$
Substituting $\mathbf{F}_{net}$ into the line integral of work:
$$W_{net} = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F}_{net} \cdot d\mathbf{r} = \int_{t_1}^{t_2} \left(m \frac{d\mathbf{v}}{dt}\right) \cdot (\mathbf{v} dt) = m \int_{\mathbf{v}_1}^{\mathbf{v}_2} \mathbf{v} \cdot d\mathbf{v}$$
Using the vector identity $\mathbf{v} \cdot d\mathbf{v} = \frac{1}{2} d(\mathbf{v} \cdot \mathbf{v}) = \frac{1}{2} d(v^2) = v dv$:
$$W_{net} = m \int_{v_1}^{v_2} v \, dv = \left[ \frac{1}{2} m v^2 \right]_{v_1}^{v_2} = \frac{1}{2} m v_2^2 - \frac{1}{2} m v_1^2 = K_2 - K_1 = \Delta K$$
This fundamental result holds unconditionally for:
- Any arbitrary path $C$ (rectilinear or curvilinear).
- Any force law (constant, position-dependent $\mathbf{F}(\mathbf{r})$, velocity-dependent $\mathbf{F}(\mathbf{v})$, or time-dependent $\mathbf{F}(t)$).
- Any nature of forces (conservative, non-conservative, internal, external, normal, frictional, or magnetic — noting that magnetic Lorentz forces $\mathbf{F}_B = q(\mathbf{v} \times \mathbf{B})$ always satisfy $\mathbf{F}_B \cdot \mathbf{v} \equiv 0$ and thus do identically zero work).

#### Extension to Many-Particle and Deformable Systems
For an $N$-particle system:
$$\sum_{i=1}^N W_{i,net} = \sum_{i=1}^N \Delta K_i \implies W_{ext} + W_{int} = \Delta K_{total}$$
*Critical Distinction:* While Newton's Third Law guarantees that internal forces sum to zero vectorially ($\sum \mathbf{F}_{int} = \mathbf{0}$), their corresponding work sum does **not** vanish in general:
$$W_{int} = \sum_{i<j} \int \mathbf{F}_{ij} \cdot d\mathbf{r}_i + \mathbf{F}_{ji} \cdot d\mathbf{r}_j = \sum_{i<j} \int \mathbf{F}_{ij} \cdot d(\mathbf{r}_i - \mathbf{r}_j) = \sum_{i<j} \int \mathbf{F}_{ij} \cdot d\mathbf{r}_{ij}$$
Thus, internal forces do net work whenever relative displacements occur between interacting particles (e.g., spring expansion, explosive chemical reactions, internal friction). Only for a perfectly **rigid body** ($d|\mathbf{r}_{ij}| = 0$) does internal work sum identically to zero ($W_{int}^{rigid} \equiv 0$).

---

### 1.1.2 Work-Kinetic Energy Theorem in Non-Inertial Reference Frames & Pseudo-Work
Let an observer reside in a reference frame $S'$ translating with acceleration $\mathbf{a}_0(t)$ relative to an inertial laboratory frame $S$.

#### Transformation of Kinematic Variables
$$\mathbf{r} = \mathbf{r}' + \mathbf{R}_0(t), \quad \mathbf{v} = \mathbf{v}' + \mathbf{V}_0(t), \quad \mathbf{a} = \mathbf{a}' + \mathbf{a}_0(t)$$
Multiplying by particle mass $m$:
$$m \mathbf{a}' = m \mathbf{a} - m \mathbf{a}_0(t) = \mathbf{F}_{real} + \mathbf{F}_{pseudo}$$
where the inertial pseudo-force (d'Alembert force) is defined as:
$$\mathbf{F}_{pseudo} = -m \mathbf{a}_0(t)$$

#### Formulation of Work in Frame $S'$
Taking the line integral along the trajectory $C'$ observed in $S'$:
$$\int_{C'} m \mathbf{a}' \cdot d\mathbf{r}' = \int_{C'} \mathbf{F}_{real} \cdot d\mathbf{r}' + \int_{C'} \mathbf{F}_{pseudo} \cdot d\mathbf{r}'$$
Following the identical calculus identity $m \mathbf{a}' \cdot d\mathbf{r}' = d\left(\frac{1}{2}m (v')^2\right)$, we obtain:
$$W'_{real} + W'_{pseudo} = \Delta K'$$
where:
$$W'_{real} = \int_{C'} \mathbf{F}_{real} \cdot d\mathbf{r}', \quad W'_{pseudo} = \int_{C'} (-m \mathbf{a}_0) \cdot d\mathbf{r}', \quad \Delta K' = \frac{1}{2}m (v'_2)^2 - \frac{1}{2}m (v'_1)^2$$
*Mathematical Insight:* Work is fundamentally a frame-dependent quantity because displacement is frame-dependent: $d\mathbf{r}' = d\mathbf{r} - \mathbf{V}_0 dt \ne d\mathbf{r}$. A force may perform positive work in frame $S$, negative work in frame $S'$, and zero work in frame $S''$. The Work-Kinetic Energy Theorem holds in **any** reference frame provided the work of all pseudo-forces is explicitly accounted for along the trajectory measured in that frame.

---

### 1.1.3 Conservative Vector Fields, Potential Energy & The Curl Condition
A force field $\mathbf{F}(\mathbf{r})$ is classified as **conservative** if and only if it satisfies any of the following three mathematically equivalent conditions on an open, simply connected domain $\mathcal{D} \subseteq \mathbb{R}^3$:

1. **Path Independence:** For any two points $A, B \in \mathcal{D}$ and any two piecewise smooth curves $C_1, C_2$ connecting $A$ to $B$:
   $$\int_{C_1} \mathbf{F} \cdot d\mathbf{r} = \int_{C_2} \mathbf{F} \cdot d\mathbf{r}$$
2. **Zero Closed Circulation:** For every closed contour $\Gamma \subset \mathcal{D}$:
   $$\oint_{\Gamma} \mathbf{F} \cdot d\mathbf{r} = 0$$
3. **Existence of a Scalar Potential:** There exists a continuously differentiable scalar field $U(\mathbf{r})$ such that:
   $$\mathbf{F} = -\nabla U = -\left( \frac{\partial U}{\partial x} \hat{\mathbf{i}} + \frac{\partial U}{\partial y} \hat{\mathbf{j}} + \frac{\partial U}{\partial z} \hat{\mathbf{k}} \right)$$

#### Differential Curl Condition
By Stokes' Theorem, for any orientable surface $S$ bounded by closed curve $\Gamma = \partial S$:
$$\oint_{\Gamma} \mathbf{F} \cdot d\mathbf{r} = \iint_{S} (\nabla \times \mathbf{F}) \cdot d\mathbf{A}$$
For this integral to vanish for arbitrary surfaces in $\mathcal{D}$, the integrand must vanish identically:
$$\nabla \times \mathbf{F} = \mathbf{0}$$
Expanding the curl in Cartesian components:
$$\nabla \times \mathbf{F} = \begin{vmatrix} \hat{\mathbf{i}} & \hat{\mathbf{j}} & \hat{\mathbf{k}} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_x & F_y & F_z \end{vmatrix} = \left( \frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z} \right) \hat{\mathbf{i}} + \left( \frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x} \right) \hat{\mathbf{j}} + \left( \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y} \right) \hat{\mathbf{k}} = \mathbf{0}$$
This yields the three necessary and sufficient differential equations:
$$\frac{\partial F_z}{\partial y} = \frac{\partial F_y}{\partial z}, \quad \frac{\partial F_x}{\partial z} = \frac{\partial F_z}{\partial x}, \quad \frac{\partial F_y}{\partial x} = \frac{\partial F_x}{\partial y}$$

#### Formal Definition of Potential Energy
Choosing an arbitrary reference point $\mathbf{r}_{ref}$ where $U(\mathbf{r}_{ref}) \equiv 0$:
$$U(\mathbf{r}) = -\int_{\mathbf{r}_{ref}}^{\mathbf{r}} \mathbf{F}_c \cdot d\mathbf{r}'$$
Physical meaning: The change in potential energy is the negative of the work done by the conservative force:
$$\Delta U = U(\mathbf{r}_2) - U(\mathbf{r}_1) = -W_c = -\int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F}_c \cdot d\mathbf{r}$$
When only conservative forces perform work:
$$W_{net} = W_c = -\Delta U = \Delta K \implies \Delta(K + U) = 0 \implies E = K + U = \text{constant}$$

---

### 1.1.4 Potential Energy Curves $U(x)$, Equilibrium Stability & Higher-Order Tests
In one dimension, the conservative force is given by the negative spatial gradient:
$$F(x) = -\frac{dU}{dx}$$

#### Equilibrium Criterion
An equilibrium configuration $x_0$ is defined by zero net force:
$$F(x_0) = 0 \iff \left. \frac{dU}{dx} \right|_{x_0} = 0$$

#### Analytical Taylor Expansion Around Equilibrium
To analyze stability against small perturbations $\xi = x - x_0$, expand $U(x)$ in a Taylor series about $x_0$:
$$U(x) = U(x_0) + \left. \frac{dU}{dx} \right|_{x_0} \xi + \left. \frac{1}{2!} \frac{d^2U}{dx^2} \right|_{x_0} \xi^2 + \left. \frac{1}{3!} \frac{d^3U}{dx^3} \right|_{x_0} \xi^3 + \left. \frac{1}{4!} \frac{d^4U}{dx^4} \right|_{x_0} \xi^4 + \mathcal{O}(\xi^5)$$
Since $U'(x_0) = 0$, the force for small displacement $\xi$ is:
$$F(x) = -\frac{dU}{dx} = -U''(x_0)\xi - \frac{1}{2}U'''(x_0)\xi^2 - \frac{1}{6}U^{(4)}(x_0)\xi^3 - \dots$$

#### Rigorous Stability Classification
1. **Stable Equilibrium (Local Minimum):**
   $$U''(x_0) = \left. \frac{d^2U}{dx^2} \right|_{x_0} > 0$$
   Here, $F(\xi) \approx -k_{eff}\xi$ where $k_{eff} = U''(x_0) > 0$. If displaced to $\xi > 0$, $F < 0$ (pulls backward). If displaced to $\xi < 0$, $F > 0$ (pushes forward). The force is strictly restoring.
2. **Unstable Equilibrium (Local Maximum):**
   $$U''(x_0) = \left. \frac{d^2U}{dx^2} \right|_{x_0} < 0$$
   Here, $F(\xi) \approx +|U''(x_0)|\xi$. If displaced to $\xi > 0$, $F > 0$ (accelerates further away). The force drives the particle exponentially away from equilibrium.
3. **Higher-Order & Degenerate Cases ($U''(x_0) = 0$):**
   Let $n \ge 3$ be the order of the *first non-vanishing derivative* at $x_0$, i.e., $U^{(k)}(x_0) = 0$ for $k = 1, 2, \dots, n-1$, but $U^{(n)}(x_0) \ne 0$.
   $$F(\xi) \approx -\frac{1}{(n-1)!} U^{(n)}(x_0) \xi^{n-1}$$
   - **Case 1: $n$ is Odd ($n = 3, 5, \dots$):**
     Then $n-1$ is even, so $\xi^{n-1} > 0$ for both $\xi > 0$ and $\xi < 0$. Consequently, $F(\xi)$ maintains the **same sign** on both sides of $x_0$. On one side it is restoring, but on the other side it accelerates the particle away. Hence, any equilibrium where the first non-vanishing derivative is of odd order is strictly **UNSTABLE** (Inflection Point / Saddle).
   - **Case 2: $n$ is Even ($n = 4, 6, \dots$):**
     Then $n-1$ is odd, so $\operatorname{sgn}(\xi^{n-1}) = \operatorname{sgn}(\xi)$.
     - If $U^{(n)}(x_0) > 0$, $F(\xi)$ opposes $\xi$ on both sides $\implies$ **STABLE EQUILIBRIUM** (e.g., $U(x) = \beta x^4$).
     - If $U^{(n)}(x_0) < 0$, $F(\xi)$ drives particle away on both sides $\implies$ **UNSTABLE EQUILIBRIUM** (e.g., $U(x) = -\beta x^4$).
   - **Case 3: All Derivatives Vanish:**
     $U(x) = \text{constant}$ over a finite neighborhood $\implies F(x) \equiv 0 \implies$ **NEUTRAL EQUILIBRIUM**.

---

### 1.1.5 Small Oscillations About Stable Equilibrium: Effective Spring Constant
Consider a particle of mass $m$ confined near a stable equilibrium $x_0$ with $U''(x_0) > 0$.

#### Equation of Motion
Retaining the linear restoring term in the displacement $\xi = x - x_0$:
$$m \ddot{\xi} = -U''(x_0)\xi \implies m \ddot{\xi} + k_{eff}\xi = 0$$
where the effective stiffness is:
$$k_{eff} = \left. \frac{d^2U}{dx^2} \right|_{x_0}$$
This is the canonical Simple Harmonic Oscillator (SHO) differential equation:
$$\ddot{\xi} + \omega^2 \xi = 0, \quad \omega = \sqrt{\frac{k_{eff}}{m}} = \sqrt{\frac{U''(x_0)}{m}}$$
The natural oscillation period is:
$$T = \frac{2\pi}{\omega} = 2\pi \sqrt{\frac{m}{U''(x_0)}}$$

#### Energy Landscape: Turning Points and Phase Space
Total mechanical energy is:
$$E = \frac{1}{2} m \dot{x}^2 + U(x) \implies \dot{x} = \pm \sqrt{\frac{2}{m}\left[E - U(x)\right]}$$
- **Physically Allowed Region:** $E \ge U(x)$, since kinetic energy $K = E - U(x) \ge 0$.
- **Turning Points:** Roots of $E - U(x) = 0$, where velocity momentarily vanishes ($\dot{x} = 0$).
- **Forbidden Region:** $E < U(x)$, where classical motion cannot penetrate ($K < 0$).
- **Bound State:** Motion is bounded between two turning points $x_{min} \le x \le x_{max}$.

---

### 1.1.6 Vertical Circular Motion (VCM): Light Inextensible String Boundary Regimes
Consider a bob of mass $m$ attached to a light, inextensible string of length $R$ fixed at pivot $O$. The bob is projected horizontally at the lowest point ($\theta = 0$) with speed $u$. Let $\theta$ measure the angular displacement from the downward vertical.

#### Dynamic Equations in Polar Coordinates
The forces acting on the bob are tension $\mathbf{T} = -T \hat{\mathbf{r}}$ and gravity $\mathbf{F}_g = mg\cos\theta \hat{\mathbf{r}} - mg\sin\theta \hat{\boldsymbol{\theta}}$.
1. **Radial Equation of Motion:**
   $$\Sigma F_r = T - mg\cos\theta = m a_r = \frac{m v^2}{R} \implies T(\theta) = \frac{m v^2}{R} + mg\cos\theta$$
2. **Tangential Equation of Motion:**
   $$\Sigma F_\theta = -mg\sin\theta = m a_t = m R \ddot{\theta} \implies a_t = -g\sin\theta$$

#### Mechanical Energy Conservation
Taking the lowest point ($\theta = 0$) as the zero-potential reference datum:
$$E = \frac{1}{2} m u^2 = \frac{1}{2} m v^2(\theta) + mgR(1 - \cos\theta)$$
Solving for speed squared:
$$v^2(\theta) = u^2 - 2gR(1 - \cos\theta)$$

#### Tension as a Function of Position $\theta$
Substituting $v^2(\theta)$ into the radial dynamic equation:
$$T(\theta) = \frac{m}{R}\left[ u^2 - 2gR(1 - \cos\theta) \right] + mg\cos\theta = \frac{m}{R}\left[ u^2 - gR(2 - 3\cos\theta) \right]$$

#### Comprehensive Analysis of the Three Dynamic Regimes

```
                      Top (θ = π)
                         (•)
                     /         \
                    /           \
                   /  Upper Half \
  (θ = π/2) [•] --+-------O-------+-- [•] (θ = π/2)
                   \  Lower Half /
                    \           /
                     \         /
                         (•)
                    Bottom (θ = 0)
```

#### 1. Pure Oscillation Regime ($0 < u \le \sqrt{2gR}$)
- In this regime, velocity vanishes before tension can become zero.
- Setting $v(\theta_{stop}) = 0$:
  $$u^2 - 2gR(1 - \cos\theta_{stop}) = 0 \implies \cos\theta_{stop} = 1 - \frac{u^2}{2gR} \ge 0 \implies \theta_{stop} \le \frac{\pi}{2}$$
- Evaluating tension at this turning point:
  $$T(\theta_{stop}) = mg\cos\theta_{stop} = mg\left(1 - \frac{u^2}{2gR}\right) \ge 0$$
- The bob oscillates back and forth in the lower semicircle with angular amplitude $\theta_{max} = \arccos(1 - u^2/(2gR)) \le 90^\circ$. The string never goes slack.

#### 2. Slackening & Projectile Regime ($\sqrt{2gR} < u < \sqrt{5gR}$)
- In this regime, tension vanishes in the upper semicircle while velocity is strictly non-zero.
- Setting $T(\theta_0) = 0$ for $\theta_0 \in (\pi/2, \pi)$:
  $$u^2 - gR(2 - 3\cos\theta_0) = 0 \implies \cos\theta_0 = -\frac{u^2 - 2gR}{3gR}$$
- Since $\sqrt{2gR} < u < \sqrt{5gR}$, we have $-1 < \cos\theta_0 < 0$, placing $\theta_0$ uniquely in the second quadrant ($90^\circ < \theta_0 < 180^\circ$).
- Speed at the slackening instant:
  $$v_0^2 = u^2 - 2gR(1 - \cos\theta_0) = -gR\cos\theta_0 = gR|\cos\theta_0| > 0$$
- **Parabolic Trajectory Phase:** Once $T = 0$, the string ceases to exert constraint force. The bob enters free projectile motion under gravity with:
  - Initial position: $x_0 = R\sin\theta_0$, $y_0 = -R\cos\theta_0 = R|\cos\theta_0|$ (taking pivot $O$ as origin $(0,0)$).
  - Initial velocity: $\mathbf{v}_0 = v_0(-\cos\theta_0 \hat{\mathbf{i}} + \sin\theta_0 \hat{\mathbf{j}})$ inclined at an angle $\alpha = \theta_0 - 90^\circ$ above the horizontal.
  - Maximum height above the pivot:
    $$y_{apex} = y_0 + \frac{v_{0y}^2}{2g} = -R\cos\theta_0 + \frac{(-gR\cos\theta_0)\sin^2\theta_0}{2g} = -R\cos\theta_0\left(1 + \frac{1}{2}\sin^2\theta_0\right)$$
  - Radius of curvature at the instant of slackening:
    $$\rho = \frac{v_0^2}{a_{\perp}} = \frac{-gR\cos\theta_0}{g\sin\theta_0} = R|\cot\theta_0|$$
  - Since $\rho < R$, the parabolic flight curves inward inside the circular envelope.

#### 3. Complete Loop Regime ($u \ge \sqrt{5gR}$)
- For complete looping, the string must maintain non-negative tension across the entire circle ($T(\theta) \ge 0$ for all $\theta \in [0, \pi]$).
- Since $T(\theta)$ is monotonically decreasing with $\theta$, the global minimum occurs at the topmost point ($\theta = \pi$):
  $$T_{top} = T(\pi) = \frac{m}{R}\left[ u^2 - gR(2 - 3(-1)) \right] = \frac{m}{R}(u^2 - 5gR) \ge 0 \implies u \ge \sqrt{5gR}$$
- Speed at the top:
  $$v_{top} = \sqrt{u^2 - 4gR} \ge \sqrt{gR}$$
- Tension at the bottom:
  $$T_{bot} = T(0) = \frac{m}{R}(u^2 + gR) \ge 6mg$$
- **Universal Tension Difference Identity:**
  $$T_{bot} - T_{top} = \frac{m}{R}(u^2 + gR) - \frac{m}{R}(u^2 - 5gR) = 6mg$$
  *Remarkable Theorem:* The difference between bottom and top tension is universally equal to $6mg$, strictly independent of the initial velocity $u$ and circle radius $R$.

---

### 1.1.7 Vertical Circular Motion: Light Rigid Rod & Constrained Double Track
When the bob is attached to a light, rigid, massless rod of length $R$ (or constrained between concentric smooth vertical circular tracks):

#### Axial Thrust vs. Tension
A rigid rod can transmit both tension ($N > 0$, pulling inward) and compression ($N < 0$, pushing outward). Consequently, the bob cannot leave the circular trajectory under any circumstances.

#### Looping Boundary Condition
The condition to complete a full vertical circle reduces purely to energy conservation: the speed at the top must satisfy $v_{top} \ge 0$.
$$v_{top}^2 = u^2 - 4gR \ge 0 \implies u \ge \sqrt{4gR} = 2\sqrt{gR}$$

#### Topmost Axial Normal Force Analysis
$$N_{top} + mg = \frac{m v_{top}^2}{R} \implies N_{top} = \frac{m(u^2 - 4gR)}{R} - mg = \frac{m u^2}{R} - 5mg$$
- If $u = 2\sqrt{gR}$: $v_{top} = 0 \implies N_{top} = -mg$ (Rod is in **compression**, pushing vertically upward with $mg$ to support the bob).
- If $u = \sqrt{5gR}$: $v_{top} = \sqrt{gR} \implies N_{top} = 0$ (Rod exerts zero axial force; gravity alone provides the necessary centripetal acceleration).
- If $u > \sqrt{5gR}$: $v_{top} > \sqrt{gR} \implies N_{top} > 0$ (Rod is in **tension**, pulling downward to provide excess centripetal acceleration).

---

### 1.1.8 Power Dynamics: Instantaneous, Average & Engine Mechanics Under Power Constraints

#### Definitions
- **Instantaneous Power:** The scalar rate of energy transfer:
  $$P(t) = \frac{dW}{dt} = \mathbf{F} \cdot \frac{d\mathbf{r}}{dt} = \mathbf{F} \cdot \mathbf{v} = F_t v$$
- **Average Power:**
  $$P_{avg} = \frac{\Delta W}{\Delta t} = \frac{1}{\Delta t} \int_0^{\Delta t} P(t) \, dt$$

#### Vehicle Motion Under Constant Engine Power $P$
Consider a vehicle of mass $m$ starting from rest ($v(0) = 0, x(0) = 0$) driven by an engine delivering constant rated power $P$ without resistive dissipation.

1. **Velocity as a Function of Time:**
   $$P = F v = m v \frac{dv}{dt} \implies v^2 dv = \frac{P}{m} dt$$
   Integrating both sides:
   $$\int_0^v v'^2 dv' = \frac{P}{m} \int_0^t dt' \implies \frac{1}{3}v^3 = \frac{P}{m} t \implies v(t) = \left( \frac{3Pt}{m} \right)^{1/3}$$
2. **Acceleration as a Function of Time:**
   $$a(t) = \frac{dv}{dt} = \frac{1}{3}\left( \frac{3P}{m} \right)^{1/3} t^{-2/3} = \left( \frac{P}{9 m t^2} \right)^{1/3}$$
3. **Displacement as a Function of Time:**
   $$x(t) = \int_0^t v(t') dt' = \left( \frac{3P}{m} \right)^{1/3} \int_0^t t'^{1/3} dt' = \frac{3}{4} \left( \frac{3P}{m} \right)^{1/3} t^{4/3}$$
4. **Velocity as a Function of Displacement:**
   $$P = m v^2 \frac{dv}{dx} \implies v^2 dv = \frac{P}{m} dx \implies \frac{1}{3}v^3 = \frac{P}{m} x \implies v(x) = \left( \frac{3Px}{m} \right)^{1/3}$$

#### The Physical Singularity at $t=0$ & Traction Thresholding
Notice that as $t \to 0$, the mathematical model yields $v(0) = 0 \implies F = P/v \to \infty$ and $a \to \infty$. In physical reality, tractive force is bounded by static friction between tires and road:
$$F_{max} = \mu mg \implies a_{max} = \mu g$$
A real engine thus undergoes a **two-phase motion**:
- **Phase I ($0 \le t \le t_c$): Traction-Limited (Constant Force):**
  $$F = \mu mg, \quad a = \mu g, \quad v(t) = \mu g t, \quad x(t) = \frac{1}{2}\mu g t^2$$
  The critical transition time $t_c$ occurs when power reaches engine rating $P$:
  $$P = F v(t_c) = (\mu mg)(\mu g t_c) \implies t_c = \frac{P}{\mu^2 m g^2}$$
- **Phase II ($t > t_c$): Power-Limited (Constant Power $P$):**
  For $t > t_c$, force drops as $F = P/v < \mu mg$, and velocity transitions to $v(t) = \left( v_c^3 + \frac{3P}{m}(t - t_c) \right)^{1/3}$.
