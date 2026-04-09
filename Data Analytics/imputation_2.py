import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer


data = {
    'Feature1': [1, 2, np.nan, 4, 5, 6, np.nan, 8, 9, 10],
    'Feature2': [2, 4, 6, 8, np.nan, 12, 14, 16, 18, 20],
    'Feature3': [5, 3, 6, 9, 2, np.nan, 7, 4, 1, 10]
}
df = pd.DataFrame(data)

print("Original Data with Missing Values:")
print(df)

imputer = KNNImputer(n_neighbors=2)
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("\nData after KNN Imputation:")
print(df_imputed)