"""
 Write a program to create a dictionary of Urdu words with values as their English
translation. Provide user with an option to look it up!

"""

from webbrowser import get


urdu_dict = {
    "chai": "tea",
    "khana": "food",
    "shalwar": "pant",
    "dushman": "enemy",
    "dost": "friend",   
    "dus": "ten"
}

word = input("Enter the word: ")

trans = urdu_dict.get(word)

# or

print(urdu_dict[word])

# print(trans)


# if trans:
#     print(f"The meaning of the {word} is {trans}")
# else:
#     print(f"The letters {word} doesn't exist in the dictionary")


print("______________________________________________________________________________________")

#another method
if word in urdu_dict:
    print(f"The meaning of the {word} is {urdu_dict[word]}")
else:
    print(f"The letters {word} doesn't exist in the dictionary")
