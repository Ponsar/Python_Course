# Looping Through an Entire List
# =============================== #

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Naming for loop recommendation
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

# Doing More Workd Within a For Loop
# The output shows a personalized message for each magician in the list:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!\n")

# You can also write as many lines of code as you like in the for loop. Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list. Therefore, you can do as much workas you like with each value in the list.
# Let's add a second line to our message, telling each magician that we're looking forward to their next trick:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Doing Something After a For Loop
# Any line of code after the for loop that are not indented are executed once without repitition.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!\n")

# AVOIDING INDENTATION ERRORS:

# Forgettig to Indent. Python will remind you...
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)

# Forgetting to Indent Additional Lines
# This is logical error. The syntax is valid, but the code does not produce the desired result because a problem occurs in its logic.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Indenting Unnecessarily
# If you accidentally indent a line that doesn't need to be indented, Python informs you about the unexpected indent:
# message = "Hello Python World!"
#     print(message)

# Indenting Unnecessarily After the Loop
# This is another logical error.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title())

    print("Thank you everyone, that was a great magic show!")

# Forgetting the Colon
# The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.
# magicians = ['alice', 'david', 'james']
# for magician in magicians
#     print(magicians)
