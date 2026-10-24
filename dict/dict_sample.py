dict_examples={
    "name":"Mukesh",
    "age":40,
    "status":False,
    "enrolled":None,
    "courses":["Python","AI"]
}

print(type(dict_examples))
print(dict_examples)
# print(dict_examples["Name"]) #keys are case sensitive and "Name" is not available but "name" is available. So return " KeyError: 'Name'""
print(dict_examples["name"])
print(dict_examples["age"])
print(dict_examples["status"])
print(dict_examples["enrolled"])
print(dict_examples["courses"])
print(dict_examples["courses"][0])
print(dict_examples["courses"][-1])

dict_examples["age"]=45
print(dict_examples["age"])