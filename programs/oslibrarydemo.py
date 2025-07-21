
# os library
import os
try:
    os.remove("abc.txt")
except Exception as err:
    print("system error",err)
    print("removing the file is not possible")   
    
