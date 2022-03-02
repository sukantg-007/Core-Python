def mathop(x,y):
    return x+y,x*y,x/y,x%y,x-y, x//y, x**y

t=mathop(10,20)
print(t)
add,mult,div,mod,sub,flr,exp=t
print(add,mult,div,mod,sub,flr,exp)