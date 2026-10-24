def sum_even_numbers():
    total=0
    for num in range(0,31):
        if(num%2==0):
            total=total+num
    return total
result=sum_even_numbers()
print(f"Sum of even numbers: {result}")
