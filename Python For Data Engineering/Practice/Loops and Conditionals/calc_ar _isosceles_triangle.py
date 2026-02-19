# ==========================================
# AREA OF ISOSCELES TRIANGLE
# ==========================================

# An isosceles triangle is a triangle in which:
# - Two sides are equal in length.
# - The third side is called the base.
# - The angles opposite the equal sides are equal.

# Let:
# a = equal side length
# b = base of the triangle

# If height (h) is given:
# Area = (1/2) * base * height

# If only equal sides (a) and base (b) are given:
# First, find height using Pythagoras theorem.

# Since the height divides the base into two equal parts:
# Half base = b / 2

# Using Pythagoras theorem:
# h = √(a² - (b/2)²)

# Then area:
# Area = (1/2) * b * h

# ==========================================
# Program: Equal sides and Base given
# ==========================================

import math

a = float(input("Enter equal side length: "))
b = float(input("Enter base length: "))

# Calculate height
height = math.sqrt(a**2 - (b/2)**2)

# Calculate area
area = 0.5 * b * height

print("Height of triangle =", height)
print("Area of Isosceles Triangle =", area)
