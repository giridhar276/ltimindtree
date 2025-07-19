# list
alist = [45,12,74,12,5,7,10]
alist.reverse()
print("displaying in reverse order:", alist)

print("Initial values :", alist)
alist.append(90)      # add single value
print("After appending :",alist)
alist.extend([92,39,56])   # add multiple values
print("After extending :", alist)
alist.insert(1,100)    # list.insert(index,value)
alist.insert(3,21)     # list.insert(wheretoinsert,whattoinsert)
print("After inserting :",alist)
alist.pop(0)  #  list.pop(index)  # we ar suppose to pass index to list.pop
print("Using pop method :", alist)
alist.remove(12)   #  12 is in the value in the list
print("After removing :",alist)
alist.sort()  # be default , its sorts in ascending order
print("After sorting :",alist)
alist.sort(reverse=True)  # descending order
print("After sorting in descending order:",alist)
alist.reverse()
print("displaying in reverse order:", alist)

if 120 in alist:
    alist.remove(120)
else:
    print(120,"is not found in the list")


#### check for existence of the substring
name = "python programming"
if "python" in name:
    print("substring found")
else:
    print("not found")


name = "python programming"
print(name.find("abc"))  # check for substring
# returns -1  if substring is not found
# returns index if substring is found














          








