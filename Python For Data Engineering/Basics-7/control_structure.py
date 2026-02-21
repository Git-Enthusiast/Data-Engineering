# ============================================
# Python Control Structures – Quick Revision
# ============================================

# Control structures decide the order in which
# instructions are executed in a program.

# There are 3 types:
# 1️⃣ Sequential Control
# 2️⃣ Selection Control
# 3️⃣ Iterative Control


# ============================================
# 1️⃣ Sequential Control
# ============================================
# Instructions are executed in the exact order
# they appear in the program.
# This is the default behavior in Python.

print("Hello")
print("Welcome")
print("Welcome to Amulya's Academy")

# Output:
# Hello
# Welcome
# Welcome to Amulya's Academy


# ============================================
# 2️⃣ Selection Control (if-else)
# ============================================
# Executes specific block of code based on condition.
# If condition is True → if block runs
# If condition is False → else block runs

num = int(input("Enter a number: "))

if num < 10:
    print("Number is less than 10")
else:
    print("Number is 10 or greater")


# ============================================
# 3️⃣ Iterative Control (while loop)
# ============================================
# Repeats a block of code as long as condition is True.
# Three important parts:
# 1. Initialization
# 2. Condition
# 3. Increment/Decrement

i = 0               # Initialization

while i < 10:       # Condition
    print(i)
    i += 1          # Increment

# Output:
# 0 1 2 3 4 5 6 7 8 9


# ============================================
# Quick Summary
# ============================================
# Sequential → Executes line by line
# Selection  → Executes based on condition (if-else)
# Iterative  → Repeats code using loops (while/for)
# ============================================