# PASSING A LIST
# =========== #

#   You'll often find it userful to pass a list to a function, whether it's a list of names, numbers, or more complex objects, such as dictionaries.
#   When you pass a list to a function, the function gets direct access to the contents of the list. Let's use functions to make working with lists more efficient.
#   Say we have a list of users and want to print a greeting to each. The following example sends a list of names to a function called greet_users(), which greets each person in the list individually:


# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)


# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


#   We define greet_user() so it expects a lsit of names, which it stores in the parameter names. The function loops through the list it receives and prints a greeting to each user.
#   At 1 we define a list of users and then pass the list usernames to greet_user() in our function call:
# You can call the function any time you want to greet a specific set of users.


# Modifying a List in a Function
# =========================================
#   When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function's body are permanent, allowing you to work efficiently even when you're dealing with large amounts of data.
#   Consider a company that creates 3D printed models of designs tht usrs submit. Designs that need to be printed are stored in a list, and after being printed they're moved to a separate list. The following code does this without using function:


# Start with some designs that need to be printed.
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()

#     # Simulate creating a 3D from the design.
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# This program starts with a list of designs that need to be printed and an empty list called completed_models that each design will be moved to after it has been printed.
# As long as designs remain in unprinted_designs, the while loop simulates printing each design by removing a design from the end of the list, storing it in current_design, and displaying a message that the current design is being printed.
# It then adds the design to the list of completed models. When the loop is finished running, a list of the designs that have been printed is displayed:


# We can reorganize this code by writing two functions, each of which does one specific job. Most of the code won't change; we're just making it more efficient.
# The first function will handle printing the designs, and the second will summarize the prints that have been made:


def print_models(unprinted_designs, completed_models):  # 1
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):    # 2
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# At 1 we define the function print_models() with two parameters: a list of designs that need to be printed and a list of completed models. Given these two lists, the function simulates printing each design by emptying the list of unprinted designs and filling up the list of completed models.
# At 2 we define the function show_completed_models() displays the name of each model that was printed.
#   This program has the same output as the version withut functions, but the code is much more organized. The code that does most of the work has been moved to two separate functions, which makes the main part of the program easier to understand. Look at the body of the program to see how much easier it is to understand what this program is doing:

# We set up a list of unprinted designs and an empty list that will hod the completed models. Then, because we've already defined our two functions, all we have to do is call them and pass them the right arguments. We call print_models() and pass it the two lists it needs; as expected, print_models() simulates printing the designs. Then ew call show_completed_models() and pass it the list of completed models so it can report the models that have been printed. The descriptive function names allow others to read this code and understand it, even without comments.
#   This program is easier to extend and maintain than the version without functions. If we need to print more designs later on, we can simply call print_models() again. If we realize the printing code needs to be modified, we can change the code once, and our changes will take place everywhere the function is called. This technique is more efficient than having to update code separately in several places in the program.
#   This example also demonstrates the idea that every function should have one specific job. The first function prints each design, and the second displays the completed models. This is more beneficial than using one function to do both jobs. If you're writing a function and notice the function is doing too many different tasks, try to split the code into two functions. Remember that you can always call a function from another function, which can be helpful when splitting a complex task into a series of steps.


# Preventing a Function From Modifying a List
# ===========================================

#   Sometimes you'll want to prevent a function from modifying a list. For example, say that you start with a list of unprinted designs and write a function to move them to a list of completed models, as in the previous example. You may decide that even though you've printed all the designs, you want to keep the original list of unprinted designs for your records. But because you moved all the designs names ut of unprinted_designs, the list is now empty, and the empty list is the only version you have; the original is gone. In this case, you can address this issue by passing teh funciton a copy of the list, not the original. Any changes the function makes to the list will affect only the copy, leaving the original list intact.
#   You can send a copy of a list to a function like this:
# function_name(list_name[:])

#   The slice notation [:] makes a copy of the list to send to the function.
#   If we didn't want to empty the list of unprinted designs in printing_models.py, we could call print_models() like this:
# print_models(unprinted_designs[:], completed_models)


# The function print_models() can do its work because it stll receives the names of all unprinted designs. But his time it uses a copy of the original unprinted designs list, not the actual unprinted_designs list. The list completed_models will fill up with the names of printed models like it did before, but the original list of unprinted designs will be unaffected by the funciton.
# Even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy. It's more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you're working with large lists.
