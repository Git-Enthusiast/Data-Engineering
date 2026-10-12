text = "42"  # fix: use a string that can be converted
number = int(text)
print("The number is", number)

# Alternative: handle the bad value deliberately
bad_text = "hello"
try:
    print(int(bad_text))
except ValueError:
    print("That is not a whole number.")
