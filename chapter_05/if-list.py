# Using if Statements with Lists
#   You can do some interesting work when you combine lists and if statements. You can watch for special values that need to be treated differently than other values in the list. You can manange changing conditions efficiently, such as the availability of certain items in a restaurant throuughout a shift. You can also begin to prove that your code workds as you expect it to in all possible situations.

# Checking For Special Items
#   Let's continue with the pizzeria example. The pizzeria displays a message whenever a topping is added to your pizza, as it's being made. The code for this action can be written very efficiently by making a ist of toppings that customer has requested and using a loop to announce each topping as it's added to the pizza:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

#   But what if the pizzeria runs out of green peppers? An if statement inside the for loop can handle this situation appropriately:
print("\nNo green peppers!\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!\n")

# Checking That a List Is Not Empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_toppig + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
#   The list is empty in this case, so the output asks if the user really wants a plain pizza:
#   If the list is not empty, the output will show each requested topping being added to the pizz.

# Using Multiple Lists
print("\nUsing Multiple Lists!\n")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_toppings in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry we don't have " + requested_toppings) + "."

print("\nFinished making your pizza!")
#   In just a few lines of code, we've managed a real-world situation pretty effectively!
