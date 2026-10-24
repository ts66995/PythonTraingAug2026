# This file explains what a tuple is and how it is similar to a list but cannot be
# changed after it is created. It shows how to access tuple items using index numbers
# and what error occurs when trying to modify a tuple item.

# A tuple is created using round brackets instead of the square brackets used for lists.
tuple_demo=("Python","JS","C#")
# Prints the tuple exactly as it is, including the round brackets and commas.
print(tuple_demo)
# type() confirms this object is a tuple, so this line prints <class 'tuple'>.
print(type(tuple_demo))
# Tuples also use zero-based indexing, so index 0 gives the first item.
print(tuple_demo[0])
# -1 gives the last item, counting backwards from the end of the tuple.
print(tuple_demo[-1])

# Tuples are immutable, meaning the items inside them cannot be changed after creation.
# This line tries to replace the first item and will raise a TypeError:
# 'tuple' object does not support item assignment.
tuple_demo[0]="Java"
print(tuple_demo)

# append, remove , insert, pop
# Tuples are immutable, so these operations are not available for tuples.