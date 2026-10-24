"""
This program shows how to run a for loop backwards, that is from a bigger
number to a smaller number.

The range() function can accept three values: range(start, stop, step).
    start -> the number where counting begins (this number is included)
    stop  -> the number where counting must end (this number is NOT included)
    step  -> how much to jump every time

Normally the step is +1, so numbers go up. If we give a negative step such as
-2, the numbers go down instead. That is why the loop below starts at 10 and
keeps subtracting 2 until it reaches a value that is not greater than 5.

Dry run of range(10, 5, -2):
    i = 10 -> 10 is greater than 5, so the loop body runs
    i = 8  -> 8 is greater than 5, so the loop body runs
    i = 6  -> 6 is greater than 5, so the loop body runs
    i = 4  -> 4 is not greater than 5, so the loop stops here

Expected output:
Starting the for loop:
Welcome To Loops 10
Welcome To Loops 8
Welcome To Loops 6
End of the for loop.

Common mistake to avoid:
Writing range(10, 5) without the -2 step will print nothing at all, because
Python tries to count upwards from 10 to 5 and there is nothing to count.
"""

# Practice questions to try on your own using loops:
# find all prime numbers between 10 and 50
# find all even numbers between 10 and 50
# find all duplicate numbers in a list
# find all duplicate strings in a list

# Step 1: Show a message before the loop begins so we can clearly see
# where the looping part starts in the output.
print("Starting the for loop:")

# Step 2: Start the loop from 10, stop before 5, and decrease by 2 each time.
# The negative step (-2) is what makes this loop count in reverse.
for i in range(10, 5, -2):
    # Step 3: This indented line runs once for every value of i,
    # which gives us 3 lines in the output (10, 8 and 6).
    print("Welcome To Loops", i)

# Step 4: This line is outside the loop, so it runs only once at the end.
print("End of the for loop.")

# Collection data types that we can also loop through, exactly the way we
# looped through the numbers above. We will cover these one by one:
# list
# tuple
# dictionary
# set
