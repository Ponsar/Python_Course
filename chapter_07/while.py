# Introducing while loops

#   The for loop takes a collection of items and executes a block of code once for each time in the collection. In contrast, the while loop runs as long as, or while, a certain condition is true.

# The while loop in Action
#   You can use a while loop to count up through a series of numbers. For exxample, the following while loop counts from 1 to 5:
current_number = 1 
while current_number <= 5:
    print(current_number)
    current_number += 1 # (The += operator is shorthand for current_number = current_number + 1.)


## Letting the User Choose When to Quit
#   We can make the program run as long as the user wants by putting most of the program inside a while loop. We'll define a quit value and then keep the program running as long as the user has not entered the quit value.


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = " "
# while message != 'quit':
#     message = input(prompt)
#     print(message)


#   The first time through the loop, message is just an empty string, so Python enters the loop. At message = input(prompt), Python displays the prompt and waits for the user to enter their input. Whatever they enter is stored in message and printed; then, Python reevaluates the condition in the while statement.
#   As long as the user has not entered the word 'quit', the prompt is displayed again and Python waits for more input. When the user finally enters 'quit', Python stops executing the while loop and the program ends:
#   This program works well, except that it prints the word 'quit' as if it were an actual message. A simple if test fixes this:


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = " "
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)


# Now the program makes a quick check before displaying the message and only prints the message if it does not match the quit value:


## Using a flag
#   In the previous example, we had the program perform certain tasks while a given condition was true. But what about more complicated programs in which many different events could cause the program to stop running?
#   For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active.
#   This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag is set True and stop running when any of several events sets the value of the flag to False. As a result, our overall while statement needs to check only one condition: whether or not the flat is currently True. 
#   Then, all our other tests ( to see if an event has occurred that should set the flag to False) can be neatly organized in the rest of the program.



prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# This program has the same output as the previous example where we placed the conditional test directly in the while statement. 
# But now that we have a flag to indicate whether the overall program is in an active state, 
# it would be easy to add more tests ( such as elif statements) for events that should cause active to become False. 
# This is useful in complicated programs like games in which there may be many events that should each make the program stop running. 
# When any of these events causes the active flag to become False, the main game loop will exit, a Game Over message can be displayed, and the player can be given the option to play agian.