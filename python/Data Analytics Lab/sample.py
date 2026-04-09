import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix 
# Sample dataset 
data = { 
'Age': [22, 25, 47, 52, 46, 56, 55, 60, 62, 61], 
'Purchased': [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]  # 1 = Purchased, 0 = Not Purchased 
} 
df = pd.DataFrame(data) 
# Splitting data into training and testing sets 
X = df[['Age']] 
y = df['Purchased'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
# Creating and training the Logistic Regression model 
model = LogisticRegression() 
model.fit(X_train, y_train) 
# Making predictions 
y_pred = model.predict(X_test) 
# Evaluating the model 
accuracy = accuracy_score(y_test, y_pred) 
conf_matrix = confusion_matrix(y_test, y_pred) 
report = classification_report(y_test, y_pred) 
print("Accuracy:", accuracy) 
print("Confusion Matrix:\n", conf_matrix) 
print("Classification Report:\n", report) 
# Plotting decision boundary 
plt.scatter(X, y, color='blue', label='Actual Data') 
x_range = np.linspace(X.min(), X.max(), 100) 
y_prob = model.predict_proba(x_range)[:, 1] 
plt.plot(x_range, y_prob, color='red', linewidth=2, label='Logistic Regression Curve') 
plt.xlabel('Age') 
plt.ylabel('Purchase Probability') 
plt.title('Logistic Regression Model') 
plt.legend() 
plt.show() 