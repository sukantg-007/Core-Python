f=open("abc.txt","w")
print(f.name)
print(f.mode)
print(f.closed)
print(f.readable())
print(f.writable())
f.close()
print(f.closed)