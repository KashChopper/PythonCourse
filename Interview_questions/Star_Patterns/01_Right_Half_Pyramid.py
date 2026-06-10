'''
Right-Angled Triangle Pattern
*
* *
* * *
* * * *
'''

def rightHalfPyramid(n):
    for i in range(1, n+1):
        print("* " * i)

n = 4
rightHalfPyramid(n)

'''
Inverted right half pyramid
'''

def InvertedRightHalfPyramid(row):
    for i in range(row, 0, -1):
        print("* "* i)

InvertedRightHalfPyramid(4)