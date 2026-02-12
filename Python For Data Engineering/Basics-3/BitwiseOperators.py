# ============================================================
#               PYTHON BITWISE OPERATORS
# ============================================================
# Revision Notes + Coding Reference
#
# Bitwise operators work at the **bit level**
# and are applied to integer values.
#
# They directly manipulate binary representations (0s and 1s).
#
# ------------------------------------------------------------
# Types of Bitwise Operators:
# ------------------------------------------------------------
# a) Bitwise Logical Operators
#   1️⃣ &   → Bitwise AND
#   2️⃣ |   → Bitwise OR
#   3️⃣ ^   → Bitwise XOR
#   4️⃣ ~   → Bitwise NOT
#
# b) Bitwise Shift Operators
#   5️⃣ <<  → Left Shift
#   6️⃣ >>  → Right Shift
# ============================================================


# ============================================================
# BINARY REPRESENTATION (REFERENCE)
# ============================================================
# Decimal → Binary
# 5  → 0101
# 3  → 0011
# ============================================================

a = 5   # Binary: 0101
b = 3   # Binary: 0011


# ============================================================
# 1️⃣ BITWISE AND OPERATOR (&)
# ============================================================
# Rule:
# 1 & 1 → 1
# 1 & 0 → 0
# 0 & 1 → 0
# 0 & 0 → 0
#
# Operation:
#   0101
# & 0011
# --------
#   0001  → 1 (decimal)
# ============================================================

result_and = a & b
print(f"Bitwise AND of {a} & {b} = {result_and}")


# ============================================================
# 2️⃣ BITWISE OR OPERATOR (|)
# ============================================================
# Rule:
# 1 | 1 → 1
# 1 | 0 → 1
# 0 | 1 → 1
# 0 | 0 → 0
#
# Operation:
#   0101
# | 0011
# --------
#   0111  → 7 (decimal)
# ============================================================

result_or = a | b
print(f"Bitwise OR of {a} | {b} = {result_or}")


# ============================================================
# 3️⃣ BITWISE XOR OPERATOR (^)
# ============================================================
# Rule:
# 1 ^ 1 → 0
# 1 ^ 0 → 1
# 0 ^ 1 → 1
# 0 ^ 0 → 0
#
# Operation:
#   0101
# ^ 0011
# --------
#   0110  → 6 (decimal)
# ============================================================

result_xor = a ^ b
print(f"Bitwise XOR of {a} ^ {b} = {result_xor}")


# ============================================================
# 4️⃣ BITWISE NOT OPERATOR (~)
# ============================================================
# The '~' operator flips every bit:
# 0 → 1
# 1 → 0
#
# Important:
# Python uses **2's complement representation** for integers.
#
# Formula:
# ~x = -(x + 1)
#
# Example:
# a = 5
# ~5 = -(5 + 1) = -6
#
# Binary (conceptual):
#   00000101
# → 11111010  → -6
# ============================================================

result_not = ~a
print(f"Bitwise NOT of ~{a} = {result_not}")


# ============================================================
# 5️⃣ BITWISE LEFT SHIFT OPERATOR (<<)
# ============================================================
# The '<<' operator shifts bits to the LEFT.
# New bits on the right are filled with 0.
# a << n → Shift the binary bits of a to the left by n positions
# Effect: Multiply a by 2ⁿ
# Formula: x << n = x * (2 ** n)
# Example: 5 << 1 = 10 (binary: 0101 → 1010)
# Example: 5 << 2 = 20 (binary: 0101 → 10100)
# ============================================================

result_left_shift = a << 1
print(f"Bitwise Left Shift of {a} << 1 = {result_left_shift}")


# ============================================================
# 6️⃣ BITWISE RIGHT SHIFT OPERATOR (>>)
# ============================================================
# The '>>' operator shifts bits to the RIGHT.
# Bits lost on the right are discarded.
# a >> n → Shift the binary bits of a to the right by n positions
# Effect: Divide a by 2ⁿ
# Formula: x >> n = x // (2 ** n)
# Example: 5 >> 1 = 2 (binary: 0101 → 0010)
# Example: 5 >> 2 = 1 (binary: 0101 → 0001)
# ============================================================

result_right_shift = a >> 1
print(f"Bitwise Right Shift of {a} >> 1 = {result_right_shift}")
# = 0010 → 2

# ============================================================
# ✅ KEY TAKEAWAYS (REVISION POINTS)
# ============================================================
# ✔ Bitwise operators work on binary digits (bits)
# ✔ '&'  → AND
# ✔ '|'  → OR
# ✔ '^'  → XOR
# ✔ '~'  → NOT (2's complement)
# ✔ '<<' → Multiply by powers of 2
# ✔ '>>' → Divide by powers of 2
# ============================================================
