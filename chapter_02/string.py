# A string is simply a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your string like this:

"This is a string."
'This is also a string.'

# One of the simplest tasks you can do with strings is change the case of the words in a string. Look at the following code, and try to determine what's happening:

name = "ada lovelace"
print (name.title() + "\n")

# A method is an action that Python can perform on a piece of data. The dot(.) after name in name.title() telss Python to make the title() method act on the variable name. Every method is followed by a set of parentheses, becasue methods often need additional information, so its parentheses are empty.
# Several other useful methods are available for dealing with case as well. For example, you can change a string to all uppercase or all lowercase letters like this:

name = "Ada Lovelace"
print (name.upper())
print (name.lower() + "\n")

# Combinning or Concatenating Strings

# Python uses the plus symbol (+) to combine strings. In this example, we use + to combine a full name by combining a first_name, a space, and a last_name.
# This method fo combining strings is called concatenation.

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print (full_name + "\n")

# Nicely formatted greeting:

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print("Hello, " + full_name.title() + "!\n")

# You can use concatenation to compose a message and then store the entire message in a variable:

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name 

message = "Hello, " + full_name.title() + "!"
print (message + "\n")

# Adding Whitespace to Strings with Tabs or Newlines 
# To add a tab to your text, use the character combinations \t as shows below: 

print("Python")

print("\tPython")

# To add a newline in a string, use the character combination \n as shows below: 

print ("Language:\nPython\nC\nJavaScript")

# Add Newline and Tab. "\n\t"
print("Language:\n\tPython\n\tC\n\tJavaScript")

# STRIPPING WHITESPACE
# Try this in terminal session

# favorite_language = 'python '
# favorite_language         # 'python '
# favorite_language.rstrip  # 'python'
# favorite_language         # 'python '     # looks same as when it was entered, including extra white space.

# ###

# favorite_language = 'python '
# favorite_language = favorite_language.rstrip()
# favorite_language

# ###

# favorite_language = ' python '
# favorite_language.rstrip()
# favorite_language.lstrip()
# favorite_language.strip()

