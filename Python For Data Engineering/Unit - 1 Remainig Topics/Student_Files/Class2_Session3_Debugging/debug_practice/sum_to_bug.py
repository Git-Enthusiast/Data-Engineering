# TASK: Use the debugger (breakpoint + Variables panel) to find the bug.
# sum_to(5) should return 1 + 2 + 3 + 4 + 5 = 15


def sum_to(n):
    """Return 1 + 2 + ... + n."""
    total = 0
    for i in range(1, n):
        total += i
    return total


print("sum_to(5) =", sum_to(5))
print("sum_to(10) =", sum_to(10))
