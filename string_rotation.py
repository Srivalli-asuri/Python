# Rotate a string k no.of times from left to right and right to left
#left to right
str='abcde'
k=2
em=str[k:]+str[:k]
print(em)
#right to left
str='abcde'
k=2
em=str[-k:]+str[:-k]
print(em)
