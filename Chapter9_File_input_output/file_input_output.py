"""
File i/o (input and output) is the process of reading data from a file and writing data to a file using python, allowing programs to store, retrieve, and persist data permanently instead of loosing it after execution.


TYPE OF FILES.
There are 2 types of files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)


Python has a lot of functions for reading, updating, and deleting files

"""
'''
OPENING A FILE
Python has an open() function for opening files. It takes 2 parameters: filename and
mode.
# open("filename", "mode of opening(read mode by default)")
open("this.txt", "r")
'''
file = open("Chapter9_File_input_output/file.txt", "r")
print(file.read())
file.close


'''
MODES OF OPENING A FILE
r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode.
'''