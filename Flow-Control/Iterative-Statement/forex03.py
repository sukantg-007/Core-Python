s=input("Enter a string : ")
count=0
list=[]
for x in range(len(s)):
    if s[x]=="a":
        #print(x,end="\t")
        list.append(x)
        count=count+1

print("Number of a's : ",count)
print("Number of pos : ",list)