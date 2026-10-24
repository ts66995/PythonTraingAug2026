# This file shows how to check several possible conditions one after another using if, elif, and else.
# elif is short for "else if". Python checks each condition from top to bottom and runs the first block whose condition is True.
# Once a matching block runs, Python skips every condition below it.
# else acts as a fallback and only runs if none of the conditions above it were True.

status_code=500

# make a range of status code
if status_code==100:
    print("information")
# Step 1: Python checks status_code == 200 first. Since status_code is 500, this is False, so Python moves on to the next check.
if status_code == 200:
    print("Success")
# Step 2: Python checks status_code == 300 next. This is also False, so it keeps moving down the chain.
elif status_code == 300:
    print("Redirect")
# Step 3: Python checks status_code == 400 next. Still False, so it continues.
elif status_code == 400:
    print("Client Error")
# Step 4: Python checks status_code == 500. This is True, so "Server Error" is printed and every condition after this is skipped.
elif status_code == 500:
    print("Server Error")
# Step 5: this else would only run if none of the conditions above matched. Since a match was already found above, this line does not run.
else:
    print("Unknown Status Code")
