'''
Hollow Square

* * * * * *
*         *
*         *
*         *
* * * * * *
'''

def HollowSquare(n):
    print("*" *n)
    for _ in range(n - 2):
       print("*" + " " * (n-2) + "*")
    print("*" *n)
HollowSquare(5)
