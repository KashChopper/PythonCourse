"""
for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence.

"""
item = [2, 5, "aasif", 6.5]
for i in item:
    print(i)

print("________________________________________________________________________________")

#Range function
# The range() function is used to generate a sequence of numbers. It takes three parameters:
# start: The starting value of the sequence (inclusive). Default is 0.
# stop: The ending value of the sequence (exclusive). This parameter is required.
# step: The increment value between each number in the sequence. Default is 1.
for i in range(5):
    print(i)


print("________________________________________________________________________________")

#for else loop
# An optional else can be used with a for loop. if the code is to be executed when the loops exhausts 
l = [2, 5, "aasif", 6.5]
for i in l:
    print(i)
else:
    print("Loop ended")


print("________________________________________________________________________________")

#The break statement is used to exit the loop when a certain condition is met. When the break statement is executed, the loop terminates immediately, and the program continues with the next statement after the loop.
for i in range(10):
    if i == 5:
        break
    print(i)

print("_________________________________________________________________________________ ")

#pass statement is used when you want to write a loop but don't want to execute any code inside the loop. It is a placeholder that allows you to create an empty loop without causing a syntax error.
for i in range(5):
    pass
print("_________________________________________________________________________________ ")


#Nested for loop
# A nested for loop is a loop that is contained within another loop. The inner loop is
# executed for each iteration of the outer loop. This allows you to perform more complex iterations and work with multi-dimensional data structures.
for i in range(3):
    for j in range(2):
        print(f"Outer loop iteration: {i}, Inner loop iteration: {j}")

