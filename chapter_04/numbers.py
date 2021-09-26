# Using the range() Function

# The range() function causes Python to start caunting at the first value you give it, and it stops when it reaches the second value you provide.
# To print the numbers from 1 t0 5, you would use range(1,6)
for value in range(1,5):
    print(value)

# Using range() to Make a List of Numbers
# If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.
numbers = list(range(1,6))
print(numbers)

# Even Numbers
# We can also use the range() function to tell Python to skip numbers in a given range. For example, here's how we would list the even numbers between 1 and 10:
even_numbers = list(range(2,11,2))
print(even_numbers)

# You can create almost any set of numbers you want to using the range() function.
# In Python, two asterisks(**) represent exponents. Here's how you might put the first 10 square numbers into a list:
# We start with empty list called squares[]. We tell Python to loop through each value from 1 to 10 using the range() function. Insdie the loop, the current value is raised the second power and stored in the variable square. And each new value of square is appended to the list squares. Finally, when the loop has finished running, the list of squares is printed.
squares = []
for value in range(1,11): 
    square = value**2
    squares.append(square)

print(squares)

# To write above code more precisely, omit the temporary variable square and append each new value directly to the list:
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

# Simple Statistics with a List of Numbers
# A few Python functions are specific to lists of numbers. For example, you can easily find the minimun, maximum, and sum of a list of numbers:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # output 0
print(max(digits))  # output 9
print(sum(digits))  # output 45 

# List Comprehensions
# The following example builds the same list of square numbers you saw earlier but uses a list comprehension:
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.
# To use this syntax, begin with a descriptive name for the list, such as squares. Next, you open a set of square brackets and define the expression for the values you want to store in the new list. 
# In this example the expression is value**2, which raises the value to the second power. Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets. 
# The for loop in this example is for value in range(1,11), which feeds the value 1 through 10 into the expression value**2.
# Notice that no colon is used at the end of the for statement.
squares = [value**2 for value in range(1,11)]
print(squares)