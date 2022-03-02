dict={}
while True:
    name=input("Enter std name : ")
    per=input("Enter std perc : ")    
    dict[name]=per
    x=input("Enter 1:[continue]|0:[exit] : ")
    if x=='0':
        break

print("NAME\tPERCENTAGE")
for d in dict:
    print(d,"\t",dict[d])    