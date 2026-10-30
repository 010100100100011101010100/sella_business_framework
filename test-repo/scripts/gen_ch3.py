# Chapter 3 Generator: Work, Energy & Power Mastery
# Conversational Kota Mentor Voice • Zero Emojis • Modern Typography

def get_ch3_content():
    return r"""
    <section id="ch3" class="chapter-container">
      <span class="chapter-number">Chapter 03</span>
      <h1 class="chapter-title">Work, Energy & Power Mastery</h1>

      <div class="card-box tip-card">
        <div class="card-header-tip">[MENTOR STRATEGY NOTE] Why Energy Methods Separate Top Ranks from the Rest</div>
        <p><strong>Listen closely, aspirants:</strong> Newton's Second Law ($\mathbf{F} = m\mathbf{a}$) is a vector differential equation. If the force direction changes continuously—like a bead sliding on a curved wire or a pendulum swinging through an arc—solving $\mathbf{F} = m\mathbf{a}$ directly requires solving painful differential equations. Energy methods bypass time and trajectory details completely. A single scalar equation connects your initial launch state directly to your final state.</p>
        <p><strong>The Catch?</strong> The Work-Energy Theorem ($W_{net} = \Delta K$) is foolproof, but students blunder constantly on the signs: work done by normal forces on moving wedges is NOT zero, string tension slackening is NOT velocity vanishing in vertical circles, and internal forces can do massive amounts of work. Let's master the physics so you never get trapped.</p>
      </div>

      <h2 class="section-title">3.1 First-Principles Foundations: Energy Conservation & Field Theorems</h2>
      
      <p>Where does the Work-Energy Theorem come from? It is not a separate postulate—it is simply Newton's Second Law integrated along the path of motion:</p>

      $$W_{net} = \int_{1}^{2} \mathbf{F}_{net} \cdot d\mathbf{r} = m\int_{\mathbf{v}_1}^{\mathbf{v}_2} \mathbf{v}\cdot d\mathbf{v} = \frac{1}{2}m v_2^2 - \frac{1}{2}m v_1^2 = \Delta K$$

      <p>Look at what that derivation assumed: <em>absolutely nothing about the nature of the forces!</em> It holds true in any inertial frame for gravity, spring forces, friction, normal pushes, and tension. Total work done by all forces always equals the change in kinetic energy.</p>

      <h3 class="sub-title">3.1.1 Potential Energy Curves $U(x)$ and Equilibrium Stability</h3>
      <p>Think of potential energy $U(x)$ like a rolling landscape. A ball naturally rolls downhill toward lower potential energy. The force pushing the object is simply how steep that hill is at that point, with a minus sign because the push points downhill toward lower energy: $F(x) = -\frac{dU}{dx}$. An equilibrium point $x_0$ is a flat spot—the bottom of a valley, the crest of a ridge, or a flat plateau—where the slope is zero and the net force vanishes: $\left.\frac{dU}{dx}\right|_{x_0} = 0$.</p>

      <!-- SVG Diagram 3.1: Potential Energy Curve -->
      <div class="diagram-container">
                <svg class="diagram-svg" width="600" height="240" viewBox="0 0 600 240">
          <defs>
            <marker id="arrow-ch3" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#0f172a"/>
            </marker>
          </defs>
          <line x1="50" y1="210" x2="550" y2="210" stroke="#0f172a" stroke-width="2.5" marker-end="url(#arrow-ch3)" />
          <line x1="70" y1="230" x2="70" y2="30" stroke="#0f172a" stroke-width="2.5" marker-end="url(#arrow-ch3)" />
          <text x="560" y="215" font-family="sans-serif" font-size="14" fill="#0f172a">x</text>
          <text x="60" y="25" font-family="sans-serif" font-size="14" fill="#0f172a">U(x)</text>
          <!-- Curve U(x) -->
          <path d="M 80 50 C 130 180, 180 200, 240 180 C 290 160, 320 70, 380 70 C 440 70, 480 180, 540 180" fill="none" stroke="#b45309" stroke-width="3.5" />
          <!-- Stable Point -->
          <circle cx="210" cy="188" r="7" fill="#047857" />
          <text x="150" y="210" font-family="sans-serif" font-size="13" font-weight="bold" fill="#047857">Stable: U'' &gt; 0</text>
          <!-- Unstable Point -->
          <circle cx="380" cy="70" r="7" fill="#b91c1c" />
          <text x="330" y="55" font-family="sans-serif" font-size="13" font-weight="bold" fill="#b91c1c">Unstable: U'' &lt; 0</text>
          <!-- Neutral Point -->
          <circle cx="510" cy="180" r="7" fill="#6d28d9" />
          <text x="460" y="165" font-family="sans-serif" font-size="13" font-weight="bold" fill="#6d28d9">Neutral: U'' = 0</text>
        </svg>
        <div class="diagram-caption">Figure 3.1: Potential energy landscape $U(x)$ indicating stable, unstable, and neutral equilibrium coordinates.</div>
      </div>

      <p>Classifying equilibrium points is straightforward:</p>
      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Stable Equilibrium (Valley Bottom):</strong> $\left.\frac{d^2U}{dx^2}\right|_{x_0} > 0$. The curve cups upward. If you nudge the particle, the walls push it right back. The particle oscillates in Simple Harmonic Motion with frequency:
        $$\omega = \sqrt{\frac{U''(x_0)}{m}}$$</li>
        <li><strong>Unstable Equilibrium (Hill Crest):</strong> $\left.\frac{d^2U}{dx^2}\right|_{x_0} < 0$. The curve domes downward. A tiny nudge rolls the particle further away down the slope.</li>
        <li><strong>Neutral Equilibrium (Flat Plateau):</strong> $\left.\frac{d^2U}{dx^2}\right|_{x_0} = 0$. The ground is flat. Nudging the particle simply moves it to a new resting spot with no restoring or runaway force.</li>
      </ul>

      <h3 class="sub-title">3.1.2 Vertical Circular Motion (VCM): The Definitive Regime Breakdown</h3>
      <p>Take a bob of mass $m$ tied to a light string of length $R$ and project it horizontally at the lowest point with speed $u$. Let $\theta$ be the angle from the downward vertical. Mechanical energy conservation gives velocity at any angle:</p>
      $$v^2(\theta) = u^2 - 2gR(1 - \cos\theta)$$
      <p>Now write Newton's Second Law along the radial direction toward the center:</p>
      $$T(\theta) - mg\cos\theta = \frac{mv^2(\theta)}{R} \implies T(\theta) = \frac{m}{R}\left[u^2 - gR(2 - 3\cos\theta)\right]$$

      <p>Now memorize these three distinct physical regimes—JEE Advanced tests the boundaries every year:</p>
      <ol style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>The Pure Oscillation Regime ($u \le \sqrt{2gR}$):</strong>
          Velocity vanishes ($v = 0$) at or before $\theta = 90^\circ$ (horizontal level). Because $\cos\theta \ge 0$, tension $T = \frac{m}{R}[u^2 - gR(2 - 3\cos\theta)]$ remains strictly positive throughout! The string never goes slack. The bob oscillates like a regular pendulum with maximum angular amplitude $\theta_{\max} = \arccos(1 - u^2/2gR)$.
        </li>
        <li><strong>The Slackening & Projectile Regime ($\sqrt{2gR} < u < \sqrt{5gR}$):</strong>
          Velocity is still positive at $\theta = 90^\circ$, but tension vanishes ($T = 0$) at an angle $\theta_0 \in (90^\circ, 180^\circ)$ in the upper semicircle! Setting $T(\theta_0) = 0$:
          $$\cos\theta_0 = -\frac{u^2 - 2gR}{3gR}$$
          <strong>Fatal Mistake to Avoid:</strong> The particle does NOT fall straight down! At the instant $T=0$, the string goes limp, but the particle has speed $v_0 = \sqrt{gR|\cos\theta_0|}$ directed tangentially upward. From this instant, the particle acts as a <strong>free parabolic projectile</strong> under gravity alone!
        </li>
        <li><strong>The Complete Looping Regime ($u \ge \sqrt{5gR}$):</strong>
          For complete vertical circular loops, tension must not vanish even at the very top ($\theta = 180^\circ$):
          $$T_{top} = \frac{m}{R}(u^2 - 5gR) \ge 0 \implies u \ge \sqrt{5gR}$$
          At critical speed $u = \sqrt{5gR}$, the speed at the top is $v_{top} = \sqrt{gR}$, and tension at the top is exactly zero.
          Notice this universal, launch-speed-independent identity:
          $$T_{bottom} - T_{top} = 6mg$$
        </li>
      </ol>

      <h3 class="sub-title">3.1.3 Potential Energy Landscape & Turning Point Phase Analysis</h3>
      <p>When a particle of total mechanical energy $E$ moves in a conservative one-dimensional potential field $U(x)$, its kinetic energy is strictly non-negative: $K(x) = E - U(x) \ge 0$. This fundamental thermodynamic and kinematic requirement partitions spatial geometry into allowed and forbidden physical zones:</p>
      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Classically Allowed Region:</strong> The domain where $E \ge U(x)$. Here velocity is real: $v(x) = \pm \sqrt{\frac{2(E - U(x))}{m}}$.</li>
        <li><strong>Turning Points:</strong> The boundary coordinates $x_t$ where total energy equals potential energy: $U(x_t) = E$. At these points, kinetic energy drops to zero ($K = 0$), so velocity vanishes momentarily ($v = 0$). The particle reflects back into the potential well.</li>
        <li><strong>Classically Forbidden Region:</strong> Any zone where $E < U(x)$. In classical mechanics, the particle can never penetrate this barrier because its kinetic energy would be negative, yielding imaginary velocity.</li>
      </ul>
      <p><strong>Bounded vs. Unbounded Orbits:</strong></p>
      <p>If the particle is trapped between two turning points $x_1$ and $x_2$ such that $U(x_1) = U(x_2) = E$ and $U(x) < E$ for all $x \in (x_1, x_2)$, the particle undergoes periodic oscillatory motion with period given by the path action integral:</p>
      $$T = 2 \int_{x_1}^{x_2} \frac{dx}{v(x)} = 2\sqrt{\frac{m}{2}} \int_{x_1}^{x_2} \frac{dx}{\sqrt{E - U(x)}}$$
      <p>Evaluating this integral yields the exact time period for arbitrary non-linear potentials where small-angle harmonic approximations no longer hold!</p>

      <h2 class="section-title">3.2 Master Formula Summary Table: Work, Energy & Power</h2>
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
              <td><strong>General Work Integral</strong></td>
              <td class="formula-math">$$W = \int_{C} \mathbf{F} \cdot d\mathbf{r} = \int (F_x dx + F_y dy + F_z dz)$$</td>
              <td><span class="validity-tag">All forces, curved paths</span></td>
              <td><span class="invalidity-tag">Using $W = \mathbf{F} \cdot \mathbf{s}$ when force magnitude or direction changes</span></td>
            </tr>
            <tr>
              <td><strong>Conservative Curl Condition</strong></td>
              <td class="formula-math">$$\nabla \times \mathbf{F} = \mathbf{0} \iff \oint \mathbf{F} \cdot d\mathbf{r} = 0$$</td>
              <td><span class="validity-tag">Simply connected domains</span></td>
              <td><span class="invalidity-tag">Defining potential energy $U$ for non-conservative or friction forces</span></td>
            </tr>
            <tr>
              <td><strong>Small Oscillation Frequency</strong></td>
              <td class="formula-math">$$\omega = \sqrt{\frac{U''(x_0)}{m}}$$</td>
              <td><span class="validity-tag">Small deviations about stable equilibrium</span></td>
              <td><span class="invalidity-tag">Applying to large amplitudes where non-linear higher terms dominate</span></td>
            </tr>
            <tr>
              <td><strong>String VCM Critical Looping</strong></td>
              <td class="formula-math">$$u_{\min} = \sqrt{5gR}, \quad v_{top} = \sqrt{gR}$$</td>
              <td><span class="validity-tag">Light inextensible string</span></td>
              <td><span class="invalidity-tag">Applying $\sqrt{5gR}$ to a rigid rod (rod requires only $\sqrt{4gR}$)</span></td>
            </tr>
            <tr>
              <td><strong>Universal VCM Tension Delta</strong></td>
              <td class="formula-math">$$T_{bottom} - T_{top} = 6mg$$</td>
              <td><span class="validity-tag">Complete vertical loops</span></td>
              <td><span class="invalidity-tag">Assuming delta depends on launch speed $u$</span></td>
            </tr>
            <tr>
              <td><strong>Conveyor Belt Heat Loss</strong></td>
              <td class="formula-math">$$Q = \frac{1}{2} m v^2 \quad (50\% \text{ of total work})$$</td>
              <td><span class="validity-tag">Mass dropped on constant-speed belt</span></td>
              <td><span class="invalidity-tag">Claiming zero dissipation because friction did positive work on mass</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">3.3 10 Forensic NTA/JEE Negative-Marking Trap Alerts</h2>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.1] The "Normal Force Never Does Work" Dogma</div>
        <p><strong>The Trap:</strong> Believing blindly that normal contact force can never do work because it is perpendicular to the contact surface.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Normal force does zero work <em>only</em> if the contact surface is stationary in your reference frame! In a movable wedge system, as the block slides down, the normal force on the wedge pushes it horizontally in the direction of motion ($W_N > 0$ on wedge), while doing equal negative work on the block ($W_N < 0$ on block). The net work summed over the closed rigid system is zero ($\sum W_N = 0$), but on individual components, normal force transfers mechanical energy!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.2] String Slackening vs Velocity Vanishing in VCM</div>
        <p><strong>The Trap:</strong> When a bob launched with $u = \sqrt{3gR}$ enters vertical circular motion, setting $v = 0$ to find the peak elevation.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> For $\sqrt{2gR} < u < \sqrt{5gR}$, tension dies first ($T = 0$) while velocity is still non-zero ($v_0 = \sqrt{gR/3}$). The bob does not stop—it leaves the circle and flies as a free projectile under gravity! Peak height is $h = h_{slack} + \frac{v_{0y}^2}{2g}$.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.3] Reference Frame Relativity of Work and Kinetic Energy</div>
        <p><strong>The Trap:</strong> Assuming work done by a force is an absolute scalar invariant that has the same numerical value in all reference frames.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Displacement is frame-dependent: $d\mathbf{r} = d\mathbf{r}' + \mathbf{V}_0 dt$. Therefore, work done $W = \int \mathbf{F} \cdot d\mathbf{r}$ and kinetic energy are strictly frame-dependent! However, the Work-Energy Theorem $\Delta K = W_{net}$ holds true in every single inertial frame.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.4] The Spring Potential Energy Sign Blunder</div>
        <p><strong>The Trap:</strong> Writing spring potential energy as negative $-\frac{1}{2}kx^2$ by false analogy with gravitational potential energy $-GMm/r$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Work done by the spring force on a block is $W_s = -\Delta U_s = -\frac{1}{2}k(x_2^2 - x_1^2)$. The elastic potential energy stored in an elongated or compressed spring is <strong>strictly positive</strong>: $U_s = +\frac{1}{2}kx^2 \ge 0$.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.5] VCM Looping with a Rigid Rod vs Light String</div>
        <p><strong>The Trap:</strong> Applying $u = \sqrt{5gR}$ to determine the minimum launch speed to complete a vertical loop for a mass fixed to a light rigid rod.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> A rigid rod can support compression ($N < 0$) without collapsing or slacking. To loop, velocity at the top only needs to not become imaginary: $v_{top} \ge 0$. By energy conservation, $u_{\min} = \sqrt{4gR} = 2\sqrt{gR}$, NOT $\sqrt{5gR}$!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.6] The 50% Thermal Dissipation Paradox on Conveyor Belts</div>
        <p><strong>The Trap:</strong> Dropping a mass $m$ gently onto a conveyor belt moving at speed $v$. Students compute work done on the mass as $\frac{1}{2}mv^2$ and claim the motor supplied only $\frac{1}{2}mv^2$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> During the slipping phase, the belt travels exactly <strong>twice</strong> the distance that the block slides across the floor! Work done by the motor is $W_{motor} = mv^2$. The block gains kinetic energy $K = \frac{1}{2}mv^2$, and exactly $50\%$ of the energy ($Q = \frac{1}{2}mv^2$) is dissipated as thermal friction heat, universally independent of $\mu$!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.7] Integrating Potential to Find Force (Upside Down Calculus)</div>
        <p><strong>The Trap:</strong> Given $U(x,y) = x^2 y$, finding the force component as $F_x = -\int U dx$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Force is the negative spatial derivative (gradient): $\mathbf{F} = -\nabla U = -\left(\frac{\partial U}{\partial x}\hat{i} + \frac{\partial U}{\partial y}\hat{j}\right) = -2xy\hat{i} - x^2\hat{j}$. Never integrate a potential function to find force.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.8] Forgetting Pseudo-Work in Accelerating Frames</div>
        <p><strong>The Trap:</strong> Applying the work-energy theorem in an accelerating frame without accounting for the work done by pseudo-forces.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> In an accelerating frame $S'$ with acceleration $\mathbf{a}_0$, you must include the work done by the pseudo-force: $W_{real} + W_{pseudo} = \Delta K'$, where $W_{pseudo} = \int (-m\mathbf{a}_0) \cdot d\mathbf{r}'$.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.9] Constant Power Engine Velocity Singularity at Launch</div>
        <p><strong>The Trap:</strong> Integrating $P = Fv \implies v = (3Pt/m)^{1/3}$ to calculate launch time from rest, ignoring that at $t = 0$, force would be infinite ($F = P/0$).</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> In real vehicles, force is limited by tire friction: $F_{\max} = \mu mg$. The vehicle accelerates at constant acceleration $a = \mu g$ until it reaches critical transition speed $v_c = P/(\mu mg)$, and only then transitions to constant power mode!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 3.10] Internal Conservative Forces Doing Non-Zero Work</div>
        <p><strong>The Trap:</strong> Claiming internal forces do zero work in every system because Newton's Third Law says $\sum \mathbf{F}_{int} = 0$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> $\sum \mathbf{F}_{int} = 0$ guarantees momentum conservation, NOT zero work! Internal forces do work whenever the relative distance between interacting particles changes: $W_{int} = -\Delta U_{internal}$. Only in a strictly rigid body is total internal work identically zero.</div>
      </div>

      <h2 class="section-title">3.4 Dissected JEE Advanced Previous Year Questions (PYQs)</h2>

      <!-- PYQ 3.1 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2017 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Hard • Vertical Circular Motion Slackening & Trajectory</span>
        </div>
        <div class="pyq-question">
          A light inextensible string of length $R = 1\text{ m}$ is attached to a bob of mass $m = 0.5\text{ kg}$. The bob is projected horizontally from the lowest point with speed $u = \sqrt{3gR}$. Determine (a) the angle $\theta_0$ from the downward vertical at which the string goes slack, (b) the speed $v_0$ at the slackening instant, and (c) the maximum height reached by the bob above the lowest point. Take $g = 10\text{ m/s}^2$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Condition for String Slackening ($T = 0$):</strong></p>
          <p>Write tension as a function of angle $\theta$ from the downward vertical:</p>
          $$T(\theta) = \frac{m}{R}\left[u^2 - gR(2 - 3\cos\theta)\right] = 0$$
          $$3gR - 2gR + 3gR\cos\theta_0 = 0 \implies gR(1 + 3\cos\theta_0) = 0 \implies \cos\theta_0 = -\frac{1}{3}$$
          $$\theta_0 = \arccos(-1/3) \approx 109.47^\circ \quad (\text{string slacks in upper semicircle})$$
          <p><strong>Step 2: Speed at Slackening Instant:</strong></p>
          $$v_0^2 = u^2 - 2gR(1 - \cos\theta_0) = 3gR - 2gR\left(1 - \left(-\frac{1}{3}\right)\right) = 3gR - 2gR\left(\frac{4}{3}\right) = \frac{gR}{3}$$
          $$v_0 = \sqrt{\frac{10 \times 1}{3}} = \sqrt{\frac{10}{3}}\text{ m/s} \approx 1.826\text{ m/s}$$
          <p><em>Self-Check Verification:</em> At $T=0$, gravity component must provide centripetal force: $mg|\cos\theta_0| = \frac{mv_0^2}{R} \implies mg(1/3) = \frac{mv_0^2}{R} \implies v_0^2 = \frac{gR}{3}$. Flawless consistency!</p>
          <p><strong>Step 3: Maximum Height Reached Above Lowest Point:</strong></p>
          <p>Height at slackening point above the bottom: $h_0 = R(1 - \cos\theta_0) = R\left(1 - (-1/3)\right) = \frac{4}{3}R = \frac{4}{3}\text{ m}$.</p>
          <p>At slackening, velocity is tangential to the circle, inclined at angle $\phi = \theta_0 - 90^\circ$ above the horizontal. Therefore, $\sin\phi = \cos(\theta_0 - 90^\circ) = -\cos\theta_0 = \frac{1}{3}$.</p>
          <p>Additional projectile height attained from slackening point:</p>
          $$\Delta h = \frac{v_{0y}^2}{2g} = \frac{(v_0\sin\phi)^2}{2g} = \frac{(gR/3)(1/9)}{2g} = \frac{R}{54} = \frac{1}{54}\text{ m}$$
          $$H_{\max} = h_0 + \Delta h = \frac{4}{3} + \frac{1}{54} = \frac{72 + 1}{54} = \mathbf{\frac{73}{54}\text{ m}} \approx 1.352\text{ m}$$
        </div>
      </div>

      <!-- PYQ 3.2 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2014 • Paper 2</span>
          <span class="pyq-difficulty">Difficulty: Moderate • Potential Well Equilibrium & Oscillation</span>
        </div>
        <div class="pyq-question">
          A particle of mass $m = 0.2\text{ kg}$ moves along the $x$-axis in a conservative potential field given by $U(x) = \frac{a}{x^2} - \frac{b}{x}$, where $a = 2\text{ J}\cdot\text{m}^2$ and $b = 4\text{ J}\cdot\text{m}$. Find (a) the equilibrium position $x_0$, (b) the nature of equilibrium, (c) the minimum binding energy to escape to infinity, and (d) the time period of small oscillations about $x_0$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Locate Equilibrium Position ($dU/dx = 0$):</strong></p>
          $$\frac{dU}{dx} = -\frac{2a}{x^3} + \frac{b}{x^2} = 0 \implies \frac{b}{x^2} = \frac{2a}{x^3} \implies x_0 = \frac{2a}{b} = \frac{2(2)}{4} = \mathbf{1\text{ m}}$$
          <p><strong>Step 2: Second Derivative Test for Stability:</strong></p>
          $$\frac{d^2U}{dx^2} = \frac{6a}{x^4} - \frac{2b}{x^3}$$
          $$\left.\frac{d^2U}{dx^2}\right|_{x=1} = \frac{6(2)}{1^4} - \frac{2(4)}{1^3} = 12 - 8 = +4\text{ N/m} > 0 \implies \mathbf{\text{Stable Equilibrium}}$$
          <p><strong>Step 3: Minimum Potential & Binding Energy:</strong></p>
          $$U(x_0) = \frac{2}{1^2} - \frac{4}{1} = 2 - 4 = -2\text{ J}$$
          <p>As $x \to \infty$, $U(\infty) = 0$. The binding energy to overcome the well and reach infinity is $E_{bind} = |U(x_0)| = \mathbf{2\text{ J}}$.</p>
          <p><strong>Step 4: Small Oscillation Time Period:</strong></p>
          $$k_{eff} = U''(x_0) = 4\text{ N/m}$$
          $$\omega = \sqrt{\frac{k_{eff}}{m}} = \sqrt{\frac{4}{0.2}} = \sqrt{20} = 2\sqrt{5}\text{ rad/s}$$
          $$T = \frac{2\pi}{\omega} = \frac{2\pi}{2\sqrt{5}} = \mathbf{\frac{\pi}{\sqrt{5}}\text{ s}} \approx 1.405\text{ seconds}$$
        </div>
      </div>

      <!-- PYQ 3.3 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2019 • Paper 2</span>
          <span class="pyq-difficulty">Difficulty: Hard • Work Done by Moving Incline Boundary</span>
        </div>
        <div class="pyq-question">
          A wedge of mass $M = 2\text{ kg}$ with smooth inclined face of angle $\alpha = 30^\circ$ sits on a smooth horizontal floor. A block of mass $m = 1\text{ kg}$ is released from rest at height $h = 1\text{ m}$ on the incline. Find the work done by the normal contact force on (a) the block and (b) the wedge during the descent to the floor. Take $g = 10\text{ m/s}^2$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Mechanical Energy & Momentum Conservation:</strong></p>
          <p>Friction is zero everywhere, so total mechanical energy is conserved: $\Delta K_{block} + \Delta K_{wedge} = mgh = 1 \times 10 \times 1 = 10\text{ J}$.</p>
          <p>Horizontal momentum is conserved: $m v_{bx} + M V_{wx} = 0 \implies v_{bx} = -\frac{M}{m}V_w = -2V_w$.</p>
          <p>Kinematic constraint along incline: relative velocity gives $v_{by} = (v_{bx} - V_w)\tan 30^\circ = -3V_w / \sqrt{3} = -\sqrt{3}V_w$.</p>
          <p><strong>Step 2: Solve Kinetic Energies:</strong></p>
          $$K_{wedge} = \frac{1}{2}M V_w^2 = \frac{1}{2}(2)V_w^2 = V_w^2$$
          $$K_{block} = \frac{1}{2}m(v_{bx}^2 + v_{by}^2) = \frac{1}{2}(1)[(-2V_w)^2 + (-\sqrt{3}V_w)^2] = \frac{1}{2}(4 + 3)V_w^2 = 3.5 V_w^2$$
          $$K_{wedge} + K_{block} = 10\text{ J} \implies 4.5 V_w^2 = 10 \implies V_w^2 = \frac{20}{9}$$
          $$K_{wedge} = \frac{20}{9}\text{ J} \approx 2.22\text{ J}, \quad K_{block} = 3.5\left(\frac{20}{9}\right) = \frac{70}{9}\text{ J} \approx 7.78\text{ J}$$
          <p><strong>Step 3: Work Done by Normal Force:</strong></p>
          <p>For the wedge: Normal force from the block is the <em>sole</em> agent doing work:</p>
          $$W_{N, \text{on wedge}} = \Delta K_{wedge} = \mathbf{+\frac{20}{9}\text{ J}} \approx +2.22\text{ J}$$
          <p>For the block: Gravity and normal force both act: $W_g + W_{N, \text{on block}} = \Delta K_{block}$</p>
          $$10 + W_{N, \text{on block}} = \frac{70}{9} \implies W_{N, \text{on block}} = \frac{70}{9} - 10 = \mathbf{-\frac{20}{9}\text{ J}} \approx -2.22\text{ J}$$
          <p><em>Fundamental Law Confirmed:</em> $W_{N,\text{wedge}} + W_{N,\text{block}} = +\frac{20}{9} - \frac{20}{9} \equiv 0\text{ J}$. Normal contact forces between rigid bodies transfer mechanical energy across boundaries with zero net destruction!</p>
        </div>
      </div>

      <h2 class="section-title">3.5 High-Caliber Practice Challenge Problems & Complete Solutions</h2>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 3.1] Non-Linear Spring Oscillator Escape Velocity</div>
        <p>A non-linear restoring force is given by $F(x) = -kx + \beta x^3$ where $k = 100\text{ N/m}$ and $\beta = 10\text{ N/m}^3$. A mass $m = 1\text{ kg}$ is initially at the origin $x = 0$. Determine (a) the escape displacement $x_{esc}$ where the force turns repulsive, and (b) the minimum launch velocity $v_{esc}$ required for the mass to escape to infinity.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p><strong>Step 1: Potential Energy Function:</strong></p>
            $$U(x) = -\int_0^x F(x')dx' = \int_0^x (kx' - \beta x'^3)dx' = \frac{1}{2}kx^2 - \frac{1}{4}\beta x^4$$
            <p>Force vanishes at the peak of the potential barrier: $F(x_{esc}) = -k x_{esc} + \beta x_{esc}^3 = 0 \implies x_{esc} = \sqrt{k/\beta} = \sqrt{100/10} = \sqrt{10}\text{ m}$.</p>
            <p><strong>Step 2: Potential Energy Barrier Height:</strong></p>
            $$U(x_{esc}) = \frac{1}{2}(100)(10) - \frac{1}{4}(10)(10^2) = 500 - 250 = 250\text{ J}$$
            <p>By energy conservation, minimum launch kinetic energy at origin must match the barrier crest:</p>
            $$\frac{1}{2}m v_{esc}^2 = U(x_{esc}) \implies \frac{1}{2}(1)v_{esc}^2 = 250 \implies v_{esc} = \mathbf{10\sqrt{5}\text{ m/s}} \approx 22.36\text{ m/s}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 3.2] 50% Thermal Dissipation on Conveyor Belt</div>
        <p>Sand falls vertically at a constant rate $\frac{dm}{dt} = \mu = 2\text{ kg/s}$ onto a horizontal conveyor belt moving at constant speed $v = 3\text{ m/s}$. Determine (a) the extra mechanical power required from the motor to maintain speed $v$, and (b) the rate of thermal heat dissipation at the friction boundary.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p><strong>Step 1: Force and Power Required from Motor:</strong></p>
            <p>In time $dt$, mass $dm = \mu dt$ must be accelerated from horizontal speed $0$ to $v$. The horizontal force required on the belt is:</p>
            $$F_{ext} = v\frac{dm}{dt} = \mu v = (2)(3) = 6\text{ N}$$
            <p>Mechanical power delivered by the motor:</p>
            $$P_{motor} = F_{ext} v = \mu v^2 = (2)(3^2) = \mathbf{18\text{ Watts}}$$
            <p><strong>Step 2: Rate of Kinetic Energy Gain:</strong></p>
            $$\frac{dK}{dt} = \frac{1}{2}\frac{dm}{dt}v^2 = \frac{1}{2}\mu v^2 = \frac{1}{2}(18) = 9\text{ Watts}$$
            <p><strong>Step 3: Rate of Thermal Dissipation:</strong></p>
            $$P_{heat} = P_{motor} - \frac{dK}{dt} = \mu v^2 - \frac{1}{2}\mu v^2 = \frac{1}{2}\mu v^2 = \mathbf{9\text{ Watts}}$$
            <p><strong>Mentor Takeaway:</strong> Notice this universal truth: Exactly $50\%$ of motor work becomes kinetic energy, and exactly $50\%$ is dissipated as thermal friction heat, completely independent of the friction coefficient $\mu$!</p>
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 3.3] Inverted Hemispherical Bowl Contact Separation</div>
        <p>A small particle of mass $m$ is placed atop a smooth fixed solid hemisphere of radius $R = 2\text{ m}$. Upon a slight disturbance, the particle slides down the surface. Find the angle $\theta_{sep}$ from the upward vertical and height $h_{sep}$ at which the particle loses contact with the hemisphere. Take $g = 10\text{ m/s}^2$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Let $\theta$ be the angle from the upward vertical. By mechanical energy conservation from the summit:</p>
            $$mgR = mgR\cos\theta + \frac{1}{2}mv^2 \implies v^2 = 2gR(1 - \cos\theta)$$
            <p>Radial equation of motion toward the center:</p>
            $$mg\cos\theta - N = \frac{mv^2}{R} \implies N = mg\cos\theta - \frac{m}{R}[2gR(1 - \cos\theta)] = mg(3\cos\theta - 2)$$
            <p>Separation occurs when normal contact force vanishes ($N = 0$):</p>
            $$3\cos\theta_{sep} - 2 = 0 \implies \cos\theta_{sep} = \frac{2}{3} \implies \mathbf{\theta_{sep} = \arccos(2/3)} \approx 48.19^\circ$$
            $$h_{sep} = R\cos\theta_{sep} = 2\left(\frac{2}{3}\right) = \mathbf{\frac{4}{3}\text{ m}} \approx 1.33\text{ m above center}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 3.4] Variable Mass Rocket Burnout Velocity</div>
        <p>A single-stage sounding rocket has initial wet mass $M_0 = 1000\text{ kg}$, exhaust velocity $u_{ex} = 2000\text{ m/s}$ relative to the rocket, and fuel consumption rate $\alpha = 20\text{ kg/s}$. Gravity $g = 10\text{ m/s}^2$ acts uniformly downward, and atmospheric drag is negligible. If fuel comprises $800\text{ kg}$ of the mass, calculate the burnout velocity $v_b$ when all fuel is consumed.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Dry mass at burnout: $M_b = M_0 - 800 = 200\text{ kg}$. Burn duration: $t_b = \frac{800}{20} = 40\text{ s}$.</p>
            <p>Tsiolkovsky Rocket Equation under uniform gravity:</p>
            $$v_b = u_{ex}\ln\left(\frac{M_0}{M_b}\right) - g t_b$$
            $$v_b = 2000\ln\left(\frac{1000}{200}\right) - (10)(40) = 2000\ln(5) - 400$$
            <p>Since $\ln(5) \approx 1.6094$:</p>
            $$v_b = 2000(1.6094) - 400 = 3218.8 - 400 = \mathbf{2818.8\text{ m/s}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 3.5] Power-Limited Vehicle Distance Traverse</div>
        <p>A vehicle of mass $m = 1000\text{ kg}$ is powered by an engine delivering constant rated power $P = 30\text{ kW}$. Neglecting friction and drag, find the distance $x$ traversed by the vehicle as its speed increases from $v_1 = 10\text{ m/s}$ to $v_2 = 20\text{ m/s}$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Instantaneous power formulation:</p>
            $$P = F v = m v \frac{dv}{dt} = m v^2 \frac{dv}{dx} \implies dx = \frac{m}{P} v^2 dv$$
            <p>Integrate directly between the two velocity states:</p>
            $$x = \frac{m}{P} \int_{v_1}^{v_2} v^2 dv = \frac{m}{P}\left[\frac{v_2^3 - v_1^3}{3}\right]$$
            $$x = \frac{1000}{30,000}\left[\frac{20^3 - 10^3}{3}\right] = \frac{1}{30}\left[\frac{8000 - 1000}{3}\right] = \frac{7000}{90} = \mathbf{\frac{700}{9}\text{ m}} \approx 77.78\text{ m}$$
          </div>
        </details>
      </div>
    </section>
    """

if __name__ == "__main__":
    content = get_ch3_content()
    print("Chapter 3 content generated successfully. Length:", len(content))
