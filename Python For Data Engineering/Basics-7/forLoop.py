"""
====================================================================
                        FOR LOOP IN PYTHON
====================================================================

This file explains:
1. What is a for loop
2. Syntax and working
3. for loop with range()
4. Iterating over sequences
5. break, continue, else with for
6. Nested for loops
7. Common mistakes & errors
8. Real-world examples

Python Version: Python 3.x
====================================================================
"""

# ================================================================
# 1. WHAT IS A FOR LOOP?
# ================================================================

"""
A for loop is used to iterate over a SEQUENCE of values.

Sequences include:
- list
- tuple
- string
- set
- dictionary
- range()

The loop runs once for EACH element in the sequence.
"""

# ================================================================
# 2. BASIC SYNTAX
# ================================================================

"""
for variable in sequence:
    statement(s)
"""

# ================================================================
# 3. SIMPLE for LOOP
# ================================================================

for i in [1, 2, 3, 4, 5]:
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# Why:
# for loop takes one element at a time from the list
# i gets assigned each value sequentially


# ================================================================
# 4. for LOOP WITH range()
# ================================================================

"""
range(start, stop, step)

start → starting value (default = 0)
stop  → ending value (excluded)
step  → increment/decrement (default = 1)
"""

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5

# Why:
# range(1,6) generates: 1,2,3,4,5
# stop value 6 is NOT included


# ================================================================
# 5. range() VARIATIONS
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
# Only stop provided → start defaults to 0


for i in range(1, 10, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9

# Why:
# step = 2 → values increase by 2


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
# 6. for LOOP WITH STRING
# ================================================================

for ch in "Python":
    print(ch)

# Output:
# P
# y
# t
# h
# o
# n

# Why:
# String is iterable
# Each character is accessed one by one


# ================================================================
# 7. for LOOP WITH LIST
# ================================================================

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

# Output:
# 10
# 20
# 30
# 40


# ================================================================
# 8. for LOOP WITH TUPLE
# ================================================================

data = (1, 2, 3)

for x in data:
    print(x)

# Output:
# 1
# 2
# 3


# ================================================================
# 9. for LOOP WITH SET
# ================================================================

values = {3, 1, 2}

for v in values:
    print(v)

# Output:
# Order not guaranteed

# Why:
# Set is unordered


# ================================================================
# 10. for LOOP WITH DICTIONARY
# ================================================================

student = {"name": "Rajan", "age": 21, "branch": "CSE"}

for key in student:
    print(key)

# Output:
# name
# age
# branch

# Why:
# Loop iterates over KEYS by default

for value in student.values():
    print(value)

# Output:
# Rajan
# 21
# CSE

# Why:
# Loop iterates over VALUES by default


for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Rajan
# age : 21
# branch : CSE


# ================================================================
# 11. break IN for LOOP
# ================================================================

for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Output:
# 1
# 2
# 3

# Why:
# break terminates the loop immediately


# ================================================================
# 12. continue IN for LOOP
# ================================================================

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:
# 1
# 2
# 4
# 5

# Why:
# continue skips only the current iteration


# ================================================================
# 13. for LOOP WITH else
# ================================================================

for i in range(1, 4):
    print(i)
else:
    print("Loop completed normally")

# Output:
# 1
# 2
# 3
# Loop completed normally

# Why:
# else executes because loop finished WITHOUT break


# ------------------------------------------------
# for-else with break
# ------------------------------------------------

for i in range(1, 4):
    if i == 2:
        break
    print(i)
else:
    print("This will NOT execute")

# Output:
# 1

# Why:
# break prevents else from executing


# ================================================================
# 14. NESTED for LOOP
# ================================================================

for i in range(1, 4):
    for j in range(0, 3):
        print(i, j)

# Output:
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# 3 0
# 3 1
# 3 2

# Why:
# Inner loop runs completely for each outer loop iteration


# ================================================================
# 15. COMMON MISTAKES & ERRORS
# ================================================================

# ❌ Using wrong variable
# for i in range(5):
#     print(j)

"""
Error:
NameError: name 'j' is not defined

Why:
- j was never declared
"""


# ❌ Modifying list while iterating (LOGICAL ERROR)
numbers = [1, 2, 3, 4]

for n in numbers:
    if n == 3:
        numbers.remove(n)

print(numbers)

# Output:
# [1, 2, 4]

# Why:
# Modifying list during iteration can skip elements


# ================================================================
# 16. REAL-WORLD EXAMPLE (SEARCH)
# ================================================================

items = ["pen", "book", "laptop"]

for item in items:
    if item == "laptop":
        print("Item found")
        break
    print("Checking:", item)

# Output:
# Checking: pen
# Checking: book
# Item found


# ================================================================
# 17. REAL-WORLD EXAMPLE (COUNTING)
# ================================================================

sum = 0

for i in range(1, 11):
    sum += i

print("Sum:", sum)

# Output:
# Sum: 55

# Why:
# Sum of numbers from 1 to 10


# ================================================================
# 18. WHEN TO USE for LOOP?
# ================================================================

"""
Use for loop when:
- Iterating over a sequence
- Number of iterations is known
- Traversing collections
"""

# ================================================================
# 19. for vs while (INTERVIEW POINT)
# ================================================================

"""
for   → sequence-based loop
while → condition-based loop
"""


