#### function overloading in python
#### default arguments

def display(a = 0,b = 0,c = 0,d = 1):
    print(a,b,c,d)



display()  # 0 0 0 0
display(10)# 10 0  0 0
display(10,20)  # 10 20 0 0
display(10,20,30) # 10 20 30 0 
display(10,20,30,40) # 10 20 30 40
