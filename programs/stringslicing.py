


name = "python programming"
print(name)
print("I love",name)

#string[start:stop:step]
print(name[0])  #p
print(name[1])  #y
print(name[0:8]) #python p
print(name[1:4])  #yth
print(name[8:])   #rogramming
print(name[:8])   #python p
print(name[0:18])  #python programming
print(name[0:18:1])#python programming
print(name[:])     #python programming
print(name[::])    #python programming
print(name[:18])   #python programming
print(name[0:18:2])#pto rga
print(name[0:18:3]) #ph
print(name[0:18:5])
print(name[-1])    #g
print(name[-5:-2])  #mmi
print(name[::-1])

#p   y    t    h    o   n      p   r   o   g    r   a   m   m   i   n   g
#                                              -7  -6   -5  -4  -3  -2  -1


name = "python programming"
print(name.count('python'))
print(name.capitalize())
print(name.title())
print(name.upper())
print(name.lower())
print(name.split(" ")) # output is the list
print(name.replace("python","java"))
print(name.center(30))
print(name.center(30,"*"))
print(name.islower())
print(name.isupper())
print(name.isalnum())
print(len(name))
aname = " python  "
print(len(aname))
print(len(aname.strip()))
print(len(aname.lstrip()))
print(len(aname.rstrip()))
bname = "I love {} and {}"
print(bname.format("python","C"))
print(bname.format("ooty","chennai"))


#simple if
if name.isupper():
        
    print("string is upper")
    print("inside if")
    print("still inside if")

# if-else
#simple if
if name.isupper():
    print("string is upper")
else:
    print("string is lower")


#if-elif-elif-elif-else
name = input("Enter any language:")
if name == "python":
    print("you are learning python")
elif name == "java":
    print("you are learning java")
elif name == "unix":
    print("you are learning unix")
else:
    print("you are learning someother language")




name = "python"
for char in name:
    print(char)


name = "python"
for char in name[::-1]:
    print(char)


alist = [10,20,30,40]
for val in alist:
    print(val)

    


    


















    









    











































