# This file demonstrates a couple of basic built-in operations you can
# perform on Python strings.

# Creates a variable named "name" and stores the text "Omer" in it.
name="Omer"

# len() is a built-in function that counts the number of characters in a
# string. "Omer" has 4 characters, so this prints 4.
print(len(name))

# .upper() is a built-in string method that returns a new version of the
# string with every letter converted to uppercase. This prints "OMER".
# The original "name" variable is not changed, since strings are immutable
# in Python (they cannot be modified in place).
print(name.upper())

