"""
====================================================================
                PYTHON ERRORS & EXCEPTIONS 
====================================================================

This file explains:
1. What is an error in Python
2. Types of errors
   - Syntax Errors
   - Runtime Errors (Exceptions)
   - Logical Errors
3. Common built-in exceptions
4. Real code examples with actual error messages
5. Why each error occurs
6. How to avoid or fix them

Python Version: Python 3.14.2
====================================================================
"""

# ================================================================
# 1. WHAT IS AN ERROR?
# ================================================================

"""
An ERROR is a problem in a Python program that causes:
- Program to stop execution
- Unexpected behavior
- Incorrect output

Python reports errors using ERROR MESSAGES.
"""


# ================================================================
# 2. TYPES OF ERRORS IN PYTHON
# ================================================================

"""
Python errors are broadly divided into:

1. Syntax Errors   → Code is grammatically incorrect
2. Runtime Errors  → Code is syntactically correct but fails while running
3. Logical Errors  → Code runs but gives wrong output
"""


# ================================================================
# 3. SYNTAX ERRORS
# ================================================================

"""
Syntax Errors occur when Python cannot understand the code.
They are detected BEFORE execution.
"""

# ❌ Example 1: Missing colon
# if True
#     print("Hello")

"""
Error Message:
SyntaxError: expected ':'

Why:
- if statement must end with colon
"""


# ❌ Example 2: Missing closing parenthesis
# print("Hello"

"""
Error Message:
SyntaxError: '(' was never closed

Why:
- Parenthesis not properly closed
"""


# ❌ Example 3: Incorrect indentation
# if True:
# print("Hello")

"""
Error Message:
IndentationError: expected an indented block

Why:
- Python uses indentation to define blocks
"""


# ================================================================
# 4. RUNTIME ERRORS (EXCEPTIONS)
# ================================================================

"""
Runtime errors occur AFTER the program starts running.
These are also called EXCEPTIONS.
"""


# ------------------------------------------------
# NameError
# ------------------------------------------------
# print(x)

"""
Error Message:
NameError: name 'x' is not defined

Why:
- Variable x was never created
"""


# ------------------------------------------------
# TypeError
# ------------------------------------------------
# print(10 + "20")

"""
Error Message:
TypeError: unsupported operand type(s) for +: 'int' and 'str'

Why:
- Python cannot add int and string
"""


# ------------------------------------------------
# ValueError
# ------------------------------------------------
# int("abc")

"""
Error Message:
ValueError: invalid literal for int() with base 10: 'abc'

Why:
- 'abc' cannot be converted to integer
"""


# ------------------------------------------------
# ZeroDivisionError
# ------------------------------------------------
# print(10 / 0)

"""
Error Message:
ZeroDivisionError: division by zero

Why:
- Division by zero is mathematically undefined
"""


# ------------------------------------------------
# IndexError
# ------------------------------------------------
# lst = [1, 2, 3]
# print(lst[5])

"""
Error Message:
IndexError: list index out of range

Why:
- Index 5 does not exist in the list
"""


# ------------------------------------------------
# KeyError
# ------------------------------------------------
# data = {"name": "Rajan"}
# print(data["age"])

"""
Error Message:
KeyError: 'age'

Why:
- Key does not exist in dictionary
"""


# ------------------------------------------------
# AttributeError
# ------------------------------------------------
# x = 10
# x.append(5)

"""
Error Message:
AttributeError: 'int' object has no attribute 'append'

Why:
- append() method belongs to list, not int
"""


# ------------------------------------------------
# ImportError
# ------------------------------------------------
# import non_existing_module

"""
Error Message:
ModuleNotFoundError: No module named 'non_existing_module'

Why:
- Module does not exist or not installed
"""


# ------------------------------------------------
# FileNotFoundError
# ------------------------------------------------
# open("missing_file.txt")

"""
Error Message:
FileNotFoundError: [Errno 2] No such file or directory: 'missing_file.txt'

Why:
- File does not exist in given path
"""


# ------------------------------------------------
# OverflowError
# ------------------------------------------------
# import math
# print(math.exp(1000))

"""
Error Message:
OverflowError: math range error

Why:
- Result too large to represent
"""


# ------------------------------------------------
# MemoryError
# ------------------------------------------------
# big_list = [1] * (10**10)

"""
Error Message:
MemoryError

Why:
- Not enough memory to create object
"""


# ------------------------------------------------
# RecursionError
# ------------------------------------------------
# def fun():
#     return fun()
#
# fun()

"""
Error Message:
RecursionError: maximum recursion depth exceeded

Why:
- Infinite recursive calls
"""

# ------------------------------------------------
# IndentationError (VERY IMPORTANT)
# ------------------------------------------------

"""
IndentationError occurs when:
- Indentation (spaces/tabs) is missing
- Indentation is inconsistent
- Block indentation is incorrect

Python uses indentation to define code blocks
(unlike C/Java which use braces {}).
"""

# ❌ Example 1: Missing indentation after if
# if True:
# print("Hello")

"""
Error Message:
IndentationError: expected an indented block

Why:
- Code inside if must be indented
- Python expects at least one indented statement
"""


# ❌ Example 2: Unexpected indentation
#  print("Hello")

"""
Error Message:
IndentationError: unexpected indent

Why:
- Indentation given where it is not required
"""


# ❌ Example 3: Inconsistent use of tabs and spaces
# if True:
#     print("Hello")
# 	print("World")

"""
Error Message:
IndentationError: inconsistent use of tabs and spaces in indentation

Why:
- Mixing tabs and spaces in the same block
- Python cannot determine block structure
"""


# ✅ Correct indentation example
if True:
    print("Correctly indented block")

"""
Why this works:
- Consistent indentation
- Block structure is clear to Python
"""

# ================================================================
# 5. LOGICAL ERRORS
# ================================================================

"""
Logical Errors:
- No error message
- Program runs successfully
- Output is WRONG
"""

# Example: Finding average (wrong logic)
total = 10 + 20 + 30
average = total / 2     # ❌ WRONG (should be 3)

print("Average:", average)
# Output: 30.0

"""
Why this is wrong:
- Total numbers = 3
- Divided by 2 instead of 3
- Python does NOT detect logical errors
"""


# ================================================================
# 6. MULTIPLE ERRORS IN REAL SCENARIO
# ================================================================

# Example: Calculator input
# num1 = int(input("Enter number: "))
# num2 = int(input("Enter number: "))
# print(num1 / num2)

"""
Possible Errors:
1. ValueError → if user enters non-number
2. ZeroDivisionError → if num2 = 0
"""


# ================================================================
# 7. HANDLING ERRORS (PREVIEW)
# ================================================================

"""
Errors can be handled using try-except block
"""

try:
    x = int("10")
    y = 0
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid conversion")

# Output:
# Cannot divide by zero


# ================================================================
# 8. SUMMARY (VERY IMPORTANT)
# ================================================================

"""
SYNTAX ERROR
- Code is invalid
- Program does NOT start

RUNTIME ERROR (EXCEPTION)
- Code starts
- Program crashes during execution

LOGICAL ERROR
- No crash
- Wrong output

COMMON EXCEPTIONS:
- NameError
- TypeError
- ValueError
- ZeroDivisionError
- IndexError
- KeyError
- AttributeError
- ImportError
- FileNotFoundError
- RecursionError
- IndentationError
"""

print("\n========== END OF ERRORS & EXCEPTIONS REVISION ==========")
