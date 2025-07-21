# re.search(pattern,string)
# check for patterns anywhere in the string

import re
fobj = open("data.txt")

for line in fobj:
    line = line.strip()  # removing whitespaces at the end
    if re.search("python",line):
        print(line)
fobj.close()
