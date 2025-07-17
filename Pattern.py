# Print the patterns
# H
# E
# N
rows=5
for i in range(1,rows+1):
    res=''
    for j in range(1,rows+1):
        if j==1 or j==rows or i==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
rows=5
#E
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or i==1 or i==rows or i==(rows//2)+1:
            res+='*'+' '
        else:
            res+=' '+' '
    print(res)
 #N
rows=5
for i in range(rows+1):
     res=""
     for j in range(rows+1):
         if j==1 or j==rows or i==j:
            res+='*'+' '
         else:
            res+=' '+' '
     print(res)






