def calculate_average(numbers:list)->float:
    total=0
    for i in numbers:
        total+=i 
    avg_numbers=total/len(numbers)

    return avg_numbers
# numbers=[10,20,30,40,50]
# res=calculate_average(numbers)
# print(res) 

numbers=[]
for i in range(5):
    entered_numbers=float(input("Enter the number ")) #if you enter 25.5, Python raises a ValueError because int() cannot directly convert the string "25.5" into an integer.
    numbers.append(entered_numbers)

res=calculate_average(numbers)
print(res) 
  