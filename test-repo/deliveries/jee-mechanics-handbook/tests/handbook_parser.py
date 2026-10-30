"""
handbook_parser.py
Parser and DOM extractor for the JEE Mechanics & Rotational Dynamics Master Handbook.
Provides shared fixtures and data structures for Tiers 1-4 test suites without external dependencies.
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

DELIVERY_ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML_PATH = DELIVERY_ROOT / "index.html"
STYLES_CSS_PATH = DELIVERY_ROOT / "styles.css"
CSS_DIR = DELIVERY_ROOT / "css"
JS_DIR = DELIVERY_ROOT / "js"
ASSETS_DIR = DELIVERY_ROOT / "assets"


class HandbookData:
    """Singleton-style cached parser for handbook deliverables."""
    _instance = None

    def __init__(self):
        self.root_dir = DELIVERY_ROOT
        self.html_path = INDEX_HTML_PATH
        self.css_path = STYLES_CSS_PATH

        self.html_content = ""
        self.css_content = ""
        self.print_css_content = ""
        self.js_content = ""

        self._load_files()
        self._parse_chapters()

    @classmethod
    def get_instance(cls, reload: bool = False) -> "HandbookData":
        if cls._instance is None or reload:
            cls._instance = HandbookData()
        return cls._instance

    def _load_files(self):
        if self.html_path.exists():
            with open(self.html_path, "r", encoding="utf-8") as f:
                self.html_content = f.read()

        if self.css_path.exists():
            with open(self.css_path, "r", encoding="utf-8") as f:
                self.css_content = f.read()

        # Check alternative css/ directory locations
        alt_style = CSS_DIR / "style.css"
        if alt_style.exists():
            with open(alt_style, "r", encoding="utf-8") as f:
                self.css_content += "\n" + f.read()

        alt_print = CSS_DIR / "print.css"
        if alt_print.exists():
            with open(alt_print, "r", encoding="utf-8") as f:
                self.print_css_content = f.read()
        else:
            # Check @media print within styles.css
            m = re.search(r"@media\s+print\s*\{(.*)\}\s*$", self.css_content, re.DOTALL)
            if m:
                self.print_css_content = m.group(1)

        # Load JS files
        if JS_DIR.exists():
            for js_file in sorted(JS_DIR.glob("*.js")):
                try:
                    with open(js_file, "r", encoding="utf-8") as f:
                        self.js_content += f"\n/* {js_file.name} */\n" + f.read()
                except Exception:
                    pass

    def _parse_chapters(self):
        """Extract structured data for chapters 1 through 6."""
        self.chapters: Dict[str, Dict[str, Any]] = {}

        # Look for section or article tags with id="chN" or id="chapter-N"
        ch_matches = re.findall(
            r'<(?:section|article)[^>]*\bid=[\'"](ch[1-6]|chapter-[1-6])[\'"][^>]*>(.*?)(?=<(?:section|article)[^>]*\bid=[\'"](?:ch[1-6]|chapter-[1-6]|trap-index|pyq-index|practice-index)[\'"]|</main>|\Z)',
            self.html_content,
            re.DOTALL | re.IGNORECASE
        )

        for raw_id, content in ch_matches:
            ch_num = re.search(r'[1-6]', raw_id).group(0)
            key = f"ch{ch_num}"

            # Chapter title
            title_m = re.search(r'<(?:h1|h2)[^>]*class=[\'"][^\'"]*chapter-title[^\'"]*[\'"][^>]*>(.*?)</(?:h1|h2)>', content, re.DOTALL)
            title = title_m.group(1).strip() if title_m else ""

            # Traps (numbered sequence)
            trap_numbers = re.findall(r'Trap\s+Alert\s+([0-9]+\.[0-9]+)', content, re.IGNORECASE)
            trap_boxes = re.split(r'class=[\'"][^\'"]*\btrap-card\b[^\'"]*[\'"]', content)[1:]
            if not trap_boxes:
                trap_boxes = re.split(r'class=[\'"][^\'"]*\bcallout-trap\b[^\'"]*[\'"]', content)[1:]

            # PYQs
            pyq_boxes = re.split(r'class=[\'"][^\'"]*\bpyq-box\b[^\'"]*[\'"]', content)[1:]
            if not pyq_boxes:
                pyq_boxes = re.split(r'class=[\'"][^\'"]*\bcard-pyq\b[^\'"]*[\'"]', content)[1:]

            # Challenges
            challenge_boxes = re.split(r'class=[\'"][^\'"]*\bchallenge-box\b[^\'"]*[\'"]', content)[1:]
            if not challenge_boxes:
                challenge_boxes = re.split(r'class=[\'"][^\'"]*\bcard-challenge\b[^\'"]*[\'"]', content)[1:]

            # SVGs
            svgs = re.findall(r'(<svg[^>]*>.*?</svg>)', content, re.DOTALL | re.IGNORECASE)

            # Formula tables
            tables = re.findall(r'<table[^>]*class=[\'"][^\'"]*formula-table[^\'"]*[\'"][^>]*>(.*?)</table>', content, re.DOTALL | re.IGNORECASE)
            if not tables:
                tables = re.findall(r'<table[^>]*>(.*?)</table>', content, re.DOTALL | re.IGNORECASE)

            # Clean word count for chapter
            clean_text = re.sub(r'<[^>]+>', ' ', content)
            words = clean_text.split()

            self.chapters[key] = {
                "id": raw_id,
                "num": int(ch_num),
                "title": title,
                "content": content,
                "trap_numbers": trap_numbers,
                "trap_count": len(trap_numbers),
                "trap_boxes": trap_boxes,
                "pyq_count": len(pyq_boxes),
                "pyq_boxes": pyq_boxes,
                "challenge_count": len(challenge_boxes),
                "challenge_boxes": challenge_boxes,
                "svgs": svgs,
                "svg_count": len(svgs),
                "tables": tables,
                "table_count": len(tables),
                "word_count": len(words),
            }

    def get_document_word_count(self) -> int:
        """Returns total word count of cleaned text across index.html."""
        clean = re.sub(r'<[^>]+>', ' ', self.html_content)
        return len(clean.split())

    def get_all_ids(self) -> List[str]:
        """Returns all DOM element IDs present in index.html."""
        return re.findall(r'id=[\'"]([^\'"]+)[\'"]', self.html_content)

    def get_sidebar_hrefs(self) -> List[str]:
        """Returns internal anchor href targets in sidebar navigation."""
        sidebar_m = re.search(r'<(?:aside|nav)[^>]*class=[\'"][^\'"]*(?:sidebar|sidebar-nav)[^\'"]*[\'"][^>]*>(.*?)</(?:aside|nav)>', self.html_content, re.DOTALL | re.IGNORECASE)
        if not sidebar_m:
            sidebar_m = re.search(r'<aside[^>]*>(.*?)</aside>', self.html_content, re.DOTALL | re.IGNORECASE)
        if sidebar_m:
            return re.findall(r'<a[^>]+href=[\'"]#([^\'"]+)[\'"]', sidebar_m.group(1))
        return re.findall(r'<a[^>]+href=[\'"]#([^\'"]+)[\'"]', self.html_content)

    def get_placeholders(self, text: Optional[str] = None) -> List[str]:
        """Detects placeholder/stub text patterns in prose content (ignoring HTML attributes)."""
        target = text if text is not None else self.html_content
        clean_target = re.sub(r'<[^>]+>', ' ', target)
        patterns = [
            r'\bTODO\b',
            r'\bTBD\b',
            r'\[insert\b',
            r'lorem\s+ipsum',
            r'coming\s+soon',
            r'\bplaceholder\b'
        ]
        matches = []
        for pat in patterns:
            found = re.findall(pat, clean_target, re.IGNORECASE)
            if found:
                matches.extend(found)
        return matches

    def check_svg_xml_validity(self, svg_str: str) -> Tuple[bool, str]:
        """Validates XML well-formedness of an SVG element."""
        xml_input = svg_str
        if 'xmlns=' not in xml_input:
            xml_input = re.sub(r'<svg\b', '<svg xmlns="http://www.w3.org/2000/svg"', xml_input, count=1)
        try:
            ET.fromstring(xml_input)
            return True, ""
        except ET.ParseError as e:
            return False, str(e)
