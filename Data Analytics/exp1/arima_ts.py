import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from statsmodels.tsa.arima.model import ARIMA 
from sklearn.metrics import mean_squared_error 
# Generating sample time series data 
date_rng = pd.date_range(start='1/1/2020', periods=24, freq='M') 
data = {'Date': date_rng, 'Sales': [200, 220, 250, 270, 300, 320, 310, 290, 330, 360, 390, 410, 450, 
470, 490, 520, 550, 580, 600, 620, 650, 670, 690, 710]} 
df = pd.DataFrame(data) 
df.set_index('Date', inplace=True) 
# Splitting data into training and testing sets 
train_size = int(len(df) * 0.8) 
train, test = df[:train_size], df[train_size:] 
# Building and fitting the ARIMA model 
model = ARIMA(train, order=(2, 1, 2))  # (p, d, q) values chosen arbitrarily 
model_fit = model.fit() 
# Making predictions 
predictions = model_fit.forecast(steps=len(test)) 
# Evaluating the model 
mse = mean_squared_error(test, predictions) 
print("Mean Squared Error:", mse) 
# Plotting the results 
plt.figure(figsize=(10, 5)) 
plt.plot(train, label='Training Data') 
plt.plot(test, label='Actual Sales', color='blue') 
plt.plot(test.index, predictions, label='Predicted Sales', color='red', linestyle='dashed') 
plt.xlabel('Date') 
plt.ylabel('Sales') 
plt.title('ARIMA Time Series Forecasting') 
plt.legend() 
plt.show()