# Write the table in th format 3X1=3 to3X10=30 and take in put from the user do you want another table if 'yes' then print that table. if "no" then exit.
isAnotherTableRequired="yes"
while isAnotherTableRequired=="yes":
    number=int(input("Enter the table number:"))
    for i in range(1,11):
        print(f" {number} X {i} = ",number*i)
    isAnotherTableRequired=input("Do you want to print another table?(yes/no) :").lower()
