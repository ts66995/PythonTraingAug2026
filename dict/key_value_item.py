student={
    "name":"Sreelatha",
    "age":40,
    "grade":"A"
}

print("Keys: ")
for x in student.keys():
    print(x)

print("Values: ")
for x in student.values():
    print(x)

print("Items: ")
for x in student.items():
    print(x)

print("Items unpacked as Key,values: ")
for key,value in student.items():
    print(key,value)