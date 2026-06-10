'''
Left Half Pyramid

        *
      * *
    * * *
  * * * *

'''

def leftHalfPyramid(n):
    for i in range(1, n+1):
        print(" "* (n-i), "*"* i)

leftHalfPyramid(4)


'''
Inverted left half pyramid
  * * * *
    * * *
      * *
        *
'''

def InvertedLeftHalfPyramid(n):
    for i in range(n, 0, -1):
        print(" "* (n-i) + "*"*i)
    
InvertedLeftHalfPyramid(4)