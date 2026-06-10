'''
Triangle star pattern
         *
        * *
       * * *
      * * * *
'''

def TriangleStarPattern(row):
    for i in range(1, row+1):
        print(" " * (row-i) + "* " *i)  # Keep a space after the * 


TriangleStarPattern(4)