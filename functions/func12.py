#variable length arg : *
#key variable length arg : **--it will be dictionay
#Parameter cannot follow "**" parameter
def add(x,**arg):
    sum=x
    for k,v in arg.items():
        print(k,"...",v)
        sum=sum+v
    return sum

#print(add(40,a=10,b=20,c=30))#TypeError: add() takes 0 positional arguments but 1 was given
print(add(40,a=10,b=20,c=30))