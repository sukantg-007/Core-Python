def findeo(n):
    return 1 if n%2==0 else 0
def findFact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def fineReverse(n):
    s=str(n)
    return int(s[::-1])

print('even' if findeo(25)==1 else 'odd')
print(findFact(5))
print(type(fineReverse(123456)))