

# 1. Greet user
name = "Alice"
print("Hello, {}!".format(name))        # str.format()
print(f"Hello, {name}!")                # f-string

# 2. Multiple variables
age = 30
 print("Name: {}, Age: {}".format(name, age))  # str.format()
print(f"Name: {name}, Age: {age}")            # f-string

# 3. Positional arguments
print("The {1} is better than the {0}.".format("past", "future"))  # str.format()
past = "past"
future = "future"
print(f"The {future} is better than the {past}.")                  # f-string
