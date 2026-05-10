"""
The property decorator in Python is a built-in function that allows you to define methods in a class that can be accessed like attributes. It provides a way to customize the behavior of attribute access, allowing you to define getter, setter, and deleter methods for an attribute. The property decorator is used to create managed attributes in a class, enabling you to control how attributes are accessed and modified.

"""

class Employee:
    def __init__(self, salary, bonus):
        self._salary = salary  # Using a protected attribute to store the salary
        self._bonus = bonus    # Using a protected attribute to store the bonus
    

    @property
    def total_salary(self):
        return self._salary + self._bonus  # Calculating total salary by adding salary and bonus
    
e = Employee(50000, 10000)
print(f"Total Salary: {e.total_salary}")  # Accessing total_salary as an attribute, but it will call the total_salary method to calculate the value 