

word=input("Enter a String:")
size=len(word)
result=""
for i in range(size-1,-1,-1):
    result+=word[i]
print(result)


#########
word=input("Enter a String:") # python
revstr = ""
for char in word:
    revstr= char + revstr
print(revstr)

#p
#y+p = yp
#t +yp =  typ
#h + typ =   htyp
#o + htyp = ohtyp
#n + ohtyp = nohtyp


