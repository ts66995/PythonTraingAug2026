# This file shows how a function can accept a variable (changing) number of
# extra arguments using *args, in addition to its normal named parameters.

# num1 and num2 have default values of 0, so they work fine even if the
# caller supplies fewer arguments than expected.
# *args collects any additional positional arguments the caller passes,
# beyond num1 and num2, and stores them together as a tuple.
# Note: naming this function "sum" reuses the name of Python's own
# built-in sum() function; that built-in is no longer usable under the
# name "sum" inside this file once this function is defined.
def sum(num1=0,num2=0,*args):

    # Step 1: Adds only the two named parameters first.
    total=num1+num2
    # Step 2: Goes through every extra value stored in args, one at a
    # time, and keeps adding each one to the running total.
    for num in args:
        total =num+total
    # Step 3: Sends back the final combined total to the caller.
    return total

# Step 4: Calls sum with three values. 12 goes to num1, 15 goes to num2,
# and 55 (the extra value) goes into args as (55,). total becomes
# 12 + 15 = 27, then 55 + 27 = 82 inside the loop, so result becomes 82.
result=sum(12,15,55)

# Step 5: Prints the final result, 82.
print(result)
