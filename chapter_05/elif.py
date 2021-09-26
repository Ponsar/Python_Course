# You can use as many elif blocks in your code as you like. For example, if the amusement park were to implement a discount for seniors, you could add one more conditional test to the code to determine whether someone qualified for the senior discount. Let's say that anyone 65 or older pays half the regular admission, or $5.
# Most of this code is unchanged. The second elif block checks to make sure a person is less than age 65 before assigning them the full admission rate $10. 
# Notice that the value assigned in the else block needs to changed to $5, because the only ages that make it to this block are people 65 or older.
age = 12

if age < 4:
    prince = 0
elif age < 18: 
    price = 5 
elif age < 65: 
    price = 10 
else:
    price = 5 

print("Your admission cost is $" + str(price) + ".")

# Omitting the else Block
# Python does not require an "else" block at the end of an if-elif chain. Sometimes an else block is useful; sometimes it it clear to use an additional elif statement that catches the specific condition of interest:
age = 12 

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("\nYour admission cost is $" + str(price) + ".")

# Testing Multiple Conditons
# The if-elif-else chin is powerful, butit's only appropriate to use when you just need one test to pass. As soon as Python finds one test to passes, it skips the rest to the tests. This behavior is beneficial, because it's efficient and allows you to test for one specific condition.
# However, sometimes it's important to check all the conditions of interest. In this case, you should use a series of simple if statements with no "elif" or "else block". This thechniqe makes sense when more than one condition could be True, and you want to act on every coondition that is True.
# Let's reconsider the pizzeria example. If someone requests a two-topping pizza, you'll need to be sure include both toppings on their pizza:
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("\nAdding mushroom.")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#   This code would not work properly if we used an if-elif-else block, because the code would stop running after only one test passes. Here's what that would look like:
print("\nThis is not working properly as we used an if-elif-else block!\n")

requested_toppings = ['mushrooms', 'extra cheese',]

if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nfinished making your pizza!")

# In summary, if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements.