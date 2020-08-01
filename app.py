import requests
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import data

style.use('dark_background')

start_date = dt.datetime(2016, 1, 1)
end_date = dt.datetime.now()

# Retrieve historical stock prices, save to csv, read csv file and plot closing prices
df = web.DataReader('TSLA', 'yahoo', start_date, end_date)
df.to_csv('TSLA.csv')
df = pd.read_csv('tsla.csv', parse_dates=False, index_col=0)
df['Close'].plot()

# Moving averages. 20 day for short term momentum, 100 day for longer term trend
df['SMA20'] = df['Close'].rolling(window=20).mean()
df['SMA100'] = df['Close'].rolling(window=100).mean()

plt.plot(df['SMA20'], 'r--', label='SMA20')
plt.plot(df['SMA100'], 'y--', label='SMA100')
plt.legend()

# Labels and title for the plotted graph
plt.xlabel('DATE')
plt.ylabel('Price $')
plt.title('Tesla Stock Price')
plt.show()
