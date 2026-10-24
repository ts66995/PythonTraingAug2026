# This file shows how a for loop is used to go through every item in a list one at a
# time. It also shows how the break statement can stop a loop early once a specific
# condition is met, instead of letting the loop continue through the rest of the items.

tools=["GenAI","RAG","LangChain","LangFlow"]

# This for loop visits each item in the tools list, one by one, from start to end.
# On every round, "value" holds whichever item is currently being looked at.
for value in tools:
    # Prints the current item being visited in this round of the loop.
    print(value)
    # Checks whether the current item is exactly the text "LangFlow".
    if value=="LangFlow":
        print("LangFlow found!")
        # break stops the loop immediately, so any items after "LangFlow" are skipped.
        break