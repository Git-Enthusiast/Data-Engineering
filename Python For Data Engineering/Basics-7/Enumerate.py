myString = "Hello World"

for i, j in enumerate(myString ,start=1):
    print(i, j)


myList = ["apple", "banana", "cherry"]

for index, fruit in enumerate(myList):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry

myTuple = ("apple", "banana", "cherry")

for index, fruit in enumerate(myTuple):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry