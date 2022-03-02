#index position

s='This is python'.split()
count=0
for i in s:
    if i=='python':
        count=count+1
    print(i)
print("char 'python' occures : ",count)