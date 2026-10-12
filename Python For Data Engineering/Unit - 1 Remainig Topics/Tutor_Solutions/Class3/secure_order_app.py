import os

PRICE = 100


def get_quantity():
    """Ask until the user enters a positive whole number."""
    while True:
        value = input("Enter quantity: ")
        try:
            quantity = int(value)
        except ValueError:
            print("Please enter a valid whole number.")
            continue
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
        return quantity


def get_discount():
    """Ask until the user enters a rate between 0 and 1."""
    while True:
        value = input("Discount rate as a decimal, for example 0.1: ")
        try:
            rate = float(value)
        except ValueError:
            print("Please enter a number such as 0.1.")
            continue
        if not 0 <= rate <= 1:
            print("Rate must be between 0 and 1.")
            continue
        return rate


def is_valid_quantity(value):
    """Return True for whole numbers of 1 or more."""
    return isinstance(value, int) and value >= 1


def main():
    api_key = os.environ.get("API_KEY")
    if api_key is None:
        print("Note: API key not configured.")
    quantity = get_quantity()
    discount = get_discount()
    print("Total:", PRICE * quantity * (1 - discount))


if __name__ == "__main__":
    main()
