# Write your code for Project 1 here!
# 1. Take the Name input
name=input("Type your name: ")

# 2. Take the Birth Year input (and convert to int)
birth_year=(input("Enter your Year of birth: "))
birth_year=int(birth_year)
year=int(input("Enter the Year to know your age at that year "))
# 3. Calculate Age
age=year-birth_year
# 4. Print the final message using an F-string
print(f"Hello {name}")
print(f"Age at the year you selected {year} is: {age} ")