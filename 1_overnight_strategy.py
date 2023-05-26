# 1st strategy: Overnight strategy
# We buy at the end of each day, and sell at the beginning of each following day.

# Import needed libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# User inputs the asset ticker (and keep it in uppercase, to use it in plot title)
ticker = input("Enter the ticker symbol: ").upper()

# User inputs the trading fee percentage, representative of transaction costs
trading_fee_percentage = float(input("Enter the trading fee percentage (e.g., 0.1 for 0.1%): ")) / 100

# Download historical market data (here we can change start and end dates)
start_date = "1993-01-01"
end_date = "2021-05-01"
hist = yf.download(ticker, start=start_date, end=end_date)


# Calculate the trading fees to buy and sell the asset (add a column in 'hist' dataframe)
buying_fee = trading_fee_percentage * hist['Close']
selling_fee = trading_fee_percentage * hist['Open'].shift(-1)

# Overnight strategy: buy at the closing price, sell at the opening price the next day, and subtract the transaction costs
hist['Overnight_Returns'] = ((hist['Open'].shift(-1) - selling_fee) - (hist['Close']) + buying_fee) / (hist['Close'] + buying_fee)

# Calculate cumulative returns of the Overnight strategy
hist['Cumulative_Returns'] = (1 + hist['Overnight_Returns']).cumprod() - 1

# To compare if it is worthy to sell the asset each morning before buying it back each evening rather than just keep the asset:
# Buy and hold strategy: buy at the first closing price, sell at the last closing price (taking into account trading fees)
initial_price = hist['Close'].iloc[0] * (1 + trading_fee_percentage)
hist['Buy_And_Hold_Returns'] = (hist['Close'] - initial_price) / initial_price
# Subtract selling fee on the last day performance (the day we sell)
hist['Buy_And_Hold_Returns'].iloc[-1] -= trading_fee_percentage * hist['Close'].iloc[-1] 


# Plot the Overnight cumulative returns and Buy-and-Hold returns (starting at 1)
plt.figure(figsize=(10,5))
plt.plot(1 + hist['Cumulative_Returns'], label='Overnight Strategy')
plt.plot(1 + hist['Buy_And_Hold_Returns'], label='Buy-and-Hold Strategy', color='gray', alpha=0.5)

plt.title(f'Overnight vs Buy-and-Hold Returns for {ticker}')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend(loc='best')
plt.grid()
plt.show()
