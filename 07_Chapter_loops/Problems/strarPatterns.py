"""
    HALF PYRAMID PATTERN
    *
    * *
    * * *
    * * * *
"""
print("___________________ HALF PYRAMID________________________")
for i in range(1,5):
    print("* " * i)


"""
   INVERTED HALF PYRAMID

   * * * *
   * * * 
   * * 
   *

"""

print("__________________INVERTED HALF PYRAMID___________________")

for i in range(4,0,-1):
    print("* " * i)



"""   FULL PYRAMID
         *
        * *
       * * *
      * * * *    
"""
print("___________________ FULL PYRAMID________________________")
n = 4
for i in range(1, n+1):
    print(" " * (n-i), "* " * i)        


'''

   INVERTED FULL PYRAMID
   
      * * * *
       * * *
        * *
         *
'''

print("___________________ INVERTED FULL PYRAMID________________________")

num = 4

for i in range(num, 0, -1):
    print(" " * (n-i), "* " * i)   # keep space after printing the start or use end="" in print statement to avoid new line after printing the start
#OR
for i in range(num, 0, -1):
    print(" "* (n-i), "* "* i, end="")
    print("\n")

    #OR
for i in range(0, num+1):
    print(" "* i,"* " * (n-i))

#OR

for i in range(0, num+1):
    print(" "* i, end="")
    print("* " * (n-i))

#OR

for i in range(1, num+1):
    print(" " * (i-1), end="")
    print("* " * (num-i+1))
