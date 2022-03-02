def printf(x, *y):
    print(x)
    for i in y:
        print(i)
    
printf(10)
printf(1,1,2,3,4,5)


def printg(*x, y):
    printf(y,*x)

#printg(1,2,3,4,8)#TypeError: printg() missing 1 required keyword-only argument: 'y'
printg(1,2,3,4,5,y=10)