# This file shows what a nested list is, meaning a list that contains other lists
# inside it as its items. It shows how to reach an item inside one of those inner
# lists by using two index numbers together, one right after the other.

# tools is a list of four items, and each of those items is itself a list.
# Index 0 is ["Python","JS","C#"], index 1 is ["N8N","LangChain"], and so on.
tools=[["Python","JS","C#"],["N8N","LangChain"],[12,13.5,89],[True,False]]

# tools[1] first picks the inner list at index 1, which is ["N8N","LangChain"].
# Adding [1] after that picks index 1 of that inner list, which is "LangChain".
print(tools[1][1])
# tools[-2] first picks the second-last inner list, which is [12,13.5,89].
# Adding [-2] after that picks the second-last item of that inner list, which is 13.5.
print(tools[-2][-2])





