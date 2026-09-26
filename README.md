# Amiyen Business Math Calculator

This version continues the project from the working Basic Business Math and Markup/Markdown modules and wires the remaining navigation categories into Flask, SQLite, `functions.py`, `input.py`, and `tne.py`.

## Run

```bash
pip install -r requirements.txt
python app.py
```

Then open the local Flask address shown in the terminal.

## Important input conventions

- Percentage/rate inputs use normal percentage numbers. Enter `25` for 25%, not `0.25`.
- Probability inputs such as `P(A)` use decimal probability values from 0 to 1.
- Overtime rate is a multiplier. Example: `1.5` means time-and-a-half.
- Statistics values and weights are comma-separated lists, for example `10, 12, 15, 20`.
- Capital Budgeting future cash flows are comma-separated and should not include the initial investment; the initial investment has its own field.
- Insurance short-rate factor is entered as a decimal factor, for example `0.60`.

## Implemented categories

1. Basic Business Math
2. Markup and Markdown
3. Discounts
4. Profit and Loss
5. Simple Interest
6. Compound Interest
7. Annuities
8. Loans
9. Present and Future Value
10. Depreciation
11. Commission
12. Payroll and Wages
13. Taxes
14. Break-Even Analysis
15. Business Revenue and Cost
16. Ratios and Proportions
17. Statistics
18. Probability
19. Percentage and Rate Conversions
20. Financial Ratios
21. Capital Budgeting
22. Stocks and Bonds
23. Insurance
24. Promissory Notes

The supplied business-math formula CSV is included under `reference/` for comparison.

## Database behavior

`database.initialize_database()` creates missing tables and adds missing columns without intentionally deleting existing Basic Business Math or Markup/Markdown records. New calculation history is stored in the corresponding SQLite table.

## Notes

The Basic Business Math and Markup/Markdown logic were kept structurally close to the existing project. The later modules use the same separation of responsibilities:

- `input.py` validates whether required values are present.
- `functions.py` contains the mathematical formulas.
- `tne.py` coordinates calculations.
- `database.py` initializes and updates SQLite tables.
- `app.py` handles Flask routes and forms.

## Dashboard and CSV history

The UI now uses dashboards instead of visible history tables.

- `/dashboard` shows an overview of all 24 calculator modules.
- Every calculator page shows latest-value cards, a history trend, and calculation activity.
- The old HTML history tables are still rendered as hidden data sources for the local JavaScript dashboard, but they are no longer displayed to the user.
- Every calculator page has an **Export CSV** button. CSV files are generated directly from SQLite using `/export/<module>.csv`.
- Charts are drawn with the browser Canvas API, so no Chart.js/CDN or internet connection is required.

The calculation logic and the original SQLite tables were not replaced.
