import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
import warnings

# Suppress warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Set date range for data
end_date = dt.date.today()
start_date = end_date - dt.timedelta(days=500)

# Download stock data
stocks = ["TCS.NS"]
data = yf.download(stocks, start=start_date, end=end_date, interval="1D")
data = np.round(data, 2)

#Finding the lowest value 
Low = data["Low"].min()
Low_date = data["Low"].idxmin()  # Date when the minimum occurs
Low_position = data.index.get_loc(Low_date)

#Lowest Value
a = len(data) - Low_position
b = 1

#Highest value 
High = data["High"].max()
High_date = data["High"].idxmax()
High_position = data.index.get_loc(High_date)

#Higest Value 
c = len(data) - High_position
d = 1 

two_points  = [[(data.index[-a],data["Low"].iloc[-a]),(data.index[-b], data["Low"].iloc[-b])], 
               [(data.index[-c],data["High"].iloc[-c]),(data.index[-d], data["High"].iloc[-d])]]

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 8))

# Plot candlestick chart
mpf.plot(data, type='candle', style='charles', alines = dict(alines = two_points, colors=['g','k']) , volume=False, title='TCS Stock with Trendline')


plt.show()





