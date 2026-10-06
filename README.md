Liquidity Risk & LCR Calculator

A Python-based educational project for calculating the Liquidity Coverage Ratio (LCR) and performing simplified liquidity stress testing.

The project demonstrates how Python and pandas can be used to automate liquidity risk calculations commonly used in banking.

Project Overview

The calculator processes balance-sheet and liquidity assumptions from a CSV input file and calculates:

- High-Quality Liquid Assets (HQLA)
- Adjusted HQLA after haircuts
- Expected cash outflows
- Expected cash inflows
- Eligible inflows subject to the 75% inflow cap
- Net cash outflows
- Liquidity Coverage Ratio (LCR)

The project also includes simplified stress-testing scenarios to assess how changes in deposit and wholesale funding run-off assumptions affect the LCR.

Methodology

The simplified LCR calculation is:

LCR = HQLA / Net Cash Outflows × 100

Where:

Net Cash Outflows = Expected Cash Outflows − Eligible Cash Inflows

The model applies a simplified 75% cap on eligible cash inflows and adjusts HQLA for asset-specific haircuts.

Stress Testing

The model includes four scenarios:

Scenario| LCR| Status
Base Case| 173.73%| PASS
Deposit Stress| 125.00%| PASS
Funding Stress| 109.00%| PASS
Combined Stress| 87.00%| FAIL

The combined stress scenario demonstrates how simultaneous deterioration in deposit and wholesale funding assumptions can result in a liquidity shortfall.

Visualization

The project generates a bar chart comparing LCR across the different scenarios, with the 100% threshold highlighted.

Technologies

- Python
- pandas
- matplotlib
- CSV data processing
- Git / GitHub

Project Structure

project/
│
├── project.py
├── LCR Inputs.csv
├── README.md
├── requirements.txt
└── .gitignore

How to Run

Clone the repository and navigate to the project directory.

Install the required dependencies:

pip install -r requirements.txt

Run the calculator:

python project.py

The script reads the input data from "LCR Inputs.csv", calculates the base-case LCR, performs the stress tests and generates the visualization.

Example Use Cases

The model can be used to explore how liquidity risk changes when:

- deposit run-off assumptions increase,
- wholesale funding becomes less stable,
- HQLA is reduced through asset haircuts,
- expected cash inflows are constrained.

Key Learning Objectives

This project was developed to combine banking liquidity risk knowledge with practical Python skills, including:

- CSV data processing with pandas
- Data filtering and transformation
- Financial calculations
- Python functions
- Scenario analysis
- Stress testing
- Data visualization with matplotlib
- Git and GitHub version control

Disclaimer

This is an educational portfolio project inspired by banking liquidity risk concepts.

It uses simplified assumptions and is not intended to calculate regulatory LCR for an actual financial institution.
