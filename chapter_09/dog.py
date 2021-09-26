# Creating and Using a Class
# ============================

# Creating the Dog Class

# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initiate name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!.")


# # Making an Instance from a Class
# my_dog = Dog('Willie', 6)
# # Accessing Attributes:
# # To Access the attributes of an instance, you use dot notation.
# # eg. my_dog.name
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")

# # Calling Methods
# my_dog.sit()
# my_dog.roll_over()

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)   # Creating Multiple Instances

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.roll_over()  # Calling Methods


print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()  # Calling Methods
