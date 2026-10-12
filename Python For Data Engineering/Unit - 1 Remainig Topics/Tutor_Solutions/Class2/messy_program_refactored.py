DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1


def calculate_total(price, quantity, surcharge_rate=0.0):
    """Return the total cost.

    A discount applies when the subtotal is over the threshold,
    then an optional surcharge is added.
    """
    total = price * quantity
    if total > DISCOUNT_THRESHOLD:
        total -= total * DISCOUNT_RATE
    return total + total * surcharge_rate


print(calculate_total(100, 3))
print(calculate_total(20, 10))
print(calculate_total(50, 4, surcharge_rate=0.2))
