testCases = ["Login Test", "Logout Test", "Search test", "Payment test"]
userChoice=input("Do you want to remove the last test case? (yes/no): ")
if userChoice.lower()=='yes':
    testCases.pop()
    print(f"Updated Test Cases: ",testCases)
else:
    print(f"Updated Test Cases: ",testCases)