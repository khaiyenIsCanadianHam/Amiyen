"""Automated smoke + formula tests for all 24 Amiyen calculators.

Run from the app folder:
    python test_all.py

The tests use a temporary SQLite database, so amiyenDB.db is not modified.
"""

from pathlib import Path
import contextlib
import io
import math
import sqlite3
import statistics
import tempfile

import database
import functions
import tne


def almost_equal(actual, expected, tolerance=1e-6):
    if expected is None:
        return actual is None
    if isinstance(expected, bool):
        return actual is expected or actual == expected
    if isinstance(expected, (int, float)):
        return isinstance(actual, (int, float)) and math.isclose(
            float(actual), float(expected), rel_tol=tolerance, abs_tol=tolerance
        )
    return actual == expected


def assert_values(name, actual, expected):
    if len(actual) != len(expected):
        raise AssertionError(
            f"{name}: returned {len(actual)} values, expected {len(expected)}"
        )

    problems = []
    for index, (actual_value, expected_value) in enumerate(zip(actual, expected)):
        if not almost_equal(actual_value, expected_value):
            problems.append(
                f"value {index}: got {actual_value!r}, expected {expected_value!r}"
            )

    if problems:
        raise AssertionError(name + ": " + "; ".join(problems))


def create_test_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for table_name, columns in database.TABLES.items():
        database._ensureTable(cursor, table_name, columns)
    conn.commit()
    conn.close()


def latest_row_count(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    conn.close()
    return count


def run_quietly(function, *args):
    with contextlib.redirect_stdout(io.StringIO()):
        return function(*args)


def test_all():
    passed = 0
    failed = 0
    details = []

    with tempfile.TemporaryDirectory(prefix="amiyen_tests_") as temp_dir:
        db_path = str(Path(temp_dir) / "amiyen_test.db")
        create_test_database(db_path)

        tests = []

        # 1. Basic Business Math. Seed an old percentage so change calculations are testable.
        database.updateBbm_db(200, 25, 800, None, None, None, db_path)
        tests.append({
            "name": "Basic Business Math",
            "table": "bbm_db",
            "before": 1,
            "calculate": lambda: tne.calcVal_bbm(None, 50, 800, db_path),
            "expected": (400, 50, 800, 100, 100, 0),
            "save": lambda result: database.updateBbm_db(*result, db_path),
        })

        # 2. Markup and Markdown. Seed the original/latest selling price.
        database.updateMam_db(None, None, None, 1000, None, None, None, None, None, None, db_path)
        tests.append({
            "name": "Markup and Markdown",
            "table": "mam_db",
            "before": 1,
            "calculate": lambda: tne.calcVal_mam(900, 200, None, db_path),
            "expected": (
                200,
                (200 / 700) * 100,
                (200 / 900) * 100,
                900,
                900,
                700,
                100,
                10,
                900,
                900,
            ),
            "save": lambda result: database.updateMam_db(*result, db_path),
        })

        tests.extend([
            {
                "name": "Discounts",
                "table": "dis_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_dis(1000, 20, 10),
                "expected": (1000, 20, 10, 200, 800, 800, 20, 720, 28),
                "save": lambda r: database.updateDis_db(*r, db_path),
            },
            {
                "name": "Profit and Loss",
                "table": "pnl_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_pnl(800, 1000, 25),
                "expected": (800, 1000, 25, 200, 0, 25, 20, 1000, 800, 0),
                "save": lambda r: database.updatePnl_db(*r, db_path),
            },
            {
                "name": "Simple Interest",
                "table": "sin_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_sin(1000, 10, 2),
                "expected": (200, 1000, 10, 2, 1200, 1200),
                "save": lambda r: database.updateSin_db(*r, db_path),
            },
        ])

        compound_amount = 1000 * (1 + (0.12 / 12)) ** 24
        effective_annual_rate = ((1 + (0.12 / 12)) ** 12 - 1) * 100
        tests.append({
            "name": "Compound Interest",
            "table": "cin_db",
            "before": 0,
            "calculate": lambda: tne.calcVal_cin(1000, 12, 2, 12),
            "expected": (
                1000, 12, 2, 12,
                compound_amount,
                compound_amount - 1000,
                1000,
                compound_amount,
                1000,
                effective_annual_rate,
            ),
            "save": lambda r: database.updateCin_db(*r, db_path),
        })

        annuity_rate = 0.01
        annuity_periods = 12
        annuity_payment = 100
        annuity_fv = annuity_payment * (((1 + annuity_rate) ** annuity_periods - 1) / annuity_rate)
        annuity_pv = annuity_payment * ((1 - (1 + annuity_rate) ** (-annuity_periods)) / annuity_rate)
        tests.append({
            "name": "Annuities",
            "table": "ann_db",
            "before": 0,
            "calculate": lambda: tne.calcVal_ann(100, 1, 12),
            "expected": (
                100, 1, 12,
                annuity_fv,
                annuity_pv,
                annuity_fv * 1.01,
                annuity_pv * 1.01,
                100,
            ),
            "save": lambda r: database.updateAnn_db(*r, db_path),
        })

        loan_rate = 0.01
        loan_principal = 12000
        loan_periods = 12
        loan_payment = loan_principal * loan_rate / (1 - (1 + loan_rate) ** (-loan_periods))
        loan_total = loan_payment * loan_periods
        loan_balance = (
            loan_principal * (1 + loan_rate) ** 6
            - loan_payment * (((1 + loan_rate) ** 6 - 1) / loan_rate)
        )
        tests.append({
            "name": "Loans",
            "table": "loa_db",
            "before": 0,
            "calculate": lambda: tne.calcVal_loa(12000, 1, 12, 6),
            "expected": (
                12000, 1, 12, 6,
                loan_payment,
                loan_payment,
                loan_total,
                loan_total - 12000,
                loan_balance,
            ),
            "save": lambda r: database.updateLoa_db(*r, db_path),
        })

        pfv_future = 1000 * 1.05 ** 2
        pfv_simple = 1000 * (1 + 0.05 * 2)
        pfv_compound = 1000 * (1 + 0.05 / 12) ** 24
        tests.append({
            "name": "Present and Future Value",
            "table": "pfv_db",
            "before": 0,
            "calculate": lambda: tne.calcVal_pfv(1000, 5, 2, 2, 12),
            "expected": (1000, 5, 2, 2, 12, pfv_future, 1000, pfv_simple, pfv_compound),
            "save": lambda r: database.updatePfv_db(*r, db_path),
        })

        straight_line = (10000 - 1000) / 5
        declining_book = 10000 * 0.8 ** 2
        tests.extend([
            {
                "name": "Depreciation",
                "table": "dep_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_dep(10000, 1000, 5, 2, 20),
                "expected": (
                    10000, 1000, 5, 2, 20,
                    straight_line,
                    10000 - straight_line * 2,
                    9000,
                    declining_book * 0.2,
                    declining_book,
                ),
                "save": lambda r: database.updateDep_db(*r, db_path),
            },
            {
                "name": "Commission",
                "table": "com_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_com(10000, 5, 500),
                "expected": (10000, 5, 500, 500, 1000, 5, 10000),
                "save": lambda r: database.updateCom_db(*r, db_path),
            },
            {
                "name": "Payroll and Wages",
                "table": "paw_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_paw(100, 40, 1.5, 10, 500, 200, 100, 50),
                "expected": (100, 40, 1.5, 10, 500, 200, 100, 50, 5550, 4000, 1500, 4750, 800),
                "save": lambda r: database.updatePaw_db(*r, db_path),
            },
            {
                "name": "Taxes",
                "table": "tax_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_tax(50000, 10000, 10, 2000),
                "expected": (50000, 10000, 10, 2000, 4000, 40000, 44000),
                "save": lambda r: database.updateTax_db(*r, db_path),
            },
            {
                "name": "Break-Even Analysis",
                "table": "bea_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_bea(100, 60, 4000, 100),
                "expected": (100, 60, 4000, 100, 40, 40, 100, 10000, 0, 10000, 10000),
                "save": lambda r: database.updateBea_db(*r, db_path),
            },
            {
                "name": "Business Revenue and Cost",
                "table": "brc_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_brc(100, 100, 2000, 50),
                "expected": (100, 100, 2000, 50, 10000, 7000, 5000, 3000, 70, 100, 30),
                "save": lambda r: database.updateBrc_db(*r, db_path),
            },
            {
                "name": "Ratios and Proportions",
                "table": "rnp_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_rnp(2, 4, 3, 6, 100, 20, 5, 2),
                "expected": (2, 4, 3, 6, 100, 20, 5, 2, 0.5, True, True, 5, 10, 2.5),
                "save": lambda r: database.updateRnp_db(*r, db_path),
            },
        ])

        stat_values = [1, 2, 3, 4]
        stat_weights = [1, 1, 1, 1]
        tests.append({
            "name": "Statistics",
            "table": "sta_db",
            "before": 0,
            "calculate": lambda: tne.calcVal_sta(stat_values, stat_weights),
            "expected": (
                "1, 2, 3, 4",
                "1, 1, 1, 1",
                2.5,
                2.5,
                3,
                1.25,
                math.sqrt(1.25),
                2.5,
                2.5,
                2.5,
                statistics.mode(stat_values),
                statistics.variance(stat_values),
                statistics.stdev(stat_values),
            ),
            "save": lambda r: database.updateSta_db(*r, db_path),
        })

        tests.extend([
            {
                "name": "Probability",
                "table": "pro_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_pro(2, 5, 0.4, 0.5, 0.2),
                "expected": (2, 5, 0.4, 0.5, 0.2, 0.4, 0.6, 0.7, 0.2, 0.4),
                "save": lambda r: database.updatePro_db(*r, db_path),
            },
            {
                "name": "Percentage and Rate Conversions",
                "table": "prc_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_prc(0.25, 25, 0.25, 12),
                "expected": (0.25, 25, 0.25, 12, 25, 0.25, 0.25, 25, 1, 3, 6),
                "save": lambda r: database.updatePrc_db(*r, db_path),
            },
            {
                "name": "Financial Ratios",
                "table": "fra_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_fra(
                    20000, 10000, 5000, 2000, 10000, 3000,
                    30000, 15000, 12000, 18000, 50000
                ),
                "expected": (
                    20000, 10000, 5000, 2000, 10000, 3000,
                    30000, 15000, 12000, 18000, 50000,
                    2, 1.5, 20, 10, 20, 12000 / 18000, 6,
                ),
                "save": lambda r: database.updateFra_db(*r, db_path),
            },
        ])

        cash_flows = [400, 400, 400]
        npv = sum(cf / 1.1 ** t for t, cf in enumerate(cash_flows, start=1)) - 1000
        irr = functions.calcInternalRateOfReturn([-1000] + cash_flows)
        tests.append({
            "name": "Capital Budgeting",
            "table": "cbu_db",
            "before": 0,
            "calculate": lambda: tne.calcVal_cbu(1000, 400, 10, cash_flows),
            "expected": (1000, 400, 10, "400, 400, 400", npv, irr, 2.5),
            "save": lambda r: database.updateCbu_db(*r, db_path),
        })

        tests.extend([
            {
                "name": "Stocks and Bonds",
                "table": "sbo_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_sbo(5, 100, 60, 1000),
                "expected": (5, 100, 60, 1000, 5, 6),
                "save": lambda r: database.updateSbo_db(*r, db_path),
            },
            {
                "name": "Insurance",
                "table": "inc_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_inc(100000, 2, 1200, 0.25),
                "expected": (100000, 2, 1200, 0.25, 2000, 300),
                "save": lambda r: database.updateInc_db(*r, db_path),
            },
            {
                "name": "Promissory Notes",
                "table": "pno_db",
                "before": 0,
                "calculate": lambda: tne.calcVal_pno(10000, 6, 1, 5),
                "expected": (10000, 6, 1, 5, 10600, 530, 10070),
                "save": lambda r: database.updatePno_db(*r, db_path),
            },
        ])

        print("Amiyen — all calculator tests")
        print("=" * 54)

        for test in tests:
            try:
                result = run_quietly(test["calculate"])
                assert_values(test["name"], result, test["expected"])

                before_count = latest_row_count(db_path, test["table"])
                save_result = run_quietly(test["save"], result)
                after_count = latest_row_count(db_path, test["table"])

                if save_result != 1:
                    raise AssertionError("database update returned failure")
                if after_count != before_count + 1:
                    raise AssertionError(
                        f"database row count did not increase ({before_count} -> {after_count})"
                    )

                passed += 1
                print(f"[PASS] {test['name']}")
            except Exception as error:
                failed += 1
                details.append((test["name"], str(error)))
                print(f"[FAIL] {test['name']}: {error}")

    print("=" * 54)
    print(f"Result: {passed}/{passed + failed} calculator modules passed")

    if details:
        print("\nFailures:")
        for name, error in details:
            print(f"- {name}: {error}")

    return failed == 0


if __name__ == "__main__":
    success = test_all()
    raise SystemExit(0 if success else 1)
