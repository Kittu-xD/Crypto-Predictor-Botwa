import yfinance as yf
import pandas as pd

# Download Bitcoin historical data from Yahoo Finance
btc = yf.download('BTC-USD', start='2010-01-01')

# Select only the Date and Close columns
btc = btc[['Close']]

# Rename the Close column to Price
btc.rename(columns={'Close': 'Price'}, inplace=True)

# Add a Date column with the date index converted to a string
btc['Date'] = btc.index.strftime('%Y-%m-%d')

# Save the Bitcoin data to a CSV file
btc.to_csv('bitcoin_data.csv', index=False)

print('Bitcoin data saved to bitcoin_data.csv')
