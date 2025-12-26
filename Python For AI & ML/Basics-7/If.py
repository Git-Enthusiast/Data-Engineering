# Decision Making Statement in Python
# #####################      if     #####################
# Sometimes, python programs has to take decisons
# using certains conditions.
# 1. Number is evn or odd
# 2. Voting age 
# so the condition checking is the backbone of  decision
# making.

########################################################

#          if Statements in Python

########################################################

# if Statement is used for deciosn making.
# in If statement, we check a condition. depending on
# truth value of condition, decision will be taken.
# Written using "if Keyword

# Syntax: 
# if condition/test_expression:
#       statement 1
#       statement 2
# rest of statements

# To check Number is Even
num= int(input("Please Enter an integer to check whether even or not"))
if (num%2 == 0):
    print("The given number ",num," is an even number")
    
# To check Voting age of a person
age = int(input("Please Enter Your age to check whether You are eligible for Voting or not"))
if (age>18): print("You are Eligible for Voting.")
# for single statement u can write in above line format also
