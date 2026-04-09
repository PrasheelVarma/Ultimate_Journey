import numpy as np
import pandas as pd
from scipy import stats
from sklearn.impute import SimpleImputer

data = {
    'Sensor1': [10, 12, 13, 500, 15, 14, 11, 10, 9, 300], 
    'Sensor2': [20, 21, 19, 22, np.nan, 23, 200, 22, 21, 24], 
    'Sensor3': [30, 31, 29, 32, 30, 28, 33, 500, 30, 29] 
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

z_scores = np.abs(stats.zscore(df_imputed))
df_no_outliers = df_imputed[(z_scores < 3).all(axis=1)]

Q1 = df_imputed.quantile(0.25)
Q3 = df_imputed.quantile(0.75)
IQR = Q3 - Q1

filtered_df = df_imputed[~((df_imputed < (Q1 - 1.5 * IQR)) | (df_imputed > (Q3 + 1.5 * IQR))).any(axis=1)]

def moving_average(series, window_size=3):
    return series.rolling(window=window_size, min_periods=1).mean() 

df_smoothed = filtered_df.apply(moving_average)
print("\nCleaned and Smoothed Data:")
print(df_smoothed)