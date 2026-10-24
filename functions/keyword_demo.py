# This file demonstrates two ways of passing arguments to a function:
# keyword arguments and positional arguments.

# Defines a function with three parameters, each with a default value.
# These defaults only apply when the caller does not provide that argument.
def display(name="Guest",age=18,state="KA"):
    print(f"Hello : {name}, Age: {age}, State: {state}")

# Keyword arguments: each value is matched to a parameter by name
# (state=, name=, age=) instead of by position. This means the order
# they are written in does not matter, since Python knows exactly which
# parameter each value belongs to.
display(state="UP",name="Abhishek",age=28)

# Positional arguments: values are matched to parameters purely by their
# order. "Prashant" goes to name, 26 goes to age, and "MH" goes to state,
# because that is the order the parameters were defined in the function.
display("Prashant",26,"MH")