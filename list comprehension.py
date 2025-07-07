# Rotate a list by k positions to the right.
# Example:
# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]
lst = [1, 2, 3, 4, 5]
k = 2
b=lst[-k:]+lst[:-k]
print(b)
# Remove all duplicates from a list without using set().
# Input: [1, 2, 3, 2, 1, 4, 5]
# Output: [1, 2, 3, 4, 5]
i=[1, 2, 3, 2, 1, 4, 5]
o=[]
for ch in i:
    if ch not in o:
        o.append(ch)
print(o)

# Find all pairs in a list that sum up to a target.
# Input: lst = [2, 4, 3, 5, 7], target = 7
# Output: [(2, 5), (4, 3)]
lst = [2, 4, 3, 5, 7]
target = 7
output = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            output.append((lst[i],lst[j]))
print(output)
# Flatten a 2D list without using built-in flatten functions.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]
input=[[1, 2], [3, 4], [5]]
o=[ ]
for sublist in input:
    for list in sublist:
        o.append(list)
print(o)

# Count the frequency of each element in a list and return a dictionary.
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: {1: 2, 2: 3, 3: 1, 4: 1}
i=[1, 2, 2, 3, 1, 4, 2]
freq={}
for item in i:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1

print(freq)

# Part B: Strings (5 Questions)
# Check if a string is a palindrome (ignoring spaces and case).
# Input: "A man a plan a canal Panama"
# Output: True
ip="A man a plan a canal Panama"
cleaned=ip.replace(' ','').lower()
ispalindrome=cleaned==cleaned[::-1]
print(ispalindrome)
# Find the first non-repeating character in a string.
# Input: "aabbcdeff"
# Output: 'c'
inp='aabbcdeff'
freq={}
for item in inp:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)
for ch in freq:
    if freq[ch]==1:
        print(ch)
        break

# Remove all vowels from a string.
# Input: "Hello World"
# Output: "Hll Wrld"
inp="Hello World"
out=""
for ch in inp:
    if ch not in 'AEIOUaeiou':
        out+=ch

print(out)
# Count the number of words in a string without using .split().
# Input: "Python is great"
# Output: 3
i= "Python is great"
count=1
for ch in i:
    if ch==" ":
        count+=1
print(count)

# Find the longest word in a sentence.
# Input: "The quick brown fox jumps over the lazy dog"
# Output: "jumps"
i="The quick brown fox jumpsss over the lazy dog"
b=i.split(" ")
longest=''
l=0
for words in b:
    if len(words)>l:
        l=len(words)
        longest=words
print(longest)










