'''
Reverse left half pyramid

        * * * *
          * * *
            * *
              *

'''

def ReverseLeftHalfPyramid(row):
    for i in range(0, row):
        print(" " * i + "*"* (row-i))


ReverseLeftHalfPyramid(4)