def myFun():
    print("hello world")

myFun()

print(__name__)  # this will print from which file you are printing it

if __name__ == "__main__":
    print("We are directly running this code ")