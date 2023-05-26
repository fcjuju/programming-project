import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the stock you want to study by provinding the corresponding ticker (and translate it into uppercase for for the aesthetics of the graphs)
ticker = input("Enter the ticker symbol: ").upper()

# Define short and long Moving Average length (eg. 50-200 MAs crossing, also known as the Golden cross)
short_ma_length = 50
long_ma_length = 200

# Define the start and end dates
start_date = "2016-01-01"
end_date = "2023-12-31"

# Calculate the new start date for the data download, which is the long_ma_length trading days before the desired start date
# It allows us to already be in position on the start date chosen above
start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
new_start_date_dt = start_date_dt - timedelta(days=long_ma_length*7/5 + 10) # Multiply by 7/5 to account for weekends, + 10 to be sure to have enough data due to possible free days
new_start_date_dt = new_start_date_dt.strftime("%Y-%m-%d")

# Download historical data
data = yf.download(ticker, start=new_start_date_dt, end=end_date)

# Calculate short and long-term MAs
data['Short_MA'] = data['Close'].rolling(window=short_ma_length).mean()
data['Long_MA'] = data['Close'].rolling(window=long_ma_length).mean()

# Create a column 'Position' such that if the Short_MA is greater than Long_MA then position is 1 else it is -1
data['Position'] = np.where(data['Short_MA'] > data['Long_MA'], 1, -1)

# Calculate changes in position 
# Needed to print buy and sell signals on the first graph, and in case we want to take transaction cost into account (neglected here)
data['Position_Change'] = data['Position'].diff()

# Calculate daily returns
data['Market_Returns'] = data['Close'].pct_change()
data['Strategy_Returns'] = data['Market_Returns'] * data['Position'].shift()

# Remove the additional dates that we don't need
data = data.loc[start_date:]

# Calculate cumulative returns (Buy & Hold + Moving Average Crossover strategies to compare them on the second graph)
data['Cumulative_Market_Returns'] = (1 + data['Market_Returns']).cumprod() - 1
data['Cumulative_Strategy_Returns'] = (1 + data['Strategy_Returns']).cumprod() - 1

# Create a plot space to add two different graphs
plt.figure(figsize=(20,10))

# 1st graph: Plot the asset closing price, short-term MA, long-term MA, buy and sell signals
plt.subplot(2, 1, 1)
plt.plot(data['Close'], label=ticker, color='blue', alpha=0.35)
plt.plot(data['Short_MA'], label=f'{short_ma_length}-day MA', color='red', alpha=0.35)
plt.plot(data['Long_MA'], label=f'{long_ma_length}-day MA', color='green', alpha=0.35)
plt.plot(data[data['Position_Change'] == 2].index, data['Short_MA'][data['Position_Change'] == 2], '^' , markersize=5, color='m')
plt.plot(data[data['Position_Change'] == -2].index, data['Short_MA'][data['Position_Change'] == -2], 'v' , markersize=5, color='k')
plt.title(f"{ticker} - {short_ma_length}/{long_ma_length} Moving Average Crossover")
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()

# 2nd graph: Plot the cumulative returns of both Buy & Hold + Moving Average Crossover strategies to compare them, starting at 1)
plt.subplot(2, 1, 2)
plt.plot(1 + data['Cumulative_Market_Returns'], label='Market Returns', color='blue')
plt.plot(1 + data['Cumulative_Strategy_Returns'], label='Strategy Returns', color='cyan')
plt.title(f"{ticker} - {short_ma_length}/{long_ma_length} Moving Average Crossover Strategy vs. Buy and Hold")
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid()

# Print the two graph together, without overlap
plt.tight_layout()
plt.show()

