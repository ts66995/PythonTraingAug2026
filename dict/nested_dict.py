student={
    "name": "sreelatha",
    "age":43,
    "courses":["Python","AI"],
    "address":[
        {
            "area":"Sarjapur",
            "zip":"560099"
        },
        {
            "area":"Indiranagar",
            "zip":"560038"
        },
        {
            "area":"MGRoard",
            "zip":"560001"
        }
    ]    
}

print(student["address"])
print(student["address"][0])
print(student["address"][1]["area"])
print(student["address"][-1]["zip"])