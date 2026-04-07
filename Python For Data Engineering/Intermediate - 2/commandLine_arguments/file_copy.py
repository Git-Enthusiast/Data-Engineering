"""
========================================================
   Command Line Arguments in Python (sys.argv)
========================================================

GOAL:
-----
Read data from one file and write it to another file
using dynamic file names passed via command line.

Example:
--------
text1.txt → contains: "Hello World"
text2.txt → empty

Command:
--------
python file_copy.py text1.txt text2.txt

Result:
-------
text2.txt → "Hello World"

--------------------------------------------------------
WHAT IS sys.argv?
--------------------------------------------------------
sys.argv is a list that stores command line arguments.

sys.argv[0] → script name
sys.argv[1] → first argument
sys.argv[2] → second argument

--------------------------------------------------------
ADVANTAGE:
--------------------------------------------------------
✔ Dynamic file handling
✔ Reusable script
✔ No hardcoding
"""

import sys


# =======================================================
# 1. CHECK ARGUMENT COUNT
# =======================================================

if len(sys.argv) != 3:
    print("Usage: python file_copy.py <source_file> <destination_file>")
    sys.exit(1)

# Extract file names
source_file = sys.argv[1]
destination_file = sys.argv[2]


# =======================================================
# 2. READ FROM SOURCE FILE
# =======================================================

try:
    with open(source_file, 'r') as f:
        data = f.read()
        print(f"Reading from '{source_file}' successful.")

except FileNotFoundError:
    print(f"Error: File '{source_file}' not found.")
    sys.exit(1)

except Exception as e:
    print("Error while reading file:", e)
    sys.exit(1)


# =======================================================
# 3. WRITE TO DESTINATION FILE
# =======================================================

try:
    with open(destination_file, 'w') as f:
        f.write(data)
        print(f"Writing to '{destination_file}' successful.")

except Exception as e:
    print("Error while writing file:", e)
    sys.exit(1)


# =======================================================
# 4. SUCCESS MESSAGE
# =======================================================

print("\nFile copied successfully!")
print(f"{source_file} → {destination_file}")


# =======================================================
# 5. EXTRA: OPTIONAL APPEND MODE
# =======================================================

"""
If you want to APPEND instead of overwrite:

Change:
    open(destination_file, 'w')

To:
    open(destination_file, 'a')
"""


# =======================================================
# 6. EXTRA: SHOW FILE CONTENT AFTER COPY
# =======================================================

print("\nContent in destination file:")

try:
    with open(destination_file, 'r') as f:
        print(f.read())

except Exception as e:
    print("Error reading destination file:", e)


# =======================================================
# 7. INTERVIEW NOTES
# =======================================================

"""
IMPORTANT QUESTIONS:

Q1: What is sys.argv?
→ List of command line arguments

Q2: Why check len(sys.argv)?
→ To ensure correct number of arguments

Q3: Difference between 'w' and 'a'?
→ 'w' overwrites, 'a' appends

Q4: What happens if file doesn't exist?
→ FileNotFoundError

Q5: Advantage of using command line args?
→ Makes program dynamic and reusable
"""


# =======================================================
# 8. HOW TO RUN (STEP-BY-STEP)
# =======================================================

"""
1. Create files:
   text1.txt → Hello World
   text2.txt → (empty)

2. Save this file as:
   file_copy.py

3. Run in terminal:
   python file_copy.py text1.txt text2.txt

4. Check text2.txt
"""


# =======================================================
# 9. ONE-LINE SUMMARY
# =======================================================

"""
sys.argv allows dynamic input from command line,
making file handling flexible and reusable.
"""