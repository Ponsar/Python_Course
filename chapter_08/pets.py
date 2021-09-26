## PASSING ARGUMENTS ##
# ==================== #

# Postional Arguments
# # ==================
# def describe_pet(animal_type, pet_name):
#     """Display about a pet!"""
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}.")


# describe_pet('hamster', 'harry')

# Multiple Function calls
# ===================== #


# def describe_pet(animal_type, pet_name):
#     """Display about a pet!"""
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}.")


# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# Order Matters in a Positional Arguments
# ====================================== #


# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s is a {pet_name.title()}.")


# describe_pet('mitu', 'dog')

# Keyword Arguments #
# ================ #

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s is a {pet_name.title()}.")


# describe_pet(animal_type='hamster', pet_name='harry')

# Default Value #
# ============ #


# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is a {pet_name.title()}.")


# describe_pet(pet_name='harry')  # Note that the order of the parameters in the funciton definition had to be changed. Because the default value makes it unnecessary to specify a type of animal as an argument, the only argument left in the funciton call is the pet's name. Python still interprets this as a positional argument, so if the funciton is called with just a pet's name, that argument will match up with the first parameter listed in the function's definition. This is the reason the first parameter needs to be pet_name.
# # This function call would have the same output as the above example. The only argument provided is 'willie', so it is matched up with the first parameter in the definition, pet_name. Because no argument if provided for animal_type, Python uses the default value 'dog'.
# describe_pet('willie')
# # Because an explicit argument for animal_type is provided, Python wil ignore the parameter's default value.
# describe_pet(pet_name='harry', animal_type='hamster')
# # NOTE: When you use the default values, any parameter with a default value needs to be listed after all the parameters that don't have default values. This allows Pythons to continue interpreting positional arguments correctly.


# Equivalent Functions Calls #
# ========================== #

# def describe_pet(pet_name, animal_type='dog'):
#     """"Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s is a {pet_name.title()}.")


# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')

# # A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
# # NOTE: It doesn't matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand.


## Exercise ##
# ========== #


# 8.3
# ===
# def make_shirt(shirt_size, shirt_message='never give up'):
#     """Display a message printed on shirt."""
#     print(
#         f"I have a shirt in {shirt_size.upper()} and a message \"{shirt_message.title()}\" printed on it.")


# make_shirt('size m')

def make_shirt(size='large', )
