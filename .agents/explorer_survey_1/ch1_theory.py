import sys

content = r"""# PART 1: CHAPTER 1 — VECTORS, CALCULUS & ADVANCED 2D KINEMATICS

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
"""

with open("/Users/shera/Desktop/business_framework/.agents/explorer_survey_1/survey_ch1_ch2.md", "a", encoding="utf-8") as f:
    f.write(content)

print("Chapter 1 Theory appended successfully.")
