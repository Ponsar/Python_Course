# Working with Part of a List

# Slicing a List
# To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function, Python stops one item before the second index you specify. To output the first three elements in a list,you would request indices 0 through 3, which would return elements 0, 1, and 2.
# The following example involves a list of players on a team:
players = ['charles', 'martina', 'michael', "florence", 'eli']
print(players[0:3])

# You can generate any subset of a list. For example, if you want the second, third, and fourth items in a list, you would start the slice at index 1 and end at index 4:
# Through second to fourth item. starts with 'martina' and ends with 'florence:
players = ['charles', 'martina', 'michael', "florence", 'eli']
print(players[1:4])

# If you omit the first in the first index in a slice, Python automatically starts your slice at the beginning of the list: 
# Without starting index, Python starts at the beginning of the list:

players = ['charles','martina', 'michael', "florence", 'eli']
print(players[:4])

# A similar syntax works if you want a slice that includes the end of a list.
# Python returns all items from the third item through the end of the list:
players = ['charles','martina', 'michael', "florence", 'eli']
print(players[2:])
 
# Negative index
# If we want to output the last four, we can use the slice [-4:]:
players = ['charles','martina', 'michael', "florence", 'eli']
print(players[-4:])

# Looping Through a Slice
# You can use a slice in a for loop if you want to loop through a subset of the elements in a list. In the next example we loop through the first three players and print their names as part of a simple rooster:
# Instead of looping through the entire list of players, Python loops through only the first three names:
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


