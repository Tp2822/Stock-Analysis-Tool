import yfinance as yf
import math
import statistics

# Use below to see data and names included in yfinance
#stock = yf.Ticker("AAPL")
#print(stock.info.keys())

def format_money(number):
    if not isinstance(number, (int, float)):
        return number
    if number >= 1000000000000:
        return f"${round(number/1000000000000, 2)} T"
    elif number >= 1000000000 and number < 1000000000000:
        return f"${round(number/1000000000, 2)} B"
    elif number < 1000000000 and number >= 1000000:
        return f"${round(number/1000000, 2)} M"
    else:
        return f"${round(number, 2)}"

def format_percentage(number):
    if not isinstance(number, (int, float)):
            return number
    else:
        return f"{round(number,2)}%"

def format_ratio(number):
    if not isinstance(number, (int, float)):
        return number
    else:
        return f"{round(number,2)}"

def format_decimal_to_percentage(number):
    if not isinstance(number, (int, float)):
        return number
    else:
        return f"{round(number * 100, 2)}%"

def stock_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    stock_name = info.get("displayName", "Unknown")
    current_price = format_money(info.get("currentPrice", "N/A"))
    market_cap = format_money(info.get("marketCap", "N/A"))
    trailing_pe = format_ratio(info.get("trailingPE", "N/A"))
    revenue = format_money(info.get("totalRevenue", "N/A"))
    earnings_per_share = format_money(info.get("trailingEps", "N/A"))
    dividend_yield = format_percentage(info.get("dividendYield", "N/A"))
    week_high = format_money(info.get("fiftyTwoWeekHigh", "N/A"))
    week_low = format_money(info.get("fiftyTwoWeekLow", "N/A"))

    return (f"{stock_name} ({ticker.upper()})\n" 
            f"Current Price: {current_price}\n" 
            f"Market Cap: {market_cap}\n" 
            f"P/E Ratio: {trailing_pe}\n"
            f"Total Revenue: {revenue}\n" 
            f"Earnings per Share: {earnings_per_share}\n"
            f"Dividend Yield: {dividend_yield}\n"
            f"52-Week-High: {week_high}\n"
            f"52-Week-Low: {week_low}")

# Run this to see history columns
#stock = yf.Ticker("AAPL")
#history = stock.history(period="1mo")
#print(history.columns)

def get_history(ticker, performance_time):
    stock = yf.Ticker(ticker)
    periods = {
        "1 month": "1mo",
        "6 months": "6mo",
        "1 year": "1y",
        "5 years": "5y"
    }
    if performance_time not in periods:
        return "Invalid time period!"
    return stock.history(period=periods[performance_time])

def ticker_return(history, performance_time):
    prices = history["Close"].tolist()
    start_price = prices[0]
    end_price = prices[-1]
    returns = format_percentage(((end_price - start_price)/start_price)* 100)
    return (f"{performance_time} Return: {returns}")

def ticker_volatility(history, performance_time):
    prices = history["Close"].tolist()
    i = 1
    daily_return_list = []
    while i < len(prices):
        start_price = prices[i-1]
        end_price = prices[i]
        daily_return = ((end_price - start_price)/start_price) 
        daily_return_list.append(daily_return)
        i += 1
    volatility = format_percentage(statistics.stdev(daily_return_list) * math.sqrt(252) * 100)
    return (f"{performance_time} Volatility: {volatility}")

def fifty_twohundred_day_avg(ticker):
    stock = yf.Ticker(ticker)
    one_year_history = stock.history(period="1y")
    prices = one_year_history["Close"].tolist()
    fifty_result = sum(prices[-50:])/len(prices[-50:])
    two_hundred_result = sum(prices[-200:])/len(prices[-200:])
    return (f"50 Day Average: {format_money(fifty_result)}\n"
            f"200 Day Average: {format_money(two_hundred_result)}")

# Run this to see balance sheet rows
#stock = yf.Ticker("AAPL")
#balance_sheet = stock.balance_sheet
#for row in balance_sheet.index:
#    print(row)

# Run this to see income statement columns
#stock = yf.Ticker("AAPL")
#income = stock.income_stmt
#print(income.index)

def ticker_profitability(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    revenue_growth = format_decimal_to_percentage(info.get("revenueGrowth", "N/A"))
    earnings_growth = format_decimal_to_percentage(info.get("earningsGrowth", "N/A"))
    profit_margin = format_decimal_to_percentage(info.get("profitMargins", "N/A"))
    return_on_assets = format_decimal_to_percentage(info.get("returnOnAssets", "N/A"))
    return_on_equity = format_decimal_to_percentage(info.get("returnOnEquity", "N/A"))

    return (f"Revenue Growth: {revenue_growth}\n"
            f"Earnings Growth: {earnings_growth}\n"
            f"Profit Margin: {profit_margin}\n"
            f"Return on Equity: {return_on_equity}\n"
            f"Return on Assets: {return_on_assets}")

def ticker_debt(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    debt_to_equity = format_ratio(info.get("debtToEquity", "N/A"))

    balance_sheet = stock.balance_sheet.loc["Total Debt"].tolist()
    if len(balance_sheet) < 2 or math.isnan(balance_sheet[0]) or math.isnan(balance_sheet[1]):
        return "Not enough data available!"
    else:
        debt_growth = format_percentage(((balance_sheet[0] - balance_sheet[1])/balance_sheet[1]) * 100)

    ebit = stock.income_stmt.loc["EBIT"].tolist()
    interest_expense = stock.income_stmt.loc["Interest Expense"].tolist()
    i = 0
    interest_coverage = "N/A"
    while i < len(ebit):
        if not math.isnan(ebit[i]) and not math.isnan(interest_expense[i]):
            interest_coverage = format_ratio(abs(ebit[i] / interest_expense[i]))
            break
        i += 1

    return (f"Debt-to-Equity: {debt_to_equity}\n"
            f"Debt Growth: {debt_growth}\n"
            f"Interest Coverage: {interest_coverage}")

def ticker_cash(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    free_cash_flow = format_money(info.get("freeCashflow", "N/A"))
    operating_cash_flow = format_money(info.get("operatingCashflow", "N/A"))

    return (f"Free Cash Flow: {free_cash_flow}\n"
            f"Operating Cash Flow: {operating_cash_flow}")

thresholds = {
    "Technology": {"growth_strong": 0.1530*1.10, "growth_moderate": 0.1530*0.90, 
                   "margin_strong": 0.1486*1.10, "margin_moderate": 0.1486*0.90,
                   "fcf_strong": 0.15, "fcf_moderate": 0.08,
                   "debt_strong": 0.1172*0.90, "debt_moderate": 0.1172*1.10,
                   "earnings_growth_strong": 0.1972*1.10, "earnings_growth_moderate": 0.1972*0.90},
    "Healthcare": {"growth_strong": 0.3088*1.10, "growth_moderate": 0.3088*0.90,
                   "margin_strong": 0.0736*1.10, "margin_moderate": 0.0736*0.90,
                   "fcf_strong": 0.10, "fcf_moderate": 0.06,
                   "debt_strong": 0.2418*0.90, "debt_moderate": 0.2418*1.10,
                   "earnings_growth_strong": 0.2049*1.10, "earnings_growth_moderate": 0.2049*0.90},
    "Financial Services": {"growth_strong": 0.0827*1.10, "growth_moderate": 0.0827*0.90,
                           "margin_strong": 0.2031*1.10, "margin_moderate": 0.2031*0.90,
                           "fcf_strong": 0.05, "fcf_moderate": 0.02,
                           "debt_strong": None, "debt_moderate": None,
                           "earnings_growth_strong": 0.1752*1.10, "earnings_growth_moderate": 0.1752*0.90},
    "default": {"growth_strong": 0.1666*1.10, "growth_moderate": 0.1666*0.90,
                "margin_strong": 0.0856*1.10, "margin_moderate": 0.0856*0.90,
                "fcf_strong": 0.08, "fcf_moderate": 0.04,
                "debt_strong": 0.1714*0.90, "debt_moderate": 0.1714*1.10,
                "earnings_growth_strong": 0.1368*1.10, "earnings_growth_moderate": 0.1368*0.90}
}

def rate(value, strong, moderate):
    if strong is None or moderate is None:
        return "N/A (not applicable)"
    if value is None or value == "N/A":
        return "N/A"
    if value >= strong:
        return "✓ Strong"
    elif value >= moderate:
        return "⚠ Moderate"
    else:
        return "✗ Weak"

def rate_lower_is_better(value, strong, moderate):
    if strong is None or moderate is None:
        return "N/A (not applicable)"
    if value is None or value == "N/A":
        return "N/A"
    if value <= strong:
        return "✓ Strong"
    elif value <= moderate:
        return "⚠ Moderate"
    else:
        return "✗ Weak"

def financial_health(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    sector = info.get("sector", "default")
    thresholds_for_sector = thresholds.get(sector, thresholds["default"])

    revenue_growth = info.get("revenueGrowth")
    revenue_growth_rating = rate(revenue_growth, thresholds_for_sector["growth_strong"], thresholds_for_sector["growth_moderate"])

    profit_margin = info.get("profitMargins")
    profit_margin_rating = rate(profit_margin, thresholds_for_sector["margin_strong"], thresholds_for_sector["margin_moderate"])

    free_cash_flow = info.get("freeCashflow")
    total_revenue = info.get("totalRevenue")
    if free_cash_flow is not None and total_revenue is not None:
        free_cash_flow_ratio = free_cash_flow / total_revenue
    else:
        free_cash_flow_ratio = None
    free_cash_flow_rating = rate(free_cash_flow_ratio, thresholds_for_sector["fcf_strong"], thresholds_for_sector["fcf_moderate"])

    total_debt = info.get("totalDebt")
    market_cap = info.get("marketCap")
    if total_debt is not None and market_cap is not None and market_cap != 0:
        debt_levels = total_debt / market_cap
    else:
        debt_levels = None

    debt_levels_rating = rate_lower_is_better(debt_levels, thresholds_for_sector["debt_strong"], thresholds_for_sector["debt_moderate"])

    earnings_growth = info.get("earningsGrowth")
    earnings_growth_rating = rate(earnings_growth, thresholds_for_sector["earnings_growth_strong"], thresholds_for_sector["earnings_growth_moderate"])

    return (f"Financial Health Ratings for {ticker.upper()}:\n"
            f"Revenue Growth:        {revenue_growth_rating}\n" 
            f"Profit Margin:         {profit_margin_rating}\n"
            f"Free Cash Flow:        {free_cash_flow_rating}\n"
            f"Debt Levels:           {debt_levels_rating}\n"
            f"Earnings Growth:       {earnings_growth_rating}")


ticker = input("Enter stock ticker: ").upper()
stock = yf.Ticker(ticker)
info = stock.info
if "displayName" not in info:
    print("Invalid ticker!")
    exit()

print("========================================")
print("         STOCK ANALYSIS TOOL")
print("========================================\n")
print("1. Company Overview")
print("2. Historical Performance")
print("3. Profitability")  
print("4. Financial Health")
print("5. Full analysis")
print("6. Exit")

while True:
    input_choice = input("Please select an option (1-6): ")

    if input_choice == "1":
        print("========================================")
        print("         COMPANY OVERVIEW")
        print("========================================\n")
        print(stock_data(ticker))
    elif input_choice == "2":
        print("========================================")
        print("         HISTORICAL PERFORMANCE")
        print("========================================\n")
        print("1 month")
        print("6 months")
        print("1 year")
        print("5 years")
        performance_time = input(f"Please choose from the options above to generate the historical performance of {ticker.upper()}: ")
        history = get_history(ticker, performance_time)

        if isinstance(history, str):
            print(history)
        else:
            print(ticker_return(history, performance_time))
            print(ticker_volatility(history, performance_time))
            print(fifty_twohundred_day_avg(ticker))
    elif input_choice == "3":
        print("========================================")
        print("         PROFITABILITY")
        print("========================================\n")
        print(ticker_profitability(ticker))
        print("========================================")
        print("         DEBT")
        print("========================================\n")
        print(ticker_debt(ticker))
        print("========================================")
        print("         CASH FLOW")
        print("========================================\n")
        print(ticker_cash(ticker))  
    elif input_choice == "4":
        print("========================================")
        print("         FINANCIAL HEALTH")
        print("========================================\n")
        print(financial_health(ticker))
    elif input_choice == "5":
        print("========================================")
        print("         FULL ANALYSIS")
        print("========================================\n")
        print(stock_data(ticker))
        print("========================================")
        print("         HISTORICAL PERFORMANCE")
        print("========================================\n")
        print("1 month")
        print("6 months")
        print("1 year")
        print("5 years")
        performance_time = input(f"Please choose from the options above to generate the historical performance of {ticker.upper()}: ")
        history = get_history(ticker, performance_time)

        if isinstance(history, str):
            print(history)
        else:
            print(ticker_return(history, performance_time))
            print(ticker_volatility(history, performance_time))
            print(fifty_twohundred_day_avg(ticker))     
        print("========================================")
        print("         FINANCIAL HEALTH")
        print("========================================\n")
        print(financial_health(ticker))
    elif input_choice == "6":
        print("========================================")
        print("         EXITING PROGRAM")
        print("========================================\n")
        break