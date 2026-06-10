'''
Reverse triangle pattern

    * * * * 
     * * *
      * *
       *
'''

def ReverseTrianglePattern(n):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "* "*i)

ReverseTrianglePattern(4)