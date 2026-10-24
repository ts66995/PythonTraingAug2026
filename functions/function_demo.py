# This file demonstrates default parameter values in a Python function.
# A default value is used automatically when the caller does not supply
# a value for that parameter.

# Defines a function with three parameters, each having a default value:
# name defaults to "Guest", age defaults to 18, state defaults to "KA".
# These defaults are only used for parameters the caller leaves out.
def display(name="Guest",age=18,state="KA"):
    # Prints a formatted message using an f-string, which lets us insert
    # variable values directly inside the {} braces of the text.
    print(f"Hello : {name}, Age: {age}, State: {state}")


# Calls display with two positional arguments: "Renu" fills name and 26
# fills age. Since no third argument is given, state keeps its default
# value of "KA".
display("Renu",26)