# create a dictionary of 4 categories and print seperately using functions
dic={
    'fruits':['apple','banana','mango'],
    'vegetables':['tomato','beetroot','potato'],
    'subjects':['telugu','hindi','english']
}
def fruit():
    print("fruits :",dic['fruits'])
fruit()

def vegetable():
    print("Vegetables :" ,dic['vegetables'])
vegetable()

def subject():
    print('subjects : ' , dic['subjects'])
subject()
# print the items in asc or dsc
items = [8, 6, 9, 2, 5, 1]

# Bubble sort (ascending)
for i in range(len(items)):
    for j in range(0, len(items) - i - 1):
        if items[j] > items[j + 1]:
            items[j], items[j + 1] = items[j + 1], items[j]

print("Ascending:", items)
# print avg of the items quantity and items price

# find the frequency of letters the string using dictionary
st='abcccdee'
res={}
for ch in st:
    if ch in res:
        res[ch]+=1
    else:
        res[ch]=1

print(res)
