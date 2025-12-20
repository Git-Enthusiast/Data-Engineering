# ============================================================
#        PYTHON OPERATOR PRECEDENCE & ASSOCIATIVITY
# ============================================================
# Revision Notes + Coding Reference
#
# Python follows a strict order while evaluating expressions.
# This order is controlled by:
#   1️⃣ Operator Precedence  → Which operator executes first
#   2️⃣ Associativity        → Direction of evaluation when
#                              operators have SAME precedence
# ============================================================


# ============================================================
# 🔢 OPERATOR PRECEDENCE (HIGHEST → LOWEST)
# ============================================================
#  1️⃣ Parentheses                     ( )
#  2️⃣ Exponentiation                  **
#  3️⃣ Unary Operators                 +  -  ~
#  4️⃣ Multiplication / Division       *  /  //  %
#  5️⃣ Addition / Subtraction          +  -
#  6️⃣ Bitwise Shift                   <<  >>
#  7️⃣ Bitwise AND                     &
#  8️⃣ Bitwise XOR                     ^
#  9️⃣ Bitwise OR                      |
# 🔟 Comparison / Identity / Membership == != < > <= >=
# 11️⃣ Logical NOT                     not
# 12️⃣ Logical AND                     and
# 13️⃣ Logical OR                      or
# 14️⃣ Assignment Expression           :=
#
# Rule:
# Operators with HIGHER precedence execute FIRST
# ============================================================


# ============================================================
# 🔁 OPERATOR ASSOCIATIVITY
# ============================================================
# Associativity decides the direction of evaluation when
# multiple operators of SAME precedence appear.
#
# ➤ LEFT-ASSOCIATIVE (Most operators)
#   Evaluation happens from LEFT → RIGHT
#
# ➤ RIGHT-ASSOCIATIVE
#   Evaluation happens from RIGHT → LEFT
#
# NOTE:
# The exponentiation operator (**) is RIGHT-associative
# ============================================================


# ============================================================
# 1️⃣ PARENTHESES (HIGHEST PRECEDENCE)
# ============================================================
# Expressions inside parentheses are evaluated FIRST

expr_parentheses = (3 + 4) * 2

# Step-by-step:
# (3 + 4) = 7
# 7 * 2 = 14

print("Parentheses Example:", expr_parentheses)


# ============================================================
# 2️⃣ EXPONENTIATION OPERATOR (**)
# ============================================================
# Exponentiation has HIGH precedence
# It is RIGHT-ASSOCIATIVE

expr_exponent = 2 ** 3 ** 2

# Evaluation order:
# 3 ** 2 = 9
# 2 ** 9 = 512

print("Exponentiation Example (2 ** 3 ** 2):", expr_exponent)


# ============================================================
# 3️⃣ UNARY OPERATORS (+, -, ~)
# ============================================================
# Unary operators apply to a SINGLE operand

x = 5

expr_unary_plus = +x     # Positive value
expr_unary_minus = -x    # Negative value
expr_unary_not = ~x      # Bitwise NOT → -(x + 1)

print("Unary +x:", expr_unary_plus)
print("Unary -x:", expr_unary_minus)
print("Unary ~x:", expr_unary_not)


# ============================================================
# 4️⃣ MULTIPLICATION, DIVISION, MODULO
# ============================================================
# These operators have higher precedence than + and -

expr_mul_div = 3 + 4 * 2

# Evaluation:
# 4 * 2 = 8
# 3 + 8 = 11

print("Multiplication Precedence Example:", expr_mul_div)


# ============================================================
# 5️⃣ ADDITION AND SUBTRACTION (LEFT-ASSOCIATIVE)
# ============================================================
# Evaluated from LEFT → RIGHT

expr_add_sub = 10 - 4 + 2

# Evaluation:
# 10 - 4 = 6
# 6 + 2 = 8

print("Addition/Subtraction Associativity:", expr_add_sub)


# ============================================================
# 6️⃣ BITWISE SHIFT OPERATORS (<<, >>)
# ============================================================

expr_shift = 8 >> 1 + 1

# Evaluation:
# 1 + 1 = 2   (addition first)
# 8 >> 2 = 2

print("Bitwise Shift Example:", expr_shift)


# ============================================================
# 7️⃣ BITWISE AND (&), XOR (^), OR (|)
# ============================================================
# Precedence order:
# &  >  ^  >  |

expr_bitwise = 5 & 3 | 2

# Step-by-step:
# 5 & 3 = 1
# 1 | 2 = 3

print("Bitwise Precedence Example:", expr_bitwise)


# ============================================================
# 8️⃣ COMPARISON OPERATORS
# ============================================================
# Comparisons have lower precedence than arithmetic

expr_comparison = 10 + 5 > 12

# Evaluation:
# 10 + 5 = 15
# 15 > 12 → True

print("Comparison Example:", expr_comparison)


# ============================================================
# 9️⃣ LOGICAL OPERATORS (not, and, or)
# ============================================================
# Precedence:
# not > and > or

expr_logical = not False and True or False

# Step-by-step:
# not False = True
# True and True = True
# True or False = True

print("Logical Operators Precedence Example:", expr_logical)


# ============================================================
# 🔟 WALRUS OPERATOR (:=)
# ============================================================
# Assignment inside expressions

if (n := len("Python")) > 5:
    print("Walrus Operator Example: Length =", n)


# ============================================================
# ✅ FINAL REVISION SUMMARY
# ============================================================
# ✔ Parentheses override precedence
# ✔ Exponentiation is RIGHT-associative
# ✔ Most operators are LEFT-associative
# ✔ Arithmetic > Bitwise > Comparison > Logical
# ✔ Use parentheses for clarity and readability
# ============================================================
