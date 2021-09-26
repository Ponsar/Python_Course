# Importing an Entire Module
# ================================================

# import pizza

# pizza.make_pizza(16, 'pepperozni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Importing Specific functions
# from module_name import function_name
# from dudule_name import function_0, function_1, function_2
# =================================================


# from pizza import make_pizza

# make_pizza(15, 'pepperoni')
# make_pizza(13, 'mushrooms', 'green peppers', 'extra cheese')


# Using as to Give a Function an Alia
# from module_name import function_name as fn
# ===================================================


# from pizza import make_pizza as mp

# mp(19, 'pepperoni')
# mp(15, 'mushroom', 'green peppers', 'extra cheese')


# Using as to Give a Module as Alia
# ==========================================

# from typing import MutableMapping
# import pizza as p

# p.make_pizza(15, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functi
# from module_name import *
# ====================================

# from pizza import *

# make_pizza(12, 'pepperoni')
# make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')


# Styling Functions
# =====================================


# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#     function body...
