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