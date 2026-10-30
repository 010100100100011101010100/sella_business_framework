# Chapter 5 Generator: Rotational Mechanics & Toppling
# Conversational Kota Mentor Voice • Zero Emojis • Modern Typography

def get_ch5_content():
    return r"""
    <section id="ch5" class="chapter-container">
      <span class="chapter-number">Chapter 05</span>
      <h1 class="chapter-title">Rotational Mechanics & Toppling Dynamics</h1>

      <div class="card-box tip-card">
        <div class="card-header-tip">[MENTOR STRATEGY NOTE] Why Rotational Dynamics Makes or Breaks Top Ranks</div>
        <p><strong>Listen to me very carefully:</strong> Rotational mechanics accounts for 14–16% of JEE Advanced Physics. It is historically the single highest-yield, highest-negative-marking chapter in the entire syllabus. Every year, students walk out of the exam hall weeping because they wrote $\tau = I\alpha$ about an accelerating point, or believed that the contact point in pure rolling has zero acceleration.</p>
        <p><strong>The Reality:</strong> Pure rolling is nothing more than translation plus rotation coupled by a single constraint equation. Once you understand how to pick your reference axis—especially the Center of Mass and the Instantaneous Axis of Rotation (IAOR)—the problems solve themselves in 4 lines. Let's master the mechanics.</p>
      </div>

      <h2 class="section-title">5.1 First-Principles Foundations: Rigid Body Dynamics & Kinematics</h2>

      <h3 class="sub-title">5.1.1 Moment of Inertia, Steiner's Theorem & The 2D Lamina Restriction</h3>
      <p>Think of Moment of Inertia $I$ as "rotational stubbornness." In straight-line motion, mass $m$ measures how stubborn an object is against changing speed ($F = ma$). In rotation, Moment of Inertia does the exact same job for spinning ($\tau = I\alpha$). But while mass is fixed, rotational stubbornness depends heavily on how far the mass sits from the spin axis:</p>
      $$I = \int r_\perp^2 dm$$
      <p>where $r_\perp$ is the perpendicular distance from each mass element $dm$ to the chosen axis of rotation.</p>

      <div class="card-box tip-card">
        <div class="card-header-tip">[KEY PRINCIPLE] Foundational Axis Theorems & Their Strict Domain of Validity</div>
        <p><strong>1. Parallel Axis Theorem (Steiner's Theorem):</strong></p>
        $$I_{axis} = I_{cm} + M d_\perp^2$$
        <p><em>Strict Condition:</em> One of the two parallel axes <strong>MUST pass through the Center of Mass (COM)</strong>. The distance $d_\perp$ is the perpendicular distance between the two parallel axes. It is a fatal blunder to apply this theorem directly between two arbitrary non-COM axes!</p>
        <p><strong>2. Perpendicular Axis Theorem:</strong></p>
        $$I_z = I_x + I_y$$
        <p><em>Strict Condition:</em> Valid <strong>ONLY for 2D Planar Laminas</strong> lying completely in the $xy$-plane ($z \equiv 0$). The $z$-axis must be perpendicular to the lamina and pass through the intersection point of the mutually perpendicular $x$ and $y$ axes. Applying this theorem to a 3D sphere, cylinder, or cube is a gross conceptual error!</p>
      </div>

      <p><strong>Canonical Continuous Body Moments of Inertia (JEE Advanced Standard):</strong></p>
      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Uniform Thin Rod ($M, L$):</strong> $I_{cm,\perp} = \frac{1}{12}ML^2$; End axis $I_{end,\perp} = \frac{1}{3}ML^2$; Inclined at angle $\theta$: $I = \frac{1}{12}ML^2\sin^2\theta$.</li>
        <li><strong>Uniform Circular Ring ($M, R$):</strong> Central transverse axis $I_z = MR^2$; Diameter axis $I_d = \frac{1}{2}MR^2$; Tangent in-plane $I_{tan,\parallel} = \frac{3}{2}MR^2$; Tangent perpendicular $I_{tan,\perp} = 2MR^2$.</li>
        <li><strong>Uniform Circular Disc ($M, R$):</strong> Central transverse axis $I_z = \frac{1}{2}MR^2$; Diameter axis $I_d = \frac{1}{4}MR^2$; Tangent in-plane $I_{tan,\parallel} = \frac{5}{4}MR^2$; Tangent perpendicular $I_{tan,\perp} = \frac{3}{2}MR^2$.</li>
        <li><strong>Uniform Thin Spherical Shell ($M, R$):</strong> Diameter axis $I_d = \mathbf{\frac{2}{3}MR^2}$; Tangent axis $I_{tan} = \frac{5}{3}MR^2$.</li>
        <li><strong>Uniform Solid Sphere ($M, R$):</strong> Diameter axis $I_d = \mathbf{\frac{2}{5}MR^2}$; Tangent axis $I_{tan} = \frac{7}{5}MR^2$.</li>
        <li><strong>Uniform Solid Cylinder ($M, R, L$):</strong> Longitudinal axis $I_z = \frac{1}{2}MR^2$; Central transverse axis $I_{trans, cm} = \frac{1}{4}MR^2 + \frac{1}{12}ML^2$.</li>
      </ul>

      <!-- SVG Diagram 5.1: Pure Rolling & Toppling Mechanics -->
      <div class="diagram-container">
                <svg class="diagram-svg" width="600" height="260" viewBox="0 0 600 260">
          <defs>
            <marker id="arrow-ch5" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626"/>
            </marker>
          </defs>
          <!-- Left: Pure Rolling Wheel -->
          <circle cx="150" cy="120" r="70" fill="#f8fafc" stroke="#0f172a" stroke-width="2.5" />
          <line x1="30" y1="190" x2="270" y2="190" stroke="#0f172a" stroke-width="3" />
          <!-- Center Point -->
          <circle cx="150" cy="120" r="5" fill="#0f172a" />
          <line x1="150" y1="120" x2="210" y2="120" stroke="#b45309" stroke-width="3" />
          <text x="165" y="110" font-family="sans-serif" font-size="12" font-weight="bold" fill="#b45309">v_cm</text>
          
          <!-- Top Point Velocity -->
          <circle cx="150" cy="50" r="4" fill="#dc2626" />
          <line x1="150" y1="50" x2="250" y2="50" stroke="#dc2626" stroke-width="3.5" />
          <text x="200" y="42" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">v_top = 2v_cm</text>

          <!-- Contact Point Velocity & Acceleration -->
          <circle cx="150" cy="190" r="5" fill="#047857" />
          <line x1="150" y1="190" x2="150" y2="140" stroke="#047857" stroke-width="3.5" stroke-dasharray="4,3" />
          <text x="158" y="165" font-family="sans-serif" font-size="11" font-weight="bold" fill="#047857">a_c = ω²R ↑</text>
          <text x="90" y="215" font-family="sans-serif" font-size="12" font-weight="bold" fill="#047857">v_contact = 0 (IAOR)</text>

          <!-- Right: Toppling Block -->
          <rect x="370" y="70" width="80" height="120" fill="#f1f5f9" stroke="#0f172a" stroke-width="2.5" />
          <line x1="330" y1="190" x2="570" y2="190" stroke="#0f172a" stroke-width="3" />
          <!-- Center of mass of block -->
          <circle cx="410" cy="130" r="4" fill="#0f172a" />
          <text x="418" y="130" font-family="sans-serif" font-size="11" fill="#0f172a">COM</text>
          <line x1="410" y1="130" x2="410" y2="175" stroke="#0f172a" stroke-width="2.5" />
          <text x="415" y="165" font-family="sans-serif" font-size="11" fill="#0f172a">mg</text>

          <!-- Applied Force F at height h -->
          <line x1="320" y1="80" x2="370" y2="80" stroke="#dc2626" stroke-width="3" marker-end="url(#arrow-ch5)" />
          <text x="325" y="72" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">F (at h)</text>

          <!-- Shifted Normal Reaction N -->
          <circle cx="445" cy="190" r="4" fill="#b45309" />
          <line x1="445" y1="190" x2="445" y2="135" stroke="#b45309" stroke-width="3" />
          <text x="450" y="150" font-family="sans-serif" font-size="12" font-weight="bold" fill="#b45309">N (shifted)</text>
          <line x1="410" y1="198" x2="445" y2="198" stroke="#b45309" stroke-width="1.5" />
          <text x="415" y="215" font-family="sans-serif" font-size="11" fill="#b45309">x_N ≤ b/2</text>

          <!-- Friction Force -->
          <line x1="445" y1="190" x2="390" y2="190" stroke="#0284c7" stroke-width="3" />
          <text x="390" y="180" font-family="sans-serif" font-size="11" font-weight="bold" fill="#0284c7">f_s</text>
        </svg>
        <div class="diagram-caption">Figure 5.1: (Left) Velocity distribution and centripetal acceleration in pure rolling. (Right) Toppling mechanics: normal reaction shifts toward tipping edge to counteract overturning torque.</div>
      </div>

      <h3 class="sub-title">5.1.2 The Generalized Torque Equation About Arbitrary Reference Points</h3>
      <p>Let $O$ be an arbitrary reference point that may itself accelerate with acceleration $\mathbf{a}_O$ relative to an inertial frame. The fundamental angular momentum equation is:</p>
      $$\boldsymbol{\tau}_O = \frac{d\mathbf{L}_O}{dt} + \mathbf{v}_O \times \mathbf{P}$$
      <p>where $\mathbf{P} = M\mathbf{v}_{cm}$ is the total linear momentum. The simple formula $\boldsymbol{\tau}_O = I_O \boldsymbol{\alpha}$ holds <strong>strictly if and only if</strong> one of the following three conditions is met:</p>
      <ol style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>The reference point $O$ is stationary in an inertial frame ($\mathbf{v}_O = \mathbf{0}, \mathbf{a}_O = \mathbf{0}$).</strong></li>
        <li><strong>The reference point $O$ is the Center of Mass ($O \equiv C$):</strong> Here $\mathbf{r}_{cm/O} = \mathbf{0}$, meaning pseudo-forces exert identically zero torque: $\boldsymbol{\tau}_{cm} = I_{cm}\boldsymbol{\alpha}$ unconditionally in any reference frame!</li>
        <li><strong>The acceleration of point $O$ is directed along the line connecting $O$ and the Center of Mass ($\mathbf{a}_O \parallel \mathbf{r}_{cm/O}$):</strong> The cross product $\mathbf{r}_{cm/O} \times (-M\mathbf{a}_O) = \mathbf{0}$.</li>
      </ol>
      <p>If torque is evaluated about an arbitrary accelerating point $P$ not satisfying these conditions, one <strong>MUST include the torque of the pseudo-force</strong> acting at the center of mass:</p>
      $$\boldsymbol{\tau}_{P, net} = \boldsymbol{\tau}_{P, real} + \mathbf{r}_{cm/P} \times (-M \mathbf{a}_P) = I_P \boldsymbol{\alpha}$$

      <h3 class="sub-title">5.1.3 Pure Rolling Dynamics on Horizontal & Inclined Planes</h3>
      <p>Pure rolling is the superposition of translational motion of the center of mass and rotation about the center of mass, subject to the non-slip kinematic constraint at the instantaneous contact point $C$:</p>
      $$\mathbf{v}_C = \mathbf{v}_{cm} + \boldsymbol{\omega} \times \mathbf{R} = \mathbf{0} \implies v_{cm} = \omega R$$
      $$\mathbf{a}_{C, tangential} = \mathbf{a}_{cm} - \boldsymbol{\alpha} R = \mathbf{0} \implies a_{cm} = \alpha R$$
      <p><strong>Crucial Acceleration Fact:</strong> While the <em>tangential</em> acceleration of the contact point is zero, its <em>radial/centripetal</em> acceleration is non-zero: $\mathbf{a}_C = \omega^2 R \hat{\mathbf{n}}$ directed toward the wheel center. The contact point is executing a cycloid path!</p>

      <p><strong>Pure Rolling Down an Inclined Plane of Angle $\theta$:</strong></p>
      <p>Writing Newton's second law along the incline and torque about the Center of Mass:</p>
      $$Mg\sin\theta - f_s = M a_{cm}$$
      $$\tau_{cm} = f_s R = I_{cm} \alpha = I_{cm} \left(\frac{a_{cm}}{R}\right) \implies f_s = \frac{I_{cm}}{R^2} a_{cm}$$
      <p>Substituting $f_s$ into the linear equation yields the universal rolling acceleration equation:</p>
      $$a_{cm} = \frac{g \sin\theta}{1 + \frac{I_{cm}}{MR^2}} = \frac{g \sin\theta}{1 + \frac{k^2}{R^2}}$$
      <p>where $k$ is the radius of gyration. The required static friction force to prevent slipping is:</p>
      $$f_s = \frac{Mg\sin\theta}{1 + \frac{MR^2}{I_{cm}}}$$
      <p>To ensure pure rolling without slipping, $f_s \le \mu_s N = \mu_s Mg\cos\theta$. This establishes the critical incline angle threshold:</p>
      $$\tan\theta_c = \mu_s \left(1 + \frac{MR^2}{I_{cm}}\right)$$

      <h3 class="sub-title">5.1.4 Toppling vs. Sliding Mechanics</h3>
      <p>Consider a rectangular block of mass $M$, width $b$, and height $h$ resting on a horizontal plane with static friction coefficient $\mu_s$. A horizontal force $F$ is applied at height $y$ above the base.</p>
      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Normal Force Shift:</strong> As $F$ increases, the normal force shifts forward by distance $x_N$ from the center to counteract the overturning torque $F y$. Torque balance about COM gives:
        $$N x_N = F\left(y - \frac{h}{2}\right) + f_s \left(\frac{h}{2}\right) = F y \implies x_N = \frac{F y}{Mg}$$</li>
        <li><strong>Toppling Condition:</strong> The block begins to topple when the normal force shifts all the way to the forward edge: $x_{N,\max} = \frac{b}{2}$. The critical toppling force is:
        $$F_{topple} = \frac{b}{2y} Mg$$</li>
        <li><strong>Sliding Condition:</strong> The block begins to slide when $F$ overcomes maximum static friction:
        $$F_{slide} = \mu_s Mg$$</li>
        <li><strong>Universal Criterion:</strong>
          <ul>
            <li>If $F_{slide} < F_{topple} \iff \mu_s < \frac{b}{2y}$: The block <strong>slides before toppling</strong>.</li>
            <li>If $F_{topple} < F_{slide} \iff \mu_s > \frac{b}{2y}$: The block <strong>topples before sliding</strong>.</li>
          </ul>
        </li>
      </ul>

      <h3 class="sub-title">5.1.5 The Instantaneous Center of Rotation (IAOR) Velocity Vector Field</h3>
      <p>For any rigid body undergoing planar general motion, there exists at every instant a unique point in space (which may lie inside or outside the body) that has dead zero velocity: $\mathbf{v}_{IAOR} = \mathbf{0}$. This point is the <strong>Instantaneous Axis of Rotation (IAOR)</strong>.</p>
      <p><strong>The Beauty of the IAOR:</strong></p>
      <p>At that instant, the complex combined motion of translation plus rotation reduces purely to pure rotation about the IAOR with angular velocity $\omega$! The velocity of any particle $P$ in the body is simply:</p>
      $$\mathbf{v}_P = \boldsymbol{\omega} \times \mathbf{r}_{P/IAOR} \implies v_P = \omega r_P$$
      <p>and the direction of $\mathbf{v}_P$ is perpendicular to the line joining $P$ to the IAOR. Furthermore, kinetic energy simplifies to a single term:</p>
      $$K = \frac{1}{2} I_{IAOR} \omega^2$$
      <p>By Steiner's parallel axis theorem, $I_{IAOR} = I_{cm} + M R^2$, which immediately yields $\frac{1}{2}(I_{cm} + MR^2)\omega^2 = \frac{1}{2}I_{cm}\omega^2 + \frac{1}{2}Mv_{cm}^2$. The two descriptions are mathematically and physically identical!</p>

      <h2 class="section-title">5.2 Master Formula Summary Table: Rotational Dynamics</h2>
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
              <td><strong>Parallel Axis Theorem</strong></td>
              <td class="formula-math">$$I_{axis} = I_{cm} + M d_\perp^2$$</td>
              <td><span class="validity-tag">One axis must pass through Center of Mass</span></td>
              <td><span class="invalidity-tag">Applying between two arbitrary non-COM parallel axes</span></td>
            </tr>
            <tr>
              <td><strong>Perpendicular Axis Theorem</strong></td>
              <td class="formula-math">$$I_z = I_x + I_y$$</td>
              <td><span class="validity-tag">Strictly planar 2D laminar bodies ($z=0$)</span></td>
              <td><span class="invalidity-tag">Applying to 3D bodies like spheres, cylinders, or boxes</span></td>
            </tr>
            <tr>
              <td><strong>Generalized Torque Equation</strong></td>
              <td class="formula-math">$$\boldsymbol{\tau}_O = I_O \boldsymbol{\alpha}$$</td>
              <td><span class="validity-tag">$O$ fixed in inertial frame, or $O \equiv C$, or $\mathbf{a}_O \parallel \mathbf{r}_{cm/O}$</span></td>
              <td><span class="invalidity-tag">Taking torque about an accelerating point without adding pseudo-torque</span></td>
            </tr>
            <tr>
              <td><strong>Pure Rolling Incline Acceleration</strong></td>
              <td class="formula-math">$$a_{cm} = \frac{g\sin\theta}{1 + I_{cm}/(MR^2)}$$</td>
              <td><span class="validity-tag">Pure rolling without slipping ($f_s \le \mu_s N$)</span></td>
              <td><span class="invalidity-tag">Using this formula when slipping occurs ($a_{cm} = g(\sin\theta - \mu_k\cos\theta)$)</span></td>
            </tr>
            <tr>
              <td><strong>Angular Momentum Decomposition</strong></td>
              <td class="formula-math">$$\mathbf{L}_O = \mathbf{r}_{cm/O} \times M\mathbf{v}_{cm} + I_{cm}\boldsymbol{\omega}$$</td>
              <td><span class="validity-tag">Rigid body executing planar general motion</span></td>
              <td><span class="invalidity-tag">Writing $L = I_O \omega$ when axis through $O$ is not a principal axis</span></td>
            </tr>
            <tr>
              <td><strong>Center of Percussion</strong></td>
              <td class="formula-math">$$d_{cop} = \frac{I_{hinge}}{M d_{cm}}$$</td>
              <td><span class="validity-tag">Pivoted body subjected to transverse impact</span></td>
              <td><span class="invalidity-tag">Assuming zero hinge reaction when struck at the center of mass</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">5.3 10 Forensic NTA/JEE Negative-Marking Trap Alerts</h2>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.1] Acceleration of Contact Point in Pure Rolling</div>
        <p><strong>The Trap:</strong> Because the instantaneous velocity of the contact point is zero ($\mathbf{v}_C = \mathbf{0}$), students deduce that its acceleration is also zero ($\mathbf{a}_C = \mathbf{0}$).</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> The contact point is stationary only for an infinitesimal instant. While tangential acceleration vanishes, its <strong>centripetal acceleration is non-zero: $\mathbf{a}_C = \omega^2 R$ directed straight upward toward the center of the wheel</strong>! Writing $\mathbf{a}_C = \mathbf{0}$ leads to catastrophic errors in normal reaction and pseudo-force problems.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.2] Perpendicular Axis Theorem on a Solid Cylinder or Sphere</div>
        <p><strong>The Trap:</strong> Finding moment of inertia of a solid cylinder of radius $R$ about diameter by claiming $I_z = I_x + I_y \implies I_d = \frac{1}{2}I_z = \frac{1}{4}MR^2$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> The perpendicular axis theorem is valid <strong>strictly for 2D flat sheets</strong>! A cylinder has length $L$, so its transverse moment of inertia is $I_{\text{trans}} = \frac{1}{4}MR^2 + \frac{1}{12}ML^2$. Setting $L = 0$ is valid only for an infinitesimally thin disc.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.3] Friction Direction in Pure Rolling</div>
        <p><strong>The Trap:</strong> Assuming static friction on a rolling wheel always acts backward to oppose translational motion.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Friction acts to prevent relative slipping at the contact point. If a wheel is driven by an axle torque $\tau$ (like the rear wheel of an accelerating car), static friction acts <strong>FORWARD</strong> to propel the vehicle! On an unpowered front wheel, static friction acts backward to provide rotational angular acceleration.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.4] Writing $\tau = I\alpha$ About an Accelerating Point</div>
        <p><strong>The Trap:</strong> Writing $\tau_P = I_P \alpha$ about the contact point of an accelerating rolling body when the contact surface is itself accelerating (e.g., rolling inside an accelerating elevator or truck).</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Point $P$ accelerates, so you must include the pseudo-torque: $\boldsymbol{\tau}_{P, real} + \mathbf{r}_{cm/P} \times (-M\mathbf{a}_P) = I_P \boldsymbol{\alpha}$. Alternatively and much more reliably: <strong>Always take torque about the Center of Mass (COM)</strong>, where pseudo-torque is identically zero regardless of any reference frame acceleration!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.5] Released Horizontal Rod Tip Acceleration $> g$</div>
        <p><strong>The Trap:</strong> A uniform rod of length $L$ is pivoted horizontally at one end and released from rest. Students assume no part of the rod can accelerate faster than $g$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Torque about the hinge: $\tau = Mg\left(\frac{L}{2}\right) = I_{hinge} \alpha = \left(\frac{1}{3}ML^2\right)\alpha \implies \alpha = \frac{3g}{2L}$. The tangential acceleration of the free tip is $a_{tip} = \alpha L = \mathbf{\frac{3}{2}g = 1.5g > g}$! An object resting on the tip will lose contact immediately and undergo free fall ($a = g$).</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.6] Misapplying Steiner's Theorem Between Non-COM Axes</div>
        <p><strong>The Trap:</strong> Given moment of inertia about one end of a rod $I_{end} = \frac{1}{3}ML^2$, finding $I$ about an axis at distance $d = L/4$ from that end by adding $M(L/4)^2$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Steiner's theorem works ONLY relative to the COM: $I_{new} = I_{cm} + M d_{cm}^2 = \frac{1}{12}ML^2 + M(L/4)^2 = \frac{1}{12}ML^2 + \frac{1}{16}ML^2 = \frac{7}{48}ML^2$. You cannot shift directly between two non-COM axes!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.7] Kinetic Energy of Rolling without Slipping</div>
        <p><strong>The Trap:</strong> Calculating total kinetic energy of a rolling body as either purely $\frac{1}{2}M v_{cm}^2$ or purely $\frac{1}{2}I_{cm}\omega^2$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> By Koenig's theorem: $K_{total} = \frac{1}{2}M v_{cm}^2 + \frac{1}{2}I_{cm}\omega^2 = \frac{1}{2}M v_{cm}^2\left(1 + \frac{k^2}{R^2}\right)$. Alternatively, using the Instantaneous Axis of Rotation (IAOR): $K_{total} = \frac{1}{2}I_{IAOR}\omega^2$. Both yield identical results.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.8] Toppling on Incline vs. Sliding Competition</div>
        <p><strong>The Trap:</strong> Assuming a cube on an incline always topples when the tilt reaches $\theta = 45^\circ$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> For a cube of side $a$, toppling occurs when $\tan\theta = \frac{a/2}{a/2} = 1 \implies \theta = 45^\circ$. HOWEVER, if the coefficient of friction satisfies $\mu < 1$, the cube will start sliding at $\theta = \arctan(\mu) < 45^\circ$ before toppling can ever occur! Always compare $\theta_{slide} = \arctan\mu$ with $\theta_{topple} = \arctan(b/h)$.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.9] Conservation of Angular Momentum Across Hinges</div>
        <p><strong>The Trap:</strong> Conserving angular momentum about the Center of Mass when a projectile strikes a hinged rod.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> The hinge exerts an unknown external impulsive reaction force $\mathbf{J}_{hinge}$. This reaction creates a non-zero torque about the Center of Mass ($\boldsymbol{\tau}_{cm} \ne \mathbf{0}$). You <strong>MUST conserve angular momentum about the hinge pivot</strong>, where the lever arm of the hinge reaction is identically zero!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 5.10] Rolling with Slipping Transition Time</div>
        <p><strong>The Trap:</strong> Projecting a spinning bowling ball onto a rough floor with $\omega_0$ and $v_0 = 0$. Students assume static friction acts immediately.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Slipping occurs initially, so friction is kinetic: $f_k = \mu_k Mg$ (constant). Acceleration is $a_{cm} = \mu_k g$ forward, and angular deceleration is $\alpha = \frac{f_k R}{I_{cm}} = \frac{\mu_k Mg R}{I_{cm}}$ backward. Pure rolling begins only when $v(t) = \omega(t) R$. From that instant onward, friction drops discontinuously to zero on a level floor!</div>
      </div>

      <h2 class="section-title">5.4 Dissected JEE Advanced Previous Year Questions (PYQs)</h2>

      <!-- PYQ 5.1 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2016 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Hard • Pure Rolling on Incline Transition</span>
        </div>
        <div class="pyq-question">
          A uniform disc of mass $M = 2\text{ kg}$ and radius $R = 0.5\text{ m}$ is rolling without slipping on a horizontal surface with linear speed $v_0 = 6\text{ m/s}$. It smoothly ascends a rough incline of inclination angle $\theta = 30^\circ$. The coefficient of static friction between the disc and the incline is $\mu_s = 0.4$. (a) Determine whether the disc rolls without slipping up the incline. (b) Find the maximum vertical height $h_{\max}$ reached by the disc. Take $g = 10\text{ m/s}^2$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Check Condition for Pure Rolling on Incline:</strong></p>
          <p>For a uniform disc, $I_{cm} = \frac{1}{2}MR^2$, so the radius of gyration ratio is $\frac{k^2}{R^2} = \frac{1}{2}$.</p>
          <p>The minimum coefficient of static friction required to prevent slipping on an incline is:</p>
          $$\mu_{\min} = \frac{\tan\theta}{1 + \frac{MR^2}{I_{cm}}} = \frac{\tan 30^\circ}{1 + 2} = \frac{1}{3\sqrt{3}} \approx 0.192$$
          <p>Since the given friction coefficient $\mu_s = 0.4 > 0.192$, the disc <strong>rolls purely without slipping</strong> during the entire ascent!</p>
          <p><strong>Step 2: Conservation of Total Mechanical Energy:</strong></p>
          <p>In pure rolling, static friction does zero net mechanical work ($W_{f_s} = 0$). Therefore, total mechanical energy is conserved between the floor and maximum height:</p>
          $$E_i = \frac{1}{2}M v_0^2 + \frac{1}{2}I_{cm}\omega_0^2 = \frac{1}{2}M v_0^2 + \frac{1}{4}M v_0^2 = \frac{3}{4}M v_0^2$$
          $$E_f = M g h_{\max}$$
          <p>Equating initial and final energy:</p>
          $$M g h_{\max} = \frac{3}{4} M v_0^2 \implies h_{\max} = \frac{3 v_0^2}{4 g}$$
          <p>Substituting $v_0 = 6\text{ m/s}$ and $g = 10\text{ m/s}^2$:</p>
          $$h_{\max} = \frac{3(36)}{40} = \mathbf{2.70\text{ meters}}$$
          <p><em>Distance traveled along incline:</em> $s = \frac{h_{\max}}{\sin 30^\circ} = \frac{2.7}{0.5} = \mathbf{5.4\text{ meters}}$.</p>
        </div>
      </div>

      <!-- PYQ 5.2 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2019 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Hard • Pivoted Rod Hinge Reaction Dynamics</span>
        </div>
        <div class="pyq-question">
          A uniform thin rod of mass $M = 1.5\text{ kg}$ and length $L = 1.0\text{ m}$ is pivoted about a frictionless horizontal axis passing through one end. The rod is released from rest from a horizontal position. Find the horizontal and vertical components of the hinge reaction force on the rod at the instant it has rotated through angle $\theta = 60^\circ$ from the initial horizontal. Take $g = 10\text{ m/s}^2$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Angular Velocity from Energy Conservation:</strong></p>
          <p>The Center of Mass is at distance $d = L/2$ from the hinge. When the rod drops by $\theta = 60^\circ$, COM falls by $\Delta h = \frac{L}{2}\sin 60^\circ = \frac{L\sqrt{3}}{4}$.</p>
          $$\Delta U = Mg\left(\frac{L\sqrt{3}}{4}\right) = \frac{1}{2} I_{hinge} \omega^2 = \frac{1}{6}ML^2 \omega^2$$
          $$\omega^2 = \frac{3\sqrt{3}g}{2L}$$
          <p><strong>Step 2: Angular Acceleration from Torque:</strong></p>
          <p>Torque about the hinge at angle $\theta$ below horizontal:</p>
          $$\tau_{hinge} = Mg\left(\frac{L}{2}\cos\theta\right) = \left(\frac{1}{3}ML^2\right)\alpha$$
          $$\alpha = \frac{3g\cos\theta}{2L}$$
          <p>At $\theta = 60^\circ$: $\alpha = \frac{3g(1/2)}{2L} = \frac{3g}{4L}$.</p>
          <p><strong>Step 3: Accelerations of the Center of Mass:</strong></p>
          <p>Tangential acceleration of COM: $a_t = \alpha \left(\frac{L}{2}\right) = \frac{3g}{8}$.</p>
          <p>Radial centripetal acceleration toward hinge: $a_r = \omega^2 \left(\frac{L}{2}\right) = \frac{3\sqrt{3}g}{4}$.</p>
          <p><strong>Step 4: Hinge Reaction Components:</strong></p>
          <p>Resolving accelerations horizontally ($x$) and vertically ($y$):</p>
          $$a_x = a_r \cos 60^\circ - a_t \sin 60^\circ = \frac{3\sqrt{3}g}{8} - \frac{3\sqrt{3}g}{16} = \frac{3\sqrt{3}g}{16}$$
          $$N_x = M a_x = (1.5)\left(\frac{3\sqrt{3}(10)}{16}\right) \approx \mathbf{4.87\text{ N}}$$
          $$a_y = a_r \sin 60^\circ + a_t \cos 60^\circ = \frac{9g}{8} + \frac{3g}{16} = \frac{21g}{16}$$
          <p>Vertical equation of motion: $Mg - N_y = M a_y \implies N_y = M(g - a_y) = -\frac{5Mg}{16}$</p>
          $$N_y = -\frac{5(1.5)(10)}{16} = \mathbf{-4.69\text{ N}} \quad (\text{hinge pulls downward!})$$
        </div>
      </div>

      <!-- PYQ 5.3 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2021 • Paper 2</span>
          <span class="pyq-difficulty">Difficulty: Hard • Horizontal Force Applied to Rolling Cylinder</span>
        </div>
        <div class="pyq-question">
          A solid uniform cylinder of mass $M = 4\text{ kg}$ and radius $R = 0.2\text{ m}$ rests on a rough horizontal floor with static friction coefficient $\mu_s = 0.3$. A horizontal pulling force $F = 18\text{ N}$ is applied to a string wound around the top of the cylinder (at height $2R$ above the ground). Determine (a) the acceleration of the center of mass $a_{cm}$, (b) the magnitude and direction of the static friction force $f_s$, and (c) the maximum force $F_{\max}$ for which pure rolling without slipping is maintained.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Equations of Motion Assuming Pure Rolling:</strong></p>
          <p>Let friction $f_s$ act forward in the direction of $F$ (we will let the sign verify direction):</p>
          $$F + f_s = M a_{cm}$$
          <p>Taking torque about the Center of Mass (clockwise positive):</p>
          $$\tau_{cm} = F R - f_s R = I_{cm} \alpha = \left(\frac{1}{2}MR^2\right)\left(\frac{a_{cm}}{R}\right) = \frac{1}{2}MR a_{cm}$$
          $$F - f_s = \frac{1}{2} M a_{cm}$$
          <p><strong>Step 2: Solve Acceleration and Friction:</strong></p>
          <p>Adding the two equations:</p>
          $$2F = \frac{3}{2} M a_{cm} \implies a_{cm} = \frac{4F}{3M}$$
          $$a_{cm} = \frac{4(18)}{3(4)} = \frac{72}{12} = \mathbf{6.0\text{ m/s}^2}$$
          <p>Subtracting the torque equation from the force equation:</p>
          $$2f_s = \frac{1}{2} M a_{cm} \implies f_s = \frac{1}{4} M a_{cm} = \frac{1}{4} M \left(\frac{4F}{3M}\right) = \frac{F}{3}$$
          $$f_s = \frac{18}{3} = \mathbf{+6.0\text{ N}} \quad (\text{acts FORWARD in direction of } F!)$$
          <p><strong>Step 3: Threshold for Slipping ($f_s \le \mu_s N$):</strong></p>
          <p>Normal force: $N = Mg = 4(10) = 40\text{ N}$. Maximum static friction: $f_{s,\max} = \mu_s N = 0.3(40) = 12\text{ N}$.</p>
          $$f_s = \frac{F}{3} \le 12\text{ N} \implies F_{\max} = 3(12) = \mathbf{36\text{ Newtons}}$$
          <p>Since $F = 18\text{ N} < 36\text{ N}$, the assumption of pure rolling is fully valid!</p>
        </div>
      </div>

      <h2 class="section-title">5.5 High-Caliber Practice Challenge Problems & Complete Solutions</h2>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 5.1] The Critical Spool Pulling Angle</div>
        <p>A spool of mass $M$ consists of an inner cylinder of radius $r = 10\text{ cm}$ and two outer flanges of radius $R = 20\text{ cm}$. A light thread wound around the inner spool is pulled with force $F$ at an angle $\theta$ above the horizontal. Find the critical angle $\theta_0$ at which the spool slides without rolling (zero angular acceleration $\alpha = 0$).</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>For pure rolling, the Instantaneous Axis of Rotation (IAOR) is the line of contact with the ground at the bottom of the outer radius $R$.</p>
            <p>The torque about this contact point $C$ determines whether the spool rolls clockwise or counterclockwise:</p>
            $$\tau_C = F d_{\perp} = F (R\cos\theta - r)$$
            <p>Setting $\tau_C = 0$ for zero angular acceleration:</p>
            $$R\cos\theta_0 - r = 0 \implies \cos\theta_0 = \frac{r}{R} = \frac{10}{20} = 0.5 \implies \mathbf{\theta_0 = 60^\circ}$$
            <p><strong>Physical Regimes:</strong></p>
            <ul style="margin-left: 1.5rem; line-height: 1.8;">
              <li>If $\theta < 60^\circ$: $\tau_C > 0$ (Clockwise torque) $\implies$ rolls forward (rightward).</li>
              <li>If $\theta > 60^\circ$: $\tau_C < 0$ (Counterclockwise torque) $\implies$ rolls backward (leftward).</li>
              <li>If $\theta = 60^\circ$: $\tau_C = 0 \implies$ spool cannot roll; it purely skids forward!</li>
            </ul>
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 5.2] Center of Percussion of a Baseball Bat</div>
        <p>A baseball bat of mass $M = 1.0\text{ kg}$ is modeled as a slender rod of length $L = 0.9\text{ m}$ pivoted at the handle grip $O$. Determine the sweet spot distance $d_{cop}$ from the pivot where a baseball must strike so that the instantaneous impulsive reaction force at the grip vanishes identically ($J_{hinge} = 0$).</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Let an impulse $J$ be applied at distance $d$ from the pivot $O$. Linear impulse equation:</p>
            $$J + J_{hinge} = M \Delta V_{cm} = M \left(\omega \frac{L}{2}\right)$$
            <p>Angular impulse about pivot $O$:</p>
            $$J d = I_{hinge} \omega = \left(\frac{1}{3}ML^2\right)\omega \implies \omega = \frac{3J d}{ML^2}$$
            <p>Substituting $\omega$ into the linear impulse equation:</p>
            $$J + J_{hinge} = M \left(\frac{3J d}{ML^2}\right)\left(\frac{L}{2}\right) = \frac{3J d}{2L}$$
            <p>Setting $J_{hinge} = 0$:</p>
            $$J = \frac{3J d}{2L} \implies d = \mathbf{\frac{2}{3}L}$$
            <p>For $L = 0.9\text{ m}$:</p>
            $$d_{cop} = \frac{2}{3}(0.9) = \mathbf{0.60\text{ meters}} = 60\text{ cm from the grip}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 5.3] Toppling of a Tall Crate on Accelerating Truck</div>
        <p>A rectangular shipping container of width $b = 1.2\text{ m}$ and height $h = 2.4\text{ m}$ rests on the flat bed of a truck with friction coefficient $\mu_s = 0.7$. The truck accelerates horizontally forward with acceleration $a$. Find (a) the maximum acceleration $a_{\max}$ the truck can maintain without the crate toppling, and (b) whether the crate topples or slides first.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>In the non-inertial reference frame of the truck accelerating at $a$, a backward pseudo-force $M a$ acts through the Center of Mass at height $h/2 = 1.2\text{ m}$.</p>
            <p><strong>Condition for Toppling:</strong> Torque about the rear tipping edge must vanish at the verge of tipping (normal reaction concentrated at the rear corner):</p>
            $$Mg\left(\frac{b}{2}\right) - Ma\left(\frac{h}{2}\right) = 0 \implies a_{topple} = g \left(\frac{b}{h}\right)$$
            $$a_{topple} = (10)\left(\frac{1.2}{2.4}\right) = (10)(0.5) = \mathbf{5.0\text{ m/s}^2}$$
            <p><strong>Condition for Sliding:</strong></p>
            $$a_{slide} = \mu_s g = (0.7)(10) = 7.0\text{ m/s}^2$$
            <p>Since $a_{topple} = 5.0\text{ m/s}^2 < a_{slide} = 7.0\text{ m/s}^2$, the crate <strong>topples over backward before it can slide</strong>. Maximum safe acceleration is $5.0\text{ m/s}^2$.</p>
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 5.4] Separation Angle for a Sphere Rolling Off a Cylinder</div>
        <p>A small solid uniform sphere of radius $r$ rolls without slipping from rest at the top summit of a large fixed solid cylinder of radius $R \gg r$. Determine the angle $\theta_{sep}$ from the upward vertical at which the sphere loses contact with the cylinder.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>For a solid sphere, $I_{cm} = \frac{2}{5}mr^2$, so $k^2/r^2 = 2/5$. Effective kinetic energy factor is $1 + 2/5 = 7/5$.</p>
            <p>By energy conservation at angle $\theta$:</p>
            $$mg(R+r)(1 - \cos\theta) = \frac{1}{2}m v^2 + \frac{1}{2}I\omega^2 = \frac{7}{10} m v^2 \implies v^2 = \frac{10}{7}g(R+r)(1 - \cos\theta)$$
            <p>Normal force along the radial line toward cylinder center:</p>
            $$mg\cos\theta - N = \frac{m v^2}{R+r} = \frac{10}{7}mg(1 - \cos\theta)$$
            $$N = mg\left[\cos\theta - \frac{10}{7}(1 - \cos\theta)\right] = mg\left[\frac{17}{7}\cos\theta - \frac{10}{7}\right]$$
            <p>Separation occurs when $N = 0$:</p>
            $$\frac{17}{7}\cos\theta_{sep} = \frac{10}{7} \implies \cos\theta_{sep} = \frac{10}{17} \implies \mathbf{\theta_{sep} = \arccos(10/17) \approx 53.97^\circ}$$
            <p><em>Comparison:</em> A frictionless sliding particle separates at $\cos\theta = 2/3 \approx 48.2^\circ$. Rotational inertia stores energy, delaying separation until a larger angle ($54.0^\circ$)!</p>
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 5.5] Inelastic Impact with a Free Floating Rod</div>
        <p>A uniform thin rod of mass $M = 2\text{ kg}$ and length $L = 1.2\text{ m}$ lies at rest on a frictionless horizontal table. A small putty ball of mass $m = 1\text{ kg}$ traveling perpendicular to the rod with speed $v = 12\text{ m/s}$ strikes one end of the rod and sticks to it permanently. Calculate (a) the velocity of the center of mass of the combined system $V_{cm}$, and (b) the angular velocity $\omega$ of the system about its new center of mass immediately after collision.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p><strong>Step 1: Center of Mass Velocity:</strong></p>
            <p>Linear momentum is conserved in the horizontal plane:</p>
            $$m v = (M + m) V_{cm} \implies V_{cm} = \frac{m v}{M + m} = \frac{1(12)}{2 + 1} = \frac{12}{3} = \mathbf{4.0\text{ m/s}}$$
            <p><strong>Step 2: Position of Combined Center of Mass:</strong></p>
            <p>Taking the center of the rod as origin: putty is at $x = L/2 = 0.6\text{ m}$.</p>
            $$x_{cm} = \frac{M(0) + m(L/2)}{M + m} = \frac{1(0.6)}{3} = 0.2\text{ m from rod center}$$
            <p>Distance of putty from new COM: $d_p = 0.6 - 0.2 = 0.4\text{ m}$. Distance of rod center from new COM: $d_r = 0.2\text{ m}$.</p>
            <p><strong>Step 3: New Moment of Inertia about Combined COM:</strong></p>
            $$I_{new} = \left[\frac{1}{12}ML^2 + M d_r^2\right] + m d_p^2$$
            $$I_{new} = \left[\frac{1}{12}(2)(1.2^2) + 2(0.2^2)\right] + 1(0.4^2) = [0.24 + 0.08] + 0.16 = 0.32 + 0.16 = 0.48\text{ kg}\cdot\text{m}^2$$
            <p><strong>Step 4: Angular Momentum Conservation About New COM:</strong></p>
            <p>Initial angular momentum of putty about the new COM coordinate:</p>
            $$L_{init} = m v d_p = (1)(12)(0.4) = 4.8\text{ kg}\cdot\text{m}^2/\text{s}$$
            $$I_{new} \omega = 4.8 \implies \omega = \frac{4.8}{0.48} = \mathbf{10.0\text{ rad/s}}$$
          </div>
        </details>
      </div>
    </section>
    """

if __name__ == "__main__":
    content = get_ch5_content()
    print("Chapter 5 content generated successfully. Length:", len(content))
