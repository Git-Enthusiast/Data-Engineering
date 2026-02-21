#   Take integer inputs till the user enters 0 and print the sum of all numbers

total_sum = 0

while True:
    try:
        number = int(input("Enter an integer (0 to exit): "))
        
        if number == 0:
            print("Successfully Exit.")
            break
        
        total_sum += number

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

print(f"The sum of the entered integers is: {total_sum}")