validUsename="admin"
validPassword="admin123"
attemps=0
maxAttempts=3
while attemps<maxAttempts:
    currentUsername = input("Enter username: ")
    currentPassword = input("Enter password: ")
    if validUsename==currentUsername and validPassword==currentPassword:
        print("Login successful")
        break
    else:
        attemps=attemps+1
        if attemps<=maxAttempts:
            # print("Invalid username or password")
            remainingAttemps=maxAttempts-attemps
            if remainingAttemps>0:
                print(f"Invalid username or password.{remainingAttemps} attemps remaining : ")
            else:
                print("Account Locked")