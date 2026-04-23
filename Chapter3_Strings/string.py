"""
A string is a sequence of characters enclosed in quotes used to store text data
"""

a = 'aacif'                                 #Single quote string
b = "bashir"                                #Double quote string
c = """Dar"""                               #Triple quotes string

print(a,b,c)

#____________________________________________________________________________________

#⚽️ 1
# String indexing 
# String indexing is the process of accessing individual characters of string using position numbering(Index)

name = "Aacif"
print(name[0])                              #A


# ⚽️ 2
# String slicing
# String slicing is the process of accessing a range of characters in a string
print(name[1:4])                            #aci

# ⚽️ 3
# String slicing with step/ skip values
print(name[::2])                            #Aci
print(name[0:4:2])                          #Ac

# ⚽️ 4
# Negative indexing
# it is used to access the elements from the end of the string
print(name[-1])                             #f
print(name[-4:-1])                          #aci

# ⚽️ 5
# String concatenation
# it is used to join two or more strings together
a = "Aasif"
b = "Bashir"                                #AasifBashir
print(a+b)


# ⚽️ 6
# String repetition
# it is used to repeat the string multiple times
print(name * 2)                             #AacifAacif


# ⚽️ 7
# String formatting
# it is used to format the string by inserting values into placeholders
name = "Aasif"
age = 25
print(f"My name is {name} and I am {age} years old.")

# ⚽️ 8
# String membership
# it is used to check if a substring exists within a string
print("A" in name)                            #True
print("a" not in name)                        #False