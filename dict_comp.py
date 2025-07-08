# Delete a list of keys from a dictionary
# sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
# # Keys to remove
# keys = ["name", "salary"]

sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
a=["name","salary"]
for keys in a:
    sample_dict.__delitem__(keys)
print(sample_dict)
# Count the frequency of each character in a given string using a dictionary.
j='pyytthon'
d={}
for x in j:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
print(d)
# Write a Python program to create a dictionary with two keys:
# "even" → containing all even numbers from the list
# "odd" → containing all odd numbers from the list
# Expected Output:
# {'even': [0, 2, 4, 6, 8], 'odd': [1, 3, 5, 7, 9]}
dict={'even':[],'odd':[]}
for x in range(10):
    if x%2==0:
        dict['even'].append(x)
    else:
        dict['odd'].append(x)
print(dict)
# What is the difference between dict.get() and direct key access?
# directaccessing gives you a error when key is not present where as get method returns none if not present
a={1:'a' ,2: 'b'}
print(a[1])
# print(a[3])
print(a.get(6))
# Convert a dictionary to a list of tuples.
a={1:'a' ,2: 'b'}
d=list(a.items())
print(d)
# Write a program to store names as keys and their lengths as values
# names = input("Enter names separated by space: ").split()
# d = {name: len(name) for name in names}
# print(d)
# Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and "odd" if the number is odd
# Expected Output:
#
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
res={'even' : [ i for i in range(1,10) if i%2==0],
     'odd'  : [i for i in range(1,10) if i%2!=0]
     }
print(res)
# Create Reverse Word Dictionary
# Given list of words:
# words = ["cat", "dog", "bat"]
# Create a dictionary with words as keys and their reversed strings as values
#
# Expected Output:
# {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}
words = ["cat", "dog", "bat"]
d = {}
for word in words:
    d[word] = ''.join(reversed(word))
print(d)
# Write a program to sum all the values in a dictionary.
d={'sri':1 , 'valli' :2 ,'asuri' :3}
value=0
for key,values in d.items():
    value+=values
print(value)


