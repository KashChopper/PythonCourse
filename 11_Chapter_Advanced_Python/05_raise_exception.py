num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))

if num2 == 0:
    raise ZeroDivisionError("You can't divide by zero. ")
else:
    print(num1/num2)