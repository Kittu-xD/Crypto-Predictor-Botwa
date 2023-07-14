import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression

# Load data from CSV
data = pd.read_csv('crypto_data.csv')

# Convert date string to datetime object
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

# Create a linear regression model
model = LinearRegression()

# Prepare the training data
X = data['Date'].apply(lambda x: x.toordinal()).values.reshape(-1, 1)
y = data['Price'].values.reshape(-1, 1)

# Train the model
model.fit(X, y)

# Predict the price for a given date
date_str = input("Enter the future date(ex: 09-01-2024): ")
date = datetime.strptime(date_str, '%d-%m-%Y')
ordinal_date = date.toordinal()
predicted_price = model.predict([[ordinal_date]])

print(f'Predicted price for {date_str}: {predicted_price[0][0]}')
