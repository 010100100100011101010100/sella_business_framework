# Authoritative Survey & Master Blueprint: Chapters 1 & 2
## JEE Main & Advanced Classical Mechanics & Rotational Dynamics Master Handbook

---

### Executive Overview & Pedagogical Scope
This document constitutes the comprehensive pedagogical and mathematical foundation for **Chapter 1 (Vectors, Calculus & Advanced 2D Kinematics)** and **Chapter 2 (Newton's Laws & Complex Friction Dynamics)** of the *JEE Main & Advanced Classical Mechanics Master Handbook*. 

Every topic is constructed from rigorous first-principles physics, incorporating:
1. Complete calculus and vector derivations (Cartesian, polar, tangential-normal coordinates; multi-variable constraints).
2. Master Formula Tables with exhaustive mathematical and physical domains of validity.
3. 10+ Numbered NTA/JEE Negative-Marking Trap Alerts per chapter detailing psychological failure modes, mathematical counter-examples, and definitive student rules.
4. Fully dissected JEE Advanced Previous Year Questions (PYQs) with step-by-step derivations and error diagnostics.
5. High-rigor Challenge Practice Problems with exhaustive analytical solutions.
6. Publication-grade SVG diagram specifications matching the book's soft warm paper aesthetic (`#fcfaf2` background, `#1e293b` ink, vibrant vector tints).

---

# PART 1: CHAPTER 1 — VECTORS, CALCULUS & ADVANCED 2D KINEMATICS

## 1.1 Complete Theoretical Framework & First-Principles Derivations

### 1.1.1 Curvilinear Coordinate Systems in Mechanics

In classical mechanics, the state of motion of a particle of mass $m$ is characterized by its position vector $\mathbf{r}(t)$, velocity $\mathbf{v}(t) = \frac{d\mathbf{r}}{dt}$, and acceleration $\mathbf{a}(t) = \frac{d^2\mathbf{r}}{dt^2}$ relative to a chosen inertial frame. The choice of coordinate basis defines the elegance and tractability of kinematic solutions.

#### 1. Cartesian Coordinate Basis ($\mathbb{R}^3$)
In standard Cartesian coordinates with fixed orthonormal basis vectors $\{\hat{i}, \hat{j}, \hat{k}\}$:
$$\mathbf{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$$
Since $\frac{d\hat{i}}{dt} = \frac{d\hat{j}}{dt} = \frac{d\hat{k}}{dt} = \mathbf{0}$:
$$\mathbf{v}(t) = \dot{x}\hat{i} + \dot{y}\hat{j} + \dot{z}\hat{k}$$
$$\mathbf{a}(t) = \ddot{x}\hat{i} + \ddot{y}\hat{j} + \ddot{z}\hat{k}$$
The motion decouples completely into three mutually independent 1D kinematic equations along the $x$, $y$, and $z$ axes.

#### 2. Plane Polar Coordinate Basis ($(r, \theta)$)
When a particle executes planar motion with central symmetry or rotational tendencies, Cartesian decomposition obscures the underlying physics. We define planar polar coordinates $(r, \theta)$ where:
$$x = r\cos\theta, \quad y = r\sin\theta$$
Here, $r \in [0, \infty)$ is the radial distance from the origin, and $\theta \in [0, 2\pi)$ is the counter-clockwise azimuth measured from the positive $x$-axis.

The position vector is:
$$\mathbf{r} = r\hat{r}$$
where the radial unit vector $\hat{r}$ and transverse (azimuthal) unit vector $\hat{\theta}$ are defined as:
$$\hat{r} = \cos\theta \hat{i} + \sin\theta \hat{j}$$
$$\hat{\theta} = -\sin\theta \hat{i} + \cos\theta \hat{j}$$
Notice that unlike Cartesian unit vectors, $\hat{r}$ and $\hat{\theta}$ are functions of time because they rotate with the particle's azimuthal coordinate $\theta(t)$.

**First-Principles Derivation of Unit Vector Derivatives:**
Differentiating $\hat{r}$ with respect to time $t$:
$$\frac{d\hat{r}}{dt} = \frac{d}{dt}(\cos\theta \hat{i} + \sin\theta \hat{j}) = (-\sin\theta \dot{\theta})\hat{i} + (\cos\theta \dot{\theta})\hat{j} = \dot{\theta} (-\sin\theta \hat{i} + \cos\theta \hat{j}) = \dot{\theta} \hat{\theta}$$
Similarly, differentiating $\hat{\theta}$:
$$\frac{d\hat{\theta}}{dt} = \frac{d}{dt}(-\sin\theta \hat{i} + \cos\theta \hat{j}) = (-\cos\theta \dot{\theta})\hat{i} - (\sin\theta \dot{\theta})\hat{j} = -\dot{\theta} (\cos\theta \hat{i} + \sin\theta \hat{j}) = -\dot{\theta} \hat{r}$$

**Velocity in Polar Coordinates:**
Applying the product rule to $\mathbf{r} = r\hat{r}$:
$$\mathbf{v} = \frac{d\mathbf{r}}{dt} = \frac{d}{dt}(r\hat{r}) = \dot{r}\hat{r} + r\frac{d\hat{r}}{dt} = \dot{r}\hat{r} + r\dot{\theta}\hat{\theta}$$
Thus, the velocity components are:
- Radial velocity: $v_r = \dot{r}$ (rate at which distance from origin increases)
- Transverse velocity: $v_\theta = r\dot{\theta} = r\omega$ (speed perpendicular to the position vector)
- Speed magnitude: $v = |\mathbf{v}| = \sqrt{\dot{r}^2 + (r\dot{\theta})^2}$

**Acceleration in Polar Coordinates:**
Differentiating velocity $\mathbf{v}$ with respect to time:
$$\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d}{dt}(\dot{r}\hat{r} + r\dot{\theta}\hat{\theta}) = \ddot{r}\hat{r} + \dot{r}\frac{d\hat{r}}{dt} + (\dot{r}\dot{\theta} + r\ddot{\theta})\hat{\theta} + r\dot{\theta}\frac{d\hat{\theta}}{dt}$$
Substituting $\frac{d\hat{r}}{dt} = \dot{\theta}\hat{\theta}$ and $\frac{d\hat{\theta}}{dt} = -\dot{\theta}\hat{r}$:
$$\mathbf{a} = \ddot{r}\hat{r} + \dot{r}(\dot{\theta}\hat{\theta}) + \dot{r}\dot{\theta}\hat{\theta} + r\ddot{\theta}\hat{\theta} + r\dot{\theta}(-\dot{\theta}\hat{r})$$
Collecting components along $\hat{r}$ and $\hat{\theta}$:
$$\mathbf{a} = (\ddot{r} - r\dot{\theta}^2)\hat{r} + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{\theta}$$

**Physical Dissection of the Four Terms:**
1. $\ddot{r}\hat{r}$: Linear radial acceleration (rate of change of radial speed).
2. $-r\dot{\theta}^2\hat{r}$: Centripetal acceleration (directed towards origin, arising because transverse velocity vector rotates).
3. $r\ddot{\theta}\hat{\theta}$: Angular acceleration contribution to transverse linear acceleration.
4. $2\dot{r}\dot{\theta}\hat{\theta}$: **Coriolis acceleration term**. It consists of two identical contributions $\dot{r}\dot{\theta}$: one from the change in direction of the radial velocity vector $\dot{r}\hat{r}$ as $\hat{r}$ rotates, and one from the change in magnitude of transverse velocity $r\dot{\theta}$ as the radial lever arm $r$ expands. This term is vital in rotating coordinate problems and central force mechanics.

#### 3. Tangential-Normal (Path / Intrinsic) Coordinates
When a particle moves along an arbitrary 2D curve $\mathcal{C}$ parametrized by arc length $s$, it is physically natural to resolve vectors along the curve's instantaneous tangent and normal:
- Unit tangent vector: $\hat{t} = \frac{d\mathbf{r}}{ds}$ pointing in the direction of instantaneous motion.
- Unit normal vector: $\hat{n}$ pointing towards the concave side (center of curvature), orthogonal to $\hat{t}$ ($\hat{t} \cdot \hat{n} = 0$).

Velocity is strictly directed along the tangent:
$$\mathbf{v} = \frac{d\mathbf{r}}{dt} = \frac{d\mathbf{r}}{ds} \frac{ds}{dt} = v\hat{t}, \quad \text{where } v = \frac{ds}{dt} = |\mathbf{v}|$$

Differentiating velocity with respect to time:
$$\mathbf{a} = \frac{d\mathbf{v}}{dt} = \frac{d(v\hat{t})}{dt} = \frac{dv}{dt}\hat{t} + v\frac{d\hat{t}}{dt}$$
By chain rule, $\frac{d\hat{t}}{dt} = \frac{d\hat{t}}{ds}\frac{ds}{dt} = v \frac{d\hat{t}}{ds}$.
From the Frenet-Serret formulas of differential geometry, the rate of change of the tangent vector with respect to arc length is proportional to the principal normal:
$$\frac{d\hat{t}}{ds} = \kappa \hat{n} = \frac{1}{R}\hat{n}$$
where $\kappa$ is the curvature and $R$ is the local radius of curvature of the trajectory.
Substituting this in:
$$\mathbf{a} = \frac{dv}{dt}\hat{t} + \frac{v^2}{R}\hat{n} = a_t\hat{t} + a_n\hat{n}$$
- **Tangential acceleration**: $a_t = \frac{dv}{dt} = \frac{d|\mathbf{v}|}{dt} = \frac{\mathbf{v} \cdot \mathbf{a}}{v}$. It is responsible *solely* for changing the speed of the particle.
- **Normal (centripetal) acceleration**: $a_n = \frac{v^2}{R} = \frac{|\mathbf{v} \times \mathbf{a}|}{v}$. It is responsible *solely* for changing the direction of the velocity vector.
- Total acceleration magnitude: $a = \sqrt{a_t^2 + a_n^2} = \sqrt{\left(\frac{dv}{dt}\right)^2 + \left(\frac{v^2}{R}\right)^2}$.

---

### 1.1.2 Advanced Calculus Applications in Kinematics

Kinematic equations $v = u + at$, $s = ut + \frac{1}{2}at^2$, and $v^2 = u^2 + 2as$ are valid **only** when acceleration is strictly constant. In JEE Advanced, acceleration is almost universally non-uniform: $a = a(t)$, $a = a(x)$, or $a = a(v)$.

#### 1. Time-Dependent Acceleration $a = f(t)$
Direct integration yields:
$$v(t) = v_0 + \int_0^t f(t') dt'$$
$$x(t) = x_0 + \int_0^t v(t') dt' = x_0 + v_0 t + \int_0^t \left(\int_0^{t'} f(\tau) d\tau\right) dt'$$

#### 2. Position-Dependent Acceleration $a = f(x)$
Using the chain rule transformation:
$$a = \frac{dv}{dt} = \frac{dv}{dx}\frac{dx}{dt} = v\frac{dv}{dx}$$
Separating variables:
$$v dv = f(x) dx \implies \int_{v_0}^v v' dv' = \int_{x_0}^x f(x') dx'$$
$$\frac{1}{2}v^2 - \frac{1}{2}v_0^2 = \int_{x_0}^x f(x') dx' \implies v(x) = \pm \sqrt{v_0^2 + 2\int_{x_0}^x f(x') dx'}$$
To find time as a function of position:
$$\frac{dx}{dt} = v(x) \implies t = \int_{x_0}^x \frac{dx'}{v(x')}$$
*Crucial turning point consideration*: Whenever $v(x) = 0$, the particle stops instantaneously and may reverse direction. The sign of $v(x)$ must be tracked piecewise.

#### 3. Velocity-Dependent Acceleration $a = f(v)$ (Resistive Media)
In a medium with drag (e.g. fluid resistance), $a$ is a function of $v$.
- To obtain $v(t)$:
  $$\frac{dv}{dt} = f(v) \implies t = \int_{v_0}^v \frac{dv'}{f(v')}$$
- To obtain $v(x)$ and stopping distance:
  $$v\frac{dv}{dx} = f(v) \implies x = \int_{v_0}^v \frac{v' dv'}{f(v')}$$

**Case A: Linear Drag ($F_{drag} = -mkv \implies a = -kv$)**
- Time response:
  $$\frac{dv}{dt} = -kv \implies \int_{v_0}^v \frac{dv'}{v'} = -kt \implies \ln\left(\frac{v}{v_0}\right) = -kt \implies v(t) = v_0 e^{-kt}$$
  The velocity approaches zero asymptotically as $t \to \infty$.
- Position response:
  $$v\frac{dv}{dx} = -kv \implies \frac{dv}{dx} = -k \implies \int_{v_0}^v dv' = -k \int_0^x dx' \implies v - v_0 = -kx$$
  $$v(x) = v_0 - kx$$
- Total stopping distance:
  Setting $v = 0$:
  $$x_{stop} = \frac{v_0}{k}$$
  *Remarkable Physical Result*: Although the particle takes infinite time to come to a mathematical stop ($t \to \infty$), it covers a strictly finite distance $x_{stop} = \frac{v_0}{k}$!

**Case B: Quadratic Drag ($F_{drag} = -m\beta v^2 \implies a = -\beta v^2$)**
- Time response:
  $$\frac{dv}{dt} = -\beta v^2 \implies \int_{v_0}^v \frac{dv'}{v'^2} = -\beta t \implies -\left[\frac{1}{v} - \frac{1}{v_0}\right] = -\beta t \implies v(t) = \frac{v_0}{1 + \beta v_0 t}$$
- Position response:
  $$v\frac{dv}{dx} = -\beta v^2 \implies \frac{dv}{v} = -\beta dx \implies \ln\left(\frac{v}{v_0}\right) = -\beta x \implies v(x) = v_0 e^{-\beta x}$$
- Distance analysis: Here, as $v \to 0$, $x \to \infty$. The particle never comes to a finite stopping distance without a threshold dry friction term.

**Case C: Vertical Motion under Gravity with Drag**
For upward motion with quadratic drag ($a = -g - \beta v^2$):
$$v \frac{dv}{dy} = -(g + \beta v^2) \implies \int_0^H dy = -\int_{u}^0 \frac{v dv}{g + \beta v^2}$$
$$H_{max} = \frac{1}{2\beta}\ln\left(1 + \frac{\beta u^2}{g}\right)$$
Comparing with zero drag ($H_0 = \frac{u^2}{2g}$): since $\ln(1+z) < z$ for all $z > 0$, $H_{max} < H_0$.
Terminal velocity during downward fall ($a = g - \beta v^2 = 0$):
$$v_T = \sqrt{\frac{g}{\beta}}$$

---

### 1.1.3 Relative Motion Framework in 2D

The relative position, velocity, and acceleration of particle $A$ with respect to frame/particle $B$ are defined by:
$$\mathbf{r}_{A/B} = \mathbf{r}_A - \mathbf{r}_B$$
$$\mathbf{v}_{A/B} = \mathbf{v}_A - \mathbf{v}_B$$
$$\mathbf{a}_{A/B} = \mathbf{a}_A - \mathbf{a}_B$$

#### 1. River-Swimmer Dynamics
Let the river flow along $+x$ with velocity $\mathbf{v}_r = v_r \hat{i}$. The banks are parallel to the $x$-axis, separated by width $d$.
Let the swimmer's velocity relative to water be $\mathbf{v}_{s/r}$ of magnitude $u = |\mathbf{v}_{s/r}|$.
Let the swimmer head at an angle $\theta$ upstream from the transverse direction (i.e. angle $\theta$ w.r.t the $y$-axis pointing towards $-x$):
$$\mathbf{v}_{s/r} = -u\sin\theta \hat{i} + u\cos\theta \hat{j}$$
The swimmer's ground velocity is:
$$\mathbf{v}_s = \mathbf{v}_{s/r} + \mathbf{v}_r = (v_r - u\sin\theta)\hat{i} + (u\cos\theta)\hat{j}$$
The time taken to cross the river depends *only* on the $y$-component of velocity:
$$t = \frac{d}{v_{s, y}} = \frac{d}{u\cos\theta}$$
The downstream drift $x$ upon reaching the opposite bank is:
$$x = v_{s, x} t = (v_r - u\sin\theta)\left(\frac{d}{u\cos\theta}\right) = d\left(\frac{v_r}{u}\sec\theta - \tan\theta\right)$$

**Condition for Shortest Time:**
To minimize $t = \frac{d}{u\cos\theta}$, we must maximize $\cos\theta \implies \theta = 0^\circ$.
- Heading: Perpendicular to the current ($\theta = 0^\circ$).
- Minimum crossing time: $t_{min} = \frac{d}{u}$.
- Drift at minimum time: $x = v_r t_{min} = \frac{v_r d}{u}$.

**Condition for Shortest Path (Minimum Drift):**
We analyze two distinct physical regimes:
- **Regime 1: $u \geq v_r$ (Swimmer faster than river)**
  Zero drift is achievable ($x = 0$):
  $$v_r - u\sin\theta = 0 \implies \sin\theta = \frac{v_r}{u}$$
  The crossing time for zero drift is:
  $$t = \frac{d}{u\cos\theta} = \frac{d}{u\sqrt{1 - \sin^2\theta}} = \frac{d}{\sqrt{u^2 - v_r^2}}$$
- **Regime 2: $u < v_r$ (River faster than swimmer)**
  Zero drift is mathematically impossible because $\sin\theta = v_r/u > 1$ has no real solutions. The current inevitably sweeps the swimmer downstream.
  To find the heading $\theta$ that yields minimum drift, we differentiate $x(\theta)$:
  $$\frac{dx}{d\theta} = d\left(\frac{v_r}{u}\sec\theta\tan\theta - \sec^2\theta\right) = \frac{d}{\cos^2\theta}\left(\frac{v_r}{u}\sin\theta - 1\right) = 0$$
  $$\sin\theta = \frac{u}{v_r}$$
  *Notice the profound inverted symmetry*: When $u \geq v_r$, $\sin\theta = v_r/u$; when $u < v_r$, $\sin\theta = u/v_r$!
  
  **Geometric Proof (Circle & Tangent Method):**
  In velocity space, the swimmer's ground velocity is $\mathbf{v}_s = \mathbf{v}_r + \mathbf{v}_{s/r}$.
  Plot $\mathbf{v}_r$ from the origin $O$ to point $P(v_r, 0)$. From $P$, the vector $\mathbf{v}_{s/r}$ of fixed radius $u$ can point in any direction, tracing a circle of radius $u$ centered at $P$.
  Since $u < v_r$, the origin $O(0,0)$ lies outside this circle. The ground velocity $\mathbf{v}_s$ connects $O$ to a point on the circle.
  To minimize drift, the angle between $\mathbf{v}_s$ and the bank must be maximized, meaning $\mathbf{v}_s$ must make the minimum angle with the $y$-axis. This occurs when the line from $O$ is **strictly tangent** to the circle of radius $u$!
  In the right triangle formed by $O$, the tangent point $T$, and the center $P$:
  - Hypotenuse $OP = v_r$
  - Perpendicular side $PT = u$
  - The angle opposite to $PT$ satisfies: $\sin\alpha = \frac{u}{v_r}$.
  - Ground velocity magnitude: $v_s = \sqrt{v_r^2 - u^2}$.
  - Minimum drift:
    $$x_{min} = d \cot\alpha = d \frac{\sqrt{v_r^2 - u^2}}{u}$$

#### 2. Rain-Man Problem with Moving & Accelerating Observer
Let rain fall with velocity $\mathbf{v}_r = v_{rx}\hat{i} - v_{ry}\hat{j}$ relative to the ground.
Let an observer move with velocity $\mathbf{v}_m(t) = v_m(t)\hat{i}$.
The relative velocity of rain with respect to the observer is:
$$\mathbf{v}_{r/m} = \mathbf{v}_r - \mathbf{v}_m = (v_{rx} - v_m)\hat{i} - v_{ry}\hat{j}$$
To block the incoming rain, the umbrella must be aligned parallel to $-\mathbf{v}_{r/m}$:
$$\mathbf{v}_{umbrella} \parallel -\mathbf{v}_{r/m} = (v_m - v_{rx})\hat{i} + v_{ry}\hat{j}$$
The angle $\phi$ that the umbrella must make with the vertical is:
$$\tan\phi = \frac{v_m - v_{rx}}{v_{ry}}$$
If the man accelerates with constant acceleration $a$, then $v_m(t) = v_0 + at$, and:
$$\phi(t) = \arctan\left(\frac{v_0 + at - v_{rx}}{v_{ry}}\right)$$
Differentiating with respect to time gives the rate of tilt:
$$\frac{d\phi}{dt} = \frac{1}{1 + \left(\frac{v_0 + at - v_{rx}}{v_{ry}}\right)^2} \frac{a}{v_{ry}} = \frac{a v_{ry}}{v_{ry}^2 + (v_m(t) - v_{rx})^2}$$

#### 3. Relative Motion Between Two Projectiles in Free Fall
Consider two projectiles $1$ and $2$ launched with initial velocities $\mathbf{u}_1$ and $\mathbf{u}_2$ from initial positions $\mathbf{r}_{01}$ and $\mathbf{r}_{02}$ under uniform gravity $\mathbf{g} = -g\hat{j}$.
The accelerations are:
$$\mathbf{a}_1 = -g\hat{j}, \quad \mathbf{a}_2 = -g\hat{j}$$
The relative acceleration is:
$$\mathbf{a}_{rel} = \mathbf{a}_1 - \mathbf{a}_2 = (-g\hat{j}) - (-g\hat{j}) = \mathbf{0}$$
*Fundamental Theorem of Free-Fall Relative Motion*:
In a uniform gravitational field without air resistance, the relative acceleration between any two freely falling particles is **identically zero**. Therefore, the relative motion observed from one projectile looking at the other is **pure uniform motion in a straight line at constant velocity**:
$$\mathbf{v}_{rel}(t) = \mathbf{u}_1 - \mathbf{u}_2 = \mathbf{u}_{rel} = \text{constant}$$
$$\mathbf{r}_{rel}(t) = \mathbf{r}_{0, rel} + \mathbf{u}_{rel} t$$
where $\mathbf{r}_{0, rel} = \mathbf{r}_{01} - \mathbf{r}_{02}$.

**Collision Condition:**
For the two projectiles to collide at time $t_{coll} > 0$:
$$\mathbf{r}_{rel}(t_{coll}) = \mathbf{0} \implies \mathbf{r}_{0, rel} + \mathbf{u}_{rel} t_{coll} = \mathbf{0} \implies \mathbf{u}_{rel} = -\frac{\mathbf{r}_{0, rel}}{t_{coll}}$$
This proves that:
1. $\mathbf{u}_{rel}$ must be directed strictly anti-parallel to $\mathbf{r}_{0, rel}$.
2. The cross-product condition for collision is:
   $$\mathbf{r}_{0, rel} \times \mathbf{u}_{rel} = \mathbf{0}$$
3. The collision time is:
   $$t_{coll} = \frac{|\mathbf{r}_{0, rel}|}{|\mathbf{u}_{rel}|}$$
   provided that both projectiles are still airborne at $t = t_{coll}$ ($y_1(t_{coll}) \geq 0$ and $y_2(t_{coll}) \geq 0$).

**Distance and Time of Closest Approach:**
If they do not collide, the distance between them at time $t$ is:
$$D^2(t) = |\mathbf{r}_{rel}(t)|^2 = (\mathbf{r}_0 + \mathbf{u}_{rel} t) \cdot (\mathbf{r}_0 + \mathbf{u}_{rel} t) = r_0^2 + 2(\mathbf{r}_0 \cdot \mathbf{u}_{rel})t + u_{rel}^2 t^2$$
To find the minimum distance, differentiate with respect to $t$:
$$\frac{d(D^2)}{dt} = 2(\mathbf{r}_0 \cdot \mathbf{u}_{rel}) + 2 u_{rel}^2 t = 0 \implies t_{min} = -\frac{\mathbf{r}_{0, rel} \cdot \mathbf{u}_{rel}}{u_{rel}^2}$$
For $t_{min} > 0$, we require $\mathbf{r}_{0, rel} \cdot \mathbf{u}_{rel} < 0$ (they must be approaching initially).
Substituting $t_{min}$ back into the distance equation:
$$D_{min}^2 = r_0^2 - \frac{(\mathbf{r}_0 \cdot \mathbf{u}_{rel})^2}{u_{rel}^2} = \frac{r_0^2 u_{rel}^2 - (\mathbf{r}_0 \cdot \mathbf{u}_{rel})^2}{u_{rel}^2} = \frac{|\mathbf{r}_{0, rel} \times \mathbf{u}_{rel}|^2}{u_{rel}^2}$$
$$D_{min} = \frac{|\mathbf{r}_{0, rel} \times \mathbf{u}_{rel}|}{|\mathbf{u}_{rel}|}$$
Geometrically, $D_{min}$ is the length of the perpendicular dropped from the origin onto the relative trajectory line $\mathbf{r}_{rel}(t)$.

---

### 1.1.4 Projectile Motion on Inclined Planes

Consider a planar incline of inclination angle $\beta$ to the horizontal. A particle is projected from the incline with speed $u$ at an angle $\alpha$ relative to the incline surface.

```
                  ^ y' (perpendicular to incline)
                  |    /
                  |   /  u (velocity)
                  |  / ) alpha
                  | /
------------------+--------------------> x' (along incline)
                / | \
               /  |  \
              /   |   \  beta (incline angle)
             /    v g  \
            /           \
```

#### 1. Motion Up the Incline
Choose rotated Cartesian coordinate axes:
- $x'$-axis: along the incline directed upwards.
- $y'$-axis: perpendicular to the incline directed upwards.

Resolving the acceleration due to gravity $\mathbf{g}$ along these axes:
$$a_{x'} = -g\sin\beta, \quad a_{y'} = -g\cos\beta$$
Initial velocity components:
$$u_{x'} = u\cos\alpha, \quad u_{y'} = u\sin\alpha$$

**Time of Flight ($T_{up}$):**
The particle lands on the incline when its displacement perpendicular to the incline returns to zero: $y'(T) = 0$.
$$y'(T) = u_{y'} T + \frac{1}{2}a_{y'} T^2 = 0 \implies u\sin\alpha T - \frac{1}{2}g\cos\beta T^2 = 0$$
Since $T > 0$:
$$T_{up} = \frac{2u\sin\alpha}{g\cos\beta}$$

**Range Along the Incline ($R_{up}$):**
The range $R_{up}$ is the displacement along the $x'$-axis at $t = T_{up}$:
$$R_{up} = x'(T) = u_{x'} T + \frac{1}{2}a_{x'} T^2 = (u\cos\alpha)\left(\frac{2u\sin\alpha}{g\cos\beta}\right) - \frac{1}{2}(g\sin\beta)\left(\frac{2u\sin\alpha}{g\cos\beta}\right)^2$$
Factoring out $\frac{2u^2\sin\alpha}{g\cos^2\beta}$:
$$R_{up} = \frac{2u^2\sin\alpha}{g\cos^2\beta} [\cos\alpha\cos\beta - \sin\alpha\sin\beta] = \frac{2u^2\sin\alpha\cos(\alpha+\beta)}{g\cos^2\beta}$$
Using the trigonometric product-to-sum identity $2\sin A \cos B = \sin(A+B) + \sin(A-B)$:
$$2\sin\alpha\cos(\alpha+\beta) = \sin(2\alpha+\beta) - \sin\beta$$
Thus, the master range formula up the incline is:
$$R_{up} = \frac{u^2}{g\cos^2\beta}[\sin(2\alpha + \beta) - \sin\beta]$$

**Condition for Maximum Range Up the Incline:**
Since $u$, $g$, and $\beta$ are fixed, $R_{up}$ is maximized when $\sin(2\alpha + \beta) = 1$:
$$2\alpha + \beta = \frac{\pi}{2} \implies \alpha_{max} = \frac{\pi}{4} - \frac{\beta}{2}$$
Substituting this into the range equation:
$$R_{max, up} = \frac{u^2}{g\cos^2\beta}[1 - \sin\beta] = \frac{u^2(1 - \sin\beta)}{g(1 - \sin^2\beta)} = \frac{u^2(1 - \sin\beta)}{g(1 - \sin\beta)(1 + \sin\beta)}$$
$$R_{max, up} = \frac{u^2}{g(1 + \sin\beta)}$$

**Condition for Striking the Incline Perpendicularly:**
At the instant of impact $t = T_{up}$, the velocity vector must be purely normal to the incline, which means its component along the incline must vanish:
$$v_{x'}(T_{up}) = 0$$
$$u_{x'} + a_{x'} T_{up} = 0 \implies u\cos\alpha - (g\sin\beta)\left(\frac{2u\sin\alpha}{g\cos\beta}\right) = 0$$
$$u\cos\alpha = 2u\sin\alpha\tan\beta \implies \cot\alpha = 2\tan\beta$$
$$\tan\alpha = \frac{1}{2}\cot\beta \iff 2\tan\alpha\tan\beta = 1$$

**Condition for Striking the Incline Horizontally:**
At impact, the velocity vector $\mathbf{v}$ makes an angle of $0^\circ$ with the horizontal. In the rotated frame, the horizontal line makes an angle of $-\beta$ with the $x'$-axis.
Therefore:
$$\tan(-\beta) = \frac{v_{y'}(T)}{v_{x'}(T)}$$
Since $v_{y'}(T) = -u_{y'} = -u\sin\alpha$, and $v_{x'}(T) = u\cos\alpha - g\sin\beta T$:
$$-\tan\beta = \frac{-u\sin\alpha}{u\cos\alpha - 2u\sin\alpha\tan\beta} \implies \tan\beta (u\cos\alpha - 2u\sin\alpha\tan\beta) = u\sin\alpha$$
Dividing by $u\cos\alpha$:
$$\tan\beta(1 - 2\tan\alpha\tan\beta) = \tan\alpha \implies \tan\alpha(1 + 2\tan^2\beta) = \tan\beta$$
$$\tan\alpha = \frac{\tan\beta}{1 + 2\tan^2\beta}$$

#### 2. Motion Down the Incline
When the particle is projected down an incline of angle $\beta$ with speed $u$ at angle $\alpha$ to the incline surface, we choose the $x'$-axis pointing downwards along the incline and $y'$-axis normal pointing upwards.
The acceleration components are:
$$a_{x'} = +g\sin\beta, \quad a_{y'} = -g\cos\beta$$
Initial velocity:
$$u_{x'} = u\cos\alpha, \quad u_{y'} = u\sin\alpha$$
The time of flight is identical to the upward case:
$$T_{down} = \frac{2u\sin\alpha}{g\cos\beta}$$
The range down the incline is:
$$R_{down} = u_{x'} T + \frac{1}{2}a_{x'} T^2 = \frac{u^2}{g\cos^2\beta}[\sin(2\alpha - \beta) + \sin\beta]$$
Maximum range down the incline occurs when $\sin(2\alpha - \beta) = 1$:
$$2\alpha - \beta = \frac{\pi}{2} \implies \alpha_{max} = \frac{\pi}{4} + \frac{\beta}{2}$$
$$R_{max, down} = \frac{u^2}{g(1 - \sin\beta)}$$

---

### 1.1.5 Radius of Curvature: Differential & Physical Formulations

The radius of curvature $R$ of a particle's trajectory at any point is the radius of the **osculating circle** that best approximates the curve at that point.

#### 1. Kinematic / Physical Formulation
The normal acceleration component $a_\perp$ is related to the instantaneous speed $v$ and radius of curvature $R$ by:
$$a_n = a_\perp = \frac{v^2}{R} \implies R = \frac{v^2}{a_\perp}$$
where $a_\perp$ is the magnitude of the component of acceleration perpendicular to the instantaneous velocity vector:
$$a_\perp = |\mathbf{a} \times \hat{v}| = \frac{|\mathbf{v} \times \mathbf{a}|}{v}$$
Substituting this into the radius formula gives the invariant vector form:
$$R = \frac{v^3}{|\mathbf{v} \times \mathbf{a}|}$$

#### 2. Rigorous Derivation of the Cartesian Calculus Formula
Let the trajectory of a particle be given by the function $y = f(x)$.
Let $\psi$ be the angle that the tangent line makes with the $x$-axis:
$$\tan\psi = \frac{dy}{dx} = y'$$
The arc length element $ds$ is related to $dx$ and $dy$ by:
$$ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + (y')^2} dx$$
By definition, the curvature $\kappa = \frac{1}{R}$ is the rate of change of the tangent direction with respect to arc length:
$$\kappa = \frac{1}{R} = \left|\frac{d\psi}{ds}\right|$$
Using the chain rule:
$$\frac{d\psi}{ds} = \frac{d\psi}{dx}\frac{dx}{ds} = \frac{d\psi}{dx} \frac{1}{\sqrt{1 + (y')^2}}$$
Differentiating $\tan\psi = y'$ with respect to $x$:
$$\sec^2\psi \frac{d\psi}{dx} = y'' \implies \frac{d\psi}{dx} = \frac{y''}{\sec^2\psi} = \frac{y''}{1 + \tan^2\psi} = \frac{y''}{1 + (y')^2}$$
Substituting $\frac{d\psi}{dx}$ into the curvature expression:
$$\kappa = \frac{1}{R} = \left|\frac{\frac{y''}{1 + (y')^2}}{\sqrt{1 + (y')^2}}\right| = \frac{|y''|}{(1 + (y')^2)^{3/2}}$$
Inverting yields the classic differential geometry formula:
$$R = \frac{\left[1 + \left(\frac{dy}{dx}\right)^2\right]^{3/2}}{\left|\frac{d^2y}{dx^2}\right|}$$

#### 3. General Parametric Form ($x(t), y(t)$)
When coordinates are parametrized by time $t$:
$$\dot{x} = \frac{dx}{dt}, \quad \dot{y} = \frac{dy}{dt} \implies v = \sqrt{\dot{x}^2 + \dot{y}^2}$$
The acceleration components are $\ddot{x}$ and $\ddot{y}$.
The 2D cross product $\mathbf{v} \times \mathbf{a}$ is:
$$\mathbf{v} \times \mathbf{a} = (\dot{x}\hat{i} + \dot{y}\hat{j}) \times (\ddot{x}\hat{i} + \ddot{y}\hat{j}) = (\dot{x}\ddot{y} - \dot{y}\ddot{x})\hat{k}$$
$$|\mathbf{v} \times \mathbf{a}| = |\dot{x}\ddot{y} - \dot{y}\ddot{x}|$$
Substituting into $R = \frac{v^3}{|\mathbf{v} \times \mathbf{a}|}$:
$$R = \frac{(\dot{x}^2 + \dot{y}^2)^{3/2}}{|\dot{x}\ddot{y} - \dot{y}\ddot{x}|}$$

#### 4. Application to Standard Physics Trajectories
- **Standard Projectile Motion at Apex:**
  At the peak, velocity is horizontal: $v = u\cos\theta$.
  Acceleration is purely vertical: $a = g$, and since $\mathbf{v} \perp \mathbf{a}$, $a_\perp = g$.
  $$R_{apex} = \frac{(u\cos\theta)^2}{g} = \frac{u^2\cos^2\theta}{g}$$
- **Standard Projectile Motion at Launch Point:**
  At launch, speed is $v = u$, velocity is at angle $\theta$ above horizontal.
  Acceleration is $g$ downwards. The component perpendicular to velocity is $a_\perp = g\cos\theta$.
  $$R_{launch} = \frac{u^2}{g\cos\theta}$$

## 1.2 Master Formula Summary Table: Kinematics & Vectors

| Formula | Description | Mathematical Domain of Validity | Physical Domain of Validity / Restrictions |
| :--- | :--- | :--- | :--- |
| $\mathbf{v} = \dot{r}\hat{r} + r\dot{\theta}\hat{\theta}$ | Velocity in planar polar coordinates | $r(t), \theta(t) \in C^1$, $r > 0$ | Strictly 2D planar motion; origin must not pass through the particle ($r \neq 0$). |
| $\mathbf{a} = (\ddot{r} - r\dot{\theta}^2)\hat{r} + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{\theta}$ | Acceleration in planar polar coordinates | $r(t), \theta(t) \in C^2$, $r > 0$ | Strictly 2D planar motion; inertial frame with fixed origin. |
| $\mathbf{a} = \frac{dv}{dt}\hat{t} + \frac{v^2}{R}\hat{n}$ | Acceleration in intrinsic path coordinates | Trajectory curve $\mathcal{C} \in C^2$, curvature $\kappa = 1/R$ well-defined | Speed $v > 0$; $R$ is local radius of curvature; $\hat{n}$ points towards concave side. Inapplicable at inflection points where $R \to \infty$. |
| $v dv = a(x) dx$ | Position-dependent acceleration quadrature | $a(x)$ integrable, $v(x)$ single-valued on domain | Valid along a monotonic segment of motion. Fails across turning points ($v=0$) unless split into piecewise branches. |
| $v(t) = v_0 e^{-kt}, \; x_{stop} = \frac{v_0}{k}$ | Linear drag velocity and stopping distance | $k > 0$, $v(t) \geq 0$ | Laminar flow (low Reynolds number $Re < 1$). Particle stops at $x = v_0/k$ as $t \to \infty$. |
| $v(t) = \frac{v_0}{1 + \beta v_0 t}, \; v(x) = v_0 e^{-\beta x}$ | Quadratic drag velocity and spatial decay | $\beta > 0$, $v_0 > 0$ | High Reynolds number turbulent drag ($Re > 10^3$). Mathematical stopping distance is infinite ($x \to \infty$ as $v \to 0$). |
| $t_{cross} = \frac{d}{u\cos\theta}$ | River crossing time | $u > 0$, $\theta \in (-\pi/2, \pi/2)$ | Uniform river flow; straight parallel banks separated by width $d$; swimmer maintains constant heading $\theta$ upstream from normal. |
| $x_{min} = d \frac{\sqrt{v_r^2 - u^2}}{u}$ | Minimum drift when $u < v_r$ | $0 < u < v_r$ | Swimmer's speed $u$ strictly less than river speed $v_r$. Heading angle must satisfy $\sin\theta = u/v_r$. |
| $T = \frac{2u\sin\alpha}{g\cos\beta}$ | Time of flight on inclined plane | $g > 0$, $\beta \in [0, \pi/2)$, $\alpha \in (0, \pi)$ | Constant gravitational field; planar incline; zero aerodynamic drag; launch from incline surface. |
| $R_{up} = \frac{u^2}{g\cos^2\beta}[\sin(2\alpha+\beta) - \sin\beta]$ | Range up the incline | $\beta \in [0, \pi/2)$, $\alpha \in (0, \pi - \beta)$ | Zero air drag; flat incline; $\alpha$ measured relative to incline surface; $\beta$ is incline angle to horizontal. |
| $\alpha_{max, up} = \frac{\pi}{4} - \frac{\beta}{2}, \; R_{max, up} = \frac{u^2}{g(1 + \sin\beta)}$ | Maximum range up incline | $\beta \in [0, \pi/2)$ | Particle launched uphill; valid for all launch speeds $u$. |
| $2\tan\alpha\tan\beta = 1$ | Perpendicular landing on inclined plane | $\beta \in (0, \pi/2)$, $\alpha \in (0, \pi/2)$ | Incline must have non-zero slope ($\beta \neq 0$); launch angle $\alpha$ w.r.t incline. Velocity component along incline vanishes ($v_x = 0$) at impact. |
| $R = \frac{v^2}{a_\perp} = \frac{v^3}{|\mathbf{v} \times \mathbf{a}|}$ | Radius of curvature (kinematic) | $v > 0$, $a_\perp > 0$ | General 3D or 2D trajectories. Fails along straight paths where $a_\perp = 0$ ($R \to \infty$). |
| $R = \frac{[1 + (y')^2]^{3/2}}{|y''|}$ | Radius of curvature (Cartesian) | $y(x) \in C^2$, $y'' \neq 0$ | Trajectory expressible as a single-valued function $y(x)$ with non-vertical tangent ($|y'| < \infty$). |
| $\mathbf{a}_{rel} = \mathbf{0}, \; \mathbf{r}_{rel}(t) = \mathbf{r}_0 + \mathbf{v}_{rel} t$ | Relative motion of two projectiles | Constant uniform gravitational field $\mathbf{g}$ | Negligible air resistance; both particles in free flight simultaneously. |
| $D_{min} = \frac{|\mathbf{r}_0 \times \mathbf{v}_{rel}|}{|\mathbf{v}_{rel}|}$ | Closest approach distance between projectiles | $|\mathbf{v}_{rel}| \neq 0$ | Distance of closest approach occurs at $t_{min} = -\frac{\mathbf{r}_0 \cdot \mathbf{v}_{rel}}{v_{rel}^2}$. Valid only if $t_{min} \geq 0$ and both particles remain airborne at $t_{min}$. |

---

## 1.3 NTA / JEE Negative-Marking Trap Alerts (Chapter 1)

### ⚠️ Trap Alert 1.1: Confusing Rate of Change of Speed with Magnitude of Acceleration
- **The Trap**: Assuming that $\frac{d|\mathbf{v}|}{dt} = |\mathbf{a}|$, or equivalently, thinking that if speed is constant, acceleration must be zero.
- **Why Students Fall For It**: The notation $a = \frac{dv}{dt}$ is carelessly used in school physics for 1D motion, leading students to conflate scalar speed $v = |\mathbf{v}|$ with vector velocity $\mathbf{v}$.
- **Mathematical Reality**:
  $$\mathbf{a} = \frac{dv}{dt}\hat{t} + \frac{v^2}{R}\hat{n} \implies |\mathbf{a}| = \sqrt{\left(\frac{dv}{dt}\right)^2 + \left(\frac{v^2}{R}\right)^2}$$
  Therefore, $\frac{d|\mathbf{v}|}{dt} = a_t = \frac{\mathbf{v} \cdot \mathbf{a}}{|\mathbf{v}|} \leq |\mathbf{a}|$. Equality holds **if and only if** $a_n = 0$ (pure rectilinear motion). In uniform circular motion, speed is constant ($\frac{d|\mathbf{v}|}{dt} = 0$), yet $|\mathbf{a}| = \frac{v^2}{R} \neq 0$!
- **IITian Rule**: Never equate $|\mathbf{a}|$ to $\frac{dv}{dt}$ unless you have explicitly verified that the trajectory is a straight line. Always compute $a_t = \frac{\mathbf{v} \cdot \mathbf{a}}{v}$ and $a_n = \frac{|\mathbf{v} \times \mathbf{a}|}{v}$.

---

### ⚠️ Trap Alert 1.2: Blind Integration of $\int v dt$ to Find Distance Instead of Displacement
- **The Trap**: Evaluating $\int_{t_1}^{t_2} v(t) dt$ and labeling the result as "distance travelled."
- **Why Students Fall For It**: In 1D motion where the particle never turns back, displacement equals distance. Students forget to check whether $v(t)$ crosses zero.
- **Mathematical Reality**:
  $$\text{Displacement} = \Delta x = \int_{t_1}^{t_2} v(t) dt$$
  $$\text{Distance} = s = \int_{t_1}^{t_2} |v(t)| dt$$
  If $v(t) = 6 - 2t$, the displacement from $t = 0$ to $t = 5$ is $\int_0^5 (6 - 2t) dt = [6t - t^2]_0^5 = 30 - 25 = 5\text{ m}$.
  However, $v(t) = 0$ at $t = 3\text{ s}$. The particle moves forward for $t \in [0, 3]$ ($\Delta x_1 = 9\text{ m}$) and moves backward for $t \in [3, 5]$ ($\Delta x_2 = -4\text{ m}$).
  The actual distance is $9 + |-4| = 13\text{ m}$!
- **IITian Rule**: Whenever asked for "distance travelled" or "average speed", immediately locate all roots of $v(t) = 0$ within the integration interval and integrate $|v(t)|$ piecewise.

---

### ⚠️ Trap Alert 1.3: Angle Confusion on Inclined Plane Projectiles ($\alpha$ vs $\theta = \alpha + \beta$)
- **The Trap**: Plugging the launch angle w.r.t the horizontal into the incline range formula, or confusing $\alpha$ (angle w.r.t the incline) with $\theta$ (angle w.r.t the horizontal).
- **Why Students Fall For It**: In standard ground projectiles, launch angle is measured from the horizontal. In incline problems, the formula $R = \frac{u^2}{g\cos^2\beta}[\sin(2\alpha+\beta) - \sin\beta]$ explicitly defines $\alpha$ as the angle between the initial velocity vector and the incline surface.
- **Mathematical Reality**:
  If a problem states "a projectile is launched at $60^\circ$ to the horizontal on an incline of $30^\circ$":
  $$\theta = 60^\circ, \quad \beta = 30^\circ \implies \alpha = \theta - \beta = 60^\circ - 30^\circ = 30^\circ$$
  Plugging $\alpha = 60^\circ$ into the incline formula leads to completely incorrect answers (and matches the exact distractor option set by the JEE paper-setter!).
- **IITian Rule**: Always draw the rotated coordinate frame. Write $\alpha = \theta_{horizontal} - \beta$ explicitly before writing any kinematic formula.

---

### ⚠️ Trap Alert 1.4: Misinterpreting the "Perpendicular Impact" Condition on an Incline
- **The Trap**: Setting $v_y = 0$ or setting $\mathbf{v} \cdot \mathbf{g} = 0$ when the projectile lands perpendicular to the incline.
- **Why Students Fall For It**: Students confuse the apex condition of a standard projectile ($v_y = 0$) with landing perpendicularly on an incline.
- **Mathematical Reality**:
  When a projectile strikes an incline perpendicularly, its velocity vector is normal to the incline surface. In our rotated coordinate system ($x'$ along incline, $y'$ normal to incline):
  $$\mathbf{v}(T) = v_{x'}\hat{i}' + v_{y'}\hat{j}' \implies v_{x'}(T) = 0, \quad v_{y'}(T) \neq 0$$
  Setting $v_{x'} = 0$ yields $u\cos\alpha - g\sin\beta T = 0 \implies 2\tan\alpha\tan\beta = 1$.
  If a student sets $v_{y'} = 0$, that corresponds to grazing the incline tangentially, not striking it perpendicularly!
- **IITian Rule**: Striking an incline perpendicularly means zero velocity along the incline: $v_{\parallel} = 0$.

---

### ⚠️ Trap Alert 1.5: The River-Swimmer "Zero Drift Fallacy" When $u < v_r$
- **The Trap**: Writing $\sin\theta = v_r / u$ when the river speed $v_r$ exceeds the swimmer's speed $u$, concluding that the angle does not exist and therefore drift is unbounded or undetermined.
- **Why Students Fall For It**: Memorizing the zero-drift formula $\sin\theta = v_r/u$ without understanding that it requires $u \geq v_r$.
- **Mathematical Reality**:
  When $u < v_r$, zero drift is impossible. To achieve *minimum* (non-zero) drift, one must minimize $x(\theta) = d\left(\frac{v_r}{u}\sec\theta - \tan\theta\right)$.
  Setting $\frac{dx}{d\theta} = 0$ yields:
  $$\sin\theta = \frac{u}{v_r}$$
  The minimum drift is strictly $x_{min} = d \frac{\sqrt{v_r^2 - u^2}}{u}$.
- **IITian Rule**: Always compare swimmer speed $u$ with river speed $v_r$ first:
  - If $u \geq v_r$: Shortest path has $x_{min} = 0$ at $\sin\theta = v_r / u$.
  - If $u < v_r$: Shortest path has $x_{min} = d\frac{\sqrt{v_r^2 - u^2}}{u}$ at $\sin\theta = u / v_r$.

---

### ⚠️ Trap Alert 1.6: Umbrella Orientation in Relative Rain Motion
- **The Trap**: Holding the umbrella along the vector direction of $\mathbf{v}_{r/m}$ instead of $-\mathbf{v}_{r/m}$, resulting in a $180^\circ$ reversal of the protection angle.
- **Why Students Fall For It**: Confusing the direction from which rain arrives with the direction towards which rain moves.
- **Mathematical Reality**:
  If rain falls vertically ($\mathbf{v}_r = -v_r \hat{j}$) and a man runs forward ($\mathbf{v}_m = v_m \hat{i}$):
  $$\mathbf{v}_{r/m} = -v_m \hat{i} - v_r \hat{j}$$
  The rain appears to move *downwards and backwards* towards the man. Therefore, to intercept the incoming rain droplets, the umbrella handle must point towards the origin from the droplet's incoming vector:
  $$\mathbf{v}_{umbrella} \parallel -\mathbf{v}_{r/m} = +v_m \hat{i} + v_r \hat{j}$$
  The umbrella must be tilted **forward** into the wind by angle $\phi = \arctan(v_m / v_r)$ from the vertical.
- **IITian Rule**: Raindrops hit you from direction $-\mathbf{v}_{r/m}$. The umbrella head must face $-\mathbf{v}_{r/m}$ (tilted in the direction of your motion).

---

### ⚠️ Trap Alert 1.7: Radius of Curvature: Forgetting $a_\perp \neq g$ at Arbitrary Points
- **The Trap**: Calculating radius of curvature of a projectile as $R = \frac{v^2}{g}$ at an arbitrary point of trajectory.
- **Why Students Fall For It**: At the highest point (apex), velocity is horizontal and acceleration is purely vertical, so $a_\perp = g$. Students over-generalize this to every point along the trajectory.
- **Mathematical Reality**:
  At any point where velocity makes an angle $\theta$ with the horizontal, the velocity magnitude is $v = \frac{u\cos\theta_0}{\cos\theta}$.
  The acceleration of gravity $\mathbf{g}$ points vertically downward. The component perpendicular to velocity is:
  $$a_\perp = g\cos\theta$$
  Thus:
  $$R = \frac{v^2}{a_\perp} = \frac{v^2}{g\cos\theta} = \frac{u^2\cos^2\theta_0}{g\cos^3\theta}$$
  Only at the apex ($\theta = 0$) does $a_\perp = g$, giving $R_{apex} = \frac{u^2\cos^2\theta_0}{g}$. At the launch point ($\theta = \theta_0$), $R = \frac{u^2}{g\cos\theta_0} \neq \frac{u^2}{g}$.
- **IITian Rule**: In $R = v^2/a_\perp$, $a_\perp$ is strictly the acceleration component normal to the instantaneous tangent: $a_\perp = |\mathbf{a} \times \hat{v}|$.

---

### ⚠️ Trap Alert 1.8: Closest Approach of Two Projectiles: Assuming Simultaneous Apex
- **The Trap**: Assuming that the distance of closest approach between two projectiles occurs when one or both reach their maximum height.
- **Why Students Fall For It**: Misled by symmetrical trajectories in standalone single-projectile problems.
- **Mathematical Reality**:
  In a relative frame, both projectiles experience identical acceleration $\mathbf{g}$, so $\mathbf{a}_{rel} = \mathbf{0}$.
  The relative trajectory is a **straight line** at constant velocity $\mathbf{u}_{rel} = \mathbf{u}_1 - \mathbf{u}_2$.
  The closest approach occurs when the position vector from projectile 2 to projectile 1 is perpendicular to the relative velocity vector:
  $$\mathbf{r}_{rel}(t) \cdot \mathbf{u}_{rel} = 0 \implies t_{min} = -\frac{\mathbf{r}_{0, rel} \cdot \mathbf{u}_{rel}}{|\mathbf{u}_{rel}|^2}$$
  This time has no correlation whatsoever with the apex times $t_1 = \frac{u_{1y}}{g}$ or $t_2 = \frac{u_{2y}}{g}$.
- **IITian Rule**: Convert to the relative frame instantly: $\mathbf{a}_{rel} = \mathbf{0}$. Drop a perpendicular from the origin to the straight relative velocity ray.

---

### ⚠️ Trap Alert 1.9: Average Speed vs Magnitude of Average Velocity
- **The Trap**: Assuming $\langle v \rangle = |\langle \mathbf{v} \rangle|$, or computing average velocity by taking the arithmetic mean $\frac{v_1 + v_2}{2}$.
- **Why Students Fall For It**: The arithmetic mean formula $\frac{u+v}{2}$ is valid **only** for constant acceleration in 1D.
- **Mathematical Reality**:
  $$\text{Average Speed} = \frac{\text{Total Path Length}}{\Delta t} = \frac{\int |v(t)| dt}{\Delta t}$$
  $$\text{Magnitude of Average Velocity} = \frac{|\text{Net Displacement}|}{\Delta t} = \frac{|\int \mathbf{v}(t) dt|}{\Delta t}$$
  By the triangle inequality for integrals:
  $$\left|\int_{t_1}^{t_2} \mathbf{v}(t) dt\right| \leq \int_{t_1}^{t_2} |\mathbf{v}(t)| dt \implies |\langle \mathbf{v} \rangle| \leq \langle v \rangle$$
  Furthermore, if a particle covers two equal distances at speeds $v_1$ and $v_2$, the average speed is the harmonic mean $\frac{2 v_1 v_2}{v_1 + v_2}$, not the arithmetic mean $\frac{v_1 + v_2}{2}$.
- **IITian Rule**: Average velocity is strictly $\frac{\Delta \mathbf{r}}{\Delta t}$; average speed is strictly $\frac{\text{total distance}}{\Delta t}$. Never average speeds directly without weighting by time intervals.

---

### ⚠️ Trap Alert 1.10: Forgetting Coriolis Acceleration in Polar Coordinates
- **The Trap**: Writing the transverse acceleration in polar coordinates as simply $a_\theta = r\ddot{\theta} = r\alpha$.
- **Why Students Fall For It**: Students remember $a = r\alpha$ from rigid body circular motion where $r$ is constant ($\dot{r} = 0$).
- **Mathematical Reality**:
  When a particle is free to move radially (e.g. an insect crawling along the spoke of a rotating wheel, or a mass sliding along a rotating rod):
  $$\dot{r} \neq 0$$
  The complete transverse acceleration is:
  $$a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta}$$
  Omitting the term $2\dot{r}\dot{\theta}$ (the Coriolis acceleration) loses 100% of the transverse inertial effect in problems where angular velocity is constant ($\ddot{\theta} = 0$) but radial speed is non-zero ($\dot{r} \neq 0$).
- **IITian Rule**: In any rotating frame or polar coordinate system where the radial distance varies with time, the Coriolis term $2\dot{r}\dot{\theta}\hat{\theta}$ is mandatory.

## 1.4 Dissected JEE Advanced Previous Year Questions (PYQs)

### PYQ 1.1: JEE Advanced 2016 (Paper 1) — Parabolic Trajectory Kinematics & Acceleration Vector
**Problem Statement:**
A particle of mass $m$ moves in the $xy$-plane under the action of a force $\mathbf{F}$ such that its position coordinates as functions of time are given by:
$$x(t) = c t, \quad y(t) = \alpha x^2(t)$$
where $c > 0$ and $\alpha > 0$ are positive constants. At $t = 1\text{ s}$, determine:
1. The velocity vector $\mathbf{v}(t)$ and speed $v(t)$.
2. The acceleration vector $\mathbf{a}(t)$.
3. The tangential acceleration $a_t$ and normal acceleration $a_n$.
4. The local radius of curvature $R$ of the particle's trajectory at $t = 1\text{ s}$.

**Key Insight:**
The trajectory is explicitly given in parametric form through $x(t) = ct$, giving $y(t) = \alpha c^2 t^2$. By applying calculus to the parametric coordinates, velocity and acceleration vectors are directly computable. Crucially, tangential acceleration is the projection of $\mathbf{a}$ onto $\hat{v}$ ($a_t = \frac{\mathbf{v} \cdot \mathbf{a}}{v} = \frac{d|\mathbf{v}|}{dt}$), normal acceleration is $a_n = \sqrt{|\mathbf{a}|^2 - a_t^2}$, and the radius of curvature is $R = \frac{v^2}{a_n}$.

**Step-by-Step Mathematical Derivation:**
1. **Position, Velocity, and Acceleration Vectors:**
   Given $x(t) = ct$ and $y(t) = \alpha c^2 t^2$:
   $$v_x(t) = \dot{x}(t) = c$$
   $$v_y(t) = \dot{y}(t) = 2\alpha c^2 t$$
   Therefore, the velocity vector is:
   $$\mathbf{v}(t) = c\hat{i} + 2\alpha c^2 t\hat{j}$$
   The instantaneous speed is:
   $$v(t) = |\mathbf{v}(t)| = \sqrt{c^2 + 4\alpha^2 c^4 t^2} = c\sqrt{1 + 4\alpha^2 c^2 t^2}$$
   Differentiating velocity with respect to time:
   $$a_x(t) = \ddot{x}(t) = 0$$
   $$a_y(t) = \ddot{y}(t) = 2\alpha c^2$$
   Therefore, the acceleration vector is constant:
   $$\mathbf{a}(t) = 2\alpha c^2\hat{j}$$
   At $t = 1\text{ s}$:
   $$\mathbf{v}(1) = c\hat{i} + 2\alpha c^2\hat{j}, \quad v(1) = c\sqrt{1 + 4\alpha^2 c^2}$$
   $$\mathbf{a}(1) = 2\alpha c^2\hat{j}, \quad |\mathbf{a}(1)| = 2\alpha c^2$$

2. **Tangential Acceleration $a_t$:**
   Using the scalar product relation:
   $$a_t = \frac{\mathbf{v} \cdot \mathbf{a}}{v} = \frac{(c\hat{i} + 2\alpha c^2\hat{j}) \cdot (2\alpha c^2\hat{j})}{c\sqrt{1 + 4\alpha^2 c^2}} = \frac{4\alpha^2 c^4}{c\sqrt{1 + 4\alpha^2 c^2}} = \frac{4\alpha^2 c^3}{\sqrt{1 + 4\alpha^2 c^2}}$$
   *Verification via $\frac{dv}{dt}$*:
   $$\frac{dv}{dt} = \frac{d}{dt}\left[c\sqrt{1 + 4\alpha^2 c^2 t^2}\right] = c \frac{8\alpha^2 c^2 t}{2\sqrt{1 + 4\alpha^2 c^2 t^2}} = \frac{4\alpha^2 c^3 t}{\sqrt{1 + 4\alpha^2 c^2 t^2}}$$
   At $t = 1\text{ s}$, $\frac{dv}{dt} = \frac{4\alpha^2 c^3}{\sqrt{1 + 4\alpha^2 c^2}}$, which exactly matches!

3. **Normal Acceleration $a_n$:**
   Since $\mathbf{a} = a_t\hat{t} + a_n\hat{n}$ and $\hat{t} \perp \hat{n}$:
   $$a_n = \sqrt{|\mathbf{a}|^2 - a_t^2} = \sqrt{(2\alpha c^2)^2 - \frac{16\alpha^4 c^6}{1 + 4\alpha^2 c^2}} = \sqrt{4\alpha^2 c^4 \left(1 - \frac{4\alpha^2 c^2}{1 + 4\alpha^2 c^2}\right)} = \sqrt{\frac{4\alpha^2 c^4}{1 + 4\alpha^2 c^2}} = \frac{2\alpha c^2}{\sqrt{1 + 4\alpha^2 c^2}}$$
   *Direct Vector Cross-Product Verification*:
   $$a_n = \frac{|\mathbf{v} \times \mathbf{a}|}{v} = \frac{|(c\hat{i} + 2\alpha c^2\hat{j}) \times (2\alpha c^2\hat{j})|}{c\sqrt{1 + 4\alpha^2 c^2}} = \frac{|2\alpha c^3\hat{k}|}{c\sqrt{1 + 4\alpha^2 c^2}} = \frac{2\alpha c^2}{\sqrt{1 + 4\alpha^2 c^2}}$$
   The agreement is exact.

4. **Radius of Curvature $R$:**
   $$R = \frac{v^2}{a_n} = \frac{c^2(1 + 4\alpha^2 c^2)}{\frac{2\alpha c^2}{\sqrt{1 + 4\alpha^2 c^2}}} = \frac{(1 + 4\alpha^2 c^2)^{3/2}}{2\alpha}$$
   *Verification via Differential Geometry Formula*:
   The Cartesian equation is $y(x) = \alpha x^2$.
   $$\frac{dy}{dx} = 2\alpha x, \quad \frac{d^2y}{dx^2} = 2\alpha$$
   $$R = \frac{[1 + (dy/dx)^2]^{3/2}}{|d^2y/dx^2|} = \frac{[1 + 4\alpha^2 x^2]^{3/2}}{2\alpha}$$
   At $t = 1\text{ s}$, $x = c(1) = c$. Substituting $x = c$:
   $$R = \frac{(1 + 4\alpha^2 c^2)^{3/2}}{2\alpha}$$
   The two completely independent methods yield the exact identical algebraic expression.

**Common Student Pitfalls:**
- Conflating $|\mathbf{a}|$ with $a_t$ and stating $a_t = 2\alpha c^2$, thereby erroneously concluding $a_n = 0$.
- Forgetting that the velocity vector has an $x$-component when computing the cross product.

---

### PYQ 1.2: JEE Advanced 2010 — Projectile Motion on an Inclined Plane with Perpendicular Strike
**Problem Statement:**
A ball is projected from a point on an inclined plane of inclination $\beta = 30^\circ$ with an initial speed $u = 10\sqrt{3}\text{ m/s}$ at an angle $\alpha$ with the inclined plane. The ball strikes the inclined plane perpendicularly at point $P$.
Taking $g = 10\text{ m/s}^2$, find:
1. The angle of projection $\alpha$ with the inclined plane.
2. The time of flight $T$.
3. The distance along the incline from the launch point to point $P$ (the range $R$).
4. The velocity with which the ball strikes the incline.

**Key Insight:**
Striking the inclined plane perpendicularly means that the velocity component along the incline $v_{x'}$ is zero at $t = T$. In the rotated coordinate system ($x'$ along incline upwards, $y'$ perpendicular to incline upwards):
$$a_{x'} = -g\sin\beta, \quad a_{y'} = -g\cos\beta$$
The condition $v_{x'}(T) = 0$ provides the master constraint $2\tan\alpha\tan\beta = 1$.

**Step-by-Step Mathematical Derivation:**
1. **Finding Angle $\alpha$:**
   $$\tan\alpha = \frac{1}{2}\cot\beta$$
   Given $\beta = 30^\circ \implies \cot 30^\circ = \sqrt{3}$:
   $$\tan\alpha = \frac{\sqrt{3}}{2} \implies \alpha = \arctan\left(\frac{\sqrt{3}}{2}\right)$$
   From this:
   $$\sin\alpha = \frac{\sqrt{3}}{\sqrt{(\sqrt{3})^2 + 2^2}} = \sqrt{\frac{3}{7}}, \quad \cos\alpha = \frac{2}{\sqrt{7}}$$

2. **Time of Flight $T$:**
   $$T = \frac{2u\sin\alpha}{g\cos\beta}$$
   Substituting numerical values:
   $u = 10\sqrt{3}\text{ m/s}$, $g = 10\text{ m/s}^2$, $\beta = 30^\circ \implies \cos 30^\circ = \frac{\sqrt{3}}{2}$:
   $$T = \frac{2(10\sqrt{3})\sqrt{3/7}}{10(\sqrt{3}/2)} = \frac{20\sqrt{3}\sqrt{3/7}}{5\sqrt{3}} = 4\sqrt{\frac{3}{7}} = \frac{4\sqrt{21}}{7}\text{ s} \approx 2.62\text{ s}$$

3. **Range $R$ Along the Incline:**
   Since $v_{x'}(T) = 0$ and acceleration along the incline is constant $a_{x'} = -g\sin 30^\circ = -5\text{ m/s}^2$:
   By the third kinematic equation along $x'$:
   $$v_{x'}^2 = u_{x'}^2 + 2 a_{x'} R \implies 0 = (u\cos\alpha)^2 - 2(g\sin\beta)R$$
   $$R = \frac{u^2\cos^2\alpha}{2g\sin\beta}$$
   Substituting values:
   $$u^2 = (10\sqrt{3})^2 = 300$$
   $$\cos^2\alpha = \frac{4}{7}$$
   $$2g\sin\beta = 2(10)\sin 30^\circ = 10$$
   $$R = \frac{300 \times \frac{4}{7}}{10} = \frac{120}{7}\text{ m} \approx 17.14\text{ m}$$

4. **Impact Velocity:**
   Since the strike is perpendicular, the impact velocity has magnitude $|v_{y'}(T)|$:
   $$v_{y'}(T) = u_{y'} + a_{y'} T = u\sin\alpha - (g\cos\beta) T = u\sin\alpha - (g\cos\beta)\left(\frac{2u\sin\alpha}{g\cos\beta}\right) = -u\sin\alpha$$
   Thus, the impact speed is:
   $$v_{impact} = |v_{y'}(T)| = u\sin\alpha = 10\sqrt{3}\sqrt{\frac{3}{7}} = \frac{30}{\sqrt{7}}\text{ m/s} = \frac{30\sqrt{7}}{7}\text{ m/s} \approx 11.34\text{ m/s}$$
   Notice that the strike speed is directed purely into the incline surface.

**Common Student Pitfalls:**
- Setting $v_{y'} = 0$ instead of $v_{x'} = 0$.
- Using the standard range formula $\frac{u^2\sin 2\theta}{g}$ instead of the inclined plane formula.

---

### PYQ 1.3: JEE Advanced 2021 — Relative Free-Fall Kinematics of Two Projectiles
**Problem Statement:**
Two particles $A$ and $B$ are projected simultaneously in the vertical $xy$-plane. Particle $A$ is projected from the origin $(0, 0)$ with velocity $\mathbf{u}_A = (20\hat{i} + 20\hat{j})\text{ m/s}$. Particle $B$ is projected from the point $(40\text{ m}, 20\text{ m})$ with initial velocity $\mathbf{u}_B = (-10\hat{i} + 10\hat{j})\text{ m/s}$. Acceleration due to gravity is $\mathbf{g} = -10\hat{j}\text{ m/s}^2$.
1. Determine the relative velocity $\mathbf{v}_{A/B}(t)$ of $A$ with respect to $B$.
2. Determine whether the particles collide, and if not, compute the distance of closest approach $D_{min}$.
3. Find the time $t_{min}$ at which the distance of closest approach is achieved.

**Key Insight:**
Since both particles experience identical downward gravitational acceleration $\mathbf{g} = -10\hat{j}\text{ m/s}^2$, the relative acceleration is $\mathbf{a}_{A/B} = \mathbf{a}_A - \mathbf{a}_B = \mathbf{0}$. Therefore, the relative motion of $A$ as seen by $B$ is strictly **rectilinear uniform motion at constant velocity**.

**Step-by-Step Mathematical Derivation:**
1. **Relative Velocity:**
   $$\mathbf{v}_{A/B} = \mathbf{u}_A - \mathbf{u}_B = (20\hat{i} + 20\hat{j}) - (-10\hat{i} + 10\hat{j}) = 30\hat{i} + 10\hat{j}\text{ m/s}$$
   Notice that $\mathbf{v}_{A/B}$ is completely independent of time.
   Speed of $A$ relative to $B$:
   $$u_{rel} = |\mathbf{v}_{A/B}| = \sqrt{30^2 + 10^2} = \sqrt{1000} = 10\sqrt{10}\text{ m/s}$$

2. **Initial Relative Position Vector:**
   $$\mathbf{r}_0 = \mathbf{r}_A(0) - \mathbf{r}_B(0) = (0\hat{i} + 0\hat{j}) - (40\hat{i} + 20\hat{j}) = -40\hat{i} - 20\hat{j}\text{ m}$$
   The position of $A$ relative to $B$ as a function of time is:
   $$\mathbf{r}_{A/B}(t) = \mathbf{r}_0 + \mathbf{v}_{A/B} t = (-40 + 30t)\hat{i} + (-20 + 10t)\hat{j}$$

3. **Collision Condition Check:**
   For collision, $\mathbf{r}_{A/B}(t) = \mathbf{0}$ requires both coordinates to vanish simultaneously:
   $$-40 + 30t = 0 \implies t = \frac{4}{3}\text{ s}$$
   $$-20 + 10t = 0 \implies t = 2\text{ s}$$
   Since the times are unequal ($4/3 \neq 2$), the particles **do not collide**.
   *Cross Product Check*:
   $$\mathbf{r}_0 \times \mathbf{v}_{A/B} = (-40\hat{i} - 20\hat{j}) \times (30\hat{i} + 10\hat{j}) = [(-40)(10) - (-20)(30)]\hat{k} = [-400 + 600]\hat{k} = +200\hat{k} \neq \mathbf{0}$$
   Because the cross product is non-zero, the relative trajectory ray does not pass through the origin.

4. **Time of Closest Approach $t_{min}$:**
   $$t_{min} = -\frac{\mathbf{r}_0 \cdot \mathbf{v}_{A/B}}{|\mathbf{v}_{A/B}|^2}$$
   Evaluating the dot product:
   $$\mathbf{r}_0 \cdot \mathbf{v}_{A/B} = (-40)(30) + (-20)(10) = -1200 - 200 = -1400\text{ m}^2/\text{s}$$
   $$|\mathbf{v}_{A/B}|^2 = 1000\text{ m}^2/\text{s}^2$$
   $$t_{min} = -\frac{-1400}{1000} = 1.4\text{ s}$$
   Check airborne condition at $t = 1.4\text{ s}$:
   $$y_A(1.4) = 20(1.4) - \frac{1}{2}(10)(1.4)^2 = 28 - 9.8 = 18.2\text{ m} > 0$$
   $$y_B(1.4) = 20 + 10(1.4) - \frac{1}{2}(10)(1.4)^2 = 20 + 14 - 9.8 = 24.2\text{ m} > 0$$
   Both particles are well above the ground, so $t_{min} = 1.4\text{ s}$ is physically valid!

5. **Distance of Closest Approach $D_{min}$:**
   $$D_{min} = \frac{|\mathbf{r}_0 \times \mathbf{v}_{A/B}|}{|\mathbf{v}_{A/B}|} = \frac{200}{10\sqrt{10}} = \frac{20}{\sqrt{10}} = 2\sqrt{10}\text{ m} \approx 6.32\text{ m}$$

---

## 1.5 High-Rigor Practice Challenge Problems (Chapter 1)

### Challenge Problem 1.1: River Crossing in a Parabolic Flow Profile
**Problem Statement:**
A river of width $d$ flows parallel to the $x$-axis between straight banks at $y = 0$ and $y = d$. The flow velocity of the river varies quadratically across its width according to:
$$v_r(y) = 4 v_0 \frac{y(d - y)}{d^2}$$
where $v_0$ is the maximum current speed at the center of the river ($y = d/2$). A swimmer enters the water at $(0, 0)$ and maintains a constant swimming speed $u$ relative to the water, always steering perpendicular to the river banks (i.e. strictly along $+y$).
1. Derive the equation of the trajectory $y(x)$ of the swimmer.
2. Determine the total downstream drift $X$ of the swimmer upon reaching the opposite bank $y = d$.
3. Find the maximum speed of the swimmer relative to the ground during the crossing.

**Full Step-by-Step Solution:**
1. **Kinematic Equations:**
   The swimmer always heads along $+y$, so the velocity relative to the water is $\mathbf{v}_{s/r} = u\hat{j}$.
   The ground velocity components are:
   $$\frac{dy}{dt} = u = \text{constant}$$
   $$\frac{dx}{dt} = v_r(y) = \frac{4v_0}{d^2} y(d - y)$$
   Since $\frac{dy}{dt} = u$, we have $y(t) = ut$, and the total crossing time is $T = \frac{d}{u}$.

2. **Trajectory Equation $x(y)$:**
   Using the chain rule:
   $$\frac{dx}{dy} = \frac{dx/dt}{dy/dt} = \frac{4v_0}{u d^2}(d y - y^2)$$
   Integrating from $y = 0$ where $x = 0$:
   $$x(y) = \frac{4v_0}{u d^2} \int_0^y (d \eta - \eta^2) d\eta = \frac{4v_0}{u d^2} \left[\frac{d y^2}{2} - \frac{y^3}{3}\right]$$
   $$x(y) = \frac{2v_0}{3u d^2} y^2 (3d - 2y)$$

3. **Total Downstream Drift $X$:**
   Setting $y = d$:
   $$X = x(d) = \frac{2v_0}{3u d^2} d^2 (3d - 2d) = \frac{2v_0}{3u} (d) = \frac{2 v_0 d}{3 u}$$

4. **Maximum Ground Speed:**
   The ground speed is $v(y) = \sqrt{v_x^2 + v_y^2} = \sqrt{v_r(y)^2 + u^2}$.
   This is maximized where $v_r(y)$ is maximum, which occurs at the midpoint $y = d/2$ where $v_r = v_0$:
   $$v_{max} = \sqrt{v_0^2 + u^2}$$

**Answer Key:**
1. $x(y) = \frac{2v_0}{3u d^2} y^2 (3d - 2y)$
2. $X = \frac{2 v_0 d}{3 u}$
3. $v_{max} = \sqrt{v_0^2 + u^2}$

---

### Challenge Problem 1.2: Successive Bounces of an Elastic Projectile Down an Incline
**Problem Statement:**
An incline makes an angle $\beta$ with the horizontal. A small elastic ball is dropped vertically from rest from a height $h$ directly above the incline onto a point $O$ on the incline. The collision is perfectly elastic ($e = 1$). After the first bounce at $O$, the ball executes projectile motion and strikes the incline at point $P_1$, bouncing again to strike at $P_2$, and so on.
1. Prove that the ratio of the distances between successive bounce points satisfies:
   $$L_1 : L_2 : L_3 : \dots : L_n = 1 : 2 : 3 : \dots : n$$
   where $L_k$ is the distance along the incline between the $(k-1)$-th and $k$-th bounce points.
2. Determine the exact value of $L_1$ in terms of $h$ and $\beta$.

**Full Step-by-Step Solution:**
1. **First Collision Velocity at Origin $O$:**
   The ball falls freely through height $h$:
   $$v_0 = \sqrt{2gh}$$
   directed vertically downwards.
   Rotate coordinates: $x'$ along the incline downwards, $y'$ perpendicular to the incline upwards.
   The angle between the vertical and the normal to the incline ($\hat{j}'$) is $\beta$.
   Therefore, the velocity components just before impact are:
   $$v_{0x'} = v_0 \sin\beta, \quad v_{0y'} = -v_0 \cos\beta$$
   Since the collision is perfectly elastic ($e = 1$) and the incline is smooth:
   - Tangential component is unchanged: $u_{1x'} = v_{0x'} = v_0\sin\beta$
   - Normal component is reversed: $u_{1y'} = -(-v_0\cos\beta) = +v_0\cos\beta$

2. **First Projectile Flight ($O$ to $P_1$):**
   Accelerations: $a_{x'} = g\sin\beta$, $a_{y'} = -g\cos\beta$.
   Time between 0 and 1st bounce:
   $$y'(T_1) = 0 \implies u_{1y'} T_1 - \frac{1}{2}g\cos\beta T_1^2 = 0 \implies T_1 = \frac{2 u_{1y'}}{g\cos\beta} = \frac{2 v_0\cos\beta}{g\cos\beta} = \frac{2v_0}{g}$$
   Velocity components just before the second impact at $P_1$:
   $$v_{1y'}^- = u_{1y'} - g\cos\beta T_1 = v_0\cos\beta - g\cos\beta \left(\frac{2v_0}{g}\right) = -v_0\cos\beta$$
   $$v_{1x'}^- = u_{1x'} + g\sin\beta T_1 = v_0\sin\beta + g\sin\beta \left(\frac{2v_0}{g}\right) = 3 v_0\sin\beta$$
   The distance of the first bounce:
   $$L_1 = u_{1x'} T_1 + \frac{1}{2}g\sin\beta T_1^2 = (v_0\sin\beta)\left(\frac{2v_0}{g}\right) + \frac{1}{2}g\sin\beta \left(\frac{2v_0}{g}\right)^2 = \frac{2v_0^2}{g}\sin\beta + \frac{2v_0^2}{g}\sin\beta = \frac{4v_0^2}{g}\sin\beta$$
   Since $v_0^2 = 2gh$:
   $$L_1 = \frac{4(2gh)}{g}\sin\beta = 8h\sin\beta$$

3. **Generalization by Mathematical Induction for $k$-th Bounce:**
   Notice that for every elastic bounce, $v_{ky'}^- = -v_0\cos\beta$ is reversed to $u_{(k+1)y'} = +v_0\cos\beta$.
   Thus, the normal initial velocity is **constant for all bounces**:
   $$u_{ky'} = v_0\cos\beta \implies T_k = \frac{2v_0}{g} = T_1 \quad \forall k$$
   Every flight takes the exact same time $T = \frac{2v_0}{g}$!
   In each flight of duration $T$, the tangential velocity increases by:
   $$\Delta v_{x'} = g\sin\beta T = g\sin\beta \left(\frac{2v_0}{g}\right) = 2v_0\sin\beta$$
   Therefore:
   $$u_{kx'} = v_0\sin\beta + (k-1)(2v_0\sin\beta) = (2k - 1)v_0\sin\beta$$
   The range during the $k$-th bounce is:
   $$L_k = u_{kx'} T + \frac{1}{2}g\sin\beta T^2 = (2k - 1)v_0\sin\beta \left(\frac{2v_0}{g}\right) + \frac{1}{2}g\sin\beta \left(\frac{2v_0}{g}\right)^2$$
   $$L_k = (2k - 1)\frac{2v_0^2}{g}\sin\beta + \frac{2v_0^2}{g}\sin\beta = 2k \frac{2v_0^2}{g}\sin\beta = k \left(\frac{4v_0^2}{g}\sin\beta\right) = k L_1$$
   Thus:
   $$L_1 : L_2 : L_3 : \dots : L_n = 1 : 2 : 3 : \dots : n$$
   This completes the formal proof.

**Answer Key:**
1. Proved: $L_k = k L_1 \implies L_1 : L_2 : \dots : L_n = 1 : 2 : \dots : n$.
2. $L_1 = 8h\sin\beta$.

---

### Challenge Problem 1.3: The Classical Pure Pursuit Trajectory
**Problem Statement:**
A fox at origin $(0, 0)$ chases a hare that starts at $(d, 0)$ and runs along the straight vertical line $x = d$ with constant speed $u$ in the $+y$ direction. The fox runs with constant speed $v > u$, and its instantaneous velocity vector is always pointed directly towards the current position of the hare.
1. Formulate the differential equation of the pursuit curve $y(x)$.
2. Integrate the differential equation to find the explicit trajectory $y(x)$.
3. Determine the exact time $T_{catch}$ and the $y$-coordinate at which the fox catches the hare.

**Full Step-by-Step Solution:**
1. **Setting Up the Kinematics:**
   At time $t$, let the hare be at coordinates $(d, ut)$.
   Let the fox be at coordinates $(x, y)$.
   The line of sight from the fox to the hare has slope:
   $$\frac{dy}{dx} = \frac{ut - y}{d - x}$$
   Rearranging:
   $$(d - x)\frac{dy}{dx} = ut - y$$
   Differentiating both sides with respect to $x$:
   $$- \frac{dy}{dx} + (d - x)\frac{d^2y}{dx^2} = u \frac{dt}{dx} - \frac{dy}{dx} \implies (d - x)\frac{d^2y}{dx^2} = u \frac{dt}{dx}$$
   Since the fox runs with constant speed $v$:
   $$v = \frac{ds}{dt} = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} = \frac{dx}{dt}\sqrt{1 + \left(\frac{dy}{dx}\right)^2}$$
   Therefore:
   $$\frac{dt}{dx} = \frac{\sqrt{1 + (y')^2}}{v}$$
   Substituting this into our differential equation:
   $$(d - x)\frac{d^2y}{dx^2} = \frac{u}{v}\sqrt{1 + \left(\frac{dy}{dx}\right)^2}$$
   Let $p = \frac{dy}{dx} = y'$ and define the dimensionless ratio $k = \frac{u}{v} < 1$:
   $$(d - x)\frac{dp}{dx} = k\sqrt{1 + p^2}$$

2. **Integration:**
   Separating variables:
   $$\frac{dp}{\sqrt{1 + p^2}} = \frac{k dx}{d - x}$$
   Integrating both sides:
   $$\ln\left(p + \sqrt{1 + p^2}\right) = -k\ln(d - x) + C_1 = \ln\left[C (d - x)^{-k}\right]$$
   At $t = 0$, the fox is at $(0, 0)$ heading towards $(d, 0)$, so the initial slope is horizontal: $p(0) = 0$ at $x = 0$.
   $$\ln(0 + 1) = \ln(C d^{-k}) \implies C d^{-k} = 1 \implies C = d^k$$
   Thus:
   $$p + \sqrt{1 + p^2} = \left(\frac{d}{d - x}\right)^k$$
   Let $w = \left(\frac{d - x}{d}\right)^k$, so $p + \sqrt{1 + p^2} = \frac{1}{w}$.
   Since $( \sqrt{1+p^2} + p )(\sqrt{1+p^2} - p) = 1$:
   $$\sqrt{1+p^2} - p = w$$
   Subtracting the two equations:
   $$2p = \frac{1}{w} - w \implies p = \frac{dy}{dx} = \frac{1}{2}\left[\left(\frac{d - x}{d}\right)^{-k} - \left(\frac{d - x}{d}\right)^k\right]$$
   Integrating $y(x)$ with boundary condition $y(0) = 0$:
   $$y(x) = \frac{1}{2} \int_0^x \left[\left(1 - \frac{\xi}{d}\right)^{-k} - \left(1 - \frac{\xi}{d}\right)^k\right] d\xi$$
   Let $z = 1 - \frac{\xi}{d}$, $d\xi = -d dz$:
   $$y(x) = \frac{d}{2} \left[\frac{\left(1 - \frac{x}{d}\right)^{1 - k} - 1}{k - 1} - \frac{\left(1 - \frac{x}{d}\right)^{1 + k} - 1}{-(1 + k)}\right]$$
   $$y(x) = \frac{d}{2}\left[\frac{1 - \left(1 - \frac{x}{d}\right)^{1 - k}}{1 - k} - \frac{1 - \left(1 - \frac{x}{d}\right)^{1 + k}}{1 + k}\right]$$

3. **Capture Time and Position:**
   Capture occurs when the fox reaches $x = d$:
   Setting $x = d$ in $y(x)$:
   $$y_{catch} = \frac{d}{2}\left[\frac{1}{1 - k} - \frac{1}{1 + k}\right] = \frac{d}{2}\left[\frac{(1+k) - (1-k)}{1 - k^2}\right] = \frac{d k}{1 - k^2}$$
   Substituting $k = \frac{u}{v}$:
   $$y_{catch} = \frac{d(u/v)}{1 - u^2/v^2} = \frac{u v d}{v^2 - u^2}$$
   Since the hare moves at constant speed $u$, the capture time is:
   $$T_{catch} = \frac{y_{catch}}{u} = \frac{v d}{v^2 - u^2}$$

**Answer Key:**
1. $(d - x)\frac{d^2y}{dx^2} = \frac{u}{v}\sqrt{1 + (y')^2}$
2. $y(x) = \frac{d}{2}\left[\frac{1 - (1 - x/d)^{1 - u/v}}{1 - u/v} - \frac{1 - (1 - x/d)^{1 + u/v}}{1 + u/v}\right]$
3. $T_{catch} = \frac{v d}{v^2 - u^2}, \quad y_{catch} = \frac{u v d}{v^2 - u^2}$

---

### Challenge Problem 1.4: Vertical Projectile with Quadratic Drag
**Problem Statement:**
A body of mass $m$ is projected vertically upwards with an initial velocity $v_0$ in an atmosphere where the air resistance is proportional to the square of its speed: $F_{drag} = m \beta v^2$.
1. Derive the maximum height $H$ reached by the body.
2. Derive the time of ascent $t_{up}$ taken to reach maximum height.
3. Derive the velocity $v_1$ with which the body returns to the launch point and show that $v_1 < v_0$.
4. Derive the time of descent $t_{down}$ and prove rigorously that $t_{down} > t_{up}$.

**Full Step-by-Step Solution:**
1. **Upward Motion:**
   During upward motion, both gravity and drag act downwards:
   $$a = \frac{dv}{dt} = -(g + \beta v^2)$$
   Using $v\frac{dv}{dy} = -(g + \beta v^2)$:
   $$\int_0^H dy = -\int_{v_0}^0 \frac{v dv}{g + \beta v^2} = \int_0^{v_0} \frac{v dv}{g + \beta v^2} = \frac{1}{2\beta} \left[\ln(g + \beta v^2)\right]_0^{v_0}$$
   $$H = \frac{1}{2\beta} \ln\left(1 + \frac{\beta v_0^2}{g}\right)$$
   Let $v_T = \sqrt{g/\beta}$ be the terminal speed. Then $\beta = g/v_T^2$:
   $$H = \frac{v_T^2}{2g}\ln\left(1 + \frac{v_0^2}{v_T^2}\right)$$

2. **Time of Ascent $t_{up}$:**
   $$\frac{dv}{dt} = -(g + \beta v^2) \implies dt = -\frac{dv}{g + \beta v^2}$$
   $$t_{up} = \int_0^{v_0} \frac{dv}{g + \beta v^2} = \frac{1}{\sqrt{g\beta}} \left[\arctan\left(\sqrt{\frac{\beta}{g}} v\right)\right]_0^{v_0} = \frac{v_T}{g}\arctan\left(\frac{v_0}{v_T}\right)$$

3. **Downward Motion and Return Velocity $v_1$:**
   During descent, gravity acts downwards while drag acts upwards:
   $$a = g - \beta v^2 \implies v \frac{dv}{dy} = g - \beta v^2$$
   Integrating from $y = H$ (where $v = 0$) to $y = 0$ (where $v = v_1$):
   $$\int_0^{v_1} \frac{v dv}{g - \beta v^2} = \int_0^H dy = H$$
   $$-\frac{1}{2\beta} \ln\left(\frac{g - \beta v_1^2}{g}\right) = H \implies \ln\left(1 - \frac{v_1^2}{v_T^2}\right) = -2\beta H$$
   $$1 - \frac{v_1^2}{v_T^2} = e^{-2\beta H}$$
   From the ascent formula, $2\beta H = \ln\left(1 + \frac{v_0^2}{v_T^2}\right) \implies e^{-2\beta H} = \frac{1}{1 + \frac{v_0^2}{v_T^2}}$.
   Therefore:
   $$1 - \frac{v_1^2}{v_T^2} = \frac{1}{1 + \frac{v_0^2}{v_T^2}} \implies \frac{v_1^2}{v_T^2} = 1 - \frac{1}{1 + \frac{v_0^2}{v_T^2}} = \frac{v_0^2/v_T^2}{1 + v_0^2/v_T^2}$$
   $$v_1 = \frac{v_0}{\sqrt{1 + \frac{v_0^2}{v_T^2}}} < v_0$$
   This proves that mechanical energy is dissipated by air resistance, so $v_1 < v_0$.

4. **Time of Descent $t_{down}$ and Comparison:**
   $$\frac{dv}{dt} = g - \beta v^2 \implies t_{down} = \int_0^{v_1} \frac{dv}{g - \beta v^2} = \frac{1}{2\sqrt{g\beta}} \ln\left(\frac{1 + v_1/v_T}{1 - v_1/v_T}\right) = \frac{v_T}{g}\text{arctanh}\left(\frac{v_1}{v_T}\right)$$
   Substitute $\frac{v_1}{v_T} = \frac{v_0/v_T}{\sqrt{1 + v_0^2/v_T^2}} = \sin\phi$, where $\tan\phi = \frac{v_0}{v_T}$.
   Then:
   $$t_{up} = \frac{v_T}{g} \phi$$
   $$t_{down} = \frac{v_T}{g} \text{arctanh}(\sin\phi) = \frac{v_T}{g} \ln\left(\frac{1 + \sin\phi}{\cos\phi}\right) = \frac{v_T}{g} \ln(\sec\phi + \tan\phi)$$
   Since $\ln(\sec\phi + \tan\phi) > \phi$ for all $\phi \in (0, \pi/2)$ (readily verified by differentiation: $\frac{d}{d\phi}[\ln(\sec\phi+\tan\phi) - \phi] = \sec\phi - 1 > 0$):
   $$t_{down} > t_{up}$$
   The time of descent is strictly greater than the time of ascent.

**Answer Key:**
1. $H = \frac{1}{2\beta} \ln\left(1 + \frac{\beta v_0^2}{g}\right)$
2. $t_{up} = \frac{1}{\sqrt{g\beta}}\arctan\left(\sqrt{\frac{\beta}{g}} v_0\right)$
3. $v_1 = \frac{v_0}{\sqrt{1 + \beta v_0^2 / g}} < v_0$
4. Proved: $t_{down} > t_{up}$.

---

### Challenge Problem 1.5: Radius of Curvature of a Cycloid Trajectory
**Problem Statement:**
A particle moves along a cycloid in the vertical $xy$-plane given parametrically by:
$$x(\theta) = R(\theta - \sin\theta), \quad y(\theta) = R(1 - \cos\theta)$$
where $R$ is a constant and the parameter $\theta$ evolves such that $\dot{\theta} = \omega = \text{constant}$.
1. Derive the velocity components $\dot{x}, \dot{y}$ and the acceleration components $\ddot{x}, \ddot{y}$.
2. Compute the instantaneous speed $v(\theta)$ and tangential acceleration $a_t(\theta)$.
3. Prove that the radius of curvature of the cycloid at any point is:
   $$R_c(\theta) = 4 R \sin\left(\frac{\theta}{2}\right) = 2\sqrt{2 R y}$$

**Full Step-by-Step Solution:**
1. **Derivatives:**
   $$\dot{x} = R\dot{\theta}(1 - \cos\theta) = R\omega(1 - \cos\theta) = 2R\omega\sin^2\left(\frac{\theta}{2}\right)$$
   $$\dot{y} = R\dot{\theta}\sin\theta = R\omega\sin\theta = 2R\omega\sin\left(\frac{\theta}{2}\right)\cos\left(\frac{\theta}{2}\right)$$
   Second derivatives:
   $$\ddot{x} = R\omega^2 \sin\theta$$
   $$\ddot{y} = R\omega^2 \cos\theta$$

2. **Speed and Tangential Acceleration:**
   $$v^2 = \dot{x}^2 + \dot{y}^2 = R^2\omega^2\left[(1 - \cos\theta)^2 + \sin^2\theta\right] = R^2\omega^2[1 - 2\cos\theta + \cos^2\theta + \sin^2\theta]$$
   $$v^2 = 2R^2\omega^2(1 - \cos\theta) = 4R^2\omega^2\sin^2\left(\frac{\theta}{2}\right)$$
   $$v = 2R\omega \sin\left(\frac{\theta}{2}\right) \quad \left(\text{for } \theta \in [0, 2\pi]\right)$$
   Tangential acceleration:
   $$a_t = \frac{dv}{dt} = \frac{dv}{d\theta}\dot{\theta} = \left[R\omega \cos\left(\frac{\theta}{2}\right)\right]\omega = R\omega^2\cos\left(\frac{\theta}{2}\right)$$

3. **Radius of Curvature Calculation:**
   Using the cross product $\mathbf{v} \times \mathbf{a}$:
   $$\dot{x}\ddot{y} - \dot{y}\ddot{x} = [R\omega(1 - \cos\theta)][R\omega^2\cos\theta] - [R\omega\sin\theta][R\omega^2\sin\theta]$$
   $$= R^2\omega^3 [\cos\theta - \cos^2\theta - \sin^2\theta] = R^2\omega^3 [\cos\theta - 1] = -R^2\omega^3(1 - \cos\theta) = -2R^2\omega^3\sin^2\left(\frac{\theta}{2}\right)$$
   Magnitude:
   $$|\dot{x}\ddot{y} - \dot{y}\ddot{x}| = 2R^2\omega^3\sin^2\left(\frac{\theta}{2}\right)$$
   Now calculate $R_c$:
   $$R_c = \frac{v^3}{|\dot{x}\ddot{y} - \dot{y}\ddot{x}|} = \frac{\left[2R\omega\sin(\theta/2)\right]^3}{2R^2\omega^3\sin^2(\theta/2)} = \frac{8R^3\omega^3\sin^3(\theta/2)}{2R^2\omega^3\sin^2(\theta/2)} = 4R\sin\left(\frac{\theta}{2}\right)$$
   Since $y = R(1 - \cos\theta) = 2R\sin^2(\theta/2) \implies \sin(\theta/2) = \sqrt{\frac{y}{2R}}$:
   $$R_c = 4R \sqrt{\frac{y}{2R}} = 4R \frac{\sqrt{y}}{\sqrt{2R}} = 2\sqrt{2Ry}$$
   This completes the proof.

**Answer Key:**
1. $\mathbf{v} = R\omega(1 - \cos\theta)\hat{i} + R\omega\sin\theta\hat{j}, \quad \mathbf{a} = R\omega^2\sin\theta\hat{i} + R\omega^2\cos\theta\hat{j}$
2. $v = 2R\omega\sin(\theta/2), \quad a_t = R\omega^2\cos(\theta/2)$
3. Proved: $R_c = 4R\sin(\theta/2) = 2\sqrt{2Ry}$.

---

## 1.6 Publication-Grade Diagram Specifications (Chapter 1)

### Diagram 1.1: Plane Polar Coordinate Basis and Velocity/Acceleration Resolution
- **Format**: SVG (Inline / Standalone)
- **ViewBox**: `0 0 650 450`
- **Aesthetic Theme**: Soft warm paper yellow (`#fcfaf2` background, `#1e293b` ink lines, subtle `#e2e8f0` grid).
- **Visual Components**:
  1. **Axes**: Horizontal Cartesian $x$-axis and vertical $y$-axis with slate arrows and labels.
  2. **Particle Position**: Point $P(r, \theta)$ indicated by a filled circle `#2563eb` with position vector $\mathbf{r}$ drawn from $O(0,0)$ to $P$ with label $\mathbf{r} = r\hat{r}$.
  3. **Polar Unit Vectors**: Orthonormal basis vectors rooted at $P$:
     - $\hat{r}$ pointing radially outward (color: `#2563eb`, thickness: 2.5px).
     - $\hat{\theta}$ pointing perpendicular to $\hat{r}$ in increasing $\theta$ direction (color: `#059669`, thickness: 2.5px).
  4. **Velocity Vector Decomposition**:
     - Resultant velocity $\mathbf{v}$ (color: `#d97706`, thickness: 2.5px).
     - Radial projection $v_r = \dot{r}$ along $\hat{r}$ (dashed `#2563eb`).
     - Transverse projection $v_\theta = r\dot{\theta}$ along $\hat{\theta}$ (dashed `#059669`).
  5. **Acceleration Vector Decomposition**:
     - Resultant acceleration vector $\mathbf{a}$ (color: `#dc2626`, thickness: 2.5px).
     - Component box showing $a_r = \ddot{r} - r\dot{\theta}^2$ and $a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta}$.
  6. **Coriolis Callout Box**: Stylized note card pointing to $2\dot{r}\dot{\theta}$ highlighting "Coriolis Acceleration: $\dot{r}\dot{\theta}$ from $\hat{r}$ rotation $+ \dot{r}\dot{\theta}$ from expanding lever arm".

### Diagram 1.2: Tangential-Normal Intrinsic Coordinates & Osculating Circle
- **Format**: SVG
- **ViewBox**: `0 0 700 450`
- **Visual Components**:
  1. **Arbitrary Trajectory Curve $\mathcal{C}$**: Smooth cubic Bézier curve sweeping across the diagram (color: `#1e293b`, stroke-width: 3px).
  2. **Instantaneous Point $P$**: Located along the curve.
  3. **Tangent and Normal Vectors**:
     - Unit tangent $\hat{t}$ directed forward along the curve (color: `#2563eb`, stroke-width: 2.5px).
     - Unit principal normal $\hat{n}$ directed towards the center of curvature $C$ (color: `#dc2626`, stroke-width: 2.5px).
  4. **Osculating Circle**: Circle tangent to curve at $P$ with radius $R$ centered at $C$ (dashed `#94a3b8`, fill: `rgba(37, 99, 235, 0.04)`).
  5. **Acceleration Triangle**:
     - Total acceleration $\mathbf{a}$ pointing into the concave side of the curve.
     - $a_t = \frac{dv}{dt}\hat{t}$ along tangent.
     - $a_n = \frac{v^2}{R}\hat{n}$ along normal.
     - Angle $\phi = \arctan(a_n / a_t)$.

### Diagram 1.3: River-Swimmer Geometry: Shortest Path vs Minimum Drift
- **Format**: SVG
- **ViewBox**: `0 0 750 400`
- **Visual Components**:
  1. **River Geometry**: Two parallel horizontal banks at $y = 0$ and $y = d$ with light blue water tint `#e0f2fe`. Current velocity arrows $\mathbf{v}_r$ pointing rightward.
  2. **Panel A ($u \geq v_r$)**: Shortest path vector triangle showing $\mathbf{v}_{s/r}$ angled upstream at $\sin\theta = v_r/u$ resulting in net ground velocity $\mathbf{v}_s$ strictly perpendicular to banks.
  3. **Panel B ($u < v_r$)**: Velocity circle of radius $u$ centered at $(v_r, 0)$. Tangent line drawn from origin $O$ to the circle. The tangent point forms a right triangle showing $\sin\theta = u/v_r$, and the line represents the maximum angle w.r.t the bank, proving minimum drift $x_{min} = d\frac{\sqrt{v_r^2 - u^2}}{u}$.

### Diagram 1.4: Projectile Motion on an Inclined Plane
- **Format**: SVG
- **ViewBox**: `0 0 700 450`
- **Visual Components**:
  1. **Incline Wedge**: Base line horizontal, incline face inclined at angle $\beta$.
  2. **Rotated Axes**: $x'$-axis along the incline face (dashed `#64748b`), $y'$-axis perpendicular to incline (dashed `#64748b`).
  3. **Trajectory Curve**: Parabolic arc launched from origin $O$ with initial velocity $\mathbf{u}$ at angle $\alpha$ to incline.
  4. **Gravity Decomposition**: Vector $\mathbf{g}$ pointing straight down, resolved into $-g\sin\beta\hat{i}'$ (downhill) and $-g\cos\beta\hat{j}'$ (into incline).
  5. **Impact Point $P$**: Depicting perpendicular landing where tangent to trajectory is exactly parallel to $y'$ ($v_{x'} = 0$, $v_{y'} = -u\sin\alpha$).
