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