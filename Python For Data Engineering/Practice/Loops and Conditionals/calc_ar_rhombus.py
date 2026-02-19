# ==========================================
# AREA OF RHOMBUS
# ==========================================

# A rhombus is a quadrilateral in which:
# - All four sides are equal in length.
# - Opposite sides are parallel.
# - Opposite angles are equal.
# - Diagonals bisect each other at right angles.

# There are two common formulas for area:

# 1️⃣ Using diagonals:
# Let d1 = length of first diagonal
# Let d2 = length of second diagonal
# Formula: Area = (d1 * d2) / 2

# 2️⃣ Using base and height:
# Let base = any side
# Let height = perpendicular distance from base to opposite side
# Formula: Area = base * height

# ==========================================
# Method 1: Using Diagonals
# ==========================================

d1 = float(input("Enter first diagonal length: "))
d2 = float(input("Enter second diagonal length: "))

area = 0.5 * d1 * d2

print("Area of Rhombus (using diagonals) =", area)

# ==========================================
# Method 2: Using Base and Height
# ==========================================

base = float(input("Enter side (base) length: "))
height = float(input("Enter height (perpendicular) length: "))

area2 = base * height

print("Area of Rhombus (using base and height) =", area2)
