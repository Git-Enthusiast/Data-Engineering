"""
=====================================================================
        PYTHON FLOAT DATA TYPE – COMPLETE MASTER FILE (FINAL)
=====================================================================

📌 INTRODUCTION
---------------
A float (floating-point number) represents real numbers in Python.

Definition:
    A float is a number with a decimal point.

Examples:
    10.5
    -3.14
    0.0

It consists of:
    • Integer part
    • Decimal point
    • Fractional part

---------------------------------------------------------------------
📌 IMPORTANT CHARACTERISTICS
---------------------------------------------------------------------

1️⃣ Represents Real Numbers
    Used for measurements, scientific calculations, etc.

2️⃣ Stored Using IEEE 754 Double Precision (64-bit)
    • 1 bit → Sign
    • 11 bits → Exponent
    • 52 bits → Mantissa (Fraction)

3️⃣ Immutable Data Type
    When changed, a new object is created.

4️⃣ Boolean Behavior
    0.0 → False
    Non-zero → True

5️⃣ Precision Limitation
    Because floats are stored in binary,
    some decimal values cannot be represented exactly.

Example:
    0.1 + 0.2 ≠ exactly 0.3

---------------------------------------------------------------------
📌 EXPONENTIAL (SCIENTIFIC) NOTATION
---------------------------------------------------------------------

Format:
    aEb or aeb

Meaning:
    a × 10^b

Examples:
    2e3   → 2000.0
    3e-2  → 0.03

Useful for:
    • Very large numbers
    • Very small numbers

---------------------------------------------------------------------
📌 FLOAT CONSTRUCTOR – float()
---------------------------------------------------------------------

float() → 0.0
float(10) → 10.0
float("10.5") → 10.5
float("   25.5   ") → Handles spaces
float("\n15.2\t") → Handles escape characters

Invalid:
    float("abc") → ValueError

---------------------------------------------------------------------
📌 SPECIAL FLOAT VALUES
---------------------------------------------------------------------

1️⃣ Infinity
    float("inf")
    float("infinity")

2️⃣ Negative Infinity
    float("-inf")

3️⃣ Not-a-Number (NaN)
    float("nan")

---------------------------------------------------------------------
📌 LARGEST & SMALLEST FLOAT VALUES
---------------------------------------------------------------------

Python float follows IEEE 754 (64-bit double precision).

Largest float value:
    1.7976931348623157e+308

Smallest positive normalized float:
    2.2250738585072014e-308

You can check using:

    import sys
    sys.float_info.max
    sys.float_info.min

If you exceed maximum value:
    Result becomes → infinity (inf)

Example:
    1e309 → inf

---------------------------------------------------------------------
📌 IMPORTANT FLOAT METHODS
---------------------------------------------------------------------

1️⃣ as_integer_ratio()
    Returns two integers whose ratio equals the float.

    Example:
        7.5.as_integer_ratio()
        → (15, 2)

2️⃣ is_integer()
    Checks whether float represents whole number.

    Example:
        7.0.is_integer() → True
        7.2.is_integer() → False

3️⃣ hex()
    Converts float to hexadecimal string.

4️⃣ float.fromhex()
    Converts hexadecimal string back to float.

---------------------------------------------------------------------
📌 ARITHMETIC OPERATIONS
---------------------------------------------------------------------

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor division
%   Modulus
**  Power

---------------------------------------------------------------------
                        EXAMPLES
---------------------------------------------------------------------
"""

# ==============================================================
# BASIC FLOAT VALUES
# ==============================================================

a = 10.5
b = -3.14
c = 0.0

print("Basic Float Values:")
print(a, type(a))
print(b, type(b))
print(c, type(c))


# ==============================================================
# EXPONENTIAL REPRESENTATION
# ==============================================================

exp1 = 2e3
exp2 = 3e-2

print("\nScientific Notation:")
print("2e3 =", exp1)
print("3e-2 =", exp2)


# ==============================================================
# FLOAT CONSTRUCTOR
# ==============================================================

print("\nFloat Constructor Examples:")
print(float())
print(float(10))
print(float("10.5"))
print(float("   25.5   "))
print(float("\n15.2\t"))


# ==============================================================
# SPECIAL FLOAT VALUES
# ==============================================================

positive_inf = float("inf")
negative_inf = float("-inf")
nan_value = float("nan")

print("\nSpecial Float Values:")
print("Infinity:", positive_inf)
print("Negative Infinity:", negative_inf)
print("NaN:", nan_value)


# ==============================================================
# LARGEST & SMALLEST FLOAT VALUES
# ==============================================================

import sys

print("\nFloat Limits:")
print("Largest float:", sys.float_info.max)
print("Smallest positive float:", sys.float_info.min)

print("\nExceeding maximum:")
print("1e309 =", 1e309)


# ==============================================================
# FLOAT METHODS
# ==============================================================

num = 7.5

print("\nFloat Methods:")
print("as_integer_ratio():", num.as_integer_ratio())
print("is_integer() for 7.0:", (7.0).is_integer())
print("is_integer() for 7.2:", (7.2).is_integer())

hex_value = 1.2345.hex()
print("Hex representation:", hex_value)

converted_back = float.fromhex(hex_value)
print("Converted back from hex:", converted_back)


# ==============================================================
# IMMUTABILITY DEMONSTRATION
# ==============================================================

x = 5.5
print("\nBefore change:", x, id(x))
x = x + 1
print("After change:", x, id(x))


# ==============================================================
# BOOLEAN BEHAVIOR
# ==============================================================

print("\nBoolean Behavior:")

if 5.5:
    print("5.5 is True")

if not 0.0:
    print("0.0 is False")


# ==============================================================
# PRECISION ISSUE DEMONSTRATION
# ==============================================================

print("\nFloating Point Precision Example:")
print("0.1 + 0.2 =", 0.1 + 0.2)


"""
=====================================================================
                        FINAL SUMMARY
=====================================================================

✔ Float = Number with decimal point
✔ Uses IEEE 754 (64-bit double precision)
✔ Immutable data type
✔ Supports scientific notation (2e3, 3e-2)
✔ 0.0 → False, Non-zero → True
✔ float() converts values
✔ Supports Infinity & NaN
✔ Largest float ≈ 1.79e+308
✔ Smallest positive ≈ 2.22e-308
✔ Exceeding max → inf
✔ Precision limitations exist

=====================================================================
                    END OF MASTER FILE
=====================================================================
"""