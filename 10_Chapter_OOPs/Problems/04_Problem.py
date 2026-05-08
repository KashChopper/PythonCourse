"""
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.

"""
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def bookTicket(self, fro, to):
        print(f"Ticket is booked for the train number {self.trainNo} form {fro} to {to}")
        print(f"Your ticket number is {randint(1, 300)}")

    def getStatus(self, trainNo):
        print(f"Train {trainNo} is running successfully on its time.")

    def getInfo(self, trainNo, fro, to):
        print(f"Train number {trainNo} is running from {fro} to {to}. The train will reach on the platform number {randint(1,5)}")
        
TrainNumber = int(input("Enter the train number you want to book: "))
fro = "Srinagar"
to = "Delhi"
ticket = Train(TrainNumber)
ticket.bookTicket(fro, to)

ticket.getStatus(TrainNumber)

ticket.getInfo(TrainNumber,"Srinagar", "Delhi")
