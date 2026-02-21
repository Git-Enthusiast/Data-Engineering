# ============================================
# Python enumerate() – Complete Revision
# ============================================

# 1️⃣ What is enumerate()?
# ------------------------
# - enumerate() is a built-in function in Python.
# - It returns an iterator that produces pairs of (index, value) while iterating.
# - Useful when you need the index of each element along with the value.

# Syntax:
# enumerate(iterable, start=0)
# iterable → string, list, tuple, etc.
# start    → starting index (default = 0)

# --------------------------------------------
# 2️⃣ Example with String
# --------------------------------------------
myString = "Hello World"

# start=1 → indexing starts from 1
for i, j in enumerate(myString, start=1):
    print(i, j)

# Output:
# 1 H
# 2 e
# 3 l
# 4 l
# 5 o
# 6  
# 7 W
# 8 o
# 9 r
# 10 l
# 11 d

# --------------------------------------------
# 3️⃣ Example with List
# --------------------------------------------
myList = ["apple", "banana", "cherry"]

for index, fruit in enumerate(myList):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry

# --------------------------------------------
# 4️⃣ Example with Tuple
# --------------------------------------------
myTuple = ("apple", "banana", "cherry")

for index, fruit in enumerate(myTuple):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry

# --------------------------------------------
# 5️⃣ How enumerate() works internally
# --------------------------------------------
# Internal steps:
# 1. Initialize counter = start
# 2. Loop through iterable
# 3. Return (counter, element)
# 4. Increment counter by 1
# 5. Repeat until iterable ends

# Manual simulation:
counter = 0
for element in myList:
    print(counter, element)
    counter += 1

# With start=1:
counter = 1
for element in myList:
    print(counter, element)
    counter += 1

# --------------------------------------------
# 6️⃣ Custom implementation of enumerate()
# --------------------------------------------
def my_enumerate(iterable, start=0):
    counter = start
    for element in iterable:
        yield counter, element  # yield makes it an iterator
        counter += 1

# Test custom enumerate
for index, value in my_enumerate(myList, start=1):
    print(index, value)

# Output:
# 1 apple
# 2 banana
# 3 cherry

# --------------------------------------------
# 7️⃣ Why use enumerate()?
# --------------------------------------------
# ✅ Cleaner and more readable than using range(len(sequence))
# ✅ Works with any iterable: list, tuple, string, etc.
# ✅ start parameter allows flexible indexing

# Example without enumerate:
for i in range(len(myList)):
    print(i, myList[i])

# Example with enumerate (better):
for i, val in enumerate(myList):
    print(i, val)

# --------------------------------------------
# 8️⃣ Quick Summary
# --------------------------------------------
# - enumerate() → returns (index, value) pairs
# - Default index = 0, can use start parameter
# - Works with lists, tuples, strings
# - Can implement manually using a counter + loop + yield
# - Preferred method for clean and Pythonic code