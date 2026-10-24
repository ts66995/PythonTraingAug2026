# This file shows how the enumerate function can be used with a for loop to get both
# the position number and the value of each item in a list at the same time, instead
# of only getting the value like a normal for loop does.

tools=["GenAI","RAG","LangChain","LangFlow"]

#Iterable object - String,List,Set,Dic,Tuple
# An iterable is any object that can be looped over item by item, such as these types.

# enumerate() wraps the list and produces pairs of (position, value) for each item.
# Here "index" holds the position number and "value" holds the item at that position.
for index, value in enumerate(tools):
    # Only the value is printed here, even though the index is also available above.
    print(index,value)

# explore sort and explore reverse



