"This program shows PRINT() statements with QUOTES and escape characters"
'''Also with comments in
        multi lines 
        #and '''
        # single line comment        
"Anything inside double quotes or single quotes is considered as a string in Python"

print("YES it's working!") #standard print statement that uses double quotes
print('YES it\'s working!') #standard print statement that uses single quotes and escape character
print('print (I\'m Python!)') #better use double quotes to avoid escape character else we need to use this

#Escpape characters will treat the next character differently or skip its normal function

print("Hello\'oo") #(\') to print single quote along with the string
print("Hello\"oo") #(\") to print double quote along with the string
print("Hello\\oo") #(\\) to print backslash along with the string
print("Hello\nWorld") #new line
print("Hello\tWorld") #tab space
print("Hello\bWorld") #backspace (removes the previous character)

#different ways of printing statements
print("Hello" + " Computer " + "World" ) #concatenation of strings using + operator
print("Hello" 'world' "!!!" '''quotes''') #printing multiple strings using quotes 
print("Hello", "World", "replace + with ,", "To print multiple strings as separate arguments" ) #printing multiple strings with comma
print("Hello " * 3) #printing string multiple times
print("Hello" + " " * 5, "World" "nothing") #printing spaces between strings using multiplication #and also shows (+ "" ,) usage
print("Hello\n" * 3) #printing new line multiple times (\t, \b, \\ can also be used similarly)

#OPTIMAL way to print variables and strings together
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.") #using f-strings (Python 3.6+) #auto space
print("My name is ", name, " and I'm ", age, "years old.") #using comma to separate variables and strings #manual space
print("my name is " + name + " and I'm " + str(age) ) #using + operator to concatenate strings and variables (type casting needed for non-strings) #not optimal
print("My name is {} and I am {} years old.".format(name, age)) #using format() method #auto space but not optimal