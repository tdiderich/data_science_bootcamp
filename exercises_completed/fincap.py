from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats

# google api access key
key = 'AIzaSyBh9lo7ruqvMWabcJWufswS8E8PpkKvxVs'

# import financial data
BAC = data.DataReader("BAC", 'google', start='2006-01-01', end='2016-01-01')
C = data.DataReader("C", 'google', start='2006-01-01', end='2016-01-01')
GS = data.DataReader("GS", 'google', start='2006-01-01', end='2016-01-01')
JPM = data.DataReader("JPM", 'google', start='2006-01-01', end='2016-01-01')
MS = data.DataReader("MS", 'google', start='2006-01-01', end='2016-01-01')
WFC = data.DataReader("WFC", 'google', start='2006-01-01', end='2016-01-01')

# create list for ticker symbols
tickers = ['BAC','C','GS','JPM','MS','WFC']

# concatenate data frames
frames = [BAC, C, GS, JPM, MS, WFC]
stocks = pd.concat(frames, axis=1, keys=['BAC','C','GS','JPM','MS','WFC'])

# set column names
stocks.columns.names = ['Bank Ticker','Stock Info']

# multi level index practice
grabmax = stocks.xs('Close', axis=1, level=1).max()

# create returns dataframe and add percent changes
returnsDF = pd.DataFrame()
for tick in tickers:
    returnsDF[str(tick) + ' Return'] = stocks[tick]['Close'].pct_change()
returnsDF.dropna(inplace=True)

### visulization with seaborn (verified)
# sns.pairplot(returnsDF)
# plt.show()

### max and min returns
maxvals = returnsDF.idxmax()
minvals = returnsDF.idxmin()
std = returnsDF.std()

### visulization (verified)
# sns.set_style('dark')
# sns.distplot(returnsDF['MS Return'])
# plt.show()

### visualize specific year/company in distplot (verified)
# citi2008 = returnsDF.loc['2008-01-01':'2008-12-31','MS Return']
# sns.distplot(citi2008, bins=100)
# plt.show()

### more viz - timeseries of all 'closing prices' (verified)
# sns.set_style('whitegrid')
# closing_time = stocks.xs('Close', axis=1, level=1)
# plt.plot(closing_time)
# plt.legend(tickers)
# plt.show()

### moving averages (verified)
# BAC_close = stocks.loc['2008-01-01':'2008-12-31','BAC']['Close']
# BAC_rolling_avg = BAC_close.rolling(window=30).mean()
# BAC_rolling_avg.dropna(inplace=True)

# plt.plot(BAC_close)
# plt.plot(BAC_rolling_avg)
# plt.legend(['BAC CLOSE','BAC ROLLING AVG'])
# plt.show()

### heat and cluster maps of close prices (verified)
# close_prices = pd.DataFrame()
# for tick in tickers:
#     close_prices[str(tick) + ' Close'] = stocks[tick]['Close']

# sns.heatmap(close_prices.corr())
# sns.clustermap(close_prices.corr())
# plt.show()
