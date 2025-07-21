

import re
#re.search() : used to search anything in the string
#re.match()  : used to check for pattern at the beginning of the string
#re.sub()    : substituting :  re.sub(source,destination,string)
#re.findall(): find all the patterns .. display output in list

fobj = open("data.txt")

for line in fobj:
    line = line.strip()  # removing whitespaces at the end
    if re.match("python",line):
        print(line)


fobj.close()
