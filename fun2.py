# Check if a number is even or odd.
def evenodd(n):
    if n%2==0:
        print(n,'is a even number')
    else:
        print(n,'is a odd number')
evenodd(5)
# Find the largest of three numbers.
def largest(a,b,c):
    if a>b and a>c:
        print(a,'is greater')
    elif b>a and b>c:
        print(b,'is greater')
    else:
        print(c,'is greater')

largest(0,0,0)
# Print all even numbers from 1 to n.
def even(a,b):
    for i in range(a,b):
        if i%2==0:
            print(i,'even')
        else:
            print(i , 'odd')

even(1,20)

# Print the multiplication table of a given number.
def mul(n):
    for i in range(1,11):
       print(n,'*',i,'=',n*i)

mul(8)
# Count the number of digits in a number.
def count(n):
    if n==0:
        return 1
    c=0
    while(n>0):
        n//=10
        c+=1
    return c
b=count(123456)
print(b)
# Reverse a given number.
def rev(n):
    if n==0:
        return 0
    revnum=0
    while(n>0):
        digit=n%10
        revnum=revnum*10+digit
        n//=10
    return revnum
a=rev(98765)
print(a)
# Check if a number is a palindrome.
def palindrome(n):
    if n==0:
        return 0
    revnum=0
    while(n>0):
        digit=n%10
        revnum=revnum*10+digit
        n//=10

    return revnum
n=1111
c=palindrome(n)
if c==n:
    print("Its a palindrome")
else:
    print("Not a palindrome")
# Find the factorial of a number.
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(fact(6))
# Count how many times a specific digit appears in a number.
def rep(num,digit):
    count=0
    while(num>0):
        n=num%10
        if n==digit:
            count+=1
        num//=10
    return count
print(rep(12222222222223,2))
# Check if a number is prime.
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        else:
            return True
n=50
if prime(n):
    print(n,'its a prime number')
else:
    print(n,"not a prime number")
# Print all prime numbers between 1 and n.
def isprime(num):
    if num<2:
        return False
    for i in range(2,int(num*0.5)+1):
        if num%i==0:
            return False
    return True
for i in range(2,10):
    if isprime(i):
        print(i,end=' ')

# Count the number of vowels in a string.
def str(n):
    count=0
    for char in n:
        if char=='a'or char=='e' or char=='i' or char=='o' or char=='u' :
            count+=1
    return count
print()
print(str('10kcoders'))
# Find the sum of digits of a number.
def sum(n):
    n=abs(n)
    sum=0
    while(n>0):
        num=n%10
        sum+=num
        n//=10
    return sum
print(sum(-887))
# Print the Fibonacci series up to n terms.
def fib(n):
    a,b= 0,1
    for _ in range(n):
        print(a,end=' ')
        a,b=b,a+b

fib(5)
# Find the GCD (greatest common divisor) of two numbers.
def gcd(a, b):
    gcdv = 1
    for i in range(1, min(a, b) + 1):  # include min(a, b)
        if a % i == 0 and b % i == 0:
            gcdv = i  # keep updating with latest common divisor
    return gcdv
print()
print(gcd(4,8))
# Find the LCM (least common multiple) of two numbers.
def lcm(a, b):
    lcmv = 1
    for i in range(1, max(a, b) + 1):  # include min(a, b)
        if i % a == 0 and i % b == 0:
            lcmv = i  # keep updating with latest common divisor
    return lcmv
print()
print(lcm(4,12))
# Check if a string is a palindrome.
def check_first_last_same(n):
    if n[0] == n[-1]:
        return True
    else:
        return False

if check_first_last_same("mam"):
    print("yes")
else:
    print("no")

# Count how many even and odd numbers are in a list.
l=[1,2,3,4]
even=0
odd=0
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even,even)
print(odd,odd)
# Find and print all factors of a given number.
def factor(n):
    for i in range(1,n):
        if n%i==0:
            print(i,end=' ')

factor(10)
print()
# Check if a number is an Armstrong number (e.g., 153 → 1³ + 5³ + 3³ = 153)
def arm(num):
    hundreds=num//100
    tens=(num//10) % 10
    units=num%10

    total=hundreds**3+tens**3+units**3
    return total==num

num=153
arm(num)
if arm(num):
    print("armstrong num")
else:
    print("not armstrong num")