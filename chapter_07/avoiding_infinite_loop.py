# Avoiding Infinite Loops

#   Every while loop needs a way to stop running so it won't continue to run forever. For example, this counting loop should count from 1 t0 5:

x = 1 
while x <= 5:
    print(x)
    x += 1 


#   But if you accidentally omit the line x += 1 ( as shown next), the loop will run forever:

# This loop runs forever!
x = 1
while x <= 5:
    print(x)

# If your program gets stuck in an infinite loop, Prss CTRL-C or just close the terminal window displaying your program's output.