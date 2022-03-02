#creat a zip file and add some file into it
from zipfile import *
#create object of zipfile
f=ZipFile("File.zip","w",ZIP_DEFLATED)
f.write("ex01.py")
f.write("ex02.py")
f.write("ex06.py")
f.write("ex04.py")
f.write("ex05.py")
f.close()
print("Zip file is created with name File.zip")
