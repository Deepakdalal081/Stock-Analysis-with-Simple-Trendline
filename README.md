# Stock-Analysis-with-Simple-Trendline
The script generates a candlestick chart of TCS.NS stock, highlighting key price levels with trendlines for better data interpretation.


#

![image](https://github.com/user-attachments/assets/460b87f7-7994-45d3-9a02-318c73004277)

#
This Python script demonstrates how to visualize stock data using mplfinance with additional trendline features. The code fetches historical stock data using yfinance, identifies the lowest and highest prices within the dataset, and overlays trendlines on a candlestick chart.
#
**Key Features:**
**1.Data Fetching:**

Retrieves daily stock data for the past 400 days using the Yahoo Finance API via the yfinance library.
Cleans and rounds the data for better readability.

**2.Extrema Identification:**

Identifies the lowest and highest prices from the dataset along with their respective dates.
Calculates their positions relative to the dataset for plotting.

**3.Candlestick Chart with Trendlines:**

Visualizes the stock data as a candlestick chart using mplfinance.

**4.Overlays two trendlines:**
One connecting the lowest price to the most recent price.
Another connecting the highest price to the most recent price.
Trendlines are color-coded for clarity.

**5.Custom Visualization:**

A clear and interactive chart with a professional style and annotations.

Run the script to generate the chart for the stock of your choice.
Modify the stocks list to analyze other stocks.



**This project is an excellent resource for anyone interested in financial data visualization and trend analysis using Python.**
