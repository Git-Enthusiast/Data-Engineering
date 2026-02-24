#    Print talbe of number until user enters no

while True:
    
    if ((choice := input("Please Enter 'yes' to calculate table 'no' to exit: ").lower()) == "yes"):
        try:
            number = int(input("Please Enter an integer to get it's table:"))
            for i in range(1,11):
                print(f"{number} * {i} = {number*i}")
        except ValueError:
             print("Invalid input! Please enter a valid integer.")
    elif choice == "no":
        print("Exit Successfully")
        break
    else:
        print("Please enter only 'yes' or 'no'")


     