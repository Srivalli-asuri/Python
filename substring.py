# Count the palindrome substrings in a given input.
word='malayali'
Count=0
for i in range(len(word)):
  temp=''
  for j in range(i+1,len(word)):
    temp+=word[j]
    if temp==temp[::-1]:
      Count+=1
print(Count)
