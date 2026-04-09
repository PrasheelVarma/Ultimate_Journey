# =================================================================
# 🏁 CHECKPOINT 1: THE BASICS MASTERY LAB
# Goal: Complete all 5 challenges to prove you've mastered Topic 1-7.
# =================================================================

# --- CHALLENGE 1: The Identity Setup ---
# 1. Ask for a user's First Name and Last Name separately.
# 2. Use a String Method (like .title()) to make sure they are professional.
first_name=input("Your First Name: ").strip().title()
last_name=input("Your Last Name: ").strip().title()

# 3. Create a variable called 'full_name' by joining them.
full_name=(f"{first_name} {last_name}") 
print(f"{full_name}")
# 4. TRAP: Do NOT use the '+' operator. Use an F-String.
print(f"Full Name: {first_name} {last_name}")

# --- CHALLENGE 2: The Data DNA ---
# 1. Ask the user: "How many hours do you study Python daily?"
# 2. Convert this input to a FLOAT (directly on the same line).
q1=float(input("How many hours do you learn Python daily?"))
# 3. Print the value and its data type using the type() function.
# 4. Use an F-string for this output.
print(f"you spend daily {q1} hours ")
print(f"The data type of user input: {type(q1)}")



# --- CHALLENGE 3: The Conversion & Memory Test ---
# 1. Create a variable 'pi_string' and set it to "3.14159".
PI_STRING="3.14159" 
print(f"Output 1 ={PI_STRING} type={type(PI_STRING)}")
# 2. Convert it to a float, then convert that float to an integer (Permanent change).
PI_STRING=float(PI_STRING)
print(f"Output 2 ={PI_STRING} type={type(PI_STRING)}")
PI_STRING=int(PI_STRING)
# 3. Print the final integer value.
print(f"Output 3 = {PI_STRING} type={type(PI_STRING)}")

# 4. Print the Memory Address (ID) of that final integer.
print(f"Memory Address: {id(PI_STRING)}")

# --- CHALLENGE 4: The Escape Artist ---
# 1. Use a single print() function to display the following EXACTLY:
#    Line 1: My "Python" Journey
#    Line 2: (Tab space) Starts \Now/
# 2. Note: You must use \n, \t, and \" to achieve this.
print(f"Line 1: My \"Python\" Journey \nLine 2:\tStarts \\Now/")


# --- CHALLENGE 5: The "Empty" Trap ---
# 1. Create a variable called 'nothing' and assign it the None type.
nothing=None
# 2. Print: "Is there anything here? [nothing]".
print(f"is there anything here {nothing} \tThe type is: {type(nothing)}")
# 3. Take a dummy input: user_press = input("Just press Enter: ")
user_press=input("Just press enter: ")
# 4. Print the type of 'user_press' to prove it's NOT None.
print(f"type of user press: {type(user_press)}")


