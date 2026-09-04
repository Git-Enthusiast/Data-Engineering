
# ---------------------------------------------------------
# 8. VARIABLE SCOPE
# ---------------------------------------------------------

"""
Scope means the region where a variable is accessible.

Python uses LEGB rule.

L → Local
E → Enclosed
G → Global
B → Built-in
"""


# ---------------------------------------------------------
# LOCAL SCOPE EXAMPLE
# ---------------------------------------------------------
x = 20
def example_scope():
    x = 10  # local variable
    print("Inside function:", x)
print(x)

example_scope()

# print(x)   # This would cause an error because x is local

