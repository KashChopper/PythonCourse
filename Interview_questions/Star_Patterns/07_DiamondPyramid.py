'''  

Diamond pyramid
   *
  ***
 *****
*******
 *****
  ***
   *
'''

def DiamondPyramid(n):
    for i in range(1, n+1):
        print(" "*( n-i )+ "* "* i)
    for i in range(n-1, 0, -1):
        print(" "* (n-i) + "* "* i)
    
DiamondPyramid(4)

'''
Half Diamond pyramid
* 
* *
* * *
* * * *
* * *
* *
*
'''

def HalfDiamondPyramid(n):
    # Upper half
    for i in range(1, n +1):
        print("*"* i)
    for i in range(n-1, 0, -1):
        print("*"* i)
    
HalfDiamondPyramid(4)