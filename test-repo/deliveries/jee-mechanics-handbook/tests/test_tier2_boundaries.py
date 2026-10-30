"""
test_tier2_boundaries.py
Tier 2: Boundary Value Analysis & Stress Thresholds Test Suite.
Validates exact boundary conditions across all 9 features:
1. Book Reader Shell & Aesthetics Boundaries (exact palette tokens, viewport settings)
2. KaTeX Typography & Math Boundaries (delimiter balance, non-empty math, error handling)
3. Print CSS Boundaries (running page counters, page-break avoidance, print colors)
4-9. Chapters 1-6 Boundaries (trap numbering continuity, formula validity completeness,
     challenge solutions depth, zero placeholders, chapter word counts)
10. Global Volume Boundaries (total word count > 25,000 words, exact counts of 60 traps, 18 PYQs, 30 challenges)

Total: 50 distinct test methods / assertions (>= 45 required).
"""

import re
import unittest
from typing import List

from tests.handbook_parser import HandbookData


class TestTier2Feature1ShellBoundaries(unittest.TestCase):
    """Feature 1 Boundaries: Aesthetic color tokens and viewport specifications."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance(reload=True)
        cls.css = cls.data.css_content

    def test_t2_01_bg_paper_color_token(self):
        """Boundary: Base paper background must match exact warm cream hex #fcfaf2."""
        m = re.search(r'--bg-paper\s*:\s*([^;]+);', self.css)
        self.assertIsNotNone(m, "CSS must define custom property --bg-paper.")
        val = m.group(1).strip().lower()
        self.assertEqual(val, "#fcfaf2", f"Expected --bg-paper to be #fcfaf2, got {val}")

    def test_t2_02_bg_card_color_token(self):
        """Boundary: Module card tint must match exact warm hex #f7f3e8."""
        m = re.search(r'--bg-card\s*:\s*([^;]+);', self.css)
        self.assertIsNotNone(m, "CSS must define custom property --bg-card.")
        val = m.group(1).strip().lower()
        self.assertEqual(val, "#f7f3e8", f"Expected --bg-card to be #f7f3e8, got {val}")

    def test_t2_03_border_color_token(self):
        """Boundary: Subtle border color must match exact warm border hex #e8dec8."""
        m = re.search(r'--(?:border-color|border-subtle)\s*:\s*([^;]+);', self.css)
        self.assertIsNotNone(m, "CSS must define custom property --border-color or --border-subtle.")
        val = m.group(1).strip().lower()
        self.assertEqual(val, "#e8dec8", f"Expected border token to be #e8dec8, got {val}")

    def test_t2_04_text_main_color_token(self):
        """Boundary: Main ink typography must match rich midnight ink hex #1e293b."""
        m = re.search(r'--(?:text-main|ink-primary)\s*:\s*([^;]+);', self.css)
        self.assertIsNotNone(m, "CSS must define custom property --text-main or --ink-primary.")
        val = m.group(1).strip().lower()
        self.assertEqual(val, "#1e293b", f"Expected typography ink token to be #1e293b, got {val}")

    def test_t2_05_viewport_meta_settings(self):
        """Boundary: Viewport meta tag must enforce width=device-width and initial-scale=1."""
        html = self.data.html_content
        m = re.search(r'<meta[^>]+name=[\'"]viewport[\'"][^>]+content=[\'"]([^\'"]+)[\'"]', html, re.IGNORECASE)
        self.assertIsNotNone(m, "index.html must have viewport meta with content attribute.")
        content = m.group(1).lower()
        self.assertIn("width=device-width", content, "Viewport must specify width=device-width.")
        self.assertTrue("initial-scale=1.0" in content or "initial-scale=1" in content,
                        "Viewport must specify initial-scale=1.0.")


class TestTier2Feature2KaTeXBoundaries(unittest.TestCase):
    """Feature 2 Boundaries: Delimiter integrity, balanced blocks, throwOnError setting."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()
        cls.html = cls.data.html_content

    def test_t2_06_display_math_delimiters_balanced(self):
        """Boundary: Display math delimiters ($$) must have an even count."""
        count = self.html.count("$$")
        self.assertGreater(count, 0, "Document must contain display math ($$).")
        self.assertEqual(count % 2, 0, f"Display math delimiters ($$) must be paired/even, found odd count: {count}")

    def test_t2_07_inline_math_delimiters_balanced(self):
        """Boundary: Inline math delimiters ($) in text must be balanced."""
        no_dd = re.sub(r'\$\$.*?\$\$', '', self.html, flags=re.DOTALL)
        no_scripts = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', no_dd, flags=re.DOTALL)
        count = no_scripts.count("$")
        self.assertGreater(count, 0, "Document must contain inline math ($).")
        self.assertEqual(count % 2, 0, f"Inline math delimiters ($) in body text must be paired/even, found odd count: {count}")

    def test_t2_08_no_empty_display_math(self):
        """Boundary: No empty display math blocks ($$$$)."""
        parts = self.html.split('$$')
        math_blocks = [parts[i] for i in range(1, len(parts), 2)]
        empty_blocks = [b for b in math_blocks if len(b.strip()) == 0]
        self.assertEqual(len(empty_blocks), 0, f"Found {len(empty_blocks)} empty display math blocks ($$$$).")

    def test_t2_09_no_empty_inline_math(self):
        """Boundary: No empty inline math expressions ($$)."""
        no_dd = re.sub(r'\$\$.*?\$\$', '', self.html, flags=re.DOTALL)
        no_scripts = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', no_dd, flags=re.DOTALL)
        empty_inlines = re.findall(r'\$\s+\$', no_scripts)
        self.assertEqual(len(empty_inlines), 0, f"Found {len(empty_inlines)} empty inline math expressions ($ $).")

    def test_t2_10_katex_throw_on_error_disabled(self):
        """Boundary: KaTeX config must set throwOnError: false to prevent render crashes."""
        all_code = self.data.html_content + "\n" + self.data.js_content
        has_config = bool(re.search(r'throwOnError\s*:\s*false', all_code, re.IGNORECASE))
        self.assertTrue(has_config, "KaTeX initialization must set throwOnError: false.")


class TestTier2Feature3PrintBoundaries(unittest.TestCase):
    """Feature 3 Boundaries: Print stylesheet rules, pagination, non-breaking containers."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()
        cls.css = cls.data.css_content + "\n" + cls.data.print_css_content

    def test_t2_11_print_counter_syntax(self):
        """Boundary: Dynamic running page footer/header must use counter(page) syntax."""
        has_counter = bool(re.search(r'counter\(\s*page\s*\)', self.css))
        self.assertTrue(has_counter, "@media print must utilize counter(page) for dynamic pagination.")

    def test_t2_12_table_page_break_inside_avoid(self):
        """Boundary: Formula tables must avoid page breaks inside."""
        has_table_avoid = bool(re.search(r'\.(?:formula-table-container|formula-table)[^{]*\{[^}]*(?:page-break-inside|break-inside)\s*:\s*avoid', self.css))
        self.assertTrue(has_table_avoid, "Formula tables must have page-break-inside: avoid in print rules.")

    def test_t2_13_diagram_page_break_inside_avoid(self):
        """Boundary: Diagram containers must avoid page breaks inside."""
        has_diagram_avoid = bool(re.search(r'\.diagram-container[^{]*\{[^}]*(?:page-break-inside|break-inside)\s*:\s*avoid', self.css))
        self.assertTrue(has_diagram_avoid, "Diagram containers must have page-break-inside: avoid in print rules.")

    def test_t2_14_print_font_size_units(self):
        """Boundary: Print stylesheet must define typography in print points (pt)."""
        has_pt = bool(re.search(r'@media\s+print[^{]*\{[^}]*font-size\s*:\s*[0-9]+(?:\.[0-9]+)?pt', self.css, re.DOTALL))
        self.assertTrue(has_pt, "Print typography must specify font-size in pt units for physical publication rendering.")

    def test_t2_15_print_color_fidelity(self):
        """Boundary: Print rules must set body background to white and text to black."""
        has_white_bg = bool(re.search(r'@media\s+print[^{]*\{[^}]*background(?:-color)?\s*:\s*(?:#ffffff|#fff|white)', self.css, re.DOTALL | re.IGNORECASE))
        has_black_text = bool(re.search(r'@media\s+print[^{]*\{[^}]*color\s*:\s*(?:#000000|#000|black)', self.css, re.DOTALL | re.IGNORECASE))
        self.assertTrue(has_white_bg, "Print rules must specify white background for physical paper output.")
        self.assertTrue(has_black_text, "Print rules must specify black ink for physical paper output.")


def _check_trap_continuity(test_case: unittest.TestCase, ch_key: str, ch_num: int):
    ch = HandbookData.get_instance().chapters.get(ch_key, {})
    test_case.assertTrue(bool(ch), f"Chapter {ch_num} ({ch_key}) must exist.")
    expected_traps = [f"{ch_num}.{j}" for j in range(1, 11)]
    actual_traps = ch.get("trap_numbers", [])
    test_case.assertEqual(actual_traps[:10], expected_traps,
                          f"Chapter {ch_num} trap numbers must be strictly sequential {expected_traps}, got {actual_traps[:10]}")


def _check_formula_completeness(test_case: unittest.TestCase, ch_key: str, ch_num: int):
    ch = HandbookData.get_instance().chapters.get(ch_key, {})
    test_case.assertTrue(bool(ch), f"Chapter {ch_num} ({ch_key}) must exist.")
    content = ch.get("content", "")
    table_m = re.search(r'<table[^>]*>(.*?)</table>', content, re.DOTALL)
    test_case.assertIsNotNone(table_m, f"Chapter {ch_num} must contain a formula table.")
    rows = re.findall(r'<tr>(.*?)</tr>', table_m.group(1), re.DOTALL)
    test_case.assertGreater(len(rows), 1, f"Chapter {ch_num} formula table must have at least one data row.")
    for r_idx, row in enumerate(rows[1:], 1):
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.DOTALL)
        clean_cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
        test_case.assertGreaterEqual(len(clean_cells), 4, f"Chapter {ch_num} row {r_idx} must have at least 4 columns.")
        test_case.assertGreater(len(clean_cells[2]), 5,
                                f"Chapter {ch_num} row {r_idx} 'Strict Domain of Validity' must not be empty.")
        test_case.assertGreater(len(clean_cells[3]), 5,
                                f"Chapter {ch_num} row {r_idx} 'Catastrophic Error Regime' must not be empty.")


def _check_challenge_depth(test_case: unittest.TestCase, ch_key: str, ch_num: int):
    ch = HandbookData.get_instance().chapters.get(ch_key, {})
    test_case.assertTrue(bool(ch), f"Chapter {ch_num} ({ch_key}) must exist.")
    content = ch.get("content", "")
    challenges = ch.get("challenge_boxes", [])
    test_case.assertGreaterEqual(len(challenges), 5, f"Chapter {ch_num} must have >= 5 challenge problems, found {len(challenges)}.")
    for c_idx, c_block in enumerate(challenges[:5], 1):
        m_sol = re.search(r'class=[\'"][^\'"]*challenge-solution[^\'"]*[\'"]>(.*?)</div>', c_block, re.DOTALL)
        if not m_sol:
            m_sol = re.search(r'<details[^>]*>(.*?)</details>', c_block, re.DOTALL)
        test_case.assertIsNotNone(m_sol, f"Chapter {ch_num} challenge {c_idx} must contain solution element.")
        clean_sol = re.sub(r'<[^>]+>', ' ', m_sol.group(1)).strip()
        words = clean_sol.split()
        test_case.assertGreaterEqual(len(words), 50,
                                     f"Chapter {ch_num} challenge {c_idx} solution must have >= 50 words, found {len(words)}.")


def _check_zero_placeholders(test_case: unittest.TestCase, ch_key: str, ch_num: int):
    data = HandbookData.get_instance()
    ch = data.chapters.get(ch_key, {})
    test_case.assertTrue(bool(ch), f"Chapter {ch_num} ({ch_key}) must exist.")
    content = ch.get("content", "")
    placeholders = data.get_placeholders(content)
    test_case.assertEqual(len(placeholders), 0,
                          f"Chapter {ch_num} must not contain placeholder text, found: {placeholders}")


def _check_word_count(test_case: unittest.TestCase, ch_key: str, ch_num: int):
    ch = HandbookData.get_instance().chapters.get(ch_key, {})
    test_case.assertTrue(bool(ch), f"Chapter {ch_num} ({ch_key}) must exist.")
    word_count = ch.get("word_count", 0)
    test_case.assertGreaterEqual(word_count, 3000,
                                 f"Chapter {ch_num} must contain >= 3,000 words for 50-page book equivalent, found {word_count}.")


class TestTier2Feature4Chapter1Boundaries(unittest.TestCase):
    """Feature 4 Boundaries: Chapter 1."""
    def test_t2_16_ch1_trap_numbering_continuity(self):
        _check_trap_continuity(self, "ch1", 1)

    def test_t2_17_ch1_formula_validity_completeness(self):
        _check_formula_completeness(self, "ch1", 1)

    def test_t2_18_ch1_challenge_solutions_depth(self):
        _check_challenge_depth(self, "ch1", 1)

    def test_t2_19_ch1_zero_placeholders(self):
        _check_zero_placeholders(self, "ch1", 1)

    def test_t2_20_ch1_word_count_boundary(self):
        _check_word_count(self, "ch1", 1)


class TestTier2Feature5Chapter2Boundaries(unittest.TestCase):
    """Feature 5 Boundaries: Chapter 2."""
    def test_t2_21_ch2_trap_numbering_continuity(self):
        _check_trap_continuity(self, "ch2", 2)

    def test_t2_22_ch2_formula_validity_completeness(self):
        _check_formula_completeness(self, "ch2", 2)

    def test_t2_23_ch2_challenge_solutions_depth(self):
        _check_challenge_depth(self, "ch2", 2)

    def test_t2_24_ch2_zero_placeholders(self):
        _check_zero_placeholders(self, "ch2", 2)

    def test_t2_25_ch2_word_count_boundary(self):
        _check_word_count(self, "ch2", 2)


class TestTier2Feature6Chapter3Boundaries(unittest.TestCase):
    """Feature 6 Boundaries: Chapter 3."""
    def test_t2_26_ch3_trap_numbering_continuity(self):
        _check_trap_continuity(self, "ch3", 3)

    def test_t2_27_ch3_formula_validity_completeness(self):
        _check_formula_completeness(self, "ch3", 3)

    def test_t2_28_ch3_challenge_solutions_depth(self):
        _check_challenge_depth(self, "ch3", 3)

    def test_t2_29_ch3_zero_placeholders(self):
        _check_zero_placeholders(self, "ch3", 3)

    def test_t2_30_ch3_word_count_boundary(self):
        _check_word_count(self, "ch3", 3)


class TestTier2Feature7Chapter4Boundaries(unittest.TestCase):
    """Feature 7 Boundaries: Chapter 4."""
    def test_t2_31_ch4_trap_numbering_continuity(self):
        _check_trap_continuity(self, "ch4", 4)

    def test_t2_32_ch4_formula_validity_completeness(self):
        _check_formula_completeness(self, "ch4", 4)

    def test_t2_33_ch4_challenge_solutions_depth(self):
        _check_challenge_depth(self, "ch4", 4)

    def test_t2_34_ch4_zero_placeholders(self):
        _check_zero_placeholders(self, "ch4", 4)

    def test_t2_35_ch4_word_count_boundary(self):
        _check_word_count(self, "ch4", 4)


class TestTier2Feature8Chapter5Boundaries(unittest.TestCase):
    """Feature 8 Boundaries: Chapter 5."""
    def test_t2_36_ch5_trap_numbering_continuity(self):
        _check_trap_continuity(self, "ch5", 5)

    def test_t2_37_ch5_formula_validity_completeness(self):
        _check_formula_completeness(self, "ch5", 5)

    def test_t2_38_ch5_challenge_solutions_depth(self):
        _check_challenge_depth(self, "ch5", 5)

    def test_t2_39_ch5_zero_placeholders(self):
        _check_zero_placeholders(self, "ch5", 5)

    def test_t2_40_ch5_word_count_boundary(self):
        _check_word_count(self, "ch5", 5)


class TestTier2Feature9Chapter6Boundaries(unittest.TestCase):
    """Feature 9 Boundaries: Chapter 6."""
    def test_t2_41_ch6_trap_numbering_continuity(self):
        _check_trap_continuity(self, "ch6", 6)

    def test_t2_42_ch6_formula_validity_completeness(self):
        _check_formula_completeness(self, "ch6", 6)

    def test_t2_43_ch6_challenge_solutions_depth(self):
        _check_challenge_depth(self, "ch6", 6)

    def test_t2_44_ch6_zero_placeholders(self):
        _check_zero_placeholders(self, "ch6", 6)

    def test_t2_45_ch6_word_count_boundary(self):
        _check_word_count(self, "ch6", 6)


class TestTier2GlobalVolumeBoundaries(unittest.TestCase):
    """Global Volume & Comprehensive Handbook Targets (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()

    def test_t2_46_total_word_count_50_page_equivalent(self):
        """Boundary: Total handbook text must reach >= 50-page equivalent (>25,000 words)."""
        count = self.data.get_document_word_count()
        self.assertGreater(count, 25000,
                           f"Handbook must contain > 25,000 words for a 50-page publication equivalent, found {count}.")

    def test_t2_47_document_wide_zero_placeholders(self):
        """Boundary: Document must have zero placeholder or stub patterns globally."""
        placeholders = self.data.get_placeholders()
        self.assertEqual(len(placeholders), 0,
                         f"Document contains unrendered placeholder text: {placeholders}")

    def test_t2_48_total_traps_exact_volume(self):
        """Boundary: Total number of cataloged NTA traps across all chapters must be exactly 60."""
        total_traps = sum(len(ch.get("trap_numbers", [])) for ch in self.data.chapters.values())
        self.assertEqual(total_traps, 60,
                         f"Expected exactly 60 forensic trap alerts across 6 chapters (10/ch), found {total_traps}.")

    def test_t2_49_total_pyqs_exact_volume(self):
        """Boundary: Total worked JEE Advanced PYQs across all chapters must be exactly 18."""
        total_pyqs = sum(ch.get("pyq_count", 0) for ch in self.data.chapters.values())
        self.assertEqual(total_pyqs, 18,
                         f"Expected exactly 18 worked JEE Advanced PYQs across 6 chapters (3/ch), found {total_pyqs}.")

    def test_t2_50_total_challenges_exact_volume(self):
        """Boundary: Total practice challenge problems across all chapters must be exactly 30."""
        total_challenges = sum(ch.get("challenge_count", 0) for ch in self.data.chapters.values())
        self.assertEqual(total_challenges, 30,
                         f"Expected exactly 30 practice challenge problems across 6 chapters (5/ch), found {total_challenges}.")


if __name__ == "__main__":
    unittest.main()
