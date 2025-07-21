firstname = input("Enter first name :")
lastname = input("Enter last name :")
university= input("Enter university :")
city = input("Enter city :")

fobj = open("details.txt","w")
fobj.write("Firstname :" + firstname)
fobj.write("\n")
fobj.write("last name:" + lastname )
fobj.write("\n")
fobj.write("University :" + university)
fobj.write("\n")
fobj.close()
##########################################################



