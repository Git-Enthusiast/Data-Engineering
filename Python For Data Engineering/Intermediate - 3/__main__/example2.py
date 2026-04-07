import example1
print(example1.add(2,3))

# List all names in current scope
print("All names in current scope:", dir())

# Check specifically if __name__ is present
if '__name__' in dir():
    print("__name__ exists in this scope")
    print("Its value is:", __name__)

# Define a function
def greet():
    return "Hello!"

# Check after defining a function
print("After defining function, names in scope:", dir() ,end= "\n")

"""

After defining function, names in scope: ['__builtins__', '__cached__',
 '__doc__', '__file__', '__loader__', '__name__', '__package__',
  '__spec__', 'example1', 'greet']

"""
"""

from example1 import add    # by using this way of import add 
                            # comes directly into current global scope
print(add(2, 3))  # Now add is in current scope

"""