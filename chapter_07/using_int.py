# Using int() to Accept Input
#   When you use the input() function, Python interprets everything the user enters as a string. Consider the following interpreter session, which asks for the user's age:
#   Test thie in terminal! See this in Book!
# age = input("How old are you ")
# print(age)

##
# rollercoaster.py
# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
# When you use numerical input to do calculations and comparisons, be sure to convert the input value to a numerical representation first.

# The Modulo Operator
#   A useful tool for working with numerical information is the modulo operator(%), which divides one number by another number and returns the remainder:
print( 4 % 3 )
print( 5 % 3 )
print( 6 % 3 )
print( 7 % 3 )
#   The modulo operator doesn't tell you how many times one number fits into another; it just telss you what the remainder is.
#   When one number is divisible by another number the remainder is 0, so the modulo operator always return 0. You can use this fact to determine if a number is even or odd:
