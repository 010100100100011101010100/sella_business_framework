# Chapter 6 Generator: Gravitation & Oscillatory Motion / SHM
# Conversational Kota Mentor Voice • Zero Emojis • Modern Typography

def get_ch6_content():
    return r"""
    <section id="ch6" class="chapter-container">
      <span class="chapter-number">Chapter 06</span>
      <h1 class="chapter-title">Gravitation & Oscillatory Motion (SHM)</h1>

      <div class="card-box tip-card">
        <div class="card-header-tip">[MENTOR STRATEGY NOTE] Where Gravitation Meets Harmonics</div>
        <p><strong>Listen up, aspirants:</strong> Gravitation and Simple Harmonic Motion (SHM) are intimately linked by nature's inverse-square and linear force fields. In JEE Advanced, the examiners almost never ask a simple "plug $T = 2\pi\sqrt{l/g}$" question. They test physical disc pendulums pivoted at their rim, off-center Earth tunnels where harmonic restoring forces survive along oblique chords, orbital transfers via instantaneous rocket impulses (Vis-Viva), and two-block spring oscillators where reduced mass is mandatory.</p>
        <p><strong>The Golden Truth:</strong> Potential is an integral; field is a derivative. Potential at the center of the Earth is $-1.5 GM/R$, NOT zero. And a satellite fired with reverse brakes actually speeds up as it drops to a lower orbit. Let's master the mathematical mechanics so you dominate Paper 1 and Paper 2.</p>
      </div>

      <h2 class="section-title">6.1 First-Principles Foundations: Gravitational Fields & Harmonics</h2>

      <h3 class="sub-title">6.1.1 Continuous Body Gravitational Potentials & Fields</h3>
      <p>Think of gravitational potential $V$ like altitude on a landscape. Gravitational field $\mathbf{E}$ is simply how steep that slope is, pulling naturally downhill toward lower potential: $\mathbf{E} = -\frac{dV}{dr}\hat{\mathbf{r}}$. Because gravity only pulls things together, we agree by universal convention to set our zero-reference point infinitely far away: $V(\infty) = 0$. Anywhere closer to a mass, you are sitting down inside a gravity well, which is why gravitational potential is always negative.</p>

      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Uniform Thin Spherical Shell of Mass $M$ and Radius $R$:</strong>
          <p>Inside a hollow spherical shell, the gravitational pull from all sides cancels out completely. The field is zero everywhere inside, so the potential is flat and constant, equal to its value on the surface:</p>
          $$\text{Inside } (r < R): \quad E(r) = 0, \quad V(r) = -\frac{GM}{R} = \text{constant}$$
          <p>Outside the shell, it pulls exactly as if all its mass were concentrated at the center point:</p>
          $$\text{Outside } (r \ge R): \quad E(r) = \frac{GM}{r^2}, \quad V(r) = -\frac{GM}{r}$$
        </li>
        <li><strong>Uniform Solid Sphere of Mass $M$ and Radius $R$ (Volume density $\rho = \frac{3M}{4\pi R^3}$):</strong>
          <p>As you dig deeper into a uniform solid planet, only the sphere of mass beneath your feet exerts net gravity:</p>
          $$\text{Inside } (r \le R): \quad E(r) = \frac{G M(r)}{r^2} = \mathbf{\frac{GM r}{R^3}}$$
          <p>Integrating the field inward from the surface gives the potential at any internal radius $r$:</p>
          $$V(r) = -\frac{GM}{2R^3}\left(3R^2 - r^2\right)$$
          <p>At the exact center ($r = 0$), the field is zero because mass pulls equally from all directions, but potential reaches its deepest negative pit:</p>
          $$V(0) = -\frac{3}{2}\frac{GM}{R} = \mathbf{-1.5 \frac{GM}{R}}$$
        </li>
        <li><strong>Gravitational Self-Energy ($U_{self}$):</strong>
          <p>This is simply the total work done by gravity in pulling scattered cosmic dust together from infinity to assemble the object:</p>
          $$\text{Thin Spherical Shell: } U_{self} = \mathbf{-\frac{GM^2}{2R}}$$
          $$\text{Solid Sphere: } U_{self} = \mathbf{-\frac{3}{5}\frac{GM^2}{R}}$$
        </li>
      </ul>

      <!-- SVG Diagram 6.1: Gravitational Orbits & Compound Pendulum -->
      <div class="diagram-container">
                <svg class="diagram-svg" width="600" height="260" viewBox="0 0 600 260">
          <defs>
            <marker id="arrow-ch6" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#dc2626"/>
            </marker>
          </defs>
          <!-- Left: Elliptical Kepler Orbit -->
          <ellipse cx="160" cy="130" rx="120" ry="75" fill="none" stroke="#b45309" stroke-width="2.5" />
          <!-- Sun at Focus -->
          <circle cx="110" cy="130" r="14" fill="#f59e0b" stroke="#b45309" stroke-width="2" />
          <text x="100" y="110" font-family="sans-serif" font-size="11" font-weight="bold" fill="#b45309">Sun (Focus)</text>

          <!-- Perihelion Point -->
          <circle cx="40" cy="130" r="6" fill="#0284c7" />
          <line x1="40" y1="130" x2="40" y2="70" stroke="#dc2626" stroke-width="3" marker-end="url(#arrow-ch6)" />
          <text x="45" y="65" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">v_p (max)</text>
          <text x="15" y="150" font-family="sans-serif" font-size="11" fill="#0f172a">Perihelion r_p</text>

          <!-- Aphelion Point -->
          <circle cx="280" cy="130" r="6" fill="#0284c7" />
          <line x1="280" y1="130" x2="280" y2="95" stroke="#dc2626" stroke-width="2.5" />
          <text x="285" y="90" font-family="sans-serif" font-size="11" font-weight="bold" fill="#dc2626">v_a (min)</text>
          <text x="245" y="150" font-family="sans-serif" font-size="11" fill="#0f172a">Aphelion r_a</text>

          <line x1="40" y1="130" x2="280" y2="130" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4" />
          <text x="135" y="145" font-family="sans-serif" font-size="11" fill="#64748b">Major Axis 2a</text>

          <!-- Right: Compound Pendulum Geometry -->
          <line x1="460" y1="30" x2="460" y2="230" stroke="#0f172a" stroke-width="4" stroke-linecap="round" />
          <!-- Pivot O -->
          <circle cx="460" cy="50" r="6" fill="#dc2626" />
          <text x="475" y="55" font-family="sans-serif" font-size="12" font-weight="bold" fill="#dc2626">Pivot O</text>

          <!-- COM G -->
          <circle cx="460" cy="120" r="6" fill="#047857" />
          <text x="475" y="125" font-family="sans-serif" font-size="12" font-weight="bold" fill="#047857">COM (d from O)</text>

          <!-- Center of Oscillation S -->
          <circle cx="460" cy="180" r="6" fill="#b45309" />
          <text x="475" y="185" font-family="sans-serif" font-size="12" font-weight="bold" fill="#b45309">Center of Osc. S</text>

          <!-- Equiv Length bracket -->
          <line x1="430" y1="50" x2="430" y2="180" stroke="#0f172a" stroke-width="2" />
          <polyline points="435,55 430,50 425,55" fill="none" stroke="#0f172a" stroke-width="2" />
          <polyline points="435,175 430,180 425,175" fill="none" stroke="#0f172a" stroke-width="2" />
          <text x="345" y="120" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">L = d + k²/d</text>
        </svg>
        <div class="diagram-caption">Figure 6.1: (Left) Keplerian elliptical orbit parameters and Vis-Viva conservation. (Right) Compound physical pendulum showing conjugate centers $O$ and $S$.</div>
      </div>

      <h3 class="sub-title">6.1.2 Orbital Mechanics & The Vis-Viva Energy Equation</h3>
      <p>Every closed gravitational orbit is an ellipse with the central star sitting at one focus (Kepler's First Law). Because gravity pulls directly toward the star, it exerts zero torque ($\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}_g = \mathbf{0}$). With zero torque, angular momentum $\mathbf{L} = \mathbf{r}\times m\mathbf{v}$ is strictly conserved throughout the orbit. This constant angular momentum is the physical reason planets sweep out equal areas in equal times (Kepler's Second Law: $\frac{dA}{dt} = \frac{L}{2m}$).</p>
      <p>The <strong>Vis-Viva Equation</strong> is simply conservation of energy in its most practical form. Instead of recalculating kinetic and potential energy each time, it directly links speed $v$, distance from the star $r$, and the size of the orbit $a$ in one clean formula:</p>
      $$v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)$$
      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Circular Orbit ($a = r$):</strong> Speed is constant everywhere: $v_{circ} = \sqrt{\frac{GM}{r}}$, with orbital period $T = 2\pi\sqrt{\frac{r^3}{GM}}$.</li>
        <li><strong>Parabolic Escape Trajectory ($a \to \infty$):</strong> The exact speed needed to escape the star's gravity completely: $v_{esc} = \sqrt{\frac{2GM}{r}} = \sqrt{2} v_{circ}$.</li>
        <li><strong>Kepler's Third Law:</strong> The square of orbital period scales with the cube of the semi-major axis:
        $$T^2 = \frac{4\pi^2}{GM} a^3$$</li>
      </ul>

      <h3 class="sub-title">6.1.3 Advanced Simple Harmonic Motion (SHM) Dynamics</h3>
      <p>Simple Harmonic Motion is what happens whenever an object feels a restoring force proportional to how far it is displaced: $F = -kx$. The further you push it, the harder it pushes back. This yields the universal oscillation equation:</p>
      $$\ddot{x} + \omega^2 x = 0 \implies x(t) = A\sin(\omega t + \phi)$$
      <p>Speed and acceleration at any position $x$ follow naturally:</p>
      $$v(x) = \pm \omega \sqrt{A^2 - x^2}, \quad a(x) = -\omega^2 x$$

      <p><strong>Two-Block Oscillator with Spring (Reduced Mass):</strong></p>
      <p>When two free blocks of mass $m_1$ and $m_2$ oscillate on a frictionless floor connected by a spring of stiffness $k$, they oscillate in opposition about their stationary common Center of Mass. The system behaves identically to a single block of effective "reduced mass" $\mu$ attached to a fixed wall:</p>
      $$T = 2\pi \sqrt{\frac{\mu}{k}} \quad \text{where } \mu = \frac{m_1 m_2}{m_1 + m_2}$$

      <p><strong>Heavy Spring Mass Correction:</strong></p>
      <p>If the spring itself has mass $m_s$, coils near the wall barely move while coils near the load move at full speed. Integrating the kinetic energy of all moving coils shows that the spring effectively adds exactly one-third of its mass to the oscillating load:</p>
      $$m_{eff} = M + \frac{1}{3}m_s \implies T = 2\pi \sqrt{\frac{M + \frac{1}{3}m_s}{k}}$$

      <p><strong>Compound (Physical) Pendulum & Conjugate Centers:</strong></p>
      <p>A real physical pendulum (like a baseball bat or flat disc) is simply an extended body swinging about a pivot. Its time period depends on the pivot distance $d$ from the Center of Mass:</p>
      $$T = 2\pi \sqrt{\frac{I_{pivot}}{Mgd}} = 2\pi \sqrt{\frac{L_{eq}}{g}}$$
      <p>where $L_{eq} = d + \frac{k_{cm}^2}{d}$ is the length of an equivalent simple pendulum that swings at the exact same rate.</p>
      <ul style="margin-left: 2rem; margin-bottom: 1.5rem; line-height: 1.8;">
        <li><strong>Fastest Swing (Minimum Period):</strong> Oscillation period is minimized when the pivot is placed at the body's radius of gyration: $d = k_{cm}$, giving $T_{\min} = 2\pi \sqrt{\frac{2k_{cm}}{g}}$.</li>
        <li><strong>Center of Oscillation ($S$):</strong> If you flip the body upside down and pivot it at distance $L_{eq}$ from $O$, it swings with the exact same time period $T$.</li>
      </ul>

      <h3 class="sub-title">6.1.4 Phasor Representation & Superposition of Harmonic Oscillations</h3>
      <p>Simple Harmonic Motion can be visualized as the projection of Uniform Circular Motion on a diameter. A rotating vector of length $A$ (amplitude) spinning counterclockwise at angular velocity $\omega$ with initial phase $\phi_0$ is called a <strong>phasor</strong>:</p>
      $$x(t) = A\cos(\omega t + \phi_0) = \text{Re}\left[A e^{i(\omega t + \phi_0)}\right]$$
      <p><strong>Superposition of Two Collinear SHMs of Same Frequency:</strong></p>
      <p>When two oscillations $x_1(t) = A_1\sin(\omega t + \phi_1)$ and $x_2(t) = A_2\sin(\omega t + \phi_2)$ superimpose along the same axis, vector addition of their phasors yields resultant amplitude $A_R$ and phase $\phi_R$:</p>
      $$A_R = \sqrt{A_1^2 + A_2^2 + 2A_1 A_2 \cos(\phi_2 - \phi_1)}$$
      $$\tan\phi_R = \frac{A_1\sin\phi_1 + A_2\sin\phi_2}{A_1\cos\phi_1 + A_2\cos\phi_2}$$
      <p>Notice that this is formally identical to the vector addition of two forces! If phase difference $\Delta\phi = 0$, constructive interference gives $A_R = A_1 + A_2$. If $\Delta\phi = \pi$, destructive interference gives $A_R = |A_1 - A_2|$.</p>

      <h2 class="section-title">6.2 Master Formula Summary Table: Gravitation & SHM</h2>
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
              <td><strong>Solid Sphere Gravitational Potential</strong></td>
              <td class="formula-math">$$V(r) = -\frac{GM}{2R^3}(3R^2 - r^2), \quad V(0) = -\frac{3}{2}\frac{GM}{R}$$</td>
              <td><span class="validity-tag">Interior of uniform density solid sphere ($r \le R$)</span></td>
              <td><span class="invalidity-tag">Assuming potential vanishes at the center or equals $-GM/R$</span></td>
            </tr>
            <tr>
              <td><strong>Gravitational Self-Energy</strong></td>
              <td class="formula-math">$$U_{self} = -\frac{3}{5}\frac{GM^2}{R}$$</td>
              <td><span class="validity-tag">Uniform density continuous solid sphere</span></td>
              <td><span class="invalidity-tag">Applying to hollow shells (which have $-GM^2/(2R)$)</span></td>
            </tr>
            <tr>
              <td><strong>Vis-Viva Orbital Equation</strong></td>
              <td class="formula-math">$$v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)$$</td>
              <td><span class="validity-tag">Any Keplerian orbit (circle, ellipse, parabola, hyperbola)</span></td>
              <td><span class="invalidity-tag">Substituting semi-minor axis $b$ instead of semi-major axis $a$</span></td>
            </tr>
            <tr>
              <td><strong>Reduced Mass Spring Oscillator</strong></td>
              <td class="formula-math">$$\omega = \sqrt{\frac{k}{\mu}}, \quad \mu = \frac{m_1 m_2}{m_1 + m_2}$$</td>
              <td><span class="validity-tag">Two masses free to slide without external constraint</span></td>
              <td><span class="invalidity-tag">Using reduced mass when one end of spring is rigidly anchored to a fixed wall</span></td>
            </tr>
            <tr>
              <td><strong>Heavy Spring Effective Mass</strong></td>
              <td class="formula-math">$$m_{eff} = M + \frac{1}{3}m_{spring}$$</td>
              <td><span class="validity-tag">Uniform mass distribution along spring coils</span></td>
              <td><span class="invalidity-tag">Adding the full spring mass $m_s$ to the block mass</span></td>
            </tr>
            <tr>
              <td><strong>Compound Pendulum Conjugate Length</strong></td>
              <td class="formula-math">$$L_{eq} = d + \frac{k_{cm}^2}{d}$$</td>
              <td><span class="validity-tag">Rigid body physical pendulum for small angles</span></td>
              <td><span class="invalidity-tag">Assuming $T \to 0$ when pivot is placed at the Center of Mass ($d \to 0 \implies T \to \infty$!)</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 class="section-title">6.3 10 Forensic NTA/JEE Negative-Marking Trap Alerts</h2>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.1] Gravitational Potential at Center of Earth</div>
        <p><strong>The Trap:</strong> Setting $V = 0$ at the center of Earth because gravitational field is zero ($E(0) = 0$).</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Field is the derivative of potential ($E = -dV/dr$). Zero field means potential has a local extremum, NOT that potential is zero! Potential at the center is the absolute minimum across the universe: $V(0) = \mathbf{-\frac{3}{2}\frac{GM}{R}} = -1.5\frac{GM}{R}$.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.2] The Satellite Thrusting Paradox (Orbital Deceleration)</div>
        <p><strong>The Trap:</strong> A satellite in circular orbit fires forward thrusters to increase its speed.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Forward thrust adds energy ($E$ increases, becoming less negative), which raises the satellite into a higher orbit ($r$ increases). But orbital speed is $v = \sqrt{GM/r}$, so in the higher orbit the satellite <strong>travels SLOWER</strong>! Conversely, firing reverse brakes causes the satellite to drop to a lower orbit where it speeds up!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.3] Escape Velocity Angle Independence</div>
        <p><strong>The Trap:</strong> Believing escape velocity $v_{esc} = \sqrt{2gR}$ applies only to projectiles launched vertically upward.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Escape velocity is derived purely from scalar energy conservation ($E \ge 0 \implies \frac{1}{2}mv^2 - \frac{GMm}{R} \ge 0$). It is <strong>strictly independent of launch direction</strong>, provided the trajectory does not intersect the physical surface of the planet!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.4] Spring Cut in Length Ratio $m:n$</div>
        <p><strong>The Trap:</strong> A spring of stiffness $k$ is cut in ratio $1:2$. Students guess the shorter piece has stiffness $k/2$.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Spring stiffness is inversely proportional to unstretched length: $k \cdot L = \text{constant}$. For ratio $m:n$, lengths are $L_1 = \frac{m}{m+n}L$ and $L_2 = \frac{n}{m+n}L$. The stiffnesses are: $k_1 = \mathbf{\frac{m+n}{m}k}$ and $k_2 = \mathbf{\frac{m+n}{n}k}$. For ratio $1:2$, $k_1 = 3k$ and $k_2 = \frac{3}{2}k$! Shorter springs are much stiffer.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.5] Compound Pendulum Pivot at Center of Mass</div>
        <p><strong>The Trap:</strong> Moving the pivot point closer to the Center of Mass ($d \to 0$) to minimize the oscillation period.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> As $d \to 0$, restoring torque $\tau = Mgd\sin\theta \to 0$. Consequently, the time period blows up to infinity: $T = 2\pi\sqrt{\frac{k^2+d^2}{gd}} \to \mathbf{\infty}$! The minimum time period occurs at $d = k_{cm}$, NOT at $d = 0$.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.6] Instantaneous Mass Addition to an Oscillating Cart</div>
        <p><strong>The Trap:</strong> Dropping a piece of putty onto a block executing SHM at its extreme amplitude position ($x = A$), and using momentum conservation to decrease the amplitude.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> At $x = A$, velocity is momentarily zero ($v = 0$). Momentum is trivially zero. The added mass acquires zero velocity, so total mechanical energy remains $E = \frac{1}{2}kA^2$. <strong>The amplitude remains completely unchanged ($A' = A$)!</strong> (Only the frequency drops to $\omega' = \sqrt{k/(M+m)}$). In contrast, dropping mass at the mean position ($x=0$) conserves momentum and reduces amplitude!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.7] Tunnel Through Earth Along an Arbitrary Chord</div>
        <p><strong>The Trap:</strong> Assuming a tunnel dug along an off-center chord through Earth has a different oscillation period than a diameter tunnel.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Gravitational force at distance $r$ is $\mathbf{F} = -\frac{GMm}{R^3}\mathbf{r}$. The component along the chord at displacement $x$ is $F_x = -\frac{GMm}{R^3}x$. The normal force from the tunnel wall balances perpendicular components. The resulting motion is pure SHM with time period $T = 2\pi\sqrt{\frac{R^3}{GM}} = 2\pi\sqrt{\frac{R}{g}} \approx \mathbf{84.6\text{ minutes}}$, <strong>strictly identical for ANY chord regardless of distance from center</strong>!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.8] Two-Block Spring Oscillator Frequency with Moving Wall</div>
        <p><strong>The Trap:</strong> Applying $\omega = \sqrt{k/m}$ to a block connected by a spring to another freely sliding block on a smooth floor.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> When both blocks are free, the Center of Mass is unaccelerated. You MUST use the reduced mass: $\omega = \sqrt{\frac{k}{\mu}} = \sqrt{\frac{k(m_1 + m_2)}{m_1 m_2}} > \sqrt{\frac{k}{m_1}}$. The frequency is strictly higher than if either block were fixed to a rigid wall.</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.9] Satellite Total Energy Sign Blunder</div>
        <p><strong>The Trap:</strong> Writing satellite total energy as positive because kinetic energy is positive.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> For any bound gravitational orbit, potential energy is negative and twice the magnitude of kinetic energy: $U = -2K$. Therefore, total mechanical energy is <strong>strictly negative</strong>: $E = K + U = K - 2K = -K = -\frac{GMm}{2r} < 0$. If $E \ge 0$, the orbit is unbounded (parabolic or hyperbolic) and the satellite escapes!</div>
      </div>

      <div class="card-box trap-card">
        <div class="card-header-trap">[TRAP ALERT 6.10] Effective 'g' in Liquid Buoyancy Oscillations</div>
        <p><strong>The Trap:</strong> Finding time period of a floating vertical cylinder pressed down into liquid by writing $T = 2\pi\sqrt{L/g}$ where $L$ is submerged depth.</p>
        <div class="trap-remedy"><strong>Definitive Rule:</strong> Restoring force is excess buoyancy: $F = -(\rho A x) g$. Mass of cylinder is $M = \rho_{cyl} A H = \rho A L_{sub}$. Equation: $(\rho A L_{sub}) \ddot{x} + (\rho A g) x = 0 \implies \ddot{x} + \frac{g}{L_{sub}} x = 0$. The period is indeed $T = 2\pi\sqrt{\frac{L_{sub}}{g}}$, but this holds ONLY if liquid viscosity and added mass of the surrounding fluid are neglected!</div>
      </div>

      <h2 class="section-title">6.4 Dissected JEE Advanced Previous Year Questions (PYQs)</h2>

      <!-- PYQ 6.1 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2017 • Paper 2</span>
          <span class="pyq-difficulty">Difficulty: Hard • Off-Center Earth Tunnel SHM</span>
        </div>
        <div class="pyq-question">
          A straight, frictionless tunnel is drilled through the Earth along a chord whose perpendicular distance from the Earth's center is $d = R/2$, where $R = 6400\text{ km}$ is the radius of the Earth. A small particle is dropped from rest at one entrance of the tunnel. (a) Prove that the particle executes Simple Harmonic Motion. (b) Calculate the time taken to travel from one entrance to the other. Take $g = 9.8\text{ m/s}^2$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Gravitational Force at Arbitrary Position along the Chord:</strong></p>
          <p>Let $x$ be the displacement of the particle from the midpoint of the tunnel (chord). The radial distance from Earth's center is $r = \sqrt{x^2 + d^2}$.</p>
          <p>Inside uniform Earth, gravitational field is linear: $\mathbf{E}(r) = -\frac{GM}{R^3} \mathbf{r} = -g \frac{\mathbf{r}}{R}$.</p>
          <p>The gravitational force on particle of mass $m$ is:</p>
          $$\mathbf{F}_g = -m \frac{g}{R} \mathbf{r}$$
          <p><strong>Step 2: Component Along the Tunnel Axis:</strong></p>
          <p>Resolving $\mathbf{F}_g$ along the tunnel axis (the $x$-direction):</p>
          $$F_x = \mathbf{F}_g \cdot \hat{\mathbf{i}} = -m \frac{g}{R} (\mathbf{r} \cdot \hat{\mathbf{i}}) = -m \frac{g}{R} x$$
          <p>The perpendicular force component $F_y = -m\frac{g}{R}d$ is completely balanced by the normal reaction from the frictionless tunnel wall: $N = m\frac{g}{R}d$.</p>
          <p><strong>Step 3: Equation of Motion & Proven SHM:</strong></p>
          $$m \ddot{x} = -m \frac{g}{R} x \implies \ddot{x} + \left(\frac{g}{R}\right) x = 0$$
          <p>This is precisely the Simple Harmonic Motion differential equation with natural frequency:</p>
          $$\omega = \sqrt{\frac{g}{R}}$$
          <p>Remarkably, $\omega$ is completely independent of the chord distance $d$!</p>
          <p><strong>Step 4: Travel Time Between Entrances:</strong></p>
          <p>The particle moves from one extreme $x = +x_0$ to the opposite extreme $x = -x_0$, which corresponds to exactly half an oscillation period:</p>
          $$t_{travel} = \frac{T}{2} = \frac{\pi}{\omega} = \pi \sqrt{\frac{R}{g}}$$
          $$t_{travel} = \pi \sqrt{\frac{6.4 \times 10^6}{9.8}} \approx 3.1416 \times \sqrt{653061} \approx 3.1416 \times 808.12 \approx \mathbf{2538.8\text{ seconds}} \approx \mathbf{42.3\text{ minutes}}$$
        </div>
      </div>

      <!-- PYQ 6.2 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2018 • Paper 2</span>
          <span class="pyq-difficulty">Difficulty: Hard • Orbital Transfer via Tangential Impulse</span>
        </div>
        <div class="pyq-question">
          A satellite of mass $m = 500\text{ kg}$ is in a circular orbit of radius $r_1 = 2R$ around a planet of mass $M$ and radius $R$. An instantaneous forward tangential impulse $\Delta P$ is delivered to the satellite, transferring it into an elliptical orbit whose apoapsis distance is $r_2 = 6R$. Find (a) the required impulse magnitude $\Delta P$ in terms of $m, M, R, G$, and (b) the period of the new elliptical orbit compared to the circular orbit.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Initial Circular Orbit Speed:</strong></p>
          $$v_c = \sqrt{\frac{GM}{r_1}} = \sqrt{\frac{GM}{2R}}$$
          <p><strong>Step 2: Required Periapsis Velocity for Elliptical Orbit:</strong></p>
          <p>For the new transfer ellipse: periapsis $r_p = r_1 = 2R$ and apoapsis $r_a = r_2 = 6R$.</p>
          <p>The semi-major axis is:</p>
          $$a = \frac{r_p + r_a}{2} = \frac{2R + 6R}{2} = 4R$$
          <p>Applying the Vis-Viva equation at periapsis ($r = 2R$):</p>
          $$v_p^2 = GM\left(\frac{2}{2R} - \frac{1}{4R}\right) = GM\left(\frac{1}{R} - \frac{1}{4R}\right) = \frac{3GM}{4R}$$
          $$v_p = \sqrt{\frac{3GM}{4R}} = \frac{\sqrt{3}}{2} \sqrt{\frac{GM}{R}}$$
          <p><strong>Step 3: Tangential Impulse $\Delta P$:</strong></p>
          $$\Delta v = v_p - v_c = \sqrt{\frac{3GM}{4R}} - \sqrt{\frac{GM}{2R}} = \left(\frac{\sqrt{3} - \sqrt{2}}{2}\right)\sqrt{\frac{GM}{R}}$$
          $$\Delta P = m \Delta v = \mathbf{m\left(\frac{\sqrt{3} - \sqrt{2}}{2}\right)\sqrt{\frac{GM}{R}}}$$
          <p><strong>Step 4: Ratio of Orbital Periods (Kepler's Third Law):</strong></p>
          $$\frac{T_{ellipse}}{T_{circ}} = \left(\frac{a}{r_1}\right)^{3/2} = \left(\frac{4R}{2R}\right)^{3/2} = (2)^{3/2} = \mathbf{2\sqrt{2}} \approx 2.828$$
        </div>
      </div>

      <!-- PYQ 6.3 -->
      <div class="pyq-box">
        <div class="pyq-header">
          <span class="pyq-tag">[WORKED JEE ADVANCED PYQ] JEE Advanced 2022 • Paper 1</span>
          <span class="pyq-difficulty">Difficulty: Hard • Physical Pendulum Pivoted at Rim</span>
        </div>
        <div class="pyq-question">
          A uniform thin circular disc of mass $M = 3\text{ kg}$ and radius $R = 0.4\text{ m}$ is pivoted about a fixed horizontal axis perpendicular to the plane of the disc passing through a point on its circumference. Determine (a) the time period of small oscillations $T$, and (b) the distance from the pivot to the center of oscillation $S$. Take $g = 10\text{ m/s}^2$.
        </div>
        <div class="pyq-solution">
          <div class="pyq-solution-title">First-Principles Step-by-Step Solution:</div>
          <p><strong>Step 1: Moment of Inertia About Rim Pivot:</strong></p>
          <p>Distance from pivot to Center of Mass is $d = R$.</p>
          <p>By Parallel Axis Theorem:</p>
          $$I_{pivot} = I_{cm} + M d^2 = \frac{1}{2}MR^2 + MR^2 = \frac{3}{2}MR^2$$
          <p>The radius of gyration about COM is $k_{cm} = \sqrt{\frac{I_{cm}}{M}} = \frac{R}{\sqrt{2}}$.</p>
          <p><strong>Step 2: Small Oscillation Time Period:</strong></p>
          $$T = 2\pi \sqrt{\frac{I_{pivot}}{Mgd}} = 2\pi \sqrt{\frac{\frac{3}{2}MR^2}{MgR}} = 2\pi \sqrt{\frac{3R}{2g}}$$
          <p>Substituting $R = 0.4\text{ m}$ and $g = 10\text{ m/s}^2$:</p>
          $$T = 2\pi \sqrt{\frac{3(0.4)}{2(10)}} = 2\pi \sqrt{\frac{1.2}{20}} = 2\pi \sqrt{0.06} \approx 2(3.1416)(0.2449) \approx \mathbf{1.539\text{ seconds}}$$
          <p><strong>Step 3: Distance to Center of Oscillation ($S$):</strong></p>
          <p>The equivalent simple pendulum length is:</p>
          $$L_{eq} = d + \frac{k_{cm}^2}{d} = R + \frac{R^2/2}{R} = R + \frac{R}{2} = \mathbf{\frac{3}{2}R}$$
          $$L_{eq} = 1.5(0.4) = \mathbf{0.60\text{ meters}} = 60\text{ cm from the rim pivot}$$
        </div>
      </div>

      <h2 class="section-title">6.5 High-Caliber Practice Challenge Problems & Complete Solutions</h2>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 6.1] Velocity Ratio in Halley's Comet Orbit</div>
        <p>A comet moves in an eccentric elliptical orbit around the Sun. Its distance of closest approach (perihelion) is $r_p = 0.6\text{ AU}$ and its maximum distance (aphelion) is $r_a = 35.4\text{ AU}$. Calculate (a) the ratio of its speed at perihelion to that at aphelion $v_p / v_a$, and (b) the orbital eccentricity $e$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p><strong>Step 1: Angular Momentum Conservation:</strong></p>
            <p>At both perihelion and aphelion, velocity is strictly perpendicular to the position vector ($\mathbf{r} \perp \mathbf{v}$):</p>
            $$L = m r_p v_p = m r_a v_a \implies \frac{v_p}{v_a} = \frac{r_a}{r_p} = \frac{35.4}{0.6} = \mathbf{59.0}$$
            <p><strong>Step 2: Orbital Eccentricity $e$:</strong></p>
            $$r_p = a(1 - e), \quad r_a = a(1 + e)$$
            $$\frac{r_a}{r_p} = \frac{1 + e}{1 - e} = 59 \implies 1 + e = 59 - 59e \implies 60e = 58 \implies e = \frac{58}{60} = \mathbf{\frac{29}{30}} \approx 0.9667$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 6.2] Rolling Cylinder Spring Oscillator</div>
        <p>A solid uniform cylinder of mass $M = 6\text{ kg}$ and radius $R = 0.3\text{ m}$ is attached to a horizontal spring of stiffness $k = 450\text{ N/m}$ at its central axle. The cylinder rolls without slipping on a horizontal plane. Determine the angular frequency $\omega$ and time period $T$ of small oscillations.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Total mechanical energy at displacement $x$ and velocity $v = \dot{x}$ (pure rolling implies $\omega = v/R$):</p>
            $$E = \frac{1}{2}M v^2 + \frac{1}{2}I_{cm}\omega^2 + \frac{1}{2}kx^2 = \frac{1}{2}M v^2 + \frac{1}{2}\left(\frac{1}{2}MR^2\right)\left(\frac{v}{R}\right)^2 + \frac{1}{2}kx^2$$
            $$E = \frac{3}{4} M v^2 + \frac{1}{2} k x^2$$
            <p>Differentiating with respect to time ($\frac{dE}{dt} = 0$):</p>
            $$\frac{3}{2} M v \frac{dv}{dt} + k x v = 0 \implies v\left(\frac{3}{2}M \ddot{x} + k x\right) = 0 \implies \ddot{x} + \left(\frac{2k}{3M}\right) x = 0$$
            $$\omega = \sqrt{\frac{2k}{3M}} = \sqrt{\frac{2(450)}{3(6)}} = \sqrt{\frac{900}{18}} = \sqrt{50} = 5\sqrt{2} \approx \mathbf{7.071\text{ rad/s}}$$
            $$T = \frac{2\pi}{\omega} = \frac{2\pi}{5\sqrt{2}} = \frac{\sqrt{2}\pi}{5} \approx \mathbf{0.889\text{ seconds}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 6.3] Gravitational Cloud Collapse Energy Release</div>
        <p>A diffuse, uniform spherical cloud of interstellar gas of initial radius $R_1 = 10^{11}\text{ m}$ and total mass $M = 2 \times 10^{30}\text{ kg}$ slowly contracts gravitationally under its own gravity to form a protostar of radius $R_2 = 7 \times 10^8\text{ m}$. Calculate the total amount of gravitational energy converted and radiated during this collapse.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Initial self-energy: $U_1 = -\frac{3}{5}\frac{GM^2}{R_1}$. Final self-energy: $U_2 = -\frac{3}{5}\frac{GM^2}{R_2}$.</p>
            <p>Total change in potential energy:</p>
            $$\Delta U = U_2 - U_1 = -\frac{3}{5}GM^2\left(\frac{1}{R_2} - \frac{1}{R_1}\right) \approx -\frac{3}{5}\frac{GM^2}{R_2} \quad (\text{since } R_1 \gg R_2)$$
            <p>By the Virial Theorem for self-gravitating bound systems, half of the released potential energy goes into internal thermal kinetic energy, and half is radiated away:</p>
            $$E_{radiated} = \frac{1}{2}|\Delta U| = \frac{3}{10}\frac{GM^2}{R_2}$$
            $$E_{rad} = \frac{3}{10}\frac{(6.674 \times 10^{-11})(4 \times 10^{60})}{7 \times 10^8} = \frac{8.009 \times 10^{50}}{7 \times 10^8} \approx \mathbf{1.144 \times 10^{42}\text{ Joules}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 6.4] U-Tube Liquid Column Oscillations</div>
        <p>A uniform U-tube of total cross-sectional area $A = 5\text{ cm}^2$ contains an incompressible, non-viscous liquid of density $\rho = 1000\text{ kg/m}^3$. The total length of the liquid column is $L = 1.6\text{ m}$. If the liquid is depressed slightly in one limb and released, find (a) the oscillation frequency $\omega$, and (b) the time period $T$. Take $g = 10\text{ m/s}^2$.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Let liquid in the left limb be displaced downward by $x$. The liquid in the right limb rises by $x$.</p>
            <p>Height difference between liquid levels: $\Delta h = 2x$.</p>
            <p>Restoring hydrostatic force:</p>
            $$F = -(\rho A \Delta h) g = -(2\rho A g) x$$
            <p>Total mass of the liquid column: $M = \rho A L$.</p>
            <p>Equation of motion:</p>
            $$(\rho A L) \ddot{x} + (2\rho A g) x = 0 \implies \ddot{x} + \left(\frac{2g}{L}\right) x = 0$$
            $$\omega = \sqrt{\frac{2g}{L}} = \sqrt{\frac{2(10)}{1.6}} = \sqrt{\frac{20}{1.6}} = \sqrt{12.5} \approx \mathbf{3.536\text{ rad/s}}$$
            $$T = \frac{2\pi}{\omega} = 2\pi \sqrt{\frac{L}{2g}} = 2\pi \sqrt{0.08} \approx 2(3.1416)(0.2828) \approx \mathbf{1.777\text{ seconds}}$$
          </div>
        </details>
      </div>

      <div class="challenge-box">
        <div class="challenge-header">[CHALLENGE PROBLEM 6.5] Spring-Coupled Two Block Separation Under Force</div>
        <p>Two blocks $A$ ($m_1 = 1\text{ kg}$) and $B$ ($m_2 = 2\text{ kg}$) are connected by an unstretched light spring of constant $k = 100\text{ N/m}$ on a frictionless horizontal floor. A constant horizontal pulling force $F = 30\text{ N}$ is applied to block $B$ directed away from $A$. Determine the maximum extension $x_{\max}$ of the spring during the motion.</p>
        <details class="challenge-details">
          <summary>View Complete Analytical Solution</summary>
          <div class="challenge-solution">
            <p>Acceleration of Center of Mass:</p>
            $$A_{cm} = \frac{F}{m_1 + m_2} = \frac{30}{1 + 2} = 10\text{ m/s}^2$$
            <p>In the Center of Mass reference frame (accelerating at $A_{cm}$ rightward):</p>
            <ul style="margin-left: 1.5rem; line-height: 1.8;">
              <li>On block $A$: backward pseudo-force $m_1 A_{cm} = 1(10) = 10\text{ N}$ leftward (pulling spring open).</li>
              <li>On block $B$: applied force $F = 30\text{ N}$ rightward and backward pseudo-force $m_2 A_{cm} = 2(10) = 20\text{ N}$ leftward. Net effective pulling force on $B$: $30 - 20 = 10\text{ N}$ rightward.</li>
            </ul>
            <p>Work done by effective forces in expanding spring by $x$:</p>
            $$W_{eff} = F_{eff} x = \left(\frac{m_1}{m_1 + m_2} F\right) x = \left(\frac{1}{3} \times 30\right) x = 10 x$$
            <p>At maximum extension $x_{\max}$, relative velocity vanishes ($v_{rel} = 0$). By energy conservation in C-frame:</p>
            $$W_{eff} = \frac{1}{2} k x_{\max}^2 \implies 10 x_{\max} = \frac{1}{2}(100) x_{\max}^2 \implies 10 = 50 x_{\max}$$
            $$x_{\max} = \frac{10}{50} = \mathbf{0.20\text{ meters}} = 20\text{ cm}$$
          </div>
        </details>
      </div>
    </section>
    """

if __name__ == "__main__":
    content = get_ch6_content()
    print("Chapter 6 content generated successfully. Length:", len(content))
