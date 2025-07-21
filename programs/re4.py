


import re
fobj = open("data.txt")

for line in fobj:
    line = line.strip()  # removing whitespaces at the end
    if re.search(".ython",line):
        print(line)
fobj.close()

#re.search("^python",line):     at the beginning of the string
#re.search("python$",line):     at the end of the string
#re.search("pyt*hon",line):     zero or more occurences of preceding character
#re.search("pyt+hon",line):     one or more occurences of preceding character
#re.search("pyt?hon",line):     either zero or one occurence of preceding
#re.search(".ython",line):      any single character or digit or number
