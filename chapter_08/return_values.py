## RETURN VALUES ##
# =============== #

# A function doesn't alwys have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a 'return value'. The return statement takes a value from inside a function and sends it back to the line that called the function. Return values allow you to move much of your program's grunt work into functions, which can simplify the body of your program.


# Returning a Simple Value
# ======================= #

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# Making an Argument Optional
# ========================= #

#   Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. You can use default values to make an argument optional.
#   For example, say we want to expand get_formatted.name() to handle middle names as well. A first attempt to include middle names might look like this:


# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()


# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)


#   But midlle names aren't always needed, and this function as written would not work if you tried to call it with only a first name and a last name.
#   To make the middle name optional, we can give the middle_name argument an empty default value and ignore the argument unless the user provides a value.
#   To make get_formatted_name() work without a middle name, we set the default value of middle_name to an empty string and move it to the end of the list of parameters:


# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# Returning a Dictionary
# ==================== #


# def build_person(first_name, last_name):
#     """Return a dictionary information about a person."""
#     person = {'first': first_name, 'last': last_name}   # 1
#     return person


# musician = build_person('jimi', 'hendrix')
# print(musician)


# This function takes in simple textual information and puts it into a more meaningful data structure that lets you work with the information beyond just printing it.
# The strings 'jimi' and 'hendrix' are now lableled as a first name and last name. You can easily extend this function to accept optional values like a middle name, an age, an occupation, or any other information you want to store about a person.
# For example, the following change allows you to store a person's age as well:


# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person


# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# Using a Function with a while Loop
# =============================== #


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formated."""
#     # full_name = first_name + ' ' + last_name
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# # This is an infinite loop! Try this in terminal! Open terminal by typing "python3 return_values.py"
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("first name: ")
#     l_name = input("last name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

#   For this example, we use a simple version of get_formatted_name() that doesn't involve middle names. The while loop asks the user to enter their name, and we prompt for their first and last name separately 1.
#   But there's one problem with this while loop: We haven't defined a quit condition. Where do you put a quit condition when you ask for a series of inputs?
#   We want the user to be able to quit as easily as possible, so each prompt should offer a way to quit.
#   The break statement offers a straight-forward way to exit the loop at either prompt:


def get_formatted_name(first_name, last_name):
    "Return a full name, neatly formatted."
    # full_name = first_name + ' ' + last_name
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("first name: ")
    if f_name == 'q':
        break

    l_name = input("last_name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "! Where are you coming from?")


#   We add a message that informs the user how to quit, and then we break out of the loop if the user enters the quit value at either prompt.
#   Now the programs will continue greeting people until someone enters 'q' for either name:
