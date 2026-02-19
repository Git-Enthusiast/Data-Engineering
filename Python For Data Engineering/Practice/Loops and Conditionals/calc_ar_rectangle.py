#   Program to calculate area of rectangleca
def calculate_area_rectangle(length, width):
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = calculate_area_rectangle(length, width)

print("Area of Rectangle =", area)
