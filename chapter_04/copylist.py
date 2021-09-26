# COPYIG A LIST
# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index([:]). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# To prove that we actually have two separate lists, we'll add a new food to each list and show that each list keeps track of the appropriate person's favorite foods:
print("\nTO PROVE THAT WE ACTUALLY HAVE TWO SEPARATE LISTS:\n")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# This doesn't work. The output shows that both lists are the same, which is not what we want:
print("\nThe output shows that both lists ae the same, which is not what we want:")

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)