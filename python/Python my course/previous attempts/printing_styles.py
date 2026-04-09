# --- 1. The F-string (Formatted String Literal) ---
# This is the modern, recommended way. It's the most powerful and readable.
name = "Alice"
age = 30
print(f"1. F-string: Hello, {name}. You are {age} years old.")
print(f"1. F-string with formatting: Pi is approximately {3.14159:.2f}")
print("---")

# --- 2. Comma-Separated Arguments ---
# This is simple and great for basic prints. It automatically adds spaces.
product = "Laptop"
price = 1200
print("2. Comma-separated:", product, "costs", price, "dollars.")
print("---")

# --- 3. The .format() Method ---
# This is a slightly older but still very common method.
city = "New York"
temp = 25
print("3. .format() method: The temperature in {} is {} degrees Celsius.".format(city, temp))
print("---")

# --- 4. String Concatenation (+) ---
# This is generally not recommended for complex outputs as it requires
# you to manually convert non-string types using str().
language = "Python"
version = 3.9
print("4. Concatenation: My favorite language is " + language + " and its version is " + str(version) + ".")
print("---")

# --- 5. The Old-Style % Operator ---
# This is a legacy method from Python 2. It is not used in new code but is
# important to recognize when reading older programs.
# %s is for strings, %d is for integers, %f is for floats.
# NOTE: To print a literal '%' sign, you must escape it with another '%'.
day = "Monday"
percent_complete = 75.5

print("5. Old-style percentile %% operator: Today is %s and we are %.1f%% complete." % (day, percent_complete))
print("-" * 20)
