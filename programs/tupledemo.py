

alist = [10,20,30,40,50]
alist[0] = 100
print(alist)


atup = (10,20,30,40)
alist = list(atup)  # typecasting - converting from one object to another object
alist.append(50)    # making changes to list
atup = tuple(alist) # reconverting back to tuple
print(atup)


print(atup.count(20))  # 1
print(atup.index(40))
