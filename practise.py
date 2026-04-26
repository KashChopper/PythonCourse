"""
Create a list of 5 fruits.
Print first and last item.
Add one new fruit.
Remove second fruit.
Reverse the list.
Check if "apple" exists.

"""
fruits = ["Apple", "Banana", "orange", "Mango", "Peach", "Plum"]

print(fruits[0], fruits[-1])

fruits.append("Grapes")

print(fruits)

print(fruits.remove("Banana"))

print(fruits)

fruits.reverse()
print(fruits)


print()
