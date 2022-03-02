list=['A','B','C','D','E','F','G','H','I','J']
k=0
for i in range(4):
    for j in range(i+1):
        print(list[k],end=' ')
        k=k+1
    print()