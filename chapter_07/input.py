# How the input() Function Workd

#   The input() function pauses your program and waits for the user to enter some text. Once Python receives the user's input, it stores it in a variable to make it convenient for you to work with.
#   For example, the following program asks the user to enter some text, then displays that message back to the user:
message = input("Tell me somethings, and I will repeat it back to you: ")
print(message)

#   Writing Clear Promts
name = input("Please enter your name: ")
print("Hello, " + name + "!")

#   Sometimes you'll want to write a prompt that's longer than one line. For example, you might want to tell the user why you're asking for certain input.
#   You can store your prompt in a variable and pass that variable to the input() function. This allows you to build your prompt over several lines, then write a clean inut() statement.
#   This example shows one way to build a multi-line string. The first line stores the first part of the messsage in the variable prompt.
#   In the second line, the operator += takes the string that was stored in prompt and adds the new string onto the end.

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print("\nHello, " + name + "!")
#   The prompt now spans two lines.
