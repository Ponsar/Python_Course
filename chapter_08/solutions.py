#============ Try it Yourself ====================== #

# 8-3 ================================================= #
# def make_shirt(size, message):
#     """Summarize the shirt that's going to be made."""
#     print(f"\nI am going to make a {size} t-shirt.")
#     print(f'It will say a "{message}"')


# make_shirt('large', 'I love Python!')

# 8-4. ================================================ #


# def make_shirt(size='large', message='I Love Python!'):
#     """Summarize the shirt that's going to be made."""
#     print(f"\nI am going to make a {size} T-shirt.")
#     print(f'It will say "{message}"')


# make_shirt()
# make_shirt(size='medium')
# make_shirt('small', 'Programmers are loopy!')

# 8-5 ================================================== #
# def describe_city(city, courntry='Malaysia'):
#     """Describe a city."""
#     msg = f"{city.title()} is in {courntry.title()}."
#     print(msg)


# describe_city('kuala lumpur')
# describe_city('bankok', 'thailand')
# describe_city('pinang')
# describe_city(courntry='china', city='beijing')

# ======================================================== #

# ================== Try It Yourself ====================== #

# # 8 - 6: City Names
# ==============================================
# def city_country(city, country):
#     """Return a string like Kuala Lumpur, Malaysia."""
#     return f"{city.title()}, {country.title()}"


# city = city_country('bankok', 'thailand')
# print(city)

# city = city_country('kuala lumpur', 'malaysia')
# print(city)

# city = city_country('jakarta', 'indonesia')
# print(city)

# 8-7: Album
# ============================================
# def make_album(artist, title):
#     """Build a dictionary containing information about album."""
#     build_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#     }
#     return build_dict


# album = make_album('metalica', 'ride the lightning')
# print(album)

# album = make_album('pongxvr slt', 'krvngti neci')
# print(album)

# album = make_album('vshong', 'munghuqme')
# print(album)


# with tracks:
# ======================================
# def make_album(artist, title, tracks=0):
#     """Build a dictionary containing information about an album."""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#     }
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict


# album = make_album('metallica', 'ride the lightning')
# print(album)

# album = make_album('beethoven', 'ninth symphony')
# print(album)

# album = make_album('willie nelson', 'red-headed stranger')
# print(album)

# album = make_album('iron maiden', 'piece of mind', tracks=8)
# print(album)

# 8-8: User Albums : Try this in teminal
# =====================================
# def make_album(artist, title, tracks=0):
#     """Build a dictionary containing information about an album."""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#     }
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict


# # Prepare the prompts.
# title_prompt = "\nWhat album are you thinking of? "
# artist_prompt = "Who's the artist? "

# # Let the user know how to quit.
# print("Enter 'quit' at any time to stop.")

# while True:
#     title = input(title_prompt)
#     if title == 'quit':
#         break

#     artist = input(artist_prompt)
#     if artist == 'quit':
#         break

#     album = make_album(artist, title)
#     print(album)

# print("\nThanks for responding!")
