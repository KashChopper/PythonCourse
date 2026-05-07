"""
An operator is a symbol/keyword used to perform operations on the values or variables

TYPES OF OPERATORS 

CATEGORY                    PURPOSE                         EXAMPLE

Arithmetic                  Math operations                 +, -, *, /, %, //, **

Assignment                  Assign/Update values            =, +=, -=, *=

Comparison                  Compare values                  ==, !=, >, <, >=, <=

Logical                     Combine conditions              and or not

Identity                    Same object check               is, isnot

Membership                  check presence                  in, notin

Bitwise                     Binary operations               &

"""

a = 10
b = 3

print(a/b)          #3.3333333333333335.    it is a float division
print( a//b)        #3                      it is a floor division

b += 8

print(b)            #11

a = [1, 2, 3]
print(1 in a)      # True

print(4 not in a)  # True

n = [10,20,50,90]
print(100 in n)    # False