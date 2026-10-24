# A nested condition is an if statement placed inside another if statement.
# The inner if is only checked when the outer if's condition has already been found True.
# This is useful when a decision depends on more than one thing being true, checked in stages rather than combined into a single line.

status_code=200

test_case="API Automation"


# Step 1: the outer if checks status_code first. Since status_code is 200, this condition is True, so Python enters this block and moves on to the inner if.
if status_code==200:

    # Step 2: the inner if only runs because the outer condition was already True. It checks whether test_case equals "Web Automation".
    if test_case=="Web Automation":

        print("Test case passed")

    # Step 3: test_case actually holds "API Automation", not "Web Automation", so the inner condition is False and this inner else runs instead.
    else:
        print("Test case failed")

# Step 4: this outer else only runs if the outer condition (status_code==200) had been False. Since it was True, this branch is skipped entirely and never runs in this example.
else:
    print("API call failed")
