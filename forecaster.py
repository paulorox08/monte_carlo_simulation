import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Get the data set
df = pd.read_csv('VOO.csv', parse_dates=True, index_col='Date')

# Show the data
df

### Simulate future paths ###
# Simulation parameters
num_simulations = 10
forecast_days = 365