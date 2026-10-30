import os

def build_chapter_6():
    parts = []
    
    # 2.1 Theoretical Framework
    parts.append(r"""# PART 2: CHAPTER 6 — GRAVITATION & OSCILLATORY MOTION / SHM

## 2.1 Comprehensive Theoretical Foundations & Calculus Derivations

### 2.1.1 Newton's Law of Gravitation & Gravitational Fields of Extended Bodies
Newton's Universal Law of Gravitation asserts that every point mass $m_1$ attracts every other point mass $m_2$ with a central, attractive, conservative force directed along the line joining them:
$$\mathbf{F}_{12} = -G \frac{m_1 m_2}{r^2} \hat{\mathbf{r}}_{12} = -G \frac{m_1 m_2}{|\mathbf{r}_2 - \mathbf{r}_1|^3} (\mathbf{r}_2 - \mathbf{r}_1)$$
where $G = 6.67430 \times 10^{-11} \, \text{N}\cdot\text{m}^2/\text{kg}^2$ is the universal gravitational constant.

#### Gravitational Field Intensity $\mathbf{g}$ and Potential $V$
The gravitational field intensity $\mathbf{g}(\mathbf{r})$ is the gravitational force per unit test mass:
$$\mathbf{g}(\mathbf{r}) = \frac{\mathbf{F}}{m_{\text{test}}} = -\nabla V(\mathbf{r})$$
Because the gravitational force field is irrotational ($\nabla \times \mathbf{g} = \mathbf{0}$), there exists a scalar potential field $V(\mathbf{r})$ defined with reference to infinity ($V(\infty) = 0$):
$$V(\mathbf{r}) = -\int_\infty^\mathbf{r} \mathbf{g} \cdot d\mathbf{r}'$$
For a point mass $M$:
$$\mathbf{g}(\mathbf{r}) = -\frac{GM}{r^2} \hat{\mathbf{r}}, \quad V(r) = -\frac{GM}{r}$$

#### Gauss's Law for Gravitation & Poisson's Equation
Integrating the gravitational flux through a closed Gaussian surface $S$:
$$\Phi_g = \oint_S \mathbf{g} \cdot d\mathbf{A} = -4\pi G M_{\text{enclosed}} = -4\pi G \int_V \rho(\mathbf{r}) dV$$
Applying Gauss's Divergence Theorem $\oint_S \mathbf{g} \cdot d\mathbf{A} = \int_V (\nabla \cdot \mathbf{g}) dV$:
$$\nabla \cdot \mathbf{g} = -4\pi G \rho(\mathbf{r})$$
Substituting $\mathbf{g} = -\nabla V$ yields **Poisson's Equation for Gravitation**:
$$\nabla^2 V(\mathbf{r}) = 4\pi G \rho(\mathbf{r})$$
In vacuum regions ($\rho = 0$), this reduces to Laplace's equation $\nabla^2 V = 0$.

---

### 2.1.2 Gravitational Potential & Field of Shells, Solid Spheres, Rings & Discs

#### 1. Thin Spherical Shell of Mass $M$ and Radius $R$
Surface density $\sigma = \frac{M}{4\pi R^2}$. Consider a point $P$ at distance $r$ from the shell center.
Slice the shell into elemental rings perpendicular to the axis connecting the center and $P$, parameterized by polar angle $\theta \in [0, \pi]$.
Ring radius $a = R\sin\theta$, ring area $dA = 2\pi R^2 \sin\theta d\theta$, ring mass $dm = \frac{M}{2}\sin\theta d\theta$.
Every point on this elemental ring is at the same Euclidean distance $s$ from $P$, where by the Law of Cosines:
$$s^2 = R^2 + r^2 - 2 R r \cos\theta \implies 2 s \, ds = 2 R r \sin\theta d\theta \implies \sin\theta d\theta = \frac{s \, ds}{R r}$$
The elemental gravitational potential at $P$ due to the ring is:
$$dV = -\frac{G dm}{s} = -\frac{G}{s} \left(\frac{M}{2}\sin\theta d\theta\right) = -\frac{GM}{2 R r} ds$$
Integrating from minimum distance $s_{\text{min}} = |r - R|$ to maximum distance $s_{\text{max}} = r + R$:
$$V(r) = -\frac{GM}{2 R r} \int_{|r-R|}^{r+R} ds = -\frac{GM}{2 R r} \left[ (r + R) - |r - R| \right]$$

- **Interior Point ($r < R$):** $|r - R| = R - r$.
  $$V_{\text{in}}(r) = -\frac{GM}{2 R r} \left[ (r + R) - (R - r) \right] = -\frac{GM}{2 R r} [2r] = \mathbf{-\frac{GM}{R} = \text{constant}}$$
  $$\mathbf{g_{\text{in}}(r) = -\frac{dV_{\text{in}}}{dr} = \mathbf{0}}$$
  *Newton's First Shell Theorem:* A uniform spherical shell of matter attracts no particle that is within the interior of the shell.
- **Exterior Point ($r \ge R$):** $|r - R| = r - R$.
  $$V_{\text{out}}(r) = -\frac{GM}{2 R r} \left[ (r + R) - (r - R) \right] = -\frac{GM}{2 R r} [2R] = \mathbf{-\frac{GM}{r}}$$
  $$\mathbf{g_{\text{out}}(r) = -\frac{dV_{\text{out}}}{dr} = -\frac{GM}{r^2} \hat{\mathbf{r}}}$$
  *Newton's Second Shell Theorem:* A uniform spherical shell attracts an exterior particle as if the whole mass of the shell were concentrated at its center.

#### 2. Uniform Solid Sphere of Mass $M$ and Radius $R$
Volume density $\rho = \frac{3M}{4\pi R^3}$.
- **Exterior Point ($r \ge R$):**
  Applying the shell theorem to concentric shells, the exterior field and potential behave identically to a point mass:
  $$\mathbf{g_{\text{out}}(r) = -\frac{GM}{r^2} \hat{\mathbf{r}}}, \quad \mathbf{V_{\text{out}}(r) = -\frac{GM}{r}}$$
- **Interior Point ($r \le R$):**
  By Gauss's Law on a concentric sphere of radius $r$:
  $$g(r) (4\pi r^2) = -4\pi G M_{\text{enclosed}}(r)$$
  Since $M_{\text{enclosed}}(r) = \rho \left(\frac{4}{3}\pi r^3\right) = M \left(\frac{r^3}{R^3}\right)$:
  $$g(r) (4\pi r^2) = -4\pi G M \frac{r^3}{R^3} \implies \mathbf{\mathbf{g}_{\text{in}}(r) = -\frac{GM}{R^3} r \, \hat{\mathbf{r}}}$$
  To find the interior potential $V_{\text{in}}(r)$:
  $$V_{\text{in}}(r) - V(R) = -\int_R^r g(r') dr' = -\int_R^r \left(-\frac{GM}{R^3} r'\right) dr' = \frac{GM}{R^3} \left[ \frac{r^2 - R^2}{2} \right]$$
  Since $V(R) = -\frac{GM}{R}$:
  $$V_{\text{in}}(r) = -\frac{GM}{R} + \frac{GM}{2R^3}(r^2 - R^2) = \mathbf{-\frac{GM}{2R^3} (3R^2 - r^2)}$$
  At the exact center ($r = 0$):
  $$\mathbf{V_{\text{center}} = -\frac{3}{2} \frac{GM}{R} = 1.5 \, V_{\text{surface}}}$$

#### 3. Particle Motion in a Tunnel Through the Earth
Consider a straight tunnel drilled through a uniform planet of mass $M$ and radius $R$ along an arbitrary chord at perpendicular distance $d$ from the planet's center.
Let $x$ denote the displacement of a particle of mass $m$ along the tunnel measured from the tunnel midpoint.
The distance from the planet's center is $r = \sqrt{x^2 + d^2}$.
The interior gravitational field is $\mathbf{g} = -\frac{GM}{R^3} \mathbf{r}$.
The component of gravitational force along the tunnel axis ($x$-direction) is:
$$F_x = m (\mathbf{g} \cdot \hat{\mathbf{x}}) = -m \frac{GM}{R^3} r \left(\frac{x}{r}\right) = -\frac{GMm}{R^3} x$$
Remarkably, the transverse distance $d$ completely cancels out!
The equation of motion along the tunnel is:
$$m \ddot{x} = -\frac{GMm}{R^3} x \implies \ddot{x} + \left(\frac{GM}{R^3}\right) x = 0$$
This is pure Simple Harmonic Motion with angular frequency:
$$\mathbf{\omega = \sqrt{\frac{GM}{R^3}} = \sqrt{\frac{g}{R}}}$$
The oscillation period is completely independent of the chord chosen:
$$\mathbf{T = 2\pi \sqrt{\frac{R}{g}} \approx 84.6 \, \text{minutes}}$$

#### 4. Thin Uniform Circular Ring of Mass $M$ and Radius $R$ on Axial Line
For a point on the axis at distance $x$ from the ring center:
Every mass element $dm$ is at distance $s = \sqrt{R^2 + x^2}$.
- Gravitational Potential:
  $$\mathbf{V(x) = -\frac{GM}{\sqrt{R^2 + x^2}}}$$
- Gravitational Field:
  $$\mathbf{g_x(x) = -\frac{dV}{dx} = -\frac{GM x}{(R^2 + x^2)^{3/2}}}$$
- **Field Extremum:**
  To find where field magnitude is maximized:
  $$\frac{dg_x}{dx} = -GM \frac{(R^2 + x^2)^{3/2} - x \cdot \frac{3}{2}(R^2 + x^2)^{1/2}(2x)}{(R^2 + x^2)^3} = 0$$
  $$(R^2 + x^2) - 3x^2 = 0 \implies R^2 = 2x^2 \implies \mathbf{x = \frac{R}{\sqrt{2}}}$$
  $$\mathbf{g_{\text{max}} = \frac{2 GM}{3\sqrt{3} R^2}}$$

#### 5. Uniform Thin Circular Disc of Mass $M$, Radius $R$, Surface Density $\sigma = \frac{M}{\pi R^2}$
Divide the disc into concentric rings of radius $r$, thickness $dr$, mass $dm = \sigma 2\pi r dr$.
Potential at axial distance $x$:
$$V(x) = -\int_0^R \frac{G (\sigma 2\pi r dr)}{\sqrt{r^2 + x^2}} = -2\pi G \sigma \left[ \sqrt{r^2 + x^2} \right]_0^R = \mathbf{-2\pi G \sigma \left( \sqrt{R^2 + x^2} - x \right)}$$
Gravitational field along axis:
$$\mathbf{g_x(x) = -\frac{dV}{dx} = -2\pi G \sigma \left( 1 - \frac{x}{\sqrt{R^2 + x^2}} \right)}$$
As $R \to \infty$ (infinite sheet): $g = -2\pi G \sigma = \text{constant}$.

---

### 2.1.3 Gravitational Self-Energy of Continuous Spherical Bodies

#### Definition of Gravitational Self-Energy
The gravitational self-energy $U_{\text{self}}$ of a mass distribution is defined as the total work done by an external agent against the mutual gravitational forces to assemble the body from infinitesimal mass elements initially dispersed at infinite separation:
$$U_{\text{self}} = \frac{1}{2} \int_V \rho(\mathbf{r}) V(\mathbf{r}) dV = -\frac{1}{8\pi G} \int_{\text{all space}} |\mathbf{g}(\mathbf{r})|^2 dV$$

#### Rigorous Calculus Derivation for a Uniform Solid Sphere of Mass $M$ and Radius $R$
Assemble the sphere by bringing successive spherical shells of thickness $dr$ from infinity and depositing them onto an already formed core of radius $r$ ($0 \le r \le R$).
Let the sphere have uniform mass density $\rho = \frac{3M}{4\pi R^3}$.
1. Mass of the core of radius $r$:
   $$m(r) = \frac{4}{3}\pi r^3 \rho = M \frac{r^3}{R^3}$$
2. Mass of the incremental shell of thickness $dr$:
   $$dm = 4\pi r^2 \rho \, dr = 4\pi r^2 \left(\frac{3M}{4\pi R^3}\right) dr = \frac{3M}{R^3} r^2 dr$$
3. Gravitational potential at the surface of the core:
   $$V_s(r) = -\frac{G m(r)}{r} = -\frac{G}{r} \left(M \frac{r^3}{R^3}\right) = -\frac{GM}{R^3} r^2$$
4. Work required to bring shell $dm$ from infinity:
   $$dU = V_s(r) dm = \left(-\frac{GM}{R^3} r^2\right) \left(\frac{3M}{R^3} r^2 dr\right) = -\frac{3 G M^2}{R^6} r^4 dr$$
5. Total self-energy integrated from $r = 0$ to $r = R$:
   $$U_{\text{self}} = -\frac{3 G M^2}{R^6} \int_0^R r^4 dr = -\frac{3 G M^2}{R^6} \left[ \frac{R^5}{5} \right] = \mathbf{-\frac{3}{5} \frac{GM^2}{R}}$$

#### Gravitational Self-Energy of a Thin Spherical Shell
For a thin spherical shell of mass $M$ and radius $R$, assembling it against the field of existing mass $m$:
$$dU = -\frac{G m \, dm}{R} \implies U_{\text{self}} = -\frac{G}{R} \int_0^M m \, dm = \mathbf{-\frac{1}{2} \frac{GM^2}{R}}$$

---

### 2.1.4 Kepler's Laws & Central Force Derivations

#### 1. Central Force Kinematics & Kepler's Second Law
A gravitational force $\mathbf{F}(\mathbf{r}) = f(r) \hat{\mathbf{r}}$ produces zero torque about the primary center:
$$\boldsymbol{\tau}_O = \mathbf{r} \times \mathbf{F}(\mathbf{r}) = \mathbf{r} \times (f(r)\hat{\mathbf{r}}) = \mathbf{0}$$
By the angular momentum theorem:
$$\frac{d\mathbf{L}}{dt} = \boldsymbol{\tau}_O = \mathbf{0} \implies \mathbf{L} = \mathbf{r} \times m \mathbf{v} = \text{constant vector}$$
Since $\mathbf{r} \cdot \mathbf{L} = 0$, the orbit is strictly planar.
In plane polar coordinates $(r, \theta)$:
$$\mathbf{r} = r\hat{r}, \quad \mathbf{v} = \dot{r}\hat{r} + r\dot{\theta}\hat{\theta}$$
$$L = |\mathbf{r} \times m \mathbf{v}| = m r^2 \dot{\theta} = \text{constant}$$
The infinitesimal area $dA$ swept out by the radius vector in time $dt$ is the area of a triangle:
$$dA = \frac{1}{2} |\mathbf{r} \times d\mathbf{r}| = \frac{1}{2} r (r d\theta) = \frac{1}{2} r^2 \dot{\theta} dt$$
Dividing by $dt$:
$$\mathbf{\frac{dA}{dt} = \frac{1}{2} r^2 \dot{\theta} = \frac{L}{2m} = \text{constant}}$$
*Kepler's Second Law:* The line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time.

#### 2. Kepler's First Law (The Orbital Equation)
The radial equation of motion for a reduced mass $m$ in a central gravitational field is:
$$m(\ddot{r} - r\dot{\theta}^2) = -\frac{GMm}{r^2}$$
Substituting $\dot{\theta} = \frac{L}{mr^2}$ and using the substitution $u = 1/r$, $\frac{dr}{dt} = -\frac{L}{m}\frac{du}{d\theta}$, this transforms into Binet's differential equation:
$$\frac{d^2 u}{d\theta^2} + u = \frac{GMm^2}{L^2}$$
The general solution is the polar equation of a conic section:
$$u(\theta) = \frac{1}{r(\theta)} = \frac{GMm^2}{L^2} [1 + e\cos(\theta - \theta_0)] \implies \mathbf{r(\theta) = \frac{p}{1 + e\cos\theta}}$$
where the semi-latus rectum is $p = \frac{L^2}{GMm^2}$, and the eccentricity $e$ is:
$$\mathbf{e = \sqrt{1 + \frac{2 E L^2}{m (GMm)^2}}}$$
- $E < 0 \implies 0 \le e < 1$: **Elliptical Orbit** (Bound).
- $E = 0 \implies e = 1$: **Parabolic Orbit** (Marginally Unbound).
- $E > 0 \implies e > 1$: **Hyperbolic Orbit** (Unbound).

#### 3. Kepler's Third Law (Harmonic Law)
For an ellipse with semi-major axis $a$ and semi-minor axis $b = a\sqrt{1 - e^2}$, the total geometric area is $A = \pi a b$.
The orbital period $T$ is:
$$T = \frac{\text{Total Area}}{dA/dt} = \frac{\pi a b}{L/(2m)} = \frac{2\pi m a b}{L}$$
Squaring both sides:
$$T^2 = \frac{4\pi^2 m^2 a^2 b^2}{L^2}$$
Since $p = \frac{L^2}{GMm^2} \implies L^2 = GMm^2 p$, and for an ellipse $p = \frac{b^2}{a} \implies b^2 = p a$:
$$T^2 = \frac{4\pi^2 m^2 a^2 (p a)}{GM m^2 p} = \frac{4\pi^2 a^3}{GM}$$
$$\mathbf{T^2 = \left(\frac{4\pi^2}{GM}\right) a^3}$$
*Kepler's Third Law:* The square of the orbital period is strictly proportional to the cube of the semi-major axis, completely independent of eccentricity $e$!

---

### 2.1.5 Orbital Mechanics: Vis-Viva Equation, Trajectories & Hohmann Transfer

#### Rigorous Derivation of the Vis-Viva Equation
In an elliptical orbit of semi-major axis $a$ around a primary mass $M$:
The specific mechanical energy $\epsilon = \frac{E}{m}$ is constant along the orbit:
$$\epsilon = \frac{1}{2} v^2 - \frac{GM}{r}$$
At periapsis ($r_p = a(1 - e)$) and apoapsis ($r_a = a(1 + e)$), the velocity is purely transverse:
$$v_p r_p = v_a r_a \implies v_a = v_p \frac{1 - e}{1 + e}$$
Conservation of energy between periapsis and apoapsis:
$$\frac{1}{2} v_p^2 - \frac{GM}{a(1-e)} = \frac{1}{2} v_a^2 - \frac{GM}{a(1+e)}$$
$$\frac{1}{2} v_p^2 \left[ 1 - \left(\frac{1-e}{1+e}\right)^2 \right] = \frac{GM}{a} \left[ \frac{1}{1-e} - \frac{1}{1+e} \right]$$
$$\frac{1}{2} v_p^2 \left[ \frac{4e}{(1+e)^2} \right] = \frac{GM}{a} \left[ \frac{2e}{1-e^2} \right] = \frac{GM}{a} \left[ \frac{2e}{(1-e)(1+e)} \right]$$
$$v_p^2 \frac{2e}{(1+e)^2} = \frac{GM}{a} \frac{2e}{(1-e)(1+e)} \implies v_p^2 = \frac{GM}{a} \frac{1+e}{1-e}$$
Evaluating the specific energy $\epsilon$ using periapsis values:
$$\epsilon = \frac{1}{2} v_p^2 - \frac{GM}{r_p} = \frac{1}{2}\left(\frac{GM}{a}\frac{1+e}{1-e}\right) - \frac{GM}{a(1-e)} = \frac{GM}{2a(1-e)} [(1+e) - 2] = -\frac{GM(1-e)}{2a(1-e)} = -\frac{GM}{2a}$$
Thus, for ANY bound Keplerian orbit:
$$\mathbf{\epsilon = \frac{E}{m} = -\frac{GM}{2a}}$$
Equating this to $\frac{1}{2}v^2 - \frac{GM}{r}$:
$$\frac{1}{2} v^2 - \frac{GM}{r} = -\frac{GM}{2a} \implies \frac{1}{2} v^2 = GM\left(\frac{1}{r} - \frac{1}{2a}\right)$$
$$\mathbf{v^2 = GM \left( \frac{2}{r} - \frac{1}{a} \right)}$$
This is the celebrated **Vis-Viva Equation**, valid at every point on circular, elliptical, parabolic ($a \to \infty \implies v^2 = \frac{2GM}{r}$), and hyperbolic ($a < 0$) trajectories.

#### Hohmann Transfer Orbit Dynamics
A spacecraft transfers between two coplanar circular orbits of radii $r_1$ and $r_2$ ($r_2 > r_1$) via an intermediate elliptical transfer orbit whose periapsis is at $r_1$ and apoapsis is at $r_2$.
- Semi-major axis of transfer ellipse:
  $$\mathbf{a_{\text{trans}} = \frac{r_1 + r_2}{2}}$$
- Speed in initial circular orbit at $r_1$:
  $$v_{c1} = \sqrt{\frac{GM}{r_1}}$$
- Periapsis speed on transfer ellipse at $r_1$ (using Vis-Viva):
  $$v_{t1} = \sqrt{GM\left(\frac{2}{r_1} - \frac{1}{a_{\text{trans}}}\right)} = \sqrt{GM\left(\frac{2}{r_1} - \frac{2}{r_1+r_2}\right)} = \sqrt{\frac{GM}{r_1}} \sqrt{\frac{2r_2}{r_1+r_2}}$$
- First impulsive velocity increment at $r_1$:
  $$\mathbf{\Delta v_1 = v_{t1} - v_{c1} = \sqrt{\frac{GM}{r_1}} \left( \sqrt{\frac{2r_2}{r_1 + r_2}} - 1 \right)}$$
- Apoapsis speed on transfer ellipse at $r_2$:
  $$v_{t2} = \sqrt{\frac{GM}{r_2}} \sqrt{\frac{2r_1}{r_1+r_2}}$$
- Speed in final circular orbit at $r_2$:
  $$v_{c2} = \sqrt{\frac{GM}{r_2}}$$
- Second impulsive velocity increment at $r_2$:
  $$\mathbf{\Delta v_2 = v_{c2} - v_{t2} = \sqrt{\frac{GM}{r_2}} \left( 1 - \sqrt{\frac{2r_1}{r_1 + r_2}} \right)}$$
- Total velocity requirement: $\Delta v_{\text{total}} = \Delta v_1 + \Delta v_2$.
- Transfer duration: Half the orbital period of the transfer ellipse:
  $$\mathbf{T_{\text{transfer}} = \frac{1}{2} T_{\text{trans}} = \pi \sqrt{\frac{a_{\text{trans}}^3}{GM}} = \pi \sqrt{\frac{(r_1 + r_2)^3}{8 GM}}}$$

---

### 2.1.6 Simple Harmonic Motion: Differential Form, Energy & Phasor Diagrams

#### Fundamental Differential Formulation
A system executes Simple Harmonic Motion (SHM) when its acceleration is directly proportional to its displacement from stable equilibrium and directed oppositely:
$$\ddot{x}(t) + \omega^2 x(t) = 0$$
The general solution in $\mathbb{R}$ is:
$$x(t) = A \sin(\omega t + \phi) = C_1 \cos\omega t + C_2 \sin\omega t$$
where $A$ is the amplitude, $\omega = 2\pi f = \frac{2\pi}{T}$ is the angular frequency, and $\phi$ is the initial phase.
Velocity and acceleration relations:
$$v(t) = \dot{x}(t) = \omega A \cos(\omega t + \phi) = \pm \omega \sqrt{A^2 - x^2}$$
$$a(t) = \ddot{x}(t) = -\omega^2 A \sin(\omega t + \phi) = -\omega^2 x$$

#### Mechanical Energy Distribution & Statistical Averages
For an oscillator of mass $m$ and spring stiffness $k = m\omega^2$:
- Kinetic Energy: $K(t) = \frac{1}{2} m v^2 = \frac{1}{2} m \omega^2 A^2 \cos^2(\omega t + \phi) = \frac{1}{2} k (A^2 - x^2)$.
- Potential Energy: $U(t) = \frac{1}{2} k x^2 = \frac{1}{2} k A^2 \sin^2(\omega t + \phi)$.
- Total Mechanical Energy: $E = K(t) + U(t) = \frac{1}{2} k A^2 = \frac{1}{2} m \omega^2 A^2 = \text{constant}$.

#### Rigorous Distinction: Time-Averaged vs. Space-Averaged Energy
1. **Time-Averaged Over One Full Cycle ($T = 2\pi/\omega$):**
   $$\langle K \rangle_t = \frac{1}{T} \int_0^T \frac{1}{2} k A^2 \cos^2(\omega t + \phi) dt = \frac{1}{2} k A^2 \left(\frac{1}{2}\right) = \mathbf{\frac{1}{4} k A^2}$$
   $$\langle U \rangle_t = \frac{1}{T} \int_0^T \frac{1}{2} k A^2 \sin^2(\omega t + \phi) dt = \frac{1}{2} k A^2 \left(\frac{1}{2}\right) = \mathbf{\frac{1}{4} k A^2}$$
   $$\langle K \rangle_t = \langle U \rangle_t = \frac{1}{2} E$$
2. **Space-Averaged Over Amplitude Domain ($x \in [-A, +A]$):**
   $$\langle K \rangle_x = \frac{1}{2A} \int_{-A}^A K(x) dx = \frac{1}{2A} \int_{-A}^A \frac{1}{2} k (A^2 - x^2) dx = \frac{k}{2A} \left[ A^2 x - \frac{x^3}{3} \right]_0^A = \frac{k}{2A} \left(\frac{2}{3} A^3\right) = \mathbf{\frac{1}{3} k A^2 = \frac{2}{3} E}$$
   $$\langle U \rangle_x = \frac{1}{2A} \int_{-A}^A \frac{1}{2} k x^2 dx = \frac{k}{2A} \left[ \frac{x^3}{3} \right]_0^A = \frac{k}{2A} \left(\frac{A^3}{3}\right) = \mathbf{\frac{1}{6} k A^2 = \frac{1}{3} E}$$
   **Crucial Trap Alert:** $\langle K \rangle_t \ne \langle K \rangle_x$! The space average weights the particle near the turning points where it spends more time!

---

### 2.1.7 Advanced Oscillating Systems: Two-Block Reduced Mass & Heavy Spring Correction

#### 1. Two-Block Oscillator with Spring (Reduced Mass Framework)
Consider two blocks of masses $m_1$ and $m_2$ connected by a light spring of stiffness $k$ and natural length $l_0$ on a frictionless horizontal plane.
Let $x_1$ and $x_2$ denote their coordinates ($x_2 > x_1$). Spring elongation is $\xi = (x_2 - x_1) - l_0$.
Equations of motion:
$$m_1 \ddot{x}_1 = +k \xi, \quad m_2 \ddot{x}_2 = -k \xi$$
$$\ddot{x}_2 - \ddot{x}_1 = -\frac{k}{m_2}\xi - \frac{k}{m_1}\xi = -k\left(\frac{m_1 + m_2}{m_1 m_2}\right)\xi$$
Since $\ddot{\xi} = \ddot{x}_2 - \ddot{x}_1$:
$$\ddot{\xi} + \frac{k}{\mu} \xi = 0$$
where $\mu$ is the **Reduced Mass**:
$$\mathbf{\mu = \frac{m_1 m_2}{m_1 + m_2}}$$
The natural angular frequency of oscillation is:
$$\mathbf{\omega = \sqrt{\frac{k}{\mu}} = \sqrt{k \left(\frac{1}{m_1} + \frac{1}{m_2}\right)}}$$

#### 2. Heavy Spring Correction (Rayleigh's Effective Mass)
Let a block of mass $M$ be attached to a real spring of mass $m_s$, total length $L$, and stiffness $k$.
Assume a linear velocity profile along the spring: at distance $y$ from the fixed end ($0 \le y \le L$), the velocity of the spring element $dy$ is:
$$v(y) = \frac{y}{L} v_{\text{block}}$$
The kinetic energy of the spring is obtained by integration:
$$K_{\text{spring}} = \int_0^L \frac{1}{2} (dm) v(y)^2 = \int_0^L \frac{1}{2} \left(\frac{m_s}{L} dy\right) \left(\frac{y}{L} v\right)^2 = \frac{m_s v^2}{2 L^3} \int_0^L y^2 dy = \frac{m_s v^2}{2 L^3} \left(\frac{L^3}{3}\right) = \frac{1}{2} \left(\frac{m_s}{3}\right) v^2$$
The total kinetic energy of the system is:
$$K_{\text{total}} = K_{\text{block}} + K_{\text{spring}} = \frac{1}{2} M v^2 + \frac{1}{2} \left(\frac{m_s}{3}\right) v^2 = \frac{1}{2} \left(M + \frac{m_s}{3}\right) v^2$$
The effective oscillating mass is:
$$\mathbf{M_{\text{eff}} = M + \frac{m_s}{3}}$$
The exact corrected oscillation period is:
$$\mathbf{T = 2\pi \sqrt{\frac{M + \frac{m_s}{3}}{k}}}$$

---

### 2.1.8 Compound Pendulum: Reversibility Theorem & Center of Oscillation

#### Governing Equation of Motion
A compound (physical) pendulum is a rigid body of mass $M$ free to oscillate in a vertical plane about a smooth horizontal axis passing through suspension point $S$.
Let $d$ be the distance from suspension point $S$ to the Center of Mass $C$.
Let $I_S$ be the moment of inertia about the suspension axis. By Steiner's theorem:
$$I_S = I_{cm} + M d^2 = M(k_{cm}^2 + d^2)$$
When deflected by angle $\theta$ from the vertical, restoring torque due to gravity is:
$$\tau_S = -M g d \sin\theta$$
Equation of motion:
$$I_S \ddot{\theta} + M g d \sin\theta = 0$$
For small amplitude oscillations ($\sin\theta \approx \theta$):
$$\ddot{\theta} + \frac{M g d}{M(k_{cm}^2 + d^2)} \theta = 0 \implies \ddot{\theta} + \frac{g d}{k_{cm}^2 + d^2} \theta = 0$$
The period of small oscillations is:
$$\mathbf{T = 2\pi \sqrt{\frac{I_S}{M g d}} = 2\pi \sqrt{\frac{k_{cm}^2 + d^2}{g d}}}$$

#### Equivalent Simple Pendulum Length $L_{\text{eq}}$
Comparing with a simple pendulum of length $L$ ($T = 2\pi\sqrt{L/g}$):
$$\mathbf{L_{\text{eq}} = \frac{k_{cm}^2 + d^2}{d} = d + \frac{k_{cm}^2}{d}}$$

#### Minimum Period Condition
Differentiating $T(d)$ with respect to $d$ to find the stationary points:
$$\frac{d}{dd}\left(\frac{k_{cm}^2 + d^2}{d}\right) = \frac{d}{dd}\left(\frac{k_{cm}^2}{d} + d\right) = -\frac{k_{cm}^2}{d^2} + 1 = 0 \implies \mathbf{d = k_{cm}}$$
The minimum possible period for a given body is:
$$\mathbf{T_{\text{min}} = 2\pi \sqrt{\frac{2 k_{cm}}{g}}}$$

#### Reversibility Theorem & Conjugate Center of Oscillation
For any period $T > T_{\text{min}}$, there exists a quadratic equation in $d$:
$$d^2 - L_{\text{eq}} d + k_{cm}^2 = 0$$
This quadratic equation possesses two distinct positive roots $d_1$ and $d_2$:
$$d_1 + d_2 = L_{\text{eq}}, \quad \mathbf{d_1 d_2 = k_{cm}^2}$$
*Reversibility Theorem (Kater's Theorem):* If the pendulum is suspended from a point $O$ located on the opposite side of the COM along the collinear line at distance $d_2 = k_{cm}^2 / d_1$, the period of oscillation about $O$ is **identically equal** to the period about $S$!
Point $O$ is called the **Center of Oscillation** relative to suspension point $S$, and the distance between them is the equivalent length: $SO = d_1 + d_2 = L_{\text{eq}}$.

---

### 2.1.9 Damped Oscillations: Underdamped, Overdamped, Critical Damping & Q-Factor

#### Governing Differential Equation
Consider an oscillator of mass $m$ subject to a linear elastic restoring force $-kx$ and a viscous damping force proportional to velocity $\mathbf{F}_{\text{damp}} = -b \dot{x}$:
$$m \ddot{x} + b \dot{x} + k x = 0 \implies \mathbf{\ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = 0}$$
where:
$$\gamma = \frac{b}{2m} \quad (\text{damping attenuation factor}), \quad \omega_0 = \sqrt{\frac{k}{m}} \quad (\text{undamped natural frequency})$$

#### Characteristic Roots and Dynamic Regimes
Substituting $x(t) = e^{rt}$ into the homogeneous equation yields the characteristic equation:
$$r^2 + 2\gamma r + \omega_0^2 = 0 \implies r_{1,2} = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2}$$

1. **Underdamped Regime ($\gamma < \omega_0 \iff b < 2\sqrt{km}$):**
   The roots are complex conjugates: $r_{1,2} = -\gamma \pm i \omega_d$, where the damped frequency is:
   $$\mathbf{\omega_d = \sqrt{\omega_0^2 - \gamma^2} = \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}}}$$
   The general kinematic solution is:
   $$\mathbf{x(t) = A_0 e^{-\gamma t} \cos(\omega_d t + \phi)}$$
   The amplitude decays exponentially with envelope $A(t) = A_0 e^{-\gamma t}$.
   The **Logarithmic Decrement** $\delta$ across one complete period $T_d = \frac{2\pi}{\omega_d}$ is:
   $$\mathbf{\delta = \ln\left(\frac{x(t)}{x(t + T_d)}\right) = \gamma T_d = \frac{2\pi \gamma}{\omega_d}}$$

2. **Critically Damped Regime ($\gamma = \omega_0 \iff b = 2\sqrt{km}$):**
   Repeated real roots $r_1 = r_2 = -\gamma$.
   $$\mathbf{x(t) = (C_1 + C_2 t) e^{-\gamma t}}$$
   This represents the fastest non-oscillatory return to mechanical equilibrium without overshoot.

3. **Overdamped Regime ($\gamma > \omega_0 \iff b > 2\sqrt{km}$):**
   Two distinct negative real roots $r_{1,2} = -\gamma \pm \sqrt{\gamma^2 - \omega_0^2} < 0$.
   $$\mathbf{x(t) = C_1 e^{-r_1 t} + C_2 e^{-r_2 t}}$$
   The motion is sluggish and purely non-oscillatory.

#### Quality Factor ($Q$-Factor)
The Quality Factor $Q$ quantifies the sharpness of resonance and the fractional energy retained per cycle of oscillation:
$$\mathbf{Q = 2\pi \frac{\text{Energy Stored}}{\text{Energy Dissipated Per Cycle}} = \frac{\omega_0}{2\gamma} = \frac{m \omega_0}{b} = \frac{\pi}{\delta}}$$
For high-$Q$ systems ($Q \gg 1$), the fractional energy loss per radian is:
$$\frac{\Delta E}{E} \approx \frac{1}{Q}$$

---

### 2.1.10 Driven Oscillations, Steady-State Amplitude & Resonance Dynamics

#### Governing Equation Under Harmonic Forcing
When an external periodic force $F(t) = F_0 \cos(\omega t)$ drives the damped oscillator:
$$\ddot{x} + 2\gamma \dot{x} + \omega_0^2 x = \frac{F_0}{m} \cos(\omega t)$$
The complete solution consists of transient complementary function $x_c(t) \to 0$ (which decays exponentially) and the steady-state particular integral:
$$\mathbf{x_{\text{ss}}(t) = A(\omega) \cos(\omega t - \delta)}$$

#### Steady-State Amplitude and Phase Lag
Using the complex exponential method $x = \text{Re}[X_0 e^{i\omega t}]$:
$$X_0(-\omega^2 + 2i\gamma\omega + \omega_0^2) = \frac{F_0}{m} \implies X_0 = \frac{F_0/m}{(\omega_0^2 - \omega^2) + 2i\gamma\omega}$$
The steady-state amplitude is:
$$\mathbf{A(\omega) = \frac{F_0 / m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2}}}$$
The phase lag $\delta$ by which displacement trails the driving force is:
$$\mathbf{\tan\delta = \frac{2\gamma \omega}{\omega_0^2 - \omega^2}}$$

#### Amplitude Resonance vs. Velocity Resonance
1. **Amplitude Resonance:**
   Maximizing $A(\omega)$ requires minimizing the denominator $g(\omega) = (\omega_0^2 - \omega^2)^2 + 4\gamma^2 \omega^2$.
   Setting $\frac{dg}{d(\omega^2)} = -2(\omega_0^2 - \omega^2) + 4\gamma^2 = 0$:
   $$\mathbf{\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}}$$
   - Amplitude resonance occurs at a frequency **strictly lower than $\omega_0$**!
   - Peak amplitude:
     $$A_{\text{max}} = \frac{F_0/m}{2\gamma \sqrt{\omega_0^2 - \gamma^2}} \approx \frac{F_0 Q}{m \omega_0^2} \quad (\text{for small damping})$$
   - If $\gamma > \frac{\omega_0}{\sqrt{2}}$, no amplitude resonance peak exists; $A(\omega)$ decreases monotonically with $\omega$.
2. **Velocity Resonance (Power Resonance):**
   The steady-state velocity is $v_{\text{ss}}(t) = -\omega A(\omega) \sin(\omega t - \delta)$.
   The velocity amplitude $v_0(\omega) = \omega A(\omega)$ is:
   $$v_0(\omega) = \frac{F_0/m}{\sqrt{\left(\frac{\omega_0^2 - \omega^2}{\omega}\right)^2 + 4\gamma^2}}$$
   This denominator is minimized when $\frac{\omega_0^2 - \omega^2}{\omega} = 0 \implies \mathbf{\omega = \omega_0}$.
   Velocity resonance and maximum rate of energy absorption occur **precisely at the undamped natural frequency $\omega_0$**, where $\delta = \pi/2$ (force and velocity are exactly in phase).
""")

    # 2.2 Master Formula Summary Table
    parts.append(r"""## 2.2 Master Formula Summary Table (Chapter 6)

| Formula Name | Mathematical Expression | Strict Domain of Validity | High-Stakes Invalidation Regimes |
|---|---|---|---|
| **Universal Gravitation** | $\mathbf{F} = -G \frac{M m}{r^2} \hat{\mathbf{r}}$ | Point masses, or spherically symmetric mass distributions outside their radii. | **FATAL ERROR:** Applying between bodies whose separation is comparable to their physical sizes. |
| **Shell Theorem (Interior)** | $g_{\text{in}} = 0, \quad V_{\text{in}} = -\frac{GM}{R}$ | Uniform thin spherical shell interior ($r < R$). | Fails for non-spherical cavities or non-uniform density shells. |
| **Solid Sphere Potential** | $V_{\text{in}}(r) = -\frac{GM}{2R^3}(3R^2 - r^2)$ | Uniform density solid sphere ($r \le R$). | Invalid if density varies with radius ($\rho = \rho(r)$). Must integrate Poisson's equation. |
| **Gravitational Self-Energy** | $U_{\text{self}} = -\frac{3}{5}\frac{GM^2}{R}$ | Uniform density solid sphere assembled from infinity. | Fails for hollow shells ($-\frac{1}{2}\frac{GM^2}{R}$) or planets with dense iron cores (e.g. Earth $\approx -0.84 \frac{GM^2}{R}$). |
| **Kepler's Third Law** | $T^2 = \frac{4\pi^2}{GM} a^3$ | Two-body bound Keplerian orbits where $m_{\text{planet}} \ll M_{\text{star}}$. | Invalid if planet mass is comparable to star (requires reduced mass: $M_{\text{total}} = M + m$). |
| **Vis-Viva Equation** | $v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)$ | Any Keplerian orbit in an inverse-square central field. | Invalid if non-gravitational thrust acts or in oblate planet gravity ($J_2$ perturbations). |
| **Hohmann Transfer Period** | $T_{\text{trans}} = \pi \sqrt{\frac{(r_1 + r_2)^3}{8 GM}}$ | Impulsive, tangential coplanar two-impulse transfer between circular orbits. | Invalid for non-coplanar, inclined, or continuous-thrust (ion drive) spiral transfers. |
| **SHM Velocity-Position** | $v(x) = \pm \omega \sqrt{A^2 - x^2}$ | Pure linear simple harmonic motion ($F = -kx$). | Invalid for large amplitude pendulums or non-linear restoring forces ($F = -kx - \beta x^3$). |
| **Two-Block Reduced Mass** | $\omega = \sqrt{\frac{k}{\mu}}, \quad \mu = \frac{m_1 m_2}{m_1 + m_2}$ | Isolated two-body linear system coupled by linear spring on frictionless guide. | Invalid if external friction acts differently on the two masses. |
| **Heavy Spring Correction** | $M_{\text{eff}} = M + \frac{m_s}{3}$ | Mass-spring oscillator with light-to-moderate spring mass ($m_s \lesssim M$). | Invalid if spring mass dominates ($m_s \gg M$), where wave propagation dynamics take over. |
| **Compound Pendulum Period** | $T = 2\pi \sqrt{\frac{k_{cm}^2 + d^2}{gd}}$ | Rigid body pivoting under gravity at small angles ($\theta \ll 1\text{ rad}$). | Fails for large amplitudes ($\theta_0 > 15^\circ$); requires elliptic integral $K(\sin\frac{\theta_0}{2})$. |
| **Underdamped Frequency** | $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$ | Linear viscous damping ($F_d = -bv$) with $\gamma < \omega_0$. | Invalid for quadratic aerodynamic drag ($F_d \propto v^2$) or Coulomb dry friction damping. |
""")

    # 2.3 NTA / JEE Trap Alerts
    parts.append(r"""## 2.3 NTA / JEE Trap Alerts: 12 High-Probability Negative-Marking Pitfalls

### ⚠️ Trap Alert 6.1: Assuming Gravitational Potential Inside a Solid Sphere is Constant
- **Psychological Failure Mode:** A student remembers that gravitational field inside a shell is zero and potential is constant. They mistakenly extend this to a solid sphere, writing $V_{\text{in}} = -\frac{GM}{R}$.
- **Mathematical Reality:** Inside a uniform solid sphere, mass elements at larger radii exert zero net field, but mass elements at smaller radii pull inward! Thus $g(r) = \frac{GM r}{R^3} \ne 0$. Integrating $dV = -g dr$ yields a parabolic potential:
  $$V_{\text{in}}(r) = -\frac{GM}{2R^3}(3R^2 - r^2)$$
  At the center ($r = 0$), $V_{\text{center}} = -1.5 \frac{GM}{R}$, which is 50% deeper than the surface potential!
- **Definitive Student Rule:** Inside a solid sphere, $g \propto r$ (linear) and $V(r)$ is a concave-up parabola with minimum at the center. It is never constant.

---

### ⚠️ Trap Alert 6.2: Using $g' = g(1 - 2h/R)$ When $h$ is Comparable to $R$
- **Psychological Failure Mode:** A problem asks for the acceleration due to gravity at altitude $h = R$. The student plugs $h = R$ into the first-order approximation:
  $$g' = g\left(1 - \frac{2h}{R}\right) = g(1 - 2) = -g \quad (\text{ABSURD!})$$
- **Mathematical Reality:** The linear formula $g' = g(1 - 2h/R)$ is a Taylor series expansion valid **strictly for $h \ll R$** ($h \lesssim 100\text{ km}$). For arbitrary altitude $h$:
  $$g' = \frac{GM}{(R + h)^2} = g \left( \frac{R}{R + h} \right)^2$$
  At $h = R$, $g' = g \left(\frac{R}{2R}\right)^2 = \frac{g}{4} = 0.25 g$.
- **Definitive Student Rule:** If $h > 0.05 R$ ($h > 300\text{ km}$), never use the linear approximation. Always use the exact inverse-square law $g' = g/(1 + h/R)^2$.

---

### ⚠️ Trap Alert 6.3: Missing Gravitational Self-Energy When Dispersing Celestial Bodies
- **Psychological Failure Mode:** A question asks for the minimum energy required to blow up or disintegrate a planet of mass $M$ and radius $R$. Students compute $W = M v_{\text{esc}}^2 / 2$ or treat it as moving particles from the surface.
- **Mathematical Reality:** Dispersing a continuous sphere to infinity requires overcoming its internal gravitational self-energy:
  $$W_{\text{disperse}} = U_f - U_i = 0 - \left(-\frac{3}{5}\frac{GM^2}{R}\right) = +\frac{3}{5}\frac{GM^2}{R}$$
- **Definitive Student Rule:** The energy required to shatter, disperse, or assemble any uniform spherical celestial body is strictly given by its binding energy: $\Delta E = \frac{3}{5}\frac{GM^2}{R}$.

---

### ⚠️ Trap Alert 6.4: Kepler's 3rd Law: Substituting Distance of Closest Approach Instead of Semi-Major Axis
- **Psychological Failure Mode:** Given an eccentric orbit with perihelion $r_p$ and aphelion $r_a$, a student computes period using $T^2 \propto r_p^3$ or $T^2 \propto \left(\frac{r_p + r_a}{2}\right)^2$.
- **Mathematical Reality:** Kepler's Third Law depends strictly and exclusively on the **semi-major axis** $a = \frac{r_p + r_a}{2}$:
  $$T^2 = \frac{4\pi^2}{GM} a^3 = \frac{4\pi^2}{GM} \left(\frac{r_p + r_a}{2}\right)^3$$
- **Definitive Student Rule:** In any elliptical orbit, the mean orbital distance is always the semi-major axis $a = (r_p + r_a)/2$.

---

### ⚠️ Trap Alert 6.5: Confusing Time-Averaged with Space-Averaged Kinetic Energy in SHM
- **Psychological Failure Mode:** Asked for the "average kinetic energy" of an SHM oscillator over its range of motion, students instinctively answer $\frac{1}{4} k A^2$.
- **Mathematical Reality:** 
  - Time-average over one cycle: $\langle K \rangle_t = \frac{1}{4} k A^2$.
  - Space-average across $x \in [-A, A]$:
    $$\langle K \rangle_x = \frac{1}{2A}\int_{-A}^A \frac{1}{2}k(A^2 - x^2)dx = \mathbf{\frac{1}{3} k A^2}$$
- **Definitive Student Rule:** Read the question with forensic care: if it says "average over time/cycle," the answer is $\frac{1}{4}kA^2$. If it says "average over position/path," the answer is $\frac{1}{3}kA^2$.

---

### ⚠️ Trap Alert 6.6: Compound Pendulum: Measuring Distance $d$ from the Pivot Instead of COM
- **Psychological Failure Mode:** In a uniform rod pivoted at one end, a student writes $d = L$ in $T = 2\pi\sqrt{\frac{k^2 + d^2}{gd}}$.
- **Mathematical Reality:** The variable $d$ in the compound pendulum formula is strictly the distance from the pivot $S$ to the **Center of Mass** $C$. For a rod of length $L$ pivoted at an end, $d = L/2$.
  $$T = 2\pi \sqrt{\frac{L^2/12 + (L/2)^2}{g (L/2)}} = 2\pi \sqrt{\frac{L^2/3}{g L/2}} = 2\pi \sqrt{\frac{2L}{3g}}$$
- **Definitive Student Rule:** $d \equiv |\mathbf{r}_{\text{pivot}} - \mathbf{r}_{cm}|$. Never measure $d$ from an edge or tip!

---

### ⚠️ Trap Alert 6.7: Overlooking Spring Mass Contribution in High-Frequency Oscillators
- **Psychological Failure Mode:** A spring of mass $m_s = 60\text{ g}$ supports a mass $M = 20\text{ g}$. A student calculates frequency using $M = 20\text{ g}$.
- **Mathematical Reality:** The effective mass includes one-third of the spring mass:
  $$M_{\text{eff}} = M + \frac{m_s}{3} = 20 + \frac{60}{3} = 40\text{ g}$$
  Ignoring $m_s/3$ introduces an enormous error: $\omega_{\text{incorrect}} / \omega_{\text{correct}} = \sqrt{40/20} = \sqrt{2} \approx 1.414$ (a 41.4% error!).
- **Definitive Student Rule:** If the spring mass $m_s$ is given, immediately replace $M$ with $M_{\text{eff}} = M + m_s/3$.

---

### ⚠️ Trap Alert 6.8: Amplitude Resonance vs. Natural Frequency in Driven Oscillations
- **Psychological Failure Mode:** In driven oscillations with damping, students assume the amplitude of vibration is maximized when driving frequency equals the undamped natural frequency ($\omega = \omega_0$).
- **Mathematical Reality:** 
  - Amplitude resonance occurs at $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2} < \omega_0$.
  - Velocity (power) resonance occurs at $\omega = \omega_0$.
- **Definitive Student Rule:** Displacement amplitude peaks at $\sqrt{\omega_0^2 - 2\gamma^2}$. Velocity and power absorption peak at $\omega_0$.

---

### ⚠️ Trap Alert 6.9: Gravitational Acceleration Inside Non-Uniform Planets
- **Psychological Failure Mode:** A planet has density $\rho(r) = C r$. Students assume $g(r) \propto r$ inside the planet.
- **Mathematical Reality:** By Gauss's Law:
  $$M_{\text{enc}}(r) = \int_0^r 4\pi r'^2 (C r') dr' = \pi C r^4 \implies g(r) = \frac{G M_{\text{enc}}(r)}{r^2} = \pi G C r^2 \propto r^2$$
- **Definitive Student Rule:** Never assume $g(r) \propto r$ unless density $\rho$ is explicitly stated to be uniform. For any $\rho(r) \propto r^n$, $g(r) \propto r^{n+1}$.

---

### ⚠️ Trap Alert 6.10: Energy Required to Boost an Orbit: The "Faster Speed" Paradox
- **Psychological Failure Mode:** To move a satellite from orbit radius $r_1$ to higher orbit $r_2 > r_1$, students assume speed must increase and write $\Delta E = \frac{1}{2}m v_2^2 - \frac{1}{2}m v_1^2 > 0$.
- **Mathematical Reality:** In a higher orbit, orbital speed is **lower** ($v = \sqrt{GM/r}$)! However, potential energy is much less negative:
  $$E = -\frac{GMm}{2r} \implies \Delta E = E_2 - E_1 = -\frac{GMm}{2r_2} - \left(-\frac{GMm}{2r_1}\right) = \frac{GMm}{2}\left(\frac{1}{r_1} - \frac{1}{r_2}\right) > 0$$
  The satellite absorbs energy ($\Delta E > 0$), yet its orbital speed decreases!
- **Definitive Student Rule:** Increasing total orbital energy raises the orbit and paradoxically slows down the satellite's orbital speed.

---

### ⚠️ Trap Alert 6.11: Phasor Projection Sign and Quadrant Misinterpretation
- **Psychological Failure Mode:** A particle is at $x = -A/2$ moving toward the origin ($v > 0$). A student assigns initial phase $\phi = 7\pi/6$ instead of checking the velocity sign on the phasor circle.
- **Mathematical Reality:** On the reference circle with $x = A\sin(\omega t + \phi)$:
  $$v = \omega A \cos(\omega t + \phi)$$
  For $x < 0$ and $v > 0$, we require $\sin\phi < 0$ and $\cos\phi > 0$, placing $\phi$ in the fourth quadrant ($\phi = -\pi/6$ or $11\pi/6$).
- **Definitive Student Rule:** Always sketch the reference circle with counter-clockwise rotation and verify both displacement and velocity projections simultaneously.

---

### ⚠️ Trap Alert 6.12: Assuming Motion in a Tunnel is SHM for Non-Uniform Density Planets
- **Psychological Failure Mode:** A planet has density $\rho(r) = \rho_0(1 - r/R)$. A student asserts the motion of a body in a diametric tunnel is Simple Harmonic.
- **Mathematical Reality:** SHM requires $F \propto -x$. For this non-uniform planet, $M_{\text{enc}}(r) = 4\pi \rho_0 \left(\frac{r^3}{3} - \frac{r^4}{4R}\right)$, so:
  $$F(r) = -\frac{GM_{\text{enc}}m}{r^2} = -4\pi G \rho_0 m \left(\frac{r}{3} - \frac{r^2}{4R}\right)$$
  Because of the non-linear $r^2$ term, the motion is strictly **periodic, but NOT Simple Harmonic**!
- **Definitive Student Rule:** Periodic motion is SHM if and only if restoring force is purely linear in displacement. Any higher-order terms invalidate SHM.
""")

    # 2.4 Dissected JEE Advanced PYQs
    parts.append(r"""## 2.4 Dissected JEE Advanced Previous Year Questions (PYQs)

### PYQ 6.1: JEE Advanced 2019 (Paper 2) — Non-Uniform Planet Gravitational Tunnel Dynamics
**Problem Statement:**  
A spherical planet of radius $R$ has a spherically symmetric, non-uniform mass density given by:
$$\rho(r) = \rho_0 \left(1 - \frac{r}{R}\right) \quad \text{for } 0 \le r \le R$$
A narrow diametric tunnel is bored through the center of the planet. A small test particle of mass $m$ is released from rest at the surface ($r = R$).
1. Derive the gravitational acceleration $g(r)$ as a function of radial distance $r$.
2. Determine the speed $v_0$ with which the particle passes through the planet's center.

---

#### Step-by-Step Analytical Derivation:
**Step 1: Enclosed Mass as a Function of Radius:**  
Consider a concentric spherical Gaussian shell of radius $r'$ and thickness $dr'$:
$$M_{\text{enc}}(r) = \int_0^r \rho(r') 4\pi r'^2 dr' = 4\pi \rho_0 \int_0^r \left(r'^2 - \frac{r'^3}{R}\right) dr'$$
$$M_{\text{enc}}(r) = 4\pi \rho_0 \left[ \frac{r^3}{3} - \frac{r^4}{4R} \right] = \pi \rho_0 r^3 \left( \frac{4}{3} - \frac{r}{R} \right)$$
Total mass of the planet at $r = R$:
$$M_{\text{total}} = M_{\text{enc}}(R) = \pi \rho_0 R^3 \left(\frac{4}{3} - 1\right) = \frac{1}{3} \pi \rho_0 R^3$$

**Step 2: Gravitational Acceleration Inside the Planet:**  
By Gauss's Law for gravitation, the mass outside radius $r$ exerts zero net field:
$$g(r) = \frac{G M_{\text{enc}}(r)}{r^2} = \frac{G \cdot 4\pi \rho_0 \left(\frac{r^3}{3} - \frac{r^4}{4R}\right)}{r^2} = \mathbf{4\pi G \rho_0 \left( \frac{r}{3} - \frac{r^2}{4R} \right)}$$
Notice that at the surface $r = R$:
$$g(R) = 4\pi G \rho_0 R \left(\frac{1}{3} - \frac{1}{4}\right) = \frac{\pi G \rho_0 R}{3} = \frac{G M_{\text{total}}}{R^2} \quad (\text{Perfect consistency})$$

**Step 3: Speed at Center via Work-Energy Theorem:**  
The force directed toward the center is $F(r) = -m g(r)$.
By the Work-Energy Theorem:
$$\Delta K = K_{\text{center}} - K_{\text{surface}} = \frac{1}{2} m v_0^2 - 0 = \int_R^0 F(r) dr = -\int_R^0 m g(r) dr = \int_0^R m g(r) dr$$
$$\frac{1}{2} m v_0^2 = m \int_0^R 4\pi G \rho_0 \left(\frac{r}{3} - \frac{r^2}{4R}\right) dr$$
Canceling mass $m$ and evaluating the integral:
$$\frac{1}{2} v_0^2 = 4\pi G \rho_0 \left[ \frac{r^2}{6} - \frac{r^3}{12R} \right]_0^R = 4\pi G \rho_0 \left( \frac{R^2}{6} - \frac{R^2}{12} \right) = 4\pi G \rho_0 \left(\frac{R^2}{12}\right) = \frac{\pi G \rho_0 R^2}{3}$$
$$v_0^2 = \frac{2\pi G \rho_0 R^2}{3}$$
Expressing in terms of $M_{\text{total}} = \frac{1}{3}\pi \rho_0 R^3 \implies \pi \rho_0 = \frac{3 M_{\text{total}}}{R^3}$:
$$v_0^2 = \frac{2 G R^2}{3} \left(\frac{3 M_{\text{total}}}{R^3}\right) = \frac{2 G M_{\text{total}}}{R}$$
$$\mathbf{v_0 = \sqrt{\frac{2 G M_{\text{total}}}{R}}}$$
*Remarkable Result:* The speed at the center is **identically equal to the escape velocity** from the planet's surface: $v_0 = v_{\text{esc}}$!

---

#### Examiner Trap Dissection:
- **Trap 1:** Assuming $g(r) \propto r$ (uniform density formula). This would yield $v_0 = \sqrt{G M/R}$, underestimating the true speed by a factor of $\sqrt{2}$.
- **Trap 2:** Attempting to use SHM formulas $v = \omega A$. As proven above, the restoring force is non-linear ($r - \frac{3r^2}{4R}$), so the motion is NOT Simple Harmonic.

---

### PYQ 6.2: JEE Advanced 2015 (Paper 1) — Compound Pendulum with Minimum Time Period
**Problem Statement:**  
A uniform thin circular disc of mass $M$ and radius $R$ is suspended by a horizontal knife-edge axis passing through a small hole drilled at distance $x$ from the disc's center ($0 < x < R$). The disc oscillates in its own plane with small amplitude.
1. Find the time period of oscillation $T(x)$ as a function of $x$.
2. Find the value of $x = x^*$ for which the time period is minimized, and determine the minimum time period $T_{\text{min}}$.
3. If $x = R/4$, find the conjugate distance $x'$ on the disc such that the period of oscillation about $x'$ equals the period about $x$.

---

#### Step-by-Step Analytical Derivation:
**Step 1: Moment of Inertia and Equation of Motion:**  
For in-plane oscillations, the rotation axis is perpendicular to the disc plane.
Moment of inertia about central transverse axis: $I_{cm} = \frac{1}{2} M R^2$.
The radius of gyration is:
$$k_{cm}^2 = \frac{I_{cm}}{M} = \frac{1}{2} R^2$$
By Steiner's Theorem, the moment of inertia about the suspension point at distance $x$ is:
$$I_S = I_{cm} + M x^2 = M\left(\frac{R^2}{2} + x^2\right)$$
The small-angle equation of motion is:
$$I_S \ddot{\theta} + M g x \theta = 0 \implies \ddot{\theta} + \frac{g x}{\frac{R^2}{2} + x^2} \theta = 0$$
The time period of oscillation is:
$$\mathbf{T(x) = 2\pi \sqrt{\frac{\frac{1}{2}R^2 + x^2}{g x}}}$$

**Step 2: Minimizing the Time Period:**  
To find the minimum, define $f(x) = \frac{\frac{1}{2}R^2 + x^2}{x} = \frac{R^2}{2x} + x$.
Differentiating with respect to $x$:
$$f'(x) = -\frac{R^2}{2x^2} + 1 = 0 \implies x^2 = \frac{R^2}{2} \implies \mathbf{x^* = \frac{R}{\sqrt{2}}}$$
At $x^* = R/\sqrt{2}$:
$$f(x^*) = \frac{R^2}{2(R/\sqrt{2})} + \frac{R}{\sqrt{2}} = \frac{R}{\sqrt{2}} + \frac{R}{\sqrt{2}} = \sqrt{2} R$$
Substituting into the period formula:
$$\mathbf{T_{\text{min}} = 2\pi \sqrt{\frac{\sqrt{2} R}{g}}}$$

**Step 3: Conjugate Distance $x'$ for $x = R/4$:**  
By Kater's Reversibility Theorem:
$$x \cdot x' = k_{cm}^2 = \frac{1}{2} R^2$$
Given $x = \frac{R}{4}$:
$$\left(\frac{R}{4}\right) x' = \frac{R^2}{2} \implies \mathbf{x' = 2R}$$
*Critical Examiner Insight:* Because $x' = 2R > R$, the conjugate point lies **outside the physical boundary of the disc**!
Therefore, within the physical disc itself ($x \le R$), there is **no other point** that gives the same period as $x = R/4$. The period at $x = R/4$ is unique on the physical disc!

---

### PYQ 6.3: JEE Advanced 2021 (Paper 1) — Damped Oscillator & Exponential Energy Dissipation
**Problem Statement:**  
A damped harmonic oscillator consists of a mass $m = 0.2 \, \text{kg}$ attached to a spring of stiffness $k = 80 \, \text{N/m}$. The system experiences a viscous damping force $F_d = -b v$. The amplitude of oscillation drops to half its initial value after 50 complete cycles of oscillation.
1. Determine the damping constant $b$.
2. Calculate the Quality Factor $Q$ of this oscillator.
3. Compute the percentage of mechanical energy dissipated during the first 50 cycles.

---

#### Step-by-Step Analytical Derivation:
**Step 1: Frequency and Natural Frequency:**  
Undamped natural angular frequency:
$$\omega_0 = \sqrt{\frac{k}{m}} = \sqrt{\frac{80}{0.2}} = \sqrt{400} = 20 \, \text{rad/s}$$
Since the amplitude decays over 50 cycles, damping is very light ($\gamma \ll \omega_0$), so:
$$\omega_d = \sqrt{\omega_0^2 - \gamma^2} \approx \omega_0 = 20 \, \text{rad/s}$$
The period of one cycle is:
$$T \approx \frac{2\pi}{\omega_0} = \frac{2\pi}{20} = \frac{\pi}{10} \, \text{s}$$
The duration of 50 cycles is:
$$t_{50} = 50 T = 50 \left(\frac{\pi}{10}\right) = 5\pi \, \text{s}$$

**Step 2: Damping Constant $b$:**  
The amplitude decays according to $A(t) = A_0 e^{-\gamma t}$, where $\gamma = \frac{b}{2m}$.
At $t = t_{50}$:
$$\frac{A(t_{50})}{A_0} = \frac{1}{2} = e^{-\gamma (5\pi)} \implies \gamma (5\pi) = \ln 2$$
$$\gamma = \frac{\ln 2}{5\pi} \approx \frac{0.69315}{15.708} \approx 0.04412 \, \text{s}^{-1}$$
Since $\gamma = \frac{b}{2m}$:
$$b = 2 m \gamma = 2(0.2)(0.04412) \approx \mathbf{0.01765 \, \text{kg/s} = 1.765 \times 10^{-2} \, \text{N}\cdot\text{s/m}}$$

**Step 3: Quality Factor $Q$:**  
$$Q = \frac{\omega_0}{2\gamma} = \frac{20}{2(0.04412)} = \frac{20}{0.08825} \approx \mathbf{226.6}$$

**Step 4: Energy Dissipation Over 50 Cycles:**  
The total mechanical energy is proportional to the square of amplitude:
$$E(t) \propto A(t)^2 \implies \frac{E(t_{50})}{E_0} = \left(\frac{A(t_{50})}{A_0}\right)^2 = \left(\frac{1}{2}\right)^2 = \frac{1}{4}$$
The fraction of mechanical energy dissipated is:
$$\frac{\Delta E}{E_0} = 1 - \frac{1}{4} = \frac{3}{4} = \mathbf{75\%}$$
75% of the total initial mechanical energy has been converted into thermal dissipation!
""")

    # 2.5 Practice Challenge Problems
    parts.append(r"""## 2.5 High-Caliber Practice Challenge Problems & Analytical Solutions

### Challenge Problem 6.1: Hohmann Transfer and Non-Hohmann Interplanetary Interception
**Problem:** A spacecraft is in a circular parking orbit of radius $r_1$ around the Sun. It needs to reach a target planet in an outer circular orbit of radius $r_2 = 4 r_1$.
1. Compute the total velocity increment $\Delta v_{\text{total}} = \Delta v_1 + \Delta v_2$ required for a standard Hohmann transfer in units of the initial orbital speed $v_1 = \sqrt{GM/r_1}$.
2. If the spacecraft instead fires an impulsive burn at $r_1$ that puts it into a parabolic escape trajectory ($e = 1$) to cross the target orbit at $r_2$, find the required initial velocity boost $\Delta v_{\text{parabolic}}$ and compare the flight times.

#### Analytical Solution:
**Step 1: Hohmann Velocity Boosts:**  
Initial circular speed: $v_1 = \sqrt{\frac{GM}{r_1}}$.
Target circular speed: $v_2 = \sqrt{\frac{GM}{4r_1}} = \frac{1}{2} v_1$.
Semi-major axis of transfer orbit: $a_t = \frac{r_1 + 4r_1}{2} = 2.5 r_1$.
- Periapsis speed on transfer orbit:
  $$v_{t1} = \sqrt{GM\left(\frac{2}{r_1} - \frac{1}{2.5r_1}\right)} = \sqrt{\frac{GM}{r_1}\left(2 - 0.4\right)} = \sqrt{1.6} v_1 \approx 1.2649 v_1$$
  $$\Delta v_1 = v_{t1} - v_1 = (\sqrt{1.6} - 1) v_1 \approx \mathbf{0.2649 v_1}$$
- Apoapsis speed on transfer orbit:
  $$v_{t2} = \sqrt{GM\left(\frac{2}{4r_1} - \frac{1}{2.5r_1}\right)} = \sqrt{\frac{GM}{r_1}\left(0.5 - 0.4\right)} = \sqrt{0.1} v_1 \approx 0.3162 v_1$$
  $$\Delta v_2 = v_2 - v_{t2} = (0.5 - \sqrt{0.1}) v_1 \approx \mathbf{0.1838 v_1}$$
Total Hohmann cost:
$$\mathbf{\Delta v_{\text{total}} = (0.2649 + 0.1838) v_1 = 0.4487 v_1}$$

**Step 2: Hohmann Flight Time:**  
$$T_{\text{Hohmann}} = \pi \sqrt{\frac{a_t^3}{GM}} = \pi \sqrt{\frac{(2.5 r_1)^3}{GM}} = \pi (2.5)^{3/2} \sqrt{\frac{r_1^3}{GM}} \approx 3.9528 \pi \sqrt{\frac{r_1^3}{GM}}$$

**Step 3: Parabolic Flight Trajectory:**  
To achieve parabolic escape at $r_1$, the required speed is:
$$v_{\text{esc}} = \sqrt{\frac{2GM}{r_1}} = \sqrt{2} v_1 \approx 1.4142 v_1$$
The initial boost is:
$$\mathbf{\Delta v_{\text{parabolic}} = (\sqrt{2} - 1) v_1 \approx 0.4142 v_1}$$
By Barker's equation, the transit time to $r = 4r_1$ is:
$$t_{\text{parabolic}} = \frac{1}{3}\sqrt{\frac{2 r_1^3}{GM}} \left[ \tan\left(\frac{\nu}{2}\right) + \frac{1}{3}\tan^3\left(\frac{\nu}{2}\right) \right] \approx 1.886 \sqrt{\frac{r_1^3}{GM}}$$
This represents a **52% reduction in transit time** at the expense of requiring an active retro-burn to capture at the destination!

---

### Challenge Problem 6.2: Gravitational Field of a Massive Thin Torus
**Problem:** A uniform thin wire of total mass $M$ is formed into a circular ring of radius $R$. A small test mass $m$ is placed on the axis of the ring at distance $x$ from the ring's center.
1. Determine the axial gravitational field $g_x(x)$.
2. If the particle is displaced slightly in the transverse plane ($y$-direction) while maintaining $x = 0$, prove that the radial equilibrium at the ring center is unstable.
3. Formulate Earnshaw's Theorem for gravitational equilibria based on Laplace's equation.

#### Analytical Solution:
**Step 1: Axial Gravitational Field:**  
As derived in Section 2.1.2:
$$g_x(x) = -\frac{GM x}{(R^2 + x^2)^{3/2}}$$
For $x \ll R$:
$$g_x(x) \approx -\frac{GM}{R^3} x$$
Along the $x$-axis, the restoring force is linear, so the particle executes SHM with $\omega_x = \sqrt{\frac{GM}{R^3}}$.

**Step 2: Transverse In-Plane Stability Analysis:**  
Let the particle be displaced in the plane of the ring to $(0, y, 0)$ where $y \ll R$.
By Laplace's Equation in the vacuum interior around the center ($\rho = 0$):
$$\nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} + \frac{\partial^2 V}{\partial z^2} = 0$$
By circular symmetry in the $yz$-plane:
$$\frac{\partial^2 V}{\partial y^2} = \frac{\partial^2 V}{\partial z^2}$$
From the axial field:
$$\frac{\partial^2 V}{\partial x^2} = -\frac{\partial g_x}{\partial x} = \frac{GM}{R^3} > 0$$
Substituting into Laplace's equation:
$$\frac{GM}{R^3} + 2 \frac{\partial^2 V}{\partial y^2} = 0 \implies \mathbf{\frac{\partial^2 V}{\partial y^2} = -\frac{GM}{2R^3} < 0}$$
Because the second derivative is negative, the potential energy $U = m V$ has a **local maximum** in the transverse direction.
The transverse force is repulsive:
$$F_y = -m \frac{\partial V}{\partial y} \approx +m \left(\frac{GM}{2R^3}\right) y$$
Any infinitesimal transverse displacement $y$ grows exponentially!
*Earnshaw's Theorem:* A particle cannot be in stable static equilibrium in any direction under inverse-square gravitational forces alone, because $\nabla^2 V = 0$ forbids simultaneous local minima in all three spatial dimensions.

---

### Challenge Problem 6.3: Double Compound Pendulum Normal Modes
**Problem:** Two identical uniform thin rods, each of mass $M$ and length $L$, are coupled in series. The first rod is pivoted smoothly at one end to a fixed ceiling. The second rod is pivoted to the lower end of the first rod. Both rods oscillate in the same vertical plane.
Derive the coupled linear equations of motion for small angular deflections $(\theta_1, \theta_2)$ and compute the two normal mode frequencies.

#### Analytical Solution:
**Step 1: Kinetic Energy Formulation:**  
Let $\theta_1$ and $\theta_2$ be the angles of rods 1 and 2 from the vertical.
- Center of mass of rod 1: $(x_1, y_1) = \left(\frac{L}{2}\sin\theta_1, \frac{L}{2}\cos\theta_1\right)$.
- Center of mass of rod 2: $(x_2, y_2) = \left(L\sin\theta_1 + \frac{L}{2}\sin\theta_2, L\cos\theta_1 + \frac{L}{2}\cos\theta_2\right)$.
For small angles, velocities are:
$$\dot{x}_1 = \frac{L}{2}\dot{\theta}_1, \quad \dot{x}_2 = L\dot{\theta}_1 + \frac{L}{2}\dot{\theta}_2$$
The total kinetic energy is:
$$T = \left(\frac{1}{2} M \dot{x}_1^2 + \frac{1}{2} I_{cm} \dot{\theta}_1^2\right) + \left(\frac{1}{2} M \dot{x}_2^2 + \frac{1}{2} I_{cm} \dot{\theta}_2^2\right)$$
Using $I_{cm} = \frac{1}{12}ML^2$:
$$T = \frac{1}{6} M L^2 \dot{\theta}_1^2 + \frac{1}{2} M \left(L^2 \dot{\theta}_1^2 + \frac{L^2}{4}\dot{\theta}_2^2 + L^2 \dot{\theta}_1\dot{\theta}_2\right) + \frac{1}{24} M L^2 \dot{\theta}_2^2$$
$$T = \frac{1}{2} M L^2 \left[ \frac{4}{3}\dot{\theta}_1^2 + \frac{1}{3}\dot{\theta}_2^2 + \dot{\theta}_1\dot{\theta}_2 \right]$$

**Step 2: Potential Energy:**  
$$V = M g \frac{L}{2}(1 - \cos\theta_1) + M g \left[ L(1 - \cos\theta_1) + \frac{L}{2}(1 - \cos\theta_2) \right] \approx \frac{1}{2} M g L \left( 3\theta_1^2 + \theta_2^2 \right)$$

**Step 3: Linear Equations of Motion:**  
Applying Euler-Lagrange $\frac{d}{dt}\left(\frac{\partial T}{\partial \dot{\theta}_i}\right) + \frac{\partial V}{\partial \theta_i} = 0$:
$$\frac{4}{3} L \ddot{\theta}_1 + \frac{1}{2} L \ddot{\theta}_2 + \frac{3}{2} g \theta_1 = 0 \implies \frac{8}{3} L \ddot{\theta}_1 + L \ddot{\theta}_2 + 3 g \theta_1 = 0$$
$$\frac{1}{2} L \ddot{\theta}_1 + \frac{1}{3} L \ddot{\theta}_2 + \frac{1}{2} g \theta_2 = 0 \implies L \ddot{\theta}_1 + \frac{2}{3} L \ddot{\theta}_2 + g \theta_2 = 0$$

**Step 4: Normal Mode Eigenvalues:**  
Assuming harmonic solutions $\theta_1, \theta_2 \propto e^{i\omega t}$ and defining $\lambda = \frac{\omega^2 L}{g}$:
$$\det \begin{bmatrix} 3 - \frac{8}{3}\lambda & -\lambda \\ -\lambda & 1 - \frac{2}{3}\lambda \end{bmatrix} = 0$$
$$\left(3 - \frac{8}{3}\lambda\right)\left(1 - \frac{2}{3}\lambda\right) - \lambda^2 = 0 \implies 3 - 2\lambda - \frac{8}{3}\lambda + \frac{16}{9}\lambda^2 - \lambda^2 = 0$$
$$\frac{7}{9}\lambda^2 - \frac{14}{3}\lambda + 3 = 0 \implies 7\lambda^2 - 42\lambda + 27 = 0$$
Solving the quadratic formula:
$$\lambda = \frac{42 \pm \sqrt{1764 - 756}}{14} = \frac{42 \pm \sqrt{1008}}{14} = 3 \pm \frac{12\sqrt{7}}{14} = 3 \pm \frac{6\sqrt{7}}{7} \approx 3 \pm 2.2678$$
- Mode 1 (In-phase): $\lambda_1 \approx 0.7322 \implies \mathbf{\omega_1 \approx 0.8557 \sqrt{\frac{g}{L}}}$.
- Mode 2 (Out-of-phase): $\lambda_2 \approx 5.2678 \implies \mathbf{\omega_2 \approx 2.2952 \sqrt{\frac{g}{L}}}$.

---

### Challenge Problem 6.4: Oscillations of Liquid in a Variable Cross-Section U-Tube
**Problem:** A U-tube contains an incompressible, inviscid liquid of density $\rho$ and total mass $M$. The left vertical limb has uniform cross-sectional area $A_1$, and the right vertical limb has cross-sectional area $A_2$. The horizontal connecting tube of length $L$ has uniform area $A_0$.
Determine the natural frequency of small liquid oscillations.

#### Analytical Solution:
**Step 1: Kinematic Continuity:**  
Let the liquid surface in the left column be displaced downward by distance $y_1$.
By conservation of fluid volume:
$$\Delta V = A_1 y_1 = A_2 y_2 \implies y_2 = \frac{A_1}{A_2} y_1$$
The flow velocities in the sections are:
$$v_1 = \dot{y}_1, \quad v_2 = \dot{y}_2 = \frac{A_1}{A_2} \dot{y}_1, \quad v_0 = \frac{A_1}{A_0} \dot{y}_1$$

**Step 2: Total Mechanical Energy:**  
Total kinetic energy:
$$K = \frac{1}{2} (\rho A_1 h_1) v_1^2 + \frac{1}{2} (\rho A_2 h_2) v_2^2 + \frac{1}{2} (\rho A_0 L) v_0^2$$
$$K = \frac{1}{2} \rho A_1 \dot{y}_1^2 \left[ h_1 + h_2 \left(\frac{A_1}{A_2}\right) + L \left(\frac{A_1}{A_0}\right) \right]$$
Total potential energy relative to equilibrium:
$$U = \frac{1}{2} \rho g A_1 y_1^2 + \frac{1}{2} \rho g A_2 y_2^2 = \frac{1}{2} \rho g A_1 y_1^2 \left(1 + \frac{A_1}{A_2}\right)$$

**Step 3: Conservation of Energy:**  
Differentiating $K + U = \text{constant}$ with respect to time yields SHM:
$$\ddot{y}_1 + \omega^2 y_1 = 0$$
$$\mathbf{\omega = \sqrt{\frac{g \left(1 + \frac{A_1}{A_2}\right)}{h_1 + h_2 \frac{A_1}{A_2} + L \frac{A_1}{A_0}}}}$$

---

### Challenge Problem 6.5: Tidal Disruption Radius (The Roche Limit)
**Problem:** A spherical, self-gravitating liquid satellite of mass $m$ and radius $r$ orbits a massive primary planet of mass $M$ and radius $R$ in a circular orbit of radius $d$.
Derive the critical Roche Limit $d_{\text{Roche}}$ inside which the planet's tidal gravitational forces overcome the satellite's internal self-gravitation, causing the satellite to disintegrate.

#### Analytical Solution:
**Step 1: Tidal Gravitational Force Across the Satellite:**  
Consider a test mass $\Delta m$ on the satellite's surface closest to the primary planet.
Distance of satellite COM from planet: $d$.
Distance of test mass from planet: $d - r$.
The gravitational force exerted by the primary on $\Delta m$ is:
$$F_{\text{primary}} = \frac{G M \Delta m}{(d - r)^2} \approx \frac{G M \Delta m}{d^2} \left(1 + \frac{2r}{d}\right)$$
The orbital acceleration of the satellite COM is $a_{\text{orb}} = \frac{G M}{d^2}$.
In the non-inertial accelerating frame of the satellite COM, the net outward tidal pulling force on $\Delta m$ is:
$$F_{\text{tidal}} = F_{\text{primary}} - \Delta m \, a_{\text{orb}} = \frac{G M \Delta m}{d^2} \left(1 + \frac{2r}{d}\right) - \frac{G M \Delta m}{d^2} = \mathbf{\frac{2 G M \Delta m r}{d^3}}$$

**Step 2: Satellite's Internal Self-Gravitation:**  
The inward restoring gravitational attraction exerted by the satellite itself on $\Delta m$ at its surface is:
$$F_{\text{self}} = \frac{G m \Delta m}{r^2}$$

**Step 3: Tidal Disruption Threshold:**  
Disruption occurs when the outward tidal stretching force exceeds the inward self-gravitational binding:
$$F_{\text{tidal}} \ge F_{\text{self}} \implies \frac{2 G M \Delta m r}{d^3} \ge \frac{G m \Delta m}{r^2}$$
$$\frac{2 M r}{d^3} \ge \frac{m}{r^2} \implies d^3 \le 2 \frac{M}{m} r^3 \implies d \le r \left(\frac{2 M}{m}\right)^{1/3}$$

Expressing masses in terms of average bulk densities $\rho_{\text{planet}}$ and $\rho_{\text{sat}}$:
$$M = \frac{4}{3}\pi R^3 \rho_{\text{planet}}, \quad m = \frac{4}{3}\pi r^3 \rho_{\text{sat}} \implies \frac{M}{m} = \frac{R^3}{r^3} \left(\frac{\rho_{\text{planet}}}{\rho_{\text{sat}}}\right)$$
Substituting this ratio:
$$d_{\text{Roche}} = r \left[ 2 \frac{R^3}{r^3} \left(\frac{\rho_{\text{planet}}}{\rho_{\text{sat}}}\right) \right]^{1/3} = \mathbf{R \left(2 \frac{\rho_{\text{planet}}}{\rho_{\text{sat}}}\right)^{1/3}}$$
*(For a rigid satellite, $d_{\text{Roche}} \approx 1.26 R (\rho_p/\rho_s)^{1/3}$; for a fluid satellite accounting for tidal elongation into a prolate ellipsoid, Roche's exact hydrodynamic limit is $d_{\text{fluid}} \approx 2.44 R (\rho_p/\rho_s)^{1/3}$.)*
""")

    # 2.6 SVG Specifications
    parts.append(r"""## 2.6 Publication-Grade Diagram Specifications (Chapter 6)

### Diagram 6.1: Gravitational Potential & Field Profiles: Solid Sphere vs. Spherical Shell
- **SVG Canvas:** `viewBox="0 0 800 500"`
- **Palette:** Soft cream background `#fcfaf2`, solid sphere blue `#2563eb`, shell amber `#d97706`, axis slate `#475569`, text `#0f172a`.
- **Components:**
  1. **Two Coordinated Cartesian Plots:**
     - Left Plot: Gravitational Field Magnitude $g(r)$ vs. $r/R$.
       - Solid Sphere: Linear rise $g \propto r$ from $(0,0)$ to $(R, g_0)$, followed by $1/r^2$ decay.
       - Shell: Flat zero line $g = 0$ for $r < R$, abrupt jump to $g_0$ at $r = R$, followed by identical $1/r^2$ decay.
     - Right Plot: Gravitational Potential $V(r)$ vs. $r/R$.
       - Solid Sphere: Smooth concave parabola from $-1.5 V_0$ at $r=0$ to $-V_0$ at $r=R$, then $-1/r$ curve.
       - Shell: Completely flat horizontal line at $-V_0$ for $r \in [0, R]$, then $-1/r$ curve.
  2. **Boundary Discontinuity Markers:** Dashed vertical line at $r = R$ highlighting the derivative discontinuity in $V(r)$ and step discontinuity in $g(r)$ for the shell.

---

### Diagram 6.2: Vis-Viva Orbital Geometry & Hohmann Transfer Ellipse
- **SVG Canvas:** `viewBox="0 0 800 520"`
- **Palette:** Soft cream background `#fcfaf2`, primary Sun gold `#eab308`, inner orbit cyan `#0284c7`, outer orbit green `#16a34a`, transfer ellipse crimson `#dc2626`.
- **Components:**
  1. **Primary Body:** Central Sun at focal point $(320, 260)$.
  2. **Orbit 1 (Inner Circular):** Radius $r_1 = 90\text{px}$, cyan dashed line with velocity arrow $\mathbf{v}_{c1}$.
  3. **Orbit 2 (Outer Circular):** Radius $r_2 = 240\text{px}$, green dashed line with velocity arrow $\mathbf{v}_{c2}$.
  4. **Transfer Ellipse:** Red solid semi-ellipse tangent to Orbit 1 at Periapsis $P (230, 260)$ and tangent to Orbit 2 at Apoapsis $A (560, 260)$.
  5. **Velocity Boost Vectors:**
     - $\Delta \mathbf{v}_1$ tangent vector at $P$.
     - $\Delta \mathbf{v}_2$ tangent vector at $A$.
  6. **Geometric Callouts:** Semi-major axis $a_{\text{trans}} = (r_1 + r_2)/2$, transfer time $\pi\sqrt{a_t^3/GM}$.

---

### Diagram 6.3: Compound Pendulum $T(d)$ Conjugate Curves & Resonance Response
- **SVG Canvas:** `viewBox="0 0 800 500"`
- **Palette:** Soft cream background `#fcfaf2`, period curve purple `#7c3aed`, resonance amplitude crimson `#dc2626`, phase cyan `#0284c7`.
- **Components:**
  1. **Plot A (Left): Compound Pendulum $T(d)$ Curve:**
     - $x$-axis: Suspension distance $d$ from COM.
     - Asymptotes: $T \to \infty$ as $d \to 0$ and as $d \to \infty$.
     - Minimum point at $d = k_{cm}$, marked with horizontal dashed tangent $T_{\text{min}} = 2\pi\sqrt{2k_{cm}/g}$.
     - Horizontal secant line at $T > T_{\text{min}}$ intersecting the two branches at conjugate points $d_1$ and $d_2 = k_{cm}^2/d_1$.
  2. **Plot B (Right): Driven Resonance Curves:**
     - Family of amplitude curves $A(\omega)$ for low, medium, and critical damping.
     - Peak shift toward lower frequencies $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$.
     - Phase curve $\delta(\omega)$ crossing $\pi/2$ exactly at $\omega = \omega_0$.
""")

    return "\n\n".join(parts)

if __name__ == "__main__":
    ch6_text = build_chapter_6()
    print(f"Chapter 6 generated successfully. Total length: {len(ch6_text)} characters, {len(ch6_text.splitlines())} lines.")
