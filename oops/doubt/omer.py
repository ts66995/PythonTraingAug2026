# This file shows the order in which constructors and overridden methods
# run when a child class inherits from a parent class, and both define
# their own version of __init__ and demo.

class Parent:
    def __init__(self):
        print("Parent class constructor called")

    def demo(self):
        print("Parent class demo method called")

class Child(Parent):
    # Child defines its own __init__, so creating a Child object runs
    # this version, not the Parent's. Note that this __init__ does not
    # call super().__init__(), so the Parent's constructor message never
    # prints when a Child object is created.
    def __init__(self):
        print("Child class constructor called")

    # Child overrides demo(). super().demo() explicitly calls the Parent's
    # version first, so both messages print, Parent's message before
    # Child's message.
    def demo(self):
        super().demo()
        print("Child class demo method called")


# Step 1: Creates a Child object. Only "Child class constructor called"
# prints here, because Child's __init__ does not call the Parent's __init__.
obj1=Child()
# Step 2: Calls demo() on obj1. Since obj1 is a Child, Child's demo() runs,
# which first calls the Parent's demo() through super(), then prints its
# own message. Output: "Parent class demo method called" followed by
# "Child class demo method called".
obj1.demo()

