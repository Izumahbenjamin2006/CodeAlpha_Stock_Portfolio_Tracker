import csv  # Import the built-in CSV module for clean file handling

# 1. DATA LAYER: Hardcoded dictionary of stock prices
def get_stock_prices():
    """Returns a hardcoded dictionary of stock prices."""
    return {
        "AAPL": 180.00, "TSLA": 250.00, "GOOGL": 140.00, 
        "MSFT": 380.00, "AMZN": 175.00, "NVDA": 800.00,
        "META": 505.00, "JPM": 195.00
    }

# 2. INPUT LAYER: Handles user input and validation
def get_user_input(prices):
    """Prompts user for stock and quantity, returns valid data."""
    print("\n--- Available Stocks ---")
    for symbol, price in prices.items():
        print(f"  {symbol}: ${price:.2f}")
    print("------------------------")

    portfolio = []
    
    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        
        if symbol == "DONE" or symbol == "":
            break
            
        if symbol not in prices:
            print("⚠️ Stock not found. Please try again.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("⚠️ Quantity must be greater than zero.")
                continue
        except ValueError:
            print("⚠️ Invalid input. Please enter a whole number.")
            continue
            
        portfolio.append({"symbol": symbol, "quantity": quantity})
        
    return portfolio

# 3. LOGIC LAYER: Basic arithmetic to calculate totals
def calculate_totals(portfolio, prices):
    """Calculates individual costs and total investment."""
    total_investment = 0.0
    
    for stock in portfolio:
        price = prices[stock["symbol"]]
        cost = price * stock["quantity"]
        
        # Add calculated data to the stock dictionary
        stock["price"] = price       
        stock["cost"] = cost         
        total_investment += cost
        
    return total_investment

# 4. OUTPUT LAYER: Displays results and handles clean CSV saving
def display_and_save(portfolio, total_investment):
    """Prints the summary and saves to a perfectly formatted CSV file."""
    print("\n" + "="*50)
    print("           PORTFOLIO SUMMARY")
    print("="*50)
    print(f"{'Symbol':<8} | {'Qty':<5} | {'Price':<10} | {'Total':<12}")
    print("-" * 50)
    
    for stock in portfolio:
        print(f"{stock['symbol']:<8} | {stock['quantity']:<5} | ${stock['price']:<9.2f} | ${stock['cost']:<11.2f}")
        
    print("-" * 50)
    print(f"TOTAL INVESTMENT: {'':<20} ${total_investment:.2f}")
    print("="*50)

    # --- CLEAN CSV GENERATION ---
    save_choice = input("\nSave results to 'portfolio.csv'? (y/n): ").lower()
    if save_choice == 'y':
        # Note: newline='' prevents blank lines between rows on Windows
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)
            
            # Write the header row
            writer.writerow(["Symbol", "Quantity", "Price", "Total"])
            
            # Write the data rows
            for stock in portfolio:
                writer.writerow([
                    stock['symbol'], 
                    stock['quantity'], 
                    f"{stock['price']:.2f}",  # Formats to 2 decimal places
                    f"{stock['cost']:.2f}"    # Formats to 2 decimal places
                ])
        print("✅ Successfully saved a clean 'portfolio.csv'!")

# 5. MAIN EXECUTION: Ties everything together
def main():
    """Main function to run the Stock Portfolio Tracker."""
    print("Welcome to the Stock Portfolio Tracker!")
    
    prices = get_stock_prices()
    portfolio = get_user_input(prices)
    
    if not portfolio:
        print("\nNo stocks added. Exiting program.")
        return
        
    total = calculate_totals(portfolio, prices)
    display_and_save(portfolio, total)

# Run the program
if __name__ == "__main__":
    main()