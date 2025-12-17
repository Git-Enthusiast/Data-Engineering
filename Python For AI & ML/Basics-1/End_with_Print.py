# By default, Python's print() function appends a newline 
# character (`\n`) after each output, automatically moving 
# the cursor to the next line for subsequent print statements.
# This behavior is hardcoded as the default value `end='\n'` 
# in the print() function signature.

# However, you can customize this behavior by using the `end`
# parameter of the print() function. By specifying a different

# Use Case 1: Printing on the Same Line with Spaces

print("Hello,", end=" ")
print("World!")

# Use Case 2: Printing Without Any Separator (Empty `end`)

print("H", end="")
print("e", end="")
print("l", end="")
print("l", end="")
print("o")

# Use Case 3: Loop Printing with Comma Separator

for i in range(5):
    print(i, end=", ")
print()  # To move to the next line after the loop

# Use Case 4: To use any custom Character as 'end' value

print("Item 1", end=" - ")
print("Item 2", end=" - ")
print("Item 3")

# Use Case 5: Tab Separators for Aligned Columns

print("Name", end="\t")
print("Age", end=" \t")
print("City")

# Use Case 6: Progress Bar Simulation

for  i  in range(10):
     print(f"\rProgress: {i}%", end="")
     print ("Done!")
     
     
# USe Case 7: CSV-Livke Output

data = [["Name", "Age", "City"], ["Alice", "25", "NYC"], ["Bob", "30", "LA"]]
for row in data:    
    for item in row:
        print(item, end=",")
    print()  # Newline for next row

    
    
