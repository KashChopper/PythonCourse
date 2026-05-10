class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute 

    # Getter method for name
    def get_name(self):
        return self.__name
    
    # Setter method for name
    def set_name(self, name):
        self.__name = name.strip()  # Removing any leading or trailing whitespace from the name

e = Employee("Aasif", 120000)

print(e.get_name())  # Accessing name using getter
e.set_name("Aasif Khan")  # Modifying name using setter
print(e.get_name())  # Accessing updated name using getter