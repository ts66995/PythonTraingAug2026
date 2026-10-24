"""
Until now we used a for loop with range() to repeat over numbers. But a for
loop can also repeat over the items of a collection, and a list is the most
commonly used collection in Python.

A list is an ordered group of values written inside square brackets and
separated by commas. It can hold text, numbers, or a mix of both.

When we loop over a list, we do not need range() and we do not need to
calculate the size of the list. Python simply hands over one item at a time,
from the first item to the last item, and stops automatically after the last
one. This is very useful in automation work, where we often keep a list of
tool names, browser names, test case names or URLs and want to process each
of them the same way.

Expected output:
Selenium
Playwright
LangChain
Puppeteer
BeautifulSoup
"""

# Step 1: Create a list of tool names.
# Square brackets [ ] tell Python this is a list.
# Each value inside quotes is a string, and the items stay in the same
# order in which we wrote them.
tools = ["Selenium", "Playwright", "LangChain", "Puppeteer", "BeautifulSoup"]

# Step 2: Loop through the list.
# In the first repetition the variable "t" holds "Selenium",
# in the second repetition it holds "Playwright", and so on until the
# last item is finished. The name "t" is our own choice, we could also
# call it "tool" to make the code easier to read.
for t in tools:
    # Step 3: Print the item that is currently stored in t.
    # Because this line is indented, it runs once for every item,
    # so we get 5 lines of output for a list of 5 items.
    print(t)
