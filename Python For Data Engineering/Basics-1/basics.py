'''

# Python Fundamentals – Quick Revision Notes

---

## 1️⃣ Identifiers

Identifiers are names used in a Python program.
Examples: variable names, function names, class names.

### ✅ Rules

- Can contain letters (A–Z, a–z), digits (0–9), and underscore (_)
- Must start with a letter or underscore
- Cannot start with a digit
- Cannot contain special characters like @, #, $, %, etc.
- Cannot use Python keywords

### ✔ Valid Examples

```python
name = "Rajan"
_age = 21
total_marks = 450

❌ Invalid Examples:
1name = "Rajan"      # Cannot start with digit
my-name = "Rajan"    # Hyphen not allowed
class = 10           # 'class' is a keyword
2️⃣ Keywords

Keywords are reserved words in Python.
They have predefined meanings.

Examples:
if, else, while, for, and, or, True, False, None

⚠️ Keywords cannot be used as identifiers.

To see all Python keywords:
help('keywords')
3️⃣ Control Characters

Control characters control the output format.

Common Control Characters:

\n → New line

\t → Tab space

\\ → Backslash

\" → Double quote inside string

Example:
print("Hello\nWorld")

Output:

Hello
World
Example with Tab:
print("Name:\tRajan")

Output:

Name:   Rajan
4️⃣ Line Joining Methods

Sometimes a statement is too long and we want to write it in multiple lines.

There are two methods:

✅ 1. Implicit Line Joining

No special symbol needed.
Python automatically joins lines when inside:

Parentheses ()

Square brackets []

Curly braces {}

🔹 Example using Parentheses:
total = (10 +
         20 +
         30)
print(total)
🔹 Example using List:
numbers = [
    10,
    20,
    30,
    40
]
🔹 Example using Dictionary:
student = {
    "name": "Rajan",
    "age": 21,
    "course": "CSE"
}

✔ No backslash needed
✔ Cleaner and recommended method

✅ 2. Explicit Line Joining

Uses backslash \ to continue statement on next line.

🔹 Example:
total = 10 + \
        20 + \
        30
print(total)

✔ Backslash tells Python that statement continues
⚠️ No space allowed after backslash

'''
