x = 10
print("Integer Example:")
print(f"Initial ID of x: {id(x)}")
x  = x+1
print(f"New Value of x: {x}")
print(f"New ID of x: {id(x)}")
print("-" * 20)

y = 10.5
print("Float Example:")
print(f"Initial ID of y: {id(y)}")
y = y + 1.1
print(f"New Value of y: {y}")
print(f"New ID of y: {id(y)}")
print("-" * 20)

z = "Hello"
print("String Example:")
print(f"Initial ID of z: {id(z)}")
z = z + " World"
print(f"New Value of z: {z}")
print(f"New ID of z: {id(z)}")