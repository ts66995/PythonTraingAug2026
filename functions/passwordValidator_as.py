def validate_password(password: str) -> str:
    has_uppercase=False
    has_lowercase = False 
    has_number = False 
    has_special = False
    for char in password:
        if char.isupper():
            has_uppercase=True
        elif char.islower():
            has_lowercase=True
        elif char.isdigit():
            has_number=True
        elif char in "@#$%":
            has_special=True
    if (len(password)>=8 and has_uppercase and has_lowercase and has_number and has_special):
        return "Valid Password"
    else:
        return "Invalid Password"

entered_password = input("Enter password: ")
result = validate_password(entered_password)
print(result)
