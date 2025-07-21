import os
import datetime

os.mkdir("newdir")
print("newdir created")
## deleting directory
os.rmdir("newdir")
print("newdi deleted")
# dipslay os name
print("OS name :", os.name)
# display file size
print(os.path.getsize("clients.txt"),"bytes")
# display todays time
print(datetime.datetime.now())

# display accessed time of the time
accessedtime = os.path.getatime("clients.txt")  # will return epoch time
print(accessedtime)
print(datetime.datetime.fromtimestamp(accessedtime)) # epoch to human readable
#### display present working directory
print("current working directory :", os.getcwd())
## dsiplay files in present working directory
for file in os.listdir():
    print(file)  
