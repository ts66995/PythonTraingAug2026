# Find All Even Numbers Between 10 and 50
for num in range(10, 51):
    if num % 2 == 0:
        print(num, end=" ")
        even_numbers = []
# Alternative: Store the Even Numbers in a List
for num in range(10, 51):

    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)