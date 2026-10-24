# In Python, every value stored in a variable has a data type.
# Python figures out the data type automatically based on the value you give it - you never have to declare it yourself.
# This is called dynamic typing.
# This file creates a variable of each common data type and then uses the type() function to confirm what type Python assigned to it.

num1=15
# Step 1: num1 is a whole number with no decimal point. In Python this type is called int (integer).
print(num1)
print(type(num1))

num2=15.25
# Step 2: num2 is a number that includes a decimal point. In Python this type is called float.
print(num2)
print(type(num2))

status=False
# Step 3: status can only hold one of two values, True or False. In Python this type is called bool (boolean). Booleans are commonly the result of a comparison.
print(status)
print(type(status))

full_name="Sreelatha"
# Step 4: full_name holds text, written inside quotes. In Python this type is called str (string).
print(full_name)
print(type(full_name))

list1=[1,2,3,4,5]
# Step 5: list1 holds several values together inside square brackets, in a specific order. In Python this type is called a list. Items in a list can be added, removed, or changed later, and each item can be accessed by its position (index).
print(list1)
print(list1[3])
print(type(list1))

dict1={"name":"Sreelatha","age":40}
# Step 6: dict1 holds data as key-value pairs inside curly braces. In Python this type is called a dict (dictionary). Instead of accessing a value by position like a list, you access it using its key, for example dict1["name"].
print(dict1)
print(dict1["name"])
print(type(dict1))
