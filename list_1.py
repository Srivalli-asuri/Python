
# 1. Take the list, take the sub list from the list and replace that sublist with sum of the sublist
def sum(l,start,end):
    sublist=l[start:end]
    sum=0
    for i in sublist:
        sum+=i
    print(sum)
    l[start:end]=[sum]
    return l

a=sum([1,2,3,4,5],1,3)
print(a)

# 2. Find the second largest values in a list
l=[1,2,3,9,11]
f=float('-inf')
s=float('-inf')
for i in l:
   if i>f:
       s=f
       f=i
   elif f>i>s:
       s=i
print('the second largest value in list is',s)
