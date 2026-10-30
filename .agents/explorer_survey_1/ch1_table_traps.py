import sys

content = r"""
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
"""

with open("/Users/shera/Desktop/business_framework/.agents/explorer_survey_1/survey_ch1_ch2.md", "a", encoding="utf-8") as f:
    f.write(content)

print("Chapter 1 Table and Traps appended successfully.")
