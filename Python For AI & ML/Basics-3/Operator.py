# ############ Operators in Python ############

# Operators are special symbols in Python that carry out 
# operations on operands (values or data).
# They are used to perform various mathematical, logical,
# and comparison operations.
# Here are some common types of operators in Python:

# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Logical Operators
# 4. Assignment and Compound Operators
# 5. Bitwise Operators
# 6. Ternary Operator

# Special Operators in Python:
# 1. Identity Operators: 'is' and 'is not'
# 2. Membership Operators: 'in' and 'not in'
# 3. Walrus Operator: ':='


# 1. Arithmetic Operators
# Used to perform arithmetic operations on two or more operands.
# Below are some common arithmetic operators:
# a. Addition (+)
a = 10
b = 5
sum_result = a + b  # 10 + 5 = 15
print("Addition:", sum_result)
# b. Subtraction (-)
sub_result = a - b  # 10 - 5 = 5
print("Subtraction:", sub_result)
# c. Multiplication (*)
mul_result = a * b  # 10 * 5 = 50
print("Multiplication:", mul_result)
# d. Division (/)
div_result = a / b  # 10 / 5 = 2.0  
# Note: Division always returns a float
print("Division:", div_result)
# e. Floor Division (//)
floor_div_result = a // b  # 10 // 5 = 2
print("Floor Division:", floor_div_result)
float_floor_div_result = 10.5 // 2  # 10.5 // 2 = 5.0
print("Float Floor Division:", float_floor_div_result)
negative_floor_div_result = -10 // 3  # -10 // 3 = -4
print("Negative Floor Division:", negative_floor_div_result)
# Note: Floor division rounds down to the nearest whole number.
# For positive numbers, it behaves like regular division followed by truncation.
# For negative numbers, it rounds down to the next lower integer.
# f. Modulus (%)
mod_result = a % b  # 10 % 5 = 0
print("Modulus:", mod_result)
# g. Exponentiation (**)
exp_result = a ** b  # 10 ** 5 = 100000
print("Exponentiation:", exp_result)
# Output:
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0
# Floor Division: 2
# Modulus: 0
# Exponentiation: 100000

# Note : If any Operand is of type float, the result will be of type float.
# 2. Comparison Operators
# Used to compare two values and return a boolean result (True or False).
# Common comparison operators include:
# a. greater than (>)
x = 10
y = 5
greater_than_result = x > y  # 10 > 5 = True
print("Greater than:", greater_than_result)
# b. less than (<)
less_than_result = x < y  # 10 < 5 = False
print("Less than:", less_than_result)
# c. equal to (==)
equal_to_result = x == y  # 10 == 5 = False
print("Equal to:", equal_to_result)
# d. not equal to (!=)
not_equal_to_result = x != y  # 10 != 5 = True
print("Not equal to:", not_equal_to_result)
# e. greater than or equal to (>=)
greater_equal_to_result = x >= y  # 10 >= 5 = True
print("Greater than or equal to:", greater_equal_to_result)
# f. less than or equal to (<=)
less_equal_to_result = x <= y  # 10 <= 5 = False
print("Less than or equal to:", less_equal_to_result)

# 3. Assignment and Compound Operators
# Used to assign values to variables and perform operations in a concise way.
# a. Assignment (=)
c = 10
print("Assignment:", c)
# b. Compound Assignment Operators
# These operators combine an arithmetic operation with assignment.
# i. Addition Assignment (+=)
c += 5  # Equivalent to c = c + 5
print("Addition Assignment:", c)
# ii. Subtraction Assignment (-=)
c -= 3  # Equivalent to c = c - 3
print("Subtraction Assignment:", c)
# iii. Multiplication Assignment (*=)
c *= 2  # Equivalent to c = c * 2
print("Multiplication Assignment:", c)
# iv. Division Assignment (/=)
c /= 4  # Equivalent to c = c / 4
print("Division Assignment:", c)
# v. Floor Division Assignment (//=)
c //= 2  # Equivalent to c = c // 2
print("Floor Division Assignment:", c)
# vi. Modulus Assignment (%=)
c %= 3  # Equivalent to c = c % 3
print("Modulus Assignment:", c)
# vii. Exponentiation Assignment (**=)
c **= 2  # Equivalent to c = c ** 2
print("Exponentiation Assignment:", c)


# Special Operators in Python:
#