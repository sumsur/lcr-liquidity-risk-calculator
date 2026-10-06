LCR Calculator

A Python-based educational project for calculating the Liquidity Coverage Ratio (LCR) and performing simplified liquidity stress testing.

Project Overview

The project demonstrates how Python can be used to automate key liquidity risk calculations commonly used in banking.

The calculator processes balance-sheet and liquidity inputs from a CSV file and calculates:

- High-Quality Liquid Assets (HQLA)
- Adjusted HQLA after haircuts
- Expected cash outflows
- Expected cash inflows
- Eligible inflows subject to the 75% inflow cap
- Net cash outflows
- Liquidity Coverage Ratio (LCR)

The project also includes simplified stress-testing scenarios to assess how changes in deposit run-off and wholesale funding run-off affect the LCR.

Methodology

The basic LCR calculation is:

LCR = HQLA / Net Cash Outflows × 100

Where:

Net Cash Outflows = Expected Cash Outflows − Eligible Cash Inflows

The model applies a simplified 75% cap to eligible cash inflows.

HQLA is adjusted for asset-specific haircuts before calculating the LCR.

Stress Testing

The project includes simplified liquidity stress scenarios:

- Base Case
- Deposit Stress
- Funding Stress
- Combined Deposit & Funding Stress

Stress scenarios modify selected run-off assumptions and recalculate the resulting LCR.

The stress-testing component is designed for educational and portfolio purposes and does not represent a fully regulatory-compliant LCR implementation.

Technologies

- Python
- pandas
- CSV data processing

Project Structure

project/
│
├── project.py
├── LCR Inputs.csv
├── README.md
├── requirements.txt
└── .gitignore

How to Run

Install the required Python package:

pip install -r requirements.txt

Then run:

python project.py

The script reads the input data from "LCR Inputs.csv" and calculates the base-case LCR and stress-test results.

Example Use Case

The project can be used to explore how liquidity risk changes when:

- deposit run-off assumptions increase,
- wholesale funding becomes less stable,
- available HQLA is reduced through asset haircuts,
- expected cash inflows are constrained.

Disclaimer

This is an educational portfolio project inspired by banking liquidity risk concepts.

It uses simplified assumptions and is not intended to calculate regulatory LCR for an actual financial institution.
