# This file defines simple math functions (add, multiply, divide, subtract)
# that other files can import and reuse instead of rewriting the same logic.
# In Python, a file like this that only contains functions/variables to be
# imported elsewhere is called a "module".

# This line runs immediately the moment this file is imported anywhere.
# It helps us see, in the console, exactly when this module starts loading.
print("Calculator module loading")

# Adds two whole numbers together and gives back the result.
# "num1: int" and "num2: int" are type hints telling readers (and tools)
# that these inputs are expected to be integers.
# "-> int" is a type hint saying this function returns an integer.
# Type hints are optional in Python; they don't stop other types from
# being passed in, they just document the intention.
def sum(num1: int, num2: int) -> int:
    result=num1+num2  # add the two numbers and store the answer
    return result      # send the answer back to whoever called this function

# Multiplies two numbers and returns the product.
# No type hints here, so it will work with integers, floats, etc.
def multiply(num1,num2):
    result=num1*num2
    return result

# Divides the first number by the second number and returns the result.
# Note: if num2 is 0, this will raise a ZeroDivisionError, since dividing
# by zero is not allowed in math or in Python.
def divide(num1,num2):
    result=num1/num2
    return result

# Subtracts the second number from the first number and returns the result.
def subtract(num1,num2):
    result=num1-num2
    return result

# This line runs right after all the functions above have been defined,
# confirming that the module finished loading without errors.
print("Calculator module loaded successfully")