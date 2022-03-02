import functools as ft
pi=3.14
def add(*val):
    return sum(val)

def mult(*val):
    if len(val)==0:
        return 0
    else:
        return ft.reduce(lambda x,y:x*y,val)


