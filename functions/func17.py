def clen(n):
    return len(str(n))

clen=lambda x: len(str(x))
def reverse(n):
    digit=clen(n)-1
    if n==0:
        return 0
    else:
        return n%10*pow(10,digit)+reverse(n//10)

reverse= lambda x: 0 if x==0 else x%10*pow(10,clen(x))+reverse(x//10)    
print(reverse(557))

