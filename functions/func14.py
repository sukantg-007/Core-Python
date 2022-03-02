#global variable and local variable
a=10#global
def f1():
    b=20#local
    print(b)
    print(a)

def f2():
    print(a)
    print(b)#NameError: name 'b' is not defined 

f1()
f2()