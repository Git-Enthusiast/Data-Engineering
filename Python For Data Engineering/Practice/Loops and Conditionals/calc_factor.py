'''
To calculate the factors of a number, we find all numbers that divide the given number exactly (remainder = 0).

🔹 What is a Factor?

A factor of a number is a number that divides it completely.

Example:
Factors of 12 → 1, 2, 3, 4, 6, 12

Because:

12 ÷ 1 = 12

12 ÷ 2 = 6

12 ÷ 3 = 4

12 ÷ 4 = 3

12 ÷ 6 = 2

12 ÷ 12 = 1

'''

def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

num = int(input("Enter a number: "))
print("Factors are:", find_factors(num))