# This file shows multi-level inheritance: C inherits from B, and B
# inherits from A, forming a chain (A -> B -> C). It also demonstrates a
# very common misunderstanding beginners have about how inheritance works.

class A:

    def demo1(self):
        print("Class A demo1 method called")


# B inherits from A, so every B object automatically has demo1() as well
# as its own demo2().
class B(A):
    def demo2(self):
        print("Class B demo2 method called")


# C inherits from B, and B already inherits from A, so C objects get
# demo1() (from A), demo2() (from B), and demo3() (its own).
class C(B):
    def demo3(self):
        print("Class C demo3 method called")

# Step 1: Creates an object of class A specifically, not class B or C.
obj = A()
# Step 2: This line will raise an AttributeError: 'A' object has no
# attribute 'demo3'. Inheritance only flows downward, from parent to
# child, never upward. A child class (like C) gains everything its
# parent has, but a parent class (like A) never gains anything defined
# only in its children. To call demo3() successfully, obj would need to
# be created from C instead, for example obj = C().
obj.demo3()
