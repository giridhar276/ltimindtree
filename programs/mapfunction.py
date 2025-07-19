##output:   [15,25,35,45]
alist =[10,20,30,40]
blist = []
for val in alist:
    blist.append(val + 5)
print(blist)

## method2
#map(function,list)
alist =[10,20,30,40]
print(list(map(lambda x : x+5,alist)))  # [15,25,35,45]
##########################################################

alist = ["python","unix","c","oracle"]
#[6,4,,1,6]
print(list(map(lambda x: len(x),alist)))
##########################################################
##### map() without lambda ########
def myfunc(x):
    return x+5

alist =[10,20,30,40]
print(list(map(myfunc,alist)))

















