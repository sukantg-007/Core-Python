dict={x:x**2 for x in range(1,11)}
dict1={}
for i in range(1,11):
    dict1[i]='even' if i%2==0 else 'odd'
counte=0
counto=0
for k in dict1:
    if dict1.get(k) == 'odd':
        counto+=1
    else:
        counte+=1 
print(dict)
print(dict1)
print("count of even numbers ",counte)
print("count of odd numbers ",counto)
print(dict1)
