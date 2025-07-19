book = {"chap1":10 ,"chap2":20 ,"chap3":30 ,"chap1":100}
# add new key-value pairs
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print("updated book :",book)
## display individual values
print(book["chap1"])
print(book["chap4"])
## display keys
print(book.keys())
# display values
print(book.values())
# display items
print(book.items())
# remove key-value pair
book.pop("chap1")  # chap1-100 will be removed from dictionary
print(book)
book.popitem()     # remove  
print(book)
book.popitem()

print(book)



 


#method2
book.update(newbook)
print("updated book:", book)
























