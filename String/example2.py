#merge two string alternatively
a = input('Enter first string : ')
b = input('Enter second string : ')
alen = len(a)
blen = len(b)
acount,bcount,i=0,0,0
s=""
'''
g = min(m,n)
print(g)
k = ''
for i in range(g):
    k =k + a[i] + b[i]
print(k)
if len(a)<len(b):
    k = k + b[(g):]
if len(a)>len(b):
    k = k + a[(g):]
print(k)
'''
while True:
    if acount<alen:
        s=s+a[acount]
        acount+=1
        i=i+1
    if bcount<blen:
        s=s+b[bcount]
        bcount+=1
        i=i+1
    if i==(alen+blen):
        break
print(s)

#---alternate----