# A List of Dictionares

#   The alien_0 dictionary contains a variety of information about one alien, but it has no room to store information about a second alien, much less a screen full of aliens.
#   How can you manage a fleet of aliens?
#   One way is to make a list of aliens in which each alien is a dictionary of information about that alien. for example, the following code builds a list of three aliens:
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

###
#   A more realistic example would involve more than three aliens with code that automatically generates each alien. In the following example we use range() to create a fleet of 30 aiens:
print("\nNext Block!\n")

aliens = [] #   Make an empty list for storing aliens

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
#   These aliens all have the same characteristics, but Python considers each one a separate object, which allows us to modify each alien individually.
#   How might you work with a set of aliens like this? Imagine that one aspect of a game has some aliens changing color and moving faster as the game progresses. When it's time to change colors, we can use a for loop and an if statment to change the color of aliens. F
#   For example, to change the first three aliens to yellow, medium-speed aliens worth 10 points each, we could do this:
print('\nNext Block!\n')

# Make am empty list for storing aliens.
aliens = []   

# Make 30 green aliens.
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

    for alien in aliens[0:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = '10'

# Show the first 5 aliens.
for alien in aliens[0:5]:
    print(alien)
print("...Next Block\n")
#   Because we want to modify the frist three aliens, we loop through a slice that includes only the first three aliens. All of the aliens are green now but that won't always be the case, so we write an if statement to make sure we're only modifying green aliens. If the alien is green, we change the color to 'yellow', the speed to 'medium', and the point value to 10, as shown in the following output:


#   You could expand this loop by adding an elif block that turns yellow aliens into red, fast-moving ons worth 15 points each. Without showing the entire program again, that loop would look like this:
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'
    print(alien)
print("...")
#   It's common to store a number of dictionaries in a list when each dictionary contains many kinds of information about one subject.
