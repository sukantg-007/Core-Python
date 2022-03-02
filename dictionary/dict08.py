word=input("Enter word : ")
dict={}
for w in word:
    dict[w]=dict.get(w,0)+1

for k,v in dict.items():
    print("Key : ",k," Occurence : ",v)
word=input("Enter sentence : ")
dict2={}
for w in word.split():
    dict2[w]=dict2.get(w,0)+1

for k,v in dict2.items():
    print("Key : ",k," Occurence : ",v)
