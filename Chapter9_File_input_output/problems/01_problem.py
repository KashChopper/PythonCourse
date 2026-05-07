# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word "aasif".

with open("Chapter9_File_input_output/apend.txt") as file:
    data = file.read()

if "aasif" in data:
    print("yes")
else:
    print('NO')