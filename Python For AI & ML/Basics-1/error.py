print("There is no Error in this line")
print("There is no Error in this line too")

# Prin("There is error in this line")

# ============================================================
# SYNTAX ERROR vs RUNTIME ERROR IN PYTHON (COMPLETE SUMMARY)
# ============================================================

# ------------------------------------------------------------
# 1. SYNTAX ERROR
# ------------------------------------------------------------
# Definition:
# A SyntaxError occurs when Python cannot understand the
# structure (grammar) of the code.
#
# Key characteristics:
# - Happens BEFORE program execution
# - The entire file is checked first
# - NO line of code runs
# - Bytecode (.pyc) is NOT generated
# - Cannot be caught using try-except
#
# Common causes:
# - Missing colon (:)
# - Unclosed quotes or brackets
# - Invalid indentation
# - Incorrect keywords
# - Broken expressions
#
# Examples:
# if True
#     print("Hello")           # missing colon
#
# print("Hello)                # unclosed string
#
# for i in range(5))
#     print(i)                 # extra parenthesis
#
# Error message type:
# - SyntaxError
# - IndentationError (a type of SyntaxError)
#
# Important rule:
# - If a SyntaxError exists anywhere in the file,
#   the program will NOT run at all.
#
# ------------------------------------------------------------
# 2. RUNTIME ERROR
# ------------------------------------------------------------
# Definition:
# A RuntimeError occurs when Python understands the code
# but fails while executing it.
#
# Key characteristics:
# - Happens DURING execution
# - Code runs until the error line is reached
# - Bytecode (.pyc) IS generated
# - Can be handled using try-except
#
# Common causes:
# - Using undefined variables or functions
# - Division by zero
# - Invalid type operations
# - Index out of range
# - File or module not found
#
# Examples:
# print("Line 1")
# x = 10 / 0                  # ZeroDivisionError
#
# Prin("Hello")               # NameError (misspelled print)
#
# lst = [1, 2, 3]
# print(lst[5])               # IndexError
#
# Error message types:
# - NameError
# - TypeError
# - ZeroDivisionError
# - IndexError
# - ValueError
# - ModuleNotFoundError
#
# Important rule:
# - If ANY line executes successfully,
#   then the file has NO syntax errors.
#
# ------------------------------------------------------------
# 3. HOW PYTHON EXECUTES CODE (IMPORTANT)
# ------------------------------------------------------------
# Step 1: Python checks the entire file for syntax errors
# Step 2: If syntax is valid, Python compiles to bytecode (.pyc)
# Step 3: Bytecode is executed line by line by the PVM
#
# - Syntax errors stop execution at Step 1
# - Runtime errors occur at Step 3
#
# ------------------------------------------------------------
# 4. KEY DIFFERENCES (ONE-LOOK COMPARISON)
# ------------------------------------------------------------
# Syntax Error:
# - Grammar problem
# - Detected before execution
# - No code runs
# - Cannot be caught
#
# Runtime Error:
# - Logic/data problem
# - Detected during execution
# - Partial execution possible
# - Can be caught with try-except
#
# ------------------------------------------------------------
# 5. GOLDEN RULE (REMEMBER FOREVER)
# ------------------------------------------------------------
# If Python runs even ONE line of code,
# then the entire file is syntactically correct.
#
# ------------------------------------------------------------
# END OF SUMMARY
# ============================================================
