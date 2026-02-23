# What is Function in Python?
# A function is a block of reusable code that performs a specific task.
# Functions help in organizing code, improving readability, and avoiding redundancy.
# In Python, functions are defined using the 'def' keyword followed by the function name and parentheses.
def greet(name):
    """
    This function takes a name as input
    and prints a greeting message.
    """
    print(f"Hello, {name}! Welcome to Python functions.")

# Calling the function with an argument
greet("Rajan")

# Functions can also return values using the 'return' statement.
def multiply(x, y): # Here in function definition x,y is called formal parameter
    """
    This function takes two numbers as input
    and returns their product.
    """
    return x * y
result = multiply(4, 5) # Here in function call 4,5 is called actual parameter which positional arguments. 
print(f"The product is: {result}")

# Functions can have default parameter values
def power(base, exponent=2):
    """
    This function raises the base to the power of exponent.
    If exponent is not provided, it defaults to 2 (square).
    """
    return base ** exponent
squared_value = power(3)
cubed_value = power(3, 3)
print(f"3 squared is: {squared_value}")
print(f"3 cubed is: {cubed_value}")

# Functions can also accept variable number of arguments using *args and **kwargs
def display_info(*args, **kwargs):
    """
    This function accepts any number of positional and keyword arguments
    and displays them.
    """
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
display_info(1, 2, 3, name="Rajan", age=25)

# This is a brief overview of functions in Python.
# Functions are a fundamental building block in Python programming.
# They allow you to encapsulate logic, making your code modular and easier to maintain.
# You can define your own functions or use built-in functions provided by Python.
# Remember to always document your functions using docstrings for better understanding.
# Functions can also be nested, meaning you can define a function inside another function.

def outer_function(msg):
    """
    This is the outer function that takes a message as input.
    """
    def inner_function():
        """
        This is the inner function that prints the message from the outer function.
        """
        print(msg)
    inner_function()
outer_function("Hello from the outer function!")

# This concludes the introduction to functions in Python.
# Functions are ignored by the Python interpreter
# Functions are "ignored" in the sense that their code is not executed until they are explicitly called.
# They are meant for humans to read and understand the code better

