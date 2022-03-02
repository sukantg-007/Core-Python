import os
#os.rmdir("new_new_dir")
print(os.listdir("."))
print("-------------------------------")
#os.walk(path,topdown=true,onerror=None,followlinks=False)
for dirpath,dirname,filename in os.walk("."):
    print("Current dir path : ",dirpath)
    print("Directries : ",dirname)
    print("File names : ",filename)
    print()
    print("--------------------------")
    print()
