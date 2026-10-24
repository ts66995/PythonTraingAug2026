# This file shows a class with several small "display" methods, each
# responsible for printing just one piece of information about a Student,
# plus one display_all method that prints everything together. It also
# shows default parameter values for every constructor argument.

class Student:

    # Every parameter has a default value, so a Student can be created
    # even when some (or all) arguments are left out, in which case that
    # field falls back to its default (for example age defaults to 18).
    # "self" always refers to the specific Student object being worked on,
    # so self.name only affects that one object, not every Student.
    def __init__(self,name="NA",age=18,email="sample@example.com",address="BLR",phone=0):
        self.name=name
        self.age=age
        self.email=email
        self.address=address
        self.phone=phone

    def display_name(self):
        print("Student Name is ", self.name)

    def display_email(self):
        print(f"Student Email is {self.email}")

    def display_address(self):
        print(f"Student Address is {self.address}")

    def display_phone(self):
        print(f"Student Phone is {self.phone}")

    def display_age(self):
        print(f"Student Age is {self.age}")

    # Combines every piece of information into a single print statement,
    # instead of calling each of the display_* methods above separately.
    def display_all(self):
        print(f"Student Name is {self.name} Age is {self.age} Email is {self.email} Address is {self.address} Phone is {self.phone}")


# Step 1: Creates three separate Student objects. Each one supplies all
# five arguments by position (name, age, email, address, phone), so none
# of the default values defined in __init__ are actually used here.
student1=Student("Akshay",30,"selenium@gmail.com","Pune",78784)
student2=Student("Rohit",25,"playwright@gmail.com","BLR",1412541)
student3=Student("Balaji",35,"python@gmail.com","HYD",989561)

# Step 2: Calls display_all only on student3, so only Balaji's details are
# printed; student1 and student2 are created but never displayed here.
# The trailing comment shows that student3.display_all() is really just a
# shortcut for Student.display_all(student3): calling a method on an
# object automatically passes that object in as the "self" argument.
student3.display_all() #Student.display_all(student3)
