# 1. Print a specific part of a string without using slicing

st="srivalli"
s=''
count=0
for i in st:
    count+=1
    if 4<=count<=8:
        s+=i
print(s)
# 2. Print the string to replace "is" with "si" without using replace method
str="This is a Beautiful place to live.She is Dancing"
res=""
i=0
while i<len(str):
    if i+1<len(str) and str[i]=='i' and str[i+1]=='s':
        res+='si'
        i+=2
    else:
        res+=str[i]
        i+=1

print(res)
