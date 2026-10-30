import os

def build_part_3():
    parts = []
    
    parts.append(r"""# PART 3: WEB BOOK READER ARCHITECTURE, KATEX TYPESETTING & PRINT/EXPORT ENGINE

## 3.1 Web Book Reader Responsive Architecture & Layout

### 3.1.1 Architectural Overview
The *JEE Main & Advanced Classical Mechanics Master Handbook* is architected as a high-performance, single-page standalone web application (`index.html`) requiring **zero local runtime dependencies, build pipelines, or web server daemons**. It opens natively in any modern web browser (`open index.html` or `file:///...`) and deploys instantly to static hosting platforms (GitHub Pages, Vercel, Cloudflare Pages).

```
+---------------------------------------------------------------------------------------+
|  TOP PROGRESS BAR (sticky, height: 4px, background: #d97706, width: scrollPercent)     |
+---------------------------------------------------------------------------------------+
|  HAMBURGER (mobile) | CHAPTER HEADER & BREADCRUMB                      | PRINT / THEME |
+---------------------+--------------------------------------------------+--------------+
|  SIDEBAR NAV        |  MAIN CONTENT CONTAINER (#book-content)          | QUICK JUMP   |
|  (Fixed 300px       |  (Max-width: 860px, centered, padding: 48px)     | ON THIS PAGE |
|   Collapsible)      |                                                  | (Scrollspy)  |
|                     |  - Chapter Title & Overview Cards                |              |
|  - Ch 1: Kinematics |  - Rigorous Mathematical Derivations             | - Section 1  |
|  - Ch 2: NLM        |  - Master Formula Reference Matrix               | - Section 2  |
|  - Ch 3: Energy     |  - 10+ NTA Negative-Marking Trap Cards           | - Traps      |
|  - Ch 4: Momentum   |  - Fully Worked Dissected JEE Advanced PYQs      | - PYQs       |
|  - Ch 5: Rotation   |  - High-Caliber Challenge Problems & Keys        | - Challenges |
|  - Ch 6: Grav & SHM |  - High-Fidelity Inline SVG Physics Blueprints   | - Diagrams   |
|                     |                                                  |              |
|  [Expand / Fold]    |  [Next Chapter Button] [Back to Top Button]       |              |
+---------------------+--------------------------------------------------+--------------+
```

### 3.1.2 Semantic DOM Architecture
The web book follows strict HTML5 semantic hierarchy:
```html
<!DOCTYPE html>
<html lang="en" data-theme="warm-paper">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JEE Mechanics & Rotational Dynamics Master Handbook</title>
  <!-- KaTeX Typography Stylesheet -->
  <link rel="stylesheet" href="assets/katex/katex.min.css" id="katex-css">
  <!-- Core Design System -->
  <link rel="stylesheet" href="assets/css/handbook.css">
</head>
<body class="handbook-body">
  <!-- Dynamic Top Scroll Progress Indicator -->
  <div id="reading-progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>

  <!-- App Header (Visible on Mobile & Tablet) -->
  <header class="mobile-header">
    <button id="sidebar-toggle" aria-label="Toggle Table of Contents">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M4 6h16M4 12h16M4 18h16" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
    <span class="mobile-title">JEE Classical Mechanics Handbook</span>
    <button id="print-button" onclick="window.print()" aria-label="Print Handbook">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2M6 14h12v8H6z" stroke-width="2"/></svg>
    </button>
  </header>

  <!-- Shell Wrapper -->
  <div class="book-shell">
    <!-- Collapsible Responsive Navigation Sidebar -->
    <nav id="sidebar" class="sidebar-nav" aria-label="Table of Contents">
      <div class="sidebar-brand">
        <h2>JEE Physics Master Handbook</h2>
        <span class="badge-edition">IIT JEE Advanced 2027</span>
      </div>
      <div class="sidebar-search">
        <input type="text" id="topic-search" placeholder="Search formulas, traps, PYQs..." aria-label="Search Handbook">
      </div>
      <ul class="chapter-nav-list" id="chapter-tree">
        <!-- Dynamically or statically hydrated chapter tree -->
      </ul>
    </nav>

    <!-- Main Reading Column -->
    <main id="book-content" class="book-content" tabindex="-1">
      <!-- Active Chapter Container -->
      <article class="handbook-chapter" id="chapter-5">
        <!-- Embedded Chapter Markdown Content -->
      </article>
    </main>

    <!-- Sticky On-This-Page Secondary Outline (Desktop) -->
    <aside id="page-outline" class="page-outline" aria-label="Current Section Navigation">
      <div class="outline-header">On This Page</div>
      <ul class="outline-list" id="outline-tree"></ul>
    </aside>
  </div>

  <!-- KaTeX Typesetting Engine & Offline Fallback Scripts -->
  <script src="assets/katex/katex.min.js"></script>
  <script src="assets/katex/contrib/auto-render.min.js"></script>
  <script src="assets/js/reader-engine.js"></script>
</body>
</html>
```

---

## 3.2 Visual Styling System & Soft Warm Yellow Paper Theme

### 3.2.1 Color Palette & Design Tokens
The visual design implements an eye-fatigue-reducing, soft warm yellow / cream paper aesthetic modeled after archival university physics texts:

```css
:root {
  /* Surface & Background Tokens */
  --bg-paper: #fcfaf2;           /* Soft cream/warm paper base background */
  --bg-card: #f7f3e8;            /* Tinted card background for modules */
  --bg-card-hover: #f2ece0;      /* Card hover state */
  --border-subtle: #e8dec8;      /* Warm golden-sand borders */
  --border-strong: #d5c7aa;      /* Accented separators and outlines */
  --bg-sidebar: #f5f0e3;         /* Nav sidebar subtle contrast */
  
  /* Ink & Typography Tokens */
  --ink-primary: #1e293b;        /* Deep midnight slate for body text */
  --ink-secondary: #475569;      /* Muted ink for captions and meta info */
  --ink-headings: #0f172a;       /* High-contrast ink for H1-H3 */
  --font-serif: "Merriweather", "Georgia", "Cambria", serif;
  --font-sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-mono: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;

  /* Pedagogical Callout Accents */
  /* Trap Alerts (Negative-Marking Warnings) */
  --trap-bg: #fef2f2;
  --trap-border: #ef4444;
  --trap-text: #991b1b;
  --trap-badge: #dc2626;

  /* IIT Professor Tips & Physical Insights */
  --tip-bg: #ecfdf5;
  --tip-border: #10b981;
  --tip-text: #065f46;
  --tip-badge: #059669;

  /* Calculus & First-Principles Derivations */
  --deriv-bg: #eff6ff;
  --deriv-border: #3b82f6;
  --deriv-text: #1e40af;
  --deriv-badge: #2563eb;

  /* PYQs & Exam Hall Dissections */
  --pyq-bg: #fffbeb;
  --pyq-border: #f59e0b;
  --pyq-text: #92400e;
  --pyq-badge: #d97706;

  /* Layout Dimensions */
  --sidebar-width: 310px;
  --outline-width: 240px;
  --content-max-width: 860px;
  --progress-height: 4px;
}
```

### 3.2.2 Typography & Spacing Scale
```css
body.handbook-body {
  margin: 0;
  padding: 0;
  background-color: var(--bg-paper);
  color: var(--ink-primary);
  font-family: var(--font-sans);
  font-size: 16.5px;
  line-height: 1.75;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Headings Typography */
h1, h2, h3, h4, h5, h6 {
  color: var(--ink-headings);
  font-family: var(--font-serif);
  font-weight: 700;
  line-height: 1.3;
  margin-top: 2rem;
  margin-bottom: 1rem;
  scroll-margin-top: 80px;
}

h1 { font-size: 2.2rem; border-bottom: 2px solid var(--border-subtle); padding-bottom: 0.5rem; }
h2 { font-size: 1.7rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 0.35rem; }
h3 { font-size: 1.35rem; }
h4 { font-size: 1.15rem; font-family: var(--font-sans); font-weight: 600; }

p, li {
  margin-bottom: 1rem;
}

/* Interactive Callout Cards */
.card-callout {
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  margin: 1.5rem 0;
  border-left: 5px solid;
  position: relative;
  background-color: var(--bg-card);
}

.card-trap {
  background-color: var(--trap-bg);
  border-left-color: var(--trap-border);
  color: var(--trap-text);
}

.card-tip {
  background-color: var(--tip-bg);
  border-left-color: var(--tip-border);
  color: var(--tip-text);
}

.card-derivation {
  background-color: var(--deriv-bg);
  border-left-color: var(--deriv-border);
  color: var(--deriv-text);
}

.card-pyq {
  background-color: var(--pyq-bg);
  border-left-color: var(--pyq-border);
  color: var(--pyq-text);
}

/* Collapsible Derivation Accordion */
details.derivation-fold {
  background-color: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  padding: 0.75rem 1rem;
  margin: 1.25rem 0;
  transition: background-color 0.2s ease;
}

details.derivation-fold[open] {
  background-color: #fffdf7;
  border-color: var(--border-strong);
}

details.derivation-fold summary {
  font-family: var(--font-sans);
  font-weight: 600;
  cursor: pointer;
  color: var(--ink-headings);
  display: flex;
  align-items: center;
  user-select: none;
}
```

---

## 3.3 KaTeX Mathematical Typesetting Engine & Offline Resilience

### 3.3.1 KaTeX Configuration & Physics Macros
KaTeX is configured to render math delimiters with supreme speed and support comprehensive physics notation (vectors, tensors, derivatives, Nabla operators):

```javascript
// reader-engine.js: KaTeX Render Engine Initialization
document.addEventListener("DOMContentLoaded", function () {
  const katexConfig = {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "\\[", right: "\\]", display: true },
      { left: "$", right: "$", display: false },
      { left: "\\(", right: "\\)", display: false }
    ],
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
    throwOnError: false,
    errorColor: "#ef4444",
    strict: false,
    macros: {
      // Vectors and Tensors
      "\\bm": "\\boldsymbol{#1}",
      "\\mathbf": "\\boldsymbol{#1}",
      "\\va": "\\vec{#1}",
      "\\vb": "\\mathbf{#1}",
      "\\vu": "\\hat{#1}",
      // Vector Calculus Operators
      "\\grad": "\\boldsymbol{\\nabla}",
      "\\div": "\\boldsymbol{\\nabla} \\cdot",
      "\\curl": "\\boldsymbol{\\nabla} \\times",
      "\\laplacian": "\\nabla^2",
      // Differential and Derivative Notation
      "\\dd": "\\mathrm{d}#1",
      "\\dv": "\\frac{\\mathrm{d}#1}{\\mathrm{d}#2}",
      "\\pdv": "\\frac{\\partial #1}{\\partial #2}",
      // Rotational Mechanics Shorthands
      "\\Icm": "I_{\\text{cm}}",
      "\\rcm": "\\mathbf{r}_{\\text{cm}}",
      "\\vcm": "\\mathbf{v}_{\\text{cm}}",
      "\\acm": "\\mathbf{a}_{\\text{cm}}",
      "\\Lcm": "\\mathbf{L}_{\\text{cm}}",
      "\\IAOR": "\\text{IAOR}"
    }
  };

  // Perform Initial Auto-Render
  if (window.renderMathInElement) {
    renderMathInElement(document.getElementById("book-content"), katexConfig);
  } else {
    initKaTeXOfflineFallback(katexConfig);
  }
});
```

### 3.3.2 Robust Offline Fallback Pipeline
To ensure 100% resilience when viewing the file offline without internet connectivity:
```javascript
// Offline Fallback Mechanism for Standalone HTML distribution
function initKaTeXOfflineFallback(config) {
  console.warn("KaTeX CDN unreachable. Attempting local assets/vendor/ fallback...");
  
  const localCss = document.createElement("link");
  localCss.rel = "stylesheet";
  localCss.href = "assets/katex/katex.min.css";
  document.head.appendChild(localCss);

  const localJs = document.createElement("script");
  localJs.src = "assets/katex/katex.min.js";
  localJs.onload = function () {
    const localAutoRender = document.createElement("script");
    localAutoRender.src = "assets/katex/contrib/auto-render.min.js";
    localAutoRender.onload = function () {
      renderMathInElement(document.getElementById("book-content"), config);
      console.log("KaTeX successfully loaded from local offline assets.");
    };
    document.body.appendChild(localAutoRender);
  };
  document.body.appendChild(localJs);
}
```

### 3.3.3 Asynchronous Chunked Rendering (Performance Optimization)
On massive 50-page equivalent chapters containing >500 complex mathematical formulas, synchronous rendering can freeze the browser main thread for 400-800ms. We employ `requestIdleCallback` to render sections progressively without frame drops:
```javascript
function renderEquationsChunked(container, config) {
  const sections = Array.from(container.querySelectorAll("section, .card-callout, table"));
  let index = 0;

  function processNextChunk(deadline) {
    while (index < sections.length && (deadline.timeRemaining() > 5 || deadline.didTimeout)) {
      renderMathInElement(sections[index], config);
      index++;
    }
    if (index < sections.length) {
      if (window.requestIdleCallback) {
        window.requestIdleCallback(processNextChunk);
      } else {
        setTimeout(processNextChunk, 16);
      }
    }
  }

  if (window.requestIdleCallback) {
    window.requestIdleCallback(processNextChunk);
  } else {
    renderMathInElement(container, config);
  }
}
```

---

## 3.4 Publication-Grade Print Stylesheet Engine (@media print)

### 3.4.1 Print Architecture Specifications
When the reader triggers `window.print()` (`Cmd + P`), the stylesheet transitions from interactive web reader to a **50-page publication-grade physical book** with the following ironclad guarantees:
1. Complete removal of web chrome (sidebar, progress bar, search inputs, buttons).
2. Pure white background (`#ffffff`) with deep black ink (`#000000`) for maximum legibility and ink-conserving monochrome/grayscale print fidelity.
3. Explicit `@page` dimensions (Standard A4 / Letter with exact geometric margins: `18mm 15mm 20mm 15mm`).
4. Strict **orphan and widow suppression** (`orphans: 3; widows: 3;`).
5. Forced page breaks before each chapter (`page-break-before: always; break-before: page;`).
6. **Zero broken equation blocks:** All display equations (`.katex-display`), formula tables, SVG diagrams, and callout cards have `page-break-inside: avoid; break-inside: avoid;`.
7. Running headers and footers with automated page numbering via CSS counters.

### 3.4.2 Comprehensive `@media print` CSS Blueprint
```css
/* ==========================================================================
   PUBLICATION PRINT ENGINE (@media print)
   Converts Web Reader into a Crisp, 50-Page Archival Physical Book
   ========================================================================== */

@media print {
  /* Page Geometry & Margins */
  @page {
    size: A4 portrait;
    margin: 18mm 15mm 20mm 15mm;
    
    /* Running Header (Top) */
    @top-center {
      content: "JEE Main & Advanced Classical Mechanics & Rotational Dynamics Master Handbook";
      font-family: "Merriweather", serif;
      font-size: 8pt;
      color: #64748b;
      border-bottom: 0.5pt solid #cbd5e1;
      padding-bottom: 4pt;
    }

    /* Running Footer (Bottom) */
    @bottom-left {
      content: "Chapter " counter(chapter);
      font-family: "Inter", sans-serif;
      font-size: 8pt;
      color: #64748b;
    }

    @bottom-right {
      content: "Page " counter(page) " of " counter(pages);
      font-family: "Inter", sans-serif;
      font-size: 8pt;
      font-weight: 600;
      color: #0f172a;
    }
  }

  /* Reset Root Colors for Physical Ink */
  :root {
    --bg-paper: #ffffff !important;
    --bg-card: #f8fafc !important;
    --ink-primary: #000000 !important;
    --ink-secondary: #334155 !important;
    --ink-headings: #000000 !important;
    --border-subtle: #cbd5e1 !important;
    --border-strong: #94a3b8 !important;
  }

  body.handbook-body {
    background: #ffffff !important;
    color: #000000 !important;
    font-size: 10pt !important;
    line-height: 1.5 !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  /* Hide Interactive Web Chrome Elements */
  #reading-progress-bar,
  .mobile-header,
  #sidebar,
  #page-outline,
  .sidebar-toggle,
  .badge-edition,
  .sidebar-search,
  button,
  .no-print {
    display: none !important;
    visibility: hidden !important;
  }

  /* Full Width Content Layout */
  .book-shell {
    display: block !important;
  }

  .book-content {
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    box-shadow: none !important;
  }

  /* Chapter Breaks & Counters */
  .handbook-chapter {
    page-break-before: always !important;
    break-before: page !important;
    counter-increment: chapter;
  }

  .handbook-chapter:first-of-type {
    page-break-before: avoid !important;
    break-before: avoid !important;
  }

  /* Heading Formatting & Page Break Safety */
  h1 {
    font-size: 18pt !important;
    margin-top: 0 !important;
    padding-top: 10pt !important;
    border-bottom: 1.5pt solid #000000 !important;
    page-break-after: avoid !important;
    break-after: avoid !important;
  }

  h2 {
    font-size: 14pt !important;
    margin-top: 14pt !important;
    border-bottom: 0.75pt solid #64748b !important;
    page-break-after: avoid !important;
    break-after: avoid !important;
  }

  h3 {
    font-size: 11.5pt !important;
    margin-top: 12pt !important;
    page-break-after: avoid !important;
    break-after: avoid !important;
  }

  /* Paragraphs & Strict Orphan Prevention */
  p, li {
    orphans: 3 !important;
    widows: 3 !important;
  }

  /* Non-Breaking Equation Displays */
  .katex-display {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    margin: 8pt 0 !important;
    padding: 4pt 0 !important;
  }

  .katex {
    font-size: 1.05em !important;
  }

  /* Non-Breaking Callout Cards & Tables */
  .card-callout,
  .card-trap,
  .card-tip,
  .card-derivation,
  .card-pyq,
  table,
  figure,
  .diagram-container {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    border-radius: 4px !important;
    box-shadow: none !important;
  }

  .card-callout {
    border: 1pt solid #cbd5e1 !important;
    border-left: 3.5pt solid #000000 !important;
    background-color: #f8fafc !important;
    padding: 8pt 10pt !important;
    margin: 10pt 0 !important;
  }

  .card-trap {
    border-left-color: #dc2626 !important;
    background-color: #fef2f2 !important;
  }

  .card-pyq {
    border-left-color: #d97706 !important;
    background-color: #fffbeb !important;
  }

  /* Force Open All Collapsible Derivations in Print */
  details.derivation-fold {
    border: 0.5pt solid #cbd5e1 !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }

  details.derivation-fold[open],
  details.derivation-fold {
    display: block !important;
  }

  details.derivation-fold summary {
    font-weight: 700 !important;
    border-bottom: 0.5pt solid #cbd5e1 !important;
    margin-bottom: 6pt !important;
  }

  /* Tables: Crisp Borders and Repeated Table Headers */
  table {
    width: 100% !important;
    border-collapse: collapse !important;
    font-size: 8.5pt !important;
    margin: 10pt 0 !important;
  }

  thead {
    display: table-header-group !important;
  }

  tr {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }

  th, td {
    border: 0.5pt solid #94a3b8 !important;
    padding: 4pt 6pt !important;
    text-align: left !important;
  }

  th {
    background-color: #f1f5f9 !important;
    font-weight: 700 !important;
    color: #000000 !important;
  }

  /* High-Resolution Vector SVG Print Scaling */
  svg {
    max-width: 100% !important;
    height: auto !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
}
```

---

## 3.5 SVG Diagram Publication Standard & Visual Tokens

### 3.5.1 Publication Guidelines for Vector Physics Schematics
Every physics diagram embedded in the handbook must adhere to strict publication-grade vector standards:
1. **Responsive Viewbox:** All SVGs must specify `viewBox="0 0 W H"` with `width="100%"` and `style="max-width: ...px; height: auto;"` to enable seamless fluid scaling from mobile screens to high-resolution print.
2. **Non-Scaling Strokes:** Key lines and vectors must declare `vector-effect="non-scaling-stroke"` so lines maintain a crisp, uniform stroke weight regardless of browser zoom level or scaling.
3. **Typography Standard:** Embedded SVG text labels must use `font-family="Inter, -apple-system, sans-serif"` or `font-family="Merriweather, serif"` with clear contrast against backgrounds.
4. **Color Tokens Mapping:**
   - Backgrounds: Transparent or `#fcfaf2` (warm cream).
   - Coordinate Axes & Reference Lines: `#475569` (slate 600), stroke width 1.5px.
   - Mechanical Bodies (Blocks, Cylinders, Rods): Fill `#f1f5f9` (subtle slate), stroke `#334155` (slate 700, 2px).
   - Force Vectors: `#ef4444` (crimson red, 2.5px with `marker-end="url(#arrow-red)"`).
   - Velocity Vectors: `#0284c7` (cyan blue, 2px with `marker-end="url(#arrow-blue)"`).
   - Acceleration Vectors: `#dc2626` (dashed red, 2px).
   - Angular Quantities ($\omega, \alpha$): `#7c3aed` (vibrant purple arc with arrowhead).
   - Equilibrium Pivots & Hinges: `#059669` (emerald green).

### 3.5.2 Reusable Vector Marker Definitions
Every SVG includes a standard `<defs>` block defining crisp, standardized arrowheads:
```xml
<defs>
  <!-- Force Vector Arrowhead (Crimson Red) -->
  <marker id="arrow-force" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444"/>
  </marker>

  <!-- Velocity Vector Arrowhead (Cyan Blue) -->
  <marker id="arrow-velocity" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7"/>
  </marker>

  <!-- Angular Rotation Arrowhead (Purple) -->
  <marker id="arrow-angular" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M 0 1 L 10 5 L 0 9 z" fill="#7c3aed"/>
  </marker>

  <!-- Dimension Line Double Arrowhead (Slate) -->
  <marker id="arrow-dimension" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto">
    <path d="M 0 2 L 5 5 L 0 8 z" fill="#64748b"/>
  </marker>
</defs>
```
""")
    return "\n\n".join(parts)

if __name__ == "__main__":
    tech_text = build_part_3()
    print(f"Technical Engine generated successfully. Total length: {len(tech_text)} characters, {len(tech_text.splitlines())} lines.")
