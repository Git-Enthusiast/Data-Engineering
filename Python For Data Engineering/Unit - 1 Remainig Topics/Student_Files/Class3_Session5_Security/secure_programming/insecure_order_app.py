# TASK: This program has several security and reliability problems.
# 1. Add input validation (reject text, zero and negative quantities).
# 2. Replace the bare except with a specific exception.
# 3. Remove the hard-coded API key (use an environment variable).
# 4. Do not use eval() on user input.

API_KEY = "sk-live-1234abcd"
PRICE = 100


def get_quantity():
    return int(input("Enter quantity: "))


def calculate_discount():
    rate_text = input("Discount rate as a decimal, for example 0.1: ")
    return eval(rate_text)


def main():
    print("Using key:", API_KEY)
    try:
        quantity = get_quantity()
        discount = calculate_discount()
        total = PRICE * quantity * (1 - discount)
        print("Total:", total)
    except:
        pass


if __name__ == "__main__":
    main()
