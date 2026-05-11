# try:
#     num = int(input("Enter second number: "))
#     print(num)

# except Exception as e:
#     print("Enter int value. ", e)

# finally:
#     print("I am in finally")
# # we can also use the print statement instead of finally statement, 

# print("I am finally ")

# # then why use the finally, we use finally especially in the function it will always get printed while print will not get always printed

# print("Finally used in function ")

def main():
    try:
        num = int(input("Enter number for function: "))
        print(num)
        return

    except Exception as e:
        print("Enter int value. ", e)
        return

    finally:
        print("I am in finally")

    print("I am print ")  # This will not get print

main()

