from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import random

data_iris = load_iris()
target_names = data_iris.target_names  # Fixed variable name and removed print()

print("Sample Data from Iris Dataset")
print("*" * 40)
for i in range(10):
    m = random.randint(0, 149)  # Changed to 149 (iris has 150 samples, 0-149)
    print(data_iris.data[m], "===> ", target_names[data_iris.target[m]])  # Fixed variable name

X = data_iris.data
Y = data_iris.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

print("The Training Data set length is:", len(X_train))  # Fixed syntax
print("The Testing dataset length is:", len(X_test))    # Fixed syntax

try:
    nn = int(input("Enter the number of neighbours: "))
    knn = KNeighborsClassifier(nn)
    knn.fit(X_train, Y_train)
    print("The score is:", knn.score(X_test, Y_test))  # Fixed syntax
    
    test_data = input("Enter the Test Data: ").split(",")
    for i in range(len(test_data)):
        test_data[i] = float(test_data[i])
    
    print()  # Moved inside try block
    v = knn.predict([test_data])
    print("The predicted output is:", target_names[v[0]])  # Fixed variable name and indexing
    
except:
    print("Please supply valid input---")  # Fixed typo