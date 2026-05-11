try:
    num = int(input("Enter second number: "))
    print(num)

except Exception as e:
    print("Enter int value. ", e)

else:
    print("I am in else")