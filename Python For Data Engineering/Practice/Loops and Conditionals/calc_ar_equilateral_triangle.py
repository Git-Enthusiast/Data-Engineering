# ==========================================
# AREA OF EQUILATERAL TRIANGLE
# ==========================================

# An equilateral triangle is a triangle in which:
# - All three sides are equal in length.
# - All three angles are 60 degrees.

# Let:
# side = length of one side of the triangle

# Formula for area:
# Area = (√3 / 4) * side^2

# ==========================================
# Python Program
# ==========================================

import math

# Input from user
side = float(input("Enter side of equilateral triangle: "))

# Calculate area
area = (math.sqrt(3) / 4) * side**2

# Output
print("Area of Equilateral Triangle =", area)
