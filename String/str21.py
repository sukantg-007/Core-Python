file=input("Enter file name [file.ext] : ")
if file.endswith("txt"):
    print("File type : Notepad")
elif file.endswith("doc") or file.endswith("docx"):
    print("File type : Word")
elif file.endswith("py"):
    print("File type : Python")
elif file.endswith("xls"):
    print("File type : Excel")
else:
    print("File type : Excel")



