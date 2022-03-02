def f1(arg1, arg2, arg3=10, arg4=20):
    print(arg1,arg2,arg3,arg4)

f1(3,2)
f1(10,20,30,40)
f1(10,20,arg4=30)
f1(arg4=30, arg1=20, arg2=50)
#f1()#TypeError: f1() missing 2 required positional arguments: 'arg1' and 'arg2'
#f1(arg3=10,arg4=20,30,40)#SyntaxError: positional argument follows keyword argument
f1(1,2,arg5=30)