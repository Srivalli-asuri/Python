# 1. Reverse the list without using methods
l=[1,2,3,4]
r=[]
for i in range(len(l)-1,-1,-1):
    r.append(l[i])
print(r)
# 2. Sort the list without using methods.
def sort(l):
    n=len(l)
    for i in range(n):
        for j in range(n-1):
            if l[j]>=l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l

print(sort([1,6,7,2,9]))

# 3. Remove duplicates in the list without using methods
def duplicates(list):
    d=[]
    for i in list:
        if i not in d:
            d.append(i)
    print(d)

duplicates([1,2,2,4,5,5,9])

# 4.1) Print the largest value in every list and concate the list
#  [ [2,3,1], [4,5,3], [7,6,8] ] => o/p [3,5,8]
def largest(l):
    a=[]
    for i in l:
        a.append(max(i))
    print(a)

largest([ [2,3,1], [4,5,3], [7,6,8] ])

# 4.2) Sum of Every list
def sum(l):
    sum=0
    for sublist in l:
        for list in sublist:
            
            sum+=list

        print(sum)

sum([[1,2,3],[1,2,3],[1,2,3]])
