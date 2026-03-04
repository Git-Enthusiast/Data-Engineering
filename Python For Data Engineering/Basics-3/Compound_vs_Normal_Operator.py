"""
===========================================================
Topic: Why `a += b` is NOT always equal to `a = a + b`
===========================================================

This file demonstrates the difference between:

    1️⃣  Compound Operator  ->  a += b
    2️⃣  Normal Assignment  ->  a = a + b

The behavior differs based on:
    ✔ Immutable Data Types  (int, str, tuple)
    ✔ Mutable Data Types    (list, set, dict)

Key Internal Difference:
    a += b      -> Calls __iadd__()  (In-place addition)
    a = a + b   -> Calls __add__()   (Creates new object)

Let’s understand with examples.
"""

print("\n==============================")
print("IMMUTABLE DATA TYPE (INTEGER)")
print("==============================")

a = 10
print("Initial value of a:", a)
print("Initial memory address of a:", id(a))

a += 5
print("\nAfter a += 5")
print("Value of a:", a)
print("Memory address of a:", id(a))

"""
Observation:
Even though we used +=, a new object is created.
Because integers are IMMUTABLE.
"""

print("\nResetting a to 10...\n")

a = 10
print("Initial memory address of a:", id(a))

a = a + 5
print("\nAfter a = a + 5")
print("Value of a:", a)
print("Memory address of a:", id(a))

"""
Conclusion for Immutable Types:
Both `a += b` and `a = a + b` create a NEW object.
Memory address changes in both cases.
They behave the SAME.
"""



print("\n\n==============================")
print("MUTABLE DATA TYPE (LIST)")
print("==============================")

list1 = [1, 2, 3]
print("Original list:", list1)
print("Original memory address:", id(list1))

print("\nUsing normal assignment: list1 = list1 + [4, 5]")

list1 = list1 + [4, 5]
print("Updated list:", list1)
print("Memory address after + :", id(list1))

"""
Observation:
A NEW list is created.
Memory address changes.
Original object is NOT modified in-place.
"""



print("\nResetting list...\n")

list2 = [1, 2, 3]
print("Original list:", list2)
print("Original memory address:", id(list2))

print("\nUsing compound operator: list2 += [4, 5]")

list2 += [4, 5]
print("Updated list:", list2)
print("Memory address after += :", id(list2))

"""
Observation:
Memory address stays the SAME.
The original list is modified IN-PLACE.
No new object is created.
"""



print("\n\n========================================")
print("IMPORTANT REAL-WORLD SIDE EFFECT")
print("========================================")

a = [1, 2, 3]
b = a   # Both variables refer to same list

print("Initial a:", a)
print("Initial b:", b)

print("\nUsing a += [4]")

a += [4]

print("After modification:")
print("a:", a)
print("b:", b)

"""
Because += modifies the list in-place,
'b' also gets affected!

This can cause unexpected bugs in real projects.
"""



print("\n\n========================================")
print("WHY DOES THIS HAPPEN?")
print("========================================")

"""
Internally Python calls:

    a += b      ->  a.__iadd__(b)   (In-place add)
    a = a + b   ->  a.__add__(b)    (Normal add)

Mutable objects (like list) implement __iadd__
to modify the same object.

Immutable objects (like int, str, tuple)
cannot modify themselves, so they create a new object.
"""



print("\n\n========================================")
print("FINAL KEY TAKEAWAY")
print("========================================")

"""
✔ For IMMUTABLE types:
    a += b  ≈  a = a + b   (both create new object)

✔ For MUTABLE types:
    a += b  modifies object in-place
    a = a + b  creates new object

Therefore:
They are NOT always equivalent.
Be careful when working with mutable objects!
"""

print("\n✅ End of Demonstration")