# Looping Through All Key_Value Pairs
#   If you want to see everything stored dcitionary, you could loop through the dictionary using a "for" loop:
#   To write a "for" loop for a dictionary, you create names for the two variables that will hold the key and value in each key-value pair.
#   You can choose any names you want for these two variables.
#   This code would work just as well if you had used abbreviation for the variable names, like this:
#   for k, v in user_o.item()
#   The second half of the "for" statement includes the name of the dictionary followed by the method items(), which returns a list of key-value pairs.
#   The "for" loop then stores each of these pairs in the two variables provided.
user_0 = {
    'username': 'xvr',
    'first': 'hee',
    'last': 'xvr'
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
#   Notice the key-value pairs are not returend in the order in which they were stored, even when looping through a dictionary.

print("\nNext:\n")
# Looping through all key-value pairs works particularly well for dictionaries like this:
favorite_languages = {
    'Jen': 'python',
    'Zamiram': 'c',
    'Pongsar': 'python',
    'Dxram': 'ruby',
    'Phil': 'c++'
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
        language.title() + ".\n")


# Looping Through All the Keys in a Dictionary
#   The keys() method is useful when you don't need to work with all of the values in a dictionary. Let's loop through the favorite_languages dictionary and print the names of everyone who took the poll:
favorite_languages = { 
    'pongsar': 'python',
    'zamiram': 'C',
    'khur': 'ruby',
    'phi': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())
# #   Looping through the keys is actually the default behaviour when looping through a dictionary, so this code would have exactly the same output if you wrote...
# for name in favorite_languages:
# # rather than...
# for name in favorite_languages.keys():
#   You can choose to use the keys() method expicitly if it makes your code easier to read, or you can omit it if you wish.


print("\n")
#   You can access the value associated with any key you care about inside the loop by using the current key. Let's print a message to a couple of friends about the languages they chose. 
#   We'll loop through the names in the dictionary as we did previously, but when the name matches one of our friends, we'll display a message about their favorite language:
favorite_languages = {
    'pongsar': 'python',
    'zamiram': 'ruby',
    'jungram': 'php',
    'deeram': 'java',
    }

friends = ['pongsar', 'deeram']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " + 
            favorite_languages[name].title() + "!")     ### To access the favorite language, we use the name of the dictionary and the current value of name as the key. Everyone's name is printed, but our friends receive a special message:


print("\n")
#   You can also use the keys() method to find out if a particular person was polled. This time, let's find out if Zamiram took the poll:
favorite_languages = {
    'pongsar': 'python',
    'jungram': 'c',
    'deeram': 'ruby',
    'mayram': 'java'
    }

if 'zamiram' not in favorite_languages.keys():
    print("Zamiram, please take our poll")
#   The keys() method isn't just for looping: It actually returns a list of all the keys, and the line at "if" simply checks if 'zamiram' is in this list. Because she's not, a message is printed inviting her to take the poll:

print("\n")
# Looping Through a Dictionary's Keys in Order
#   A dictionary always maintains a clear connection between each key and its associated value, but you never get the items from a dictionary in any predicable order. That's not a problem, because you'll usually just want to obtain the correct value associated with each key.
#   One way to return items in a certain order is to sort the keys as they're returned in the "for" loop. You can use the sorted() function to get a copy of the keys in order:
favorite_languages = {
    'kenram': 'java',
    'duko': 'javascript',
    'sinram': 'php',
    'jungram': 'python',
    'pongsar': 'rubu',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.\n")


# Looping Through All Values in a Dictionary
#   If you are primarily interested in the values that a dictionary contains, you can use the values() method to return a list of values without any keys.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phi': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n")
#   This approach pulls all the values from the dictionary without checking for repeats. That might work work fine with a small number of values, but in a poll with a large number of respondents, this would result in a very repetitive list.
#   To see each language chosen without repetition, we can use a "set". 
#   A "set" is similar to a list except that each item in the set must be unique:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phi': 'python',
    }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
#   When we wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items.
#   And we use set() to pull out the unique languages in favorite_languages.values().
#   The result is a nonrepetitive list of languages that have been mentiioned by people taking the poll:
#   As you continue learning about Python, you'll often find a built-in feature of the language that helps you do exactly what you want with your data.