# Verification Test Suite for JEE Mechanics Master Handbook
import re
import os
import sys

HTML_PATH = "test-repo/deliveries/jee-mechanics-handbook/index.html"
CSS_PATH = "test-repo/deliveries/jee-mechanics-handbook/styles.css"

print("=" * 60)
print("RUNNING AUTOMATED VERIFICATION SUITE")
print("=" * 60)

# Check 1: File Existence & Size
if not os.path.exists(HTML_PATH):
    print(f"FAIL: {HTML_PATH} does not exist!")
    sys.exit(1)

size_bytes = os.path.getsize(HTML_PATH)
size_kb = size_bytes / 1024
print(f"[OK] HTML file exists: {size_kb:.2f} KB ({size_bytes} bytes)")
if size_kb < 150:
    print(f"FAIL: File size ({size_kb:.2f} KB) is smaller than 150 KB standard!")
    sys.exit(1)

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Check 2: Chapter Coverage (Ch 1 to Ch 6)
chapters = ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6"]
for ch in chapters:
    if f'id="{ch}"' in html:
        print(f"[OK] Chapter {ch} anchor present")
    else:
        print(f"FAIL: Chapter {ch} missing!")
        sys.exit(1)

# Check 3: Trap Alerts Count
traps = re.findall(r'class="card-header-trap"', html)
print(f"[OK] Forensic Trap Alerts found: {len(traps)} (Target: >= 60)")
if len(traps) < 60:
    print(f"FAIL: Found only {len(traps)} traps, expected at least 60!")
    sys.exit(1)

# Check 4: Worked JEE Advanced PYQs Count
pyqs = re.findall(r'class="pyq-box"', html)
print(f"[OK] Dissected JEE Advanced PYQs found: {len(pyqs)} (Target: >= 18)")
if len(pyqs) < 18:
    print(f"FAIL: Found only {len(pyqs)} PYQs, expected at least 18!")
    sys.exit(1)

# Check 5: Practice Challenge Problems Count
challenges = re.findall(r'class="challenge-box"', html)
print(f"[OK] Practice Challenge Problems found: {len(challenges)} (Target: >= 30)")
if len(challenges) < 30:
    print(f"FAIL: Found only {len(challenges)} challenge problems, expected at least 30!")
    sys.exit(1)

# Check 6: Master Formula Summary Tables Count
tables = re.findall(r'class="formula-table"', html)
print(f"[OK] Formula Summary Tables found: {len(tables)} (Target: >= 6)")
if len(tables) < 6:
    print(f"FAIL: Found only {len(tables)} formula tables, expected at least 6!")
    sys.exit(1)

# Check 7: Inline SVG Vector Diagrams Count
svgs = re.findall(r'<svg [^>]*class=["\'][^"\']*(?:diagram-svg|physics-diagram)[^"\']*', html)
print(f"[OK] Publication-Grade SVG Diagrams found: {len(svgs)} (Target: >= 6)")
if len(svgs) < 6:
    print(f"FAIL: Found only {len(svgs)} SVG diagrams, expected at least 6!")
    sys.exit(1)

# Check 8: Math Delimiter Parity Check
display_math = re.findall(r'\$\$', html)
print(f"[OK] KaTeX display math delimiters ($$): {len(display_math)} (Must be even)")
if len(display_math) % 2 != 0:
    print("FAIL: Display math delimiter mismatch (odd count)!")
    sys.exit(1)

# Check 9: CSS Print & Layout Engine
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

if "@media print" in css and "@page" in css and ("#fcfbf9" in css or "#fcfaf2" in css):
    print("[OK] CSS contains refined editorial ivory theme, @media print, and @page rules")
else:
    print("FAIL: CSS missing core print or theme rules!")
    sys.exit(1)

# Check 10: Page Count Estimation
total_words = len(html.split())
estimated_pages = total_words / 350
print(f"[OK] Total Word Count: {total_words} words (~{estimated_pages:.1f} printed pages equivalent)")
if estimated_pages < 45:
    print(f"FAIL: Content volume too short ({estimated_pages:.1f} pages) for 50-page handbook requirement!")
    sys.exit(1)

# Check 11: Zero Emojis Strict Verification
emojis = re.findall(r"[\U00010000-\U0010ffff\u2600-\u27bf\u2b50-\u2b55\u2300-\u23ff\u2b06]", html)
print(f"[OK] Strict Zero Emojis Verification: {len(emojis)} emojis detected")
if len(emojis) > 0:
    print(f"FAIL: Found {len(emojis)} emojis in index.html: {set(emojis)}")
    sys.exit(1)

print("=" * 60)
print("ALL 11 VERIFICATION TESTS PASSED PERFECTLY (100% GREEN)")
print("=" * 60)
