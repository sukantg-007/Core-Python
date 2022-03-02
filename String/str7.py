#w ap to access char of str forward and backward dir
s=input("Enter a str : ")
i=0
while i<len(s):
    print(s[i],end='\t')
    i=i+1
i=i-1
print()
print('---------------------------')
while i>=0:
    print(s[i],end='\t')
    i=i-1