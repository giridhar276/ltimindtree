
# random library

import random
print(random.random()) # random decimal between 0 and 1

# random number betwween the mentioned range
print(random.randrange(1,100))
print(random.randrange(1000,1000000))

alist = [34,67,2,78,32,3,34,9]
print("before shuffling :", alist)
# random.shuttle(list) ---> shuffles the list
random.shuffle(alist)
print("after shuffling :", alist)

### random.choice(list) 
alist = ["python","unix","c","java","oracle","oracle","microsoft","react"]
print(random.choice(alist))

print(random.sample(alist,3))  # 3 random samples  

print(random.uniform(1.1,9.9))  # generate decimal value between these values
