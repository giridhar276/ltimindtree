

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



numbers = [x for x in range(1, 11)]
print(numbers)


# Generate a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)


#Create a list of even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)


#Create a list of odd numbers from 1 to 15
odds = [x for x in range(1, 16) if x % 2 != 0]
print(odds)

#Convert all items in a list of strings to uppercase
fruits = ["apple", "banana", "cherry"]
uppercased = [fruit.upper() for fruit in fruits]
print(uppercased)


Get all vowels from a string
#Input: "education"


word = "education"
vowels = [ch for ch in word if ch in "aeiou"]
print(vowels)
#Output: ['e', 'u', 'a', 'i', 'o']



#Create a list of numbers divisible by 3 from 1 to 30
div_by_3 = [x for x in range(1, 31) if x % 3 == 0]
print(div_by_3)


#Create a list of positive numbers from a list
nums = [-5, 3, -1, 9, 0, -2]
positives = [x for x in nums if x > 0]
print(positives)



#Create a list of lengths of each word in a sentence
sentence = "I love Python programming"
lengths = [len(word) for word in sentence.split()]
print(lengths)


#Create a list of squares only for even numbers from 1 to 10
squares_even = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares_even)


#Create a list with 'even' or 'odd' labels for numbers 1 to 5
labels = ['even' if x % 2 == 0 else 'odd' for x in range(1, 6)]
print(labels)



#Get all words with more than 3 characters

words = ["hi", "hello", "sun", "world"]
filtered = [w for w in words if len(w) > 3]
print(filtered)
#Output: ['hello', 'world']


#Get numbers greater than 10 from a list
nums = [5, 12, 7, 15, 3]
greater_than_10 = [x for x in nums if x > 10]
print(greater_than_10)


# Remove spaces from a list of strings
#Input: [" hello", "world ", " python "]
words = ["  hello", "world  ", "  python  "]
stripped = [w.strip() for w in words]
print(stripped)


#Get common elements from two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = [x for x in a if x in b]
print(common)


#Create a list of strings that are digits only
items = ["123", "abc", "456", "xyz"]
digits_only = [x for x in items if x.isdigit()]
print(digits_only)
#Output: ['123', '456']


























Convert all items in a list of strings to uppercase
