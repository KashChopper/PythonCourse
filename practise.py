try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    if b == 0:
        raise ZeroDivisionError("Division by zero")

    result = a / b

except ZeroDivisionError as e:
    print("Exception:", e)

except ValueError:
    print("Exception: Please enter valid integers")

else:
    print("Result =", result)

finally:
    print("Program execution completed")