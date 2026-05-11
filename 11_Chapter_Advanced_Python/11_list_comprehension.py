myList = [1, 3,5,7]

sqList = []
for item in myList:
    sqList.append(item*item)

print(sqList)

# this can be simplified byy enumerate

squareList = [item * item for item in myList]
print(squareList)