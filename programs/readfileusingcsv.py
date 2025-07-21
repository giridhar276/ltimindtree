## using fobj.readlines()
fobj= open("products.csv")
for line in fobj.readlines():
    print(line)
fobj.close()

############################## using csv library ###############
#Advantage : Each line is converted to list automatically, not required to split
import csv
fobj= open("products.csv")
# converting file object to csv object
# reading line by line
reader = csv.reader(fobj)  
for line in reader:
    print(line) # each line is the list
########################## using csv library and DictReader() method ####
import csv
fobj= open("products.csv")
# converting file object to csv object
# reading line by line
reader = csv.DictReader(fobj) 
for line in reader:
    print(line)   # each dict is dictionary 
