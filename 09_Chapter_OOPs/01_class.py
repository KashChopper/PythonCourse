class Employee:
    name = "Aasif"  # This is a class attribute
    age = 24        # This is a class attribute
    salary = 123333 # This is a class attribute

aasif = Employee()
print(aasif.name, aasif.salary)



ayan = Employee()
ayan.name = "Ayan"  # This is a instance/object attribute
print(ayan.age, ayan.name, ayan.salary)

# here name is instance/object attribute and  salary and age is class attribute