"""
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score
"""

import random


def game():
    score = random.randint(1,100)

    with open("Chapter9_File_input_output/problems/hi_score.txt") as file:
        hiscore = file.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score is: {score}")
    if score > hiscore:
        hiscore = score
        print(f"New high score {score}")
    else:
        print("Try again!")
    with open("Chapter9_File_input_output/problems/hi_score.txt", "w") as file:
        file.write(str(hiscore))

game()
