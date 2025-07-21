
import os
dirname = "examples2"
# check for existence of the file or directory
if os.path.exists(dirname):
    print("directory already exists")
else:
    os.mkdir(dirname)
    print(dirname,"created")


#######################################################

filename = "customers.txt"
# will check whether file is existing and whether it is file or not
if not os.path.isfile(filename):  
    fobj= open(filename,"w")
    fobj.write("ltimindtree")
    fobj.write("tcs")
    fobj.close()
else:
    print("file already exists")

           
