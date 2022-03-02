#upzip of the zip file
from zipfile import *
#create zipfile object with constant ZIP_STORED
f=ZipFile("File.zip","r",ZIP_STORED)
names=f.namelist()
for name in names:
    print("File Name : ",name)
    file=open(name)
    data=file.read()
    print("Data :\n",data)
    print("---------------------------")