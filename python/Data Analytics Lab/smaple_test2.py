import numpy as np 
import pandas as pd 
# Sample dataset with redundant features 
data = { 
'Feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
'Feature2': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],  # Perfectly correlated with Feature1 
'Feature3': [5, 3, 6, 9, 2, 8, 7, 4, 1, 10], 
'Feature4': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Linearly dependent on Feature1 
} 
df = pd.DataFrame(data) 
print("Original Data:") 
print(df) 
# Identifying Redundant Features Using Correlation Matrix 
 
 
corr_matrix = df.corr().abs() 
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)) 
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)] 
# Dropping Redundant Features 
df_reduced = df.drop(columns=to_drop) 
print("\nData after Redundant Feature Removal:") 
print(df_reduced) 