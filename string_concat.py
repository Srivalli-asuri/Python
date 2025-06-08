# Solve the given programs

# chaitanya-> input
# o/p -> aiaa
def vowel(ip):
    for ch in ip:
        if ch in 'aeiou':
            print(ch,end="")

vowel('chaitanya')
# concat even positions in string chaitanya
def concat_matched_even(a, b):
    for i in range(min(len(a), len(b))):
        if i % 2 == 0:
            print(a[i] + b[i])

concat_matched_even('chaitanya','chaitanya')
# # take two indexes and concat that part of indexes
def ind(str,start,end):
    empty=''
    for i in range(start,end):
        empty=empty+str[i]
    print(empty)

ind('chaitanya',1,4)
# # ex-> 1,4 -> chaitanya -> hai
# 4  means -> 3
