# This file is similar to inheritance.py but shows what happens when the
# child class does NOT override a parent method. Manager only adds a new
# method (display_extra_details); it does not redefine display_details.

class Employee:
    # Every parameter here has a default value (""/0/0), so Employee() can
    # be created even without passing any arguments at all.
    def __init__(self, name="", age=0, salary=0):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary} - Parent Class - Employee")


class Manager(Employee):

    # Calls the parent's __init__ through super() to set up name, age, and
    # salary, then stores the extra Manager-only fields separately.
    def __init__(self, name, age, salary,department,location,teamsize):
        super().__init__(name, age, salary)
        self.department=department
        self.location=location
        self.teamsize=teamsize

    def assign_task(self):
        print(f"{self.name} is assigning a task. - Child Class - Manager")

    # Unlike inheritance.py, this method has a different name
    # (display_extra_details) instead of reusing display_details, so it does
    # not override the parent method, it simply adds a new one. It is
    # defined here but never called in this file.
    def display_extra_details(self):
        super().display_details()


# Step 1: Creates a Manager object, running Manager's __init__, which calls
# Employee's __init__ through super() for name, age, and salary.
kunal = Manager("Kunal", 35, 90000,"QA","New Delhi",10)

# Step 2: Since Manager never overrides display_details, this call runs the
# exact display_details method inherited from the parent Employee class.
kunal.display_details()

# Step 3: Calls assign_task, a method that only exists on Manager.
kunal.assign_task()
