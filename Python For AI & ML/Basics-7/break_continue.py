"""
====================================================================
            BREAK & CONTINUE STATEMENTS IN PYTHON 
====================================================================

This file explains:
1. What is break
2. What is continue
3. How break works internally
4. How continue works internally
5. break / continue with while loop
6. break / continue with for loop
7. while-else and for-else behavior
8. Common mistakes and errors
9. Real-world use cases

Python Version: Python 3.x
====================================================================
"""

# ================================================================
# 1. WHAT IS break?
# ================================================================

"""
break is a LOOP CONTROL STATEMENT.

Purpose:
- Immediately TERMINATES the loop
- Control moves OUTSIDE the loop

break works with:
- while loop
- for loop
"""

# ================================================================
# 2. WHAT IS continue?
# ================================================================

"""
continue is a LOOP CONTROL STATEMENT.

Purpose:
- SKIPS the current iteration
- Moves to the NEXT iteration of the loop

continue does NOT stop the loop.
"""

# ================================================================
# 3. break IN while LOOP
# ================================================================

i = 1

while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# Output:
# 1
# 2

# Why:
# i = 1 → printed
# i = 2 → printed
# i = 3 → break executes → loop terminates immediately


# ================================================================
# 4. continue IN while LOOP
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
# When i == 3:
# continue skips print(i)
# Loop continues with next iteration


# ================================================================
# 5. break IN for LOOP
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
# break stops loop when i becomes 4


# ================================================================
# 6. continue IN for LOOP
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
# When i == 3 → iteration skipped


# ================================================================
# 7. break vs continue (SIDE BY SIDE)
# ================================================================

print("\nbreak example:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Output:
# 1
# 2

print("\ncontinue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:
# 1
# 2
# 4
# 5

# Key Difference:
# break    → exits loop completely
# continue → skips current iteration only


# ================================================================
# 8. break WITH while-else
# ================================================================

i = 1

while i <= 3:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("Loop finished normally")

# Output:
# 1

# Why:
# break executed → else block is SKIPPED


# ================================================================
# 9. continue WITH while-else
# ================================================================

i = 0

while i < 3:
    i += 1
    if i == 2:
        continue
    print(i)
else:
    print("Loop finished normally")

# Output:
# 1
# 3
# Loop finished normally

# Why:
# continue does NOT stop the loop
# Loop ends normally → else executes


# ================================================================
# 10. COMMON MISTAKES & ERRORS
# ================================================================

# ❌ continue without increment (INFINITE LOOP)
# i = 0
# while i < 5:
#     if i == 2:
#         continue
#     print(i)
#     i += 1

"""
Problem:
- When i == 2 → continue executes
- i += 1 is skipped
- i remains 2 forever
- Infinite loop
"""


# ❌ break outside loop
# break

"""
Error:
SyntaxError: 'break' outside loop

Why:
- break is allowed ONLY inside loops
"""


# ❌ continue outside loop
# continue

"""
Error:
SyntaxError: 'continue' not properly in loop

Why:
- continue works only inside loops
"""


# ================================================================
# 11. REAL-WORLD EXAMPLE (SEARCH)
# ================================================================

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        print("Number found")
        break
    print("Checking:", num)

# Output:
# Checking: 10
# Checking: 20
# Number found

# Why:
# break stops search once item is found


# ================================================================
# 12. REAL-WORLD EXAMPLE (SKIP INVALID DATA)
# ================================================================

data = [10, -5, 20, -1, 30]

for value in data:
    if value < 0:
        continue
    print(value)

# Output:
# 10
# 20
# 30

# Why:
# continue skips negative values


# ================================================================
# 13. WHEN TO USE break?
# ================================================================

"""
Use break when:
- Desired value is found
- Error condition occurs
- Loop must stop immediately
"""

# ================================================================
# 14. WHEN TO USE continue?
# ================================================================

"""
Use continue when:
- Some values should be skipped
- Validation fails
- Only certain cases need processing
"""

# ================================================================
# 15. EXAM / INTERVIEW SUMMARY
# ================================================================

"""
break:
- Terminates loop immediately
- Skips loop else
- Used to stop execution

continue:
- Skips current iteration
- Loop continues
- Does NOT affect loop else
"""

print("\n========== END OF BREAK & CONTINUE REVISION ==========")
