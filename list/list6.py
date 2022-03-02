#manipulation of list
list=[]
count=4
while True:
    val=eval(input("Enter val : "))    
    if val!=False:
        list.append(val)
    else:
        break
val=eval(input("enter val"))
list.insert(2,val)
print(list)
list1=[1,2,3,4]
list.extend(list1)
print(list)

    