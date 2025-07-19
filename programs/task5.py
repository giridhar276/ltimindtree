

name = input("Enter any string :")

ucount = 0
lcount = 0
dcount = 0

for char in name :
    if char.isupper():
        ucount+=1
    elif char.islower():
        lcount+=1
    elif char.isdigit():
        dcount+=1

print('Total no. of uppercase letters :', ucount)
print("Total no. of lowercase letters :", lcount)
print("Total no. of digits            :", dcount)
