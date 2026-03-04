X = ['a', 'b', 'c', 'd']

for X[-1] in X:
    print(X[-1], end="")

"""

🔎 What’s happening here?

This is a very tricky Python behavior.

Normally we write:

for i in X:

But here you wrote:

for X[-1] in X:

That means:

Instead of using a temporary variable like i,

You are assigning each loop value directly to X[-1] (the last element of the list).

📌 Step-by-step Execution

Initial list:

X = ['a', 'b', 'c', 'd']
🔁 Iteration 1:

Loop value = 'a'

Assign → X[-1] = 'a'

List becomes → ['a', 'b', 'c', 'a']

Print → a

🔁 Iteration 2:

Loop value = 'b'

Assign → X[-1] = 'b'

List becomes → ['a', 'b', 'c', 'b']

Print → b

🔁 Iteration 3:

Loop value = 'c'

Assign → X[-1] = 'c'

List becomes → ['a', 'b', 'c', 'c']

Print → c

🔁 Iteration 4:

Loop value = 'c' ❗ (Not 'd')

Why?

Because in iteration 1, 'd' was replaced with 'a'.
So the original 'd' is lost.

The loop now iterates over the modified list.

So it prints → c

✅ Final Output:
abcc

"""