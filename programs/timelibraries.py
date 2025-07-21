import time
import datetime
import calendar
import datetime

print(time.time())  #epoch time
# what is epoch time ?
# every system or server or embeddeddevice generates epoch time
# epoch time is nothing but the number seconds from jan 1st 1970

# method1
# converting to human readable format
epoch = time.time()   # ----> will display epoch time in seconds
print("current time :",datetime.datetime.fromtimestamp(epoch))

# method2
# if you want the timestamp directly
print(datetime.datetime.now())
print(datetime.date.today())
########### display calendar
print(calendar.month(2025,7))
print(calendar.calendar(2025))
