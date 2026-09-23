# CodeAlpha Stock Portfolio Tracker

A simple command-line stock portfolio tracker built for the CodeAlpha Python Programming Internship (Task 2).

## Features
- Displays a list of available stocks with hardcoded prices
- Lets the user build a portfolio by entering stock symbols and quantities
- Calculates total investment value across all holdings
- Prints a formatted summary table
- Optionally saves the report to a `.txt` file

## Key Concepts Used
- Dictionaries
- Input/output handling
- Basic arithmetic
- File handling (optional save feature)

## How to Run
```bash
python stock_tracker.py
```

## Example
```
Stock symbol (or 'done' to finish): AAPL
Quantity of AAPL: 10
  Added 10 shares of AAPL.

Stock symbol (or 'done' to finish): TSLA
Quantity of TSLA: 5
  Added 5 shares of TSLA.

Stock symbol (or 'done' to finish): done

==================================================
PORTFOLIO SUMMARY
==================================================
Symbol  Qty   Price     Value
--------------------------------------------------
AAPL    10    $180      $1800
TSLA    5     $250      $1250
--------------------------------------------------
TOTAL INVESTMENT: $3050
==================================================
```

## Internship
Built as part of the [CodeAlpha](https://www.codealpha.tech) Python Programming Internship.
