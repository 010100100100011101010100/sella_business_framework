"""
test_tier1_features.py
Tier 1: Feature Inventory & Functional Completeness Test Suite.
Validates presence and primary behavior of all 9 core features across the 6 chapters:
1. Book Reader Shell & Aesthetics
2. KaTeX Typography & Math Rendering
3. Print CSS Engine (@media print)
4. Chapter 1: Vectors & Kinematics
5. Chapter 2: Newton's Laws & Friction Dynamics
6. Chapter 3: Work, Energy & Power
7. Chapter 4: Center of Mass & Collisions
8. Chapter 5: Rotational Mechanics & Toppling
9. Chapter 6: Gravitation & Oscillatory Motion / SHM

Total: 45 distinct test methods / assertions (5 per feature).
"""

import os
import re
import unittest
from pathlib import Path

from tests.handbook_parser import HandbookData


class TestTier1Feature1ReaderShell(unittest.TestCase):
    """Feature 1: Book Reader Shell & Aesthetics (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance(reload=True)

    def test_f1_01_standalone_html5_structure(self):
        """Verify HTML5 DOCTYPE and standard root structure."""
        html = self.data.html_content
        self.assertTrue(html.startswith("<!DOCTYPE html>") or "<!DOCTYPE html>" in html[:100],
                        "index.html must start with standard HTML5 DOCTYPE declaration.")
        self.assertIn("<html", html, "index.html must declare <html> element.")
        self.assertIn("<head>", html, "index.html must contain <head> element.")
        self.assertTrue(bool(re.search(r'<body\b', html, re.IGNORECASE)), "index.html must contain <body> element.")

    def test_f1_02_document_metadata_and_viewport(self):
        """Verify document title, description, and mobile viewport meta."""
        html = self.data.html_content
        title_m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        self.assertIsNotNone(title_m, "index.html must contain a <title> tag.")
        self.assertTrue("JEE" in title_m.group(1) and "Mechanics" in title_m.group(1),
                        f"Title '{title_m.group(1)}' must reference JEE and Mechanics.")
        viewport_m = re.search(r'<meta[^>]+name=[\'"]viewport[\'"][^>]*>', html, re.IGNORECASE)
        self.assertIsNotNone(viewport_m, "index.html must declare a responsive viewport meta tag.")

    def test_f1_03_book_wrapper_container(self):
        """Verify main flex/grid layout wrapper for book shell."""
        html = self.data.html_content
        has_wrapper = bool(re.search(r'class=[\'"][^\'"]*\b(?:book-wrapper|book-shell)\b', html)) or 'id="book-wrapper"' in html
        self.assertTrue(has_wrapper, "index.html must contain a top-level book wrapper container (.book-wrapper or .book-shell).")

    def test_f1_04_navigation_sidebar_present(self):
        """Verify presence of sidebar navigation element with links."""
        html = self.data.html_content
        has_sidebar = ('class="book-sidebar"' in html or 'class="sidebar-nav"' in html or
                       'id="sidebar"' in html or '<aside' in html)
        self.assertTrue(has_sidebar, "index.html must contain a navigation sidebar.")
        sidebar_links = self.data.get_sidebar_hrefs()
        self.assertGreaterEqual(len(sidebar_links), 6,
                                f"Sidebar must contain at least 6 navigation links, found {len(sidebar_links)}.")

    def test_f1_05_reading_progress_indicator(self):
        """Verify reading progress bar element is present in DOM."""
        html = self.data.html_content
        has_progress = 'id="progress-bar"' in html or 'id="reading-progress-bar"' in html
        self.assertTrue(has_progress, "index.html must contain a reading progress bar (#progress-bar or #reading-progress-bar).")


class TestTier1Feature2KaTeXMath(unittest.TestCase):
    """Feature 2: KaTeX Typography & Math Rendering (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()

    def test_f2_01_katex_stylesheet_link(self):
        """Verify KaTeX CSS stylesheet is linked."""
        html = self.data.html_content
        has_katex_css = bool(re.search(r'<link[^>]+href=[\'"][^\'"]*katex(?:\.min)?\.css[\'"]', html, re.IGNORECASE))
        self.assertTrue(has_katex_css, "index.html must link KaTeX CSS (katex.min.css).")

    def test_f2_02_katex_core_js_script(self):
        """Verify KaTeX core JS library script tag is present."""
        html = self.data.html_content
        has_katex_js = bool(re.search(r'<script[^>]+src=[\'"][^\'"]*katex(?:\.min)?\.js[\'"]', html, re.IGNORECASE))
        self.assertTrue(has_katex_js, "index.html must include KaTeX core script (katex.min.js).")

    def test_f2_03_katex_autorender_extension(self):
        """Verify KaTeX auto-render extension script is present."""
        html = self.data.html_content
        has_autorender = bool(re.search(r'auto-render(?:\.min)?\.js', html, re.IGNORECASE))
        self.assertTrue(has_autorender, "index.html must include KaTeX auto-render extension script.")

    def test_f2_04_katex_delimiters_configured(self):
        """Verify inline ($) and display ($$) math delimiters are configured."""
        all_code = self.data.html_content + "\n" + self.data.js_content
        has_delimiters = "renderMathInElement" in all_code and ("delimiters" in all_code or "$$" in all_code)
        self.assertTrue(has_delimiters, "KaTeX auto-render delimiter configuration must be defined in HTML or JS.")

    def test_f2_05_latex_math_notations_present(self):
        """Verify document contains extensive LaTeX mathematical typesetting."""
        html = self.data.html_content
        display_math = re.findall(r'\$\$.*?\$\$', html, re.DOTALL)
        self.assertGreaterEqual(len(display_math), 50,
                                f"Document must contain substantial display math ($$), found {len(display_math)}.")


class TestTier1Feature3PrintEngine(unittest.TestCase):
    """Feature 3: Print CSS Engine (@media print) (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()

    def test_f3_01_print_media_block_exists(self):
        """Verify @media print block exists in stylesheet."""
        css = self.data.css_content + "\n" + self.data.print_css_content
        self.assertIn("@media print", css, "Stylesheets must define an @media print block.")

    def test_f3_02_print_page_dimensions_defined(self):
        """Verify @page rule defines A4 paper size and margins."""
        css = self.data.css_content + "\n" + self.data.print_css_content
        has_page = bool(re.search(r'@page\s*\{[^}]*size\s*:\s*A4', css, re.IGNORECASE))
        self.assertTrue(has_page, "@media print must specify '@page { size: A4; }'.")

    def test_f3_03_chapter_page_break_rules(self):
        """Verify chapters enforce forced page break before."""
        css = self.data.css_content + "\n" + self.data.print_css_content
        has_break = bool(re.search(r'(?:page-break-before|break-before)\s*:\s*(?:always|page)', css, re.IGNORECASE))
        self.assertTrue(has_break, "@media print must define page-break-before: always or break-before: page for chapters.")

    def test_f3_04_card_break_inside_avoidance(self):
        """Verify cards, formulas, and diagrams avoid page breaks inside."""
        css = self.data.css_content + "\n" + self.data.print_css_content
        has_avoid = bool(re.search(r'(?:page-break-inside|break-inside)\s*:\s*avoid', css, re.IGNORECASE))
        self.assertTrue(has_avoid, "@media print must specify page-break-inside: avoid for cards and tables.")

    def test_f3_05_navigation_suppressed_in_print(self):
        """Verify sidebar navigation and progress bar are suppressed in print."""
        css = self.data.css_content + "\n" + self.data.print_css_content
        has_nav_hide = bool(re.search(r'(?:sidebar|progress-bar)[^}]*display\s*:\s*none', css, re.IGNORECASE))
        self.assertTrue(has_nav_hide, "@media print must suppress interactive UI (.book-sidebar, #progress-bar) with display: none.")


class TestTier1Feature4Chapter1Kinematics(unittest.TestCase):
    """Feature 4: Chapter 1 - Kinematics (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()
        cls.ch = cls.data.chapters.get("ch1", {})

    def test_f4_01_container_and_title(self):
        """Verify Chapter 1 container and title exist."""
        self.assertTrue(bool(self.ch), "Chapter 1 section container must exist.")
        self.assertIn("Kinematics", self.ch.get("title", ""), "Chapter 1 title must reference Kinematics.")

    def test_f4_02_formula_table_present(self):
        """Verify Chapter 1 contains master formula summary table."""
        self.assertGreaterEqual(self.ch.get("table_count", 0), 1, "Chapter 1 must contain a master formula table.")

    def test_f4_03_traps_count(self):
        """Verify Chapter 1 contains >= 10 NTA trap alerts."""
        traps = self.ch.get("trap_numbers", [])
        self.assertGreaterEqual(len(traps), 10, f"Chapter 1 must have >= 10 NTA trap alerts, found {len(traps)}.")

    def test_f4_04_pyqs_count(self):
        """Verify Chapter 1 contains >= 3 worked JEE Advanced PYQs."""
        pyqs = self.ch.get("pyq_count", 0)
        self.assertGreaterEqual(pyqs, 3, f"Chapter 1 must have >= 3 worked PYQs, found {pyqs}.")

    def test_f4_05_challenges_and_svg_present(self):
        """Verify Chapter 1 contains >= 5 challenge problems and inline SVG diagram."""
        challenges = self.ch.get("challenge_count", 0)
        svgs = self.ch.get("svg_count", 0)
        self.assertGreaterEqual(challenges, 5, f"Chapter 1 must have >= 5 challenge problems, found {challenges}.")
        self.assertGreaterEqual(svgs, 1, f"Chapter 1 must have >= 1 inline SVG diagram, found {svgs}.")


class TestTier1Feature5Chapter2NewtonLaws(unittest.TestCase):
    """Feature 5: Chapter 2 - Newton's Laws & Friction (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()
        cls.ch = cls.data.chapters.get("ch2", {})

    def test_f5_01_container_and_title(self):
        """Verify Chapter 2 container and title exist."""
        self.assertTrue(bool(self.ch), "Chapter 2 section container must exist.")
        self.assertTrue("Newton" in self.ch.get("title", "") or "Friction" in self.ch.get("title", ""),
                        "Chapter 2 title must reference Newton's Laws or Friction.")

    def test_f5_02_formula_table_present(self):
        """Verify Chapter 2 contains master formula summary table."""
        self.assertGreaterEqual(self.ch.get("table_count", 0), 1, "Chapter 2 must contain a master formula table.")

    def test_f5_03_traps_count(self):
        """Verify Chapter 2 contains >= 10 NTA trap alerts."""
        traps = self.ch.get("trap_numbers", [])
        self.assertGreaterEqual(len(traps), 10, f"Chapter 2 must have >= 10 NTA trap alerts, found {len(traps)}.")

    def test_f5_04_pyqs_count(self):
        """Verify Chapter 2 contains >= 3 worked JEE Advanced PYQs."""
        pyqs = self.ch.get("pyq_count", 0)
        self.assertGreaterEqual(pyqs, 3, f"Chapter 2 must have >= 3 worked PYQs, found {pyqs}.")

    def test_f5_05_challenges_and_svg_present(self):
        """Verify Chapter 2 contains >= 5 challenge problems and inline SVG diagram."""
        challenges = self.ch.get("challenge_count", 0)
        svgs = self.ch.get("svg_count", 0)
        self.assertGreaterEqual(challenges, 5, f"Chapter 2 must have >= 5 challenge problems, found {challenges}.")
        self.assertGreaterEqual(svgs, 1, f"Chapter 2 must have >= 1 inline SVG diagram, found {svgs}.")


class TestTier1Feature6Chapter3WorkEnergy(unittest.TestCase):
    """Feature 6: Chapter 3 - Work, Energy & Power (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()
        cls.ch = cls.data.chapters.get("ch3", {})

    def test_f6_01_container_and_title(self):
        """Verify Chapter 3 container and title exist."""
        self.assertTrue(bool(self.ch), "Chapter 3 section container must exist.")
        self.assertIn("Work", self.ch.get("title", ""), "Chapter 3 title must reference Work & Energy.")

    def test_f6_02_formula_table_present(self):
        """Verify Chapter 3 contains master formula summary table."""
        self.assertGreaterEqual(self.ch.get("table_count", 0), 1, "Chapter 3 must contain a master formula table.")

    def test_f6_03_traps_count(self):
        """Verify Chapter 3 contains >= 10 NTA trap alerts."""
        traps = self.ch.get("trap_numbers", [])
        self.assertGreaterEqual(len(traps), 10, f"Chapter 3 must have >= 10 NTA trap alerts, found {len(traps)}.")

    def test_f6_04_pyqs_count(self):
        """Verify Chapter 3 contains >= 3 worked JEE Advanced PYQs."""
        pyqs = self.ch.get("pyq_count", 0)
        self.assertGreaterEqual(pyqs, 3, f"Chapter 3 must have >= 3 worked PYQs, found {pyqs}.")

    def test_f6_05_challenges_and_svg_present(self):
        """Verify Chapter 3 contains >= 5 challenge problems and inline SVG diagram."""
        challenges = self.ch.get("challenge_count", 0)
        svgs = self.ch.get("svg_count", 0)
        self.assertGreaterEqual(challenges, 5, f"Chapter 3 must have >= 5 challenge problems, found {challenges}.")
        self.assertGreaterEqual(svgs, 1, f"Chapter 3 must have >= 1 inline SVG diagram, found {svgs}.")


class TestTier1Feature7Chapter4CenterOfMass(unittest.TestCase):
    """Feature 7: Chapter 4 - Center of Mass & Collisions (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()
        cls.ch = cls.data.chapters.get("ch4", {})

    def test_f7_01_container_and_title(self):
        """Verify Chapter 4 container and title exist."""
        self.assertTrue(bool(self.ch), "Chapter 4 section container must exist.")
        self.assertTrue("Center of Mass" in self.ch.get("title", "") or "Collisions" in self.ch.get("title", ""),
                        "Chapter 4 title must reference Center of Mass or Collisions.")

    def test_f7_02_formula_table_present(self):
        """Verify Chapter 4 contains master formula summary table."""
        self.assertGreaterEqual(self.ch.get("table_count", 0), 1, "Chapter 4 must contain a master formula table.")

    def test_f7_03_traps_count(self):
        """Verify Chapter 4 contains >= 10 NTA trap alerts."""
        traps = self.ch.get("trap_numbers", [])
        self.assertGreaterEqual(len(traps), 10, f"Chapter 4 must have >= 10 NTA trap alerts, found {len(traps)}.")

    def test_f7_04_pyqs_count(self):
        """Verify Chapter 4 contains >= 3 worked JEE Advanced PYQs."""
        pyqs = self.ch.get("pyq_count", 0)
        self.assertGreaterEqual(pyqs, 3, f"Chapter 4 must have >= 3 worked PYQs, found {pyqs}.")

    def test_f7_05_challenges_and_svg_present(self):
        """Verify Chapter 4 contains >= 5 challenge problems and inline SVG diagram."""
        challenges = self.ch.get("challenge_count", 0)
        svgs = self.ch.get("svg_count", 0)
        self.assertGreaterEqual(challenges, 5, f"Chapter 4 must have >= 5 challenge problems, found {challenges}.")
        self.assertGreaterEqual(svgs, 1, f"Chapter 4 must have >= 1 inline SVG diagram, found {svgs}.")


class TestTier1Feature8Chapter5Rotation(unittest.TestCase):
    """Feature 8: Chapter 5 - Rotational Mechanics & Toppling (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()
        cls.ch = cls.data.chapters.get("ch5", {})

    def test_f8_01_container_and_title(self):
        """Verify Chapter 5 container and title exist."""
        self.assertTrue(bool(self.ch), "Chapter 5 section container must exist.")
        self.assertIn("Rotational", self.ch.get("title", ""), "Chapter 5 title must reference Rotational Mechanics.")

    def test_f8_02_formula_table_present(self):
        """Verify Chapter 5 contains master formula summary table."""
        self.assertGreaterEqual(self.ch.get("table_count", 0), 1, "Chapter 5 must contain a master formula table.")

    def test_f8_03_traps_count(self):
        """Verify Chapter 5 contains >= 10 NTA trap alerts."""
        traps = self.ch.get("trap_numbers", [])
        self.assertGreaterEqual(len(traps), 10, f"Chapter 5 must have >= 10 NTA trap alerts, found {len(traps)}.")

    def test_f8_04_pyqs_count(self):
        """Verify Chapter 5 contains >= 3 worked JEE Advanced PYQs."""
        pyqs = self.ch.get("pyq_count", 0)
        self.assertGreaterEqual(pyqs, 3, f"Chapter 5 must have >= 3 worked PYQs, found {pyqs}.")

    def test_f8_05_challenges_and_svg_present(self):
        """Verify Chapter 5 contains >= 5 challenge problems and inline SVG diagram."""
        challenges = self.ch.get("challenge_count", 0)
        svgs = self.ch.get("svg_count", 0)
        self.assertGreaterEqual(challenges, 5, f"Chapter 5 must have >= 5 challenge problems, found {challenges}.")
        self.assertGreaterEqual(svgs, 1, f"Chapter 5 must have >= 1 inline SVG diagram, found {svgs}.")


class TestTier1Feature9Chapter6GravitationSHM(unittest.TestCase):
    """Feature 9: Chapter 6 - Gravitation & SHM (5 assertions)."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance()
        cls.ch = cls.data.chapters.get("ch6", {})

    def test_f9_01_container_and_title(self):
        """Verify Chapter 6 container and title exist."""
        self.assertTrue(bool(self.ch), "Chapter 6 section container must exist.")
        self.assertTrue("Gravitation" in self.ch.get("title", "") or "SHM" in self.ch.get("title", ""),
                        "Chapter 6 title must reference Gravitation or SHM.")

    def test_f9_02_formula_table_present(self):
        """Verify Chapter 6 contains master formula summary table."""
        self.assertGreaterEqual(self.ch.get("table_count", 0), 1, "Chapter 6 must contain a master formula table.")

    def test_f9_03_traps_count(self):
        """Verify Chapter 6 contains >= 10 NTA trap alerts."""
        traps = self.ch.get("trap_numbers", [])
        self.assertGreaterEqual(len(traps), 10, f"Chapter 6 must have >= 10 NTA trap alerts, found {len(traps)}.")

    def test_f9_04_pyqs_count(self):
        """Verify Chapter 6 contains >= 3 worked JEE Advanced PYQs."""
        pyqs = self.ch.get("pyq_count", 0)
        self.assertGreaterEqual(pyqs, 3, f"Chapter 6 must have >= 3 worked PYQs, found {pyqs}.")

    def test_f9_05_challenges_and_svg_present(self):
        """Verify Chapter 6 contains >= 5 challenge problems and inline SVG diagram."""
        challenges = self.ch.get("challenge_count", 0)
        svgs = self.ch.get("svg_count", 0)
        self.assertGreaterEqual(challenges, 5, f"Chapter 6 must have >= 5 challenge problems, found {challenges}.")
        self.assertGreaterEqual(svgs, 1, f"Chapter 6 must have >= 1 inline SVG diagram, found {svgs}.")


if __name__ == "__main__":
    unittest.main()
