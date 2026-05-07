"""
A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. 

"""

with open("Chapter9_File_input_output/problems/donkey.txt", "r") as file:
    content = file.read()
    print(content)

    if "Donkey" in content:
        newContent = content.replace("Donkey","55555")
        with open("Chapter9_File_input_output/problems/donkey.txt", "w") as file:
            file.write(newContent)


