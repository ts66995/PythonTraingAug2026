# Conditional statements let a program make decisions and run different code depending on whether something is True or False.
# The if keyword runs a block of code only when its condition is True.
# The else keyword runs a block of code only when that condition is False.
# A condition is usually created using a comparison operator, such as >=, ==, or the logical keyword "and".

print("Start of the program")

marks=15

# Step 1: status is a variable that stores the result of a comparison, not the comparison itself.
# marks>=35 checks whether marks is 35 or higher. Since marks is 15, this comparison evaluates to False, so status becomes False.
status= marks>=35

# Step 2: because status is False, the if block is skipped and the else block runs instead, printing "Fail".
if status:
    print("Pass")
else:
    print("Fail")

status_code=404

# Step 3: the "and" keyword combines two conditions into one. Both conditions must be True for the overall result to be True.
# Here it checks that status_code is 200 or more AND less than 300, which is the typical range for a successful HTTP response.
# Since status_code is 404, the first condition (status_code>=200) is True but the second (status_code<300) is False, so the combined result is False.
if status_code>=200 and status_code<300:
    print("API call successful")
else:
    print("API call failed")

print("End of the program")
