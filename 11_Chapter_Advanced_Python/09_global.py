a = 89
def fun():
    global a # this will change the value of global a
    a = 3
    print(a)

fun()

print(a)


x = 10

def show():
    x = 20
    print(x)

show()