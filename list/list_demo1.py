# This file shows how a list can hold duplicate values and how new items can be added
# to the end of a list using the append method. It also shows how the last item of a
# list can be removed using the pop method.

# "GenAI" appears three times here. Lists allow duplicate values, unlike sets.
list_demo=["GenAI","RAG","LangChain",1.61,False,89,"GenAI","GenAI"]

# Prints the list as it looks before any items are added or removed.
print(list_demo)

# append() adds one new item to the end of the list.
list_demo.append("LangFlow")

# Each append() call adds only one item, so this adds "LangSmith" after "LangFlow".
list_demo.append("LangSmith")

# This adds "DeepEval" after "LangSmith", making three new items added in total.
list_demo.append("DeepEval")

# Prints the list after the three append() calls, showing all the new items at the end.
print(list_demo)

# pop() removes the last item from the list by default and returns the removed value.
list_demo.pop()

# Prints the list after pop() has removed "DeepEval", the item that was last in the list.
print(list_demo)

# insert method to explore

# remove method to explore

