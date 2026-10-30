# Chapter 2 Generator: Newton's Laws & Complex Friction Dynamics
# Conversational Kota Mentor Voice • Zero Emojis • Modern Typography

def get_ch2_content():
    return r"""
    <section id="ch2" class="chapter-container">
      <span class="chapter-number">Chapter 02</span>
      <h1 class="chapter-title">Newton's Laws & Complex Friction Dynamics</h1>

      <div class="card-box tip-card">
        <div class="card-header-tip">[MENTOR STRATEGY NOTE] The Reality of Friction in JEE Advanced</div>
        <p><strong>Listen to me very carefully:</strong> More students lose marks in friction than almost any other Class 11 mechanics topic. Why? Because you've been conditioned to write $f_s = \mu_s N$ the moment you see a block on a surface. That formula is <em>not</em> static friction—it is only the maximum possible breaking threshold! Static friction is a smart, self-adjusting reaction force. It only gives the exact amount needed to prevent slipping, nothing more.</p>
        <p><strong>The Golden Rule for Multi-Block Problems:</strong> Never guess which surface slips first. Assume all blocks move together as a single composite mass, compute the required acceleration, and check if any interface exceeds its friction ceiling. If one breaks, that's your first slipping surface!</p>
      </div>

      <h2 class="section-title">2.1 First-Principles Foundations: Inertial Frames & Friction Hierarchies</h2>

      <p>Newton's Second Law ($\sum \mathbf{F} = m\mathbf{a}$) is valid <em>only</em> in an inertial reference frame (a frame that is unaccelerated relative to the distant stars). When you decide to solve a problem from the perspective of an accelerating frame $S'$ (like a wedge sliding down an incline or an elevator with snapping cables), Newton's Second Law breaks unless you pay a mathematical tax: <strong>the pseudo-force</strong>.</p>

      $$\mathbf{F}_{\text{pseudo}} = -m \mathbf{a}_0$$
      <p>where $\mathbf{a}_0$ is the acceleration of your reference frame relative to the ground. Notice that minus sign! It means the pseudo-force always acts <strong>strictly opposite</strong> to the frame's acceleration vector. It acts uniformly on every atom, so its line of action passes directly through the Center of Mass (COM).</p>

      <h3 class="sub-title">2.1.1 The Multi-Block Friction Hierarchy Algorithm</h3>
      <p>Consider two blocks stacked on top of each other: block $A$ of mass $m_A$ resting on block $B$ of mass $m_B$, which sits on a frictionless floor. A horizontal force $F$ is applied to block $B$. The coefficient of static friction between $A$ and $B$ is $\mu_s$.</p>

      <!-- SVG Diagram 2.1: Multi-Block Friction Stack -->
      <div class="diagram-container">
                <svg class="diagram-svg" width="600" height="240" viewBox="0 0 600 240">
          <defs>
            <marker id="arrow-ch2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626"/>
            </marker>
          </defs>
          <line x1="60" y1="200" x2="540" y2="200" stroke="#0f172a" stroke-width="3" />
          <rect x="180" y="130" width="240" height="70" fill="#f1f5f9" stroke="#0f172a" stroke-width="2.5" />
          <text x="270" y="172" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">Block B (m_B)</text>
          <rect x="230" y="60" width="140" height="70" fill="#e2e8f0" stroke="#0f172a" stroke-width="2.5" />
          <text x="275" y="102" font-family="sans-serif" font-size="16" font-weight="bold" fill="#0f172a">Block A (m_A)</text>
          <line x1="420" y1="165" x2="500" y2="165" stroke="#dc2626" stroke-width="4" marker-end="url(#arrow-ch2)" />
          <text x="445" y="152" font-family="sans-serif" font-size="14" font-weight="bold" fill="#dc2626">Force F</text>
          <line x1="230" y1="130" x2="370" y2="130" stroke="#059669" stroke-width="3" stroke-dasharray="4,4" />
          <text x="110" y="125" font-family="sans-serif" font-size="12" font-weight="bold" fill="#059669">Friction Plane (μ_s)</text>
          <text x="210" y="225" font-family="sans-serif" font-size="12" fill="#64748b">Smooth Floor (Zero Friction)</text>
        </svg>
        <div class="diagram-caption">Figure 2.1: Two-block stacked system. Force applied to bottom block B. Friction on A is the sole driving force for A.</div>
      </div>

      <p>Here is the 3-step foolproof algorithm to solve this in under 60 seconds:</p>
      <ol style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Find the Maximum Acceleration Block A Can Sustain Without Slipping:</strong>
          What accelerates block $A$? Only static friction from block $B$! Gravity and normal reaction are vertical.
          $$f_{s,\max} = \mu_s m_A g \implies a_{A,\max} = \frac{f_{s,\max}}{m_A} = \mathbf{\mu_s g}$$
          Notice something incredible: the maximum acceleration block $A$ can ever have is purely $\mu_s g$, completely independent of its mass!
        </li>
        <li><strong>Compute the Common Critical Force $F_c$:</strong>
          If both blocks accelerate together at this threshold acceleration $a_{A,\max}$, the required pulling force on the composite system $(m_A + m_B)$ is:
          $$F_c = (m_A + m_B) a_{A,\max} = \mathbf{(m_A + m_B)\mu_s g}$$
        </li>
        <li><strong>Apply the Decision Tree:</strong>
          <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
            <li>If $F \le F_c$: <strong>No slipping occurs.</strong> Both blocks move together with common acceleration:
            $$a_A = a_B = \frac{F}{m_A + m_B}$$
            The actual friction acting between them is: $f_s = m_A a_A = \frac{m_A}{m_A + m_B}F < \mu_s m_A g$.</li>
            <li>If $F > F_c$: <strong>Relative slipping occurs!</strong> Kinetic friction $f_k = \mu_k m_A g$ acts between the blocks:
            $$a_A = \frac{f_k}{m_A} = \mu_k g = \text{constant}$$
            $$a_B = \frac{F - f_k}{m_B} = \frac{F - \mu_k m_A g}{m_B}$$
            The relative acceleration is $a_{rel} = a_B - a_A$.</li>
          </ul>
        </li>
      </ol>

      <h3 class="sub-title">2.1.2 Wedge-Block Kinematic Constraints & String Differentiation</h3>
      <p>In multi-body constrained mechanics, bodies cannot penetrate each other or pull away while remaining in contact. This geometric restriction gives rise to <strong>kinematic constraint relations</strong> that provide the vital missing algebraic equations needed to match the number of unknown dynamic variables.</p>
      <p><strong>The Virtual Work Method for Pulley Systems:</strong></p>
      <p>For any system of ideal massless inextensible strings connecting blocks through light frictionless pulleys, the tension forces are internal to the string-pulley network. Since the length of an inextensible string is strictly constant, the total virtual work done by all string tensions during any virtual displacement is identically zero:</p>
      $$\sum \mathbf{T}_i \cdot \Delta \mathbf{r}_i = 0 \implies \sum \mathbf{T}_i \cdot \mathbf{v}_i = 0 \implies \sum \mathbf{T}_i \cdot \mathbf{a}_i = 0$$
      <p>This single dot-product relation allows you to establish the exact ratio of block accelerations across any multi-pulley cascade without ever setting up laborious coordinate origin systems!</p>
      <p><strong>Wedge-Block Surface Normals:</strong></p>
      <p>When a block $A$ slides on a movable wedge $B$, their relative displacement must lie strictly parallel to the inclined contact face. If the wedge accelerates horizontally with acceleration $A_B$ to the left, the normal acceleration constraint between them requires that the velocity and acceleration components perpendicular to the contact interface must match perfectly:</p>
      $$(\mathbf{a}_A - \mathbf{a}_B) \cdot \hat{\mathbf{n}} = 0$$
      <p>Choosing coordinate axes aligned with the incline face immediately simplifies the equations of motion in the non-inertial frame of the wedge by confining relative motion to a single axis.</p>

      <h2 class="section-title">2.2 Master Formula Summary Table: Dynamics & Friction</h2>
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
              <td><strong>Static Friction Inequality</strong></td>
              <td class="formula-math">$$0 \le f_s \le \mu_s N$$</td>
              <td><span class="validity-tag">No relative motion between surfaces</span></td>
              <td><span class="invalidity-tag">Setting $f_s = \mu_s N$ unconditionally before checking force equilibrium</span></td>
            </tr>
            <tr>
              <td><strong>Kinetic Friction Law</strong></td>
              <td class="formula-math">$$f_k = \mu_k N \quad (\text{opposes relative velocity } \mathbf{v}_{rel})$$</td>
              <td><span class="validity-tag">Active surface sliding ($v_{rel} > 0$)</span></td>
              <td><span class="invalidity-tag">Making friction oppose laboratory velocity instead of relative contact velocity</span></td>
            </tr>
            <tr>
              <td><strong>Non-Inertial Pseudo-Force</strong></td>
              <td class="formula-math">$$\mathbf{F}_{\text{pseudo}} = -m \mathbf{a}_0$$</td>
              <td><span class="validity-tag">Reference frame translating with acceleration $\mathbf{a}_0$</span></td>
              <td><span class="invalidity-tag">Forgetting to reverse direction of frame acceleration vector</span></td>
            </tr>
            <tr>
              <td><strong>Incline Normal Reaction</strong></td>
              <td class="formula-math">$$N = mg\cos\theta$$</td>
              <td><span class="validity-tag">Static or sliding on flat plane of angle $\theta$</span></td>
              <td><span class="invalidity-tag">Assuming $N = mg$ on an inclined plane</span></td>
            </tr>
            <tr>
              <td><strong>Angle of Repose</strong></td>
              <td class="formula-math">$$\tan\theta_r = \mu_s$$</td>
              <td><span class="validity-tag">Block on incline under gravity alone</span></td>
              <td><span class="invalidity-tag">Applying $\tan\theta = \mu_s$ when external pulling or pushing forces act</span></td>
            </tr>
            <tr>
              <td><strong>Kinematic String Constraint</strong></td>
              <td class="formula-math">$$\sum T_i \cdot x_i = 0 \implies \sum T_i \cdot a_i = 0$$</td>
              <td><span class="validity-tag">Inextensible light strings & ideal frictionless pulleys</span></td>
              <td><span class="invalidity-tag">Ignoring string slacking ($T < 0$) when one block out-accelerates another</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">2.3 The Forensic Negative-Marking Trap Matrix (10 Alerts)</h2>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.1] The $f_s = \mu_s N$ Knee-Jerk Fallacy</div>
        <p><strong>The Trap:</strong> A 5 kg block sits on a rough table with $\mu_s = 0.5$. A horizontal force of $F = 10\text{ N}$ is applied. Students compute friction as $f = \mu_s N = 0.5 \times 50 = 25\text{ N}$ and conclude the block accelerates backward!</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Static friction NEVER creates motion from rest. The value $\mu_s N = 25\text{ N}$ is the <em>maximum threshold</em>. Because applied force $F = 10\text{ N} < 25\text{ N}$, static friction adjusts to exactly balance the applied force: $f_s = 10\text{ N}$, and the block remains in static equilibrium ($a = 0$).</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.2] Friction Opposes Motion vs. Friction Opposes RELATIVE Motion</div>
        <p><strong>The Trap:</strong> Assuming friction always opposes the velocity of an object relative to the ground.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Friction opposes <strong>relative slipping between contact surfaces</strong>, NOT ground motion! When you walk, friction from the ground pushes you FORWARD. When block $A$ sits on accelerating block $B$, friction on $A$ acts FORWARD to accelerate it. If friction opposed ground motion, walking would be physically impossible.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.3] Normal Force on an Accelerating Incline</div>
        <p><strong>The Trap:</strong> Assuming normal force on an inclined plane is always $N = mg\cos\theta$, even when the wedge is accelerating horizontally with acceleration $a_0$.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> In the non-inertial frame of the wedge accelerating rightward, a pseudo-force $m a_0$ acts leftward. Perpendicular force balance yields: $N = mg\cos\theta + m a_0\sin\theta$. Normal force increases or decreases depending on the direction of wedge acceleration!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.4] Tension Discontinuity Across Massive Pulleys</div>
        <p><strong>The Trap:</strong> Assuming string tension is identical on both sides of a massive or rough pulley ($T_1 = T_2$).</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> If a pulley has mass $M$ and radius $R$ (moment of inertia $I$), net torque is required to give it angular acceleration: $(T_1 - T_2)R = I\alpha$. Therefore, $T_1 \ne T_2$! Tension is constant across a pulley if and only if the pulley is strictly massless and frictionless.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.5] Contact Separation Criterion ($N = 0$)</div>
        <p><strong>The Trap:</strong> Attempting to find when a block flies off a curved surface or wedge by setting acceleration to zero.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Contact loss between rigid bodies is governed strictly by the normal reaction vanishing: $N \to 0$. Surfaces can only push, they cannot pull ($N \ge 0$). The moment $N = 0$, the body detaches and enters free projectile flight.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.6] Pseudo-Force in Rotating Frames</div>
        <p><strong>The Trap:</strong> Using only the centrifugal pseudo-force $-m(\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r}))$ when analyzing a particle moving inside a rotating reference frame.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> If a particle moves with relative velocity $\mathbf{v}_{rel}$ inside a rotating frame, you MUST include the <strong>Coriolis Force</strong>: $\mathbf{F}_{\text{coriolis}} = -2m(\boldsymbol{\omega}\times\mathbf{v}_{rel})$. Neglecting Coriolis leads to massive errors in Bead-on-Rotating-Rod problems.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.7] Virtual Work String Constraint Differentiation Signs</div>
        <p><strong>The Trap:</strong> Confusing positive and negative signs when applying $\sum \mathbf{T}\cdot\mathbf{a} = 0$ to complex multi-pulley systems.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Choose an unambiguous positive direction for each block. Compute the work done by internal tension: $\sum T_i x_i = 0$. Differentiating twice yields $\sum T_i a_i = 0$. If tension and acceleration are in the same direction, the dot product is positive; if opposite, it is negative.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.8] Conical Pendulum Critical Speed Limit</div>
        <p><strong>The Trap:</strong> Assuming a conical pendulum can spin at any arbitrary slow angular velocity $\omega$ and still maintain a conical orbit.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> Tension components give $T\cos\theta = mg$ and $T\sin\theta = m\omega^2 L\sin\theta$. This requires $\cos\theta = \frac{g}{\omega^2 L}$. Because $\cos\theta \le 1$, a conical orbit is physically impossible unless $\omega > \sqrt{g/L}$. For $\omega \le \sqrt{g/L}$, the string hangs purely vertically ($\theta = 0$).</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.9] Kinetic Friction Velocity Independence</div>
        <p><strong>The Trap:</strong> Assuming kinetic friction increases drastically as sliding velocity increases.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> In Coulomb's model for JEE, $f_k = \mu_k N$ is independent of sliding speed and apparent contact area. It remains constant whether sliding at $1\text{ m/s}$ or $10\text{ m/s}$ (neglecting aerodynamic heating).</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 2.10] Equilibrium Under Three Non-Parallel Forces</div>
        <p><strong>The Trap:</strong> Balancing three non-parallel forces on a rigid body without checking whether their lines of action intersect at a single common point.</p>
        <div class="trap-remedy"><strong>The Definitive Rule:</strong> For a rigid body to be in rotational equilibrium ($\sum \boldsymbol{\tau} = \mathbf{0}$) under three non-parallel coplanar forces, the three force vectors <strong>MUST be concurrent</strong>—their lines of action must intersect at the exact same spatial point!</div>
      </div>

      <h2 class="section-title">2.4 Dissected JEE Advanced Previous Year Questions (PYQs)</h2>

      <!-- PYQ 2.1 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">JEE Advanced 2020 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Very Hard • Three-Block Friction Stack Hierarchy</span>
        </div>
        <div class="pyq-question">
          Three blocks $A, B,$ and $C$ of masses $m_A = 1\text{ kg}, m_B = 2\text{ kg},$ and $m_C = 3\text{ kg}$ are stacked on top of each other. $A$ sits on $B$, $B$ sits on $C$, and $C$ rests on a frictionless horizontal floor. The coefficient of static friction between $A$ and $B$ is $\mu_1 = 0.6$, and between $B$ and $C$ is $\mu_2 = 0.2$. A horizontal force $F$ is applied to the middle block $B$. Find (a) the maximum force $F_{\max}$ such that all three blocks move together without slipping, and (b) the accelerations of all three blocks when $F = 30\text{ N}$. Take $g = 10\text{ m/s}^2$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Determine Maximum Acceleration for Each Interface:</strong></p>
          <p>For Block $A$ (driven purely by friction from $B$):</p>
          $$f_{1,\max} = \mu_1 m_A g = 0.6(1)(10) = 6\text{ N} \implies a_{A,\max} = \frac{f_{1,\max}}{m_A} = \frac{6}{1} = \mathbf{6\text{ m/s}^2}$$
          <p>For Block $C$ (driven purely by friction from $B$):</p>
          <p>Normal force on interface between $B$ and $C$ carries mass of $A$ and $B$: $N_2 = (m_A + m_B)g = (1 + 2)(10) = 30\text{ N}$.</p>
          $$f_{2,\max} = \mu_2 N_2 = 0.2(30) = 6\text{ N}$$
          <p>Block $C$ has mass $m_C = 3\text{ kg}$. The maximum acceleration friction can impart to $C$ is:</p>
          $$a_{C,\max} = \frac{f_{2,\max}}{m_C} = \frac{6}{3} = \mathbf{2\text{ m/s}^2}$$
          <p><strong>Step 2: Find Weakest Link for Co-Movement:</strong></p>
          <p>Notice that $a_{C,\max} = 2\text{ m/s}^2 < a_{A,\max} = 6\text{ m/s}^2$. Therefore, block $C$ is the <strong>weakest link</strong>! The interface between $B$ and $C$ will slip long before $A$ slips on $B$.</p>
          <p>The maximum common acceleration for all three blocks to move together is $a_{\text{common}} = 2\text{ m/s}^2$.</p>
          $$F_{\max} = (m_A + m_B + m_C) a_{\text{common}} = (1 + 2 + 3)(2) = 6 \times 2 = \mathbf{12\text{ Newtons}}$$
          <p><strong>Step 3: Analyze System at $F = 30\text{ N}$ ($F > 12\text{ N}$):</strong></p>
          <p>Because $F = 30\text{ N} > 12\text{ N}$, slipping occurs between $B$ and $C$. Kinetic friction acts on $C$:</p>
          $$f_2 = f_{2,\max} = 6\text{ N} \implies a_C = \frac{6}{3} = \mathbf{2.0\text{ m/s}^2}$$
          <p>Now check whether $A$ slips on $B$. Treat $(A + B)$ as a combined sub-system of mass $(1 + 2) = 3\text{ kg}$ subject to pulling force $F = 30\text{ N}$ forward and backward friction $f_2 = 6\text{ N}$ from $C$:</p>
          $$a_{AB} = \frac{F - f_2}{m_A + m_B} = \frac{30 - 6}{1 + 2} = \frac{24}{3} = 8\text{ m/s}^2$$
          <p>Compare $a_{AB} = 8\text{ m/s}^2$ with $a_{A,\max} = 6\text{ m/s}^2$. Since $8 > 6$, <strong>Block $A$ ALSO slips on Block $B$!</strong></p>
          <p>Therefore, kinetic friction acts at both interfaces: $f_1 = 6\text{ N}$ and $f_2 = 6\text{ N}$.</p>
          $$a_A = \frac{f_1}{m_A} = \frac{6}{1} = \mathbf{6.0\text{ m/s}^2}$$
          $$a_B = \frac{F - f_1 - f_2}{m_B} = \frac{30 - 6 - 6}{2} = \frac{18}{2} = \mathbf{9.0\text{ m/s}^2}$$
          $$a_C = \frac{f_2}{m_C} = \frac{6}{3} = \mathbf{2.0\text{ m/s}^2}$$
        </div>
      </div>

      <!-- PYQ 2.2 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">JEE Advanced 2015 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Hard • Movable Wedge & Non-Inertial Pseudo-Frames</span>
        </div>
        <div class="pyq-question">
          A smooth wedge of mass $M = 4\text{ kg}$ with incline angle $\theta = 37^\circ$ rests on a smooth horizontal floor. A block of mass $m = 1\text{ kg}$ is placed on the inclined face of the wedge and released from rest. Determine (a) the horizontal acceleration $A$ of the wedge, and (b) the acceleration $a_{rel}$ of the block relative to the wedge. Take $g = 10\text{ m/s}^2, \sin 37^\circ = 0.6, \cos 37^\circ = 0.8$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Isolate Wedge in the Laboratory Frame:</strong></p>
          <p>The only horizontal force acting on the wedge is the horizontal component of the normal reaction $N$ from the block directed leftward:</p>
          $$N\sin\theta = M A \implies N = \frac{M A}{\sin\theta}$$
          <p><strong>Step 2: Analyze Block in Wedge Reference Frame (Accelerating Leftward at $A$):</strong></p>
          <p>In this non-inertial frame, a pseudo-force $m A$ acts rightward on the block.</p>
          <p>Because the block remains in contact with the incline, acceleration perpendicular to the incline is zero:</p>
          $$N + m A \sin\theta = m g \cos\theta \implies N = m g \cos\theta - m A \sin\theta$$
          <p><strong>Step 3: Equate Normal Reaction Expressions and Solve for $A$:</strong></p>
          $$\frac{M A}{\sin\theta} = m g \cos\theta - m A \sin\theta$$
          $$M A = m g \sin\theta\cos\theta - m A \sin^2\theta \implies A(M + m\sin^2\theta) = m g \sin\theta\cos\theta$$
          $$A = \frac{m g \sin\theta\cos\theta}{M + m\sin^2\theta}$$
          <p>Substitute values: $M = 4, m = 1, g = 10, \sin 37^\circ = 0.6, \cos 37^\circ = 0.8$:</p>
          $$A = \frac{1(10)(0.6)(0.8)}{4 + 1(0.6^2)} = \frac{4.8}{4 + 0.36} = \frac{4.8}{4.36} = \frac{480}{436} = \mathbf{\frac{120}{109}\text{ m/s}^2} \approx \mathbf{1.101\text{ m/s}^2}$$
          <p><strong>Step 4: Compute Relative Acceleration Along the Incline:</strong></p>
          <p>Forces along the incline in the wedge frame:</p>
          $$m a_{rel} = m g \sin\theta + m A \cos\theta \implies a_{rel} = g\sin\theta + A\cos\theta$$
          $$a_{rel} = 10(0.6) + \left(\frac{120}{109}\right)(0.8) = 6 + \frac{96}{109} = \frac{654 + 96}{109} = \mathbf{\frac{750}{109}\text{ m/s}^2} \approx \mathbf{6.881\text{ m/s}^2}$$
        </div>
      </div>

      <!-- PYQ 2.3 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">JEE Advanced 2018 • Paper 2</span>
          <span class="pyq-difficulty">Difficulty: Hard • Constrained Pulley System Acceleration</span>
        </div>
        <div class="pyq-question">
          In a pulley system, block $A$ of mass $m_A = 2\text{ kg}$ is suspended from a movable pulley, while block $B$ of mass $m_B = 6\text{ kg}$ rests on a smooth horizontal table connected via light inextensible strings. Find the downward acceleration of block $A$. Take $g = 10\text{ m/s}^2$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Establish String Constraint Relation:</strong></p>
          <p>Using virtual work: let $x_A$ be downward displacement of $A$, and $x_B$ be horizontal displacement of $B$.</p>
          <p>Because block $A$ is supported by two vertical segments of the loop passing around its movable pulley:</p>
          $$2 T x_A - T x_B = 0 \implies x_B = 2 x_A \implies a_B = 2 a_A$$
          <p><strong>Step 2: Write Dynamic Equations:</strong></p>
          <p>For block $B$ on the frictionless table: $T = m_B a_B = m_B (2 a_A) = 2 m_B a_A$.</p>
          <p>For block $A$ moving downward: $m_A g - 2T = m_A a_A$.</p>
          <p><strong>Step 3: Solve for $a_A$:</strong></p>
          $$m_A g - 2(2 m_B a_A) = m_A a_A \implies m_A g = (m_A + 4 m_B) a_A$$
          $$a_A = \frac{m_A g}{m_A + 4 m_B} = \frac{2(10)}{2 + 4(6)} = \frac{20}{2 + 24} = \frac{20}{26} = \mathbf{\frac{10}{13}\text{ m/s}^2} \approx \mathbf{0.769\text{ m/s}^2}$$
        </div>
      </div>

      <h2 class="section-title">2.5 High-Caliber Practice Challenge Problems & Complete Solutions</h2>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 2.1] Critical Incline Separation Under Horizontal Acceleration</div>
        <p>A small block rests on a smooth wedge of angle $\theta = 45^\circ$. The wedge is accelerated horizontally leftward with acceleration $a$. Find the critical acceleration $a_c$ at which the block loses contact with the wedge face.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>In the wedge frame, pseudo-force $m a$ acts rightward (into the incline) if accelerated leftward. But if the wedge accelerates rightward, pseudo-force acts leftward (lifting the block off the incline):</p>
            $$N = m g \cos\theta - m a \sin\theta$$
            <p>Separation occurs when $N = 0$:</p>
            $$m g \cos\theta = m a_c \sin\theta \implies a_c = g\cot\theta$$
            <p>For $\theta = 45^\circ$, $\cot 45^\circ = 1$:</p>
            $$a_c = g = \mathbf{10.0\text{ m/s}^2 \text{ rightward}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 2.2] Hanging Chain on Rough Table Critical Fraction</div>
        <p>A uniform heavy chain of total length $L$ lies on a rough horizontal table with a fraction $\eta$ hanging over the edge. The static coefficient of friction between chain and table is $\mu_s = 0.25$. Find the maximum overhang fraction $\eta_{\max}$ for which the chain remains at rest without slipping off.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Let total mass of chain be $M$. Hanging mass: $m_{hang} = \eta M$. Table mass: $m_{table} = (1 - \eta)M$.</p>
            <p>Downward pulling force of hanging part: $F_{pull} = (\eta M)g$.</p>
            <p>Maximum static friction on table part: $f_{s,\max} = \mu_s N = \mu_s (1 - \eta)Mg$.</p>
            <p>At equilibrium limit: $F_{pull} = f_{s,\max}$:</p>
            $$\eta M g = \mu_s (1 - \eta) M g \implies \eta = \mu_s - \mu_s \eta \implies \eta(1 + \mu_s) = \mu_s$$
            $$\eta_{\max} = \frac{\mu_s}{1 + \mu_s} = \frac{0.25}{1 + 0.25} = \frac{0.25}{1.25} = \mathbf{\frac{1}{5} = 0.20 \text{ (20% of total length)}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 2.3] Friction-Driven Conveyor Belt Launch Time</div>
        <p>A package of mass $m = 20\text{ kg}$ is dropped with zero initial speed onto a long conveyor belt moving at constant horizontal speed $v = 4\text{ m/s}$. The kinetic coefficient of friction is $\mu_k = 0.2$. Find (a) the time $t_{slip}$ during which the package slips on the belt, and (b) the distance $s_{package}$ the package moves relative to the floor before attaining belt speed. Take $g = 10\text{ m/s}^2$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>While slipping, kinetic friction pushes the package forward:</p>
            $$f_k = \mu_k m g \implies a = \mu_k g = (0.2)(10) = 2.0\text{ m/s}^2$$
            <p>Time to accelerate from $u = 0$ to $v = 4\text{ m/s}$:</p>
            $$t_{slip} = \frac{v}{a} = \frac{4}{2} = \mathbf{2.0\text{ seconds}}$$
            <p>Distance traveled relative to the ground:</p>
            $$s_{package} = \frac{v^2}{2a} = \frac{4^2}{2(2)} = \frac{16}{4} = \mathbf{4.0\text{ meters}}$$
            <p>Note: During this same time, the belt traveled $s_{belt} = v \cdot t_{slip} = 4 \times 2 = 8\text{ m}$. The relative skid mark on the belt is $8 - 4 = 4\text{ meters}$!</p>
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 2.4] Double-Wedge Incline Acceleration Ratio</div>
        <p>A wedge $B$ of mass $M$ with angle $\theta$ slides on a smooth table, while a smaller wedge $A$ of mass $m$ slides on wedge $B$. Neglecting all friction, find the acceleration of wedge $B$ when the system is released from rest.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p><strong>Step 1: Horizontal Equation of Motion for Wedge B:</strong></p>
            <p>Let wedge $B$ accelerate leftward with acceleration $A_B$. The normal reaction $N$ from block $A$ acts perpendicular to the inclined face of wedge $B$. The horizontal component of normal force accelerates wedge $B$:</p>
            $$N\sin\theta = M A_B \implies N = \frac{M A_B}{\sin\theta}$$
            <p><strong>Step 2: Dynamics of Block A in Non-Inertial Frame of Wedge B:</strong></p>
            <p>In the reference frame of wedge $B$ accelerating leftward at $A_B$, block $A$ experiences a fictitious pseudo-force $m A_B$ directed rightward. Resolving forces perpendicular to the incline face where relative acceleration is zero:</p>
            $$N + m A_B \sin\theta = m g \cos\theta \implies N = m(g\cos\theta - A_B\sin\theta)$$
            <p><strong>Step 3: Equating Normal Reactions to Solve Acceleration:</strong></p>
            $$m(g\cos\theta - A_B\sin\theta) = \frac{M A_B}{\sin\theta} \implies m g\sin\theta\cos\theta - m A_B\sin^2\theta = M A_B$$
            $$A_B(M + m\sin^2\theta) = m g\sin\theta\cos\theta \implies A_B = \mathbf{\frac{m g \sin\theta\cos\theta}{M + m\sin^2\theta}}$$
            <p><strong>Step 4: Numerical Evaluation for $M = 3m$ and $\theta = 45^\circ$:</strong></p>
            <p>Since $\sin 45^\circ = \cos 45^\circ = \frac{1}{\sqrt{2}}$, we have $\sin\theta\cos\theta = \frac{1}{2}$ and $\sin^2 45^\circ = \frac{1}{2}$:</p>
            $$A_B = \frac{m g (1/2)}{3m + m(1/2)} = \frac{0.5 g}{3.5} = \mathbf{\frac{g}{7}} \approx 1.429\text{ m/s}^2$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 2.5] Pivoting Rod Normal Force Sign Reversal</div>
        <p>A slender uniform rod of mass $M$ and length $L$ rests against a smooth vertical wall and a smooth floor at angle $\theta$ to the horizontal. As the rod slides down, show that the normal reaction from the wall vanishes and find the angle $\theta_{sep}$ at which contact with the wall is lost.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Let horizontal position of COM be $x_{cm} = \frac{L}{2}\cos\theta$.</p>
            <p>Horizontal acceleration: $\ddot{x}_{cm} = -\frac{L}{2}(\ddot{\theta}\sin\theta + \dot{\theta}^2\cos\theta)$.</p>
            <p>Horizontal force from wall: $N_{wall} = M \ddot{x}_{cm}$.</p>
            <p>By energy conservation: $Mg\frac{L}{2}(1 - \sin\theta) = \frac{1}{2}I_O \dot{\theta}^2 = \frac{1}{6}ML^2 \dot{\theta}^2$.</p>
            <p>Setting $N_{wall} = 0$ yields the classic analytical threshold:</p>
            $$\sin\theta_{sep} = \frac{2}{3} \implies \theta_{sep} = \arcsin(2/3) \approx \mathbf{41.81^\circ}$$
          </div>
        </details>
      </div>
    </section>
    """

if __name__ == "__main__":
    c = get_ch2_content()
    print("Chapter 2 regenerated successfully. Length:", len(c))
