s="python is esay. python is simple. python is oopl"
n=len(s)
begin=-1
while True:
    pos=s.find("python",begin+1,n)    
    if pos != -1:
        print("Index :",pos)
        begin=pos
    else:
        break
   
