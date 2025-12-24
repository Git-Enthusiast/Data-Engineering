import sys
sys.stdout.reconfigure(encoding='utf-8')



"""
============================================================
📌 PYTHON print() FUNCTION – COMPLETE REVISION FILE
============================================================

The print() function is a built-in Python function used to
display output on the console (standard output) or write
output to a file/stream.

Internal Function Signature:
------------------------------------------------------------
print(*values,
      sep=" ",
      end="\n",
      file=sys.stdout,
      flush=False) -> None
"""

# ==========================================================
# 1️⃣ BASIC print() USAGE
# ==========================================================

# Printing a single value
print("Hello, Python")

# Printing multiple values
print("Rajan", "Raj", 2025)

# Note:
# - print() can accept any data type
# - Internally, Python converts values using str()

print(10, 20.5, True, None)

# ==========================================================
# 2️⃣ *values PARAMETER (VARIABLE LENGTH ARGUMENTS)
# ==========================================================

# *values means:
# - You can pass any number of arguments
# - Arguments are separated by 'sep'

print("A")
print("A", "B")
print("A", "B", "C")

# ==========================================================
# 3️⃣ sep PARAMETER (SEPARATOR)
# ==========================================================

# Default separator is a single space " "
print("Python", "Java", "C++")
# Output: Python Java C++

# Custom separator
print("Python", "Java", "C++", sep=", ")
# Output: Python, Java, C++

print(1, 2, 3, 4, sep=" | ")
# Output: 1 | 2 | 3 | 4

print("2025", "12", "24", sep="-")
# Output: 2025-12-24

# IMPORTANT:
# sep must be a string or None
# print("A", "B", sep=5)  ❌ TypeError

# ==========================================================
# 4️⃣ end PARAMETER (LINE ENDING)
# ==========================================================

# Default end is newline "\n"
print("Hello")
print("World")
# Output:
# Hello
# World

# Custom end (no newline)
print("Hello", end=" ")
print("World")
# Output: Hello World

# Printing on the same line
print("A", end="")
print("B", end="")
print("C")
# Output: ABC

# Using symbols in end
print("Loading", end="...")
print("Done")
# Output: Loading...Done

# ==========================================================
# 5️⃣ sep + end TOGETHER
# ==========================================================

print("Rajan", "Raj", 2025, sep=" | ", end=" ✅\n")
# Output: Rajan | Raj | 2025 ✅

# ==========================================================
# 6️⃣ file PARAMETER (PRINTING TO FILE)
# ==========================================================

# By default, print() writes to sys.stdout (console)

# Writing output to a file
file_obj = open("print_output.txt", "w")

print("This output goes into a file", file=file_obj)
print("Python print() function", file=file_obj)

file_obj.close()

# Recommended way using 'with'
with open("print_output_safe.txt", "w") as f:
    print("Safe file writing", file=f)
    print("No need to close manually", file=f)

# ==========================================================
# 7️⃣ flush PARAMETER (FORCE OUTPUT)
# ==========================================================

# Normally, output is buffered (stored temporarily)
# flush=True forces immediate writing

import time

print("Processing...", end="", flush=True)
time.sleep(2)
print("Done")

# Example: real-time counter
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)

print()  # newline after loop

# ==========================================================
# 8️⃣ IMPORTANT INTERNAL FACTS
# ==========================================================

# ✔ print() returns None
result = print("Return value check")
print(result)  # Output: None

# ✔ print() uses str() internally
x = 100
print(str(x))

# ✔ file must have a write() method

# ==========================================================
# 9️⃣ COMMON MISTAKES (DO NOT DO THIS)
# ==========================================================

# print("A", "B", sep=10)        ❌ sep must be string
# print("Hello", end=5)         ❌ end must be string
# print("Hello", file="a.txt")  ❌ file must be file object

# ==========================================================
# 🔟 ONE-LINE SUMMARY (EXAM READY)
# ==========================================================

# print() is a built-in function that outputs one or more
# values to the console or a file, allowing control over
# separators, line endings, output destination, and buffering.

"""
==================== END OF REVISION ========================
"""
