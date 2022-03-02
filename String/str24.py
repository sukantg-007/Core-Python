s=input("Enter a str : ")
list=s.split()
print(list)
newList=[]
for word in list:
    newList.append(word[::-1])
print(newList)
newstr=" ".join(newList)
print(newstr)