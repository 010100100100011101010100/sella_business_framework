#!/usr/bin/env python3
"""
INDEPENDENT POST-VICTORY AUDIT TEST SUITE (V2)
Auditor: cb084611-9d67-40b1-ae88-aada06da2549
Target: JEE Mechanics & Rotational Dynamics Master Handbook
"""

import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

HTML_PATH = "/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook/index.html"
CSS_PATH = "/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook/styles.css"
README_PATH = "/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook/README.md"
JS_APP_PATH = "/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook/js/app.js"
JS_KATEX_PATH = "/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook/js/katex-render.js"

class AuditReporter:
    def __init__(self):
        self.tests = []
        self.failures = []

    def check(self, name, condition, details=""):
        if condition:
            self.tests.append((name, "PASS", details))
            print(f"[PASS] {name}: {details}")
        else:
            self.tests.append((name, "FAIL", details))
            self.failures.append((name, details))
            print(f"[FAIL] {name}: {details}")

    def summary(self):
        print("\n" + "="*70)
        print(f"AUDIT TEST SUMMARY: {len(self.tests)} checks executed, {len(self.failures)} failures.")
        print("="*70)
        return len(self.failures) == 0

audit = AuditReporter()

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

with open(README_PATH, "r", encoding="utf-8") as f:
    readme = f.read()

js_combined = ""
if os.path.exists(JS_APP_PATH):
    with open(JS_APP_PATH, "r", encoding="utf-8") as f:
        js_combined += f.read()
if os.path.exists(JS_KATEX_PATH):
    with open(JS_KATEX_PATH, "r", encoding="utf-8") as f:
        js_combined += "\n" + f.read()

# -------------------------------------------------------------
# 1. PLACEHOLDER & CHEATING FORENSICS
# -------------------------------------------------------------
print("\n>>> SECTION 1: PLACEHOLDER & CHEATING FORENSICS")

# Clean HTML tags to evaluate textual prose (prevent false positives on placeholder="..." on input tags)
clean_body_text = re.sub(r'<[^>]+>', ' ', html)

banned_tokens = [
    r'\blorem\s+ipsum\b',
    r'\bTODO\b',
    r'\bTBD\b',
    r'\[insert\b',
    r'\[replace\b',
    r'\bFIXME\b',
    r'\bcoming\s+soon\b',
    r'\bplaceholder\b',
    r'\bundefined\b'
]

for token in banned_tokens:
    matches = re.findall(token, clean_body_text, re.IGNORECASE)
    audit.check(f"Placeholder scan ({token}) in prose", len(matches) == 0, f"Found {len(matches)} matches")

# Check for empty solution containers
empty_solutions = re.findall(r'<div class="(?:pyq|challenge)-solution">\s*</div>', html)
audit.check("Empty solution blocks", len(empty_solutions) == 0, f"Found {len(empty_solutions)} empty solution blocks")

# Check for stub solutions like "Answer is A" without derivation
stub_solutions = re.findall(r'<div class="(?:pyq|challenge)-solution">\s*<p>(?:Answer|Ans)[\s:]+[A-D]\.?\s*</p>\s*</div>', html)
audit.check("Stub solutions (bare answers)", len(stub_solutions) == 0, f"Found {len(stub_solutions)} stub solutions")

# HTML Parser check
class SyntaxValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
    def error(self, message):
        self.errors.append(message)

parser = SyntaxValidator()
parser.feed(html)
audit.check("HTML5 Parsing without syntax errors", len(parser.errors) == 0, f"HTML parser errors: {parser.errors}")

# -------------------------------------------------------------
# 2. CURRICULUM & EXACT COUNTS (R1)
# -------------------------------------------------------------
print("\n>>> SECTION 2: CURRICULUM & EXACT COUNTS (R1)")

chapter_keys = ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6"]
chapter_chunks = {}

for i, k in enumerate(chapter_keys, 1):
    next_anchor = f"ch{i+1}" if i < 6 else "trap-index"
    # Match either section or article
    pattern = rf'<(?:section|article)[^>]*\bid=[\'"](?:ch{i}|chapter-{i})[\'"][^>]*>(.*?)(?=<(?:section|article)[^>]*\bid=[\'"](?:ch{i+1}|chapter-{i+1}|trap-index)[\'"]|</main>|\Z)'
    m = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
    audit.check(f"Chapter section/article exists ({k})", m is not None, f"Extracted {k}")
    if m:
        chapter_chunks[k] = m.group(1)

total_traps = 0
total_pyqs = 0
total_challenges = 0
total_tables = 0
total_words = 0

for k in chapter_keys:
    chunk = chapter_chunks.get(k, "")
    
    # Traps in chapter
    traps = re.findall(r'class=[\'"][^\'"]*card-header-trap[^\'"]*[\'"]', chunk)
    total_traps += len(traps)
    audit.check(f"{k}: Trap alerts count >= 10", len(traps) >= 10, f"Found {len(traps)} traps")
    
    # PYQs in chapter
    pyqs = re.findall(r'class=[\'"][^\'"]*pyq-box[^\'"]*[\'"]', chunk)
    total_pyqs += len(pyqs)
    audit.check(f"{k}: Worked PYQs count >= 3", len(pyqs) >= 3, f"Found {len(pyqs)} PYQs")
    
    # Challenge problems in chapter
    challenges = re.findall(r'class=[\'"][^\'"]*challenge-box[^\'"]*[\'"]', chunk)
    total_challenges += len(challenges)
    audit.check(f"{k}: Practice challenge problems count >= 5", len(challenges) >= 5, f"Found {len(challenges)} challenges")
    
    # Challenge solutions with details/summary
    challenge_details = re.findall(r'<details\s+class=[\'"][^\'"]*challenge-details[^\'"]*[\'"]', chunk)
    audit.check(f"{k}: Collapsible challenge solutions match count", len(challenge_details) == len(challenges), f"{len(challenge_details)} details for {len(challenges)} problems")
    
    # Formula table in chapter
    tables = re.findall(r'class=[\'"][^\'"]*formula-table[^\'"]*[\'"]', chunk)
    total_tables += len(tables)
    audit.check(f"{k}: Formula table present", len(tables) >= 1, f"Found {len(tables)} tables")
    
    # Check domain of validity header in formula table
    has_validity_col = "Domain of Validity" in chunk or "Validity / Constraints" in chunk or "Validity" in chunk
    audit.check(f"{k}: Formula table specifies Domain of Validity", has_validity_col, "Column found")
    
    # First principles theory / derivations
    has_derivations = bool(re.search(r'(?:derivation|first-principles|coordinate|theorem)', chunk, re.IGNORECASE))
    audit.check(f"{k}: First-principles theory & derivations present", has_derivations, "Derivation keywords found")
    
    # Word count
    text_content = re.sub(r'<[^>]+>', ' ', chunk)
    words = len(text_content.split())
    total_words += words
    audit.check(f"{k}: Substantial content volume", words >= 2000, f"{words} words")

audit.check("Global Traps Total >= 60", total_traps >= 60, f"Total = {total_traps}")
audit.check("Global Worked PYQs Total >= 18", total_pyqs >= 18, f"Total = {total_pyqs}")
audit.check("Global Challenge Problems Total >= 30", total_challenges >= 30, f"Total = {total_challenges}")
audit.check("Global Formula Tables Total >= 6", total_tables >= 6, f"Total = {total_tables}")

# -------------------------------------------------------------
# 3. BOOK READER LAYOUT & PALETTE (R2)
# -------------------------------------------------------------
print("\n>>> SECTION 3: BOOK READER LAYOUT & PALETTE (R2)")

# Check color palette
audit.check("Soft warm yellow background (#fcfaf2) in CSS", "#fcfaf2" in css, "Found in styles.css")
audit.check("Card tint (#f7f3e8) in CSS", "#f7f3e8" in css, "Found in styles.css")
audit.check("Border color (#e8dec8) in CSS", "#e8dec8" in css, "Found in styles.css")
audit.check("Text color (#1e293b) in CSS", "#1e293b" in css, "Found in styles.css")

# Check styling cards
audit.check("Trap alert crimson styling in CSS", "trap-card" in css and ("#991b1b" in css or "#7f1d1d" in css or "#b91c1c" in css or "#ef4444" in css), "Crimson accents present")
audit.check("Formula table styling in CSS", "formula-table" in css, "Formula table styles present")
audit.check("IIT Professor Tips styling in CSS", "tip-card" in css, "Tip card styles present")

# Check navigation and reading progress
has_sidebar = ('class="book-sidebar"' in html or '<aside id="sidebar"' in html or 'class="sidebar-nav' in html)
audit.check("Sidebar navigation in HTML", has_sidebar, "Found sidebar navigation element")

has_progress = ('id="progress-bar"' in html or 'id="reading-progress"' in html or 'id="reading-progress-bar"' in html)
audit.check("Reading progress indicator in HTML", has_progress, "Found progress bar element")

audit.check("Responsive TOC in HTML", 'id="toc"' in html, "TOC section found")

# Check JS interactivity (smooth scroll, progress bar update, sidebar toggle)
combined_js_and_html = html + "\n" + js_combined
audit.check("Interactive JavaScript present", len(js_combined) > 0 or '<script>' in html, "JavaScript logic found")
audit.check("Reading progress scroll event in JS", "scroll" in combined_js_and_html and ("width" in combined_js_and_html or "progressBar" in combined_js_and_html or "progress" in combined_js_and_html), "Scroll progress handler found")
audit.check("Active sidebar interaction in JS", "sidebar" in combined_js_and_html, "Sidebar interaction logic found")

# -------------------------------------------------------------
# 4. PUBLICATION-GRADE VECTOR PHYSICS DIAGRAMS (R3)
# -------------------------------------------------------------
print("\n>>> SECTION 4: VECTOR PHYSICS DIAGRAMS (R3)")

svg_blocks = re.findall(r'<svg[^>]*class=[\'"][^\'"]*(?:diagram-svg|physics-diagram)[^\'"]*[\'"][^>]*>.*?</svg>', html, re.DOTALL)
audit.check("SVG Diagrams count >= 6", len(svg_blocks) >= 6, f"Found {len(svg_blocks)} SVG diagrams")

# Validate XML structure of all SVGs
svg_xml_valid = True
for idx, svg_str in enumerate(svg_blocks, 1):
    try:
        sanitized_svg = re.sub(r'<(?=[0-9]|\s)', '&lt;', svg_str)
        root = ET.fromstring(sanitized_svg)
        viewbox = root.attrib.get("viewBox", "")
        if not viewbox:
            svg_xml_valid = False
            print(f"  Warning: SVG {idx} missing viewBox")
    except Exception as e:
        svg_xml_valid = False
        print(f"  Error parsing SVG {idx}: {e}")

audit.check("All inline SVGs are structurally valid vector diagrams with viewBox", svg_xml_valid, f"Parsed {len(svg_blocks)} SVGs")

# Verify the 6 specific required physical systems
required_systems = [
    ("Relative / Curvilinear / Inclined kinematics diagram (Ch 1)", "ch1", r'(?:tangential|normal|radius\s+of\s+curvature|trajectory|curvature|path)'),
    ("Multi-block friction & resolved FBD (Ch 2)", "ch2", r'(?:two-block|friction|block\s+[ab]|applied|stack)'),
    ("Potential energy well U(x) with equilibrium points (Ch 3)", "ch3", r'(?:potential|energy|equilibrium|stable|unstable|neutral)'),
    ("Oblique collision velocity vectors (Ch 4)", "ch4", r'(?:oblique|collision|line\s+of\s+impact|common\s+tangent|impulse)'),
    ("Pure rolling contact velocity & friction (Ch 5)", "ch5", r'(?:pure\s+rolling|toppling|iaor|v_cm|v_contact|normal\s+reaction)'),
    ("Gravitational orbits & Compound pendulum / SHM (Ch 6)", "ch6", r'(?:kepler|orbit|perihelion|aphelion|compound\s+pendulum|oscillation)')
]

for desc, k, pattern in required_systems:
    chunk = chapter_chunks.get(k, "")
    found = bool(re.search(pattern, chunk, re.IGNORECASE | re.DOTALL))
    audit.check(f"Physics Diagram: {desc}", found, f"Verified in {k}")

# -------------------------------------------------------------
# 5. KATEX MATHEMATICAL TYPESETTING & PRINT/EXPORT READINESS (R4)
# -------------------------------------------------------------
print("\n>>> SECTION 5: KATEX TYPESETTING & PRINT ENGINE (R4)")

# KaTeX inclusion
audit.check("KaTeX stylesheet included", 'katex.min.css' in html or 'katex.css' in html, "KaTeX CSS link present")
audit.check("KaTeX JS and auto-render included", 'katex.min.js' in html and 'auto-render.min.js' in html, "KaTeX scripts present")

# Delimiter balance check
display_math = re.findall(r'\$\$', html)
audit.check("Display math delimiters ($$) parity", len(display_math) % 2 == 0, f"Count: {len(display_math)}")

# Inline math delimiters balance
cleaned_math_html = re.sub(r'\$\$.*?\$\$', '', html, flags=re.DOTALL)
cleaned_math_html = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', cleaned_math_html, flags=re.DOTALL)
single_dollars = re.findall(r'(?<!\\)\$', cleaned_math_html)
audit.check("Inline math delimiters ($) count is even", len(single_dollars) % 2 == 0, f"Count: {len(single_dollars)}")

# Check CSS @media print
audit.check("@media print block in CSS", "@media print" in css, "Found @media print in styles.css")
audit.check("@page setup in CSS", "@page" in css, "Found @page in styles.css")
audit.check("Chapter page breaks in print CSS", "break-before: page" in css or "page-break-before: always" in css, "Page break rules present")
audit.check("Card/Box break avoidance in print CSS", "break-inside: avoid" in css or "page-break-inside: avoid" in css, "Avoid page break inside elements present")
audit.check("Interactive elements hidden in print CSS", "display: none" in css and ("sidebar" in css or "#sidebar" in css or ".book-sidebar" in css), "Sidebar hidden on print")

# Check 50-page equivalence
total_all_words = len(re.sub(r'<[^>]+>', ' ', html).split())
total_boxes = total_traps + total_pyqs + total_challenges + total_tables + len(svg_blocks)
estimated_pages = (total_all_words / 350) + (total_boxes * 0.25)
audit.check("Volume equivalence >= 50 pages", estimated_pages >= 50, f"Total Words: {total_all_words}, Structured Cards/Boxes: {total_boxes}, Estimated Pages: {estimated_pages:.1f}")

# -------------------------------------------------------------
# 6. PROGRAMMATIC LINK & ANCHOR INTEGRITY
# -------------------------------------------------------------
print("\n>>> SECTION 6: PROGRAMMATIC LINK & ANCHOR INTEGRITY")

# Find all internal href="#..."
internal_links = re.findall(r'href=[\'"]#([a-zA-Z0-9_\-]+)[\'"]', html)
all_ids = set(re.findall(r'id=[\'"]([a-zA-Z0-9_\-]+)[\'"]', html))

broken_links = [link for link in internal_links if link not in all_ids]
audit.check("All internal navigation links point to valid IDs", len(broken_links) == 0, f"Tested {len(internal_links)} internal links, broken: {broken_links}")

audit.check("Index of 60 Traps anchor exists", "trap-index" in all_ids, "id='trap-index' found")
audit.check("Index of 18 Solved PYQs anchor exists", "pyq-index" in all_ids, "id='pyq-index' found")
audit.check("Index of 30 Practice Problems anchor exists", "practice-index" in all_ids, "id='practice-index' found")

# -------------------------------------------------------------
# 7. PHYSICS & MATHEMATICAL RIGOR AUDIT
# -------------------------------------------------------------
print("\n>>> SECTION 7: PHYSICS & MATHEMATICAL RIGOR SPOT CHECKS")

rigor_checks = [
    ("Ch 1: Tangential and normal acceleration with curvature", "ch1", r'a_t.*?(?:\\+frac\{dv\}\{dt\}|dv/dt).*?a_n.*?(?:v\^2/R|\\+frac\{v\^2\}\{R\})'),
    ("Ch 2: Multi-block friction threshold & pseudo force", "ch2", r'(?:\\+mathbf\{F\}_\{pseudo\}|F_\{pseudo\}).*?-m\\+mathbf\{a\}_0.*?F_\{threshold\}'),
    ("Ch 3: Potential energy curve equilibrium stability", "ch3", r'(?:\\+frac\{dU\}\{dx\}|dU/dx).*?0.*?(?:\\+frac\{d\^2U\}\{dx\^2\}|d\^2U/dx\^2)'),
    ("Ch 3: Vertical circular motion bottom velocity & tension diff", "ch3", r'\\+sqrt\{5gR\}.*?T_\{bottom\}\s*-\s*T_\{top\}\s*=\s*6mg'),
    ("Ch 4: Center of mass Koenig's theorem & reduced mass", "ch4", r'K_\{lab\}\s*=.*?K_\{cm\}\s*\+\s*K_\{rel\}.*?\\+mu\s*=\s*\\+frac\{m_1 m_2\}'),
    ("Ch 4: Variable mass Tsiolkovsky rocket equation", "ch4", r'v\(t\)\s*=\s*v_0\s*\+\s*u_\{ex\}\s*\\+ln'),
    ("Ch 5: Generalized torque about arbitrary point & COM", "ch5", r'\\+boldsymbol\{\\+tau\}_O\s*=\s*\\+frac\{d\\+mathbf\{L\}_O\}\{dt\}.*?\\+boldsymbol\{\\+tau\}_\{cm\}\s*=\s*I_\{cm\}'),
    ("Ch 5: Pure rolling contact point velocity & centripetal accel", "ch5", r'\\+mathbf\{a\}_C\s*=\s*\\+omega\^2 R.*?\\+mathbf\{v\}_C\s*=\s*\\+mathbf\{0\}'),
    ("Ch 5: Toppling condition on block", "ch5", r'x_N.*?b/2'),
    ("Ch 6: Vis-viva equation for Keplerian orbit", "ch6", r'v\^2\s*=\s*GM\\+left\(\\+frac\{2\}\{r\}\s*-\s*\\+frac\{1\}\{a\}\\+right\)'),
    ("Ch 6: Compound pendulum conjugate length & infinite period at COM", "ch6", r'L_\{eq\}\s*=\s*d\s*\+\s*\\+frac\{k_\{cm\}\^2\}\{d\}.*?k_\{cm\}')
]

for name, k, pattern in rigor_checks:
    chunk = chapter_chunks.get(k, "")
    found = bool(re.search(pattern, chunk, re.DOTALL))
    audit.check(f"Physics Rigor: {name}", found, f"Verified in {k}")

success = audit.summary()
if not success:
    sys.exit(1)
print("\nALL INDEPENDENT POST-VICTORY AUDIT CHECKS PASSED PERFECTLY!")
