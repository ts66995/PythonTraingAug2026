# This file explains what a Python list is and how it can hold different data types together,
# such as text, decimal numbers, boolean values and whole numbers, all inside the same list.
# It also shows how to check a list's type and how to access items in it using position
# numbers called index numbers, counting from both the front and the back of the list.


# A list is created using square brackets, with each item separated by a comma.
# Notice this single list holds a string, a float, a boolean and an integer together.
list_demo=["GenAI","RAG","LangChain",1.61,False,89]

#list_demo1=["GenAI","RAG","LangChain","LangFlow"]

# Prints the entire list exactly as it is, including the square brackets and commas.
print(list_demo)

# type() tells us what kind of object list_demo is. This line prints <class 'list'>.
print(type(list_demo))

# List indexing starts at 0, so index 0 gives the very first item in the list.
print(list_demo[0])
# This list has 6 items in total (indexes 0 to 5), so index 5 gives the last item.
print(list_demo[5])
# This line is commented out because index 6 does not exist in a 6-item list
# and running it would raise an IndexError.
#print(list_demo[6])
# Negative indexing counts backwards from the end of the list, so -1 is the last item.
print(list_demo[-1])
# -2 is the second last item in the list.
print(list_demo[-2])
# This list only has 6 items, so the valid negative index range is -1 to -6.
# -7 goes beyond that range, so this line will raise an IndexError when it runs.
print(list_demo[-7])