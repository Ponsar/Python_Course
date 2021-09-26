# Python refers to values that cannot change as immutable, and an immutable list is called a 'tuple'.

# Defining a Tuple
# A tuple looks just like a list except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item's index, just as you would for a list.
# For example, if we have a rectangle that should always be a certain size, we can ensure that its size doesn't change by putting the dimension into a tuple:
dimensions =  (200, 50)
print(dimensions[0])
print(dimensions[1])

# Lets see what happens if we try to change one of the items in the tuple dimensions:
# Python will tell us we can't assign a new value to an item in an tuple:
# dimensions = (200, 50)
# dimensions[0] = 250

# Looping Through All Values in a Tuple
# You can loop over all the values in a tuple using a for loop, just as you did with a list:
# Python returns all the elements in the tuple, just as it would for a list:
dimensions = (200, 50, 300, 100)
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
# Although you can't modify a tuple, you can assign a new value to a variable that holds a tuple. So if we wanted to change our dimensions, we could redefine the entire tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)