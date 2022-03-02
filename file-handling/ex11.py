import os
cwd=os.getcwd()
print("Current Folder : ",cwd)
#create folder in cwd
#os.mkdir("new_dir")
print("New Folder created  new_Dir")
#create folder inside folder
#os.makedirs("dir1/dir2/dir3/dir4")
print("Folders created ...")
#delete a directory
#os.rmdir("new_dir")
print("new_dir deleted")
#delete more number of directories
#os.removedirs("dir1/dir2/dir3/dir4")
print("dirs deleted")
#rename dir
os.rename("new_dir","new_new_dir")
print("renamed dir")