import pandas as pd
import numpy as np

# Sample dataset
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, np.nan, np.nan, 4, 5]
}
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1.
df_dropped = df.dropna()
print("\nData after dropping rows with missing values:")
print(df_dropped)

# 2. 
df_filled_mean = df.fillna(df.mean())
print("\nData after filling missing values with mean:")
print(df_filled_mean)

# 3. 
df_filled_median = df.fillna(df.median())
print("\nData after filling missing values with median:")
print(df_filled_median)

# 4. 
df_ffill = df.ffill() #df_ffill=df.fillna(method='ffill')
print("\nData after forward fill:")
print(df_ffill)

# 5. 
df_bfill = df.bfill() #df_bfill=df.fillna(method='bfill')
print("\nData after backward fill:") 
print(df_bfill)

# 6. Interpolating missing values
df_interpolated = df.interpolate()
print("\nData after interpolation:")
print(df_interpolated)