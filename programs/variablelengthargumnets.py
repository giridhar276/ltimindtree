###########################
# variable length arguments
###########################
# In pyton, any object starts with * --> it is treated as tuple
def display(*data):
    #print(data)
    for value in data:
        print(value)

display(10,20,30,40,1,2,4,5,6,3,6,7,4,6,4,6,23,6,3,6,3,6,3,4,6,5)



## ** kwargs becomes dictionary
def display(**kwargs):
    for k,w in kwargs.items():
        print(k,w)



display(chap1= 10 , chap2=20,chap3=30)
