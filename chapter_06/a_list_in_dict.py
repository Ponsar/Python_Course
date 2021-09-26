# Rather than putting a dictionary inside a list, it's sometimes useful to put a list inside a dictionary. For example, conside how you might describe a pizza that someone is ordering. If you wre to use only a ist, all you could really store is a list of pizza's toppings. With a dictionary, a list of topping can be just one aspect of the pizza you're describing.
# In the following example, two kinds of information are stored for each pizza: a type of crust and a list of toppings. The list of toppings is a value associated with the key 'toppings'. To use the items in the list, we give the name of the dictionary and the key 'toppings', as we sould any value in the dictionary. Instead of returning a single value, we get a ist of toppings:

# Store information about a pizza being ordered.
pizza = { 
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print("You ordered a " + pizza['crust'] + "_crust pizza " + 
    "with the following toppings:")

for topping in pizza['toppings']: 
    print("\t" + topping)


# You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary. 
# When we loop through the dictionary, the value associated with each person would be a list oflanguages rather than a single language.
# Inside the dictionary's for loop, we use another for loop to run through the list of languages associated with each person:
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
#   To define this program even further, you could include an if statement at the beginning of the dictionary's for loop to see whether each person has more than one favorite language by examining the value of len(languages).
#   If a person has more than one favorite, the output would stay the same. If the person has only one favorite language, you could change the wording to reflect that. 
#   For example, you could say Sarah's favorite language is C.