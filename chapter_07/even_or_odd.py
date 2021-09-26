
# The Modulo Operator
#   A useful tool for working with numerical information is the modulo operator(%), which divides one number by another number and returns the remainder:
print( 4 % 3 )
print( 5 % 3 )
print( 6 % 3 )
print( 7 % 3 )
#   The modulo operator doesn't tell you how many times one number fits into another; it just telss you what the remainder is.
#   When one number is divisible by another number the remainder is 0, so the modulo operator always return 0. You can use this fact to determine if a number is even or odd:

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# Accepting Input in Python 2.7
#   If you're using Python 2.7, you should use the raw_input() function when prompting for user input. This function interprets all input as string, just as input() does in PYthon 3.
#   Python 2.7 has an input() function as well, but this function interprets the user's input as Python code and attempts to run the input.
#   If you're using Python 2.7, use raw_input() instead of input().