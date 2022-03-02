#odd even 
a = input('Enter a string')
for i in range(0,len(a),2):
    print(a[i],end='')
print()
for i in range(1,len(a),2):
    print(a[i],end='')