# Passing an Arbitrary Number of Arguments
# ======================================


# def make_pizza(*toppings):
#     """Print the list of toppings that have benn requested."""
#     print(toppings)


# make_pizza('pepperoni')
# make_pizza('mushroom', 'green peppers', 'extra cheese')

# ======================================================

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the folllowing toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# =======================================================
# Mixing Positional and Arbitrary Arguments


# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# # Using Arbitrary Keyword Arguments
# # ===================================


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
