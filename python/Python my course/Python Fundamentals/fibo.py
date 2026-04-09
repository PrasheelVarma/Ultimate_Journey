# Program to print Fibonacci sequence up to n terms

n_terms = int(input("How many terms? "))

# 1. First two terms
n1, n2 = 0, 1
count = 0

# 2. Check if the number of terms is valid
if n_terms <= 0:
   print("Please enter a positive integer")
elif n_terms == 1:
   print(f"Fibonacci sequence upto {n_terms}:")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n_terms:
       print(n1)
       
       # Logic to update values
       nth = n1 + n2
       n1 = n2
       n2 = nth
       
       count += 1