#variable length args
# sytax:
# def function(*arg):
#     for i in arg:
#         #implementation


def addn(*arg):
    sum=0
    for i in arg:
        sum=sum+i
    return sum
    
print(addn())
print(addn(10))
print(addn(10,20))
print(addn(10,20,30))
print(addn(10,20,30,40))

def addl(l):
    return sum(l) if type(l) is list or type(l) is tuple or type(l) is set else l

print(addl(10))
print(addl((10,20,30)))