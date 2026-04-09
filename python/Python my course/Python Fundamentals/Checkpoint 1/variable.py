#Variable = it's like a container that have a name used to store the values or data.

variable_name = "data or value"
print(variable_name)
print(len(variable_name))  # prints the length of the string stored in variable_name

length_of_variable = len(variable_name) # storing length in another variable
print(length_of_variable) # printing the length stored in length_of_variable

print(type(variable_name)) # prints the type of the variable
print(id(variable_name)) # prints the unique id of the variable in memory
print(variable_name.upper()) # prints the string in uppercase ->similar methods: lower(), title(), capitalize()

#same variable using multiple times with different values (updating variable values)
x=5
print(x)
y="some name"
print(y)
x=80
print(x)
print(x,y,x) 
y=y+" updated"
print(y)
print(f"The updated values of x: {x-6}") #using f-strings to print updated value of x
print("The updated values of x and y:",x+30, y+" yes") #using comma to print updated value of x and y
print(f"The updated values of x and y are:{x+40} and {y+'!!!'}") #using f-strings to print both updated values

#variable with multiple values and strings
hello="Hello","hey",23,60.5,True #tuple_var
print(hello)
print(hello[2]) #accessing third value from the variable

#multiple variables in single line
a,b,c=10,"name",50.5 #assigning different values
print(a,b,c)
#swapping variables
a,b,c=b,c,a
print("After swapping:")
print(a,b,c)    

d = e = f = 100, "shared", 99.9 #assign same values
print(d, e, f) 




    



