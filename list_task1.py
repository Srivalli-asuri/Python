# Even or Odd Checker:
# Take an integer as input and print whether it's even or odd.
def even(n):
    if n%2==0:
        print("even")
    else:
        print("odd")

even(7)
# Sum of Digits:
# Given a number, find the sum of its digits (e.g., 123 ➝ 6).
def sum(n):
    sum=0
    while(n>0):
        rem=n%10
        sum+=rem
        n=n//10
    return sum
a=sum(123)
print(a)
# Count Vowels in a String:
# Input a string and count how many vowels it contains.
def vowels(str):
    count=0
    for ch in str:
        ch=ch.lower()
        if ch in 'aeiou':
            count+=1
    return count

print(vowels("srivalliI"))
# Check Palindrome:
# Check if a given string or number is a palindrome (same forward and backward).
def palindrome(n):
    num=n
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev==num

if palindrome(11111):
    print('Its a palindrome')
else:
    print("not")

def pali(str):
    duplicate=''
    for i in range(len(str)-1,-1,-1):
        duplicate+=str[i]
    return str==duplicate

if pali('mam'):
     print("palindrome")
else:
     print("not")
# Find Maximum in a List:
# Given a list of numbers, find and print the maximum number.
def list(l):
    a=l[0]
    for i in range(len(l)):
        if l[i]>a:
            a=l[i]
    return a
print(list([1,2,3,4]))
