"""
The best way to open a file and close the file automatically is the with statement
"""

with open("Chapter9_File_input_output/apend.txt", "r") as file:
    text = file.read()

print(text)