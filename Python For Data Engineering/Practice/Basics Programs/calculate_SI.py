#   Write a program to input principal, time, and rate (P, T, R) 
#   from the user and find Simple Interest.

# SI = (P*R*T) / 100

# Program to calculate Simple Interest

# SI = (P * R * T) / 100

while True:
    choice = input('If you want to calculate SI enter "yes" or enter "x" to exit: ').lower()

    if choice.lower() == "yes":
        principal_amount = float(input("Please enter Principal amount: "))
        rate_of_interest = float(input("Please enter Rate of Interest: "))
        time_period = float(input("Please enter Time period (in years): "))

        si = (principal_amount * rate_of_interest * time_period) / 100
        print(f"Your Total Simple Interest is: {si}\n")

    elif choice.lower() == "x":
        print("Program exited successfully.")
        break

    else:
        print("Invalid input! Please enter only 'yes' or 'x'.\n")
