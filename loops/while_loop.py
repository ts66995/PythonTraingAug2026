"""
A while loop repeats a block of code as long as a condition stays True.

The difference between a for loop and a while loop is simple:
    for loop   -> use it when we know how many times to repeat
    while loop -> use it when we repeat until some condition becomes False

Every while loop needs three things, and forgetting any one of them causes
problems:
    1. A starting value for the variable, created before the loop.
    2. A condition that is checked before every repetition.
    3. An update to the variable inside the loop, so the condition can
       eventually become False.

If we forget the third point, the condition stays True forever and the
program never stops. That situation is called an infinite loop, and it can
be stopped in the terminal by pressing Ctrl + C.

Dry run:
    i = 0 -> 0 <= 5 is True  -> print and i becomes 1
    i = 1 -> 1 <= 5 is True  -> print and i becomes 2
    i = 2 -> 2 <= 5 is True  -> print and i becomes 3
    i = 3 -> 3 <= 5 is True  -> print and i becomes 4
    i = 4 -> 4 <= 5 is True  -> print and i becomes 5
    i = 5 -> 5 <= 5 is True  -> print and i becomes 6
    i = 6 -> 6 <= 5 is False -> loop stops

Expected output:
Starting the while loop:
Welcome To Loops 0
Welcome To Loops 1
Welcome To Loops 2
Welcome To Loops 3
Welcome To Loops 4
Welcome To Loops 5
End of the while loop.
"""

# Step 1: Print a message before the loop starts.
print("Starting the while loop:")

# Step 2: Create the counter variable and give it a starting value.
# This must be done before the loop, otherwise Python will not know
# what "i" means when it checks the condition.
i = 0

# Step 3: Check the condition before every repetition.
# As long as i is less than or equal to 5, the indented block below runs.
# The moment the condition becomes False, Python jumps out of the loop.
while i <= 5:
    # Step 4: Print the current value of the counter.
    print("Welcome To Loops", i)

    # Step 5: Increase the counter by 1.
    # This is the most important line of a while loop. It moves the
    # counter towards the value that will make the condition False.
    # Without this line the loop would run forever.
    i = i + 1

# Step 6: This line is outside the loop, so it runs only once,
# after the condition has become False and the loop has finished.
print("End of the while loop.")
