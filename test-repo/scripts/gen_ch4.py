# Chapter 4 Generator: Center of Mass, Linear Momentum & Collisions
# Conversational Kota Mentor Voice • Zero Emojis • Modern Typography

def get_ch4_content():
    return r"""
    <section id="ch4" class="chapter-container">
      <span class="chapter-number">Chapter 04</span>
      <h1 class="chapter-title">Center of Mass, Linear Momentum & Collisions</h1>

      <div class="card-box tip-card">
        <div class="card-header-tip">[MENTOR STRATEGY NOTE] The Mindset Shift: From Particles to Systems</div>
        <p><strong>Listen up, future IITians:</strong> Up until now, you've treated every object as a point mass. That luxury ends today. In the real world, bodies have shape, internal structure, and colliding boundaries. Center of mass (COM) is the single most powerful simplifying concept in mechanics—it is the point that moves as if the entire system's mass were concentrated there and all external forces were applied directly to it.</p>
        <p><strong>Where students lose marks in JEE Advanced:</strong> They apply the coefficient of restitution $e$ along the direction of motion instead of the normal Line of Impact (LOI). They forget that fixed hinges destroy linear momentum through massive impulsive reactions. And they butcher the relative velocity signs in variable-mass rocket equations. We are going to lock down every single one of these concepts right now.</p>
      </div>

      <h2 class="section-title">4.1 First-Principles Foundations: Mass Distributions & Collision Dynamics</h2>
      
      <h3 class="sub-title">4.1.1 Continuous Mass Formulations & Standard Integrals</h3>
      <p>Think of the Center of Mass (COM) as the single balance point of the body. If you supported the object on the tip of a pin right at this point, it wouldn't tip in any direction. Mathematically, it is the weighted average position of all the mass in the system:</p>
      $$\mathbf{r}_{cm} = \frac{\sum m_i \mathbf{r}_i}{\sum m_i} = \frac{1}{M} \int \mathbf{r} \, dm$$
      <p>To save critical exam minutes, memorize these six standard geometries and how their centroids are derived:</p>
      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Uniform Semicircular Thin Wire (Radius $R$):</strong> Take polar element $dm = \lambda R d\theta$, height $y = R\sin\theta$.
        $$y_{cm} = \frac{\int_0^\pi (R\sin\theta)(\lambda R d\theta)}{\int_0^\pi \lambda R d\theta} = \frac{R\int_0^\pi \sin\theta d\theta}{\pi} = \mathbf{\frac{2R}{\pi}} \approx 0.637 R$$</li>
        <li><strong>Uniform Semicircular Planar Disc (Radius $R$):</strong> Slice into concentric semicircular strips of radius $r$, area $dA = \pi r dr$, strip centroid at $2r/\pi$.
        $$y_{cm} = \frac{\int_0^R \left(\frac{2r}{\pi}\right)(\sigma \pi r dr)}{\frac{1}{2}\sigma \pi R^2} = \frac{2\int_0^R r^2 dr}{\frac{1}{2}\pi R^2} = \mathbf{\frac{4R}{3\pi}} \approx 0.424 R$$</li>
        <li><strong>Uniform Thin Hemispherical Shell (Radius $R$):</strong> Slice into rings at polar angle $\theta$, radius $R\sin\theta$, height $y = R\cos\theta$, area $dA = 2\pi R^2 \sin\theta d\theta$.
        $$y_{cm} = \frac{\int_0^{\pi/2} (R\cos\theta)(2\pi R^2 \sigma \sin\theta d\theta)}{2\pi R^2 \sigma} = R\int_0^{\pi/2} \sin\theta\cos\theta d\theta = \mathbf{\frac{R}{2}} = 0.500 R$$</li>
        <li><strong>Uniform Solid Hemisphere (Radius $R$):</strong> Sliced into flat discs at height $z \in [0, R]$ with radius $\sqrt{R^2 - z^2}$, mass $dm = \rho \pi (R^2 - z^2) dz$.
        $$z_{cm} = \frac{\int_0^R z \pi (R^2 - z^2) dz}{\frac{2}{3}\pi R^3} = \frac{\pi \left[ \frac{R^2 z^2}{2} - \frac{z^4}{4} \right]_0^R}{\frac{2}{3}\pi R^3} = \frac{\frac{1}{4}\pi R^4}{\frac{2}{3}\pi R^3} = \mathbf{\frac{3R}{8}} = 0.375 R$$</li>
        <li><strong>Uniform Hollow Cone (Height $h$):</strong> Sliced into elemental rings along the slant face: $y_{cm} = \mathbf{\frac{h}{3}}$ from the base.</li>
        <li><strong>Uniform Solid Cone (Height $h$):</strong> Sliced into circular discs along the vertical symmetry axis: $y_{cm} = \mathbf{\frac{h}{4}}$ from the base.</li>
      </ul>

      <!-- SVG Diagram 4.1: Oblique Collision Geometry -->
      <div class="diagram-container">
                <svg class="diagram-svg" width="600" height="260" viewBox="0 0 600 260">
          <defs>
            <marker id="arrow-ch4" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626"/>
            </marker>
          </defs>
          <!-- Background guidelines -->
          <line x1="50" y1="130" x2="550" y2="130" stroke="#b45309" stroke-width="2" stroke-dasharray="6,4" />
          <text x="450" y="120" font-family="sans-serif" font-size="12" fill="#b45309" font-weight="bold">Line of Impact (LOI)</text>
          <line x1="300" y1="20" x2="300" y2="240" stroke="#047857" stroke-width="2" stroke-dasharray="6,4" />
          <text x="310" y="40" font-family="sans-serif" font-size="12" fill="#047857" font-weight="bold">Common Tangent (COT)</text>
          
          <!-- Sphere 1 (Left) -->
          <circle cx="230" cy="130" r="60" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5" />
          <circle cx="230" cy="130" r="4" fill="#0f172a" />
          <text x="215" y="135" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a">m₁</text>

          <!-- Sphere 2 (Right) -->
          <circle cx="360" cy="130" r="60" fill="#f1f5f9" stroke="#0f172a" stroke-width="2.5" />
          <circle cx="360" cy="130" r="4" fill="#0f172a" />
          <text x="350" y="135" font-family="sans-serif" font-size="14" font-weight="bold" fill="#0f172a">m₂</text>

          <!-- Contact Point -->
          <circle cx="295" cy="130" r="5" fill="#dc2626" />
          
          <!-- Velocity Vector 1 -->
          <line x1="160" y1="70" x2="220" y2="120" stroke="#dc2626" stroke-width="3" marker-end="url(#arrow-ch4)" />
          <text x="140" y="65" font-family="sans-serif" font-size="13" font-weight="bold" fill="#dc2626">u₁ (approach)</text>
          
          <!-- Velocity Vector 2 -->
          <line x1="430" y1="80" x2="370" y2="120" stroke="#0284c7" stroke-width="3" />
          <text x="420" y="75" font-family="sans-serif" font-size="13" font-weight="bold" fill="#0284c7">u₂</text>

          <!-- Impulsive Forces -->
          <line x1="285" y1="130" x2="245" y2="130" stroke="#dc2626" stroke-width="3.5" />
          <text x="250" y="150" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">-J_imp</text>
          <line x1="305" y1="130" x2="345" y2="130" stroke="#0284c7" stroke-width="3.5" />
          <text x="315" y="150" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0284c7">+J_imp</text>

          <!-- Notation Notes -->
          <rect x="30" y="195" width="240" height="55" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
          <text x="40" y="215" font-family="sans-serif" font-size="11" fill="#334155">Along COT: v_1t = u_1t, v_2t = u_2t</text>
          <text x="40" y="235" font-family="sans-serif" font-size="11" fill="#b91c1c">Along LOI: e = (v_2n - v_1n)/(u_1n - u_2n)</text>
        </svg>
        <div class="diagram-caption">Figure 4.1: Oblique collision resolution along the Line of Impact (LOI) and Common Tangent (COT). Normal impulses act exclusively along LOI.</div>
      </div>

      <h3 class="sub-title">4.1.2 Center of Mass Frame (C-Frame) & Koenig's Kinetic Energy Theorem</h3>
      <p>The Center of Mass reference frame (zero-momentum frame) translates at velocity $\mathbf{V}_{cm} = \frac{\sum m_i \mathbf{v}_i}{\sum m_i}$. In this frame, the net linear momentum vanishes identically by definition:</p>
      $$\mathbf{P}_{cm}^{C\text{-frame}} = \sum m_i \mathbf{v}_i^* = \sum m_i (\mathbf{v}_i - \mathbf{V}_{cm}) = \mathbf{P}_{lab} - M \mathbf{V}_{cm} \equiv \mathbf{0}$$
      <p><strong>Koenig's Kinetic Energy Decomposition Theorem:</strong> The total kinetic energy in the laboratory frame decouples cleanly into the kinetic energy of the center of mass plus the internal kinetic energy relative to the center of mass:</p>
      $$K_{lab} = \frac{1}{2} M V_{cm}^2 + \sum \frac{1}{2} m_i (v_i^*)^2 = K_{cm} + K_{rel}$$
      <p>For any two-body system ($m_1, m_2$), introducing the <strong>reduced mass</strong> $\mu = \frac{m_1 m_2}{m_1 + m_2}$ collapses the relative kinetic energy to that of a single virtual particle:</p>
      $$K_{rel} = \frac{1}{2} \mu v_{rel}^2 \quad \text{where } \mathbf{v}_{rel} = \mathbf{v}_1 - \mathbf{v}_2$$
      <p>When two colliding bodies coalesce or couple through a spring, maximum deformation occurs when relative velocity vanishes ($\mathbf{v}_{rel} = \mathbf{0}$). The kinetic energy converted to deformation or spring potential energy is exactly:</p>
      $$\Delta E_{\max} = K_{rel} = \frac{1}{2} \mu u_{rel}^2 = \frac{1}{2} \frac{m_1 m_2}{m_1 + m_2} (u_1 - u_2)^2$$

      <h3 class="sub-title">4.1.3 Oblique Collisions & Newton's Law of Restitution</h3>
      <p>During an impact of finite microsecond duration $\Delta t \to 0$, normal forces generate massive internal impulses $J = \int N dt \gg mg\Delta t$. Newton's experimental law of restitution governs the normal components of approach and separation along the <strong>Line of Impact (LOI)</strong>:</p>
      $$e = \frac{v_{2n} - v_{1n}}{u_{1n} - u_{2n}} = \frac{\text{Relative Speed of Separation along LOI}}{\text{Relative Speed of Approach along LOI}}$$
      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Perfectly Elastic Collision ($e = 1$):</strong> Zero mechanical energy loss. Relative separation speed equals relative approach speed.</li>
        <li><strong>Inelastic Collision ($0 < e < 1$):</strong> Fractional loss of relative normal kinetic energy:
        $$\Delta K_{loss} = \frac{1}{2} \frac{m_1 m_2}{m_1 + m_2} (1 - e^2) (u_{1n} - u_{2n})^2$$</li>
        <li><strong>Perfectly Inelastic Collision ($e = 0$):</strong> Bodies attain identical velocity components along LOI ($v_{1n} = v_{2n}$). Maximum possible mechanical energy is converted to thermal and deformation energy.</li>
        <li><strong>Tangential Component Conservation:</strong> For smooth surfaces ($\mu = 0$), impulsive friction is zero ($J_t = 0$). Consequently, velocity components parallel to the Common Tangential Plane (COT) are strictly conserved:
        $$v_{1t} = u_{1t}, \quad v_{2t} = u_{2t}$$</li>
      </ul>

      <h3 class="sub-title">4.1.4 Variable Mass Dynamics: Rocketry & Control Volume Mechanics</h3>
      <p>For an open system with mass entering or exiting at rate $\frac{dm}{dt}$ with velocity $\mathbf{v}_{in/out}$ relative to an inertial frame, Newton's second law applied to an instantaneous control volume yields the <strong>Meshchersky Equation</strong>:</p>
      $$\mathbf{F}_{ext} + \mathbf{v}_{rel} \frac{dm}{dt} = m \frac{d\mathbf{v}}{dt}$$
      <p>where $\mathbf{v}_{rel} = \mathbf{v}_{exhaust} - \mathbf{v}_{body}$ is the relative velocity of the entering or ejected mass. The term $\mathbf{F}_{thrust} = \mathbf{v}_{rel} \frac{dm}{dt}$ represents the effective <strong>thrust force</strong>.</p>
      <p>For a vertical rocket ejecting mass backward at constant relative speed $u_{ex} = |\mathbf{v}_{rel}|$ in uniform gravity $g$:</p>
      $$-mg - u_{ex} \left(-\frac{dm}{dt}\right) = m \frac{dv}{dt} \implies dv = -u_{ex} \frac{dm}{m} - g dt$$
      <p>Integrating from initial mass $M_0$ to current mass $m(t)$ yields the celebrated <strong>Tsiolkovsky Rocket Equation</strong>:</p>
      $$v(t) = v_0 + u_{ex} \ln\left(\frac{M_0}{m(t)}\right) - g t$$

      <h3 class="sub-title">4.1.5 Continuous Momentum Transfer: The Falling Chain 3x Theorem</h3>
      <p>A classic signature problem in JEE Advanced concerns a heavy flexible chain of linear mass density $\lambda = M/L$ held vertically above a scale platform and released from rest. When a length $x$ has collapsed onto the scale, what does the scale read?</p>
      <p>Most students calculate the static weight of the accumulated links: $W_{stat} = (\lambda x)g$. But the scale does NOT read $\lambda g x$—it reads <strong>three times that value: $3\lambda g x$!</strong> Why?</p>
      <p>Because falling links strike the pan with velocity $v = \sqrt{2gx}$ and come to an instantaneous stop. To destroy their downward momentum, the scale must deliver a continuous upward impulse. By Newton's Second Law applied to the control volume of the scale platform:</p>
      $$F_{scale} = N_{static} + F_{impulsive}$$
      <p>The static weight of the coiled chain resting on the scale is simply:</p>
      $$N_{static} = (\lambda x)g$$
      <p>The rate at which mass enters the scale boundary is $\frac{dm}{dt} = \lambda v$. To bring this influx from speed $v$ to zero requires an impulsive thrust force:</p>
      $$F_{impulsive} = v \frac{dm}{dt} = v (\lambda v) = \lambda v^2 = \lambda(2gx) = 2\lambda g x$$
      <p>Summing both contributions yields the celebrated <strong>3x Factor Theorem</strong>:</p>
      $$F_{scale} = \lambda g x + 2\lambda g x = \mathbf{3\lambda g x}$$
      <p>The scale reading is triple the weight of the fallen chain! At the instant the last link touches the pan ($x = L$), the scale registers $3Mg$. The moment the entire chain settles into static equilibrium, the impulsive term drops to zero and the reading falls discontinuously to $Mg$.</p>

      <h2 class="section-title">4.2 Master Formula Summary Table: Center of Mass & Momentum</h2>
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
              <td><strong>Center of Mass Coordinate</strong></td>
              <td class="formula-math">$$\mathbf{R}_{cm} = \frac{\int \mathbf{r} dm}{\int dm} = \frac{\sum m_i \mathbf{r}_i}{\sum m_i}$$</td>
              <td><span class="validity-tag">All classical discrete and continuous bodies</span></td>
              <td><span class="invalidity-tag">Confusing COM with center of gravity in non-uniform gravitational fields</span></td>
            </tr>
            <tr>
              <td><strong>Koenig's Kinetic Energy Theorem</strong></td>
              <td class="formula-math">$$K = \frac{1}{2}M V_{cm}^2 + \frac{1}{2}\mu v_{rel}^2$$</td>
              <td><span class="validity-tag">Two-body interacting system in any inertial frame</span></td>
              <td><span class="invalidity-tag">Applying reduced mass $\mu$ to three or more interacting bodies</span></td>
            </tr>
            <tr>
              <td><strong>Restitution Law (LOI)</strong></td>
              <td class="formula-math">$$e = \frac{(\mathbf{v}_2 - \mathbf{v}_1)\cdot\hat{\mathbf{n}}}{(\mathbf{u}_1 - \mathbf{u}_2)\cdot\hat{\mathbf{n}}}$$</td>
              <td><span class="validity-tag">Collinear or oblique impact along normal $\hat{\mathbf{n}}$</span></td>
              <td><span class="invalidity-tag">Applying $e$ directly to full velocity magnitudes instead of normal components</span></td>
            </tr>
            <tr>
              <td><strong>Collision Kinetic Energy Loss</strong></td>
              <td class="formula-math">$$\Delta K = \frac{1}{2}\mu (1 - e^2) u_{rel, n}^2$$</td>
              <td><span class="validity-tag">Frictionless oblique or 1D collisions</span></td>
              <td><span class="invalidity-tag">Including tangential relative velocity in $\Delta K$ calculation</span></td>
            </tr>
            <tr>
              <td><strong>Impulsive Reaction Dominance</strong></td>
              <td class="formula-math">$$\lim_{\Delta t \to 0} \int_0^{\Delta t} \mathbf{F}_{imp} dt = \Delta \mathbf{P}, \quad \int_0^{\Delta t} mg dt \approx 0$$</td>
              <td><span class="validity-tag">Short duration collision impacts ($\Delta t \approx 10^{-3}\text{ s}$)</span></td>
              <td><span class="invalidity-tag">Conserving momentum along axes with non-negligible impulsive external constraints</span></td>
            </tr>
            <tr>
              <td><strong>Rocket Burnout Speed</strong></td>
              <td class="formula-math">$$v_b = u_{ex}\ln\left(\frac{M_0}{M_b}\right) - gt_b$$</td>
              <td><span class="validity-tag">Vertical ascent, constant exhaust speed, uniform $g$</span></td>
              <td><span class="invalidity-tag">Assuming burnout speed occurs at peak apogee rather than engine cutoff</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">4.3 10 Forensic NTA/JEE Negative-Marking Trap Alerts</h2>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.1] The Line of Impact (LOI) Projection Blunder</div>
        <p><strong>The Trap:</strong> In oblique collisions, setting $e = \frac{v_2 - v_1}{u_1 - u_2}$ using overall velocity magnitudes or laboratory axes rather than the contact normal.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Restitution applies <strong>strictly and exclusively</strong> along the Line of Impact (the common normal at the contact point): $e = \frac{v_{2n} - v_{1n}}{u_{1n} - u_{2n}}$. Velocity components tangential to the contact plane remain completely unaffected: $v_{1t} = u_{1t}$ and $v_{2t} = u_{2t}$.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.2] The "COM Divides Area/Mass Equally" Fallacy</div>
        <p><strong>The Trap:</strong> Assuming that a plane or axis passing through the center of mass bisects the body into two halves of equal mass or area.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Center of mass balances first moments of mass ($\int x dm = 0$), NOT zeroth moments ($\int dm$). For a triangle of height $h$, $y_{cm} = h/3$ from the base. A horizontal cut through the COM divides the triangle into areas in the ratio $4:5$, not $1:1$!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.3] Man Walking on a Movable Boat / Wedge Shift</div>
        <p><strong>The Trap:</strong> When a person of mass $m$ walks a distance $L$ from one end of a boat of mass $M$ to the other, students calculate boat displacement as $\Delta x = \frac{m}{M}L$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> The distance $L$ is measured <em>relative to the boat</em>. Since net external horizontal force is zero, $\Delta X_{cm} = 0 \implies m(L - \Delta x_{boat}) - M\Delta x_{boat} = 0 \implies \Delta x_{boat} = \mathbf{\frac{m}{M + m}L}$. The denominator is ALWAYS the total system mass $(M+m)$!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.4] The Leaking Freight Car Paradox</div>
        <p><strong>The Trap:</strong> Water leaks vertically through a hole in the bottom of a freight car rolling frictionlessly at speed $v$. Students claim the cart accelerates because its mass decreases.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Water leaves with horizontal velocity equal to the cart ($v_{leak, x} = v$). Therefore, $v_{rel, x} = 0$, meaning the leaking water exerts <strong>zero horizontal thrust</strong> on the cart: $F_{thrust} = v_{rel,x}\frac{dm}{dt} = 0$. The cart's velocity remains strictly <strong>constant</strong>! (Conversely, if rain falls vertically into the cart, $v_{rel, x} = -v$, so the cart slows down).</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.5] Momentum Conservation Across Hinges & Pins</div>
        <p><strong>The Trap:</strong> Conserving linear momentum of a rod-bullet system when the rod is pivoted on a fixed hinge.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Fixed hinges exert massive <strong>impulsive reaction forces</strong> during collision ($\int \mathbf{N}_{hinge} dt \ne \mathbf{0}$). Linear momentum of the rod-bullet system is NOT conserved. You MUST conserve <strong>angular momentum about the hinge axis</strong>, where external reaction torque is identically zero ($\boldsymbol{\tau}_{hinge} = \mathbf{0}$).</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.6] Completely Inelastic Collision Does NOT Mean Zero Final Kinetic Energy</div>
        <p><strong>The Trap:</strong> Equating $e = 0$ (perfectly inelastic) to $\Delta K = K_{initial}$, leaving zero final kinetic energy.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> In an isolated system, linear momentum must be conserved. Therefore, $K_{final} = \frac{P_{total}^2}{2(m_1 + m_2)} > 0$ unless initial total momentum was already zero in the lab frame! Exactly the relative kinetic energy $K_{rel} = \frac{1}{2}\mu u_{rel}^2$ is dissipated; $K_{cm} = \frac{P^2}{2M_{tot}}$ is indestructible.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.7] Impulsive Friction Thresholding During Impact</div>
        <p><strong>The Trap:</strong> Applying Coulomb's static friction condition $f \le \mu N$ using normal force $N = mg$ during collision impacts.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> During impact, normal reaction is impulsive: $N_{imp} \approx \frac{\Delta p}{\Delta t} \gg mg$. The friction impulse is $J_f = \int f dt \le \mu \int N dt = \mu J_N$. Gravitational contribution is utterly negligible during the microsecond contact interval.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.8] Negative Sign in Meshchersky Rocket Thrust</div>
        <p><strong>The Trap:</strong> Writing $m \frac{dv}{dt} = v_{rel} \frac{dm}{dt}$ and ending up with deceleration because $\frac{dm}{dt} < 0$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Ejected mass travels backward: $\mathbf{v}_{rel} = -u_{ex} \hat{\mathbf{i}}$. Rate of mass change is negative: $\frac{dm}{dt} = -R_{burn}$. Thrust force is $\mathbf{F}_{thrust} = (-u_{ex}\hat{\mathbf{i}})(-R_{burn}) = +u_{ex} R_{burn} \hat{\mathbf{i}}$ (forward acceleration). Always verify physical thrust direction from first principles!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.9] Maximum Compression of a Spring Between Moving Masses</div>
        <p><strong>The Trap:</strong> Assuming maximum spring compression between two free masses on a smooth floor occurs when the first mass comes to rest in the lab frame ($v_1 = 0$).</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Maximum spring compression occurs when the spring stops compressing, which means relative velocity is zero: $\mathbf{v}_1 = \mathbf{v}_2 = \mathbf{V}_{cm}$. The energy stored in the spring is $U_{s,\max} = \frac{1}{2} k x_{\max}^2 = \frac{1}{2}\mu u_{rel}^2$.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 4.10] Center of Mass Velocity with Internal Explosions</div>
        <p><strong>The Trap:</strong> A projectile explodes mid-air into fragments. Students attempt to recalculate the trajectory of the COM using the explosive fragment speeds.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Explosive internal forces sum to zero ($\sum \mathbf{F}_{int} = \mathbf{0}$). Gravity is the sole external force acting on the system. Therefore, the center of mass of the fragments <strong>continues along the original parabolic trajectory</strong> until the first fragment strikes the ground!</div>
      </div>

      <h2 class="section-title">4.4 Dissected JEE Advanced Previous Year Questions (PYQs)</h2>

      <!-- PYQ 4.1 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2018 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Hard • Oblique Rebound on Incline</span>
        </div>
        <div class="pyq-question">
          A small ball is dropped vertically from height $h = 5\text{ m}$ onto a smooth inclined plane of angle $\theta = 30^\circ$ fixed to the ground. The coefficient of restitution between the ball and the plane is $e = \frac{1}{\sqrt{3}}$. Find the distance along the incline between the first impact point and the second impact point. Take $g = 10\text{ m/s}^2$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Impact Velocity & Axis Setup:</strong></p>
          <p>Speed just before impact: $u = \sqrt{2gh} = \sqrt{2 \times 10 \times 5} = 10\text{ m/s}$ directed vertically downward.</p>
          <p>Choose coordinate axes aligned with the incline:</p>
          <ul style="margin-left: 2rem; line-height: 1.8;">
            <li>$x$-axis: Along the incline downwards.</li>
            <li>$y$-axis: Perpendicular to the incline upwards (Line of Impact).</li>
          </ul>
          <p>Components of approach velocity just before impact:</p>
          $$u_x = u \sin\theta = 10 \sin 30^\circ = 5\text{ m/s}$$
          $$u_y = -u \cos\theta = -10 \cos 30^\circ = -5\sqrt{3}\text{ m/s}$$
          <p>Components of acceleration due to gravity:</p>
          $$g_x = g \sin\theta = 10 \sin 30^\circ = 5\text{ m/s}^2$$
          $$g_y = -g \cos\theta = -10 \cos 30^\circ = -5\sqrt{3}\text{ m/s}^2$$
          <p><strong>Step 2: Velocity Components Immediately After Impact:</strong></p>
          <p>Since the incline is smooth, parallel impulse is zero: $v_{1x} = u_x = \mathbf{5\text{ m/s}}$.</p>
          <p>Along the normal (LOI), restitution applies against a fixed mass ($M \to \infty$):</p>
          $$v_{1y} = e |u_y| = \left(\frac{1}{\sqrt{3}}\right)(5\sqrt{3}) = \mathbf{5\text{ m/s}}$$
          <p><strong>Step 3: Time of Flight to Second Impact ($y = 0$):</strong></p>
          $$y(T) = v_{1y} T - \frac{1}{2} (g\cos\theta) T^2 = 0 \implies T = \frac{2 v_{1y}}{g \cos\theta} = \frac{2(5)}{5\sqrt{3}} = \frac{2}{\sqrt{3}}\text{ seconds}$$
          <p><strong>Step 4: Distance Traversed Along Incline:</strong></p>
          $$S_x = v_{1x} T + \frac{1}{2} g_x T^2 = 5\left(\frac{2}{\sqrt{3}}\right) + \frac{1}{2}(5)\left(\frac{2}{\sqrt{3}}\right)^2 = \frac{10}{\sqrt{3}} + \frac{5}{2}\left(\frac{4}{3}\right) = \frac{10}{\sqrt{3}} + \frac{10}{3}\text{ m}$$
          $$S_x = \mathbf{\frac{10(\sqrt{3} + 1)}{3}\text{ m}} \approx 9.11\text{ meters}$$
        </div>
      </div>

      <!-- PYQ 4.2 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2015 • Paper 2</span>
          <span class="pyq-difficulty">Difficulty: Hard • Spring-Coupled Momentum & Maximum Elongation</span>
        </div>
        <div class="pyq-question">
          Two blocks of masses $m_1 = 2\text{ kg}$ and $m_2 = 3\text{ kg}$ are connected by a light spring of force constant $k = 300\text{ N/m}$ on a smooth horizontal floor. Initially, the system is at rest. Block $m_1$ is given an instantaneous horizontal impulse $J = 12\text{ N}\cdot\text{s}$ away from $m_2$. Determine (a) the velocity of the center of mass $V_{cm}$, (b) the maximum elongation $x_{\max}$ of the spring, and (c) the minimum speed attained by block $m_1$ during subsequent motion.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Center of Mass Kinematics:</strong></p>
          <p>Velocity of $m_1$ immediately after impulse: $u_1 = \frac{J}{m_1} = \frac{12}{2} = 6\text{ m/s}$, while $u_2 = 0$.</p>
          $$V_{cm} = \frac{m_1 u_1 + m_2 u_2}{m_1 + m_2} = \frac{2(6) + 3(0)}{2 + 3} = \frac{12}{5} = \mathbf{2.4\text{ m/s}}$$
          <p>Since no external horizontal force acts after impulse, $V_{cm}$ remains invariant throughout the motion.</p>
          <p><strong>Step 2: Maximum Spring Elongation:</strong></p>
          <p>Calculate reduced mass: $\mu = \frac{m_1 m_2}{m_1 + m_2} = \frac{2 \times 3}{2 + 3} = \frac{6}{5} = 1.2\text{ kg}$.</p>
          <p>Initial relative velocity: $u_{rel} = u_1 - u_2 = 6 - 0 = 6\text{ m/s}$.</p>
          <p>At maximum elongation, relative velocity is zero ($v_{rel} = 0$). By Koenig's theorem, all relative kinetic energy is converted into elastic potential energy:</p>
          $$\frac{1}{2} k x_{\max}^2 = \frac{1}{2} \mu u_{rel}^2 \implies x_{\max} = u_{rel}\sqrt{\frac{\mu}{k}} = 6\sqrt{\frac{1.2}{300}} = 6\sqrt{\frac{1}{250}} = \frac{6}{5\sqrt{10}} = \mathbf{\frac{6\sqrt{10}}{50}\text{ m}} \approx 37.9\text{ cm}$$
          <p><strong>Step 3: Minimum Speed of Block $m_1$:</strong></p>
          <p>In the C-frame, block $m_1$ oscillates with velocity amplitude: $v_{1}^* = \frac{m_2}{m_1 + m_2} u_{rel} = \frac{3}{5}(6) = 3.6\text{ m/s}$.</p>
          <p>Velocity in lab frame: $v_1(t) = V_{cm} + v_1^*(t) = 2.4 + 3.6 \cos(\omega t)$.</p>
          <p>When $\cos(\omega t) = -1$:</p>
          $$v_{1, \min} = 2.4 - 3.6 = \mathbf{-1.2\text{ m/s}}$$
          <p>The minimum <em>speed</em> (magnitude) is $|v_1| = 0\text{ m/s}$ (since velocity crosses zero as it transitions from $+6$ to $-1.2$). The minimum algebraic velocity is $-1.2\text{ m/s}$.</p>
        </div>
      </div>

      <!-- PYQ 4.3 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2020 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Hard • Continuous Mass Deposition on Rolling Cart</span>
        </div>
        <div class="pyq-question">
          An open rectangular cart of mass $M_0 = 50\text{ kg}$ is coasting horizontally on a frictionless track with speed $v_0 = 10\text{ m/s}$. Rain begins to fall vertically downward into the open top of the cart at a constant mass deposition rate $\alpha = \frac{dm}{dt} = 2\text{ kg/s}$. Find (a) the velocity of the cart after $t = 25\text{ seconds}$, and (b) the horizontal external force required to keep the cart moving at its initial constant speed $v_0$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Velocity Under Zero Horizontal External Force:</strong></p>
          <p>Rain falls vertically, so it possesses zero initial horizontal momentum ($p_{rain, x} = 0$).</p>
          <p>Because there is no external horizontal force on the cart-water system, total horizontal momentum is conserved:</p>
          $$P_x(t) = [M_0 + m_{water}(t)] v(t) = M_0 v_0 = \text{constant}$$
          $$[M_0 + \alpha t] v(t) = M_0 v_0 \implies v(t) = \frac{M_0 v_0}{M_0 + \alpha t}$$
          <p>At $t = 25\text{ s}$:</p>
          $$v(25) = \frac{50 \times 10}{50 + 2(25)} = \frac{500}{100} = \mathbf{5.0\text{ m/s}}$$
          <p><strong>Step 2: Force Required for Constant Velocity $v_0$:</strong></p>
          <p>From Meshchersky's equation, the relative horizontal velocity of incoming rain is $v_{rel, x} = 0 - v_0 = -v_0$.</p>
          $$F_{ext} + v_{rel, x} \frac{dm}{dt} = m(t) \frac{dv}{dt}$$
          <p>To maintain constant speed $v = v_0$, acceleration must be zero ($\frac{dv}{dt} = 0$):</p>
          $$F_{ext} + (-v_0) \alpha = 0 \implies F_{ext} = \alpha v_0 = (2\text{ kg/s})(10\text{ m/s}) = \mathbf{20\text{ Newtons}}$$
          <p><em>Physical Interpretation:</em> The motor must deliver $20\text{ N}$ forward to accelerate newly captured rain droplets from $0$ up to $v_0$ horizontally.</p>
        </div>
      </div>

      <h2 class="section-title">4.5 High-Caliber Practice Challenge Problems & Complete Solutions</h2>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 4.1] Movable Smooth Wedge Displacement</div>
        <p>A wedge of mass $M = 4\text{ kg}$ with a cylindrical scoop of radius $R = 1.5\text{ m}$ sits on a frictionless horizontal floor. A small block of mass $m = 1\text{ kg}$ is released from rest at the top edge of the scoop. Find the horizontal displacement of the wedge when the block reaches the lowest point of the scoop.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Because no external horizontal force acts on the (wedge + block) system, the $x$-coordinate of the system center of mass remains strictly constant: $\Delta X_{cm} = 0$.</p>
            <p>Let the wedge displace leftward by distance $\Delta x$. In the reference frame of the wedge, the block travels rightward by distance $R$.</p>
            <p>Therefore, the net horizontal displacement of the block relative to the ground is $(R - \Delta x)$ rightward.</p>
            $$m(R - \Delta x) - M \Delta x = 0 \implies \Delta x = \frac{m}{M + m} R$$
            $$\Delta x = \frac{1}{4 + 1}(1.5) = \frac{1.5}{5} = \mathbf{0.30\text{ meters}} = 30\text{ cm leftward}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 4.2] Triple Sequential Billiard Impact</div>
        <p>Three identical smooth balls $A$, $B$, and $C$ of mass $m$ lie at rest along a straight line on a smooth table. Ball $A$ is projected toward $B$ with speed $u$. The coefficient of restitution for all collisions is $e = 0.5$. Determine the final velocity of ball $C$ after all collisions have concluded.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p><strong>First Collision (A and B):</strong></p>
            <p>By momentum conservation: $u_A = u, u_B = 0 \implies v_{A1} + v_{B1} = u$.</p>
            <p>Restitution: $v_{B1} - v_{A1} = e u = 0.5 u$.</p>
            $$v_{B1} = \frac{1 + e}{2} u = \frac{1.5}{2} u = \frac{3}{4} u$$
            $$v_{A1} = \frac{1 - e}{2} u = \frac{0.5}{2} u = \frac{1}{4} u$$
            <p><strong>Second Collision (B and C):</strong></p>
            <p>Ball $B$ strikes stationary ball $C$ with speed $u' = v_{B1} = \frac{3}{4} u$. Applying identical collision formulas:</p>
            $$v_{C1} = \frac{1 + e}{2} u' = \frac{3}{4} \left(\frac{3}{4} u\right) = \mathbf{\frac{9}{16} u} \approx 0.5625 u$$
            $$v_{B2} = \frac{1 - e}{2} u' = \frac{1}{4} \left(\frac{3}{4} u\right) = \frac{3}{16} u$$
            <p><strong>Check for Subsequent Collisions:</strong> Since $v_{A1} = \frac{4}{16}u > v_{B2} = \frac{3}{16}u$, ball $A$ will collide again with ball $B$, but ball $C$ moves with $v_C = \frac{9}{16}u > v_{B2}$ and escapes freely.</p>
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 4.3] Ballistic Pendulum Loop-the-Loop Threshold</div>
        <p>A bullet of mass $m = 20\text{ g}$ is fired horizontally with speed $v$ into a wooden bob of mass $M = 980\text{ g}$ suspended by a light rigid rod of length $L = 1.25\text{ m}$. The bullet embeds completely into the bob. Determine the minimum bullet speed $v_{\min}$ required for the bob to successfully complete a vertical circle. Take $g = 10\text{ m/s}^2$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p><strong>Phase 1: Inelastic Impact:</strong></p>
            <p>Momentum conservation during microsecond impact:</p>
            $$m v = (m + M) V_0 \implies V_0 = \frac{m}{m + M} v = \frac{0.02}{0.02 + 0.98} v = \frac{v}{50}$$
            <p><strong>Phase 2: Vertical Loop with Rigid Rod:</strong></p>
            <p>Because the suspension is a <strong>rigid rod</strong>, the bob cannot go slack. Looping requires only that speed at the top remains non-negative ($v_{top} \ge 0$):</p>
            $$V_0 \ge \sqrt{4gL} = 2\sqrt{gL}$$
            $$V_0 \ge 2\sqrt{10 \times 1.25} = 2\sqrt{12.5} = \sqrt{50} = 5\sqrt{2}\text{ m/s}$$
            <p>Relating to bullet speed:</p>
            $$\frac{v_{\min}}{50} = 5\sqrt{2} \implies v_{\min} = 250\sqrt{2} \approx \mathbf{353.55\text{ m/s}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 4.4] Falling Chain on Scale — The 3x Weight Theorem</div>
        <p>A flexible heavy chain of total length $L = 2\text{ m}$ and total mass $M = 3\text{ kg}$ is held suspended vertically so that its bottom link just touches a weighing scale. The chain is released from rest. Find the reading on the scale when a length $x = 1\text{ m}$ of the chain has accumulated on the platform. Take $g = 10\text{ m/s}^2$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Let linear mass density be $\lambda = M/L = 3/2 = 1.5\text{ kg/m}$.</p>
            <p>The total normal force measured by the scale consists of two distinct contributions:</p>
            $$N_{total} = N_{static} + N_{impulsive}$$
            <p>1. <strong>Static Weight of fallen links:</strong> $N_{static} = (\lambda x) g$.</p>
            <p>2. <strong>Impulsive force of stopping falling links:</strong></p>
            <p>Speed of links falling through height $x$: $v = \sqrt{2gx}$. Rate of mass hitting the scale: $\frac{dm}{dt} = \lambda v$.</p>
            $$N_{impulsive} = v \frac{dm}{dt} = \lambda v^2 = \lambda(2gx) = 2\lambda g x$$
            <p>Summing both components yields the celebrated <strong>3x Factor Theorem</strong>:</p>
            $$N_{total} = \lambda g x + 2\lambda g x = \mathbf{3\lambda g x}$$
            <p>For $x = 1\text{ m}$:</p>
            $$N_{total} = 3(1.5)(10)(1) = \mathbf{45\text{ Newtons}}$$
            <p>Equivalent mass reading: $m_{scale} = \frac{45}{10} = \mathbf{4.5\text{ kg}}$ (which is 1.5 times the mass of the entire chain!).</p>
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 4.5] Rocket Staging & Relativistic Exhaust Efficiency</div>
        <p>A two-stage rocket has total initial mass $M_1 = 10,000\text{ kg}$. Stage 1 carries $7,000\text{ kg}$ of fuel and an empty stage dry casing of $1,000\text{ kg}$. Stage 2 carries $1,500\text{ kg}$ of fuel and a payload of $500\text{ kg}$. The exhaust velocity for both stages is $u_{ex} = 3000\text{ m/s}$. Neglecting gravity and drag, calculate the final burnout velocity $v_f$ of the payload starting from rest.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p><strong>Stage 1 Burn:</strong></p>
            <p>Initial mass $M_{01} = 10,000\text{ kg}$. Mass after Stage 1 fuel burn: $M_{b1} = 10,000 - 7,000 = 3,000\text{ kg}$.</p>
            $$v_1 = u_{ex} \ln\left(\frac{M_{01}}{M_{b1}}\right) = 3000 \ln\left(\frac{10000}{3000}\right) = 3000 \ln(10/3) \approx 3000(1.2040) = 3612\text{ m/s}$$
            <p><strong>Stage 1 Separation:</strong> Empty casing of $1,000\text{ kg}$ is jettisoned. Remaining mass for Stage 2: $M_{02} = 3000 - 1000 = 2,000\text{ kg}$.</p>
            <p><strong>Stage 2 Burn:</strong></p>
            <p>Payload mass alone remains at burnout: $M_{b2} = 2000 - 1500 = 500\text{ kg}$.</p>
            $$\Delta v_2 = u_{ex} \ln\left(\frac{M_{02}}{M_{b2}}\right) = 3000 \ln\left(\frac{2000}{500}\right) = 3000 \ln(4) \approx 3000(1.3863) = 4158.9\text{ m/s}$$
            <p><strong>Total Burnout Velocity:</strong></p>
            $$v_f = v_1 + \Delta v_2 = 3612 + 4158.9 = \mathbf{7770.9\text{ m/s}}$$
          </div>
        </details>
      </div>
    </section>
    """

if __name__ == "__main__":
    content = get_ch4_content()
    print("Chapter 4 content generated successfully. Length:", len(content))
