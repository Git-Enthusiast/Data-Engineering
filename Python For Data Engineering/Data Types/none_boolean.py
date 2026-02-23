"""
=====================================================================
        PYTHON NoneType & BOOLEAN DATA TYPES – MASTER FILE
=====================================================================

This file explains two fundamental data types in Python:

    1️⃣ NoneType
    2️⃣ Boolean (bool)

Both are very important for control flow, conditions, and logic building.

=====================================================================
                        1️⃣ NoneType
=====================================================================

📌 What is None?
----------------
• None represents the absence of a value.
• Similar to NULL in C/C++/Java.
• It means: "No value assigned yet".

Example:
    x = None

📌 Why use None?
----------------
• To declare a variable before assigning an actual value.
• Prevents syntax errors.
• Useful when value will be assigned later.

Example:
    result = None
    # Later in code
    result = 10

📌 Type of None
----------------
The type of None is:

    <class 'NoneType'>

Check using:
    type(None)

📌 Important Points
-------------------
• None is a keyword.
• There is only ONE None object in Python (singleton).
• None is immutable.
• None is considered False in boolean context.

=====================================================================
                        2️⃣ Boolean Data Type
=====================================================================

📌 What is Boolean?
-------------------
• Boolean data type represents logical values.
• It has only TWO values:

    True
    False

• Type of True and False:

    <class 'bool'>

📌 Important Notes
-------------------
• True and False are keywords.
• Boolean is a subclass of int.
    True  → 1
    False → 0

Example:
    True + True = 2
    True + False = 1

=====================================================================
                TRUTHINESS & FALSINESS IN PYTHON
=====================================================================

Python evaluates values as True or False automatically
when used inside conditions.

📌 Values considered FALSE:
----------------------------
• 0
• 0.0
• False
• None
• Empty list      []
• Empty tuple     ()
• Empty set       {}
• Empty dict      {}
• Empty string    ""
• Expressions returning None or 0

📌 Values considered TRUE:
---------------------------
• Non-zero numbers (5, -3, 2.5)
• Non-empty list  [1]
• Non-empty dict  {"a":1}
• Non-empty set   {1}
• Non-empty tuple (1,)
• Non-empty string "Hello"
• True keyword
• Expressions returning non-zero values

=====================================================================
                        EXAMPLES
=====================================================================
"""

# ==============================================================
# NoneType Examples
# ==============================================================

print("NoneType Examples:")
x = None
print("Value of x:", x)
print("Type of x:", type(x))

# Checking if variable is None
if x is None:
    print("x is None")


# ==============================================================
# Boolean Examples
# ==============================================================

print("\nBoolean Examples:")
a = True
b = False

print("Value of a:", a, type(a))
print("Value of b:", b, type(b))

# Boolean as integers
print("\nBoolean as integers:")
print("True + True =", True + True)
print("True + False =", True + False)
print("False + False =", False + False)


# ==============================================================
# Truthiness & Falsiness Examples
# ==============================================================

print("\nTruthiness & Falsiness:")

# Zero → False
if 0:
    print("0 is True")
else:
    print("0 is False")

# Non-zero → True
if 5:
    print("5 is True")

# None → False
if None:
    print("None is True")
else:
    print("None is False")

# Empty list → False
if []:
    print("Empty list is True")
else:
    print("Empty list is False")

# Non-empty list → True
if [1, 2, 3]:
    print("Non-empty list is True")

# Empty string → False
if "":
    print("Empty string is True")
else:
    print("Empty string is False")

# Non-empty string → True
if "Python":
    print("Non-empty string is True")


# ==============================================================
# Boolean Expressions
# ==============================================================

print("\nBoolean Expressions:")

print("10 > 5:", 10 > 5)
print("5 == 5:", 5 == 5)
print("3 < 1:", 3 < 1)

# Using bool() function
print("\nUsing bool() function:")
print("bool(0):", bool(0))
print("bool(10):", bool(10))
print("bool(None):", bool(None))
print("bool([]):", bool([]))
print("bool([1]):", bool([1]))


"""
=====================================================================
                        FINAL SUMMARY
=====================================================================

🔹 NoneType
    ✔ Represents absence of value
    ✔ Similar to NULL
    ✔ Only one None object (singleton)
    ✔ Immutable
    ✔ Evaluates to False

🔹 Boolean (bool)
    ✔ Two values: True and False
    ✔ Subclass of int
    ✔ True = 1, False = 0

🔹 Truthy Values
    ✔ Non-zero numbers
    ✔ Non-empty collections
    ✔ True keyword

🔹 Falsy Values
    ✔ 0, 0.0
    ✔ None
    ✔ False
    ✔ Empty collections
    ✔ Empty string

=====================================================================
                    END OF MASTER FILE
=====================================================================
"""
🧠 Deep dive into bool as subclass of int (interview level)

Perfect Rajan 🔥
Now we go interview level deep dive into:

🧠 bool as Subclass of int in Python

This is a very common interview question.

1️⃣ First Proof – Is bool really a subclass of int?
print(issubclass(bool, int))      # True
print(isinstance(True, int))      # True
print(isinstance(False, int))     # True
✅ Output:
True
True
True

So officially:

bool → subclass of int
2️⃣ Why Did Python Design It This Way?

In Python:

True  = 1
False = 0

But not just conceptually — internally also.

print(int(True))   # 1
print(int(False))  # 0

This design allows:

Arithmetic with boolean values

Logical operations combined with numeric calculations

Clean counting patterns

3️⃣ Memory-Level Behavior

Let’s inspect:

print(type(True))        # <class 'bool'>
print(type(False))       # <class 'bool'>

print(id(True))
print(id(1))

⚠ Important:

Although True == 1, they are not the same object.

print(True == 1)     # True
print(True is 1)     # False  (important for interviews)
Interview Key Point:
True == 1   → True  (value equality)
True is 1   → False (identity difference)
4️⃣ Arithmetic Behavior of bool

Since bool is subclass of int:

print(True + True)      # 2
print(True + False)     # 1
print(False + False)    # 0

print(True * 10)        # 10
print(False * 10)       # 0
Why?

Because:

True  → 1
False → 0
5️⃣ Practical Real-World Usage (Important)

This allows powerful patterns like:

Counting condition matches:
numbers = [10, 15, 20, 25, 30]

count = sum(n > 18 for n in numbers)

print(count)   # 3

Why does this work?

Because:

(n > 18) → True or False
True → 1
False → 0
sum() adds them

🔥 This is elegant Python design.

6️⃣ Is bool Exactly Same as int?

No.

Although subclass, bool overrides some behavior.

Example:

print(True + 1)      # 2
print(True + True)   # 2

But:

print(True.__class__)      # <class 'bool'>
print(int.__class__)       # <class 'type'>

Also:

print(bool(2))     # True
print(bool(0))     # False
7️⃣ Why bool is Subclass of int? (Design Philosophy)

Python philosophy:

"Booleans are just special integers."

Historically:

Many languages treat true as 1 and false as 0.

Python kept mathematical consistency.

Makes conditions seamlessly usable in arithmetic.

8️⃣ Internal Hierarchy
object
   ↓
int
   ↓
bool

Proof:

print(bool.__mro__)

Output:

(<class 'bool'>, <class 'int'>, <class 'object'>)

MRO = Method Resolution Order

Meaning:

bool inherits from int

int inherits from object

9️⃣ Important Interview Edge Case
print(True + True * False)

Step by step:

True * False → 1 * 0 → 0
True + 0 → 1

Output:

1
🔟 Tricky Interview Question
print(True == 1)      # True
print(False == 0)     # True
print(True is 1)      # False
print(False is 0)     # False

💡 Explanation:

== checks value

is checks identity (memory address)

1️⃣1️⃣ Boolean in Bitwise Operations

Since bool is int:

print(True & False)   # False
print(True | False)   # True
print(True ^ False)   # True

These behave like bitwise operations on 1 and 0.

1️⃣2️⃣ Is bool mutable?

No.

Like int, bool is immutable.

1️⃣3️⃣ When NOT to Treat bool as int

Although allowed, avoid this:

x = True + 5

Why?

It reduces code readability.

Better:

x = int(True) + 5

Cleaner intention.

🚀 Interview-Level Summary

✔ bool is subclass of int
✔ True = 1, False = 0
✔ Supports arithmetic
✔ Supports bitwise operations
✔ True == 1 but True is 1 is False
✔ Inherits from int (check using __mro__)
✔ Enables elegant counting patterns

🎯 If Interviewer Asks:

Q: Why is bool subclass of int in Python?

Best Answer:

Python treats boolean values as special integers for mathematical consistency and simplicity. True behaves like 1 and False behaves like 0, allowing boolean expressions to participate naturally in arithmetic operations while still maintaining logical semantics.

If you want next:

🧠 Deep dive into None internals

🔬 Memory model of Python objects

⚔️ == vs is deep internal explanation

📘 Full Python data model master guide

Tell me Rajan 😎

🧠 Deep dive into None internals

Perfect Rajan 🔥
Now we go interview-level deep dive into None internals — this is advanced Python object model understanding.

🧠 Deep Dive into None Internals (Interview Level)
1️⃣ What Exactly is None?

None is:

A special constant in Python

Represents absence of value

Only instance of NoneType

A singleton object

Proof:

print(type(None))              # <class 'NoneType'>
2️⃣ What is NoneType?

Internally:

print(None.__class__)          # <class 'NoneType'>

Hierarchy:

print(type(None).__mro__)

Output:

(<class 'NoneType'>, <class 'object'>)

So:

object
   ↓
NoneType

Important:

👉 You cannot create another NoneType object manually.

NoneType()   # ❌ Not allowed
3️⃣ Singleton Pattern – There Is Only ONE None

This is critical.

a = None
b = None

print(a is b)     # True

Why?

Because Python creates only one None object in memory.

This is called:

Singleton Design Pattern

Internally (CPython):

Py_None

It is a globally shared object.

4️⃣ Memory Behavior of None
print(id(None))
print(id(None))

Always same ID.

Unlike numbers:

print(id(1000))
print(id(1000))

May or may not be same (depends on optimization).

But for None:

✔ Always same object.

5️⃣ Why Should We Use is Instead of == With None?

Best practice:

if x is None:

NOT:

if x == None:

Why?

Because:

is checks identity (memory)

None is singleton → identity check is correct

== can be overridden by objects

Example:

class Test:
    def __eq__(self, other):
        return True

t = Test()

print(t == None)   # True (dangerous!)
print(t is None)   # False (correct)

🔥 Interview gold point.

6️⃣ Truthiness of None
print(bool(None))   # False

Why?

Because Python internally defines:

None → Falsy

Used in:

if result:
    ...

If result is None → condition fails.

7️⃣ None in Functions (Very Important)

If a function does not return anything:

def greet():
    print("Hello")

x = greet()
print(x)

Output:

Hello
None

Why?

Because Python automatically returns:

return None

Implicit return.

8️⃣ None vs 0 vs Empty String

Important difference:

print(None == 0)        # False
print(None == "")       # False
print(None == False)    # False

Even though all are falsy:

They are NOT equal.

Falsy ≠ Equal

9️⃣ Can You Reassign None?

No.

None = 5

❌ SyntaxError

Because:

None is keyword

Reserved constant

🔟 Internal CPython Implementation

In CPython source:

PyObject _Py_NoneStruct = {
    PyObject_HEAD_INIT(&_PyNone_Type)
};

And exposed as:

Py_None

Meaning:

Created once

Lives for entire interpreter lifetime

Reference counted but never destroyed

1️⃣1️⃣ None and Garbage Collection

None is never garbage collected.

It exists throughout program execution.

Global static object.

1️⃣2️⃣ Why Python Uses None Instead of Null Pointer?

In languages like C:

NULL → memory address 0

Danger:

Dereferencing NULL → crash

Python:

Safe object

Cannot be dereferenced

Treated like normal object

Safer design.

1️⃣3️⃣ Common Interview Trap
x = []
if x:
    print("True")

This fails because empty list is falsy.

Better:

if x is None:

To specifically check absence of value.

Difference:

Check	Meaning
if not x	Falsy check
if x is None	Exact None check
1️⃣4️⃣ Why None is Not False?
print(None == False)   # False

Because:

False is boolean

None is separate type

They only share falsy behavior

🚀 Interview-Level Summary

✔ None is singleton
✔ Only one object exists
✔ Type is NoneType
✔ Inherits from object
✔ Always use is None
✔ Implicit return value of functions
✔ Falsy but not equal to False
✔ Cannot instantiate NoneType manually
✔ Exists for entire interpreter lifetime

🎯 If Interviewer Asks:

Q: Why is None implemented as singleton in Python?

Best answer:

None represents the absence of value and must be universally consistent across the interpreter. Making it a singleton ensures memory efficiency, identity reliability, and consistent behavior when checking with is.

If you want next deep topic:

🔬 Python Object Model (Everything is object)

🧠 CPython memory model

⚔️ is vs == internal implementation

📘 Data Model & dunder methods deep dive

🏗 How Python stores integers internally
