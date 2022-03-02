import os.path as p
from sys import exit

name=input("Enter file name : ")
if p.isfile(name):
    print("File exist : ",name)
    with open(name) as f:
        data=f.read()
        print(data)
else:
    print("File does not exists: ",name)
    exit(0)

