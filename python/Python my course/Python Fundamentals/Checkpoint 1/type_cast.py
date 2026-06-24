#data types and type casting is done here
s= "10"  
n = int(s) 
num = 5
f = float(num)  
age = 25
s2 = str(age)  

print(n)  
print(f)  
print(s2)

k = 42
l = 3.14
a = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool_var = True

print(type(k))   
print(type(l)) 
print(type(a))   
print(type(li))     
print(type(d))     
print(type(bool_var))

#Taking input from user as integer
a=int(input("Enter a number, this default string number is converted to integer from the user input (type the number): "))
print(f"The integer a->{a}") #inline type casting
#Try removing that int before the (input) to see how it works!
b=input("Enter a number: ")
b=int(b) #after the user input the variable is type casted to make the string to integer
print(f"The number entered is {b}")
