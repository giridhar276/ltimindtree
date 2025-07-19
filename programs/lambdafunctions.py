# Everything is OS is called process
# Every process contains system calls



def display(a,b):
    c = a+b
    return c

total = display(10,20)
print(total)

################# lambda function ###############
# Instead of writing the above code... we rewrite the code with labmda function
# lambda function  is the replacement of single liner function
#syntax:  functioname = lambda variables : expression

display = lambda a,b : a + b
total = display(10,20)
print(total)
