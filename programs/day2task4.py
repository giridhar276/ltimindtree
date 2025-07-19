n=int(input("Enter the number: "))
fact=1
for i in range(2,n+1):
    print(fact,"*",i)
    fact*=i
    print(fact)

print(f"factorial of {n} is {fact}")
