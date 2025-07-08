# Invert a dictionary with list values (group keys by their values)
# Input:
# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# Output:
# {1: ['a', 'c'], 2: ['b'], 3: ['d']}
import copy

d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
a={}

for key,value in d.items():
    if value in a:
        a[value].append(key)
    else:
        a[value]=[key]

print(a)
# Find Max and Min Value in Dictionary
# Input:
# d = {'a': 10, 'b': 5, 'c': 15}
# Output:
# Max Value → 15
# Min Value → 5
d = {'a': 10, 'b': 5, 'c': 15}

# for key,values in d.items():
#     if values>max:
#         max=values
maxi=max(d.values())
mini=min(d.values())

print(maxi)
print(mini)

# Create a dictionary using dictionary comprehension for the given list of numbers, where:
# Each number is a key.
#
#  The value is "prime" if the number is prime.
#
#  The value is "notprime" if the number is not prime.
# Output:   {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            return False
    return True

prime_dict={numbers:"prime" if is_prime(numbers) else "notprime"  for numbers in range(15)}

print(prime_dict)
# Explain about setdefault function in dictionary data type ?
#it returns the value if it is present in the dict else if key is not present it adds the key with the given default value

# Difference between d[key] and d.get(key)?
d={1:'a' , 2:'b' ,3:'c'}
print(d[1])
print(d.get(6,'f'))
#d[key] returns the key value if not present it raises the error
#d.get(key) returns the key value if not present it gives none .we can also add value to it

# What is the difference between Shallow Copy and Deep Copy in Python? Explain with examples.
# shallow copy: it points to same adress
d=[1,2,3]
a=d
a[1]=9
print(a)
print(d)
# deep copy:it points to different adresses
a=[1,2,3]
b=copy.deepcopy(a)
b[0]=6
print(a,b)
# Count Vowels in String with Dict Comprehension.
# s = "welcome to python programming"
s = "welcome to python programming"
count=0
for ch in s:
    if ch in 'aeiouAEIOU':
        count+=1
print(count)
# What is an Automorphic Number? Give examples.
#  Expected Answer:
#        An Automorphic Number is a number whose square ends with the number itself.
# Examples: 5 (5² = 25), 6 (6² = 36), 76 (76² = 5776)
def is_automorphic(n):
    square = n * n
    digits = len(str(n))
    return square % (10 ** digits) == n

# Test
for i in range(1, 100):
    if is_automorphic(i):
        print(i, "is Automorphic")






