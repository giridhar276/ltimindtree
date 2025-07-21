# re.sub(pattern,replacement,string)
# re.sub() ----> replacing

import re
fobj = open("data.txt")

for line in fobj:
    line = line.strip()  # removing whitespaces at the end
    line = re.sub("python","java",line)
    print(line)
fobj.close()

############# reading and writing the output to other file #########

import re
fobj = open("data.txt")     # read operation
fw = open("output.txt","w") # write operation
for line in fobj:
    line = line.strip()  # removing whitespaces at the end
    line = re.sub("python","java",line)
    fwæ.write(line + "\n")
fobj.close()
fw.close()
