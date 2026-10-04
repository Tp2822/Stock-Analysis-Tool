Stock Analysis Tool
A stock analysis tool that pulls current stock data from Yahoo Finance and generates a company overview, historical performance, profitability, 
and financial health analysis for a given stock ticker. The tool provides insights into key financial metrics and ratings based 
on industry-specific thresholds.


What the tool does:
Enter a stock ticker (eg AAPL, MSFT, TSLA) and the tool gives you the following options:
1. Company Overview: current price, market cap, P/E ratio, total revenue, earnings per share, dividend yield, 52-week high and low.
2. Historical Performance: returns and volatility over 1 month, 6 months, 1 year, and 5 years, as well as 50-day and 200-day moving 
averages.
3. Profitability: revenue growth, earnings growth, profit margin, return on equity, and return on assets.
4. Financial Health: ratings for revenue growth, profit margin, free cash flow, debt levels, and earnings growth based on industry-
specific thresholds.
5. Full analysis: combines all of the above into a comprehensive report.

Why I built this tool:
I wanted a tool that combined my Economics knowledge with the Python skills I learned during the pre-course work. At university I 
had already done
a project where I did some simple analysis of some pre-given stocks. I wanted to take it a step further and create a tool that could
pull current data from Yahoo Finance and generate a more comprehensive analysis of a given stock ticker. I also wanted to learn how to 
use the yfinance library and  practice my Python skills in a real-world application.

I avoided making this tool suggest stocks to buy or sell because that would require a lot more research and analysis to do properly. 
I also wanted the user to be able to make their own decisions based on the data provided by the tool. 

How it is built:
yfinance library is used to pull current stock data from Yahoo Finance. 
Formatting functions (format_money, format_percentage, format_ratio, format_decimal_to_percentage) are used to format the data so 
that it is easier to read and understand.
A sector-specific thresholds dictionary is used to rate the financial health of the stock based on industry-specific benchmarks from Aswath Damodaran's January 2026 data. A 10% tolerance around the thresholds is used to classify strong, moderate and weak.
The free cash flow thresholds are based on assumptions as the free cash flow measure provided by Yahoo Finance isn't directly equivalent to Damodaran's FCFF measure. 
A menu-driven interface is used to allow the user to select which analysis they want to see. The tool will continue to run until 
the user chooses to exit.

How to use the tool:
1. Install the yfinance library if you haven't already: pip install yfinance
2. Run the script in a Python environment (e.g., terminal, command prompt, or an IDE like PyCharm or VSCode).
3. Enter a valid stock ticker when prompted (e.g., AAPL for Apple, MSFT for Microsoft, TSLA for Tesla).
4. Choose from the menu options to view the company overview, historical performance, profitability, financial health, or a full analysis of the 
stock.

What I'd like to add in the future:
1. Valuation comparison: compare the stock's valuation with its own historical valuation, industry average, and competitors. This 
is done by comparing the stock's P/E ratio, P/B ratio, and other valuation metrics.
2. Competitor comparison: allow the user to input stocks they would like to compare the given stock with. The tool would then 
generate a comparison table with the P/E ratio, revenue growth, profit margin, and other key metrics for each stock. 
3. Create a scoring system: rates the stock based on its growth, profitability, financial health, valuation and momentum. 
4. Analyse the risk of the stock: analyse the risk of the stock based on its volatility, beta, and maximum drawdown.
5. Create graphs: create graphs of the stock's price history, revenue growth, profit margin 
and competitor comparison. 

What I learned from building this tool:
I learned how to use the yfinance library to pull current stock data from Yahoo Finance. I also learned how to format and present the 
data in a user-friendly way. I learned how to handle missing data and errors. I also learned how to use dictionaries and functions 
to rate the financial health of a stock based on industry-specific thresholds. Overall, I learned how to combine my Economics 
knowledge with my Python skills to create a real-world application that provides valuable insights into the stock market.