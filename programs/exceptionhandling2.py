
try:
    fobj = open("languages111.txt","r")
    for line in fobj.readlines():
        print(line)
    fobj.close()

except TypeError as e:   # Exception is the base class exception
    print("system error :", err )
    print("Invalid operation")
except ValueError as err:
    print("system error :", err)
    print("Invalid input")
except FileNotFoundError as err:
    print("system error :", err)
    print("file is not found")
except (IndexError,KeyError) as err:
    print("system error:", err)
    print("index or key is not found")
except Exception as err:
    print(err)

print("tthis is my regular code")
