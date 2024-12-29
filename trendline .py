import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
import warnings

# Suppress warnings about deprecated or future issues
warnings.filterwarnings("ignore", category=FutureWarning)

# Set the date range for fetching stock data
end_date = dt.date.today()  # Today's date
start_date = end_date - dt.timedelta(days=400)  # 400 days before today

# Download stock data from Yahoo Finance
stocks = ["TCS.NS"]  # List of stocks to download
data = yf.download(stocks, start=start_date, end=end_date, interval="1D")  # Daily data
data = np.round(data, 2)  # Round the data to two decimal places for clarity

# Find the lowest price and its position in the data
Low = data["Low"].min()  # Minimum value in the "Low" column
Low_date = data["Low"].idxmin()  # The date when the lowest value occurred
Low_position = data.index.get_loc(Low_date)  # Position of the lowest value in the DataFrame

# Calculate the relative position for the lowest price
a = len(data) - Low_position  # Days from the end to the lowest point
b = 1  # The most recent day

# Find the highest price and its position in the data
High = data["High"].max()  # Maximum value in the "High" column
High_date = data["High"].idxmax()  # The date when the highest value occurred
High_position = data.index.get_loc(High_date)  # Position of the highest value in the DataFrame

# Calculate the relative position for the highest price
c = len(data) - High_position  # Days from the end to the highest point
d = 1  # The most recent day

# Define the two sets of points for trendlines
# First trendline connects the lowest value to the most recent value
# Second trendline connects the highest value to the most recent value
two_points = [
    [(data.index[-a], data["Low"].iloc[-a]), (data.index[-b], data["Low"].iloc[-b])],
    [(data.index[-c], data["High"].iloc[-c]), (data.index[-d], data["High"].iloc[-d])]
]

# Create a Matplotlib figure and axis for plotting
fig, ax = plt.subplots(figsize=(16, 8))  # Set the figure size

# Plot the candlestick chart with trendlines
mpf.plot(
    data,
    type='candle',  # Candlestick chart type
    style='charles',  # Chart style
    alines=dict(alines=two_points, colors=['g', 'k']),  # Add trendlines with green and black colors
    volume=False,  # Disable volume display
    title='TCS Stock with Trendline'  # Chart title
)

# Show the final plot
plt.show()
