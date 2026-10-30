import sys

content = r"""
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
"""

with open("/Users/shera/Desktop/business_framework/.agents/explorer_survey_1/survey_ch1_ch2.md", "a", encoding="utf-8") as f:
    f.write(content)

print("Chapter 1 PYQs, Challenges, and Diagrams appended successfully.")
