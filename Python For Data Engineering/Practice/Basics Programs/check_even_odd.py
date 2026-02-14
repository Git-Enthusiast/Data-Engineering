number = int(input("Please enter a number: "))

if number == 0:
    print("0 is even and it is zero.")
else:
    sign = "positive" if number > 0 else "negative"
    parity = "even" if number % 2 == 0 else "odd"
    print(f"{number} is a {sign} {parity} number.")
