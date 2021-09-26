# Solutions - Chapter 2
# 2-2: Simple Messages
# 2-5: Famous Quote
# 2-7: Stripping Names
# 2-9: Favorite Number
# Back to solutions.

# 2-2: Simple Messages
# Assign a message to a variable, and print that message. Then change the value of your variable to a new message, and print the new message.

msg = "I love learning to use Python."
print(msg)

msg = "It's really satisfying!"
print(msg)


# 2-5: Famous Quote
# Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
print('Albert Einstein once said, "A person who never made a mistake')
print('never tried anything new."')

# 2-7: Stripping Names
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

# Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = "\tEric Matthes\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())


# 2-9: Favorite Number
# Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.

fav_num = 42
msg = f"My favorite number is {fav_num}."

print(msg)
