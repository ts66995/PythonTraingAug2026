test_cases=[
   {
        "id":1,
        "name":"Valid Login",
        "status":"Passed"
    },
    {
        "id":2,
        "name":"Invalid Login",
        "status":"Failed"
    }, 
    {
        "id":3,
        "name":"Logout",
        "status":"Passed"
    }
    
]
for tc in test_cases:
    print(tc["id"],tc["name"],tc["status"])