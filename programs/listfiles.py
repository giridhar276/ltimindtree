#write a program to display list of files line by line
import os
try:
    files=os.listdir()
    for item in files:
        #method1
        #print(item.ljust(30) , os.stat(item).st_size,"bytes")
        #method2
        print(item.ljust(30) , os.path.getsize(item), "bytes")
    #print("File is found",files)

except Exception as err: 
    print(err)
    print("Files are not found")
