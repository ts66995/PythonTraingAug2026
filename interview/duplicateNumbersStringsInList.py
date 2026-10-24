# Find All Duplicate Numbers in a List
# Approach 1: Using Two Loops
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60] #output: [10, 20, 30]
duplicates = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            if numbers[i] not in duplicates:
                duplicates.append(numbers[i])
print(duplicates)

# Why i + 1?   :Because we want to compare each element with the elements after it, not with itself or the elements we have already checked.
# Approach 2: Using count()
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print(duplicates)
# numbers.count(num): returns the number of times num appears in the list. Interview note: This approach is easy to understand, but it can be inefficient for large lists because count() scans the list each time.

# Approach 3: Using a Set (Recommended)
# numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60] # duplicates numbers in list
numbers = ["Python","JavaScript","Playwright","Python", "TypeScript","Playwright","JavaScript"]# duplicates string in list   #output: ['JavaScript', 'Playwright', 'Python']
unique = set()
duplicates = set()
for num in numbers:
    if num in unique:
        duplicates.add(num)
    else:
        unique.add(num)
print(sorted(duplicates))