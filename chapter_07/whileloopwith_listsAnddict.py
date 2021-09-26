# So far, we have worked with only one piece of user information at a time. We receivd the user's input and then printed the input or a response to it.
# The next time through the while loop, we'd receive another input value and respond to that. But to keep track of many users and pieces of information, we'll need to use lists and dictionaries with our while loops.
#   A for loop is effective for looping through a list, but you shouldn't modigy a list inside a for loop because Python will have trouble keeping track of the items in the list.
#   To modify a list as you work through it, use a while loop. 
#   Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

## Moving Items From One List to Another
#   Consider a list of newly registered but unverified users of a website. After we verify these users, how can we move them to a separate list of confirmed users?
#   One way would be to use a while loop to pull users from the list of unconfirmed users as we verfigy them and then add them to a separate list of confirmed users. 
#   Here's what that code might look like:


# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# We begin with a list of unconfirmed users (Alice, Brian, and Candace) and an empty list to hold confirmed users.
# The while loop runs as long as the list unconfirmed_users is not empty. Within this loop,the pop() function removes unverified users one at a time from the end of unconfirmed_users.
#   Here, because Candace is last in the unconfirmed_users list, her name will be the first to be removed, stored in current_user, and added to the confirmed_users list. Next is Brian, then Alice.
# We simulate confirming each user by printing a verification message and then adding them to the list of confirmed users. As the list of unconfirmed users is empty, the loop stops and the list of confirmed users is printed:


## Removing All Instances of Specific Values from a List
#   In chapter 3 we used remove() to remove a specific value from a list. The remove() function worked because the value we were interested in appeared only once in the list.
#   But what if you want to remove all instances of a value from a list?
#       Say you have a list of pets with the value 'cat' repeated several times. To remove all instances of that value, you can run a while loop until 'cat' is no longer in the list, as shown here
print("\n")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

print("\nNext Block!")
# We start with a list containing multiple instances of 'cat'. After printing the list, Python enters the while loop because it finds the value 'cat' in the list at least once.
# Once inside the loop, Python removes the first instance of 'car', returns to the while line, and then reenters the loop when it finds that 'cat' is still in the list.
# It removes each instance of 'cat' until the value is no longer in the list, at which point Python exits the loop and prints the list again:


## Filling a Dictionary with User Input
# You can prompt for as much input as you need in each pass through a while loop. Let's make a polling program in which each pass through the loop prompts for the participant's name and response.
# We'll store the data we gather in a dictionary, because we want to connect each response with a particular user:
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # prompt for the person's name and response.
    name = input ("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False 

# Polling is complete. Show the results.
print("\n--- Poll Results ----")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")