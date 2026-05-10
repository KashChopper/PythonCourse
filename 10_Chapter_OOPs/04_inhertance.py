"""

* Inheritance is a process of one class acquiring the properties of another class
* A class which gives or share the properties is called  Base class or Parent class or Super class
* A class which acquires or accepts the property are called Sub class or Derives class or child class
* In python we achieve inheritance by passing the parent class name inside the parenthesis while creating the child class

"""

class Employee:
    company = "ITC"

    def show(self, name, salary):
        print(f"The name of the Employee is {name} and the salary is {salary}")
        


class Programer(Employee):
    company = "ITC info tech"
    def showLanguage(self):
        print(f"Programmer {self.name} is good with {self.language} language.") 

emp = Employee()
emp.show("Aasif", 120000)
print(emp.company)

pro = Programer()
print(pro.company)