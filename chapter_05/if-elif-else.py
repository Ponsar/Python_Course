# Often, you'll need to test more than two posible situations, and to evaluate these you can use Python's if-elif-else syntax. Python executes only one block in an if-elif-else chain. It runs each conditional test in order until one passes. When a test passes, the code following that test is executed and Python skips the rest of the test..
# Many real-world situations involve more than two possible conditions. for example, consider an amusement park that charges different rates for different age groups:
#   * Admission for anyone under age 4 is free.
#   * Admission for anyone between the ages of 4 and 18 is $5.
#   * Admission for anyone age 18 or older is $10.
# The following code tests for the age group of a person and then prints an admission price message:
age = 12   
if age < 4:    
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")   

# Any age greate than 17 would cause the first two tests to fail. In these situations, the else block would be executed and the admission price would be $10.
#   Rather than printing the admission price within the if-elif-else block, it would be more concise to set just the price inside the if-elif-else chain and then have a simple print statement that runs after the chain has been evaluated:
# This code produces the same output as the previous example, but the purpose of the if-elif-else chain is narrower. Instead of determining a price and displaying a message, it simply determines the admission price.
# In addition to being more efficient, this revised code is easier to modify than the original approach. To change the text of the output message, you would need to change only one print statement rather than three separate print statement.
age = 18

if age < 4:
    price = 0 
elif age < 18:
    price = 5
else:
    price = 10 

print("\nYour admission cost is $" + str(price) + ".")
