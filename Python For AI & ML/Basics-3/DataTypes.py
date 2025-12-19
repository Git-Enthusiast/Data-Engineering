import sys
sys.stdout.reconfigure(encoding='utf-8')


# ============================================================
# PYTHON DATA TYPES & TYPE CHECKING – COMPLETE BEST SUMMARY
# ============================================================

# Python is a dynamically typed language
# → Data type is decided at runtime
# → No need to declare data type explicitly


# ============================================================
# 1️⃣ NUMERIC TYPES
# ============================================================
# int     → Whole numbers, unlimited precision
# float   → Decimal numbers, accuracy up to 15-17 decimal places
# complex → Real + Imaginary numbers (special numeric type), represented as a + bj

a = 10
b = 3.14
c = 4 + 5j

print(type(a))   # <class 'int'> → a is an integer
print(type(b))   # <class 'float'> → b is a float
print(type(c))   # <class 'complex'> → c is a complex number

# Exponential data falls under float
d = 1.5e3  # 1.5 × 10^3
print(d)     # 1500.0
print(type(d)) # <class 'float'>


# ============================================================
# 2️⃣ SEQUENCE TYPES
# ============================================================
# str   → Sequence of characters (immutable)
# list  → Ordered, mutable, allows mixed data types
# tuple → Ordered, immutable, allows mixed data types


# ##############  STRING DATA TYPE  ##############

# Note: In Python, There is no separate 'char' data type. 
# A single character is simply a string of length 1.

# Strings can be defined using single, double, or triple quotes
single_quote_str = 'Hello, World!'   # Single quotes
double_quote_str = "Python is fun"   # Double quotes
triple_single_quote_str = '''This is a
multi-line string
using triple single quotes.'''       # Triple single quotes
triple_double_quote_str = """This is also a
multi-line string
using triple double quotes."""      # Triple double quotes

print(single_quote_str)  # Output: Hello, World!
print(double_quote_str)  # Output: Python is fun
print(triple_single_quote_str)
print(triple_double_quote_str)

# Length of string
sample_str = "Python"
print(len(sample_str))    # Output: 6
print(type(sample_str))   # <class 'str'>
print(sample_str[0])      # First character: 'P'
print(sample_str[-1])     # Last character: 'n'

# Python supports both Positive and Negative Indexing
# Positive indexing → starts from 0 (beginning)
# Negative indexing → starts from -1 (end)
# Example: text = "Python"
# text[0]  → 'P'
# text[-1] → 'n'

text = "Python"
my_list = [1, 2, 3, "AI", 4.5]
my_tuple = (1, 2, 3, "ML")

print(type(text))      # <class 'str'>
print(type(my_list))   # <class 'list'>
print(type(my_tuple))  # <class 'tuple'>


# ============================================================
# 3️⃣ LIST – DETAILED USE (MOST IMPORTANT)
# ============================================================

# What is a List?
# List → Ordered, mutable, allows duplicate & mixed data types

my_list = [1, 2.5, "Hello", True, 2, "World", [1, 2, 3], {"key": "value"}]
print(type(my_list))  # <class 'list'>
print(my_list)
print(len(my_list))   # 8
print(my_list[2])     # "Hello"
print(my_list[-1])    # {"key": "value"}
print(my_list[6])     # [1, 2, 3]
print(my_list[6][1])  # 2 (accessing nested list element)

# Another list for operations
numbers = [10, 20, 30]

# Accessing elements
print(numbers[0])     # 10 → first element
print(numbers[-1])    # 30 → last element

# Modifying elements (list is mutable)
numbers[1] = 25
print(numbers)        # [10, 25, 30]

# Adding elements
numbers.append(40)      # Add at end
numbers.insert(1, 15)   # Insert at index 1
print(numbers)          # [10, 15, 25, 30, 40]

# Removing elements
numbers.remove(25)    # Remove by value
numbers.pop()         # Remove last element
print(numbers)

# Looping through list
for num in numbers:
    print(num)         # Prints each element


# ############## TUPLE DATA TYPE ##############

# What is a Tuple?
# Tuple → Ordered, immutable, allows duplicate & mixed data types

my_tuple = (1, 2.5, "Hello", True, 2, "World", [1, 2, 3], {"key": "value"})
print(type(my_tuple))  # <class 'tuple'>
print(my_tuple)
print(len(my_tuple))   # 8
print(my_tuple[2])     # "Hello"
print(my_tuple[-1])    # {"key": "value"}
print(my_tuple[6])     # [1, 2, 3]
print(my_tuple[6][1])  # 2

# Tuples are immutable, cannot modify elements
# my_tuple[1] = 3.5  # Uncommenting this line will raise TypeError
# However, if a tuple contains mutable objects (like lists), those can be modified:
t5 = ([1, 2], [3, 4])
print(t5)
t5[0][0] = 10  # Modifying the first element of the first list inside the tuple
print(t5)  # Output: ([10, 2], [3, 4])
t5[1].append(5)  # Appending to the second list inside the tuple
print(t5)  # Output: ([10, 2], [3, 4, 5])
# Note: While the tuple itself is immutable, the mutable objects inside it can be changed.

# ============================================================
# 4️⃣ MAPPING TYPE (DICT)
# ============================================================

# dict → Stores data in key : value pairs
# Keys → unique, immutable (str, int, float, bool, tuple)
# Values → any data type, mutable
# Dictionaries are unordered

student = {
    "name": "Rajan",
    "age": 22,
    "branch": "CSE"
}

print(type(student))       # <class 'dict'>
print(student["name"])     # Access value using key


# ============================================================
# 5️⃣ SET TYPES
# ============================================================

# set → Unordered, mutable, unique values
# frozenset → Unordered, immutable, unique values

unique_nums = {1, 2, 3, 3}          # duplicates automatically removed
fixed_nums = frozenset([1, 2, 3])   # immutable set

print(unique_nums)   # {1, 2, 3}
print(fixed_nums)    # frozenset({1, 2, 3})
print(type(unique_nums))  # <class 'set'>
print(type(fixed_nums))   # <class 'frozenset'>


# ============================================================
# 6️⃣ BOOLEAN TYPE
# ============================================================

# bool → Represents True or False
# bool is a subclass of int (can act like 0 or 1)

is_student = True
print(type(is_student))  # <class 'bool'>


# ============================================================
# 7️⃣ BINARY TYPES
# ============================================================

# bytes     → Immutable sequence of bytes
# bytearray → Mutable sequence of bytes

data1 = b"ABC"
data2 = bytearray(b"ABC")

print(type(data1))  # <class 'bytes'>
print(type(data2))  # <class 'bytearray'>


# ============================================================
# 8️⃣ NONE TYPE
# ============================================================

# NoneType → Represents absence of value
result = None
print(type(result))  # <class 'NoneType'>


# ============================================================
# 9️⃣ isinstance() FUNCTION – TYPE CHECKING (BEST PRACTICE)
# ============================================================

# Syntax:
# isinstance(object, datatype) → Returns True if object is instance of datatype

x = 10
print(isinstance(x, int))           # True
print(isinstance(x, float))         # False
print(isinstance(x, (int, float)))  # True → supports tuple of types

# isinstance() vs type()
y = True
print(type(y) == bool)    # True → strict type check
print(isinstance(y, bool))  # True → recommended, supports inheritance


# ============================================================
# 🔟 PRACTICAL REAL-LIFE EXAMPLE
# ============================================================

data = [10, 3.14, "Python", True, None, [1, 2]]

for item in data:
    if isinstance(item, int):
        print(item, "→ Integer")
    elif isinstance(item, float):
        print(item, "→ Float")
    elif isinstance(item, str):
        print(item, "→ String")
    elif isinstance(item, bool):
        print(item, "→ Boolean")
    elif isinstance(item, list):
        print(item, "→ List")
    elif item is None:
        print(item, "→ NoneType")


# ============================================================
# RANGE DATA TYPE
# ============================================================

# range → Immutable sequence of numbers between start and stop with optional step
r = range(0, 10, 2)
print(type(r))        # <class 'range'>
print(list(r))        # Convert to list: [0, 2, 4, 6, 8]
print(r.start)        # Start value: 0
print(r.stop)         # Stop value: 10
print(r.step)         # Step: 2
print(r[3])           # 6 → fourth element
print(r[-1])          # 8 → last element
print(len(r))         # 5 → total elements

# Using range in loops
for i in range(0, 10, 2):
    print(i)  # Outputs even numbers from 0 to 8

for i in range(5):
    print(i)  # Default start=0, step=1 → outputs 0 to 4

# Printing multiple values
print(12, 12, 23, 4, 42, 2) 
# In print, commas separate multiple values and act as a space
print("Hello", "World")


# ============================================================
# FINAL KEY TAKEAWAYS
# ============================================================

# ✔ Python data types are grouped into categories
# ✔ list is mutable, tuple is immutable
# ✔ dict stores key-value pairs
# ✔ set removes duplicate values
# ✔ None represents no value
# ✔ isinstance() is safer and recommended over type()
# ✔ Use type annotations for better code clarity
