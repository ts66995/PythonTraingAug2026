"""
A for loop is used when we already know how many times we want to repeat
something. Instead of writing the same print statement 4 times, we write it
once inside a loop and Python repeats it for us.

Here we use the range() function to generate numbers. The loop picks up one
number at a time, stores it in a variable, runs the code inside the loop, and
then comes back for the next number. When no numbers are left, the loop stops
and Python continues with the lines written after the loop.

Important rule to remember about range(start, stop):
The start value is included, but the stop value is NOT included.
So range(1, 5) gives us 1, 2, 3, 4 and stops before 5.

Expected output:
Starting the for loop:
Welcome To Loops 1
Welcome To Loops 2
Welcome To Loops 3
Welcome To Loops 4
End of the for loop.
"""

# Step 1: Print a message before the loop starts.
# This line runs only once because it is written outside the loop.
print("Starting the for loop:")

# Step 2: Create the loop.
# range(1, 5) produces the numbers 1, 2, 3, 4 (5 is excluded).
# The variable "i" holds one number at a time in every repetition.
for i in range(1, 5):
    # Step 3: This line is indented, so it belongs to the loop body.
    # It runs once for every number, which means 4 times in total.
    # The comma inside print() automatically adds a space between the
    # text and the value of i.
    print("Welcome To Loops", i)

# Step 4: Print a message after the loop is finished.
# The indentation is removed here, so Python knows this line is outside
# the loop and should run only once, after all repetitions are done.
print("End of the for loop.")
