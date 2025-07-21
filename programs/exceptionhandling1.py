

try:
    fobj = open("languages111111111.txt","r")

    for line in fobj.readlines():
        print(line)

    fobj.close()

except Exception as err:   # Exception is the base class exception
    print("system error :", err)
    print("user defined error:","file is not found")


print("this is regular code")
