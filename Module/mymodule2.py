import functools as ft

def digitadd(n):
    return ft.reduce(lambda x,y:x+y,[int(x) for x in str(n)])