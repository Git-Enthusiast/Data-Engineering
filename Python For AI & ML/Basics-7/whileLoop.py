"""
====================================================================
                    WHILE LOOP IN PYTHON
====================================================================

This file explains:
1. What is a while loop
2. Syntax and flow
3. Condition evaluation
4. Increment / decrement
5. Infinite loops
6. break, continue
7. while-else
8. Common errors and mistakes
9. Real-world examples

Python Version: Python 3.x
====================================================================
"""

# ================================================================
# 1. WHAT IS A WHILE LOOP?
# ================================================================

"""
A while loop is used to repeatedly execute a block of code
AS LONG AS a given condition is True.

If condition becomes False → loop stops.
"""

# ================================================================
# 2. BASIC SYNTAX
# ================================================================

"""
while condition:
    statement(s)
"""

# ================================================================
# 3. SIMPLE WHILE LOOP
# ================================================================

i = 1

while i <= 5:
    print(i)
    i += 1

# Output:
# 1
# 2
# 3
# 4
# 5

# Why:
# Initial i = 1
# Loop runs while i <= 5
# i increases by 1 each iteration
# When i = 6 → condition becomes False → loop stops


# ================================================================
# 4. PRINT NUMBERS IN REVERSE
# ================================================================

n = 5

while n > 0:
    print(n)
    n -= 1

# Output:
# 5
# 4
# 3
# 2
# 1

# Why:
# Loop runs while n > 0
# n decreases each time
# Stops when n becomes 0


# ================================================================
# 5. WHILE LOOP WITH USER INPUT
# ================================================================

# Uncomment to test interactively
# num = int(input("Enter a number: "))
#
# while num > 0:
#     print(num)
#     num -= 1

"""
Possible Errors:
- ValueError → if input is not an integer
"""


# ================================================================
# 6. INFINITE WHILE LOOP
# ================================================================

# ❌ Example (DO NOT RUN)
# while True:
#     print("Infinite Loop")

"""
Why infinite:
- Condition True never becomes False
"""

# ✅ Controlled infinite loop
count = 1

while True:
    print(count)
    count += 1
    if count > 3:
        break

# Output:
# 1
# 2
# 3

# Why:
# Loop is infinite but break stops it when count > 3


# ================================================================
# 7. break STATEMENT
# ================================================================

i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# Output:
# 1
# 2
# 3
# 4

# Why:
# When i == 5, break exits the loop immediately


# ================================================================
# 8. continue STATEMENT
# ================================================================

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# Output:
# 1
# 2
# 4
# 5

# Why:
# continue skips current iteration when i == 3
# Loop continues with next iteration


# ================================================================
# 9. while WITH else
# ================================================================

i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished normally")

# Output:
# 1
# 2
# 3
# Loop finished normally

# Why:
# else executes only if loop ends WITHOUT break
# means if loops exits or finishes abnormally or by intruption
# "else" Block will not run -> else block will only run when
# loops finishes normally so when "break", "return", "exception"
# is used inside loop "else" block will not execute.


# ------------------------------------------------
# while-else with break
# ------------------------------------------------

i = 1

while i <= 3:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("This will NOT execute")

# Output:
# 1

# Why:
# break prevents else block from executing


# ================================================================
# 10. COMMON MISTAKES & ERRORS
# ================================================================

# ❌ Missing increment (Infinite Loop)
# i = 1
# while i <= 5:
#     print(i)

"""
Problem:
- i never changes
- Condition always True
- Infinite loop
"""

# ❌ Indentation Error
# while i <= 5:
# print(i)

"""
Error:
IndentationError: expected an indented block
"""


# ================================================================
# 11. LOGICAL ERROR EXAMPLE
# ================================================================

i = 1
sum = 0

while i <= 5:
    sum += i
    i += 1

print("Sum:", sum)

# Output:
# Sum: 15

# Why:
# 1 + 2 + 3 + 4 + 5 = 15


# ================================================================
# 12. REAL-WORLD EXAMPLE (PASSWORD CHECK)
# ================================================================

# Uncomment to test
# password = ""
#
# while password != "python123":
#     password = input("Enter password: ")
#
# print("Access Granted")

"""
Why while:
- We don't know how many attempts user will take
- Loop continues until correct password is entered
"""


# ================================================================
# 13. WHEN TO USE while LOOP?
# ================================================================

"""
Use while loop when:
- Number of iterations is NOT known
- Loop depends on condition
- Waiting for user input
- Continuous checking (menus, validation)
"""

# ================================================================
# 14. COMPARISON: while vs for
# ================================================================

"""
while → condition-based
for   → sequence-based
"""

print("\n========== END OF WHILE LOOP REVISION ==========")

