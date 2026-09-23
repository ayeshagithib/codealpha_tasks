"""
Stock Portfolio Tracker
------------------------
CodeAlpha Python Programming Internship - Task 2

Goal: Track a user's stock holdings against hardcoded stock prices,
calculate total investment value, and save a summary report.

Key concepts used: dictionary, input/output, basic arithmetic, file handling.
"""

# Hardcoded stock prices (price per share, in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
    "META": 300,
    "NFLX": 480,
}


def show_available_stocks():
    """Print the list of stocks the tracker supports, with their prices."""
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} - ${price} per share")
    print()


def get_user_portfolio():
    """
    Repeatedly ask the user for a stock symbol and quantity.
    Returns a dictionary of {symbol: quantity}.
    """
    portfolio = {}

    print("Enter stock symbol and quantity. Type 'done' as the symbol to finish.\n")

    while True:
        symbol = input("Stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' is not in our price list. Please choose from the available stocks.")
            continue

        quantity_input = input(f"Quantity of {symbol}: ").strip()

        if not quantity_input.isdigit():
            print("  Please enter a whole number for quantity.")
            continue

        quantity = int(quantity_input)

        if quantity <= 0:
            print("  Quantity must be greater than zero.")
            continue

        # If the user enters the same stock twice, add to the existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"  Added {quantity} shares of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    """
    Given a portfolio dict {symbol: quantity}, calculate the value of each
    holding and the total investment. Returns (breakdown_list, total).
    """
    breakdown = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        breakdown.append((symbol, quantity, price, value))

    return breakdown, total


def print_summary(breakdown, total):
    """Print a formatted summary table to the console."""
    print("\n" + "=" * 50)
    print("PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Symbol':<8}{'Qty':<6}{'Price':<10}{'Value':<10}")
    print("-" * 50)

    for symbol, quantity, price, value in breakdown:
        print(f"{symbol:<8}{quantity:<6}${price:<9}${value:<9}")

    print("-" * 50)
    print(f"TOTAL INVESTMENT: ${total}")
    print("=" * 50)


def save_report(breakdown, total, filename="portfolio_report.txt"):
    """Save the portfolio summary to a text file."""
    with open(filename, "w") as f:
        f.write("STOCK PORTFOLIO REPORT\n")
        f.write("=" * 50 + "\n")
        f.write(f"{'Symbol':<8}{'Qty':<6}{'Price':<10}{'Value':<10}\n")
        f.write("-" * 50 + "\n")

        for symbol, quantity, price, value in breakdown:
            f.write(f"{symbol:<8}{quantity:<6}${price:<9}${value:<9}\n")

        f.write("-" * 50 + "\n")
        f.write(f"TOTAL INVESTMENT: ${total}\n")

    print(f"\nReport saved to '{filename}'")


def main():
    print("=" * 50)
    print("  WELCOME TO THE STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    show_available_stocks()

    portfolio = get_user_portfolio()

    if not portfolio:
        print("\nNo stocks were added. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)
    print_summary(breakdown, total)

    save_choice = input("\nSave this report to a file? (y/n): ").strip().lower()
    if save_choice == "y":
        save_report(breakdown, total)


if __name__ == "__main__":
    main()
