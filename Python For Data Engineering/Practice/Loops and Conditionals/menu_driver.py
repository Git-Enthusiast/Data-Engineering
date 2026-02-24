while True:
    # Take two numbers safely
    try:
        num1 = int(input("Please Enter 1st number: "))
        num2 = int(input("Please Enter 2nd number: "))
    except ValueError:
        print("Please enter valid integers only.\n")
        continue

    # Show menu
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Modulus")

    operation_choice = input("Choose from above (1-5): ").strip()

    if operation_choice == "1":
        print(f"Addition is {num1 + num2}")
    elif operation_choice == "2":
        print(f"Subtraction is {num1 - num2}")
    elif operation_choice == "3":
        if num2 == 0:
            print("Zero Division Error.")
        else:
            print(f"Division is {num1 / num2}")
    elif operation_choice == "4":
        print(f"Multiplication is {num1 * num2}")
    elif operation_choice == "5":
        print(f"Modulus is {num1 % num2}")
    else:
        print("Please choose a valid option (1-5).")
        continue  # Ask numbers again

    # Ask user to continue
    choice = input("\nDo you want to continue? (y/n): ").lower()
    if choice == "n":
        print("Exit Successfully.")
        break
    elif choice != "y":
        print("Invalid input. Exiting.")
        break