"""
This program adds two numbers entered by the user, and explains one of the
most common mistakes made by beginners.

The point to remember is that input() always returns a string, even when the
user types a number. So if the user enters 10 and 20, Python actually stores
the text "10" and the text "20", not the numbers 10 and 20.

If we add two strings, Python joins them instead of adding them:
    "10" + "20" gives "1020"        (joining, called concatenation)
    10 + 20 gives 30                (real addition)

To get real addition, we must first convert the text into a number. This is
called type casting, and we do it using:
    int(value)   -> converts to a whole number, for example 10
    float(value) -> converts to a decimal number, for example 10.5

Here we use float() so that the program also works when the user enters
decimal values like 10.5 and 20.5.

The type() function is used only to check what data type a value is. It is
not needed for the calculation, we are printing it just to prove that the
input came in as a string.

Sample run:
Starting of the program
Enter First Number :10
<class 'str'>
Enter Second Number :20
<class 'str'>
Sum is 30.0
End of the program
"""

# Step 1: Print a message so we know the program has started.
print("Starting of the program")

# Step 2: Ask the user for the first number.
# Even if the user types 10, it is stored as the text "10".
num1 = input("Enter First Number :")

# Step 3: Check the data type of num1.
# This prints <class 'str'>, which proves that the value is a string
# and not a number, even though it looks like a number on the screen.
print(type(num1))

# Step 4: Ask the user for the second number and store it in num2.
num2 = input("Enter Second Number :")

# Step 5: Check the data type of num2 as well. It is also a string.
print(type(num2))

# Step 6: Convert both strings into decimal numbers using float(),
# and then add them. The conversion happens first, and only after that
# the + sign performs real addition instead of joining the text.
# Note: "sum" is already the name of a built-in Python function, so in
# real projects it is better to use a different name such as total.
sum = float(num1) + float(num2)

# Step 7: Display the result.
# The answer prints with a decimal point (for example 30.0) because
# float() was used for the conversion.
print("Sum is", sum)

# Step 8: Print a closing message so we know the program finished properly.
print("End of the program")
