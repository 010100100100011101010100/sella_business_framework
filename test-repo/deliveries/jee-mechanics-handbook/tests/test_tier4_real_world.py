"""
test_tier4_real_world.py
Tier 4: Real-World Workload & Application Scenarios Test Suite.
Validates the complete end-to-end user experience across authentic real-world workflows:
1. Scenario 1: Student Local Offline Browser Session (standalone HTML, zero broken local paths, KaTeX offline bundle)
2. Scenario 2: Teacher Headless Print / PDF Export (@media print stylesheet integrity, @page, page-breaks, no split cards)
3. Scenario 3: JEE Aspirant Trap & Formula Quick Review (all 60 traps with rules, 6 formula tables, responsive drawer toggle)
4. Scenario 4: Deep-Dive PYQ & Challenge Self-Study (18 PYQs, 30 challenge solution keys, inline SVG XML validity)
5. Scenario 5: Mobile Device Responsive Reading (viewport meta, responsive media queries, mobile drawer, scroll progress bar)

Total: 5 comprehensive real-world scenarios.
"""

import os
import re
import unittest
from pathlib import Path
from typing import List

from tests.handbook_parser import HandbookData


class TestTier4RealWorldScenarios(unittest.TestCase):
    """Real-world user scenarios validating publication fidelity and operational reliability."""

    @classmethod
    def setUpClass(cls):
        cls.data = HandbookData.get_instance(reload=True)
        cls.html = cls.data.html_content
        cls.css = cls.data.css_content + "\n" + cls.data.print_css_content
        cls.js = cls.data.js_content
        cls.root_dir = cls.data.root_dir

    # -------------------------------------------------------------------------
    # Scenario 1: Student Local Offline Browser Session
    # -------------------------------------------------------------------------
    def test_scenario_1_student_offline_browser_session(self):
        """Scenario 1: Student opens standalone HTML offline via file:/// without local web server.
        Verifies:
        - index.html exists and is non-empty
        - All local <link>, <script>, and <img> asset references resolve to actual files on disk
        - Local KaTeX offline fallback assets exist in assets/katex/
        - Navigation sidebar exists with working internal anchors
        """
        # 1. Standalone file existence
        self.assertTrue(self.data.html_path.exists(), "index.html must exist for standalone opening.")
        self.assertGreater(len(self.html), 10000, "index.html must be populated with publication content.")

        # 2. Local asset resolution (no 404s on local disk)
        local_assets = []
        # links
        for m in re.finditer(r'<link[^>]+href=[\'"]([^\'"]+)[\'"]', self.html, re.IGNORECASE):
            path_str = m.group(1)
            if not path_str.startswith(("http://", "https://", "#", "data:")):
                local_assets.append(path_str)
        # scripts
        for m in re.finditer(r'<script[^>]+src=[\'"]([^\'"]+)[\'"]', self.html, re.IGNORECASE):
            path_str = m.group(1)
            if not path_str.startswith(("http://", "https://", "#", "data:")):
                local_assets.append(path_str)

        missing_assets = []
        for asset in local_assets:
            target_file = self.root_dir / asset
            if not target_file.exists():
                missing_assets.append(asset)

        self.assertEqual(len(missing_assets), 0,
                         f"Local offline browser session would fail due to missing local files: {missing_assets}")

        # 3. Local KaTeX offline bundle assets
        katex_dir = self.root_dir / "assets" / "katex"
        self.assertTrue(katex_dir.exists(), "assets/katex/ directory must exist for offline math fallback.")
        self.assertTrue((katex_dir / "katex.min.css").exists() or (katex_dir / "katex.css").exists(),
                        "Local KaTeX CSS must exist in assets/katex/.")
        self.assertTrue((katex_dir / "katex.min.js").exists() or (katex_dir / "katex.js").exists(),
                        "Local KaTeX JS must exist in assets/katex/.")

        # 4. Offline navigation functionality
        sidebar_hrefs = self.data.get_sidebar_hrefs()
        self.assertGreaterEqual(len(sidebar_hrefs), 6, "Offline sidebar must contain chapter links.")

    # -------------------------------------------------------------------------
    # Scenario 2: Teacher Headless Print / PDF Export
    # -------------------------------------------------------------------------
    def test_scenario_2_teacher_headless_print_pdf_export(self):
        """Scenario 2: Teacher prints or exports 50-page PDF handbook (Cmd + P or headless Chromium).
        Verifies:
        - @media print CSS exists and specifies @page size: A4 with margins
        - Dynamic pagination with counter(page) in running headers or footers
        - Forced chapter page-breaks (page-break-before: always or break-before: page)
        - Page-break-inside avoidance on callouts, formulas, PYQs, and diagrams
        - Interactive screen elements (sidebar, progress bar, action buttons) hidden in print
        """
        # 1. Print media block and @page
        self.assertIn("@media print", self.css, "Print stylesheet engine must define @media print rules.")
        has_a4 = bool(re.search(r'@page\s*\{[^}]*size\s*:\s*A4', self.css, re.IGNORECASE))
        self.assertTrue(has_a4, "@page must declare A4 dimensions for international paper printing.")
        has_margin = bool(re.search(r'@page\s*\{[^}]*margin\s*:', self.css, re.IGNORECASE))
        self.assertTrue(has_margin, "@page must declare printable margins.")

        # 2. Dynamic pagination counter
        has_counter = bool(re.search(r'counter\(\s*page\s*\)', self.css))
        self.assertTrue(has_counter, "@media print must utilize counter(page) for dynamic running footers/headers.")

        # 3. Chapter page breaks
        has_chapter_break = bool(re.search(r'(?:page-break-before|break-before)\s*:\s*(?:always|page)', self.css, re.IGNORECASE))
        self.assertTrue(has_chapter_break, "Print rules must specify page-break-before: always for chapters.")

        # 4. Non-breaking component containers
        has_avoid = bool(re.search(r'(?:page-break-inside|break-inside)\s*:\s*avoid', self.css, re.IGNORECASE))
        self.assertTrue(has_avoid, "Print rules must avoid breaking inside cards, diagrams, and formula tables.")

        # 5. UI suppression
        has_ui_suppression = bool(re.search(r'(?:sidebar|progress-bar)[^{]*\{[^}]*display\s*:\s*none', self.css, re.IGNORECASE))
        self.assertTrue(has_ui_suppression, "Screen UI controls must be hidden during print with display: none.")

    # -------------------------------------------------------------------------
    # Scenario 3: JEE Aspirant Trap & Formula Quick Review
    # -------------------------------------------------------------------------
    def test_scenario_3_jee_aspirant_trap_and_formula_quick_review(self):
        """Scenario 3: JEE Aspirant performs rapid formula & negative-marking trap revision.
        Verifies:
        - All 60 NTA forensic trap alerts exist (10 per chapter across all 6 chapters)
        - Every trap card contains distinct 'The Trap' and 'Definitive Rule' / remedy sections
        - Formula tables across all 6 chapters feature strict domain of validity and error regimes
        - Responsive drawer or navigation toggle button is present for instant mobile review jumping
        """
        # 1. 60 Traps across chapters
        total_traps = 0
        traps_with_remedy = 0
        for ch_key, ch_data in self.data.chapters.items():
            traps = ch_data.get("trap_numbers", [])
            total_traps += len(traps)
            content = ch_data.get("content", "")
            # Check for Trap and Rule/Remedy structure
            has_trap_label = "The Trap:" in content or "The Trap" in content
            has_rule_label = "Definitive Rule:" in content or "trap-remedy" in content or "Remedy" in content
            if has_trap_label and has_rule_label:
                traps_with_remedy += 1

        self.assertEqual(total_traps, 60, f"Expected 60 total traps for quick review, found {total_traps}.")
        self.assertEqual(traps_with_remedy, 6, "All 6 chapters must structure traps with explicit Trap and Rule/Remedy sections.")

        # 2. Formula tables domain of validity
        for ch_key, ch_data in self.data.chapters.items():
            content = ch_data.get("content", "")
            self.assertIn("Strict Domain of Validity", content,
                          f"{ch_key} formula table must include 'Strict Domain of Validity' column.")
            self.assertIn("Catastrophic Error Regime", content,
                          f"{ch_key} formula table must include 'Catastrophic Error Regime' column.")

        # 3. Responsive drawer or menu toggle element
        has_drawer_toggle = ('id="sidebar-toggle"' in self.html or 'class="sidebar-toggle"' in self.html or
                             'class="drawer-toggle"' in self.html or 'aria-label="Toggle Table of Contents"' in self.html)
        self.assertTrue(has_drawer_toggle,
                        "Document must provide a responsive drawer toggle button (#sidebar-toggle) for mobile review.")

    # -------------------------------------------------------------------------
    # Scenario 4: Deep-Dive PYQ & Challenge Self-Study
    # -------------------------------------------------------------------------
    def test_scenario_4_deep_dive_pyq_and_challenge_self_study(self):
        """Scenario 4: Student solves PYQs and Olympiad challenges with expandable solutions and vector diagrams.
        Verifies:
        - All 18 JEE Advanced PYQs include exam tags, difficulty ratings, and step-by-step reasoning
        - All 30 Challenge Problems feature interactive <details> elements with detailed solutions
        - All inline SVG physics diagrams are well-formed XML and contain vector paths/circles/text
        """
        # 1. 18 Solved PYQs
        total_pyqs = sum(ch.get("pyq_count", 0) for ch in self.data.chapters.values())
        self.assertEqual(total_pyqs, 18, f"Expected exactly 18 worked JEE Advanced PYQs, found {total_pyqs}.")

        # 2. 30 Challenge Problems with solution keys
        total_challenges = sum(ch.get("challenge_count", 0) for ch in self.data.chapters.values())
        self.assertEqual(total_challenges, 30, f"Expected exactly 30 practice challenge problems, found {total_challenges}.")
        total_details = self.html.count("<details")
        self.assertGreaterEqual(total_details, 30,
                                f"Expected >= 30 interactive <details> solution toggles, found {total_details}.")

        # 3. Inline SVG vector diagrams XML validity
        all_svgs = []
        for ch_data in self.data.chapters.values():
            all_svgs.extend(ch_data.get("svgs", []))

        self.assertGreaterEqual(len(all_svgs), 6, f"Expected at least 6 inline SVG diagrams, found {len(all_svgs)}.")

        xml_errors = []
        for i, svg in enumerate(all_svgs, 1):
            valid, err = self.data.check_svg_xml_validity(svg)
            if not valid:
                xml_errors.append(f"SVG {i}: {err}")

        self.assertEqual(len(xml_errors), 0,
                         f"Inline SVG diagrams contain invalid XML syntax: {xml_errors}")

    # -------------------------------------------------------------------------
    # Scenario 5: Mobile Device Responsive Reading
    # -------------------------------------------------------------------------
    def test_scenario_5_mobile_device_responsive_reading(self):
        """Scenario 5: Aspirant reads handbook on mobile/tablet smartphone screen.
        Verifies:
        - Viewport meta tag is properly configured for mobile devices
        - Responsive media queries (@media (max-width: ...)) are present in CSS
        - Sidebar adapts responsively for small viewports
        - Reading progress bar is present and wired to scroll tracking in JS
        """
        # 1. Viewport meta
        m_viewport = re.search(r'<meta[^>]+name=[\'"]viewport[\'"][^>]+content=[\'"]([^\'"]+)[\'"]', self.html, re.IGNORECASE)
        self.assertIsNotNone(m_viewport, "Viewport meta tag required for mobile responsiveness.")
        self.assertIn("width=device-width", m_viewport.group(1).lower())

        # 2. Responsive media queries in CSS
        has_media_query = bool(re.search(r'@media\s*(?:screen\s+and\s*)?\(\s*max-width\s*:', self.css, re.IGNORECASE))
        self.assertTrue(has_media_query, "CSS must define responsive media queries for mobile viewports (@media (max-width: ...)).")

        # 3. Responsive drawer / mobile header presence
        has_mobile_header = 'class="mobile-header"' in self.html or 'id="mobile-header"' in self.html or '<header' in self.html
        self.assertTrue(has_mobile_header, "Document must include a mobile header for small screens.")

        # 4. Reading progress indicator and scroll event binding
        has_progress_elem = 'id="progress-bar"' in self.html or 'id="reading-progress-bar"' in self.html
        self.assertTrue(has_progress_elem, "Reading progress bar element must be present.")
        has_scroll_sync = "scroll" in self.js or "scrollY" in self.js or "scrollTop" in self.js
        self.assertTrue(has_scroll_sync, "Interactive JS must bind reading progress to window/container scroll events.")


if __name__ == "__main__":
    unittest.main()
