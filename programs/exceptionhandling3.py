


try:
    fobj = None
    fobj = open("languages11.txt","r")

except Exception as err:
    print(err)

else:
    for line in fobj.readlines():
        print(line)

finally:
    if fobj:
        fobj.close()


