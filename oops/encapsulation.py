# Encapsulation means hiding the internal data of an object and only
# allowing it to be read or changed through specific methods, instead of
# letting outside code touch that data directly. This file shows a simple
# example using a "private" attribute and getter/setter methods.

class Student:

    def __init__(self, name,age,phone):
        self.name=name
        self.age=age
        # Starting an attribute name with two underscores (__phone) marks it
        # as private by convention. Python renames it internally so it
        # cannot be accessed directly from outside the class as
        # student1.__phone; it must be accessed through the methods below.
        self.__phone=phone

    # A "getter" method. Its only job is to return the private value stored
    # inside the object, giving controlled read access to __phone.
    def get_phone(self):
        return self.__phone

    # A "setter" method. Its only job is to update the private value stored
    # inside the object, giving controlled write access to __phone.
    def set_phone(self, phone):
        self.__phone = phone



# Step 1: Creates a Student object. "7896451478" is stored inside the
# private __phone attribute through the constructor.
student1=Student("Mukesh", 25, "7896451478")

# Step 2: Reads the phone number using the getter method rather than
# accessing __phone directly, printing "7896451478".
print(student1.get_phone())

# Step 3: Updates the phone number using the setter method. This replaces
# the private __phone value with the new number "9876543210".
student1.set_phone("9876543210")

# Step 4: Calls the getter again to confirm the phone number was updated,
# printing "9876543210" this time.
print(student1.get_phone())
