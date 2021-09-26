
# print("Hello Python World!")


# Variables #
# ================================= #

# message = "Hello Python World!"
# print(message)


# Changing Case in a String with Methods
# ======================================

# name = 'ada lovelace'
# print(name.title())
# print(name.upper())
# print(name.lower())

# Using Variables in Strings
# ======================================== #

# first_name = 'ada'
# last_name = 'lovelace'
# full_name = f"{first_name} {last_name}"
# print(F"Hello, {full_name.title()}!")

# # You can also use f-strings to compose a message, and then assign the entire message to a variable:
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# message = f"Hello, {full_name.title()}!"
# print(message)


# Adding Whitespace to Strings with Tabs or Newlines
# ================================================ #

# print("Python")
# print("\tPython")
# print("Languages:\nPython\nC\nJavaScript")
# print("Languages:\n\tPython\n\tC\n\tJavaScript")


# ================================================ #

# course = ' python programming '

# # case
# print(course.upper())
# print(course.lower())
# print(course.title())
# # strip
# print(course.strip())
# print(course.rstrip())
# print(course.lstrip())
# # find, replace and ...
# print(course.find('pro'))
# print(course.replace('p', 'j'))
# # find true and false
# print('pro' in course)
# print('swift' not in course)
# # len
# print(len(course))
# # index
# print(course[2])
# print(course[2:-2])
# print(course[-3])
# print(course[0:3])
# print(course[0:])
# print(course[:])
# print(course[:-5])

# Numbers
# ======================== #

# x = 1         # int
# x = 1.1       # float
# x = 2 + 2j    # complex

print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)    # This will get float.
print(3 // 2)   # This will get integer.
print(3 % 2)    # This will get remainder.
print(3 * 2)
print(3 ** 2)

# augmented operator
x = 3
x = x + 2
print(x)
# exactly the same with the below
x = 3
x += 2  # augmemted operator
print(x)

# order of operation
a = 2 + 3 * 4
print(a)

b = (2 + 3) * 4
print(b)

# Underscores in NUmbers
universe_age = 14_000_000_000
print(universe_age)

# Multiple Assignment
x, y, z = 1, 2, 7
print(z)

# Constants
# Use capital letter to indicate a variable should be treated as a constant and never be changed:
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
