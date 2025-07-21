# write a menu based program for performing arithetic operations
def addition(first,second):
    return first + second

def substraction(first,second):
    return first - second

def multiply(first,second):
    return first * second

first = int(input("Enter first number :"))
second = int(input("Enter second number :"))
operation = input("Enter one among : +  -  *   % :")
?
if operation == "+":
    print(addition(first,second))
elif operation == "-":
    print(substraction(first,second))
elif operation == "*":
    print(multiply(first,second))
