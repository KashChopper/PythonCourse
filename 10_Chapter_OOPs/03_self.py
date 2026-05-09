class Bike:
    name = "Duke"           # class attribute
    color = "yellow"
    cc = 250

    def getInfo(self): # we always need to give the self as when we call it will have default one parameter
        print(f"The bike is {self.name} and the engine is {self.cc}cc.")

    def greet(rr):   # we can give any name to the parameter but by convention we use self
        print("Assalamualikum")

    @staticmethod  # we can use static method when we don't want to use self parameter and we want to call the method without creating an object
    def ask():
        print("How are you")

Bike1 = Bike()          # creating an object of the class Bike and storing it in the variable Bike1

Bike1.getInfo()         # calling the method getInfo using the object Bike1 and it will automatically pass the self parameter as Bike1 to the method getInfo
# Same call can be given as 
print("Second call")
Bike.getInfo(Bike1)     # we can also call the method getInfo using the class name and passing the object as an argument to the method getInfo and it will work fine as we are passing the object as an argument to the method getInfo and it will automatically pass the self parameter as Bike1 to the method getInfo

Bike1.greet()       # calling the method greet using the object Bike1 and it will automatically pass the self parameter as Bike1 to the method greet
Bike1.ask()

Bike.ask()         # calling the static method ask using the class name and it will work fine as we don't need to pass any argument to the static method ask as it doesn't have any parameter and it will automatically call the static method ask without any error