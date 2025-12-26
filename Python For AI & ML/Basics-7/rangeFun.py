"""
====================================================================
                RANGE() IN PYTHON 
====================================================================

This file explains:
1. What is range()
2. Syntax of range()
3. range(stop), range(start, stop), range(start, stop, step)
4. Iterating using range
5. Negative step
6. float step limitation
7. Common mistakes and errors
8. Real-world examples

Python Version: Python 3.x
====================================================================
"""

# ================================================================
# 1. WHAT IS range()?
# ================================================================

"""
range() generates a sequence of numbers.
- Immutable sequence
- Used commonly in for loops
- Does NOT store all numbers in memory (lazy evaluation)
"""

# ================================================================
# 2. BASIC SYNTAX
# ================================================================

"""
range(stop)                 → 0 to stop-1
range(start, stop)           → start to stop-1
range(start, stop, step)    → start to stop-1 with step increment
"""

# ================================================================
# 3. range(stop)
# ================================================================

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Why:
# start defaults to 0
# stop = 5 → last value = 4


# ================================================================
# 4. range(start, stop)
# ================================================================

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# Why:
# start = 1, stop = 6 → last value = 5


# ================================================================
# 5. range(start, stop, step)
# ================================================================

for i in range(1, 10, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9

# Why:
# step = 2 → increments by 2 each iteration


for i in range(10, 0, -2):
    print(i)

# Output:
# 10
# 8
# 6
# 4
# 2

# Why:
# Negative step → loop runs in reverse


# ================================================================
# 6. CONVERT range TO LIST
# ================================================================

numbers = list(range(1, 6))
print(numbers)

# Output:
# [1, 2, 3, 4, 5]

# Why:
# list() converts range object into a list


# ================================================================
# 7. range WITH for LOOP
# ================================================================

for i in range(3):
    print("Iteration:", i)

# Output:
# Iteration: 0
# Iteration: 1
# Iteration: 2


# ================================================================
# 8. range WITH len()
# ================================================================

fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, fruits[i])

# Output:
# 0 apple
# 1 banana
# 2 cherry


# ================================================================
# 9. COMMON MISTAKES
# ================================================================

# ❌ Using float in range
# for i in range(1, 5.5):
#     print(i)

"""
Error:
TypeError: 'float' object cannot be interpreted as an integer

Why:
- range() requires integer arguments
- Cannot pass float directly
"""

# ❌ step = 0
# for i in range(1, 5, 0):
#     print(i)

"""
Error:
ValueError: range() arg 3 must not be zero

Why:
- step cannot be zero → infinite loop
"""


# ❌ start > stop with positive step
for i in range(5, 1, 2):
    print(i)

# Output:
# (Nothing printed)
# Why:
# Condition already False at start → loop skipped


# ================================================================
# 10. RANGE WITH NEGATIVE STEP
# ================================================================

for i in range(5, 0, -1):
    print(i)

# Output:
# 5
# 4
# 3
# 2
# 1

# Why:
# Step = -1 → decreasing sequence


# ================================================================
# 11. range IN REVERSE USING slicing
# ================================================================

r = list(range(1, 6))
print(r[::-1])

# Output:
# [5, 4, 3, 2, 1]

# Why:
# list slicing [start:stop:step] → step = -1 reverses list


# ================================================================
# 12. REAL-WORLD EXAMPLES
# ================================================================

# Example 1: sum of first 10 numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

# Output:
# Sum: 55

# Example 2: even numbers
for i in range(2, 11, 2):
    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10


# ================================================================
# 13. INTERVIEW / EXAM POINTS
# ================================================================

"""
1. range() generates numbers up to stop-1
2. step cannot be 0
3. Arguments must be integers
4. Can be converted to list using list()
5. Negative step → reverse sequence
6. Can be used in for loop to iterate indices
"""

print("\n========== END OF RANGE() REVISION ==========")
