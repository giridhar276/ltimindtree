task = input("enter something")  # hello
freq={}
for char in task :
   freq[char]= task.count(char)  # freq['h'] = 1
for key,values in freq.items():
    print(key,values)


##################################### method 2 ################

name = input("Enter any string :")   # hello
data = list(name)  # ["h","e","l","l","o"
for char in set(data) :
    print(char, data.count(char))

