# Amiyen Business Math Calculator

Amiyen is a browser-based business math calculator built with Python, Flask, and SQLite. It provides 24 calculator modules for pricing, finance, payroll, statistics, and other business calculations. Enter values in a form, calculate results, and revisit saved calculations through dashboards or CSV exports.

## Contents

- [Features](#features)
- [Calculator modules](#calculator-modules)
- [Step-by-step setup](#step-by-step-setup)
- [Using the calculator](#using-the-calculator)
- [Input conventions](#input-conventions)
- [Calculation history and database](#calculation-history-and-database)
- [Running tests](#running-tests)
- [Project structure](#project-structure)
- [Troubleshooting](#troubleshooting)

## Features

- **24 calculators:** solve common business math problems through separate forms.
- **Saved history:** inputs and calculated results are stored in a local SQLite database.
- **Overview dashboard:** `/dashboard` summarizes records, module usage, and recent activity across all calculators.
- **Calculator dashboards:** each calculator shows latest-value cards, a history trend, and calculation activity.
- **CSV export:** download a calculator's saved history with its **Export CSV** button.
- **Local charts:** charts use the browser Canvas API without an external chart service or CDN.
- **Automatic database setup:** startup creates missing tables and adds missing columns. No separate database server or manual schema import is required.

## Calculator modules

| Module | What it calculates |
| --- | --- |
| Basic Business Math | Percentage, rate, base, and percentage changes |
| Markup and Markdown | Markup, markdown, selling price, cost, and related rates |
| Discounts | Trade discounts, net price, and successive discounts |
| Profit and Loss | Profit, loss, margin, and target selling price |
| Simple Interest | Interest and maturity value |
| Compound Interest | Compound amount, interest, present value, and effective annual rate |
| Annuities | Present and future values of ordinary annuities and annuities due |
| Loans | Periodic payments, total interest, and outstanding balance |
| Present and Future Value | Time value of money using simple and compound interest |
| Depreciation | Straight-line and declining-balance depreciation and book value |
| Commission | Commission, commission rate, sales, and total earnings |
| Payroll and Wages | Regular pay, overtime pay, deductions, and net pay |
| Taxes | Taxable income, tax, and net income using an entered tax rate |
| Break-Even Analysis | Contribution margin, break-even units and sales, and profit |
| Business Revenue and Cost | Revenue, fixed and variable costs, profit, and per-unit averages |
| Ratios and Proportions | Ratios, proportions, unit rates, and direct or inverse variation |
| Statistics | Mean, weighted mean, median, mode, range, variance, and standard deviation |
| Probability | Basic probability, complement, addition, multiplication, and conditional probability |
| Percentage and Rate Conversions | Decimal and percentage conversions and periodic rates |
| Financial Ratios | Liquidity, profitability, return, and debt-to-equity ratios |
| Capital Budgeting | Net present value, internal rate of return, and payback period |
| Stocks and Bonds | Dividend yield and current bond yield |
| Insurance | Insurance premiums and short-rate premiums |
| Promissory Notes | Maturity value, bank discount, and proceeds |

## Step-by-step setup

### 1. Install prerequisites

Install **Python 3 with pip and virtual environment support**, plus **Git** if you will clone the repository. Python **3.12** is verified with this project. You also need a web browser.

Check your Python installation:

```bash
python --version
python -m pip --version
```

On macOS or Linux, use `python3` instead of `python` if that is the command for your Python 3 installation.

### 2. Download the repository

```bash
git clone https://github.com/khaiyenIsCanadianHam/Amiyen.git
cd Amiyen
```

If you downloaded a ZIP instead, extract it and open a terminal in the extracted repository folder. If the repository is already checked out in your cloud environment, use that checkout.

### 3. Create and activate a virtual environment

Create it from the repository root:

```bash
python -m venv .venv
```

Activate it on **Windows PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on **Windows Command Prompt**:

```bat
.venv\Scripts\activate.bat
```

Or on **macOS / Linux**:

```bash
source .venv/bin/activate
```

### 4. Install the application dependency

With the virtual environment active:

```bash
python -m pip install "Flask==3.1.3"
```

**Why not use `pip install -r requirements.txt`?** The current file includes `sqlite3`, `statistics`, and `pathlib`, which are part of Python's standard library. In particular, `sqlite3` cannot be installed that way. The current application imports Flask as its only third-party dependency; `numpy_financial`, also listed in that file, is not used by the current code. The command above installs the verified Flask version without changing the dependency file.

### 5. Start the application

From the repository root:

```bash
cd app
python app.py
```

The entry point is **`app/app.py`**, not a file at the repository root. Startup initializes the SQLite database automatically and prints the server address.

For local development, open the printed address in your browser; by default it is `http://127.0.0.1:5000`. The home page opens Basic Business Math. The overview is at `/dashboard`.

`python app.py` enables Flask debug mode. Use it for development only. Stop the server with **Ctrl+C**.

### 6. Start it again later

Open a terminal in the repository root, activate the virtual environment using the command for your operating system, then run:

```bash
cd app
python app.py
```

Dependencies and database records remain on disk between runs; the server process must be started again.

## Using the calculator

1. Choose a calculator from the navigation menu.
2. Enter the values requested by its form, following the conventions below.
3. Select **Calculate**. A successful calculation saves a history record and reloads the calculator page.
4. Review its latest values, trend, and activity dashboard.
5. Select **Export CSV** to download that calculator's history, or visit `/dashboard` for the overall summary.

**Example: simple interest**

Open **Simple Interest** and enter principal `1000`, rate `10`, and time `2` years. Select **Calculate**. The interest is `200` and the maturity value is `1200`. Export the history to see the stored inputs and results.

## Input conventions

| Input | How to enter it |
| --- | --- |
| Percentage or rate | Enter `25` for 25%, rather than `0.25`, unless the field specifically asks for a decimal. |
| Probability | Enter a decimal between 0 and 1, such as `0.4` for `P(A)`. |
| Overtime rate | Enter a multiplier: `1.5` means time-and-a-half. |
| Statistics values and weights | Use comma-separated numbers, such as `10, 12, 15, 20`. Supply a corresponding weight for each value when using weights. |
| Capital Budgeting cash flows | Enter future cash flows as a comma-separated list. Put the initial investment in its separate field. |
| Insurance short-rate factor | Enter a decimal factor, such as `0.60`. |
| Annuity and loan rates | Use the rate per payment period, with the number of periods in matching units. |

Read each form's labels before submitting. Use consistent currency and time units. Calculations use the values you supply; the Taxes module does not fetch jurisdiction-specific tax rules.

## Calculation history and database

The database is **`app/data/amiyenDB.db`**. The repository includes a database, so existing records may appear on first launch. Each module stores history in its corresponding table. Basic Business Math and Markup/Markdown also use previous records for some change calculations.

Startup creates missing tables and adds missing columns without intentionally deleting existing records. The database folder must be writable. To preserve history before changes or moving the project, stop the server and back up the database file.

CSV downloads are generated from SQLite at `/export/<module>.csv`, using module codes such as `sin` for Simple Interest. The visible interface presents dashboards; hidden HTML tables supply chart data.

## Running tests

With the virtual environment active, run from the repository root:

```bash
cd app
python test_all.py
```

The existing suite checks formula results and database inserts for all **24 calculator modules**. It uses a temporary SQLite database and does not modify `app/data/amiyenDB.db`. A successful run ends with:

```text
Result: 24/24 calculator modules passed
```

The command exits with a nonzero status if any module fails. These tests cover calculations and persistence; they do not replace checking the browser interface.

## Project structure

```text
Amiyen/
├── README.md
├── requirements.txt         # Contains legacy/standard-library entries; see setup
└── app/
    ├── app.py               # Flask routes, forms, dashboards, and CSV exports
    ├── functions.py         # Mathematical formulas
    ├── input.py             # Input validation helpers
    ├── tne.py               # Calculation coordination
    ├── database.py          # Schema initialization and database updates
    ├── test_all.py          # Tests for all 24 calculator modules
    ├── data/
    │   └── amiyenDB.db      # Persistent calculation history
    ├── templates/           # HTML templates
    └── static/              # CSS and browser JavaScript
```

## Troubleshooting

| Problem | What to check |
| --- | --- |
| `No matching distribution found for sqlite3` | Use the Flask installation command in step 4. SQLite support comes with Python. |
| `No module named flask` | Activate the virtual environment and install Flask with that environment's `python -m pip`. |
| Python cannot find `app.py` | Change into the repository's `app` folder before running `python app.py`. |
| Port 5000 is already in use | From `app/`, run `python -m flask --app app run --port 5001` and use the address printed by that server. |
| SQLite reports a read-only database | Ensure `app/data/` and its database file are writable by the account running the app. |
| A form reports incomplete or invalid values | Check required fields, decimal versus percentage conventions, list formatting, and whether divisors are zero. |
| PowerShell blocks virtual environment activation | Use Command Prompt activation, or run `.\.venv\Scripts\python.exe -m pip install "Flask==3.1.3"` and `.\.venv\Scripts\python.exe app\app.py` from the repository root. |
