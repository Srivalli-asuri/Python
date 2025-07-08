# 1. Create a dictionary without using {} curly brackets.The dictionary should store the following information:
# Result = {‘name’:’kumar’,’pin’:101}
result=dict(name='kumar' , pin='209')
r=dict(n='sri',v='33')
print(result)
print(r)
# 2.Sort Dictionary by Values (Descending Order)
# EX: Input: {'apple': 50, 'banana': 20, 'mango': 80}
innput= {'apple': 50, 'banana': 20, 'mango': 80}

# 3. Count Frequency of Each Word in a Sentence?
# EX:  "hello world hello python"
i="hello world hello python"
res={}
words=i.split()
for ch in words:
    if ch in res:
        res[ch]+=1
    else:
        res[ch]=1
print(res)
# 4. Merge Two Dictionaries with out using update method?
dict1={'a':1,'b':2 }
dict2={'c':3 ,'d' :4}
merged={}
for key in dict1:
    print(key)
    merged[key]=dict1[key]
for key in dict2:
    merged[key]=dict2[key]
print(merged)
# 5. Invert a Dictionary (Swap keys and values)
# Input: {'a': 1, 'b': 2, 'c': 3}
#    Output: {1: 'a', 2: 'b', 3: 'c'}
i={'a': 1, 'b': 2, 'c': 3}
res={}
for key,values in i.items():
    res[values]=key
print(res)
# 6. Find Sum of All Values in a Dictionary
#  Input: {'a': 10, 'b': 20, 'c': 30}
i={'a': 10, 'b': 20, 'c': 30}
sum=0
for key,values in i.items():
    sum+=values

print(sum)
