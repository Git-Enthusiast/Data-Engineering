# How memory is allocated for variables in Python
a = 10
b = 10
c = 10
print(f"Memory address of a: {id(a)}")
print(f"Memory address of b: {id(b)}")
print(f"Memory address of c: {id(c)}")

# Changing the value of a variable does not affect other 
# variables even if they initially had the same value
a = 20
print(f"Value of b: {b}")
print(f"Value of c: {c}")

print(f"Memory address of a: {id(a)}")



# Creating Multiple Variables in One Line
x, y, z = 1, 2, 3
print(f"x: {x}, y: {y}, z: {z}")

# Also u can write multiple print statements in one line
print (f"x: {x}")
print (f"y: {y}")
print (f"z: {z}")

# Assigning the same value to multiple variables
m = n = p = 50
print(f"m: {m}, n: {n}, p: {p}")

# Variable Naming Conventions
# Valid variable names
valid_name = 100
_validName = 200
validName123 = 300
print(f"valid_name: {valid_name}, _validName: {_validName}, validName123: {validName123}")

# Invalid variable names (uncommenting these will raise errors)
# 1name = 400
# name-with-hyphen = 500
# name with space = 600
# name@domain = 700
# Note: Variable names cannot start with a number, cannot contain 
# hyphens or spaces, and cannot include special characters like '@'.


# Vaiables in Python are case-sensitive
var = 10
Var = 20
print(f"var: {var}, Var: {Var}")
