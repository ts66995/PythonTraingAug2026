# This is the simplest possible example of a class: one with a constructor
# that does nothing, and one method that just prints a message.

class Sudip:

    # "pass" is a placeholder that means "do nothing here". It is used
    # when Python requires a block of code (like inside a function) but
    # there is nothing to actually run. Without "pass", this empty
    # __init__ would cause a syntax error.
    def __init__(self):
        pass

    def m1(self):
        print("Method m1 called")


# Step 1: Creates a Sudip object. This runs __init__, which does nothing
# because of the "pass" statement, so nothing is printed at this point.
ob1=Sudip()

# Step 2: Calls the m1 method on ob1, which prints "Method m1 called".
ob1.m1()