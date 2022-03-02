#positional arguments
def sub(x,y):
    return x-y
print(sub(100,200))
print(sub(200,100))

#keyword arguments
def sub(x,y):
    return x-y
print(sub(x=100,y=200))
print(sub(y=200,x=100))

#Positional argument cannot appear after keyword arguments
#print(sub(x=100,200))

#print(sub(200,x=100))
#TypeError: sub() got multiple values for argument 'x'
print(sub(200,y=100))