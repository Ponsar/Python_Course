## Defining a Function

def greet_user():   # 1
    """Display a simple greeting."""    # 2
    print("Hello!") # 3

greet_user()    # 4
#   This example shows the simplest structure of a function. The line at 1 uses the keyword def to inform Python that you're defining a function. This is the function definition, which tells Python the name of the function and, if applicable, what kind of information the function needs to do its job. The parentheses hold that information. In this case,the name of the function is greet_user(), and it needs no information to do its job, so it's parentheses are empty. (Even so, the parentheses are required.) Finally, the definition ends in a colon.
#   Any indented lines that follow def greet_user(): make up the body of the function. The text at 2 is a comment called a docstring, which describes what the function does. Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your program.
#   The line print("Hello!") # is the only line of actual code in the body of this function, so greet_user() has just one job: print("Hello!").
#   When you want to use this function, you in call it. A function call tells Python to execute the code in the function. To call a function, you write the name of the function, followed by any necessry information in parentheses, as shown at 4. Because no information is needed here, calling our function is as simple as entering greet_user(). As expected, it prints Hello!:



#   Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user("pongsar")

#   Arguments and Parameters
#       In the preceding greet_user() function, we defined greet_user() to require a value ofr the variable username. Once we called the function and gave it the information (a person's name), it printed the right greeting.
#       The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job. The value 'pongsar' in greet_user('pongsar') is an example of an argument. 
#       An argument is a piece of information that is passed from a function call to a function. When we call the function, we place the value we want the function to work with in parentheses. 
#       In this case the argument 'pongsar' was passed to the function greet_user(), and the value was stored in the parameter username.

#   Note: People sometimes speaks of arguments and parameters interchangeably. Don't be surprised if you see the variables in a function definition referred to as arguments or the variables in a function call referred to as parameters.



## PASSING ARGUMENT
#   Because a function definition can have multiple parameters, a function call may need multiple arguments. You can pass arguments to your funtions in a number of ways.
#   You can use positional arguments, which nedd to be in the same order the parametrs were written; keyword arguments, where each argument consists of variable name and a value; and lists and dictionaries of values. 
#   Let's look at each of these in turn.

# Positional Arguments
#   When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided.
#   Values matched up this way are called positional arguments.
#   To see how this works, consider a function that displays information about pets. The function tells us what kind of animal each pet is and the pet's name, as shown here:
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# Multiple Function Calls
#   You can call a function as many times as needed. Describing a second, different pet requires just one more call to describe_pet():
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'whillie')

# Order Matters in Positional Arguments
#   You can get unexpected results if you mix up the order of the arguments in a function call when using positional arguments:
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')

# Keyword Arguments
#   A keyword argument is a name-value pair that you pass to a function. 
#   You directly associate the name and the value within the argument, so when you pass the argument to the function, there's no confusion (you won't end up with a harry named Hamste).
#   Keyword argument free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the functina call.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
# Note: When you use keyword arguments, be sure to use the exact names of the parameters in the function's definition.


# Default Values
#   When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter's default value.
#   So when yu define a default value for a parametr, you can exclude the corresponding argument you'd usually write in the function call. Using default values can simplify your function calls and clarify the ways in which your functions are typically used.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
# This function call would have the same output as the previous example. The only argument provides is 'willie', so it is matched up with the frist parameter in the definition, pet_name. Because no argument is provided for animal_type, Python uses the default value 'dog'.
# To describe an animal other than a dog, you could use a function call like this:
describe_pet(pet_name='harry', animal_type='hamster')
# Because an explicit argument for animal_type is provided, Python will ignore the parameter's default value.
# Note: When you use default values, any parameter with a default value needs to be lsited after all the parameters that don't have default values. This allows Python to continue interpreting positional arguments correctly.


# Equivalent Function Calls
#   Because positional arguments, keyword arguments, and default values can all be used together, often you'll have several equivalent ways to call a function.
#   Consider the following definition for describe_pets() with one default value provided:
# def describe_pet(pet_name, animal_type='dog'):
#     # With this definition, an argument always needs to be provided for pet_name, and this value can be provided using the positional or keyword format. If the animal being described is not a dog, an argument for animal_type must be included in the call, and this argument can also be specified using the positional or keyword format.
#     # All the following calls would work for this funciton:
# # A dog named Willie.
# describe_pet('Willie')
# describe_pet(pet_name='Willie')
# # A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
#   Each of these function calls would have the same output as the previous examples.
#   Note: It doesn't really matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand.


