"""
====================================================================
                    NESTED LOOPS IN PYTHON
====================================================================

Nested loop = a loop inside another loop

Outer Loop:
- Controls number of rounds

Inner Loop:
- Runs COMPLETELY for EACH iteration of outer loop

Types covered:
1. for inside for
2. while inside while
3. for inside while
4. while inside for
====================================================================
"""

# ================================================================
# 1. NESTED for LOOP (for inside for)
# ================================================================

for i in range(1, 4):          # Outer loop
    for j in range(1, 3):      # Inner loop
        print(i, j)

# Output:
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2

# Why:
# - Outer loop runs 3 times (i = 1,2,3)
# - Inner loop runs FULLY (j = 1,2) for each i
# - Total iterations = 3 × 2 = 6


# ================================================================
# 2. STEP-BY-STEP FLOW (IMPORTANT)
# ================================================================

"""
i = 1
    j = 1 → print(1,1)
    j = 2 → print(1,2)

i = 2
    j = 1 → print(2,1)
    j = 2 → print(2,2)

i = 3
    j = 1 → print(3,1)
    j = 2 → print(3,2)
"""


# ================================================================
# 3. NESTED while LOOP (while inside while)
# ================================================================

i = 1
while i <= 3:                 # Outer while loop
    j = 1
    while j <= 2:             # Inner while loop
        print(i, j)
        j += 1
    i += 1

# Output:
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2

# Why:
# - Inner while resets j = 1 for every outer iteration
# - Same behavior as nested for loop


# ================================================================
# 4. for LOOP INSIDE while LOOP
# ================================================================

i = 1
while i <= 3:
    for j in range(1, 3):
        print(i, j)
    i += 1

# Output:
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2

# Why:
# - Outer while controls rounds
# - Inner for runs completely every time


# ================================================================
# 5. while LOOP INSIDE for LOOP
# ================================================================

for i in range(1, 4):
    j = 1
    while j <= 2:
        print(i, j)
        j += 1

# Output:
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2


# ================================================================
# 6. REAL-WORLD EXAMPLE (CLASS & STUDENTS)
# ================================================================

classes = ["CSE", "ECE"]
students = ["Rajan", "Amit"]

for cls in classes:
    for student in students:
        print(cls, "-", student)

# Output:
# CSE - Rajan
# CSE - Amit
# ECE - Rajan
# ECE - Amit

# Why:
# Each student belongs to each class group iteration


# ================================================================
# 7. PATTERN PRINTING (VERY COMMON)
# ================================================================

rows = 3

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***

# Why:
# - Row number controls star count
# - Inner loop prints stars
# - print() moves to next line


# ================================================================
# 8. MULTIPLICATION TABLE (NESTED LOOP)
# ================================================================

for i in range(1, 4):
    for j in range(1, 6):
        print(i, "x", j, "=", i * j)
    print("-----")

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# -----
# 2 x 1 = 2
# ...


# ================================================================
# 9. break IN NESTED LOOPS
# ================================================================

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)

# Output:
# 1 1
# 2 1
# 3 1

# Why:
# - break exits ONLY the INNER loop
# - Outer loop continues


# ================================================================
# 10. continue IN NESTED LOOPS
# ================================================================

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)

# Output:
# 1 1
# 1 3
# 2 1
# 2 3
# 3 1
# 3 3

# Why:
# - continue skips current inner iteration only


# ================================================================
# 11. COMMON MISTAKE (INFINITE LOOP)
# ================================================================

"""
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        # j += 1   ❌ missing increment → infinite loop
    i += 1
"""

# Why:
# - j never changes
# - Condition always True


# ================================================================
# 12. INTERVIEW IMPORTANT POINTS
# ================================================================

"""
✔ Inner loop runs FULLY for each outer loop iteration
✔ Total executions = outer × inner
✔ break affects only nearest loop
✔ Nested loops increase time complexity
✔ Use carefully for performance
"""

print("\n========== END OF NESTED LOOPS REVISION ==========")
