# till 3.10 - we had switch case in python in earlier versions, but now we have match case in python 3.10 and above
# match-case works like a switch statement in other languages. It takes one value and compares it against a list of possible patterns (cases), running the block for the first pattern that matches.

status_code=600

# Step 1: match takes the value stored in status_code and compares it against each case below, checked one at a time, in order.
match status_code:
    # Step 2: this case only runs if status_code is exactly 200.
    case 200:
        print("Success")
    # Step 3: this case only runs if status_code is exactly 300.
    case 300:
        print("Redirect")
    # Step 4: this case only runs if status_code is exactly 400.
    case 400:
        print("Client Error")
    # Step 5: this case only runs if status_code is exactly 500.
    case 500:
        print("Server Error")
    # Step 6: case _ is the wildcard pattern, it matches any value that did not match one of the cases above.
    # Since status_code is 600 and none of the earlier cases matched it, this default case runs and prints "Unknown Status Code".
    case _: #default case
        print("Unknown Status Code")
