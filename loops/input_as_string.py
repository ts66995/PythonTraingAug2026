"""
This program shows how to take input from the user while the program is
running, instead of writing fixed values inside the code.

The input() function does two jobs:
    1. It displays the message we pass inside the brackets, so the user knows
       what to type. This message is called a prompt.
    2. It pauses the program and waits until the user types something and
       presses the Enter key.

Whatever the user types is returned as a string (text) and we store it in a
variable so that we can use it later in the program.

Sample run:
Starting of the program
Enter First Name :Mukesh
Enter Last Name :Otwani
Enter Address :Delhi
First Name is: Mukesh
Last Name is: Otwani
Address is: Delhi
End of the program
"""

# Step 1: Print a message so we know the program has started running.
print("Starting of the program")

# Step 2: Ask the user for the first name.
# The program stops here and waits for the user to type and press Enter.
# The typed value is then stored inside the variable f_name.
f_name = input("Enter First Name :")

# Step 3: Ask for the last name and store it in l_name.
# This line runs only after the previous input has been entered.
l_name = input("Enter Last Name :")

# Step 4: Ask for the address and store it in address.
address = input("Enter Address :")

# Step 5: Display the values that we collected.
# The text inside quotes is printed as it is, and after the comma the
# value stored in the variable is printed.
print("First Name is:", f_name)
print("Last Name is:", l_name)
print("Address is:", address)

# Step 6: Print a closing message so we know the program finished properly.
print("End of the program")
