"""
A constructor is a special method that is automatically called when an object is created
in python, the constructor method is
 
_int_()


"""

class student:
    def __init__(self):
        print("Constructor is executed")



#______________________________________

# constructor with parameters 
class student:
    def __init__(self, name , age):
        self.name = name
        self.age = age


s1 = student("Aasif", 24)
print(s1.name, s1.age)

s2 = student("Ayan", 22)

print(s2.name, s2.age)


#Static Method
# when we don't  wont to use self parameter and we need to call method without creating object

class greet:
    @staticmethod
    def ask():
        print("How are you")


greet.ask()



class Bike:
    name = "Duke"
    color = "yellow"
    cc = 250

    def __init__(self, name, price):   # dunder method which is automatically called
        self.name = name
        self.price = price
        print("I am creating an object")

    def getInfo(self): # we always need to give the self as when we call it will have default one parameter
        print(f"The bike is {self.name} and the engine is {self.cc}cc.")


    @staticmethod  # f we don't need argument in function
    def ask():
        print("How are you")

Bike1 = Bike("Pulsar", 150000)

print(Bike1.name, Bike1.color, Bike1.price)  # dunder method will get automatically printed on ever call