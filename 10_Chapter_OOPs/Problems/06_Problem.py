'''
 Create a class (2-D vector) and use it to create another class representing a 3-D
vector.

'''

class twoDVector:

    @staticmethod
    def show(i,j):
        print(f"2D vector: {i}i + {j}j")

class threeDVector(twoDVector):

    @staticmethod
    def show(i, j, k):
        twoDVector.show(i, j)
        print(f"3D vector: {i}i + {j}j + {k}k")

v1 = twoDVector()
v1.show(2,3)

v2 = threeDVector()
v2.show(5,6,7)