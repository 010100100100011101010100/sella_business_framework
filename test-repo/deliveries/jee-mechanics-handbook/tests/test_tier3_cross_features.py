"""
test_tier3_cross_features.py
Tier 3: Cross-Feature Interactions & Pairwise Combinations Test Suite.
Validates end-to-end integration and consistency across interconnected subsystems:
1. Navigation Anchors ↔ DOM IDs (Sidebar, TOC, Indexes, Footer)
2. KaTeX Typography ↔ Content Subsystems (Formulas, Traps, PYQs, Challenges, Physics Macros)
3. CSS Styling Tokens ↔ Semantic HTML Components (Cards, Tables, Callouts)
4. Print CSS Page-Breaks ↔ Chapter Boundaries & Expanding Solutions
5. Inline SVGs ↔ Figure Containers, Defs & Marker References
6. Strategic Tip Cards ↔ All 6 Curriculum Chapters

Total: 16 distinct test methods / assertions (>= 15 required).
"""

import re
import unittest
from typing import Set

from tests.handbook_parser import HandbookData


class TestTier3CrossFeatures(unittest.TestCase):
    """Pairwise cross-feature interactions and structural integrity tests."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance(reload=True)
        cls.html = cls.data.html_content
        cls.css = cls.data.css_content + "\n" + cls.data.print_css_content
        cls.js = cls.data.js_content
        cls.dom_ids = set(cls.data.get_all_ids())

    # -------------------------------------------------------------------------
    # Pair 1: Navigation Links ↔ Actual DOM IDs
    # -------------------------------------------------------------------------
    def test_t3_01_sidebar_navigation_anchors_resolve_to_dom_ids(self):
        """Cross 1: Every sidebar navigation link must resolve to a valid DOM element ID."""
        sidebar_hrefs = self.data.get_sidebar_hrefs()
        self.assertGreater(len(sidebar_hrefs), 0, "Sidebar must contain navigation anchor links.")
        broken_links = [h for h in sidebar_hrefs if h not in self.dom_ids]
        self.assertEqual(len(broken_links), 0,
                         f"Sidebar contains navigation links that do not resolve to DOM IDs: {broken_links}")

    def test_t3_02_trap_index_anchors_resolve_to_chapters(self):
        """Cross 2: NTA Trap Index anchors must resolve to valid chapter/section targets."""
        trap_index_m = re.search(r'<section[^>]*id=[\'"]trap-index[\'"][^>]*>(.*?)</section>', self.html, re.DOTALL)
        if trap_index_m:
            hrefs = re.findall(r'<a[^>]+href=[\'"]#([^\'"]+)[\'"]', trap_index_m.group(1))
            broken = [h for h in hrefs if h not in self.dom_ids]
            self.assertEqual(len(broken), 0, f"Trap index contains broken anchor links: {broken}")
        else:
            self.fail("Section #trap-index not found in index.html.")

    def test_t3_03_pyq_index_anchors_resolve_to_chapters(self):
        """Cross 3: Solved PYQ Index anchors must resolve to valid DOM targets."""
        pyq_index_m = re.search(r'<section[^>]*id=[\'"]pyq-index[\'"][^>]*>(.*?)</section>', self.html, re.DOTALL)
        if pyq_index_m:
            hrefs = re.findall(r'<a[^>]+href=[\'"]#([^\'"]+)[\'"]', pyq_index_m.group(1))
            broken = [h for h in hrefs if h not in self.dom_ids]
            self.assertEqual(len(broken), 0, f"PYQ index contains broken anchor links: {broken}")
        else:
            self.fail("Section #pyq-index not found in index.html.")

    def test_t3_04_toc_curriculum_blueprint_anchors_resolve(self):
        """Cross 4: Detailed Table of Contents anchors must resolve to valid DOM targets."""
        toc_m = re.search(r'<section[^>]*id=[\'"]toc[\'"][^>]*>(.*?)</section>', self.html, re.DOTALL)
        if toc_m:
            hrefs = re.findall(r'<a[^>]+href=[\'"]#([^\'"]+)[\'"]', toc_m.group(1))
            broken = [h for h in hrefs if h not in self.dom_ids]
            self.assertEqual(len(broken), 0, f"TOC contains broken anchor links: {broken}")
        else:
            self.fail("Section #toc not found in index.html.")

    def test_t3_05_footer_navigation_anchors_resolve(self):
        """Cross 5: Book footer quick-navigation links must resolve to valid DOM IDs."""
        footer_m = re.search(r'<footer[^>]*>(.*?)</footer>', self.html, re.DOTALL)
        if footer_m:
            hrefs = re.findall(r'<a[^>]+href=[\'"]#([^\'"]+)[\'"]', footer_m.group(1))
            broken = [h for h in hrefs if h not in self.dom_ids]
            self.assertEqual(len(broken), 0, f"Footer contains broken anchor links: {broken}")
        else:
            self.fail("Footer element not found in index.html.")

    # -------------------------------------------------------------------------
    # Pair 2: KaTeX Typesetting ↔ Physics Content Modules
    # -------------------------------------------------------------------------
    def test_t3_06_katex_physics_macros_defined(self):
        """Cross 6: Specialized physics macros must be configured in KaTeX setup."""
        all_code = self.html + "\n" + self.js
        required_macros = ["\\bm", "\\grad", "\\div", "\\curl", "\\dd", "\\Icm"]
        missing_macros = [m for m in required_macros if m not in all_code]
        self.assertEqual(len(missing_macros), 0,
                         f"KaTeX configuration is missing required physics macros: {missing_macros}")

    def test_t3_07_formula_tables_integrate_latex_math(self):
        """Cross 7: Formula tables in all 6 chapters must contain typeset LaTeX equations."""
        for ch_key, ch_data in self.data.chapters.items():
            content = ch_data.get("content", "")
            table_m = re.search(r'<table[^>]*>(.*?)</table>', content, re.DOTALL)
            self.assertIsNotNone(table_m, f"Formula table missing in {ch_key}.")
            has_latex = "$" in table_m.group(1) or "\\frac" in table_m.group(1)
            self.assertTrue(has_latex, f"{ch_key} formula table must contain LaTeX math markup.")

    def test_t3_08_trap_alert_cards_integrate_latex_math(self):
        """Cross 8: NTA Trap Alert cards in all 6 chapters must contain LaTeX mathematical expressions."""
        for ch_key, ch_data in self.data.chapters.items():
            traps = ch_data.get("trap_boxes", [])
            self.assertGreaterEqual(len(traps), 1, f"Traps missing in {ch_key}.")
            math_in_traps = any("$" in t for t in traps)
            self.assertTrue(math_in_traps, f"{ch_key} trap alert cards must contain LaTeX math markup.")

    def test_t3_09_pyq_step_solutions_integrate_latex_math(self):
        """Cross 9: Worked JEE Advanced PYQ solutions must contain multi-step LaTeX mathematical derivations."""
        for ch_key, ch_data in self.data.chapters.items():
            pyqs = ch_data.get("pyq_boxes", [])
            self.assertGreaterEqual(len(pyqs), 1, f"PYQs missing in {ch_key}.")
            math_in_pyqs = all("$" in p for p in pyqs[:3])
            self.assertTrue(math_in_pyqs, f"{ch_key} PYQs must contain LaTeX math derivations.")

    def test_t3_10_challenge_solutions_integrate_latex_math(self):
        """Cross 10: Practice challenge problem solutions must contain LaTeX mathematical solutions."""
        for ch_key, ch_data in self.data.chapters.items():
            challenges = ch_data.get("challenge_boxes", [])
            self.assertGreaterEqual(len(challenges), 1, f"Challenges missing in {ch_key}.")
            math_in_challenges = all("$" in c for c in challenges[:5])
            self.assertTrue(math_in_challenges, f"{ch_key} challenge solutions must contain LaTeX math derivations.")

    # -------------------------------------------------------------------------
    # Pair 3: CSS Styling Tokens ↔ Semantic Card Classes
    # -------------------------------------------------------------------------
    def test_t3_11_css_card_classes_correspond_to_theme_tokens(self):
        """Cross 11: Classes (.trap-card, .tip-card, .pyq-box, .challenge-box) must be defined in CSS."""
        required_classes = ["trap-card", "tip-card", "pyq-box", "challenge-box", "formula-table"]
        for cls_name in required_classes:
            pattern = rf'\.{cls_name}\b'
            self.assertTrue(bool(re.search(pattern, self.css)),
                            f"CSS must define rules for styling class '.{cls_name}'.")

    # -------------------------------------------------------------------------
    # Pair 4: Print Stylesheet ↔ Chapter Layout & Solution Details
    # -------------------------------------------------------------------------
    def test_t3_12_css_print_page_break_applies_to_chapters(self):
        """Cross 12: Print CSS rules must enforce forced page breaks on chapter containers or titles."""
        has_chapter_break = bool(re.search(
            r'(?:\.chapter|\.chapter-container|h1\.chapter-title)[^{]*\{[^}]*(?:page-break-before|break-before)\s*:\s*(?:always|page)',
            self.css
        ))
        self.assertTrue(has_chapter_break,
                        "Print CSS must bind page-break-before: always to chapter elements (.chapter, h1.chapter-title).")

    def test_t3_13_challenge_details_expanded_in_print_mode(self):
        """Cross 13: Print CSS must override challenge solutions visibility so printed books show full solutions."""
        has_print_override = bool(re.search(
            r'(?:\.challenge-solution|\.challenge-details)[^{]*\{[^}]*display\s*:\s*block',
            self.css
        ))
        self.assertTrue(has_print_override,
                        "Print CSS must ensure challenge solutions are rendered with display: block in print mode.")

    # -------------------------------------------------------------------------
    # Pair 5: Visual Blueprints ↔ Inline SVGs, Containers & Markers
    # -------------------------------------------------------------------------
    def test_t3_14_inline_svgs_wrapped_in_diagram_containers_with_captions(self):
        """Cross 14: All 6 chapters must enclose their SVG diagrams in a container with a descriptive caption."""
        for ch_key, ch_data in self.data.chapters.items():
            content = ch_data.get("content", "")
            has_diagram = ('class="diagram-container"' in content or 'class="diagram-figure"' in content or
                           '<figure' in content)
            self.assertTrue(has_diagram, f"{ch_key} inline SVG must be enclosed in a diagram container.")
            has_caption = ('class="diagram-caption"' in content or '<figcaption' in content)
            self.assertTrue(has_caption, f"{ch_key} diagram must have an accompanying caption.")

    def test_t3_15_svg_marker_references_resolve_to_defs(self):
        """Cross 15: All marker-end/marker-start url(#id) references in SVGs must resolve to <marker id=...> in defs."""
        markers_used = re.findall(r'url\(#([^\)]+)\)', self.html)
        self.assertGreater(len(markers_used), 0, "SVGs must utilize vector markers for arrows/vectors.")
        defined_markers = set(re.findall(r'<marker[^>]+id=[\'"]([^\'"]+)[\'"]', self.html))
        broken_markers = [m for m in markers_used if m not in defined_markers]
        self.assertEqual(len(broken_markers), 0,
                         f"SVG diagrams contain marker references that do not resolve to <defs>: {broken_markers}")

    # -------------------------------------------------------------------------
    # Pair 6: Executive Strategic Guidance ↔ All 6 Chapters
    # -------------------------------------------------------------------------
    def test_t3_16_strategic_tip_cards_present_in_all_chapters(self):
        """Cross 16: Every chapter must lead with an executive strategic weightage and focus callout card."""
        for ch_key, ch_data in self.data.chapters.items():
            content = ch_data.get("content", "")
            has_tip = ('class="card-box tip-card"' in content or 'class="tip-card"' in content or
                       'card-header-tip' in content)
            self.assertTrue(has_tip, f"{ch_key} must begin with a strategic JEE weightage tip callout card.")


if __name__ == "__main__":
    unittest.main()
