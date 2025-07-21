def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num=int(input("Enter a number to check prime or not:"))
if prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")
        
