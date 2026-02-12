# Calculate HCF and LCM of given two numbers
a = int(input("Please Enter 1st Number: "))
b = int(input("Please Enter 2nd Number: "))

# Take absolute value of the numbers
a = abs(a)
b = abs(b)

# Check if either number is 0
if a == 0 or b == 0:
    print("HCF is", max(a, b))
    print("LCM is 0")
else:
    dividend = max(a,b)
    divisor = min(a,b)
    remainder = dividend % divisor

    while(remainder != 0):
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor
    
    HCF = divisor
    LCM = (a * b) // HCF    # // is integer divison it gives integer value

    print(f"The LCM of {a} and {b} is {LCM}")
    print(f"The HCF of {a} and {b} is {HCF}")