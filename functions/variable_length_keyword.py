# This file shows how a function can accept a variable (changing) number of
# keyword arguments using **kwargs, and how *args and **kwargs can be
# combined together with normal parameters in the same function.

# **kwargs collects any keyword arguments (name=value pairs) the caller
# passes in, and stores them together as a dictionary. Here, kwargs will
# hold {"name": "Mukesh", "location": "BLR", "age": 30, "course": "Python",
# "email": "mukesh@example.com"}.
def display_user(**kwargs):
    # Reads the value stored under the "location" key from that
    # dictionary, printing "BLR".
    print(kwargs["location"])


# Step 1: Every argument here is passed as a keyword argument (name=value),
# so all five of them are collected together inside kwargs.
display_user(name="Mukesh",location="BLR",age=30,course="Python",email="mukesh@example.com")


# num1 and num2 capture the first two positional arguments as usual.
# *args then collects any further positional arguments as a tuple.
# **kwargs collects any keyword arguments as a dictionary.
# A function can use *args and **kwargs together, but *args must always
# be written before **kwargs in the parameter list.
def display_details(num1,num2,*args,**kwargs):
    # args[1] reads the second item stored inside the args tuple.
    print(args[1])


# Step 2: num1=10 and num2=20 fill the named parameters. The remaining
# positional values 30 and 40 go into args as (30, 40), so args[1] is 40.
# name="Mukesh" and location="BLR" are keyword arguments, so they go into
# kwargs, but kwargs is never used inside this particular function.
display_details(10,20,30,40,name="Mukesh",location="BLR")
