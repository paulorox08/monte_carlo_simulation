import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Get the data set
df = pd.read_csv('VOO.csv', parse_dates=True, index_col='Date')

# Show the data
df

### Simulate future paths ###
# Simulation parameters
num_simulations = 100
forecast_days = 365

# Initialise simulation array with all zeros
simulations = np.zeros((num_simulations, forecast_days))

# Get the last adjusted close price
last_price = df['Close'].iloc[-1]

# Calculate the daily returns and drop and remove any NA values
daily_returns = df['Close'].pct_change().dropna()

# Loop through the number of simulatiosn to forecast future cumulative returns for this asset (VOO)
for i in range(num_simulations):
    # Get random dauly returns of size forecast days and return its cumulative return
    # Return an array of size forecast_days that contains randomly selected daily returns and calculate that cumulative return
    cumulative_returns = np.random.choice(daily_returns, size=forecast_days, replace=True).cumsum()
    # Get the number of simulations with the random cumulative returns
    simulations[i, :] = last_price * (1 + cumulative_returns)

#print(simulations)

# For simulation '3' show the first 4 random cumulative returns out of the 365 random cumulative returns starting from index 0 up to but not including 4
print(simulations[2, 0:4])

#Plot the results
plt.figure(figsize=(10,6))
for i in range(num_simulations):
    plt.plot(simulations[i], alpha=0.25)
plt.title('Monte Carlo Simulation of Future Prices')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()