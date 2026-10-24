# Find All odd numbers between 1 and 50.
# The total count of odd numbers.
# The sum of all odd numbers.
noOfOddNos=0
sumOfOddNos=0
for i in range(1,51):
    if i%2==1:
        noOfOddNos=noOfOddNos+1
        sumOfOddNos=sumOfOddNos+i
        print(i,end=" ")

print("\nnoOfOddNos: ",noOfOddNos)
print("sumOfOddNos: ",sumOfOddNos)