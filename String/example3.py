a = input('Enter a string')
k = ''
m = ''
for i in range(0,len(a),2):
    m = a[i]*int(a[i+1])
    k = k+m
print(k)