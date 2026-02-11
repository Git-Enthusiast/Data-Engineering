# Write a program to print multiplication table

number = int(input("Please Enter the number to get its table:"))
for i in range(10):
    print(f"{number} * {i + 1} = {number*(i+1)}")