num=int(input("enter the number"))
isprime = False
for i in range(2,num):
    if num%i==0:
        isprime = True
if isprime:
    print("this is not prime number")
else:
    print("this is a prime number")
    
