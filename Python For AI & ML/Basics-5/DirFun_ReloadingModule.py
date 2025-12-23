# dir() in Python:
# The dir() function is used to find out which names (variables, functions, classes, etc.) 
# are defined in a module or in the current scope.
# It returns a list of names in the current local scope or the attributes of the given object.
# Here What is means by Current Local Scope :
# let's take an example 
print(dir())    # Will give all the functions, class, attributes present in this file
print(dir())    # Will return only name as only name is present in the function 
                # itself
def demo():
    name = "Rajan"
    print(dir())    # Will return only name as only name is present in the function 
                    # itself
                    # it will return only ["name"]
# Example: 
import math
print(dir(math))  # This will print all the attributes and methods of the math module
# Output will include names like 'sin', 'cos', 'pi', etc.
# Example Output:
#['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 
# 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 
# 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 
# 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 
# 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 
# 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 
# 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 
# 'tau', 'trunc', 'ulp']

# You can also use dir() without any arguments to list the names in the current local scope
a = 10
b = 20
def my_function():
    pass
print(dir())  # This will print ['a', 'b', 'my_function', ...]
# Output will include 'a', 'b', 'my_function', etc.

# Other Example:
my_String = "Hello, World!"
print(type(my_String))  # Output: <class 'str'>
print(dir(my_String)) # This will print all the attributes and methods of the str class
# Output : 
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', 
# '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 
# 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
# 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
# 'upper', 'zfill']

# Some Other Examples:
my_List = [1, 2, 3, 4, 5]
print(dir(my_List))  # This will print all the attributes and methods of the list class
# Output :
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
# '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', 
# '__le__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

my_Dict = {'a': 1, 'b': 2, 'c': 3}
print(dir(my_Dict))  # This will print all the attributes and methods of the dict class
# Output :
# ['__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

my_Set = {1, 2, 3, 4, 5}
print(dir(my_Set))  # This will print all the attributes and methods of the set class
# Output:
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', 
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', 
#  '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', 
#  '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', 
#  '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', 
#  '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 
#  'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 
#  'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 
#  'symmetric_difference_update', 'union', 'update']

# Reloading Module in Python
# let a module be "exampleModule.py"
# which we import in this file now when we write " import exampleModule.py"
# It loads module only once even let say if written 5 times same 
# Statement in same code so, If we have to load same module multiple times we 
# have to use use "importlib" syntax is below:
# import importlib
# importlib.reload(module name which we have import)
# importlib.reload(module name which we have to import)
# To get list of all accessible module from a file or scope
# use print(help("modules"))
print(help("modules"))
