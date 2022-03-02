#list=[x*x for x in range(1,11)]
# list=[x for x in range(1,11)if x%2==0]
#list=["python", "is","easy"]
#list2=[w[0] for w in list]
#list1=[10,20,30,40]
#list2=[20,40,60,80]
#list3=[x for x in list1 if x not in list2]
s=input("Enter a string : ").split()
list=[[w.upper(),len(w)] for w in s]
print(list)
list2=[[a,b] for [b,a] in sorted([[b,a] for [a,b] in list])]
print(list2)
s=" ".join([w[0] for w in list2])
print(s)