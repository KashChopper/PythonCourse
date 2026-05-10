"""
A class method is a method that is bound to the class rather than its object. It can modify a class state that applies across all instances of the class, rather than instance-specific data. Class methods are defined using the @classmethod decorator and take cls as the first parameter, which refers to the class itself.
"""

class Employee:
    a = "Employee Class Variable"

    @classmethod
    def show(cls):
        print(f"Class Method: {cls.a}")


e = Employee()

e.a = "Modified Employee Class Variable" # Modifying the class variable through an instance
# e.a will not get modified as it is an instance variable now, it will create a new variable 'a' for the instance 'e' and will not affect the class variable 'a'
e.show()


print(" ________________________________________method______________________________")

# 1. GETTER METHOD 
# A getter method is a method that is used to access the value of a private attribute in a class. It allows you to retrieve the value of an attribute without directly accessing it, providing a level of encapsulation and control over how the attribute is accessed.

#2. SETTER METHOD
# A setter method is a method that is used to set the value of a private attribute in a class. It allows you to modify the value of an attribute while providing control over how the attribute is modified, ensuring that any necessary validation or processing can be performed before the attribute is updated.

# 3. DELETER METHOD
# A deleter method is a method that is used to delete a private attribute in a class. It allows you to remove an attribute from an instance of a class, providing control over how the attribute is deleted and ensuring that any necessary cleanup or processing can be performed before the attribute is removed.


# example 

class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for salary
    def get_salary(self):
        return self.__salary

    # Setter method for salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")

e = Employee("Alice", 50000)
print(f"Employee Name: {e.get_name()}")  # Accessing name using getter
print(f"Employee Salary: {e.get_salary()}")  # Accessing salary using getter
e.set_salary(60000)  # Modifying salary using setter
print(f"Updated Employee Salary: {e.get_salary()}")  # Accessing updated salary

