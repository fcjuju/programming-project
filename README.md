# programming-project
Backtest of Overnight strategy and Moving Average Crossover strategy.

In this project, I will implement 2 trading strategies. The first strategy is the Overnight strategy, and the second is the Moving Average Crossover strategy.

Overnight strategy:
Steps of the Overnight strategy:
1. Buy at the close: The trader purchases the selected asset at the close of the trading day.
2. Hold overnight: The trader holds the asset overnight. This is the period when the market is closed and no trading takes place.
3. Sell at the open: At the opening of the next trading day, the trader sells the asset that were held overnight. 

If the price of the asset increased overnight, the trade will be profitable. If the price decreased, the trade will result in a loss.
The hope is that favorable price changes will occur during the overnight holding period (positive overnight gap).

The strategy is based on the observation that stocks often exhibit different behavior during regular trading hours compared to when the market is closed (overnight).
There are a couple of main reasons that explain the rationale of the overnight strategy:
1. Earning Announcements and News Events: Major announcements, such as earnings reports, regulatory decisions, interest rate hikes, or other significant news, often occur when markets are closed. If the news is positive, it could lead to a higher opening price the next day, whereas negative news can cause a gap down at the opening.
2. Reduced Trading Volume: During the overnight period, trading volume is generally lower. This means less liquidity, which can lead to more price volatility. With the right risk management, investors can take advantage of this higher volatility for profit.
3. Geopolitical Events: Events in different time zones can impact stock prices. For example, decisions by foreign governments or economic events like the release of economic indicators can affect domestic markets, causing price changes overnight.
4. Futures and Foreign Markets Activity: The activity in futures markets and foreign stock markets, which often operate at different hours than the domestic stock market, can impact the prices of domestic stocks.



Moving Average Crossover strategy:
Steps of the MA crossover strategy:
1. Select the Time Frames: The trader chooses two different time frames for the moving averages; a "fast" moving average (shorter term) and a "slow" moving average (longer term).
2. Identify the Crossover: The trader identifies when the fast moving average crosses the slow moving average. A crossover is the signal to either buy or sell.
3. Enter the Trade: Upon a bullish crossover (the fast MA crosses above the slow MA), the trader would enter a long position. Conversely, upon a bearish crossover (the fast MA crosses below the slow MA), the trader would enter a short position.
4. Exit the Trade: The trader typically exits the trade when the opposite crossover happens. That is, if he bought on a bullish crossover, he would sell when a bearish crossover happens, and vice versa.

The strategy is based on the observation that Moving Averages smooth out price data to form a single flowing line, making it much easier to spot trends. A rising moving average generally indicates an uptrend, while a falling moving average indicates a downtrend.
Here's the rationale of the MA crossover strategy:

Trend Identification: 

Signal Generation: When the fast moving average crosses above the slow moving average, it generates a bullish (buy) signal, indicating that the short-term trend is moving higher than the long-term trend and could continue. When the fast moving average crosses below the slow moving average, it generates a bearish (sell) signal, indicating that the short-term trend is moving lower than the long-term trend and could continue.


