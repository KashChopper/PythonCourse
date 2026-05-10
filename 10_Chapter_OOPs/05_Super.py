"""
Super() keyword is used to access methods and constructors of the parent class from the child class.
it helps in achieving inheritance properly without directly referring to the parent class name.

"""

class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling the parent class constructor
        self.age = age
    def display(self):
        super().display()  # Calling the parent class method
        print(f"Child Age: {self.age}")
# Creating an instance of the Child class
child = Child("Alice", 10)
child.display()