
file = open("Chapter9_File_input_output/readLines.txt")

firstLine = file.readline()
secondLine = file.readline()
print(firstLine, type(firstLine))
print(secondLine)

dataLines = file.readlines()
print(dataLines, type(dataLines))


print("________________________________")


file1 = open("Chapter9_File_input_output/readLines.txt")

line = file1.readline()

while line != "":
    print(line)
    line = file1.readline()
file.close()


file2 = open("Chapter9_File_input_output/apend.txt", "a")
txt = "i am append"
print(file2.write(txt))
