class Employee:
    name = "Aasif"  # This is a class attribute
    age = 24        # This is a class attribute
    salary = 123333 # This is a class attribute

aasif = Employee()
print(aasif.name, aasif.salary)



ayan = Employee()
ayan.name = "Ayan"  # instance attributes takes preference so ayan will get printed 
# First check: is attribute present in the object
# Second check: is attribute present in the class
print(ayan.age, ayan.name, ayan.salary)