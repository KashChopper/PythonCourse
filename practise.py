from random import randint
number = randint(1,100)

user = -1
guess = 0

while user != number:
    guess = guess + 1
    user = int(input("Guess number: "))


    if user < number:
        print("higher number")

    else:
         print("lower number")


print(f"You guessed in {guess} attempts")