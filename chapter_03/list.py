# What is a list?
# A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0-9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don't have to be related in any particular way. Because a list usually contains more than one elements, it's a good idea to make the name of your list plural, such as letter, digits, or names.
# In Python, square brackets ([]) indicates a list, and individual elements in the list are separated by commas. Here's a simple example of a list that contains a few kinds of bicycles:

print("\nDisplaying the elements of the list:")
bicycles = ['trek', 'connondal', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
# ======================================= #
# Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

print("\nAccesing the first element, 'trek':")
bicycles = ['trek', 'cannondl', 'redline', 'specialized']
print(bicycles[0])

print("\nAccessing the first element, 'trek', in Capitalized:")
bicycles = ['trek', 'cannondl', 'redline', 'specialized']
print(bicycles[0].title() + "\n")

# Index Positions Start at 0, Not 1.
# =================================== #

bicycles = ['trek', 'cannondal', 'redline', 'specialized']
print("\nAccessing the elements in a List by Index Position: " +
      bicycles[1].title())
print("Accessing the elements in a List by Index Position: " +
      bicycles[3].title())

# Accessing the last element in a list.
# ==================================== #
bicycles = ['trek', 'cannondal', 'redline', 'specialized']
print("\nAccesing the last element in a List, " + bicycles[-1])

# Using Individual Values From a List
# ==================================== #

print("\nUsing individual value from a List:")
bicycles = ['trek', 'cannondal', 'redline', 'specialized']
message = "\nMy first bicylces was a " + bicycles[0].title() + "." + "\n"

print(message)

# Try it Yourself.
# 3-1

names = ['Pongsar', 'Zamiram', 'Khawram', 'Marina', 'Fimay']
print(names[0] + "\n")

print(names[1] + "\n")

print(names[2] + "\n")

print(names[3] + "\n")

print(names[4] + "\n")

# Try it Yourself
# 3-2

names = ['Pongsar', 'Zamiram', 'Khawram', 'Marina', 'Fimay']
print("Hello " + names[0] + ", How are you doing?" + "\n")
print("Hello " + names[1] + ", How are you doing?" + "\n")
print("Hello " + names[2] + ", How are you doing?" + "\n")
print("Hello " + names[3] + ", How are you doing?" + "\n")

# Try it yourself
# 3-3

cars = ['ford', 'chevy', 'audi']
print("I would like to own " + cars[0] + "." + "\n")
print("I would like to own " + cars[1] + "." + "\n")
print("I would like to own " + cars[2] + "." + "\n")

# Changing, Adding, and Removing Elements
# Modifying Elements in a List
# You can change the value of any item in a list, not just the first item.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# ADDING ELEMENT TO A LIST
# Appending Elements to the End of a List
# When you append an item to a list, the new element is added to the end of the list.
# The append() method adds 'ducati' to the end of the list without effecting any of the other elements in the list:


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# The append() method makes it easy to build lists dynamically. For example, you can start with an empty list and then add items to the list using a series of append() statements. Using an empty list, let's add the elements 'honda', 'yamaha', and 'suzuki' to the list:

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Inserting Elements into a List
# You can add a new element at any position in your list by using the insert() method. You do this by specifying the index of the new element and the value of the new item.

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# REMOVING ELEMENTS FROM A LIST
# Removing an Item Using the del Statement
# If you know the position of the item you want to remove from a list, you can use the "del" statement.


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# You can remove an item form any position in a list using the "del" statement if you know its index.
# For example, here's how to remove the second item, "yamaha" in the list:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# REMOVING AN ITEM USING THE POP() METHOD
# Sometimes you'll want to use the value of an item after you remove it from a list.
# The pop() method removes the last item in a list, but it lets you work with that item after removing it.
# Let's pop a motorcycle from the list of motorcycles:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# How might this pop() method be useful? Imagine that the motorcycles in the list are stored in chronological order according to when we owned them. If this is the case, we can use the pop() method to print a statement about the last motorcycle we bought:

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# When you want to delete an item from a list and not use that item in any way, use the del statement: if you want to use an item as you remove it, use the pop() method.
# Poping Items from any Position in a List

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")


# REMOVING AN ITEM BY VALUE
# Sometimes you won't know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the remove() method.
# For example, let's say we want to remove the value 'ducati' from the list of motorcycles.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# You can also use the remove() method to work with a value that's being removed from a list. Let's remove the value 'ducati' and print a reason for removing it from the list:

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# Note: The remove() method deletes only the first occurence of the value you specify. If there's a possibility the value appears more than once in the list, you will need to use a loop to determine if all accurrence of the value have been removed.
