"""
========================================================
    Python match-case (Structural Pattern Matching) 
========================================================

Introduced in Python 3.10

match-case is similar to switch-case in other languages
but more powerful. It supports:
- Value matching
- Multiple values
- Guards (conditions)
- Tuple, List, Dictionary matching
- Pattern unpacking

IMPORTANT:
This file is for REVISION, TEACHING, and INTERVIEW prep.
"""

# -------------------------------------------------------
# 1. BASIC MATCH-CASE WITH INTEGERS
# -------------------------------------------------------

choice = 2

match choice:
    case 1:
        print("You selected Option 1")
    case 2:
        print("You selected Option 2")
    case 3:
        print("You selected Option 3")
    case _:
        print("Invalid option")  # default case


# -------------------------------------------------------
# 2. MATCH-CASE WITH STRINGS
# -------------------------------------------------------

day = "sunday"

match day:
    case "monday":
        print("Start of the work week")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")


# -------------------------------------------------------
# 3. MATCH-CASE WITH GUARD CONDITIONS (if)
# -------------------------------------------------------
# Guard allows condition checking inside case

age = 25

match age:
    case x if x < 18:
        print("Minor")
    case x if 18 <= x < 60:
        print("Adult")
    case _:
        print("Senior Citizen")


# -------------------------------------------------------
# 4. MATCH-CASE WITH TUPLES (Pattern Unpacking)
# -------------------------------------------------------

point = (8, 8)

match point:
    case (0, 0):
        print("Point at Origin")
    case (0, y):
        print(f"Point on Y-axis at {y}")
    case (x, 0):
        print(f"Point on X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")


# -------------------------------------------------------
# 5. MATCH-CASE WITH LISTS
# -------------------------------------------------------

numbers = [1, 2, 3]

match numbers:
    case [1, 2, 3]:
        print("Exact list match")
    case [1, x, y]:
        print(f"List starts with 1, values are {x} and {y}")
    case _:
        print("No list match found")


# -------------------------------------------------------
# 6. MATCH-CASE WITH DICTIONARY (VERY IMPORTANT)
# -------------------------------------------------------

student = {
    "name": "Rajan",
    "role": "student",
    "course": "CSE"
}

match student:
    case {"name": name, "role": "student"}:
        print(f"{name} is a student")
    case {"name": name, "role": "teacher"}:
        print(f"{name} is a teacher")
    case _:
        print("Unknown role")


# -------------------------------------------------------
# 7. MATCH-CASE WITH USER INPUT (MENU DRIVEN PROGRAM)
# -------------------------------------------------------

choice = 3

match choice:
    case 1:
        print("Add operation selected")
    case 2:
        print("Delete operation selected")
    case 3:
        print("Update operation selected")
    case 4:
        print("View operation selected")
    case _:
        print("Invalid menu choice")


# -------------------------------------------------------
# 8. MATCH-CASE vs IF-ELIF (LOGIC COMPARISON)
# -------------------------------------------------------

num = 10

# Using if-elif
if num == 10:
    print("Ten (if-elif)")
elif num == 20:
    print("Twenty (if-elif)")
else:
    print("Other number (if-elif)")

# Using match-case
match num:
    case 10:
        print("Ten (match-case)")
    case 20:
        print("Twenty (match-case)")
    case _:
        print("Other number (match-case)")


# -------------------------------------------------------
# 9. IMPORTANT RULES (REVISION NOTES)
# -------------------------------------------------------

"""
RULES TO REMEMBER:
1. Python version must be 3.10 or above
2. 'case _:' acts as default
3. Patterns are checked from top to bottom
4. match-case does NOT need break statements
5. Best for structured and multiple condition checks
"""


# -------------------------------------------------------
# 10. ONE-LINE INTERVIEW SUMMARY
# -------------------------------------------------------

"""
match-case is used for structural pattern matching in Python,
allowing clean, readable, and powerful handling of multiple
values, conditions, and data structures.
"""
