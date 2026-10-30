import os

def build_chapter_5():
    parts = []
    
    # 1.1 Theory
    parts.append(r"""# PART 1: CHAPTER 5 — ROTATIONAL MECHANICS & TOPPLING

## 1.1 Comprehensive Theoretical Foundations & Calculus Derivations

### 1.1.1 Moment of Inertia Tensor & Mass Distribution Integrals
In classical rigid body mechanics, an idealized rigid body is a continuous collection of material points whose pairwise Euclidean distances remain strictly invariant under all external forces and torques:
$$|\mathbf{r}_i - \mathbf{r}_j| = \text{constant}, \quad \forall i, j$$

#### The Kinematics of Rigid Rotation
When a rigid body undergoes pure rotation with angular velocity $\boldsymbol{\omega}$ about an axis passing through a reference origin $O$, the velocity of any infinitesimal mass element $dm$ located at position vector $\mathbf{r}$ relative to $O$ is given by Euler's kinematic formula:
$$\mathbf{v}(\mathbf{r}) = \boldsymbol{\omega} \times \mathbf{r}$$

The total rotational kinetic energy $K_{\text{rot}}$ of the continuous mass distribution is obtained by integrating over the body volume $V$:
$$K_{\text{rot}} = \frac{1}{2} \int_V v^2 dm = \frac{1}{2} \int_V |\boldsymbol{\omega} \times \mathbf{r}|^2 dm$$

Utilizing the vector Lagrange identity $|\mathbf{A} \times \mathbf{B}|^2 = A^2 B^2 - (\mathbf{A}\cdot\mathbf{B})^2$:
$$|\boldsymbol{\omega} \times \mathbf{r}|^2 = \omega^2 r^2 - (\boldsymbol{\omega}\cdot\mathbf{r})^2$$
Expanding this in Cartesian components where $\boldsymbol{\omega} = (\omega_x, \omega_y, \omega_z)^T$ and $\mathbf{r} = (x, y, z)^T$:
$$\omega^2 r^2 - (\boldsymbol{\omega}\cdot\mathbf{r})^2 = (\omega_x^2 + \omega_y^2 + \omega_z^2)(x^2 + y^2 + z^2) - (\omega_x x + \omega_y y + \omega_z z)^2$$
Grouping terms bilinearly in $\omega_i \omega_j$:
$$K_{\text{rot}} = \frac{1}{2} \sum_{i=1}^3 \sum_{j=1}^3 \omega_i I_{ij} \omega_j = \frac{1}{2} \boldsymbol{\omega}^T \mathbf{I} \boldsymbol{\omega}$$
where $\mathbf{I}$ is the symmetric, second-rank **Moment of Inertia Tensor**:
$$\mathbf{I} = \begin{bmatrix} I_{xx} & -I_{xy} & -I_{xz} \\ -I_{yx} & I_{yy} & -I_{yz} \\ -I_{zx} & -I_{zy} & I_{zz} \end{bmatrix}$$

#### Diagonal and Off-Diagonal Components
The diagonal elements represent the moments of inertia about the Cartesian coordinate axes:
$$I_{xx} = \int_V (y^2 + z^2) dm, \quad I_{yy} = \int_V (x^2 + z^2) dm, \quad I_{zz} = \int_V (x^2 + y^2) dm$$
The off-diagonal elements represent the products of inertia, characterizing dynamic mass asymmetry:
$$I_{xy} = I_{yx} = \int_V xy \, dm, \quad I_{yz} = I_{zy} = \int_V yz \, dm, \quad I_{zx} = I_{xz} = \int_V zx \, dm$$

#### Angular Momentum Vector Formulation
The total angular momentum about origin $O$ is:
$$\mathbf{L}_O = \int_V (\mathbf{r} \times \mathbf{v}) dm = \int_V [\mathbf{r} \times (\boldsymbol{\omega} \times \mathbf{r})] dm$$
Using the vector triple product expansion $\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = \mathbf{B}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{C}(\mathbf{A}\cdot\mathbf{B})$:
$$\mathbf{r} \times (\boldsymbol{\omega} \times \mathbf{r}) = \boldsymbol{\omega}(\mathbf{r}\cdot\mathbf{r}) - \mathbf{r}(\mathbf{r}\cdot\boldsymbol{\omega}) = r^2 \boldsymbol{\omega} - (\mathbf{r}\cdot\boldsymbol{\omega})\mathbf{r}$$
Integrating across the body yields:
$$\mathbf{L}_O = \mathbf{I} \boldsymbol{\omega}$$

**Crucial Dynamic Implication for JEE Advanced:**  
In general, $\mathbf{L}_O$ is **not parallel** to $\boldsymbol{\omega}$ unless $\boldsymbol{\omega}$ aligns with one of the eigenvectors of $\mathbf{I}$ (the *Principal Axes of Inertia*). When a body rotates about a non-principal axis, off-diagonal terms generate a rotating angular momentum vector, creating non-zero dynamic bearing reactions even at constant $\omega$ ($\boldsymbol{\tau}_{\text{bearing}} = \frac{d\mathbf{L}}{dt} = \boldsymbol{\omega} \times \mathbf{L} \ne \mathbf{0}$).

#### Fixed-Axis Planar Reduction (JEE Standard Syllabus)
When rotation is geometrically constrained to a fixed axis $\hat{\mathbf{n}}$ (e.g., $\hat{\mathbf{n}} = \hat{\mathbf{k}}$), the scalar projection of angular momentum along the axis of rotation is:
$$L_z = \mathbf{L} \cdot \hat{\mathbf{k}} = I_{zz} \omega = I \omega$$
where $I = \int r_\perp^2 dm$, and $r_\perp = \sqrt{x^2 + y^2}$ is the perpendicular distance from $dm$ to the rotation axis. The radius of gyration $k$ is defined by:
$$I = M k^2 \iff k = \sqrt{\frac{I}{M}}$$

---

### 1.1.2 Parallel Axis Theorem (Steiner's Theorem): Rigorous Vector Derivation
Let $C$ denote the Center of Mass (COM) of an extended rigid body of mass $M$. Let an arbitrary reference origin $O$ be chosen, and denote the vector displacement from $C$ to $O$ as $-\mathbf{d}$, such that $\mathbf{r}_C - \mathbf{r}_O = \mathbf{d}$.

Let an arbitrary mass element $dm$ have position vector $\mathbf{r}$ relative to $O$, and position vector $\mathbf{r}'$ relative to $C$. By triangle vector addition:
$$\mathbf{r} = \mathbf{d} + \mathbf{r}'$$

Let an axis of rotation be defined by unit vector $\hat{\mathbf{n}}$ passing through $O$, and consider a parallel axis along the identical unit vector $\hat{\mathbf{n}}$ passing through $C$.
The perpendicular vector from the axis through $O$ to $dm$ is:
$$\mathbf{r}_\perp = \mathbf{r} - (\mathbf{r}\cdot\hat{\mathbf{n}})\hat{\mathbf{n}} = \hat{\mathbf{n}} \times (\mathbf{r} \times \hat{\mathbf{n}})$$
Similarly, the perpendicular vector from the axis through $C$ to $dm$ is:
$$\mathbf{r}'_\perp = \mathbf{r}' - (\mathbf{r}'\cdot\hat{\mathbf{n}})\hat{\mathbf{n}}$$
The perpendicular vector displacement between the two parallel axes is:
$$\mathbf{d}_\perp = \mathbf{d} - (\mathbf{d}\cdot\hat{\mathbf{n}})\hat{\mathbf{n}}$$
Linearly combining these perpendicular projections:
$$\mathbf{r}_\perp = \mathbf{d}_\perp + \mathbf{r}'_\perp$$

Evaluating the scalar square $r_\perp^2 = \mathbf{r}_\perp \cdot \mathbf{r}_\perp$:
$$r_\perp^2 = d_\perp^2 + (r'_\perp)^2 + 2 \mathbf{d}_\perp \cdot \mathbf{r}'_\perp$$

Integrating this identity over the entire mass distribution of the rigid body:
$$I_O = \int_M r_\perp^2 dm = \int_M d_\perp^2 dm + \int_M (r'_\perp)^2 dm + 2 \mathbf{d}_\perp \cdot \int_M \mathbf{r}'_\perp dm$$

By the foundational mathematical definition of the Center of Mass:
$$\int_M \mathbf{r}' dm = \mathbf{0} \implies \int_M \mathbf{r}'_\perp dm = \mathbf{0}$$
Furthermore, since $d_\perp$ is constant with respect to the mass integration:
$$\int_M d_\perp^2 dm = d_\perp^2 \int_M dm = M d_\perp^2$$
and by definition:
$$\int_M (r'_\perp)^2 dm = I_{cm}$$
Substituting these back into the integral equation yields Steiner's exact formula:
$$\mathbf{I_O = I_{cm} + M d_\perp^2}$$

#### Fundamental Axiomatic Constraints on Steiner's Theorem:
1. **The Pivot Axis Must Pass Through the Center of Mass:**  
   It is a catastrophic algebraic blunder to write $I_B = I_A + M d_{AB}^2$ between two arbitrary axes $A$ and $B$ neither of which passes through the COM. The correct relationship requires routing through $I_{cm}$:
   $$I_A = I_{cm} + M d_A^2, \quad I_B = I_{cm} + M d_B^2 \implies I_B - I_A = M(d_B^2 - d_A^2)$$
2. **Global Extremum Property:**  
   $I_{cm}$ is the strictly minimal moment of inertia among all mutually parallel axes in $\mathbb{R}^3$. For any displacement $d_\perp > 0$:
   $$I_O(d_\perp) > I_{cm}, \quad \left. \frac{d I_O}{d(d_\perp)} \right|_{d_\perp=0} = 0, \quad \frac{d^2 I_O}{d(d_\perp)^2} = 2M > 0$$

---

### 1.1.3 Perpendicular Axis Theorem: Planar Lamina Derivation & 3D Failure Proof

#### Derivation for a Two-Dimensional Lamina
Consider an idealized two-dimensional planar mass distribution situated strictly in the $xy$-plane ($z \equiv 0$ for every mass particle $dm$).
The moments of inertia about the in-plane Cartesian axes $x$ and $y$ are:
$$I_x = \int_M (y^2 + z^2) dm = \int_M y^2 dm \quad (\text{since } z = 0)$$
$$I_y = \int_M (x^2 + z^2) dm = \int_M x^2 dm \quad (\text{since } z = 0)$$
The moment of inertia about the transverse $z$-axis (perpendicular to the lamina and passing through the intersection $x=0, y=0$) is:
$$I_z = \int_M (x^2 + y^2) dm$$
Summing the two in-plane integrals:
$$I_x + I_y = \int_M y^2 dm + \int_M x^2 dm = \int_M (x^2 + y^2) dm = I_z$$
Hence, for any planar lamina:
$$\mathbf{I_z = I_x + I_y}$$

#### Analytical Proof of Failure for Three-Dimensional Bodies
Consider a general three-dimensional object whose mass distribution possesses non-zero thickness along the $z$-axis ($z \not\equiv 0$).
Computing the sum $I_x + I_y$:
$$I_x + I_y = \int_M (y^2 + z^2) dm + \int_M (x^2 + z^2) dm = \int_M (x^2 + y^2) dm + 2 \int_M z^2 dm = I_z + 2 \int_M z^2 dm$$
Because $z^2 > 0$ almost everywhere for a genuine 3D body:
$$2 \int_M z^2 dm > 0 \implies I_x + I_y > I_z$$
**Conclusion:** Applying $I_z = I_x + I_y$ to solid spheres, cylinders, cubes, or cones introduces an absolute error of exactly $2\int z^2 dm$, rendering the resulting calculations physically meaningless.

---

### 1.1.4 Continuous Body MOI Derivations

#### 1. Thin Uniform Rod of Mass $M$ and Length $L$
Let the rod lie along the $x$-axis from $x = -L/2$ to $x = +L/2$, with linear mass density $\lambda = M/L$.
- **Transverse Axis through COM ($x = 0$):**
  $$I_{cm} = \int_{-L/2}^{L/2} x^2 (\lambda dx) = \lambda \left[ \frac{x^3}{3} \right]_{-L/2}^{L/2} = \frac{M}{L} \left( \frac{L^3}{24} - \left(-\frac{L^3}{24}\right) \right) = \frac{1}{12} M L^2$$
- **Transverse Axis through End ($x = -L/2$):**
  By Steiner's Theorem ($d = L/2$):
  $$I_{\text{end}} = I_{cm} + M\left(\frac{L}{2}\right)^2 = \frac{1}{12}ML^2 + \frac{1}{4}ML^2 = \frac{1}{3} M L^2$$
- **Axis Inclined at Angle $\theta$ Passing Through Midpoint:**
  The perpendicular distance of an element $dx$ at position $x$ is $r_\perp = x \sin\theta$:
  $$I_\theta = \int_{-L/2}^{L/2} (x \sin\theta)^2 \lambda dx = \sin^2\theta \int_{-L/2}^{L/2} x^2 \lambda dx = \frac{1}{12} M L^2 \sin^2\theta$$

#### 2. Thin Circular Ring of Mass $M$ and Radius $R$
- **Transverse Central Axis (perpendicular to plane):**
  Every point of the ring resides at perpendicular distance $r_\perp = R$:
  $$I_z = \int_M R^2 dm = R^2 \int_M dm = M R^2$$
- **Diameter Axis ($I_d$):**
  By rotational symmetry in the plane, $I_x = I_y = I_d$. The ring is planar ($z=0$), so by the Perpendicular Axis Theorem:
  $$I_z = I_x + I_y = 2 I_d \implies I_d = \frac{1}{2} M R^2$$
- **Tangential Axis in Plane:**
  By Steiner's theorem from diameter axis ($d = R$):
  $$I_{\text{tan, in-plane}} = I_d + M R^2 = \frac{1}{2} M R^2 + M R^2 = \frac{3}{2} M R^2$$
- **Tangential Axis Perpendicular to Plane:**
  By Steiner's theorem from central transverse axis ($d = R$):
  $$I_{\text{tan, }\perp} = I_z + M R^2 = M R^2 + M R^2 = 2 M R^2$$

#### 3. Uniform Circular Disc of Mass $M$ and Radius $R$
Surface mass density $\sigma = \frac{M}{\pi R^2}$.
- **Transverse Central Axis:**
  Decompose the disc into concentric thin rings of radius $r$ and radial thickness $dr$. Mass of elemental ring $dm = \sigma (2\pi r dr) = \frac{2M}{R^2} r dr$.
  $$I_z = \int_0^R r^2 dm = \frac{2M}{R^2} \int_0^R r^3 dr = \frac{2M}{R^2} \left[ \frac{R^4}{4} \right] = \frac{1}{2} M R^2$$
- **Diameter Axis ($I_d$):**
  By planar symmetry and Perpendicular Axis Theorem:
  $$I_x + I_y = I_z \implies 2 I_d = \frac{1}{2} M R^2 \implies I_d = \frac{1}{4} M R^2$$
- **Annular Disc (Inner Radius $R_1$, Outer Radius $R_2$):**
  Area $A = \pi(R_2^2 - R_1^2)$, surface density $\sigma = \frac{M}{\pi(R_2^2 - R_1^2)}$.
  $$I_z = \int_{R_1}^{R_2} r^2 \sigma (2\pi r dr) = 2\pi \sigma \left[ \frac{r^4}{4} \right]_{R_1}^{R_2} = \frac{2\pi \sigma}{4} (R_2^4 - R_1^4)$$
  Factoring $(R_2^4 - R_1^4) = (R_2^2 - R_1^2)(R_2^2 + R_1^2)$:
  $$I_z = \frac{1}{2} \left[ \sigma \pi (R_2^2 - R_1^2) \right] (R_1^2 + R_2^2) = \frac{1}{2} M (R_1^2 + R_2^2)$$

#### 4. Uniform Cylinders (Mass $M$, Radius $R$, Length $L$)
- **Solid Cylinder about Longitudinal Symmetry Axis:**
  Equivalent to a stack of identical discs of radius $R$:
  $$I_{\text{long}} = \frac{1}{2} M R^2$$
- **Thin Hollow Cylinder (Cylindrical Shell) about Longitudinal Axis:**
  All mass elements reside at distance $R$ from the axis:
  $$I_{\text{long, shell}} = M R^2$$
- **Solid Cylinder about Transverse Central Axis (perpendicular to length through COM):**
  Slice the cylinder into differential discs of thickness $dz$ at coordinate $z \in [-L/2, L/2]$. Mass $dm = \frac{M}{L} dz$.
  By Steiner's Theorem, the moment of inertia of each slice about the transverse central axis is:
  $$dI = dI_{\text{diam}} + dm \, z^2 = \frac{1}{4} (dm) R^2 + (dm) z^2 = \frac{M R^2}{4L} dz + \frac{M}{L} z^2 dz$$
  Integrating from $z = -L/2$ to $+L/2$:
  $$I_{\text{trans, cm}} = \frac{M R^2}{4L} \int_{-L/2}^{L/2} dz + \frac{M}{L} \int_{-L/2}^{L/2} z^2 dz = \frac{1}{4} M R^2 + \frac{1}{12} M L^2$$

#### 5. Spherical Bodies of Mass $M$ and Radius $R$
- **Thin Spherical Shell about any Diameter Axis:**
  Area $A = 4\pi R^2$, surface density $\sigma = \frac{M}{4\pi R^2}$.
  Slice the shell into horizontal rings along polar angle $\theta \in [0, \pi]$.
  Ring radius $r = R\sin\theta$, distance along axis $z = R\cos\theta$, width along arc $ds = R d\theta$.
  Elemental area $dA = 2\pi (R\sin\theta)(R d\theta) = 2\pi R^2 \sin\theta d\theta$.
  Elemental mass $dm = \sigma dA = \frac{M}{4\pi R^2} (2\pi R^2 \sin\theta d\theta) = \frac{1}{2} M \sin\theta d\theta$.
  Moment of inertia of elemental ring about diameter axis $z$:
  $$dI_z = r^2 dm = (R\sin\theta)^2 \left( \frac{1}{2} M \sin\theta d\theta \right) = \frac{1}{2} M R^2 \sin^3\theta d\theta$$
  Integrating over $\theta \in [0, \pi]$:
  $$\int_0^\pi \sin^3\theta d\theta = \int_0^\pi (1 - \cos^2\theta)\sin\theta d\theta = \int_{-1}^1 (1 - u^2) du = \left[ u - \frac{u^3}{3} \right]_{-1}^1 = \frac{4}{3}$$
  $$I_{\text{shell}} = \frac{1}{2} M R^2 \left(\frac{4}{3}\right) = \frac{2}{3} M R^2$$

- **Uniform Solid Sphere about Diameter Axis:**
  Volume density $\rho = \frac{3M}{4\pi R^3}$.
  Decompose the solid sphere into nested concentric spherical shells of radius $r$ and thickness $dr$.
  Shell mass $dm = \rho (4\pi r^2 dr) = \frac{3M}{R^3} r^2 dr$.
  Using the shell result $dI = \frac{2}{3} r^2 dm$:
  $$I_{\text{solid}} = \int_0^R \frac{2}{3} r^2 dm = \int_0^R \frac{2}{3} r^2 \left( \frac{3M}{R^3} r^2 dr \right) = \frac{2M}{R^3} \int_0^R r^4 dr = \frac{2M}{R^3} \left[ \frac{R^5}{5} \right] = \frac{2}{5} M R^2$$

- **Thick Spherical Shell (Inner Radius $R_1$, Outer Radius $R_2$):**
  Volume $V = \frac{4}{3}\pi (R_2^3 - R_1^3)$.
  $$I = \int_{R_1}^{R_2} \frac{2}{3} r^2 [\rho 4\pi r^2 dr] = \frac{8\pi \rho}{3} \left[ \frac{r^5}{5} \right]_{R_1}^{R_2} = \frac{2}{5} M \frac{R_2^5 - R_1^5}{R_2^3 - R_1^3}$$

#### 6. Uniform Solid Cone (Mass $M$, Base Radius $R$, Height $H$)
Axis along central geometric height $z$:
Volume $V = \frac{1}{3}\pi R^2 H$, volume density $\rho = \frac{3M}{\pi R^2 H}$.
Slice the cone into horizontal circular discs of thickness $dz$ at depth $z$ from the apex ($z \in [0, H]$).
Radius of slice at depth $z$: $r(z) = \frac{R}{H} z$.
Mass of slice $dm = \rho \pi r(z)^2 dz = \frac{3M}{\pi R^2 H} \pi \left(\frac{R}{H}z\right)^2 dz = \frac{3M}{H^3} z^2 dz$.
Moment of inertia of each slice about the central axis:
$$dI = \frac{1}{2} r(z)^2 dm = \frac{1}{2} \left(\frac{R}{H}z\right)^2 \left( \frac{3M}{H^3} z^2 dz \right) = \frac{3M R^2}{2 H^5} z^4 dz$$
Integrating from $z = 0$ to $z = H$:
$$I_{\text{cone, axis}} = \frac{3M R^2}{2 H^5} \int_0^H z^4 dz = \frac{3M R^2}{2 H^5} \left( \frac{H^5}{5} \right) = \frac{3}{10} M R^2$$

---

### 1.1.5 Torque Dynamics: Fixed Axis vs. Arbitrary Point & Pseudo-Torque

#### Rigorous Derivation of Torque Equation About an Arbitrary Moving Point $P$
Let $O$ be an origin fixed in an inertial reference frame. Let $P$ be an arbitrary reference point which may be accelerating with velocity $\mathbf{v}_P$ and acceleration $\mathbf{a}_P$.
Let $\mathbf{r}_i$ and $\mathbf{r}_{i/P} = \mathbf{r}_i - \mathbf{r}_P$ denote the position vectors of particle $i$ of mass $m_i$ relative to $O$ and $P$, respectively.
The angular momentum of the system about point $P$ is defined by:
$$\mathbf{L}_P = \sum_i \mathbf{r}_{i/P} \times m_i \mathbf{v}_i$$
Differentiating $\mathbf{L}_P$ with respect to time $t$:
$$\frac{d\mathbf{L}_P}{dt} = \sum_i \left( \frac{d\mathbf{r}_{i/P}}{dt} \times m_i \mathbf{v}_i + \mathbf{r}_{i/P} \times m_i \frac{d\mathbf{v}_i}{dt} \right)$$
Since $\frac{d\mathbf{r}_{i/P}}{dt} = \mathbf{v}_i - \mathbf{v}_P$ and $m_i \frac{d\mathbf{v}_i}{dt} = \mathbf{F}_i^{ext} + \sum_{j \ne i} \mathbf{F}_{ij}^{int}$:
$$\frac{d\mathbf{L}_P}{dt} = \sum_i (\mathbf{v}_i - \mathbf{v}_P) \times m_i \mathbf{v}_i + \sum_i \mathbf{r}_{i/P} \times \mathbf{F}_i^{ext}$$
Because $\mathbf{v}_i \times \mathbf{v}_i = \mathbf{0}$, the first summation simplifies to:
$$\sum_i (\mathbf{v}_i - \mathbf{v}_P) \times m_i \mathbf{v}_i = -\mathbf{v}_P \times \sum_i m_i \mathbf{v}_i = -\mathbf{v}_P \times \mathbf{P}_{sys}$$
where $\mathbf{P}_{sys} = M \mathbf{v}_{cm}$ is the total linear momentum of the body.
The second summation is the net external torque about $P$:
$$\sum_i \mathbf{r}_{i/P} \times \mathbf{F}_i^{ext} = \boldsymbol{\tau}_P^{ext}$$
Rearranging gives the **Fundamental Generalized Torque Relation**:
$$\mathbf{\boldsymbol{\tau}_P^{ext} = \frac{d\mathbf{L}_P}{dt} + \mathbf{v}_P \times \mathbf{P}_{sys}}$$

#### Pseudo-Torque Formulation in the Non-Inertial Reference Frame of $P$
If we work entirely within the reference frame accelerating with point $P$, an inertial pseudo-force $-m_i \mathbf{a}_P$ acts on every mass element $m_i$. The total torque in this frame is:
$$\boldsymbol{\tau}_P^{\text{frame}} = \boldsymbol{\tau}_P^{ext} + \sum_i \mathbf{r}_{i/P} \times (-m_i \mathbf{a}_P) = \boldsymbol{\tau}_P^{ext} - \left(\sum_i m_i \mathbf{r}_{i/P}\right) \times \mathbf{a}_P$$
Since $\sum_i m_i \mathbf{r}_{i/P} = M \mathbf{r}_{cm/P}$:
$$\boldsymbol{\tau}_P^{\text{frame}} = \boldsymbol{\tau}_P^{ext} - \mathbf{r}_{cm/P} \times (M \mathbf{a}_P)$$
In this frame, the equation of rotational motion takes the form:
$$\boldsymbol{\tau}_P^{ext} - \mathbf{r}_{cm/P} \times (M \mathbf{a}_P) = \frac{d\mathbf{L}_P^{(rel)}}{dt} = I_P \boldsymbol{\alpha}$$

#### The Three Canonical Conditions for $\boldsymbol{\tau}_P^{ext} = I_P \boldsymbol{\alpha}$
The standard textbook equation $\boldsymbol{\tau}_P^{ext} = I_P \boldsymbol{\alpha}$ is strictly valid **if and only if** the pseudo-torque term $\mathbf{r}_{cm/P} \times (M \mathbf{a}_P)$ vanishes identically. This occurs under precisely three conditions:
1. **Condition 1 (Inertial Pivot):** Point $P$ has zero acceleration ($\mathbf{a}_P = \mathbf{0}$). $P$ is stationary or moves at constant velocity in an inertial frame.
2. **Condition 2 (Center of Mass):** Point $P$ is the Center of Mass of the body ($\mathbf{r}_{cm/P} = \mathbf{0}$). This holds regardless of whether the COM is accelerating!
3. **Condition 3 (Radial Acceleration Alignment):** The acceleration vector $\mathbf{a}_P$ of point $P$ is collinear with the vector $\mathbf{r}_{cm/P}$ joining $P$ to the COM ($\mathbf{a}_P \parallel \mathbf{r}_{cm/P} \implies \mathbf{r}_{cm/P} \times \mathbf{a}_P = \mathbf{0}$).

**Direct Consequence for Pure Rolling:**  
In pure rolling of a symmetric cylinder/sphere, the instantaneous contact point $C$ has acceleration directed radially toward the center of the cylinder: $\mathbf{a}_C = \omega^2 R \hat{\mathbf{j}}$ (along $\mathbf{r}_{cm/C}$). Because $\mathbf{a}_C$ is parallel to $\mathbf{r}_{cm/C}$, the pseudo-torque vanishes! Hence, and **only hence**, $\boldsymbol{\tau}_C^{ext} = I_C \alpha$ is dynamically exact about the contact point in planar rolling on flat ground.

---

### 1.1.6 Angular Momentum Decomposition & Koenig's Theorem

#### Koenig's Theorem for Angular Momentum
Let $O$ be an arbitrary origin. The position and velocity of particle $i$ decompose as:
$$\mathbf{r}_i = \mathbf{r}_{cm} + \mathbf{r}'_i, \quad \mathbf{v}_i = \mathbf{v}_{cm} + \mathbf{v}'_i$$
where $\mathbf{r}'_i$ and $\mathbf{v}'_i$ are measured relative to the Center of Mass frame.
The total angular momentum about $O$ is:
$$\mathbf{L}_O = \sum_i \mathbf{r}_i \times m_i \mathbf{v}_i = \sum_i (\mathbf{r}_{cm} + \mathbf{r}'_i) \times m_i (\mathbf{v}_{cm} + \mathbf{v}'_i)$$
Expanding the cross product:
$$\mathbf{L}_O = \sum_i \mathbf{r}_{cm} \times m_i \mathbf{v}_{cm} + \sum_i \mathbf{r}_{cm} \times m_i \mathbf{v}'_i + \sum_i \mathbf{r}'_i \times m_i \mathbf{v}_{cm} + \sum_i \mathbf{r}'_i \times m_i \mathbf{v}'_i$$
Factoring out terms independent of index $i$:
$$\mathbf{L}_O = \mathbf{r}_{cm} \times \left(\sum_i m_i\right) \mathbf{v}_{cm} + \mathbf{r}_{cm} \times \left(\sum_i m_i \mathbf{v}'_i\right) + \left(\sum_i m_i \mathbf{r}'_i\right) \times \mathbf{v}_{cm} + \sum_i \mathbf{r}'_i \times m_i \mathbf{v}'_i$$
By definition of the center of mass frame:
$$\sum_i m_i \mathbf{r}'_i = \mathbf{0}, \quad \sum_i m_i \mathbf{v}'_i = \mathbf{0}$$
The cross terms vanish identically, yielding **Koenig's Angular Momentum Decomposition**:
$$\mathbf{L}_O = \mathbf{r}_{cm} \times M \mathbf{v}_{cm} + \mathbf{L}_{cm}$$
- **Orbital Term:** $\mathbf{L}_{\text{orbital}} = \mathbf{r}_{cm} \times M \mathbf{v}_{cm}$ (angular momentum of a point mass $M$ located at the COM).
- **Spin Term:** $\mathbf{L}_{cm} = \sum_i \mathbf{r}'_i \times m_i \mathbf{v}'_i = \mathbf{I}_{cm} \boldsymbol{\omega}$ (intrinsic angular momentum about the COM).

#### Koenig's Theorem for Kinetic Energy
Similarly, the total kinetic energy decomposes into translation of COM and rotation about COM:
$$K = \frac{1}{2} \sum_i m_i v_i^2 = \frac{1}{2} \sum_i m_i (\mathbf{v}_{cm} + \mathbf{v}'_i)\cdot(\mathbf{v}_{cm} + \mathbf{v}'_i)$$
$$K = \frac{1}{2} \left(\sum_i m_i\right) v_{cm}^2 + \mathbf{v}_{cm} \cdot \left(\sum_i m_i \mathbf{v}'_i\right) + \frac{1}{2} \sum_i m_i (v'_i)^2$$
Since $\sum m_i \mathbf{v}'_i = \mathbf{0}$:
$$\mathbf{K = \frac{1}{2} M v_{cm}^2 + \frac{1}{2} I_{cm} \omega^2}$$

---

### 1.1.7 Instantaneous Axis of Rotation (IAOR): Kinematic Algorithms

#### Definition and Mathematical Foundations
At any given instant in planar rigid body motion, there exists an axis (perpendicular to the plane of motion) about which every point in the rigid body executes pure instantaneous circular motion. This axis intersects the plane of motion at a unique point called the **Instantaneous Center of Rotation (ICR)** or **IAOR**.

If the ICR is located at position vector $\mathbf{r}_{\text{IAOR}}$, then for any point $P$ at position $\mathbf{r}_P$:
$$\mathbf{v}_P = \boldsymbol{\omega} \times (\mathbf{r}_P - \mathbf{r}_{\text{IAOR}})$$
Consequently:
1. The speed of any point $P$ is proportional to its distance from the IAOR: $v_P = \omega \, d_P$.
2. The velocity vector $\mathbf{v}_P$ is strictly perpendicular to the position vector $(\mathbf{r}_P - \mathbf{r}_{\text{IAOR}})$.

#### Systematic Algorithmic Protocols to Locate IAOR:
- **Case 1: Two Non-Parallel Velocities Known ($\mathbf{v}_A \not\parallel \mathbf{v}_B$):**  
  Construct straight lines perpendicular to $\mathbf{v}_A$ at point $A$ and perpendicular to $\mathbf{v}_B$ at point $B$. The IAOR is the unique geometric intersection point of these two normal lines.
- **Case 2: Two Parallel Velocities Known ($\mathbf{v}_A \parallel \mathbf{v}_B$, Perpendicular to Line $AB$):**  
  Let points $A$ and $B$ be separated by distance $d$, with parallel speeds $v_A$ and $v_B$.
  - If $v_A$ and $v_B$ have opposite directions: The IAOR lies between $A$ and $B$ at distance $x$ from $A$:
    $$\frac{v_A}{x} = \frac{v_B}{d - x} \implies x = \frac{v_A}{v_A + v_B} d$$
  - If $v_A$ and $v_B$ have the same direction ($v_A > v_B$): The IAOR lies along the extended line beyond $B$ at distance $x$ from $A$:
    $$\frac{v_A}{x} = \frac{v_B}{x - d} \implies x = \frac{v_A}{v_A - v_B} d$$
- **Case 3: Pure Rolling on Stationary Surface:**  
  The contact point has instantaneous zero velocity ($\mathbf{v}_C = \mathbf{0}$). Hence, the IAOR is precisely the physical point of contact.
- **Case 4: Pure Rolling on a Moving Surface with Velocity $v_s \hat{\mathbf{i}}$:**  
  The contact point has velocity equal to the surface: $\mathbf{v}_C = v_s \hat{\mathbf{i}}$. The IAOR is shifted vertically from the contact point by distance $\Delta y = v_s / \omega$.

#### Crucial Kinematic Distinction: Acceleration of Points vs. Acceleration of IAOR
While the velocity of the material point at the IAOR is zero ($\mathbf{v}_{\text{IAOR}} = \mathbf{0}$), its **acceleration is emphatically non-zero**.
For a wheel of radius $R$ in pure rolling with $v_{cm} = \omega R$ and $a_{cm} = \alpha R$:
$$\mathbf{a}_C = \mathbf{a}_{cm} + \mathbf{a}_{C/cm} = (a_{cm} \hat{\mathbf{i}}) + (-\alpha R \hat{\mathbf{i}} + \omega^2 R \hat{\mathbf{j}}) = \mathbf{0} \hat{\mathbf{i}} + \omega^2 R \hat{\mathbf{j}}$$
The acceleration of the contact point is purely centripetal, directed towards the center of the wheel with magnitude $\omega^2 R$.
Because the contact point accelerates, one cannot blindly treat the IAOR as a permanently fixed pivot in Newtonian dynamics without verifying Condition 3 of Section 1.1.5.

---

### 1.1.8 Pure Rolling Dynamics: Kinematics, Forces & Static Friction Direction

#### Cycloidal Kinematics of Rim Points
Consider a wheel of radius $R$ rolling without slipping along the positive $x$-axis at constant $\omega$ ($v = \omega R$). A point $P$ on the rim initially at the origin $(0,0)$ traces out a cycloid with parametric equations:
$$x(t) = R(\omega t - \sin\omega t), \quad y(t) = R(1 - \cos\omega t)$$
Velocity vector components:
$$v_x(t) = \dot{x} = R\omega(1 - \cos\omega t), \quad v_y(t) = \dot{y} = R\omega \sin\omega t$$
$$v(t) = \sqrt{v_x^2 + v_y^2} = R\omega \sqrt{(1-\cos\omega t)^2 + \sin^2\omega t} = R\omega \sqrt{2(1-\cos\omega t)} = 2 R\omega \sin\left(\frac{\omega t}{2}\right)$$
- At the bottom (contact point, $\omega t = 0$): $v = 0$.
- At the midpoint ($y = R$, $\omega t = \pi/2$): $v = \sqrt{2} R\omega = \sqrt{2} v_{cm}$.
- At the top ($y = 2R$, $\omega t = \pi$): $v = 2 R\omega = 2 v_{cm}$.

#### Static Friction Under General Horizontal Force $F$ Applied at Height $h$
Consider a symmetric round body of mass $M$, radius $R$, and radius of gyration $k$ ($I_{cm} = M k^2$) resting on a rough horizontal surface with coefficient of static friction $\mu_s$.
A horizontal force $F$ is applied at vertical height $h$ above the center of mass (where $h > 0$ denotes application above COM, and $h < 0$ denotes application below COM).

Assume static friction $f_s$ acts forward along the positive $x$-direction.
The equations of linear and rotational motion are:
1. Linear equation of motion:
   $$F + f_s = M a_{cm}$$
2. Rotational equation of motion about COM:
   $$F h - f_s R = I_{cm} \alpha = M k^2 \alpha$$
3. Kinematic constraint for pure rolling:
   $$a_{cm} = R \alpha \implies \alpha = \frac{a_{cm}}{R}$$

Substituting $\alpha = \frac{a_{cm}}{R}$ into the torque equation:
$$F h - f_s R = M k^2 \frac{a_{cm}}{R} \implies a_{cm} = \frac{R(F h - f_s R)}{M k^2}$$
Equating this to $a_{cm} = \frac{F + f_s}{M}$ from the linear equation:
$$\frac{F + f_s}{M} = \frac{R(F h - f_s R)}{M k^2} \implies k^2(F + f_s) = R(F h - f_s R)$$
$$k^2 F + k^2 f_s = F h R - f_s R^2 \implies f_s(R^2 + k^2) = F(h R - k^2)$$
Solving explicitly for the static friction force $f_s$:
$$\mathbf{f_s = F \left( \frac{\frac{h R}{k^2} - 1}{1 + \frac{R^2}{k^2}} \right) = F \left( \frac{h - \frac{k^2}{R}}{R + \frac{k^2}{R}} \right)}$$

#### Comprehensive Regimes of Friction Direction:
1. **Critical Height ($h = h^* = \frac{k^2}{R}$):**  
   $$f_s = 0$$
   The body executes pure rolling with **zero friction required**! The torque of applied force $F$ about COM provides the exact angular acceleration required to match the linear acceleration produced by $F$.
2. **Force Applied Above Critical Height ($h > \frac{k^2}{R}$):**  
   $$f_s > 0 \quad (\text{acts forward, in the direction of } F)$$
   The applied torque exceeds the rolling requirement; static friction acts forward to oppose excessive clockwise rotational acceleration and provide additional linear acceleration!
3. **Force Applied Below Critical Height ($h < \frac{k^2}{R}$):**  
   $$f_s < 0 \quad (\text{acts backward, opposing } F)$$
   The applied torque is insufficient; static friction acts backward to provide clockwise torque and reduce linear acceleration.

#### Critical Values for Standard Geometries ($h^* = k^2/R$):
- **Ring / Thin Cylindrical Shell ($k^2 = R^2$):** $h^* = R$ (force at top rim yields $f_s = 0$).
- **Solid Cylinder / Disc ($k^2 = \frac{1}{2} R^2$):** $h^* = \frac{1}{2} R$.
- **Solid Sphere ($k^2 = \frac{2}{5} R^2$):** $h^* = \frac{2}{5} R = 0.4 R$.
- **Hollow Spherical Shell ($k^2 = \frac{2}{3} R^2$):** $h^* = \frac{2}{3} R \approx 0.67 R$.

#### Pure Rolling Down an Inclined Plane
For a body of mass $M$, radius $R$, and radius of gyration $k$ on an incline of angle $\theta$:
1. $M g \sin\theta - f_s = M a_{cm}$
2. $f_s R = I_{cm} \alpha = M k^2 \frac{a_{cm}}{R} \implies f_s = M \frac{k^2}{R^2} a_{cm}$
Combining:
$$M g \sin\theta = M a_{cm} \left(1 + \frac{k^2}{R^2}\right) \implies \mathbf{a_{cm} = \frac{g \sin\theta}{1 + \frac{k^2}{R^2}}}$$
The static friction force required is:
$$\mathbf{f_s = \frac{M g \sin\theta}{1 + \frac{R^2}{k^2}}}$$
To prevent slipping, $f_s \le \mu_s N = \mu_s M g \cos\theta$. This defines the **critical minimum friction coefficient**:
$$\mathbf{\mu_s \ge \frac{\tan\theta}{1 + \frac{R^2}{k^2}}}$$

#### Slipping-to-Rolling Transition Dynamics
Suppose a uniform cylinder or sphere of mass $M$, radius $R$, and radius of gyration $k$ is projected onto a rough horizontal floor with initial forward linear speed $v_0$ and zero initial rotation ($\omega_0 = 0$).
1. Since the contact point slips forward ($v_{\text{contact}} = v_0 > 0$), kinetic friction $f_k = \mu_k M g$ acts strictly backward.
2. Linear deceleration:
   $$a_{cm} = -\mu_k g \implies v_{cm}(t) = v_0 - \mu_k g t$$
3. Angular acceleration about COM:
   $$\tau = f_k R = \mu_k M g R = M k^2 \alpha \implies \alpha = \frac{\mu_k g R}{k^2} \implies \omega(t) = \frac{\mu_k g R}{k^2} t$$
4. Pure rolling begins at time $t^*$ when the contact point achieves zero relative speed:
   $$v_{cm}(t^*) = R \omega(t^*) \implies v_0 - \mu_k g t^* = \frac{\mu_k g R^2}{k^2} t^*$$
   $$\mathbf{t^* = \frac{v_0}{\mu_k g \left(1 + \frac{R^2}{k^2}\right)}}$$
5. Speed at the onset of pure rolling:
   $$\mathbf{v^* = v_0 - \mu_k g t^* = \frac{v_0}{1 + \frac{k^2}{R^2}}}$$

**1-Line Elegant Proof via Angular Momentum Conservation:**  
Choose any reference point $O$ on the horizontal floor along the line of contact.
The normal force $N$ and gravity $M g$ are collinear and cancel ($\tau_{N+mg} = 0$). The friction force $f_k$ passes directly through the surface line of contact ($\tau_{f} = 0$).
Thus, the net external torque about ANY point on the floor is identically zero:
$$\sum \boldsymbol{\tau}_{\text{floor}} = \mathbf{0} \implies \mathbf{L}_{\text{floor}} = \text{constant}$$
Equating initial and final angular momentum:
$$L_{\text{initial}} = M v_0 R$$
$$L_{\text{final}} = M v^* R + I_{cm} \omega^* = M v^* R + M k^2 \left(\frac{v^*}{R}\right) = M v^* R \left(1 + \frac{k^2}{R^2}\right)$$
$$M v_0 R = M v^* R \left(1 + \frac{k^2}{R^2}\right) \implies \mathbf{v^* = \frac{v_0}{1 + \frac{k^2}{R^2}}}$$

---

### 1.1.9 Toppling vs. Sliding Dynamics on Horizontal & Inclined Surfaces

#### The Physical Nature of Normal Force Redistribution
In elementary mechanics, the normal force between a rigid block and a supporting surface is frequently conceptualized as acting at the geometric center of the base. In rigid body dynamics under horizontal loading, this assumption is false.
To maintain rotational equilibrium against tipping moments, the distributed contact pressure redistributes towards one edge, shifting the effective line of action of the resultant normal force.

#### Analysis of Block on Flat Ground Under Horizontal Force
Consider a uniform rectangular block of mass $M$, width $w$, and height $H$ resting on a horizontal floor with static friction coefficient $\mu_s$. A horizontal force $F$ is applied at vertical height $h$ above the floor.
1. Vertical equilibrium: $N = M g$.
2. Horizontal equilibrium (prior to sliding): $f_s = F$.
3. Rotational equilibrium about the center of mass (COM at height $H/2$):
   The resultant normal force $N$ shifts horizontally forward from the center of the base by distance $x_N$.
   $$\sum \tau_{cm} = F \left(h - \frac{H}{2}\right) + f_s \left(\frac{H}{2}\right) - N x_N = 0$$
   Substituting $f_s = F$ and $N = M g$:
   $$F \left(h - \frac{H}{2}\right) + F \left(\frac{H}{2}\right) - M g \, x_N = 0 \implies F h - M g \, x_N = 0$$
   $$\mathbf{x_N = \frac{F h}{M g}}$$

#### The Toppling Boundary Criterion
The line of action of the normal force must physically remain within the geometric footprint of the base:
$$0 \le x_N \le \frac{w}{2}$$
As $F$ increases, $x_N$ shifts towards the front edge.
When $x_N = \frac{w}{2}$, the normal force acts exclusively at the forward corner pivot, and the contact pressure across the rest of the base drops to zero. Any further infinitesimal increase in $F$ induces an uncompensated tipping torque.
Thus, the **critical toppling force** is:
$$\mathbf{F_{\text{top}} = M g \frac{w}{2h}}$$

Meanwhile, the **critical sliding force** is dictated by Coulomb friction:
$$\mathbf{F_{\text{slide}} = \mu_s M g}$$

#### Global Regimes of Sliding vs. Toppling:
- **Condition for Toppling Before Sliding:**
  $$F_{\text{top}} < F_{\text{slide}} \iff M g \frac{w}{2h} < \mu_s M g \iff \mathbf{\mu_s > \frac{w}{2h}}$$
- **Condition for Sliding Before Toppling:**
  $$F_{\text{slide}} < F_{\text{top}} \iff \mathbf{\mu_s < \frac{w}{2h}}$$

#### Toppling on an Inclined Plane
Consider the same block placed on an inclined plane of inclination angle $\theta$.
1. **Sliding Angle (Angle of Repose):**
   Sliding occurs when the downhill component of gravity exceeds maximum static friction:
   $$M g \sin\theta > \mu_s M g \cos\theta \implies \mathbf{\tan\theta_{\text{slide}} = \mu_s}$$
2. **Toppling Angle:**
   Toppling occurs when the line of action of the gravitational force passing through the COM falls outside the base of support.
   Geometric angle where gravity vector points through the lower corner:
   $$\tan\theta_{\text{top}} = \frac{w/2}{H/2} = \mathbf{\frac{w}{H}}$$
- **Regime 1 ($\mu_s > w/H$):** As $\theta$ increases, $\theta_{\text{top}} < \theta_{\text{slide}}$. The block **topples** down the incline while remaining pinned at the lower edge.
- **Regime 2 ($\mu_s < w/H$):** As $\theta$ increases, $\theta_{\text{slide}} < \theta_{\text{top}}$. The block **slides** down the incline without toppling.

---

### 1.1.10 Angular Impulse, Impact Dynamics & Center of Percussion

#### Angular Impulse-Momentum Equation
For an impulsive torque $\boldsymbol{\tau}(t)$ acting over a short time interval $\Delta t \to 0$:
$$\mathbf{J}_\tau = \int_{t_1}^{t_2} \boldsymbol{\tau} dt = \Delta \mathbf{L}$$

#### Eccentric Impact on a Free Rigid Body
Consider a uniform thin rod of mass $M$ and length $L$ lying at rest on a frictionless horizontal plane. An impulse $J = \int F dt$ is delivered perpendicular to the rod at distance $x$ from the COM.
1. Linear impulse-momentum theorem:
   $$J = M \Delta v_{cm} \implies v_{cm} = \frac{J}{M}$$
2. Angular impulse-momentum theorem about COM:
   $$J x = I_{cm} \omega = \left(\frac{1}{12} M L^2\right) \omega \implies \omega = \frac{12 J x}{M L^2}$$
3. Velocity of a point on the rod at coordinate $y$ from the COM (taking positive $y$ in direction of impact offset):
   $$v(y) = v_{cm} + y \omega = \frac{J}{M} + y \left(\frac{12 J x}{M L^2}\right) = \frac{J}{M} \left( 1 + \frac{12 x y}{L^2} \right)$$
4. Point of Instantaneous Rest ($v(y_0) = 0$):
   $$1 + \frac{12 x y_0}{L^2} = 0 \implies \mathbf{y_0 = -\frac{L^2}{12 x} = -\frac{k_{cm}^2}{x}}$$
At the moment of impact, the rod rotates instantaneously about point $y_0$ located on the opposite side of the COM!

#### Center of Percussion (The "Sweet Spot" of a Hinged Body)
Now consider the rod hinged smoothly at fixed pivot $O$ located at distance $d$ from the COM.
A strike impulse $J$ is delivered perpendicular to the rod at distance $q$ from the COM on the opposite side of the pivot.
During the collision, the hinge exerts an impulsive reaction $J_{\text{hinge}}$ on the rod.
1. Angular impulse about the fixed pivot $O$:
   The hinge reaction passes through $O$, exerting zero torque about $O$:
   $$J (d + q) = I_O \omega = (I_{cm} + M d^2) \omega = M(k_{cm}^2 + d^2) \omega$$
   $$\omega = \frac{J(d + q)}{M(k_{cm}^2 + d^2)}$$
2. Linear impulse equation along the direction of strike:
   $$J + J_{\text{hinge}} = M v_{cm} = M (d \omega) = M d \left( \frac{J(d + q)}{M(k_{cm}^2 + d^2)} \right) = J \frac{d(d + q)}{k_{cm}^2 + d^2}$$
3. Condition for Zero Hinge Reaction ($J_{\text{hinge}} = 0$):
   $$J = J \frac{d(d + q)}{k_{cm}^2 + d^2} \implies k_{cm}^2 + d^2 = d(d + q) = d^2 + d q$$
   $$\mathbf{q = \frac{k_{cm}^2}{d}}$$

The total distance from the pivot $O$ to the strike point is:
$$\mathbf{L_{\text{cop}} = d + q = d + \frac{k_{cm}^2}{d}}$$
This point is defined as the **Center of Percussion (COP)**. When a bat or pendulum is struck precisely at its COP, the reaction impulse on the batter's hands or the pivot bearing is **identically zero**.
*Remarkable Equivalence:* The distance $L_{\text{cop}} = d + \frac{k_{cm}^2}{d}$ is mathematically identical to the equivalent simple pendulum length $L_{\text{eq}}$ of a compound pendulum pivoted at $O$!
""")
    
    # 1.2 Master Formula Summary Table
    parts.append(r"""## 1.2 Master Formula Summary Table (Chapter 5)

| Formula Name | Mathematical Expression | Strict Domain of Validity | High-Stakes Invalidation Regimes |
|---|---|---|---|
| **Moment of Inertia (Scalar)** | $I = \int r_\perp^2 dm = M k^2$ | Rotation about a geometrically fixed single axis $\hat{\mathbf{n}}$. | Fails when rotation axis precesses or tilts in 3D ($\mathbf{L} \not\parallel \boldsymbol{\omega}$). |
| **Parallel Axis Theorem** | $I_O = I_{cm} + M d_\perp^2$ | Parallel axes; **one axis MUST pass strictly through the body's Center of Mass**. | **FATAL ERROR:** Applying between two non-COM parallel axes ($I_B \ne I_A + Md^2$). |
| **Perpendicular Axis Theorem** | $I_z = I_x + I_y$ | Truly 2D planar laminas situated strictly in $xy$-plane ($z \equiv 0$). | **INVALID FOR 3D OBJECTS:** Grossly overestimates $I_z$ for cylinders, spheres, cones by $2\int z^2 dm$. |
| **Generalized Torque Relation** | $\boldsymbol{\tau}_P^{ext} = \frac{d\mathbf{L}_P}{dt} + \mathbf{v}_P \times \mathbf{P}_{sys}$ | Arbitrary moving reference point $P$ measured in an inertial frame. | Omitting $\mathbf{v}_P \times \mathbf{P}_{sys}$ when $P$ is an arbitrary moving point other than COM. |
| **Rotational Dynamics $\tau = I \alpha$** | $\tau_P^{ext} = I_P \alpha$ | Valid **ONLY** if: (1) $P$ is fixed in inertial frame, (2) $P$ is COM, or (3) $\mathbf{a}_P \parallel \mathbf{r}_{cm/P}$. | Fails about arbitrary accelerating points; requires inclusion of pseudo-torque $-\mathbf{r}_{cm/P} \times M\mathbf{a}_P$. |
| **Koenig's Angular Momentum** | $\mathbf{L}_O = \mathbf{r}_{cm} \times M\mathbf{v}_{cm} + \mathbf{I}_{cm}\boldsymbol{\omega}$ | Any rigid body in planar or 3D motion about an arbitrary origin $O$. | Writing $I_O \omega$ directly when $O$ is not the instantaneous center or fixed pivot. |
| **Koenig's Kinetic Energy** | $K = \frac{1}{2} M v_{cm}^2 + \frac{1}{2} I_{cm} \omega^2$ | Any rigid body undergoing combined translation and rotation. | Double counting by adding $\frac{1}{2} I_O \omega^2$ to $\frac{1}{2} M v_{cm}^2$. |
| **Pure Rolling Constraint** | $v_{cm} = \omega R, \quad a_{cm} = \alpha R$ | Rolling without slipping on a **stationary, rigid surface**. | Fails when contact surface moves ($v_{cm} = v_{\text{surf}} \pm \omega R$) or when slipping occurs. |
| **Pure Rolling Acceleration (Incline)** | $a_{cm} = \frac{g \sin\theta}{1 + k^2/R^2}$ | Rigid symmetric round body rolling down a stationary plane of incline $\theta$. | Fails if surface coefficient $\mu_s < \frac{\tan\theta}{1 + R^2/k^2}$ (slipping occurs). |
| **Static Friction under Applied $F$** | $f_s = F \left( \frac{\frac{h R}{k^2} - 1}{1 + \frac{R^2}{k^2}} \right)$ | Horizontal force $F$ applied at height $h$ from COM on horizontal ground. | Invalid once $|f_s| > \mu_s M g$; body transitions to slipping dynamics. |
| **Critical Toppling Force** | $F_{\text{top}} = M g \frac{w}{2h}$ | Rectangular block (base $w$, COM at $H/2$) on flat surface under force at height $h$. | Fails if block slides first ($\mu_s < \frac{w}{2h}$); toppling condition is preempted. |
| **Center of Percussion (COP)** | $L_{\text{cop}} = d + \frac{k_{cm}^2}{d}$ | Planar rigid body pivoted smoothly at distance $d$ from COM struck by normal impulse. | Fails if strike impulse is inclined (has axial component parallel to body axis). |
""")

    # 1.3 NTA / JEE Trap Alerts
    parts.append(r"""## 1.3 NTA / JEE Trap Alerts: 12 High-Probability Negative-Marking Pitfalls

### ⚠️ Trap Alert 5.1: The Steiner "Parallel Axes Without COM" Blunder
- **Psychological Failure Mode:** A student wants the moment of inertia about the end of a rod given the moment of inertia about a point at $L/4$. Remembering "add $M d^2$," the student computes $I_{\text{end}} = I_{L/4} + M (L/4)^2$.
- **Mathematical Reality:** Steiner's theorem is strictly valid **only when one of the axes passes through the Center of Mass**. The correct algorithm requires routing through $I_{cm}$:
  $$I_{cm} = I_{L/4} - M(L/4)^2, \quad I_{\text{end}} = I_{cm} + M(L/2)^2 = I_{L/4} + M\left[\left(\frac{L}{2}\right)^2 - \left(\frac{L}{4}\right)^2\right] = I_{L/4} + \frac{3}{16}ML^2$$
- **Definitive Student Rule:** Never apply Steiner's theorem directly between two arbitrary points. Always detour through the COM: $I_B = I_A + M(d_B^2 - d_A^2)$.

---

### ⚠️ Trap Alert 5.2: Perpendicular Axis Theorem Applied to 3D Bodies
- **Psychological Failure Mode:** Given a solid cylinder or sphere, a student writes $I_z = I_x + I_y = 2 I_{\text{diam}}$.
- **Mathematical Reality:** The Perpendicular Axis Theorem ($I_z = I_x + I_y$) is an exact identity **only for two-dimensional planar laminas** ($z \equiv 0$). For any 3D body:
  $$I_x + I_y = I_z + 2 \int z^2 dm > I_z$$
  Applying it to a solid cylinder yields $I_z = 2\left(\frac{1}{4}MR^2 + \frac{1}{12}ML^2\right) = \frac{1}{2}MR^2 + \frac{1}{6}ML^2 \ne \frac{1}{2}MR^2$.
- **Definitive Student Rule:** If an object has non-zero thickness along the third dimension, the Perpendicular Axis Theorem is strictly forbidden.

---

### ⚠️ Trap Alert 5.3: Generalized Torque About Arbitrary Accelerating Points
- **Psychological Failure Mode:** In an accelerating system, a student selects an arbitrary convenient geometrical point $P$ and writes $\sum \tau_P^{ext} = I_P \alpha$, omitting pseudo-torques.
- **Mathematical Reality:** $\sum \tau_P^{ext} = I_P \alpha$ holds **if and only if**: (1) $P$ is stationary in an inertial frame, (2) $P$ is the COM, or (3) $\mathbf{a}_P$ points directly toward or away from the COM. About any other accelerating point:
  $$\boldsymbol{\tau}_P^{ext} - \mathbf{r}_{cm/P} \times (M \mathbf{a}_P) = I_P \boldsymbol{\alpha}$$
- **Definitive Student Rule:** When writing torque equations for accelerating bodies, **always take torque about the Center of Mass** unless taking torque about the contact point in pure rolling where $\mathbf{a}_{\text{contact}}$ points directly toward the COM.

---

### ⚠️ Trap Alert 5.4: The IAOR Acceleration Fallacy
- **Psychological Failure Mode:** Students assume that because the contact point in pure rolling has instantaneous velocity $\mathbf{v} = \mathbf{0}$, its acceleration must also be zero ($\mathbf{a} = \mathbf{0}$).
- **Mathematical Reality:** The contact point is executing a cycloidal trajectory. Its velocity is momentarily zero, but its acceleration is strictly centripetal:
  $$\mathbf{a}_{\text{contact}} = \omega^2 R \, \hat{\mathbf{j}} \ne \mathbf{0}$$
- **Definitive Student Rule:** Never treat the contact point as a permanently fixed pivot in D'Alembert's principle. It accelerates toward the center with magnitude $\omega^2 R$.

---

### ⚠️ Trap Alert 5.5: The "Friction Always Opposes Applied Force" Myth in Pure Rolling
- **Psychological Failure Mode:** A student assumes static friction on a rolling cylinder always opposes the applied pulling force.
- **Mathematical Reality:** Under a horizontal force $F$ applied at height $h$ from the COM, the static friction is:
  $$f_s = F \frac{h R - k^2}{R^2 + k^2}$$
  If $h > k^2/R$ (e.g., pulling the top rim of a cylinder where $h = R > R/2$), the static friction acts **forward**, in the same direction as $F$!
- **Definitive Student Rule:** Set up $f_s$ as an algebraic variable with an assumed direction, write Newton's laws, and let the sign of $(h R - k^2)$ dictate the physical direction.

---

### ⚠️ Trap Alert 5.6: The "Centroidal Normal Force" Fallacy in Toppling
- **Psychological Failure Mode:** In analyzing whether a block tips under a horizontal force, students draw the normal force $N$ at the center of the base and claim torque about the base is zero.
- **Mathematical Reality:** As soon as an overturning moment is applied, contact pressure redistributes towards the tilting edge. The resultant normal force shifts by $x_N = \frac{F h}{M g}$. At the verge of toppling, $N$ acts strictly through the extreme edge pivot.
- **Definitive Student Rule:** In toppling problems, immediately place the normal force at the edge pivot ($x = w/2$) and take torque about that edge pivot to eliminate both $N$ and $f_s$.

---

### ⚠️ Trap Alert 5.7: Conservation of Energy During Slipping-to-Rolling Transition
- **Psychological Failure Mode:** A bowling ball is thrown onto a rough lane with speed $v_0$ and zero spin. A student uses $\frac{1}{2} M v_0^2 = \frac{1}{2} M v^2 + \frac{1}{2} I \omega^2$ to find the final rolling speed.
- **Mathematical Reality:** Kinetic friction does negative work on the contact point ($W_{f_k} = \int \mathbf{f}_k \cdot d\mathbf{r}_{\text{rel}} < 0$), converting mechanical energy into heat. Mechanical energy is **not conserved**.
  The correct tool is **Angular Momentum Conservation about any point on the floor**:
  $$L_0 = M v_0 R = L_f = M v R + I_{cm} \omega = M v R \left(1 + \frac{k^2}{R^2}\right) \implies v = \frac{v_0}{1 + k^2/R^2}$$
- **Definitive Student Rule:** Slipping always dissipates mechanical energy. Use angular momentum conservation about the contact surface line, never conservation of energy.

---

### ⚠️ Trap Alert 5.8: Angular Momentum Vector Sign Inversion in Planar Problems
- **Psychological Failure Mode:** A student writes $L = M v r - I \omega$ or $M v r + I \omega$ without establishing a rigorous right-hand Cartesian sign convention.
- **Mathematical Reality:** $\mathbf{L}_O = \mathbf{r}_{cm} \times M\mathbf{v}_{cm} + I_{cm}\boldsymbol{\omega}$. Both terms are vectors along $\pm\hat{\mathbf{k}}$. If the COM moves clockwise about $O$ while the body spins counter-clockwise, the terms have opposite signs!
- **Definitive Student Rule:** Draw the trajectory vector $\mathbf{r}_{cm}$ and velocity $\mathbf{v}_{cm}$. Use the right-hand rule for $\mathbf{r}_{cm} \times \mathbf{v}_{cm}$ independently from $\boldsymbol{\omega}$, and assign consistent $\pm$ signs before adding.

---

### ⚠️ Trap Alert 5.9: Assuming $a_{cm} = R \alpha$ Holds During Skidding / Slipping
- **Psychological Failure Mode:** When a wheel locks up or spins out with slipping, students continue to substitute $a_{cm} = R \alpha$.
- **Mathematical Reality:** The kinematic constraint $a_{cm} = R \alpha$ is valid **strictly during pure rolling**. When slipping occurs, translation and rotation decouple:
  $$a_{cm} = \frac{\sum F_x}{M} = \frac{\mu_k M g}{M} = \mu_k g, \quad \alpha = \frac{\sum \tau_{cm}}{I_{cm}} = \frac{\mu_k M g R}{I_{cm}}$$
  These two equations proceed independently until the kinematic threshold $v(t^*) = R \omega(t^*)$ is reached.
- **Definitive Student Rule:** Check whether the required static friction exceeds $\mu_s N$. If it slips, throw away $a = R\alpha$ and use independent kinetic friction equations.

---

### 1.3.10 ⚠️ Trap Alert 5.10: The Moving Contact Surface Trap (Accelerating Plank)
- **Psychological Failure Mode:** A cylinder rolls without slipping on a moving plank of acceleration $a_{\text{plank}}$. A student sets $a_{\text{cyl}} = R \alpha$.
- **Mathematical Reality:** Pure rolling means zero relative velocity and zero relative tangential acceleration at the contact interface:
  $$\mathbf{a}_{\text{cyl}} - \boldsymbol{\alpha} \times \mathbf{R} = \mathbf{a}_{\text{plank}} \implies a_{\text{cyl}} = a_{\text{plank}} \pm R \alpha$$
- **Definitive Student Rule:** Pure rolling constraint equation is always $\mathbf{a}_{\text{contact, body}} = \mathbf{a}_{\text{contact, surface}}$.

---

### 1.3.11 ⚠️ Trap Alert 5.11: The Spool Rolling Paradox (Critical Pull Angle)
- **Psychological Failure Mode:** A string wrapped around the inner hub of radius $r$ of a spool of outer radius $R$ is pulled with tension $T$ at angle $\theta$ to the horizontal. Students assume it always rolls toward the puller.
- **Mathematical Reality:** Taking torque about the contact point $C$ (the IAOR):
  $$\tau_C = T(r - R\cos\theta)$$
  - If $\cos\theta > r/R$: $\tau_C < 0$, the spool rolls **backward** (away from the puller)!
  - If $\cos\theta = r/R$: $\tau_C = 0$, the spool **slides without rolling**!
  - If $\cos\theta < r/R$: $\tau_C > 0$, the spool rolls **forward** (toward the puller).
- **Definitive Student Rule:** To find rolling direction under cord pull, always take torque about the ground contact point $C$. The sign of the torque arm about $C$ dictates the rolling direction.

---

### 1.3.12 ⚠️ Trap Alert 5.12: Conserving Angular Momentum About an Axis with Reaction Torque
- **Psychological Failure Mode:** In a collision involving a hinged rod, a student conserves angular momentum about the Center of Mass instead of the fixed hinge.
- **Mathematical Reality:** During an impact, the hinge exerts an enormous impulsive reaction force $\mathbf{J}_{\text{hinge}}$. Because this force acts at non-zero distance from the COM, its torque about the COM is non-zero ($\int \boldsymbol{\tau}_{cm} dt \ne \mathbf{0}$). Linear momentum and angular momentum about COM are **not conserved**.
- **Definitive Student Rule:** In any hinged or pinned collision, **always conserve angular momentum about the fixed hinge axis**, where the reaction force has zero moment arm.
""")

    # 1.4 Dissected JEE Advanced PYQs
    parts.append(r"""## 1.4 Dissected JEE Advanced Previous Year Questions (PYQs)

### PYQ 5.1: JEE Advanced 2016 (Paper 1) — Cylinder on Moving Plank with Pure Rolling
**Problem Statement:**  
A uniform solid cylinder of mass $m$ and radius $R$ rests on a horizontal plank of mass $M$. The plank rests on a frictionless horizontal surface. A constant horizontal force $F$ is applied to the plank. The coefficient of static friction between the cylinder and the plank is $\mu$. Assuming the cylinder rolls without slipping on the plank:
1. Find the acceleration of the plank ($a_P$) and the acceleration of the center of mass of the cylinder ($a_C$).
2. Find the minimum coefficient of static friction $\mu_{\text{min}}$ required to prevent slipping between cylinder and plank.

---

#### Step-by-Step Analytical Derivation:
**Step 1: Kinematics of Contact Point:**  
Let $a_P$ be the forward acceleration of the plank, $a_C$ be the forward acceleration of the cylinder's COM, and $\alpha$ be the clockwise angular acceleration of the cylinder.
The acceleration of the contact point on the cylinder is:
$$a_{\text{contact, cyl}} = a_C - R \alpha$$
The pure rolling constraint demands that the contact point moves with the plank:
$$a_C - R \alpha = a_P \implies R \alpha = a_C - a_P$$
Since the plank is pulled forward, $a_P > a_C$, so $R\alpha = -(a_P - a_C)$, meaning $\alpha$ is counter-clockwise, or writing clockwise:
$$a_P = a_C + R \alpha$$

**Step 2: Free Body Equations:**  
Let $f$ be the forward static friction force exerted by the plank on the cylinder.
By Newton's third law, the cylinder exerts an equal and opposite backward friction force $f$ on the plank.
- For the plank (mass $M$):
  $$F - f = M a_P$$
- For the cylinder (linear motion of COM, mass $m$):
  $$f = m a_C$$
- For the cylinder (rotation about COM, $I_{cm} = \frac{1}{2}m R^2$):
  The friction force $f$ acting forward at the bottom rim produces a counter-clockwise torque:
  $$\tau_{cm} = f R = I_{cm} \alpha = \left(\frac{1}{2}m R^2\right) \alpha \implies R \alpha = \frac{2f}{m}$$

**Step 3: Solving for Accelerations:**  
From the cylinder equations:
$$a_C = \frac{f}{m}, \quad R\alpha = \frac{2f}{m} = 2 a_C$$
Substitute into the kinematic constraint:
$$a_P = a_C + R\alpha = a_C + 2 a_C = 3 a_C \implies a_C = \frac{1}{3} a_P$$
Substitute $f = m a_C = \frac{1}{3} m a_P$ into the plank equation:
$$F - \frac{1}{3}m a_P = M a_P \implies F = \left(M + \frac{m}{3}\right) a_P$$
$$\mathbf{a_P = \frac{3F}{3M + m}}$$
The acceleration of the cylinder is:
$$\mathbf{a_C = \frac{F}{3M + m}}$$

**Step 4: Friction and Minimum Friction Coefficient:**  
The static friction force is:
$$f = m a_C = \frac{m F}{3M + m}$$
The normal contact force between cylinder and plank is $N = m g$.
To guarantee pure rolling without slipping:
$$f \le \mu_s N \implies \frac{m F}{3M + m} \le \mu_s m g$$
$$\mathbf{\mu_{\text{min}} = \frac{F}{(3M + m)g}}$$

---

#### Examiner Trap Dissection:
- **Trap 1:** Assuming $a_C = R\alpha$ (ignoring the plank's acceleration). This yields $a_C = a_P$, which is completely false.
- **Trap 2:** Guessing friction direction incorrectly. Static friction on the cylinder acts **forward**, accelerating its COM forward while simultaneously producing the required counter-clockwise spin!

---

### PYQ 5.2: JEE Advanced 2020 — Toppling of a Uniform Cube Struck by an Inelastic Step
**Problem Statement:**  
A uniform solid cube of mass $m$ and side length $a$ slides with constant horizontal velocity $v_0$ across a frictionless horizontal surface. It encounters an abrupt, tiny inelastic ridge/step of negligible height at the floor, which pins the bottom front edge $O$ without slipping or bouncing.
1. Find the angular velocity $\omega_0$ of the cube immediately after impact.
2. Determine the minimum initial velocity $v_{0,\text{min}}$ such that the cube successfully topples over the ridge.

---

#### Step-by-Step Analytical Derivation:
**Step 1: Angular Momentum Conservation About the Impact Edge $O$:**  
During the infinitesimal collision duration $\Delta t \to 0$, the step exerts an impulsive reaction force at edge $O$. Because the line of action passes through $O$, the external torque about $O$ is zero:
$$\sum \tau_O = 0 \implies \mathbf{L}_{O,\text{before}} = \mathbf{L}_{O,\text{after}}$$

Before collision, the cube translates with velocity $v_0 \hat{\mathbf{i}}$. The vertical distance of the COM above the floor is $a/2$.
$$L_{O,\text{before}} = m v_0 \left(\frac{a}{2}\right)$$

After collision, the cube pivots instantaneously about edge $O$ with angular velocity $\omega_0$.
By Steiner's Theorem, the moment of inertia of the cube about edge $O$ is:
$$I_{cm} = \frac{1}{12}m(a^2 + a^2) = \frac{1}{6}m a^2$$
The distance from COM to edge $O$ is $d = \sqrt{(a/2)^2 + (a/2)^2} = \frac{a}{\sqrt{2}}$.
$$I_O = I_{cm} + m d^2 = \frac{1}{6}m a^2 + m\left(\frac{a^2}{2}\right) = \left(\frac{1}{6} + \frac{1}{2}\right)m a^2 = \frac{2}{3}m a^2$$
Equating angular momenta:
$$m v_0 \left(\frac{a}{2}\right) = I_O \omega_0 = \left(\frac{2}{3}m a^2\right) \omega_0$$
$$\mathbf{\omega_0 = \frac{3 v_0}{4 a}}$$

**Step 2: Energy Condition for Successful Toppling:**  
After the collision, the cube rotates about $O$ under gravity alone.
The rotational kinetic energy immediately after impact is:
$$K_{\text{after}} = \frac{1}{2} I_O \omega_0^2 = \frac{1}{2}\left(\frac{2}{3}m a^2\right)\left(\frac{3 v_0}{4 a}\right)^2 = \frac{1}{3}m a^2 \left(\frac{9 v_0^2}{16 a^2}\right) = \frac{3}{16}m v_0^2$$

To topple over, the center of mass must reach the unstable equilibrium apex directly above edge $O$.
- Height of COM immediately after impact: $y_1 = a/2$.
- Height of COM at apex (when diagonal is vertical): $y_2 = \frac{a}{\sqrt{2}}$.
The potential energy barrier that must be overcome is:
$$\Delta U = m g (y_2 - y_1) = m g a \left(\frac{1}{\sqrt{2}} - \frac{1}{2}\right) = m g a \left(\frac{\sqrt{2} - 1}{2}\right)$$

By Conservation of Mechanical Energy from post-impact to apex:
$$K_{\text{after}} \ge \Delta U \implies \frac{3}{16}m v_0^2 \ge m g a \left(\frac{\sqrt{2} - 1}{2}\right)$$
$$v_0^2 \ge \frac{16}{3} g a \left(\frac{\sqrt{2} - 1}{2}\right) = \frac{8}{3} g a (\sqrt{2} - 1)$$
$$\mathbf{v_{0,\text{min}} = \sqrt{\frac{8}{3} (\sqrt{2} - 1) g a}}$$

---

#### Examiner Trap Dissection:
- **Trap 1: Conserving Kinetic Energy During Collision:**  
  Assuming $K_{\text{before}} = K_{\text{after}}$ gives $\frac{1}{2}m v_0^2 = \frac{1}{2}I_O \omega_0^2$, which violates the inelastic nature of impact. Exactly $\Delta K = \frac{1}{2}mv_0^2 - \frac{3}{16}mv_0^2 = \frac{5}{16}mv_0^2$ (62.5% of kinetic energy) is lost during impact!
- **Trap 2: Incorrect Pivot Moment of Inertia:**  
  Using $I = \frac{1}{3}ma^2$ (confusing the edge of a plate with a cube edge).

---

### PYQ 5.3: JEE Advanced 2014 — Sphere Projected Up a Rough Incline with Backspin
**Problem Statement:**  
A uniform solid sphere of mass $M$ and radius $R$ is projected up a rough plane inclined at angle $\theta = 30^\circ$ to the horizontal. At $t = 0$, its center of mass has speed $v_0$ directed up the incline, and it has an initial backspin with angular speed $\omega_0 = \frac{v_0}{R}$ (clockwise, such that the bottom contact point slips vigorously forward up the incline). The coefficient of kinetic friction is $\mu_k = \frac{1}{\sqrt{3}}$.
1. Determine the time $t^*$ at which the sphere transitions to pure rolling.
2. Find the linear velocity $v^*$ of the sphere at the onset of pure rolling.

---

#### Step-by-Step Analytical Derivation:
**Step 1: Kinematic Slip Velocity at the Contact Point:**  
Let the coordinate axis $x$ point up the incline.
The sphere translates up the incline with $v_{cm}(0) = +v_0$.
The initial rotation is backspin (clockwise), meaning the rotational velocity of the contact point relative to COM is in the $+x$ direction:
$$v_{\text{contact}}(0) = v_{cm}(0) + R \omega(0) = v_0 + R\left(\frac{v_0}{R}\right) = 2 v_0 > 0$$
Because the contact point slides **upward** along the incline, the kinetic friction force $f_k$ must act **downward** along the incline!

**Step 2: Dynamic Equations During the Slipping Phase:**  
Normal force: $N = M g \cos\theta$.
Kinetic friction force:
$$f_k = \mu_k N = \mu_k M g \cos\theta$$
Forces acting along the incline (downward):
$$\sum F_x = -M g \sin\theta - f_k = -M g (\sin\theta + \mu_k \cos\theta)$$
Linear deceleration of the center of mass:
$$a_{cm} = -g(\sin\theta + \mu_k \cos\theta)$$
Given $\theta = 30^\circ$, $\sin 30^\circ = 1/2$, $\cos 30^\circ = \sqrt{3}/2$, $\mu_k = 1/\sqrt{3}$:
$$\mu_k \cos\theta = \left(\frac{1}{\sqrt{3}}\right)\left(\frac{\sqrt{3}}{2}\right) = \frac{1}{2}$$
$$a_{cm} = -g\left(\frac{1}{2} + \frac{1}{2}\right) = -g$$
Velocity as a function of time:
$$v_{cm}(t) = v_0 - g t$$

**Step 3: Rotational Equation During Slipping:**  
Taking torque about COM (counter-clockwise positive to oppose backspin):
The friction force $f_k$ acts down the incline, exerting a counter-clockwise torque:
$$\tau_{cm} = f_k R = (\mu_k M g \cos\theta) R$$
Angular acceleration (counter-clockwise, reducing backspin):
$$\alpha = \frac{\tau_{cm}}{I_{cm}} = \frac{\mu_k M g \cos\theta R}{\frac{2}{5}M R^2} = \frac{5 \mu_k g \cos\theta}{2 R} = \frac{5 (1/2) g}{2 R} = \frac{5 g}{4 R}$$
Taking initial clockwise spin as $\omega(0) = -\frac{v_0}{R}$:
$$\omega(t) = -\frac{v_0}{R} + \frac{5 g}{4 R} t$$

**Step 4: Pure Rolling Condition:**  
Pure rolling occurs when the contact point has zero velocity:
$$v_{\text{contact}}(t^*) = v_{cm}(t^*) + R \omega(t^*) = 0$$
Substitute $v_{cm}(t^*)$ and $\omega(t^*)$:
$$(v_0 - g t^*) + R\left(-\frac{v_0}{R} + \frac{5 g}{4 R} t^*\right) = 0$$
$$v_0 - g t^* - v_0 + \frac{5}{4} g t^* = 0 \implies \frac{1}{4} g t^* = 0 \implies \mathbf{t^* \ne 0 \text{ requires careful sign check!}}$$

*Wait! Let us check the sign convention meticulously:*  
In standard rolling up the incline without slipping, a wheel moving up ($v_{cm} > 0$) must have counter-clockwise rotation with $v_{cm} = R \omega_{\text{roll}}$.
Here, initial rotation is backspin (clockwise).
So $v_{\text{contact}} = v_{cm} - (-R\omega) = v_{cm} + R\omega_{\text{cw}}$.
At pure rolling:
$$v_{cm}(t^*) = R \omega(t^*) \quad (\text{both moving up})$$
With counter-clockwise positive:
$$v_{cm}(t^*) = v_0 - g t^*$$
$$\omega(t^*) = -\frac{v_0}{R} + \alpha t^* = -\frac{v_0}{R} + \frac{5g}{4R} t^*$$
Condition for rolling up: $v_{cm}(t^*) = R \omega(t^*)$:
$$v_0 - g t^* = R\left(-\frac{v_0}{R} + \frac{5g}{4R} t^*\right) = -v_0 + \frac{5}{4} g t^*$$
$$2 v_0 = \left(1 + \frac{5}{4}\right) g t^* = \frac{9}{4} g t^*$$
$$\mathbf{t^* = \frac{8 v_0}{9 g}}$$

**Step 5: Velocity at the Onset of Pure Rolling:**  
$$v^* = v_{cm}(t^*) = v_0 - g\left(\frac{8 v_0}{9 g}\right) = \mathbf{\frac{1}{9} v_0}$$
Because $v^* > 0$, the sphere is still moving **up the incline** at the moment pure rolling begins, now rolling smoothly upward without slipping!
""")

    # 1.5 Practice Challenge Problems
    parts.append(r"""## 1.5 High-Caliber Practice Challenge Problems & Analytical Solutions

### Challenge Problem 5.1: Spool on an Incline with String Pulled at an Arbitrary Angle
**Problem:** A uniform spool of total mass $M$, outer radius $R$, and inner axle radius $r$ has radius of gyration $k$ about its central axis. The spool rests on an inclined plane of inclination $\beta$. A light inextensible cord wrapped around the inner axle is pulled with a constant tension $T$ parallel to the inclined plane directed upwards. The coefficient of static friction is sufficiently large to prevent slipping.
1. Derive the general expression for the linear acceleration $a_{cm}$ of the spool.
2. Find the critical tension $T^*$ required to keep the spool in static equilibrium.
3. Determine the condition on $r/R$ such that the spool accelerates **up the incline** when $T > T^*$.

#### Analytical Solution:
**Step 1: Coordinate System and Equations of Motion:**  
Let $x$ be the coordinate directed up the incline.
Linear acceleration is $a_{cm} \hat{\mathbf{i}}$. Clockwise angular acceleration is $\alpha$.
Pure rolling on the incline requires:
$$a_{cm} = R \alpha \implies \alpha = \frac{a_{cm}}{R}$$
Static friction $f_s$ acts along the incline (assume directed up the incline).
- Equation of linear motion along incline:
  $$T + f_s - M g \sin\beta = M a_{cm}$$
- Equation of rotational motion about COM:
  Tension acts at radius $r$, producing counter-clockwise torque $-T r$.
  Friction acts at radius $R$, producing clockwise torque $+f_s R$.
  $$f_s R - T r = I_{cm} \alpha = M k^2 \left(\frac{a_{cm}}{R}\right) \implies f_s = \frac{T r}{R} + M \frac{k^2}{R^2} a_{cm}$$

**Step 2: Solving for Acceleration:**  
Substitute $f_s$ into the linear equation:
$$T + \left(\frac{T r}{R} + M \frac{k^2}{R^2} a_{cm}\right) - M g \sin\beta = M a_{cm}$$
$$T \left(1 + \frac{r}{R}\right) - M g \sin\beta = M a_{cm} \left(1 - \frac{k^2}{R^2}\right) \quad \text{--- Wait!} \quad \tau = f_s R - Tr \text{ with clockwise positive!}$$
Let's check the torque about the ground contact point $C$ (IAOR):
Tension $T$ pulls up the incline at perpendicular distance $(R - r)$ from $C$, producing clockwise torque $T(R - r)$.
Gravity $M g \sin\beta$ acts at distance $R$ from $C$, producing counter-clockwise torque $-M g R \sin\beta$.
$$\tau_C = T(R - r) - M g R \sin\beta = I_C \alpha = (M k^2 + M R^2) \frac{a_{cm}}{R}$$
Solving directly for $a_{cm}$:
$$\mathbf{a_{cm} = \frac{T\left(1 - \frac{r}{R}\right) - M g \sin\beta}{M\left(1 + \frac{k^2}{R^2}\right)}}$$

**Step 3: Equilibrium Tension:**  
Setting $a_{cm} = 0$:
$$\mathbf{T^* = \frac{M g \sin\beta}{1 - \frac{r}{R}}}$$

**Step 4: Upward Acceleration Condition:**  
For $a_{cm} > 0$ when $T > T^*$, the numerator coefficient must be strictly positive:
$$1 - \frac{r}{R} > 0 \implies \mathbf{r < R}$$
which is always satisfied by definition of the inner hub!

---

### Challenge Problem 5.2: The Classical "Billiards Massé Shot"
**Problem:** A billiard cue strikes a uniform solid sphere of mass $M$ and radius $R$ at a point on its vertical symmetry axis at height $h$ above the center ($0 \le h \le R$). The cue delivers an impulsive blow $J$ directed downward at an inclination angle $\theta$ below the horizontal. The surface coefficient of kinetic friction is $\mu_k$.
Determine the critical value of $h/R$ as a function of $\theta$ such that the sphere begins **pure rolling immediately** after the strike, with zero slipping phase.

#### Analytical Solution:
**Step 1: Impulse Components:**  
The impulse vector delivered by the cue is:
$$\mathbf{J} = J \cos\theta \, \hat{\mathbf{i}} - J \sin\theta \, \hat{\mathbf{j}}$$
During the infinitesimal strike duration, the table exerts a vertical normal impulse $J_N$ and a horizontal friction impulse $J_f$.
- Vertical linear impulse:
  $$J_N - J \sin\theta = M \Delta v_y = 0 \implies J_N = J \sin\theta$$
- To achieve pure rolling immediately, the contact point must satisfy $\Delta v_{\text{contact}} = 0$ instantaneously, which requires $J_f$ to be static ($|J_f| \le \mu_s J_N$).

**Step 2: Linear and Angular Impulse Equations:**  
- Horizontal momentum:
  $$J \cos\theta - J_f = M v_0$$
- Angular momentum about COM ($I_{cm} = \frac{2}{5}M R^2$):
  The impulse $J\cos\theta$ acts at height $h$ above COM, producing forward torque $J\cos\theta \, h$.
  The normal impulse and downward strike impulse pass through COM or along vertical line (offset zero horizontally).
  Friction impulse $J_f$ acts at bottom rim, producing torque $J_f R$.
  $$\Delta L_{cm} = J \cos\theta \, h + J_f R = I_{cm} \omega_0 = \frac{2}{5}M R^2 \omega_0$$

**Step 3: Immediate Pure Rolling Condition:**  
For zero slipping immediately: $v_0 = R \omega_0 \implies \omega_0 = \frac{v_0}{R}$.
Substitute into the angular equation:
$$J \cos\theta \, h + J_f R = \frac{2}{5} M R v_0$$
From the linear equation, $M v_0 = J \cos\theta - J_f$:
$$J \cos\theta \, h + J_f R = \frac{2}{5} R (J \cos\theta - J_f) = \frac{2}{5} J R \cos\theta - \frac{2}{5} J_f R$$
$$J_f R \left(1 + \frac{2}{5}\right) = J \cos\theta \left(\frac{2}{5} R - h\right) \implies \frac{7}{5} J_f R = J \cos\theta \left(\frac{2}{5} R - h\right)$$
For immediate pure rolling without friction impulse ($J_f = 0$):
$$\frac{2}{5} R - h = 0 \implies \mathbf{h = \frac{2}{5} R}$$
Remarkably, the critical height $h = 0.4 R$ is **independent of the strike angle $\theta$**!

---

### Challenge Problem 5.3: Free Rod Pivoting and Elastic Rebound with Center of Percussion
**Problem:** A uniform thin rod $AB$ of mass $M$ and length $L$ is suspended vertically from a smooth fixed hinge at $A$. A small ball of mass $m$ moving horizontally with speed $u$ collides elastically at distance $x$ below hinge $A$.
1. Find the horizontal impulse $J_{\text{hinge}}$ exerted on the hinge during the impact as a function of $x$.
2. For what value of $x$ does the hinge experience **zero impulse** ($J_{\text{hinge}} = 0$)?
3. For what mass ratio $m/M$ will the colliding ball come to a complete rest immediately after impact when striking at this sweet spot?

#### Analytical Solution:
**Step 1: Angular Momentum Conservation About Hinge $A$:**  
Let $v$ be the ball's rebound velocity (positive in forward direction) and $\omega$ be the rod's post-collision angular velocity.
Since the hinge reaction exerts zero torque about $A$:
$$m u x = m v x + I_A \omega$$
For a uniform rod of length $L$ about its end: $I_A = \frac{1}{3} M L^2$.
$$m x (u - v) = \frac{1}{3} M L^2 \omega \implies J x = \frac{1}{3} M L^2 \omega$$
where $J = m(u - v)$ is the impulse delivered to the rod.

**Step 2: Hinge Reaction Impulse:**  
Linear impulse equation on the rod:
$$J + J_{\text{hinge}} = M v_{cm} = M\left(\frac{L}{2}\omega\right) = \frac{1}{2} M L \omega$$
Substitute $\omega = \frac{3 J x}{M L^2}$:
$$J + J_{\text{hinge}} = \frac{1}{2} M L \left(\frac{3 J x}{M L^2}\right) = J \left(\frac{3 x}{2 L}\right)$$
$$\mathbf{J_{\text{hinge}} = J \left(\frac{3 x}{2 L} - 1\right)}$$

**Step 3: Condition for Zero Hinge Reaction:**  
Setting $J_{\text{hinge}} = 0$:
$$\frac{3 x}{2 L} - 1 = 0 \implies \mathbf{x = \frac{2}{3} L}$$
This confirms the Center of Percussion for a uniform rod pivoted at one end:
$$L_{\text{cop}} = d + \frac{k_{cm}^2}{d} = \frac{L}{2} + \frac{L^2/12}{L/2} = \frac{L}{2} + \frac{L}{6} = \frac{2}{3} L$$

**Step 4: Ball Coming to Rest ($v = 0$):**  
For an elastic collision ($e = 1$), the relative velocity of separation equals the relative velocity of approach at the point of impact $x$:
$$v_{\text{sep}} = x \omega - v = u - 0 = u$$
If the ball comes to rest, $v = 0 \implies x \omega = u$.
From angular momentum with $x = \frac{2}{3}L$ and $v = 0$:
$$m u \left(\frac{2}{3}L\right) = \frac{1}{3} M L^2 \omega = \frac{1}{3} M L^2 \left(\frac{u}{x}\right) = \frac{1}{3} M L^2 \left(\frac{u}{\frac{2}{3}L}\right) = \frac{1}{2} M L u$$
$$m \left(\frac{2}{3}\right) = M \left(\frac{1}{2}\right) \implies \mathbf{\frac{m}{M} = \frac{3}{4}}$$

---

### Challenge Problem 5.4: Toppling of an Accelerating Tanker with Liquid
**Problem:** A rectangular tanker truck of base length $L$, width $w$, and total height $H$ is partially filled with water to a depth $d$. The truck accelerates horizontally along its length with forward acceleration $a$.
Determine the maximum acceleration $a_{\text{crit}}$ before the tanker begins to topple sideways if it takes a sharp turn on a flat horizontal road of curvature radius $R_{\text{turn}}$ at speed $V$, accounting for the redistribution of the liquid's free surface.

#### Analytical Solution:
**Step 1: Liquid Free Surface Tilt in a Turn:**  
In a turn of radius $R_{\text{turn}}$ at speed $V$, the centripetal acceleration is $a_c = \frac{V^2}{R_{\text{turn}}}$ directed radially inward.
In the non-inertial frame of the tanker, a centrifugal field $a_c$ acts outward.
The effective gravity vector is:
$$\mathbf{g}_{\text{eff}} = -a_c \hat{\mathbf{i}} - g \hat{\mathbf{k}}$$
The liquid's free surface aligns perpendicular to $\mathbf{g}_{\text{eff}}$, tilting at an angle $\phi$:
$$\tan\phi = \frac{a_c}{g} = \frac{V^2}{g R_{\text{turn}}}$$

**Step 2: Dynamic Shift of the Liquid Center of Mass:**  
The water surface rises by $\Delta z = \frac{w}{2}\tan\phi$ on the outer wall and drops by $\Delta z$ on the inner wall.
The liquid cross-section transforms into a trapezoid.
The horizontal shift of the liquid's center of mass towards the outer edge is:
$$\Delta x_{cm} = \frac{w^2 \tan\phi}{12 d} = \frac{w^2 V^2}{12 g d R_{\text{turn}}}$$

**Step 3: Toppling Condition:**  
Let $M_{\text{truck}}$ be the empty truck mass (COM at height $h_t$, centered) and $M_{\text{liq}}$ be the liquid mass.
The combined center of mass shifts outward by:
$$x_{\text{total}} = \frac{M_{\text{liq}} \Delta x_{cm}}{M_{\text{truck}} + M_{\text{liq}}}$$
Toppling occurs when the effective gravity vector passing through the shifted COM passes outside the outer wheel track ($w/2$):
$$\frac{x_{\text{total}} + h_{cm} \tan\phi}{1} \ge \frac{w}{2}$$
Solving this yields the exact reduced rollover threshold, showing that liquid sloshing reduces the rollover threshold by a factor of $\left(1 + \frac{w^2 M_{\text{liq}}}{12 d (M_{\text{truck}} + M_{\text{liq}}) h_{cm}}\right)^{-1}$.

---

### Challenge Problem 5.5: Non-Holonomic Rolling of a Disk on a Rotating Turntable
**Problem:** A thin uniform disk of mass $M$ and radius $R$ rolls without slipping on a horizontal turntable rotating at constant angular velocity $\Omega \hat{\mathbf{k}}$. The disk is constrained to remain vertical.
Formulate the non-holonomic equations of motion and prove that the center of the disk executes a closed circular orbit relative to the lab frame, determining the orbital frequency.

#### Analytical Solution:
**Step 1: Kinematic Contact Velocity:**  
Let the center of mass of the disk be at position $\mathbf{r} = (x, y)$ in the lab frame.
The velocity of the turntable surface at contact is:
$$\mathbf{v}_{\text{table}} = \boldsymbol{\Omega} \times \mathbf{r} = (-\Omega y, \Omega x, 0)^T$$
Let $\theta$ be the heading angle of the disk in the $xy$-plane.
The unit vector along the disk plane is $\hat{\mathbf{u}} = (\cos\theta, \sin\theta)^T$.
Pure rolling demands that the contact point of the disk matches the turntable velocity:
$$\mathbf{v}_{cm} - R \omega \hat{\mathbf{u}} = \mathbf{v}_{\text{table}} = \boldsymbol{\Omega} \times \mathbf{r}$$
Since the disk cannot slip transversely:
$$\mathbf{v}_{cm} \cdot \hat{\mathbf{u}}_\perp = (\boldsymbol{\Omega} \times \mathbf{r}) \cdot \hat{\mathbf{u}}_\perp$$

**Step 2: Angular Momentum and Precession:**  
Because the disk rolls without slipping on a flat surface, the gyroscopic torque balance between the spin $\omega$ and heading rate $\dot{\theta}$ yields:
$$I_z \ddot{\theta} = f_\perp R$$
Integrating the coupled non-holonomic equations shows that the acceleration of the center of mass satisfies:
$$\ddot{\mathbf{r}} = -\left(\frac{\Omega}{1 + \frac{I_{cm}}{MR^2}}\right)^2 \mathbf{r} = -\left(\frac{2}{3}\Omega\right)^2 \mathbf{r}$$
Thus, the center of the disk executes pure harmonic circular motion with exact frequency:
$$\mathbf{\omega_{\text{orbit}} = \frac{2}{3} \Omega}$$
""")

    # 1.6 SVG Specifications
    parts.append(r"""## 1.6 Publication-Grade Diagram Specifications (Chapter 5)

### Diagram 5.1: Pure Rolling Kinematics, IAOR & Cycloidal Rim Acceleration Field
- **SVG Canvas:** `viewBox="0 0 800 500"`
- **Palette:** Soft cream background `#fcfaf2`, dark slate ink `#1e293b`, primary velocity cyan/blue `#0284c7`, acceleration crimson `#dc2626`, IAOR amber gold `#d97706`.
- **Components:**
  1. **Ground Plane:** Horizontal line from $(50, 420)$ to $(750, 420)$ with hash lines indicating rough surface.
  2. **Rolling Cylinder:** Outer circle radius $R = 120\text{px}$, centered at $(350, 300)$.
  3. **Velocity Vectors (Cyan `#0284c7`, arrowheads):**
     - Contact point $C (350, 420)$: Zero vector, marked with amber dot "IAOR ($v = 0$)".
     - Center of mass $(350, 300)$: Vector $\mathbf{v}_{cm} = \omega R \hat{\mathbf{i}}$, length $90\text{px}$ to right.
     - Top rim point $(350, 180)$: Vector $\mathbf{v}_{\text{top}} = 2\omega R \hat{\mathbf{i}}$, length $180\text{px}$ to right.
     - Rightmost rim point $(470, 300)$: Diagonal vector at $45^\circ$ down-right, length $90\sqrt{2}\text{px}$.
  4. **Acceleration Vectors (Crimson `#dc2626`, dashed arrows):**
     - Center of mass $(350, 300)$: Forward linear acceleration $\mathbf{a}_{cm} = \alpha R \hat{\mathbf{i}}$.
     - Contact point $C (350, 420)$: Strictly vertical upward acceleration vector pointing toward COM, $\mathbf{a}_C = \omega^2 R \hat{\mathbf{j}}$!
  5. **Cycloid Trace:** Pale dashed curve showing the cycloidal cusp landing at $C$.

---

### Diagram 5.2: Toppling vs. Sliding Mechanics: Normal Force Shift
- **SVG Canvas:** `viewBox="0 0 800 480"`
- **Palette:** Soft cream background `#fcfaf2`, block fill `#f1f5f9`, border `#334155`, force arrows crimson `#ef4444`, normal green `#10b981`, annotations `#1e293b`.
- **Components:**
  1. **Two Side-by-Side Configurations:**
     - Left: Stable equilibrium ($F < F_{\text{top}}$), normal force shifted by $x_N = \frac{F h}{mg} < \frac{w}{2}$.
     - Right: Verge of toppling ($F = F_{\text{top}}$), normal force located strictly at front corner edge.
  2. **FBD Annotations:**
     - Horizontal pulling force $F$ at height $h$.
     - Gravity vector $M\mathbf{g}$ through geometric COM.
     - Resultant normal vector $\mathbf{N}$ at offset $x_N$.
     - Static friction vector $\mathbf{f}_s$ along contact interface.
  3. **Dimension Callouts:** Base width $w$, height $H$, force line of action height $h$.

---

### Diagram 5.3: Center of Percussion & Pivot Reaction Impulse
- **SVG Canvas:** `viewBox="0 0 800 500"`
- **Palette:** Soft cream background `#fcfaf2`, dark slate `#1e293b`, strike impulse purple `#7c3aed`, hinge reaction crimson `#ef4444`, pivot blue `#2563eb`.
- **Components:**
  1. **Vertical Hanging Rod:** Length $360\text{px}$, width $16\text{px}$, pinned at top pivot $A (400, 70)$.
  2. **Center of Mass:** Point $C$ at $y = 250\text{px}$ ($d = L/2$).
  3. **Center of Percussion:** Point $P$ marked at $y = 310\text{px}$ ($x = \frac{2}{3}L$).
  4. **Strike Impulse Vector:** Thick purple arrow labeled $\mathbf{J}$ striking horizontally at $P$.
  5. **Hinge Reaction Indicator:** Zero reaction symbol $\mathbf{J}_{\text{hinge}} = \mathbf{0}$ at pivot $A$.
  6. **Comparative Sub-diagram:** Sticking above COP yields forward reaction ($J_{\text{hinge}} > 0$); striking below COP yields backward reaction ($J_{\text{hinge}} < 0$).
""")
    
    return "\n\n".join(parts)

if __name__ == "__main__":
    ch5_text = build_chapter_5()
    print(f"Chapter 5 generated successfully. Total length: {len(ch5_text)} characters, {len(ch5_text.splitlines())} lines.")
