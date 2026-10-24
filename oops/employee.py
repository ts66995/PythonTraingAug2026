# This file shows how to create a class in Python and use it as a blueprint
# to build multiple objects (instances) that each hold their own data.
# A class groups related data together, here every Employee object stores
# a name, salary, department, joining date, and bonus.

class Employee:

    # __init__ is a special method that Python calls automatically every
    # time a new Employee object is created. It is commonly called the
    # constructor because its job is to set up (construct) the object.
    # "self" refers to the specific object being created, so self.name
    # stores the value in that particular object, not in every Employee.
    # "bonus=0" is a default value, used only when the caller does not
    # pass a bonus while creating the object.
    def __init__(self,name,salary,department,joiningdate,bonus=0):
        self.name=name
        self.salary=salary
        self.department=department
        self.joiningdate=joiningdate
        self.bonus=bonus




# Step 1: Creates three separate Employee objects. Each call to Employee(...)
# runs __init__ again, so emp1, emp2, and emp3 each get their own independent
# copy of name, salary, department, joiningdate, and bonus.
# None of them pass a bonus value, so all three keep the default bonus of 0.
emp1=Employee("Mukesh",50000,"IT","2026-01-01")
emp2=Employee("Mahesh",60000,"HR","2025-05-15")
emp3=Employee("Suresh",70000,"Finance","2024-09-10")

# Step 2: Dot notation (object.attribute) is used to read a value stored
# inside a specific object. emp1.salary reads the salary stored only in emp1.
print(emp1.salary)
# Step 3: Reads the joiningdate stored only in emp2, not the other objects.
print(emp2.joiningdate)
# Step 4: Reads the department stored only in emp3, not the other objects.
print(emp3.department)

