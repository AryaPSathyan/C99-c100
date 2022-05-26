import os
import shutil

path = input("enter the name of the directery to be organised:")

# listing all the files and folders on the path
list_of_files = os.listdir(path)

# splitting the ext for all the files
for file in list_of_files:
    name,ext = os.path.splitext(file)

    # this is going to store the extention type
    ext = ext[1:]

    # this forces the next iteration if it is a folder
    if ext =='':
        continue

    # this will move the file to the directery where the ext already exist 
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

        # this will create the file 
    else :
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)