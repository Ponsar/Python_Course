# The loop in this example first checks if the current value of car is 'bmw'. If it is, the value if printed in uppercase. If the value of car is anything other than 'bmw', it's printed in title case:
# This example combines a number of the concepts you'll learn about in this chapter.
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# CONDITIONAL TESTS

# At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test. Python uses the values True or False to decide whether the code in an if statement should be executed. If a . conditional test evaluates to Tre, Python executes the code following the if statement. If the test evaluates to False, Python ignores the code following the if statement.
# Checking for Equallity
# (==) This equality operator returns True if the values on the left and right side of the operator match, and False if they don't match.
print("\nThe output is True:")

car = 'bmw'
print(car == 'bmw')

print("\nThe output is False:")

car = 'audi'
print(car == 'bmw')

# Ignoring Case When Checking for Equality
#   Testing for equality is case sensitive in Python. For example, two values with different capitalization are not considered equal:
print("\nThe output is False:")

car = 'Audi'
print(car == 'audi')

#   If case matters, this behavior is advantageous. But if case doesn't matter and instead you just want to test the value of a variable, you can convert the variable's value to lowercase before doing the comaparison:
#   This test would return True no matter how the value 'Audi' is formatted because the test if now case insensitive. The lower() function doesn't chnge the value that was originally stored in car, so you can do this kind of comparison without effecting the original variable:
print("\nThis test returns True:")

car = "Audi"
print(car.lower() == 'audi')

print("\nWe can see that the value stored in car has not been effected by the conditional test:")
print(car)

# Checking for Inequality
# When you want to determine whether two values are not equal, you can combine an exclamation point and equal sign (!=). The exclamation point represents not, as it does in many programming languages.
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("\nHold the anchovies!")

# Numerical Comparisons
print("\nThis is True:")
age = 18 
print(age == 18)

# You can also test to see if two numbers are not equal. For example, the following code prints a message if the given answer if not correct:
# The conditional test passes, because the value of answer (17) is not equal to 42. Because the test passes, the indented code block is executed:
answer = 17 

if answer != 42:
    print("\nThat is not the correct answer. Please try again!")

#   You can include various mathematical comparison in your conditional statements as well, such as less than, less than or equal to, greater than, and greater than or equal to:
#   Each mathematical comparison cab be used as part of an if statement, which can help you detect the exact conditons of interest.
age = 19

print("\nThis is True:")
print( age< 19)

print("\nThis is True:")
print( age <= 21)

print("\nThis is False:")
print( age > 21)

print("\nThis is False:")
print( age >= 21)

# Checking Multiple Conditons
#   You may want to check multiple conditions at the same time. For example, sometimes you might need two conditions to be True to take an action. Other times you might be satisfied with just one condition being True. The keywords "and" and "or" can help you in thsee situations.
#   Using "and" to Check Multiple Conditions
#       To check whether two conditions are both True simultaneously, use the keyword "and" to combine the two conditional tests; if each test passes, the overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.
#           For example, you can check whether two people are both over 21 using the following test:
print("\nThis is False:")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

print("\nThis is True:")
age_1 = 22 
print(age_0 >= 21 and age_1 >= 21)
# To improve readability, you can use parentheses around the individual tests, but they are not required. If you use parentheses, your test would look like this:
print(age_0 >= 21) and (age_1 >= 21)
# This also works:
print(age_0 >= 21 and age_1 >= 21)

# Using "or" to Check Multiple Conditions
#   The keyword "or" allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass. An "or" expression fails only when both individual tests fial.
#   Let's consider two ages again, but this time we'll look for only one person to be over 21;
print("\nThis is 'or' keyowrd and the output is True:")
age_0 = 22
age_1 = 18 
print(age_0 >= 21 or age_1 >= 21)

print("\nThis is False:")
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

# Checking Whether a Value Is in a List
# To find out whether a particular value is already in a list, use the keyword "in"
requested_toppings = ['mushrooms', 'onion', 'pineapple']

print("\nThis is True:")
print('mushrooms' in requested_toppings)

print("\nThis is False:")
print('pepperoni' in requested_toppings)

# Checking Whether a Value Is Not in a List
# Use keyword "not in" 
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print("\n" + user.title() + ", you can post a response if you wish.")

# Boolean Expressions
# A Boolean expression is just another name for a conditional test. A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.
# Boolean values are often used to keep track of certain conditions, such as whether a game is running or whether a user can edit certain content on a website:
# Boolean valuse provide an effective way to track the state of a program or a particular condition that is important in your program.
game_active = True
can_edit = False 
