class Bike:
    name = "Duke"
    color = "yellow"
    cc = 250

    def getInfo(self): # we always need to give the self as when we call it will have default one parameter
        print(f"The bike is {self.name} and the engine is {self.cc}cc.")

    def greet(rr):
        print("Assalamualikum")

    @staticmethod  # f we don't need argument in function
    def ask():
        print("How are you")

Bike1 = Bike()

Bike1.getInfo()
# Same call can be given as 
print("Second call")
Bike.getInfo(Bike1)

Bike1.greet()
Bike1.ask()