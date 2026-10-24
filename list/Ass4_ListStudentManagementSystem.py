students=[]
for i in range(1,4):
    print(f"Enter details of Student: {i}")
    name = input("Enter student name: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")

    #individual student
    student=[name,address,phone]
    
    students.append(student)

# Displaying student details
for individualStudent in students:
    name = individualStudent[0]
    address = individualStudent[1]
    phone = individualStudent[2]
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone: {phone}")

