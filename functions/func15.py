# def f1():
#     global a
#     a=10
#     print(a)

# def f2():
#     print(a)

# f1()
# f2()

a=10
def f1():
    a=20
    print(a)
    print(globals()['a'])

f1()