# What is a Python Dictionary?
# A dictionary in python is a collection of key value pairs
# each key is unique and used to acccess the value from the dictionary
# 2.	How can you access a value from a dictionary?
# we can access the value using [] brackets or .get method
a={1:'a' , 2: 'b' ,3: 'c'}
print(a[1])
print(a.get(1))

# 3.	What will happen if you access a non-existent key  Give an example?
# it will give you a key errror

# 4.	How do you add or update a key-value pair in a dictionary?
a={1:'a' , 2: 'b' ,3: 'c'}
a[4]='d'  #adding the new keyvalue pair
a[2]='f' #updating the existing one
print(a)
# 5.	How do you remove a key-value pair from a dictionary?
a={1:'a' , 2: 'b' ,3: 'c'}
del a[1]
print(a)
s=a.pop(3)
print(s)
# 6.	How do you get all the keys, values, or items in a dictionary?
a={1:'a' , 2: 'b' ,3: 'c'}
print("keys",a.keys())
print("values",a.values())
print("items",a.items())
