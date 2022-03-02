s=input("Entera str : ")
for i in s:
    print(i,end='\t')
print()
for i in s[::]:
    print(i,end='\t')
print()

for i in s[::-1]:
    print(i,end='\t')
print()