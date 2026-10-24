bugIDs = ["BUG101", "BUG102", "BUG103", "BUG104", "BUG105"]
userChoice=input("Enter bug ID to search : ")
bugFoundFlag=False
for bugID in bugIDs:
    if bugID==userChoice.upper():
        print("Bug Found")
        bugFoundFlag=True
        break
if not bugFoundFlag:
        print("Bug Not Found")