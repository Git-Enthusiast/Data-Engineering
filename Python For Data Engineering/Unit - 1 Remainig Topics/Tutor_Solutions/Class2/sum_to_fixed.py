def sum_to(n):
    """Return 1 + 2 + ... + n."""
    total = 0
    for i in range(1, n + 1):  # fix: range end is exclusive
        total += i
    return total


print("sum_to(5) =", sum_to(5))
print("sum_to(10) =", sum_to(10))
