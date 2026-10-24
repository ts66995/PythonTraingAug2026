numbers=[10,20,30,40,50]
def calculate_sum(numbers:list)->int:
    total=0
    for num in numbers:
        total=total+num
    return total

result=calculate_sum(numbers)
print(f"Total Sum: {result}")