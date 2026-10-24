def validate_login(username:str,password:str)->str:
    if username=='admin' and password=="admin123":
        return "Login Successful"
    else:
        return "Login Failed" 
entered_username=input("Enter username: ")
entered_password=input("Enter password: ")

print(validate_login(entered_username,entered_password))    