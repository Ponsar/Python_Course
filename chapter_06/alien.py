# Dictionaries

#   A Simple Dictionary
alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])
#   The dictionary alien_0 stores the alien's color and point value. The two print statements access and display that information, as shown in the output:

# Working with Dictionaries
#   A dictionary in Python is a collection of key_value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.
#   A key value can be number, a string, a list, or even another dictionary.
#   In fact, you can use any object that can create in Python as a value in a dictionary.
#   In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces, as shown in the earlier example:
#   alien_0 = {'color' : 'green', 'points' : 5}

#   A key-value is a set of values associated with each other. When you provide a key, Python returns the value associated with that key. 
#   Every key is connected to its value by a colon, and individual key-value pairs are separated by commas. You can store as many key-value as you want in a dictinary.
#   The simplest dictionary has exactly one key-value pair, as shown in this modified version of the alien_0 dictionary:
alien_0 = {'color': 'green'}
#   This dictionary stores one pieces of information about alien_0, namely the alien's color. The string 'color' is key in this dictionary, and its associated value is 'green'.

# Accessing Values in a Dictionary
#   To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:
alien_0 = {'color': 'green'}
print(alien_0['color'])
#   This returns the value associated with the key 'color' from the dictionary alien_0:

# If a player shoots down this elien, you can look up how many points they should earn using code like this:
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("\nYou just earned " + str(new_points) + " points!\n")

# Adding New Key-Value Pairs
#   Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any times. 
#   For example, to add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets along with the new value.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0 
alien_0['y_position'] = 25
print(alien_0)
# Notice that the order of the key-value pairs does not match order in which we added them. Python does not care about the order in which you store each key-value pair;
# it cares only about the connection between each key and its value.

# Starting with an Empty Dictionary
print("\nStarting with Empty Dictionary:\n")

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values in a Dictionary
#   To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.
#   For example, consider an alien that changes from green to yellow as game progresses:
alien_0 = {'color' : 'green'}
print("\nThe alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#   For more interesting example, let's track the position of an alien that can move at different speeds. We'll store a value representing the alien's current speed and then use it to determine how far to the right the alien should move:
print("\nCheck the following:\n")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien tVo the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow': 
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# Removing Key-Value Pairs
#   When you no longer need a piece of information that's stored in a dictionary, you can use the "del" statement to completely remove a key-value pair.
#   All "del" needs is the name of the dictionary and the key that you want to remove.
#   For example, let's remove the key 'point' from the alien_0 dictionary alongside with its value:
print("\nRemoving Key-Value Pairs!\n")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0["points"]
print(alien_0)
# Note: Be aware that the deleted key-value pair is removed permannetly.


# A Dicionary of Similar Objects
#   The previous example involved storing different kinds of information about one object, an alien in a game. You can also use a dictionary to store one kind of information about many objects.
#   For example, say you want to poll a number of people and ask them what their favorite programming language is. A dictionary is useful for storing the results of a simple poll, like this:
# As You see, we've broken a larger dictionary into several lines. Each key is the name of a person who responded to the poll, and each value is their language choice.
# When you know you'll need more than one line to define a dictionary, press ENTER after the openning brace. Then indent the next line one level(four braces), and write the first key-value pair, followed by a comma. From this point forward when you press ENTER, you text editor should automatically indent all subsequent key-value pairs to match the first key-value pair.
#   Once you've finished defining the dictionary, add a closing brace on a new line after the last key-value pair and indent it one level so it aligns with the keys in the dictionary. It's good practice to include a comma after the lasy key-value pair as well, so you're ready to add a new key-value pair on the next line.
favorite_languages = {
    'Jen': 'python',
    'Zamiram': 'c',
    'Pongsar': 'python',
    'Dxram': 'ruby',
    'Phil': 'c++'
    }

print("Pongsar's favorite language is " + 
    favorite_languages['Pongsar'].title() + 
    ".")

print("\nPongsar's favorite language is " + favorite_languages['Pongsar'].title() + ".")
#   This example also shows how you can break up a long print statement over several lines. The word print is shorter than most dictinary names, so it makes sense to include the first part of what you want to print right after the openning parenthesis.
#   Choose an appropriate point at which to break what's being printed, and add a concatenation operator (+) at the end of the first line. Press ENTER and then press TAB to align all subsequent lines at one indentation level under the print statement. When you've finished composing your output, you can place the closing parenthesis on the last line of the print block.
