list=eval(input("Enter list : "))
i=0
while i<len(list):
    print("Index {:02d}...Number : {:03d}".format(i,list[i]))
    i+=1