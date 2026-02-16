#   Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)
while True:
    choice = input('Please Enter "yes" if you want to use arithmetic operation or "x" to exit: ').lower()

    if choice == "yes":
        num1 = float(input("Please Enter 1st number: "))
        num2 = float(input("Please Enter 2nd number: "))
        operation = input("Please Enter the Operator (+ - * / %): ").strip()

        if operation == "+":
            print(f"The sum of {num1} and {num2} is: {num1 + num2}")
        elif operation == "-":
            print(f"The subtraction of {num1} and {num2} is: {num1 - num2}")
        elif operation == "*":
            print(f"The product of {num1} and {num2} is: {num1 * num2}")
        elif operation == "/":
            if num2 == 0:
                print("Invalid value for denominator. It can't be zero.")
            else:
                print(f"The division of {num1} and {num2} is: {num1 / num2}")
        elif operation == "%":
            print(f"The modulus of {num1} and {num2} is: {num1 % num2}")
        else:
            print("Invalid Operation! Please enter only + - * / %")

    elif choice == "x":
        print("Program exited successfully.")
        break

    else:
        print('Invalid Input! Please enter "yes" or "x".')
