bug = { 
    "id": "BUG-101", 
    "title": "Login button not working", 
    "priority": "High", 
    "status": "Open" 
}

# Print the current bug details 
for key, value in bug.items(): 
    print(f"{key}: {value}")
# Change the status from Open to Closed and entering assigned person name
bug["status"]="Closed"
personName=input("Enter assigned person name: ")
bug["assignedTo"]=personName

#Print the updated bug details
for key,value in bug.items():
    print(f"{key} : {value}")

#Bonus  
updatedPriority=input("Enter new priority: ")
bug["priority"]=updatedPriority

for key,value in bug.items():
    print(f"{key} : {value}")