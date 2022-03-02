with open("pqr.txt","r+") as f:
    data=f.read()
    f.seek(0)
    f.write("Start\n")
    f.write(data)
    
    