
import time
import os
import datetime
t=os.path.getatime("clients.txt")
print(t)

print("current time: ",datetime.datetime.fromtimestamp(t))

