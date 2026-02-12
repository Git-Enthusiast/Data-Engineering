#   Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.

print('''Please Enter number to get sum of it 
        and press "x" if you want to quit ''')
total_sum = 0
while True:
    user_input = input("Enter a number or 'x' to quit: ")
    
    if user_input.lower() == 'x':
        break
    
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a valid number or 'x'.")

print(f"The sum of all entered numbers is: {total_sum}")