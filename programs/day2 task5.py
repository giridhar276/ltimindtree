str1 = input("enter a sentence")
str1 = str1.split(" ")
str1.sort()
for i in str1:
    print(i.capitalize())
