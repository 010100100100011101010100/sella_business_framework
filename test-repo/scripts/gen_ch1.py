# Chapter 1 Generator: Vectors, Calculus & Advanced 2D Kinematics
# Conversational Kota Mentor Voice • Zero Emojis • Modern Typography

def get_ch1_content():
    return r"""
    <section id="ch1" class="chapter-container">
      <span class="chapter-number">Chapter 01</span>
      <h1 class="chapter-title">Vectors, Calculus & Advanced 2D Kinematics</h1>

      <div class="card-box tip-card">
        <div class="card-header-tip">[MENTOR STRATEGY NOTE] Welcome to Mechanics</div>
        <p><strong>Listen up:</strong> Mechanics isn't a collection of 50 disconnected equations to memorize the night before the exam. It's a game of reference frames, constraint geometry, and calculus. In JEE Advanced, Kinematics rarely appears as a standalone trivial question—it shows up as the first layer inside rotational dynamics, electromagnetic Lorentz trajectories, and variable mass systems.</p>
        <p><strong>The Golden Rule:</strong> The moment you see variable acceleration $a(t), a(v),$ or $a(x)$, throw your high-school kinematic equations ($v = u + at, s = ut + \frac{1}{2}at^2$) straight out the window. If you use them when acceleration changes, you are handing the examiner an easy -1.</p>
      </div>

      <h2 class="section-title">1.1 First-Principles Foundations: The Calculus of Motion</h2>
      
      <p>Let's strip kinematics down to first principles. Where an object is located relative to an origin $O$ is described by its position vector:</p>
      $$\mathbf{r}(t) = x(t)\hat{\mathbf{i}} + y(t)\hat{\mathbf{j}} + z(t)\hat{\mathbf{k}}$$
      <p>Velocity is simply how fast that position vector changes over time. Notice that velocity always points along the exact direction the object is traveling:</p>
      $$\mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = \dot{x}\hat{\mathbf{i}} + \dot{y}\hat{\mathbf{j}} + \dot{z}\hat{\mathbf{k}} = v \hat{\mathbf{t}}$$
      <p>where $v = |\mathbf{v}|$ is your speed, and $\hat{\mathbf{t}}$ is the unit vector pointing forward along the path.</p>

      <p>Now, what happens when velocity changes? Acceleration has <strong>two completely separate duties</strong>:</p>
      $$\mathbf{a} = \frac{d\mathbf{v}}{dt} = a_t \hat{\mathbf{t}} + a_n \hat{\mathbf{n}}$$
      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Tangential Acceleration ($a_t = \frac{dv}{dt}$):</strong> This is your <em>speedometer</em>. It only changes how fast you are moving. If speed is constant, $a_t = 0$.</li>
        <li><strong>Normal / Centripetal Acceleration ($a_n = \frac{v^2}{\rho}$):</strong> This is your <em>steering wheel</em>. It only changes your direction by bending the trajectory into a curve of radius $\rho$.</li>
      </ul>
      <p>Total acceleration magnitude is the Pythagorean sum: $a = \sqrt{a_t^2 + a_n^2}$. If a car drives in a circle at constant speed, $a_t = 0$ but $a = a_n = v^2/R \ne 0$.</p>

      <h3 class="sub-title">1.1.1 The Radius of Curvature Master Method</h3>
      <p>Think of the radius of curvature $\rho$ as the radius of the circle that best fits the curve at that exact point. To find it, use the simple relation between normal acceleration and speed:</p>
      $$a_\perp = \frac{v^2}{\rho} \implies \rho = \frac{v^2}{a_\perp}$$
      <p>Whenever you need $\rho$ on any trajectory:</p>
      <ol style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li>Find the speed $v = |\mathbf{v}|$.</li>
        <li>Find the net acceleration $\mathbf{a}$.</li>
        <li>Take the component of acceleration perpendicular to motion: $a_\perp = \sqrt{a^2 - a_\parallel^2}$.</li>
        <li>Compute $\rho = v^2 / a_\perp$.</li>
      </ol>
      <p>If the trajectory is given as a formula $y = f(x)$, calculus gives:</p>
      $$\rho = \frac{\left[1 + \left(\frac{dy}{dx}\right)^2\right]^{3/2}}{\left|\frac{d^2y}{dx^2}\right|}$$

      <!-- SVG Diagram 1.1 -->
      <div class="diagram-container">
                <svg class="diagram-svg" width="600" height="260" viewBox="0 0 600 260">
          <defs>
            <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#059669"/>
            </marker>
          </defs>
          <line x1="40" y1="220" x2="560" y2="220" stroke="#0f172a" stroke-width="2" />
          <line x1="60" y1="220" x2="480" y2="70" stroke="#2563eb" stroke-width="2.5" />
          <path d="M 120 220 A 60 60 0 0 0 115 200" fill="none" stroke="#2563eb" stroke-width="1.5" />
          <text x="130" y="212" font-family="sans-serif" font-size="12" fill="#2563eb" font-weight="bold">Incline Angle: β</text>
          <path d="M 60 220 Q 230 40 400 100" fill="none" stroke="#dc2626" stroke-width="3" />
          <line x1="60" y1="220" x2="150" y2="130" stroke="#059669" stroke-width="3" marker-end="url(#arrow)" />
          <text x="140" y="125" font-family="sans-serif" font-size="13" font-weight="bold" fill="#059669">Launch Velocity u</text>
          <path d="M 110 200 A 30 30 0 0 0 95 185" fill="none" stroke="#059669" stroke-width="1.5" />
          <text x="115" y="180" font-family="sans-serif" font-size="11" fill="#059669">Angle: α</text>
          <circle cx="400" cy="100" r="5" fill="#dc2626" />
          <text x="415" y="105" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">Impact Point</text>
          <line x1="250" y1="120" x2="250" y2="175" stroke="#0f172a" stroke-width="2.5" />
          <text x="258" y="165" font-family="sans-serif" font-size="12" fill="#0f172a">Gravity g</text>
          <line x1="250" y1="120" x2="280" y2="140" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
          <text x="285" y="145" font-family="sans-serif" font-size="11" fill="#64748b">g·sin(β)</text>
          <line x1="250" y1="120" x2="220" y2="160" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
          <text x="175" y="170" font-family="sans-serif" font-size="11" fill="#64748b">g·cos(β)</text>
        </svg>
        <div class="diagram-caption">Figure 1.1: Projectile on an inclined plane. Resolving gravity along the incline (g·sin β) and perpendicular to the incline (g·cos β).</div>
      </div>

      <h3 class="sub-title">1.1.2 Projectile Motion on Inclined Planes</h3>
      <p>Let's demolish this classic exam topic. An inclined plane is tilted at angle $\beta$ to the horizontal. A projectile is launched from the incline with speed $u$ at an angle $\alpha$ <em>relative to the incline surface</em>.</p>
      <p><strong>The Mentor's Coordinate Hack:</strong> Don't use standard horizontal ($x$) and vertical ($y$) axes—that makes the ground boundary condition an annoying linear equation $y = x\tan\beta$. Instead, rotate your coordinate frame so the $x$-axis lies <em>along the incline</em> and the $y$-axis is <em>perpendicular to the incline</em>!</p>
      <p>Now resolve acceleration due to gravity:</p>
      $$a_x = -g\sin\beta, \quad a_y = -g\cos\beta$$
      <p>Notice that gravity now acts along <strong>both</strong> axes! The flight ends when the projectile hits the incline, which is simply $y = 0$. That gives the time of flight instantly:</p>
      $$y(T) = (u\sin\alpha)T - \frac{1}{2}(g\cos\beta)T^2 = 0 \implies T = \frac{2u\sin\alpha}{g\cos\beta}$$
      <p>Range along the incline is the displacement along $x$ over this time $T$:</p>
      $$R = (u\cos\alpha)T - \frac{1}{2}(g\sin\beta)T^2 = \frac{u^2}{g\cos^2\beta}\left[\sin(2\alpha + \beta) - \sin\beta\right]$$
      <p>To maximize range up the incline, maximize $\sin(2\alpha + \beta) = 1 \implies 2\alpha + \beta = 90^\circ$:</p>
      $$\alpha_{\text{optimal}} = \frac{\pi}{4} - \frac{\beta}{2} = 45^\circ - \frac{\beta}{2}$$
      $$R_{\max} = \frac{u^2}{g(1 + \sin\beta)}$$
            <p>For a downhill projectile, simply flip the sign of $\beta$: $R_{\max, \text{down}} = \frac{u^2}{g(1 - \sin\beta)}$.</p>

      <h3 class="sub-title">1.1.3 River-Swimmer Optimal Drift Calculus & 3D Vector Interception</h3>
      <p>Let us dissect the river-swimmer problem with vector precision. Let river velocity be $\mathbf{v}_r = u\hat{i}$ and swimmer speed in still water be $v$. The width of the river is $d$. The swimmer heads at angle $\theta$ relative to the upstream bank.</p>
      <p><strong>Case 1: Crossing in Minimum Time:</strong></p>
      <p>The time to cross depends strictly on the perpendicular velocity component $v_y = v\sin\theta$:</p>
      $$t = \frac{d}{v\sin\theta}$$
      <p>To minimize $t$, maximize $\sin\theta = 1 \implies \theta = 90^\circ$ (swimming directly perpendicular to the bank). The minimum crossing time is $t_{\min} = \frac{d}{v}$. During this time, the swimmer drifts downstream by distance $x = u \cdot t_{\min} = \frac{u}{v}d$.</p>
      <p><strong>Case 2: Zero Drift Condition ($v \ge u$):</strong></p>
      <p>If the swimmer can swim faster than the river current, zero drift ($x = 0$) is possible by heading upstream such that the upstream velocity component cancels river flow:</p>
      $$v\cos\phi = u \implies \cos\phi = \frac{u}{v}$$
      <p>where $\phi$ is the angle with the upstream direction. The resulting crossing speed is $\sqrt{v^2 - u^2}$, and crossing time is $t = \frac{d}{\sqrt{v^2 - u^2}}$.</p>
      <p><strong>Case 3: Drift Minimization When River Outruns Swimmer ($u > v$):</strong></p>
      <p>This is where 80% of JEE aspirants lose marks. When $u > v$, zero drift is physically impossible—the current will inevitably sweep the swimmer downstream. The question becomes: <em>What heading angle $\theta$ minimizes the total downstream drift $x$?</em></p>
      <p>Let the swimmer head at angle $\theta$ to the upstream bank ($90^\circ < \theta < 180^\circ$). The crossing time is $t = \frac{d}{v\sin\theta}$, and the net downstream drift is:</p>
      $$x = (u - v\cos\theta)t = (u - v\cos\theta)\frac{d}{v\sin\theta} = d\left(\frac{u}{v}\csc\theta - \cot\theta\right)$$
      <p>To minimize drift, differentiate $x$ with respect to $\theta$ and set to zero:</p>
      $$\frac{dx}{d\theta} = d\left(-\frac{u}{v}\csc\theta\cot\theta + \csc^2\theta\right) = 0 \implies \cos\theta = \frac{v}{u}$$
      <p>Look at that magnificent result: when $u > v$, the optimal heading satisfies $\cos\theta = \mathbf{v/u}$, and the minimum downstream drift is:</p>
      $$x_{\min} = d \sqrt{\frac{u^2}{v^2} - 1}$$
      <p><strong>The Geometric Tangent Construction:</strong> Draw a circle of radius $v$ centered at the origin, with vector $\mathbf{u}$ along the horizontal axis. The minimum drift occurs when the resultant velocity vector $\mathbf{v}_{res} = \mathbf{u} + \mathbf{v}$ is tangent to the circle of radius $v$! This pure geometric construction yields $\sin\alpha = v/u$ in two seconds flat without calculus.</p>

      <h2 class="section-title">1.2 Master Formula Summary Table: Kinematics</h2>
      <div class="formula-table-container">
        <table class="formula-table">
          <thead>
            <tr>
              <th>Physical Principle</th>
              <th>Mathematical Formulation</th>
              <th>Strict Domain of Validity</th>
              <th>Catastrophic Error Regime</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Constant Acceleration Kinematics</strong></td>
              <td class="formula-math">$$\mathbf{v} = \mathbf{u} + \mathbf{a}t, \quad \Delta\mathbf{r} = \mathbf{u}t + \frac{1}{2}\mathbf{a}t^2$$</td>
              <td><span class="validity-tag">Strictly constant acceleration vector</span></td>
              <td><span class="invalidity-tag">Applying to variable acceleration like spring oscillations or drag</span></td>
            </tr>
            <tr>
              <td><strong>General 1D Differential Calculus</strong></td>
              <td class="formula-math">$$v = \frac{dx}{dt}, \quad a = \frac{dv}{dt} = v\frac{dv}{dx}$$</td>
              <td><span class="validity-tag">Always valid in 1D continuous paths</span></td>
              <td><span class="invalidity-tag">Integrating $v dv = a dx$ when $a$ depends on time $t$ rather than position $x$</span></td>
            </tr>
            <tr>
              <td><strong>Intrinsic Radius of Curvature</strong></td>
              <td class="formula-math">$$\rho = \frac{v^2}{a_\perp} = \frac{v^3}{|\mathbf{v} \times \mathbf{a}|}$$</td>
              <td><span class="validity-tag">Any smooth 2D/3D trajectory ($a_\perp > 0$)</span></td>
              <td><span class="invalidity-tag">Substituting full acceleration magnitude instead of normal component $a_\perp$</span></td>
            </tr>
            <tr>
              <td><strong>Incline Projectile Optimal Launch</strong></td>
              <td class="formula-math">$$\alpha_{opt} = \frac{\pi}{4} - \frac{\beta}{2}, \quad R_{\max} = \frac{u^2}{g(1 + \sin\beta)}$$</td>
              <td><span class="validity-tag">Flat incline, uniform gravity, zero air drag</span></td>
              <td><span class="invalidity-tag">Measuring launch angle $\alpha$ from horizontal instead of incline surface</span></td>
            </tr>
            <tr>
              <td><strong>River-Swimmer Drift Minimization</strong></td>
              <td class="formula-math">$$\sin\theta = \frac{v_{mr}}{u_r} \quad (\text{for } u_r > v_{mr})$$</td>
              <td><span class="validity-tag">River speed exceeds swimmer speed in still water</span></td>
              <td><span class="invalidity-tag">Attempting perpendicular crossing ($\theta = 90^\circ$) and getting massive drift</span></td>
            </tr>
            <tr>
              <td><strong>Relative Velocity Definition</strong></td>
              <td class="formula-math">$$\mathbf{v}_{A/B} = \mathbf{v}_A - \mathbf{v}_B$$</td>
              <td><span class="validity-tag">All classical non-relativistic reference frames</span></td>
              <td><span class="invalidity-tag">Adding velocity vectors directly instead of subtracting relative frame</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">1.3 The Forensic Negative-Marking Trap Matrix (10 Alerts)</h2>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.1] Average Speed vs. Magnitude of Average Velocity</div>
        <p><strong>The Trap:</strong> Assuming average speed $\langle v \rangle$ equals the magnitude of average velocity $|\langle \mathbf{v} \rangle|$.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Average speed is Total Distance / Total Time: $\langle v \rangle = \frac{\int v dt}{\Delta t}$. Average velocity is Net Displacement / Total Time: $\langle \mathbf{v} \rangle = \frac{\Delta \mathbf{r}}{\Delta t}$. Because straight-line distance is always $\ge$ net displacement, $\langle v \rangle \ge |\langle \mathbf{v} \rangle|$. They are equal if and only if the particle moves in a straight line without reversing direction!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.2] Zero Velocity Does NOT Mean Zero Acceleration</div>
        <p><strong>The Trap:</strong> Setting acceleration to zero when a particle momentarily comes to rest ($v = 0$).</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Acceleration is the rate of change of velocity ($a = dv/dt$), not velocity itself. At the apex of a vertical toss, $v = 0$, but acceleration is $g = 9.8\text{ m/s}^2$ downward! If acceleration were zero at the apex, the ball would freeze in mid-air forever.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.3] Incline Projectile Angle Referencing Blunder</div>
        <p><strong>The Trap:</strong> Blindly using launch angle $\theta$ in formulas without checking whether the problem defines it relative to the horizontal ground or relative to the inclined plane surface.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Always re-sketch and confirm: if launch angle from horizontal is $\theta$ and incline angle is $\beta$, the launch angle relative to the incline is $\alpha = \theta - \beta$. If you confuse these two angles, your range formula will be completely wrong.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.4] Radius of Curvature Acceleration Projection Error</div>
        <p><strong>The Trap:</strong> Computing $\rho = v^2 / a$ using the total acceleration $a$ instead of the normal acceleration component $a_\perp$.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> By definition, curvature reflects trajectory bending, which is governed strictly by $a_\perp = v^2/\rho$. For a standard projectile at launch with speed $u$ at angle $\theta$, gravity acts straight down ($g$). Velocity is at angle $\theta$. The normal component of gravity is $a_\perp = g\cos\theta$. Therefore, $\rho = \frac{u^2}{g\cos\theta}$, NOT $u^2/g$!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.5] River-Swimmer Drift Minimization when River Outruns Swimmer</div>
        <p><strong>The Trap:</strong> When river flow $u$ exceeds swimmer still-water speed $v$, students try to swim straight across or aim upstream at $\sin\theta = u/v > 1$, which is mathematically impossible.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> When $u > v$, drift cannot be zero. Draw the velocity circle: the tangent from the origin to the circle of radius $v$ centered at $(\mathbf{u})$ gives the minimum drift direction: $\sin\theta_{\min} = v/u$. The swimmer must aim upstream at angle $\theta = \arcsin(v/u)$ to the bank to minimize total downstream drift!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.6] Rain-Man Relative Velocity Vector Sign Inversion</div>
        <p><strong>The Trap:</strong> Drawing the relative rain velocity as $\mathbf{v}_{rain} + \mathbf{v}_{man}$ instead of $\mathbf{v}_{rain} - \mathbf{v}_{man}$.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> The umbrella must point along the velocity of rain <em>relative to the person</em>: $\mathbf{v}_{r/m} = \mathbf{v}_r - \mathbf{v}_m$. If rain falls vertically with $-u\hat{\mathbf{j}}$ and you walk forward with $+v\hat{\mathbf{i}}$, then $\mathbf{v}_{r/m} = -v\hat{\mathbf{i}} - u\hat{\mathbf{j}}$. The rain appears to come from ahead of you, so you must tilt the umbrella forward!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.7] Turning Point vs. Peak Height Identification</div>
        <p><strong>The Trap:</strong> Assuming a particle turns around only when position reaches a maximum, without checking for velocity sign change.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> A physical turning point occurs strictly where velocity changes sign: $\dot{x}(t_0) = 0$ with $\ddot{x}(t_0) \ne 0$. If velocity touches zero but doesn't change sign (e.g., $v(t) = t^2$), the particle merely pauses and continues in the same direction!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.8] Misapplying Constant Acceleration to Non-Uniform Jerk</div>
        <p><strong>The Trap:</strong> Given acceleration $a = 2t$, calculating distance as $s = ut + \frac{1}{2}(2t)t^2 = ut + t^3$.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> The formula $\frac{1}{2}at^2$ is derived by integrating a <em>constant</em> acceleration twice. When $a(t) = 2t$, you must integrate from scratch: $v(t) = \int 2t dt = t^2 + v_0$, then $s(t) = \int (t^2 + v_0) dt = \frac{1}{3}t^3 + v_0 t$. The factor is $1/3$, not $1/2$ or $1$!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.9] Projectile Velocity at Specified Height Has Two Solutions</div>
        <p><strong>The Trap:</strong> Assuming there is only one time and velocity when a projectile reaches height $h$.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Gravity acts symmetrically. The projectile crosses height $h$ twice: once on the way up with velocity $(u_x \hat{\mathbf{i}} + v_y \hat{\mathbf{j}})$, and once on the way down with velocity $(u_x \hat{\mathbf{i}} - v_y \hat{\mathbf{j}})$. Their speeds are identical ($v = \sqrt{u^2 - 2gh}$), but their velocity vectors are completely different!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 1.10] Horizontal Component of Velocity in Projectile Motion</div>
        <p><strong>The Trap:</strong> Forgetting that air drag or incline coordinate frames change the horizontal acceleration.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Horizontal velocity is constant ($u_x = u\cos\theta$) <em>if and only if</em> there is zero horizontal force. In an inclined coordinate system, $a_x = -g\sin\beta \ne 0$. In real air drag, $a_x = -k v^2 \cos\theta \ne 0$. Always verify the net force along each axis before assuming velocity is constant!</div>
      </div>

      <h2 class="section-title">1.4 Dissected JEE Advanced Previous Year Questions (PYQs)</h2>

      <!-- PYQ 1.1 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">JEE Advanced 2019 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Hard • Optimal River Drift Calculus</span>
        </div>
        <div class="pyq-question">
          A river of width $d = 400\text{ m}$ flows with uniform speed $u = 5\text{ m/s}$. A swimmer can swim with speed $v = 3\text{ m/s}$ in still water. Since the river flow speed exceeds the swimmer's speed ($u > v$), the swimmer cannot reach the directly opposite bank. Determine: (a) the minimum downstream drift $x_{\min}$ achievable, and (b) the direction $\theta$ relative to the river bank at which the swimmer must steer to achieve this minimum drift.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Setup Coordinate Frame & Velocity Components:</strong></p>
          <p>Let the river flow along the positive $x$-axis: $\mathbf{u}_r = u\hat{\mathbf{i}} = 5\hat{\mathbf{i}}\text{ m/s}$.</p>
          <p>Let the swimmer head at angle $\theta$ relative to the upstream bank ($90^\circ < \theta < 180^\circ$):</p>
          $$\mathbf{v}_{swimmer} = (u - v\cos\theta)\hat{\mathbf{i}} + (v\sin\theta)\hat{\mathbf{j}}$$
          <p><strong>Step 2: Calculate Crossing Time and Drift:</strong></p>
          <p>Time to cross the river of width $d = 400\text{ m}$ is determined purely by the $y$-component:</p>
          $$t = \frac{d}{v_y} = \frac{d}{v\sin\theta}$$
          <p>The downstream drift $x$ is the horizontal distance traveled during this time:</p>
          $$x(\theta) = v_x t = (u - v\cos\theta)\left(\frac{d}{v\sin\theta}\right) = d\left(\frac{u}{v}\csc\theta - \cot\theta\right)$$
          <p><strong>Step 3: Minimize Drift Using Calculus:</strong></p>
          <p>Differentiating $x(\theta)$ with respect to $\theta$ and setting to zero:</p>
          $$\frac{dx}{d\theta} = d\left(-\frac{u}{v}\csc\theta\cot\theta + \csc^2\theta\right) = 0$$
          <p>Solving for the launch angle $\theta$:</p>
          $$\cos\theta = \frac{v}{u}$$
          <p>Substituting swimmer speed $v = 3\text{ m/s}$ and river speed $u = 5\text{ m/s}$:</p>
          $$\cos\theta = \frac{3}{5} \implies \sin\theta = \frac{4}{5}$$
          $$\theta = \arccos(3/5) \approx 53.13^\circ \quad (\text{directed upstream})$$
          <p><strong>Step 4: Compute Minimum Drift:</strong></p>
          <p>Substitute these values back into the drift equation:</p>
          $$x_{\min} = 400\left(\frac{5}{3}\cdot\frac{5}{4} - \frac{3}{4}\right) = 400\left(\frac{25}{12} - \frac{9}{12}\right)$$
          $$x_{\min} = 400 \times \frac{16}{12} = \frac{1600}{3}\text{ m} \approx \mathbf{533.33\text{ meters}}$$
        </div>
      </div>

      <!-- PYQ 1.2 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">JEE Advanced 2016 • Paper 2</span>
          <span class="pyq-difficulty">Difficulty: Moderate • Projectile on Incline Range Ratio</span>
        </div>
        <div class="pyq-question">
          A projectile is launched from the base of an inclined plane of inclination $\beta = 30^\circ$. If the projectile strikes the incline perpendicularly, find the ratio of the launch angle $\theta$ (measured from the horizontal) to the inclination angle $\beta$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Rotate to Incline Coordinate System:</strong></p>
          <p>Let the $x$-axis be directed up the incline, and the $y$-axis be normal to the incline.</p>
          <p>The launch angle relative to the incline surface is $\alpha = \theta - \beta$.</p>
          <p>Velocity components at launch: $u_x = u\cos\alpha, u_y = u\sin\alpha$.</p>
          <p>Acceleration components: $a_x = -g\sin\beta, a_y = -g\cos\beta$.</p>
          <p><strong>Step 2: Perpendicular Impact Condition:</strong></p>
          <p>Striking the plane <em>perpendicularly</em> means the parallel velocity component vanishes at impact: $v_x(T) = 0$.</p>
          $$v_x(T) = u\cos\alpha - (g\sin\beta)T = 0 \implies T = \frac{u\cos\alpha}{g\sin\beta}$$
          <p><strong>Step 3: Total Time of Flight from Normal Motion ($y = 0$):</strong></p>
          $$T = \frac{2u\sin\alpha}{g\cos\beta}$$
          <p><strong>Step 4: Equate Both Expressions for Time of Flight $T$:</strong></p>
          $$\frac{u\cos\alpha}{g\sin\beta} = \frac{2u\sin\alpha}{g\cos\beta}$$
          <p>Dividing both sides by $\cos\alpha$ and rearranging yields:</p>
          $$\tan\alpha = \frac{1}{2}\cot\beta$$
          <p>Given $\beta = 30^\circ$, we have $\cot 30^\circ = \sqrt{3}$:</p>
          $$\tan\alpha = \frac{\sqrt{3}}{2} \implies \alpha = \arctan\left(\frac{\sqrt{3}}{2}\right) \approx 40.89^\circ$$
          $$\theta = \alpha + \beta = 40.89^\circ + 30^\circ = 70.89^\circ$$
          $$\text{Ratio: } \frac{\theta}{\beta} = \frac{70.89^\circ}{30^\circ} \approx \mathbf{2.36}$$
        </div>
      </div>

      <!-- PYQ 1.3 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">JEE Advanced 2021 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Hard • Trajectory Curvature & Normal Acceleration</span>
        </div>
        <div class="pyq-question">
          A particle moves in the $xy$-plane according to the trajectory $y = \alpha x^2$, where $\alpha = 0.5\text{ m}^{-1}$. The $x$-component of velocity is maintained constant at $v_x = c = 4\text{ m/s}$. Find the magnitude of the particle's total acceleration $\mathbf{a}$ and the radius of curvature $\rho$ at the point $x = 1\text{ m}$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Compute Kinematic Derivatives with Respect to Time:</strong></p>
          <p>Given $x(t)$ has constant velocity: $\dot{x} = 4\text{ m/s} \implies \ddot{x} = 0$.</p>
          $$y = \alpha x^2 \implies \dot{y} = 2\alpha x \dot{x} = 2(0.5)(1)(4) = \mathbf{4\text{ m/s}}$$
          $$\ddot{y} = \frac{d}{dt}(2\alpha x \dot{x}) = 2\alpha (\dot{x}^2 + x\ddot{x}) = 2(0.5)(4^2 + 1 \times 0) = \mathbf{16\text{ m/s}^2}$$
          <p><strong>Step 2: Total Velocity and Acceleration Vectors:</strong></p>
          $$\mathbf{v} = 4\hat{\mathbf{i}} + 4\hat{\mathbf{j}} \implies v = \sqrt{4^2 + 4^2} = 4\sqrt{2}\text{ m/s}$$
          $$\mathbf{a} = \ddot{x}\hat{\mathbf{i}} + \ddot{y}\hat{\mathbf{j}} = 0\hat{\mathbf{i}} + 16\hat{\mathbf{j}} \implies a = \mathbf{16\text{ m/s}^2}$$
          <p><strong>Step 3: Decompose into Tangential and Normal Acceleration:</strong></p>
          $$a_t = \frac{\mathbf{v}\cdot\mathbf{a}}{v} = \frac{(4)(0) + (4)(16)}{4\sqrt{2}} = \frac{64}{4\sqrt{2}} = \frac{16}{\sqrt{2}} = 8\sqrt{2}\text{ m/s}^2$$
          $$a_n = \sqrt{a^2 - a_t^2} = \sqrt{16^2 - (8\sqrt{2})^2} = \sqrt{256 - 128} = \sqrt{128} = 8\sqrt{2}\text{ m/s}^2$$
          <p><strong>Step 4: Compute Radius of Curvature:</strong></p>
          $$\rho = \frac{v^2}{a_n} = \frac{(4\sqrt{2})^2}{8\sqrt{2}} = \frac{32}{8\sqrt{2}} = \frac{4}{\sqrt{2}} = \mathbf{2\sqrt{2}\text{ m}} \approx \mathbf{2.83\text{ meters}}$$
        </div>
      </div>

      <h2 class="section-title">1.5 High-Caliber Practice Challenge Problems & Complete Solutions</h2>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 1.1] The Parabolic Safety Envelope</div>
        <p>A defensive battery on a level plain can fire shells in any direction with fixed muzzle speed $u = 200\text{ m/s}$. Find the mathematical equation of the parabolic boundary (envelope of safety) beyond which no shell can reach. Take $g = 10\text{ m/s}^2$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>The trajectory equation for launch angle $\theta$ is:</p>
            $$y = x\tan\theta - \frac{gx^2}{2u^2}(1 + \tan^2\theta)$$
            <p>Treat this as a quadratic equation in $T = \tan\theta$:</p>
            $$\left(\frac{gx^2}{2u^2}\right)T^2 - x T + \left(y + \frac{gx^2}{2u^2}\right) = 0$$
            <p>For a target $(x, y)$ to be reachable, the discriminant must be non-negative ($\Delta \ge 0$):</p>
            $$\Delta = (-x)^2 - 4\left(\frac{gx^2}{2u^2}\right)\left(y + \frac{gx^2}{2u^2}\right) \ge 0$$
            $$x^2 - \frac{2gx^2}{u^2}y - \frac{g^2 x^4}{u^4} \ge 0 \implies 1 - \frac{2gy}{u^2} - \frac{gx^2}{u^2} \ge 0$$
            $$y \le \frac{u^2}{2g} - \frac{gx^2}{2u^2}$$
            <p>Substituting $u = 200\text{ m/s}$ and $g = 10\text{ m/s}^2$:</p>
            $$\frac{u^2}{2g} = \frac{40,000}{20} = 2000\text{ m}, \quad \frac{g}{2u^2} = \frac{10}{2(40,000)} = \frac{1}{8000}$$
            $$y_{\text{envelope}}(x) = \mathbf{2000 - \frac{x^2}{8000}\text{ meters}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 1.2] Cyclic Pursuit on a Regular Hexagon</div>
        <p>Six particles $A_1, A_2, \dots, A_6$ are positioned at the vertices of a regular hexagon of side length $L = 60\text{ m}$. Each particle moves with constant speed $v = 5\text{ m/s}$ heading continuously toward its clockwise neighbor. Find the time $t_{col}$ required for all six particles to collide at the center of the hexagon.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Consider any two adjacent particles $A_1$ and $A_2$. By circular symmetry, the particles remain at the vertices of a shrinking regular hexagon at every instant.</p>
            <p>The interior angle of a regular hexagon is $120^\circ$. The angle between the velocity vector of $A_1$ (pointing toward $A_2$) and the velocity vector of $A_2$ is $60^\circ$.</p>
            <p>The rate at which the distance $r$ between $A_1$ and $A_2$ decreases (relative approach speed along the line connecting them) is:</p>
            $$v_{app} = v_1 + v_2\cos(180^\circ - 120^\circ) = v - v\cos(120^\circ) = v - v(-0.5) = 1.5 v$$
            <p>Alternatively, looking at the line connecting $A_1$ to $A_2$: $A_1$ moves directly toward $A_2$ at speed $v$, while $A_2$ moves at angle $60^\circ$ away from this line. Thus:</p>
            $$-\frac{dr}{dt} = v - v\cos 60^\circ = v - \frac{1}{2}v = \frac{1}{2}v$$
            <p>Integrating from $r = L$ to $r = 0$:</p>
            $$t_{col} = \frac{L}{\frac{1}{2}v} = \frac{2L}{v} = \frac{2(60)}{5} = \mathbf{24.0\text{ seconds}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 1.3] Non-Uniform Jerk Trajectory Integration</div>
        <p>A particle starts from rest at the origin ($x=0, v=0$ at $t=0$). Its rate of change of acceleration (jerk) is given by $j(t) = 6t\text{ m/s}^3$. Find (a) the velocity $v(t)$, (b) the position $x(t)$, and (c) the average velocity over the time interval from $t = 0$ to $t = 2\text{ s}$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Integrate jerk to get acceleration:</p>
            $$a(t) = \int j(t) dt = \int 6t dt = 3t^2 + a_0 = 3t^2\text{ m/s}^2 \quad (\text{since } a(0)=0)$$
            <p>Integrate acceleration to get velocity:</p>
            $$v(t) = \int 3t^2 dt = t^3 + v_0 = t^3\text{ m/s} \quad (\text{since } v(0)=0)$$
            <p>Integrate velocity to get position:</p>
            $$x(t) = \int t^3 dt = \frac{1}{4}t^4 + x_0 = \frac{1}{4}t^4\text{ m}$$
            <p>At $t = 2\text{ s}$:</p>
            $$x(2) = \frac{1}{4}(2^4) = \frac{16}{4} = 4\text{ meters}$$
            $$\langle v \rangle = \frac{x(2) - x(0)}{2 - 0} = \frac{4 - 0}{2} = \mathbf{2.0\text{ m/s}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 1.4] Optimal Launch Angle to Clear Elevated Wall</div>
        <p>A stone is to be thrown from the ground to clear a vertical wall of height $H = 20\text{ m}$ situated at a horizontal distance $D = 40\text{ m}$ from the launch point. Determine the minimum initial launch speed $u_{\min}$ required. Take $g = 10\text{ m/s}^2$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Using the parabolic safety envelope equation: a point $(D, H)$ lies on the boundary of reachability if:</p>
            $$H = \frac{u_{\min}^2}{2g} - \frac{g D^2}{2 u_{\min}^2}$$
            <p>Let $w = u_{\min}^2 / (2g)$. Then $H = w - \frac{D^2}{4w} \implies w^2 - H w - \frac{D^2}{4} = 0$.</p>
            $$w = \frac{H + \sqrt{H^2 + D^2}}{2}$$
            $$w = \frac{20 + \sqrt{20^2 + 40^2}}{2} = \frac{20 + \sqrt{400 + 1600}}{2} = \frac{20 + 20\sqrt{5}}{2} = 10(1 + \sqrt{5})\text{ m}$$
            <p>Since $w = u_{\min}^2 / (2g)$:</p>
            $$u_{\min}^2 = 2g w = 2(10)(10)(1 + \sqrt{5}) = 200(1 + 2.236) = 647.2\text{ m}^2/\text{s}^2$$
            $$u_{\min} = \sqrt{647.2} \approx \mathbf{25.44\text{ m/s}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 1.5] Wind-Affected Asymmetric Projectile Range</div>
        <p>A projectile is launched with speed $u = 50\text{ m/s}$ at an angle $\theta = 45^\circ$ to the horizontal. A steady horizontal wind produces a constant horizontal deceleration $a_x = -2\text{ m/s}^2$ against the flight. Gravity $g = 10\text{ m/s}^2$ acts vertically. Find the horizontal range $R$ of the projectile on level ground.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Initial velocity components:</p>
            $$u_x = 50\cos 45^\circ = 25\sqrt{2}\text{ m/s}, \quad u_y = 50\sin 45^\circ = 25\sqrt{2}\text{ m/s}$$
            <p>Time of flight is determined purely by vertical motion ($y = 0$):</p>
            $$T = \frac{2u_y}{g} = \frac{2(25\sqrt{2})}{10} = 5\sqrt{2}\text{ seconds}$$
            <p>Horizontal displacement with wind deceleration $a_x = -2\text{ m/s}^2$:</p>
            $$R = u_x T + \frac{1}{2}a_x T^2 = (25\sqrt{2})(5\sqrt{2}) - \frac{1}{2}(2)(5\sqrt{2})^2$$
            $$R = 25 \times 2 \times 5 - 1(50) = 250 - 50 = \mathbf{200.0\text{ meters}}$$
            <p>Without wind, range would be $u^2/g = 2500/10 = 250\text{ m}$. The wind robs exactly $50\text{ m}$ of distance!</p>
          </div>
        </details>
      </div>
    </section>
    """

if __name__ == "__main__":
    c = get_ch1_content()
    print("Chapter 1 regenerated successfully. Length:", len(c))
