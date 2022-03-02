# 4 3 1
#  B1 n =no of choacletes
# m = total
#      L1     L2      L3            L4        L5
#      B1    B1-1    B2+B1-1    B3 + B2+B1 -1   B4 + B3 + B2+B1 -1
#       4     3        6          12                24
#FIND L4 
a = int(input('Enter the no of choclates of first kid '))
b = int(input('Enter the no kids line'))
if b == 2:
    print(a-1)
else : 
    print((a-1)*(2**(b-2)))
#print(3* 2**3)

