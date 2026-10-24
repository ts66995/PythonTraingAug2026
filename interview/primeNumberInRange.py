# Find All Prime Numbers Between 10 and 50
import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
for num in range(10, 51):
    if is_prime(num):
        print(num, end=" ")

"""
        Why do we use end=" " in Python?

In Python, the print() function automatically moves to a new line after printing something.

By using end=" ", we tell Python to print a space instead of moving to a new line.

Let's understand this with examples.

1. Without end=" "
for num in range(10, 16):
    print(num)

Output:

10
11
12
13
14
15

Explanation:

range(10, 16) generates numbers from 10 to 15.
print(num) prints each number.
By default, print() adds a newline (\n) after every number.

Therefore, each number appears on a separate line.

2. With end=" "
for num in range(10, 16):
    print(num, end=" ")

Output:

10 11 12 13 14 15

Explanation:

The statement:

print(num, end=" ")

tells Python to:

Print the value of num.
Add a space after the number.
Stay on the same line instead of moving to a new line.

This is useful when we want to display multiple numbers on a single line.

3. Understanding the end parameter

The end parameter determines what Python prints at the end of each print() statement.

Code	Output	Explanation
print(num)	10 followed by a new line	Default behavior
print(num, end=" ")	10	Adds a space
print(num, end="")	10	Adds nothing
print(num, end=", ")	10,	Adds a comma and a space
print(num, end="\n")	10 followed by a new line	Explicitly adds a newline
"""