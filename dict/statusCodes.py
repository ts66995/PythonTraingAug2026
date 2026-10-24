status_codes = { 
    200: "OK", 
    201: "Created", 
    400: "Bad Request", 
    401: "Unauthorized", 
    404: "Not Found", 
    500: "Internal Server Error" 
}
statusCodeEntered=int(input("Enter staus code: "))
if statusCodeEntered in status_codes: 
    print(f"{statusCodeEntered} : {status_codes[statusCodeEntered]}") 
else: 
    print("Status code not available")


if statusCodeEntered>=200 and statusCodeEntered<=299: # We can write as if 200 <= statusCodeEntered <= 299:
    print("Success Response")
elif statusCodeEntered>=400 and statusCodeEntered<=499:
    print("Client Error")
elif statusCodeEntered>=500 and statusCodeEntered<=599:
    print("Server Error")