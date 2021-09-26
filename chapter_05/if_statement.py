
# if statement
#   When you understand conditional tests, you can start writing if statements. Several different kinds of "if statement" Several different kinds of if statements exist, and your choice of which to use depends on the number of conditions you need to test. You saw several examples of if statement in the discussion about conditional tests, but now let's dig deeper into the topic.
# if condition_test:
#       do something
# Indentatation plays the same role in if statements as it did in "for" loops. All indented lines after an "if" statement will be executed if the test passes, and the entire block of indented lines will be ignored if the test does not pass.

age = 19 
if age >= 18: 
    print("You are old enough to vote!")

# You can have many lines of code as you want in the block following the if statement. Let's add another line of output:
# The conditional test passes, and both print statements are indented, so both lines are printed:
age = 20 
if age >= 19:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")