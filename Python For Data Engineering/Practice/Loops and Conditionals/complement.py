#    Write a python program to find the complement of a given number. 

def find_complement(n):
    binary = bin(n)[2:] # start with index 2 go to end step by default 1
    complement = ""
    for ch in binary:
        if ch == '0':
            complement += "1"
        else:
            complement += "0"

    return int(complement,2)

number = int(input("Please Enter the integer: "))
print(f"The complement of {number} is {find_complement(number)}")