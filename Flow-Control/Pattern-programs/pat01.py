# for i in range(4):
#     for j in range(4):
#         if j<=i:
#             print("* ",end=" ")
#     print()

for i in range(4):
    for j in range(i+1):        
            print("*",end=" ")
    print()

#-----python method
for i in range(1,5):
    print("* "*i)