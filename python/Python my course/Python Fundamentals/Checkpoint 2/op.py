print("OPERATORS")

print("Arithmetic Operators")
A = 17 ;B = 4
print(f"A={A} B={B}")
print(f"Addition: A+B = {6+5}")
print(f"Subtraction:A-B={A-B} ")
print(f"Multiply:A*B={A*B}")
print(f"Division:A/B={A/B}")
print(f"Floor Division:A//B={A//B}")
print(f"Modulus:A%B={A%B}")
print(f"Power:A**B={A**B}")

print("\n")

print("RELATIONAL OPERATORS")

print(f"A={A},B={B}")
print(f"Equals A==B:{A==B}")
print(f"Not Equals A!=B:{A!=B}")
print(f"A Less Than B A<B:{A<B}")
print(f"A Greater Than B A>B:{A>B}")
print(f"A less than or equals to B A<=B:{A<=B}")
print(f"A is greater than or equals to B A>=B:{A>=B}")

print("\n")

print("ASSIGNMENT OPERATOR")
num1=5; num2=8; result=num1
print("num1=5, num2=8, result=num1")
print("Assign values")
print(f"print the assigned values for the varibales:{num1,num2,result}")
print(f"Swap the values for the variable:")
num1,num2=num2,num1
print(f"After Swaping: num1={num1} and num2={num2}")

print(f"operator assignment:")
#note:it will update the num1  value with new assigned values!!!
num1+=num2 #instead of num1=num1+num2
print(f"+=:{num1}")
num1-=num2
print(f"-=:{num1}")
num1*=num2
print(f"*=:{num1}")
num1/=num2 
print(f"/=:{num1}")
num1%=num2
print(f"%=:{num1}")
num1//=num2
print(f"//=:{num1}")
num1**=num2
print(f"**=:{num1}")
#bitwise assignments
x=5; y=8
print(f"x={x} y={y}")
x&=y #x=x&y
print(f"Bitwise AND & x&y={x}") #same for- or|, XOR^, shifts <<, >>

#logical assignments are not possible: (and=, or=, not=) 

print("\n")

print("LOGICAL OPERATOR")
a,b,c=True, False, True
print(f"The values of:\na= {a}\nb= {b}\nc= {c}")
print("AND OPERATION")
print(f"a and b = {a and b}")
print(f"a and c = {a and c}")
print("OR OPERATION")
print(f"a or b = {a or b}")
print(f"a or c = {a or c}")
print("NOT OPERATION")
print(f"not of a = {not a}")
print(f"not of a and b = {not a and b}")
print(f"not of a or b = {not (a or b)}")

print("\n")

print("BITWISE OPERATORS")
print("It performs the operations on the bit not the values")
print(f"A={A} and B={B}")
print(f"bitwise AND &:{A&B}")
print(f"bitwise OR |:{A|B}")
print(f"bitwise XOR ^:{A^B}")
print(f"bitwise Right shift >>:{A>>B}")
print(f"bitwise Left shift <<:{A<<B}")

print("\n")

""" -------------------------------------------"""

print("OTHER OPERATORS")
#1.Walrus Operator
print("Walrus Operator: :=")
# assigns and checks the expression at a time
a = [1, 2, 3, 4, 5] # a list
print(f"The list of a: {a}")
# walrus operator
while(x := len(a)) > 2:
    a.pop() 
    print(x)

print("\n")

#2.Identity Operator
print("Identity Operator ->is; is not")
a = 10;b = 20;c = a
print(f"The values: a={a},b={b},c={c}")
print(f"a is not b:{a is not b}")
print(f"a is c:{a is c}")

print("\n")

#3.Membership Operator
print("Membership Operator-> in; not in")
list1 = [1, 2, 3, 4, 5]
print(f"The given:\nlist={list1}")
print(f"2 is present in list: {2 in list1}")      # in
print(f"2 is not present in the list: {2 not in list1}")    # not in

print("\n")

#4.Operator.contains() Method
print("operator.contains() Method")
print("#similar to not and not in")
import operator #needs this import
print(operator.contains([1, 2, 3, 4, 5], 2))         # list
print(operator.contains("Hello World", 'O'))         # string
print(operator.contains({1, 2, 3, 4, 5}, 6))         # set
print(operator.contains({1: "Geeks", 2:"for"}, 3))   # dictionary key
print(operator.contains((1, 2, 3, 4, 5), 9))         # tuple

print("\n")

#5.Ternary Operator
print("Ternary Operator")
n = 5
print(f"The value we taken for n={n}")
res = "Even" if n % 2 == 0 else "Odd"
print(res)
#nested if else, else if
n = -5
print(f"The value we taken for n={n}")
res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(res)