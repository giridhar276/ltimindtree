'''
num=int(input("enter any number"))
sums=0 
for i in range(1,num+1):
    sums=sums+i
print(sums)
#
'''
def sums(num):
    sums = 0
    for i in range(1,num+1):
        sums=sums+i
        #return sums
    print(sums)

num=int(input("enter any number"))
sums(num)


def sumwithret(num):
    sums = 0
    for i in range(1,num+1):
        sums=sums+i
    return sums

num=int(input("enter any number"))

result = sumwithret(num)
print(result)
