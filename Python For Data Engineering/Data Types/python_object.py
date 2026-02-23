Perfect Rajan 🔥
Now we go **core CS + interview-level**:

# 🔬 Python Object Model — “Everything is an Object”

This is **one of the most important Python concepts**.

---

# 1️⃣ What Does “Everything is an Object” Mean?

In Python:

* Numbers are objects
* Strings are objects
* Functions are objects
* Classes are objects
* Even `None`, `True`, `False` are objects
* Even classes themselves are objects

Proof:

```python
print(type(10))
print(type("hello"))
print(type(True))
print(type(None))
```

Output:

```
<class 'int'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
```

Everything has:

* A type
* A memory address
* Methods
* Attributes

---

# 2️⃣ What is an Object Internally?

In Python, every object has:

1. **Identity** → memory address
2. **Type** → what kind of object
3. **Value** → the data it holds

You can check:

```python
x = 10

print(id(x))      # Identity
print(type(x))    # Type
print(x)          # Value
```

---

# 3️⃣ Identity (`id()`)

```python
a = 100
b = 100

print(a is b)
```

For small integers → True (optimization)

Python caches small integers (-5 to 256).

But:

```python
a = 1000
b = 1000

print(a is b)   # Might be False
```

Because new objects may be created.

---

# 4️⃣ Python Memory Structure (Simplified)

Every Python object internally contains:

```
---------------------------------
| Reference Count               |
| Type Pointer                  |
| Actual Value Data             |
---------------------------------
```

In CPython (C structure):

```c
typedef struct {
    PyObject_HEAD
} PyObject;
```

Every object begins with:

* Reference count
* Pointer to its type

---

# 5️⃣ Everything Inherits from `object`

Proof:

```python
print(int.__mro__)
print(str.__mro__)
print(bool.__mro__)
```

Output shows:

```
(<class 'int'>, <class 'object'>)
```

So hierarchy:

```
object
   ↑
int
   ↑
bool
```

The base of everything is:

```python
object
```

---

# 6️⃣ Functions Are Objects Too

```python
def greet():
    print("Hello")

print(type(greet))
```

Output:

```
<class 'function'>
```

You can assign:

```python
x = greet
x()
```

Functions can:

* Be passed as arguments
* Be returned from functions
* Stored in variables

This is called:

> First-Class Functions

---

# 7️⃣ Classes Are Also Objects

```python
class Person:
    pass

print(type(Person))
```

Output:

```
<class 'type'>
```

Important:

Classes are created by `type`.

And even `type` itself:

```python
print(type(type))
```

Output:

```
<class 'type'>
```

Mind-blowing fact:

```
type is instance of type
```

---

# 8️⃣ The Meta-Level

This is the deep part.

```python
print(type(int))
```

Output:

```
<class 'type'>
```

So:

* `int` is an object
* Created by `type`
* `type` is also an object
* And is instance of itself

Hierarchy:

```
object
   ↑
type
   ↑
int, str, list, etc.
```

---

# 9️⃣ Mutability in Object Model

Objects can be:

### Immutable:

* int
* float
* bool
* str
* tuple

Changing them → creates new object.

### Mutable:

* list
* dict
* set

Example:

```python
x = [1, 2]
print(id(x))

x.append(3)
print(id(x))   # Same ID
```

---

# 🔟 Variable Is NOT the Object

Important concept:

Variables are just **references (labels)**.

```python
x = 10
```

Means:

```
x → points to object 10
```

Reassignment:

```python
x = 20
```

Now:

```
x → points to new object 20
```

Old object may be garbage collected.

---

# 1️⃣1️⃣ Reference Counting

Python uses:

> Reference Counting + Garbage Collection

Every object tracks how many references point to it.

Example:

```python
import sys

x = 10
print(sys.getrefcount(x))
```

When ref count becomes 0 → object destroyed.

---

# 1️⃣2️⃣ Dynamic Typing

In Python:

```python
x = 10
x = "hello"
```

The variable has no fixed type.

The object has the type.

This is called:

> Duck Typing + Dynamic Typing

---

# 1️⃣3️⃣ Attribute Access

Since everything is object:

```python
print(dir(10))
```

Shows all methods of int object.

Example:

```python
print((10).bit_length())
```

Objects contain:

* Attributes
* Methods
* Behavior

---

# 1️⃣4️⃣ Why Python Chose This Model?

Because:

* Uniformity
* Simplicity
* Consistency
* Everything behaves similarly

No primitives vs objects difference like Java.

In Java:

```
int ≠ Object
```

In Python:

```
int IS object
```

Cleaner design.

---

# 🎯 Interview-Level Summary

✔ Everything is object
✔ Variables store references
✔ Every object has: identity, type, value
✔ All objects inherit from `object`
✔ Classes are objects
✔ Functions are objects
✔ `type` creates classes
✔ `type` is instance of itself
✔ Memory managed via reference counting

---

# If Interviewer Asks:

**Q: What does “Everything is an object” mean in Python?**

Best Answer:

> In Python, all entities including numbers, strings, functions, classes, and even types themselves are objects. Every object has identity, type, and value, and all objects inherit from the base `object` class. Variables are merely references to these objects, which enables Python’s dynamic and flexible design.

---

