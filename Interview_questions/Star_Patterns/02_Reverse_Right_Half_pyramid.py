'''
Reverse Right Half Pyramid

          *
        * *
      * * *
    * * * *

'''

def reverseRightHalfPyramid(n):
    for i in range(1, n+1):
        print(" "*(n-i), "*"*i)

reverseRightHalfPyramid(4)
