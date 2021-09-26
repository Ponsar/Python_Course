# A Dicionary of Similar Objects
#   The previous example involved storing different kinds of information about one object, an alien in a game. You can also use a dictionary to store one kind of information about many objects.
#   For example, say you want to poll a number of people and ask them what their favorite programming language is. A dictionary is useful for storing the results of a simple poll, like this:
# As You see, we've broken a larger dictionary into several lines. Each key is the name of a person who responded to the poll, and each value is their language choice.
# When you know you'll need more than one line to define a dictionary, press ENTER after the openning brace. Then indent the next line one level(four braces), and write the first key-value pair, followed by a comma. From this point forward when you press ENTER, you text editor should automatically indent all subsequent key-value pairs to match the first key-value pair.
#   Once you've finished defining the dictionary, add a closing brace on a new line after the last key-value pair and indent it one level so it aligns with the keys in the dictionary. It's good practice to include a comma after the lasy key-value pair as well, so you're ready to add a new key-value pair on the next line.
favorite_languages = {
    'Jen': 'python',
    'Zamiram': 'c',
    'Pongsar': 'python',
    'Dxram': 'ruby',
    'Phil': 'c++'
    }

print("Pongsar's favorite language is " + 
    favorite_languages['Pongsar'].title() + 
    ".")

print("\nPongsar's favorite language is " + favorite_languages['Pongsar'].title() + ".")
#   This example also shows how you can break up a long print statement over several lines. The word print is shorter than most dictinary names, so it makes sense to include the first part of what you want to print right after the openning parenthesis.
#   Choose an appropriate point at which to break what's being printed, and add a concatenation operator (+) at the end of the first line. Press ENTER and then press TAB to align all subsequent lines at one indentation level under the print statement. When you've finished composing your output, you can place the closing parenthesis on the last line of the print block.
