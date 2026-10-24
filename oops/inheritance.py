# Inheritance lets one class (the child) reuse the attributes and methods
# of another class (the parent) instead of rewriting them from scratch.
# This file shows a Manager class that inherits from an Employee class.

class Employee:
    # The parent class. Any class that inherits from Employee automatically
    # gets its __init__ and display_details, and can reuse or override them.
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary} - Parent Class - Employee")


# Writing "(Employee)" after the class name makes Manager a child class
# that inherits from the Employee parent class.
class Manager(Employee):

    # Manager needs more information than Employee (department, location,
    # teamsize), so it defines its own __init__ instead of reusing Employee's.
    # super().__init__(...) calls the parent class's __init__ to set up
    # name, age, and salary, so that logic does not need to be repeated here.
    def __init__(self, name, age, salary,department,location,teamsize):
        super().__init__(name, age, salary)
        self.department=department
        self.location=location
        self.teamsize=teamsize

    # A method that only exists on Manager, not on Employee.
    def assign_task(self):
        print(f"{self.name} is assigning a task. - Child Class - Manager")

    # This is called "method overriding": Manager defines its own
    # display_details, replacing the version it would have inherited as-is
    # from Employee. super().display_details() still calls the parent
    # version first, so the parent's print statement runs too.
    def display_details(self):
        super().display_details()
        # This line is commented out, so it does not run. If uncommented,
        # it would print the Manager-specific details (department,
        # location, teamsize) right after the parent's details are printed.
        #print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department}, Location: {self.location}, Team Size: {self.teamsize} - Child Class - Manager")


# Step 1: Creates a Manager object. This runs Manager's own __init__, which
# in turn calls Employee's __init__ through super() to set name, age, salary.
kunal = Manager("Kunal", 35, 90000,"QA","New Delhi",10)



# Step 2: Calls Manager's display_details (not Employee's directly), which
# itself calls the parent's display_details first, printing the Employee line.
kunal.display_details()

# Step 3: Calls assign_task, a method that only Manager has, since it was
# never defined on the parent Employee class.
kunal.assign_task()
