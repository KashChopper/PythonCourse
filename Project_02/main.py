"""
We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.

"""
from random import randint

random_number = randint(1,100)
userInput = -1

guesses = 0

while userInput != random_number:
    guesses += 1
    userInput = int(input("Guess the number: "))

    if userInput < random_number:
        print("Higher number please: ")
    else:
        print("Lower number please")

print(f"You haves guessed the number correctly in {guesses} attempts")