


## file write operation
# if the file is not existing.. file gets created first
# if the file is already existing ... it overwrites the existing content

# opening file
fobj = open("clients.txt","w")

fobj.write("tcs\n")
fobj.write("cts\n")
fobj.write("microsoft\n")

fobj.writelines(["wipro\n","infosys\n","ibm\n"])

for val in range(1,10):
    fobj.write(str(val) + "\n")

# close file
fobj.close()
