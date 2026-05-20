"""
A decorator is a function that takes another function as an argument and return a new function that modifies the behavior of the original function. The new function is often referred to as "decorated" function

"""

def greet(fn):
    def modifiedFn():
        print("Good morning")
        fn()
        print("Thanks for using this function")
    return modifiedFn
 
# def hello():
#     print("hello world")

# greet(hello)()  #This works as decorator 

# Perfect way to use decorator

@greet
def hello():
    print("Hello world")
    
# Now we need to call only hello function and it will automatically call the greet function as well

hello()
