import os
import re
import sys

HTML_PATH = "/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook/index.html"
CSS_PATH = "/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook/styles.css"
README_PATH = "/Users/shera/Desktop/business_framework/test-repo/deliveries/jee-mechanics-handbook/README.md"

print("Loading files...")
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_text = f.read()

with open(CSS_PATH, "r", encoding="utf-8") as f:
    css_text = f.read()

print(f"HTML Size: {len(html_text)} bytes, {len(html_text.splitlines())} lines")
print(f"CSS Size: {len(css_text)} bytes, {len(css_text.splitlines())} lines")

# Split by <section id="ch[1-6]"
chapter_ids = ["ch1", "ch2", "ch3", "ch4", "ch5", "ch6"]
chapters = {}

for i, ch_id in enumerate(chapter_ids):
    next_id = chapter_ids[i+1] if i + 1 < len(chapter_ids) else "trap-index"
    pattern = rf'(<section id="{ch_id}" class="chapter-container">.*?)(?=<section id="{next_id}")'
    m = re.search(pattern, html_text, re.DOTALL)
    if m:
        chapters[ch_id] = m.group(1)
    else:
        print(f"ERROR: Could not isolate chapter {ch_id}")

print(f"\n--- CHAPTERS ISOLATED: {len(chapters)} ---")

per_chapter_results = []

for ch_id, ch_body in chapters.items():
    title_m = re.search(r'<h2[^>]*>(.*?)</h2>', ch_body)
    title = title_m.group(1) if title_m else "No title"
    title_clean = re.sub(r'<[^>]+>', '', title).strip()
    
    traps = re.findall(r'class="card-header-trap"', ch_body)
    trap_titles = re.findall(r'<div class="card-header-trap">(.*?)</div>', ch_body)
    pyqs = re.findall(r'class="pyq-box"', ch_body)
    pyq_titles = re.findall(r'<div class="pyq-header">(.*?)</div>', ch_body)
    challenges = re.findall(r'class="challenge-box"', ch_body)
    challenge_titles = re.findall(r'<div class="challenge-header">(.*?)</div>', ch_body)
    tables = re.findall(r'class="formula-table"', ch_body)
    tips = re.findall(r'class="tip-card"', ch_body)
    svgs = re.findall(r'<svg[^>]*class="diagram-svg"[^>]*>', ch_body)
    
    # Check derivations/subsections
    subsections = re.findall(r'<h3[^>]*>(.*?)</h3>', ch_body)
    
    # Words in chapter
    clean_text = re.sub(r'<[^>]+>', ' ', ch_body)
    words = len(clean_text.split())
    
    res = {
        "id": ch_id,
        "title": title_clean,
        "words": words,
        "traps": len(traps),
        "pyqs": len(pyqs),
        "challenges": len(challenges),
        "tables": len(tables),
        "tips": len(tips),
        "svgs": len(svgs),
        "subsections": [re.sub(r'<[^>]+>', '', s).strip() for s in subsections],
        "trap_titles": [re.sub(r'<[^>]+>', '', t).strip() for t in trap_titles[:3]],
        "pyq_titles": [re.sub(r'<[^>]+>', '', p).strip() for p in pyq_titles],
        "challenge_titles": [re.sub(r'<[^>]+>', '', c).strip() for c in challenge_titles]
    }
    per_chapter_results.append(res)
    
    print(f"\n{ch_id.upper()}: {title_clean}")
    print(f"  Word count: {words}")
    print(f"  Subsections ({len(subsections)}): {[re.sub(r'<[^>]+>', '', s).strip() for s in subsections]}")
    print(f"  Trap Alerts count: {len(traps)} (Target: >=10) -> {'PASS' if len(traps) >= 10 else 'FAIL'}")
    print(f"  PYQs count: {len(pyqs)} (Target: >=3) -> {'PASS' if len(pyqs) >= 3 else 'FAIL'}")
    print(f"  Challenges count: {len(challenges)} (Target: >=5) -> {'PASS' if len(challenges) >= 5 else 'FAIL'}")
    print(f"  Formula Tables count: {len(tables)} (Target: >=1) -> {'PASS' if len(tables) >= 1 else 'FAIL'}")
    print(f"  SVGs count: {len(svgs)}")
    print(f"  PYQs: {[re.sub(r'<[^>]+>', '', p).strip() for p in pyq_titles]}")

# Global checks
print("\n" + "="*60)
print("GLOBAL SUMMARY AUDIT")
print("="*60)
total_words = sum(r["words"] for r in per_chapter_results)
total_traps = sum(r["traps"] for r in per_chapter_results)
total_pyqs = sum(r["pyqs"] for r in per_chapter_results)
total_challenges = sum(r["challenges"] for r in per_chapter_results)
total_tables = sum(r["tables"] for r in per_chapter_results)
total_svgs = sum(r["svgs"] for r in per_chapter_results)

print(f"Total Words (all 6 chapters): {total_words}")
print(f"Estimated Book Pages (@ 400 words/page): {total_words / 400:.1f}")
print(f"Total Traps: {total_traps} (Target: >= 60)")
print(f"Total PYQs: {total_pyqs} (Target: >= 18)")
print(f"Total Challenges: {total_challenges} (Target: >= 30)")
print(f"Total Tables: {total_tables} (Target: >= 6)")
print(f"Total SVGs: {total_svgs} (Target: >= 6)")
