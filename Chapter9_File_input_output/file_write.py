message = "this string will get added to the file"

file = open("Chapter9_File_input_output/writeFile.txt", "w")

file.write(message)

file.close()