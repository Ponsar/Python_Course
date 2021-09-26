# You can nest a dictionary inside a another dictionary, but your code can get complicated quickly when you do.
users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print ("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())
#   Notice that the structure of each user's dictionary is identical. Although not required by Python, this structure makes nested dictionaries easier to work with. 
#   If each user's dictionary had different keys, the code inside the for loop would be more complicated.