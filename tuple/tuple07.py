l=[[1,"A"],[2,"B"],[3,"C"]]
t=((x,y) for [x,y] in l if x%2!=0)
for x in t:
    print(x)