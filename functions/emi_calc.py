# This file shows how to use functions that were written in a different
# file (calc.py) instead of writing that logic again from scratch.
# This is one of the main benefits of functions: write once, reuse anywhere.

# This imports four specific functions from calc.py so we can call them here.
# When this line runs, Python opens calc.py and runs it top to bottom, which
# is why you will see the "Calculator module loading" messages printed too.
from calc import subtract,sum,divide,multiply

# Calls the sum function with 10 and 5, then prints whatever it returns (15).
print(sum(10, 5))

# Calls the multiply function with 10 and 5, then prints the result (50).
print(multiply(10, 5))

# Calls the divide function with 15 and 5, then prints the result (3.0).
print(divide(15,5))

# Calls the subtract function with 20 and 5, then prints the result (15).
print(subtract(20, 5))

