# ============================================================
# PYTHON SPECIAL OPERATORS & MEMORY MODEL – COMPLETE REVISION
# ============================================================
# This file is a COMBINED + REFACTORED VERSION of:
# 1. Identity vs Equality & Memory Model (int, str, list, tuple)
# 2. Special Operators (Membership + Identity operators)
#
# Purpose:
# - Interview preparation
# - Conceptual clarity
# - Teaching & revision notes
# ============================================================

# ------------------------------------------------------------
# IMPORTANT TERMINOLOGY
# ------------------------------------------------------------
# ==   -> Value Equality (content comparison)
# is   -> Identity (memory address comparison)
# id() -> Returns identity (memory address) of an object
#
# IMMUTABLE TYPES  -> int, float, str, tuple
# MUTABLE TYPES    -> list, dict, set
#
# Rule:
# - Immutable objects MAY be reused by Python
# - Mutable objects are NEVER reused automatically


# ============================================================
# SECTION 1️⃣ : MEMBERSHIP OPERATORS (in, not in)
# ============================================================
# Membership operators are used to check whether a value
# exists inside a sequence or collection.
#
# Supported types:
# - string
# - list
# - tuple
# - set
# - dictionary (KEYS only by default)

# ------------------------------------------------------------
# 1.1 Membership Operator with LIST
# ------------------------------------------------------------
print("\n--- MEMBERSHIP OPERATOR : LIST ---")

my_list = [1, 2, 3, 4, 5]

# 'in' operator
is_in_list = 3 in my_list           # True, because 3 exists in the list
print("Is 3 in the list?", is_in_list)

is_not_in_list = 6 in my_list       # False, because 6 does not exist
print("Is 6 in the list?", is_not_in_list)

# 'not in' operator
is_not_in_list_neg = 6 not in my_list  # True, because 6 is absent
print("Is 6 not in the list?", is_not_in_list_neg)


# ------------------------------------------------------------
# 1.2 Membership Operator with STRING
# ------------------------------------------------------------
print("\n--- MEMBERSHIP OPERATOR : STRING ---")

my_string = "Hello, World!"

is_in_string = 'H' in my_string     # True, character exists in string
print("Is 'H' in the string?", is_in_string)


# ------------------------------------------------------------
# 1.3 Membership Operator with DICTIONARY (TRICKY)
# ------------------------------------------------------------
# IMPORTANT:
# - 'in' checks ONLY KEYS in dictionary
# - It does NOT check values

print("\n--- MEMBERSHIP OPERATOR : DICTIONARY ---")

my_dict = {'a': 100, 'b': 200, 'c': 300}

# Key checking (default behavior)
is_key_in_dict = 'a' in my_dict      # True, 'a' is a key
print("Is 'a' a key in the dictionary?", is_key_in_dict)

# Value checking (WRONG assumption)
is_value_in_dict = 100 in my_dict    # False, values are NOT checked
print("Is 100 a key in the dictionary?", is_value_in_dict)

# Correct way to check values
is_value_in_dict_values = 100 in my_dict.values()  # True
print("Is 100 a value in the dictionary?", is_value_in_dict_values)


# ------------------------------------------------------------
# 1.4 Tricky Membership Example
# ------------------------------------------------------------
print("\n--- TRICKY MEMBERSHIP EXAMPLES ---")

lst = [10, 20, 30, 40, 50]

print(lst in lst)   # False -> list is not an element of itself
print(20 in lst)    # True  -> 20 is an element


# ============================================================
# SECTION 2️⃣ : IDENTITY OPERATORS (is, is not)
# ============================================================
# Identity operators compare MEMORY LOCATION, not values
# Internally compares id(object)

# ------------------------------------------------------------
# 2.1 Identity Operator with LIST (Mutable)
# ------------------------------------------------------------
print("\n--- IDENTITY OPERATOR : LIST ---")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# a is b -> id(a) == id(b)?
print("a is b:", a is b)    # False, different list objects
print("a is c:", a is c)    # True, same reference

# 'is not' operator
print("a is not b:", a is not b)  # True
print("a is not c:", a is not c)  # False


# ------------------------------------------------------------
# 2.2 Identity vs Equality (Mutable Objects)
# ------------------------------------------------------------
print("\n--- MUTABLE OBJECT COMPARISON ---")

list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()

print("list1 is list2:", list1 is list2)   # True, same object
print("list1 is list3:", list1 is list3)   # False, new object
print("list1 == list3:", list1 == list3)   # True, same content

# NOTE:
# - copy() creates a NEW object
# - content may be same, identity is different


# ============================================================
# SECTION 3️⃣ : IMMUTABLE OBJECTS & MEMORY REUSE
# ============================================================

# ------------------------------------------------------------
# 3.1 Integer (IMMUTABLE + CACHING)
# ------------------------------------------------------------
print("\n--- INTEGER : IMMUTABLE + CACHING ---")

i1 = 10
i2 = 10

print(i1 == i2)   # True
print(i1 is i2)   # True (cached integer)
print(id(i1), id(i2))

# Python caches small integers (usually -5 to 256)


# ------------------------------------------------------------
# 3.2 String (IMMUTABLE + INTERNING)
# ------------------------------------------------------------
print("\n--- STRING : IMMUTABLE + INTERNING ---")

str1 = "hello"
str2 = "hello"

print("str1 is str2:", str1 is str2)   # True (interned string)

# Runtime string creation (no interning)
str3 = "".join(["h", "e", "l", "l", "o"])

print("str1 is str3:", str1 is str3)   # False
print("str1 == str3:", str1 == str3)   # True


# ------------------------------------------------------------
# 3.3 Tuple (IMMUTABLE but NOT GUARANTEED TO BE REUSED)
# ------------------------------------------------------------
print("\n--- TUPLE : IMMUTABLE ---")

t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(t1 == t2)   # True
print(t1 is t2)   # May be True (implementation dependent)

# Runtime tuple creation
t3 = tuple([1, 2, 3])
t4 = tuple([1, 2, 3])

print(t3 is t4)   # False


# ============================================================
# SECTION 4️⃣ : BEST PRACTICES (INTERVIEW GOLD)
# ============================================================

# 1. Use '==' for VALUE comparison
# 2. Use 'is' for IDENTITY comparison
# 3. NEVER use 'is' for value comparison
# 4. ALWAYS use 'is None' for None checks

x = None
print(x is None)   # Correct way

# ============================================================
# END OF COMBINED REVISION FILE
# ============================================================
