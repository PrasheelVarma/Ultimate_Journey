# --- THE "INTERNING" & IDENTITY MASTERY LAB ---

# 1. SMALL INTEGERS (-5 to 256)
# These are cached (Integer Caching). 
x = 256
y = 256
print(f"Int 256: x is y? {x is y}") # True

# LARGE INTEGERS (Outside the cache)
x = 257
y = 257
print(f"Int 257: x is y? {x is y}") # False (New object created for each)

# 2. STRINGS (Interning)
# Term: "Interning" - Reusing string objects for speed.
s1 = "Python"
s2 = "Python"
print(f"\nSimple String: s1 is s2? {s1 is s2}") # True

s3 = "Python 3.12!" # Contains space and symbol
s4 = "Python 3.12!"
print(f"Complex String: s3 is s4? {s3 is s4}") # False (Usually not interned)

# 3. FLOATS (Never Interned)
f1 = 1.0
f2 = 1.0
print(f"\nFloats: f1 is f2? {f1 is f2}") # False (Always separate objects)

# 4. BOOLEANS & NONE (Singletons)
# There is only ONE 'True', ONE 'False', and ONE 'None' in Python's memory.
# These will ALWAYS return True for 'is'.
a = True
b = True
print(f"\nBooleans: a is b? {a is b}") # True

n1 = None
n2 = None
print(f"None Type: n1 is n2? {n1 is n2}") # True

# 5. COLLECTIONS (Lists, Dicts, Sets)
# Even if empty or identical, they are ALWAYS new boxes.
list_a = []
list_b = []
print(f"\nEmpty Lists: list_a is list_b? {list_a is list_b}") # False