list=[  ["A",20],
        ["B",40],
        ["C",60],
        ["D",40],
        ["E",60],
]

list2=set([b for [a,b] in list])
list3=sorted([x for x in list2])

# list2=[]
# for x in list:
#     if x[1] not in list2:
#         list2.append(x[1])    
print(list3)
for x in sorted(list):
    if x[1]==list3[1]:
        print(x[0])