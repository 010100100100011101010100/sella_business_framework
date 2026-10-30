#!/usr/bin/env python3
"""
run_tests.py
Master Test Suite Runner for JEE Mechanics & Rotational Dynamics Master Handbook.
Orchestrates and executes 4 tiers of end-to-end automated testing:
  - Tier 1: Core Feature Inventory & Functional Completeness (45 tests)
  - Tier 2: Boundary Value Analysis & Stress Thresholds (50 tests)
  - Tier 3: Cross-Feature Interactions & Pairwise Combinations (16 tests)
  - Tier 4: Real-World Application & Workload Scenarios (5 scenarios)

Total Suite: 116 tests.
"""

import argparse
import json
import sys
import time
import unittest
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

# Ensure delivery root and tests package are in sys.path
TESTS_DIR = Path(__file__).resolve().parent
DELIVERY_ROOT = TESTS_DIR.parent
if str(DELIVERY_ROOT) not in sys.path:
    sys.path.insert(0, str(DELIVERY_ROOT))

from tests import (
    test_tier1_features,
    test_tier2_boundaries,
    test_tier3_cross_features,
    test_tier4_real_world,
)


class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


class CustomTestResult(unittest.TestResult):
    """Structured test collector recording detailed test outcomes and timings."""

    def __init__(self, verbose: bool = False):
        super().__init__()
        self.verbose = verbose
        self.records: List[Dict[str, Any]] = []
        self._test_start_time = 0.0

    def startTest(self, test: unittest.TestCase):
        super().startTest(test)
        self._test_start_time = time.time()

    def addSuccess(self, test: unittest.TestCase):
        super().addSuccess(test)
        elapsed = time.time() - self._test_start_time
        doc = test.shortDescription() or test._testMethodName
        self.records.append({
            "id": test.id(),
            "name": test._testMethodName,
            "description": doc,
            "status": "PASS",
            "duration": elapsed,
            "error": None
        })
        if self.verbose:
            print(f"  {Color.GREEN} PASS{Color.RESET} {test.id()} {Color.DIM}({elapsed*1000:.1f}ms){Color.RESET}")

    def addFailure(self, test: unittest.TestCase, err):
        super().addFailure(test, err)
        elapsed = time.time() - self._test_start_time
        doc = test.shortDescription() or test._testMethodName
        err_msg = self._exc_info_to_string(err, test)
        self.records.append({
            "id": test.id(),
            "name": test._testMethodName,
            "description": doc,
            "status": "FAIL",
            "duration": elapsed,
            "error": err_msg
        })
        if self.verbose:
            print(f"  {Color.RED} FAIL{Color.RESET} {test.id()} {Color.DIM}({elapsed*1000:.1f}ms){Color.RESET}")

    def addError(self, test: unittest.TestCase, err):
        super().addError(test, err)
        elapsed = time.time() - self._test_start_time
        doc = test.shortDescription() or test._testMethodName
        err_msg = self._exc_info_to_string(err, test)
        self.records.append({
            "id": test.id(),
            "name": test._testMethodName,
            "description": doc,
            "status": "ERROR",
            "duration": elapsed,
            "error": err_msg
        })
        if self.verbose:
            print(f"  {Color.RED} ERROR{Color.RESET} {test.id()} {Color.DIM}({elapsed*1000:.1f}ms){Color.RESET}")


def build_tier_suite(tier: int) -> unittest.TestSuite:
    """Loads tests corresponding to a specific tier."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    if tier == 1:
        suite.addTests(loader.loadTestsFromModule(test_tier1_features))
    elif tier == 2:
        suite.addTests(loader.loadTestsFromModule(test_tier2_boundaries))
    elif tier == 3:
        suite.addTests(loader.loadTestsFromModule(test_tier3_cross_features))
    elif tier == 4:
        suite.addTests(loader.loadTestsFromModule(test_tier4_real_world))
    return suite


def run_test_suite(selected_tier: str = "all", verbose: bool = False, json_output: Optional[str] = None) -> int:
    """Executes selected test tiers and generates formatted report."""
    tiers_to_run = [1, 2, 3, 4] if selected_tier == "all" else [int(selected_tier)]

    tier_descriptions = {
        1: "Tier 1: Core Feature Inventory & Functional Completeness (45 tests)",
        2: "Tier 2: Boundary Value Analysis & Stress Thresholds (50 tests)",
        3: "Tier 3: Cross-Feature Interactions & Pairwise Combinations (16 tests)",
        4: "Tier 4: Real-World Application & Workload Scenarios (5 scenarios)",
    }

    print(f"\n{Color.BOLD}{Color.CYAN}════════════════════════════════════════════════════════════════════════════════{Color.RESET}")
    print(f"{Color.BOLD}{Color.YELLOW}   JEE Mechanics & Rotational Dynamics Master Handbook — E2E Test Suite{Color.RESET}")
    print(f"{Color.BOLD}{Color.CYAN}════════════════════════════════════════════════════════════════════════════════{Color.RESET}")
    print(f"{Color.DIM}Target Repository : {DELIVERY_ROOT}{Color.RESET}")
    print(f"{Color.DIM}Execution Scope   : Tier(s) {', '.join(str(t) for t in tiers_to_run)}{Color.RESET}\n")

    tier_results = {}
    total_start = time.time()

    for t in tiers_to_run:
        suite = build_tier_suite(t)
        desc = tier_descriptions.get(t, f"Tier {t}")
        print(f"{Color.BOLD}▶ Running {desc}...{Color.RESET}")

        result = CustomTestResult(verbose=verbose)
        suite.run(result)

        passed = len(result.records) - len(result.failures) - len(result.errors)
        failed = len(result.failures)
        errors = len(result.errors)
        total = len(result.records)

        status_color = Color.GREEN if (failed == 0 and errors == 0) else Color.RED
        print(f"  Status: {status_color}{passed}/{total} Passed{Color.RESET} "
              f"({failed} Failed, {errors} Errors)\n")

        tier_results[t] = {
            "title": desc,
            "total": total,
            "passed": passed,
            "failed": failed,
            "errors": errors,
            "records": result.records,
            "failures": result.failures,
            "err_list": result.errors
        }

    total_duration = time.time() - total_start

    # Consolidated Results Table
    print(f"{Color.BOLD}{Color.CYAN}────────────────────────────────────────────────────────────────────────────────{Color.RESET}")
    print(f"{Color.BOLD}Consolidated Test Results Summary{Color.RESET}")
    print(f"{Color.BOLD}{Color.CYAN}────────────────────────────────────────────────────────────────────────────────{Color.RESET}")
    print(f"{'Tier':<8} | {'Scope':<50} | {'Pass Rate':<12} | {'Status'}")
    print(f"{'-'*8}-|-{'-'*50}-|-{'-'*12}-|--------")

    grand_total = 0
    grand_passed = 0
    grand_failed = 0
    grand_errors = 0

    for t in tiers_to_run:
        r = tier_results[t]
        grand_total += r["total"]
        grand_passed += r["passed"]
        grand_failed += r["failed"]
        grand_errors += r["errors"]
        rate = (r["passed"] / r["total"] * 100) if r["total"] > 0 else 0
        status_text = f"{Color.GREEN}PASS{Color.RESET}" if (r["failed"] == 0 and r["errors"] == 0) else f"{Color.RED}FAIL{Color.RESET}"
        print(f"Tier {t:<3} | {r['title'][:50]:<50} | {rate:5.1f}% ({r['passed']}/{r['total']}) | {status_text}")

    print(f"{'-'*8}-|-{'-'*50}-|-{'-'*12}-|--------")
    overall_rate = (grand_passed / grand_total * 100) if grand_total > 0 else 0
    print(f"{Color.BOLD}{'TOTAL':<8} | {'All Selected Tiers':<50} | {overall_rate:5.1f}% ({grand_passed}/{grand_total}) | "
          f"{Color.GREEN if grand_failed + grand_errors == 0 else Color.RED}"
          f"{'PASS' if grand_failed + grand_errors == 0 else 'FAIL'}{Color.RESET}{Color.RESET}\n")

    # Detailed Failure Diagnostics
    if grand_failed > 0 or grand_errors > 0:
        print(f"{Color.BOLD}{Color.RED}Failure Diagnostics & Defect Analysis:{Color.RESET}")
        print(f"{Color.DIM}Escalate these defects to implementing agents for subsequent milestone refinement:{Color.RESET}\n")

        for t in tiers_to_run:
            r = tier_results[t]
            if r["failed"] > 0 or r["errors"] > 0:
                print(f"{Color.BOLD}{Color.YELLOW}[{r['title']}]{Color.RESET}")
                for test_case, trace in r["failures"] + r["err_list"]:
                    # Extract last assertion error line
                    lines = [l.strip() for l in trace.strip().splitlines() if l.strip()]
                    last_line = lines[-1] if lines else "Unknown assertion failure"
                    test_id = test_case.id() if hasattr(test_case, 'id') else str(test_case)
                    print(f"  • {Color.RED}{test_id}{Color.RESET}")
                    print(f"    {Color.DIM}→ {last_line}{Color.RESET}")
                print()

    # Optional JSON Export
    if json_output:
        report_data = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_tests": grand_total,
            "passed": grand_passed,
            "failed": grand_failed,
            "errors": grand_errors,
            "pass_rate_percent": round(overall_rate, 2),
            "execution_time_seconds": round(total_duration, 3),
            "tiers": {
                f"tier_{t}": {
                    "title": tier_results[t]["title"],
                    "total": tier_results[t]["total"],
                    "passed": tier_results[t]["passed"],
                    "failed": tier_results[t]["failed"],
                    "records": tier_results[t]["records"]
                }
                for t in tiers_to_run
            }
        }
        with open(json_output, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2)
        print(f"{Color.CYAN}Structured JSON test report saved to: {json_output}{Color.RESET}\n")

    return 0 if (grand_failed == 0 and grand_errors == 0) else 1


def main():
    parser = argparse.ArgumentParser(
        description="Master Test Runner for JEE Mechanics & Rotational Dynamics Master Handbook."
    )
    parser.add_argument(
        "--tier",
        choices=["1", "2", "3", "4", "all"],
        default="all",
        help="Specify which tier to execute (1, 2, 3, 4, or all). Default is all."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output printing each individual test assertion."
    )
    parser.add_argument(
        "--json",
        type=str,
        default=None,
        help="Path to export structured test results as JSON."
    )

    args = parser.parse_args()
    exit_code = run_test_suite(selected_tier=args.tier, verbose=args.verbose, json_output=args.json)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
