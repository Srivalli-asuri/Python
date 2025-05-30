#sum of digits
def sumod(n):
    sum=0
    while n>0:
        num=n%10
        sum+=num
        n//=10
    return sum
print(sumod(1234))
#reverse a number
def revn(n):
    rev=0
    while n>0:
        num=n%10
        rev=rev*10+num
        n//=10
    return rev
print(revn(1234))
#palindrome
def palindrome(o):
    return o==revn(o)
o=1112
if palindrome(o):
    print("its a palindrome")
else:
    print("not a palindrome")

#
def countf(a,b):
    count=0
    for i in range(a,b):
        if palindrome(i):
            count+=1
    return count
print('the no.of palindromes bw the given range are',countf(1,1000))
##ananymous function to check even or odd using ternary operators
b=lambda a:'even' if a%2==0 else 'odd'
print(b(3))
