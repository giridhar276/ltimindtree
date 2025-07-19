

aset = {10,10,10,10,10,20,20,20,30}
bset = {30,30,30,40,40,40,50}


print(aset)
print(bset)

print(aset.union(bset))
print(aset.intersection(bset))

# add new value to the set
aset.add(60)
print("After adding :", aset)


print(aset.issubset(bset))
print(aset.issuperset(bset))
