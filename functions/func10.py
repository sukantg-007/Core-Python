#after default arg we should not take non-default arg

def add(x,y=0):
    return x+y

#print(add())TypeError: add() missing 1 required positional argument: 'x' 
print(add(10))
#print(add(y=10))TypeError: add() missing 1 required positional argument: 'x'  