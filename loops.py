
# 1. Write a program to print the sum of all even numbers between 1 and 100.
sum=0
for i in range(2,101,2):
    sum+=i
print("the sum of all even numbers between 1 and 100 is" , sum)
# 2. Write a program that prints the first 10 powers of 2 using a loop.
power=0
for i in range(0,11):
    power=2**i
    print('2 power',i,'is',power)
# 3. Calculate the factorial of a number entered by the user.
n=int(input("enter the number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
# 4. Print the reverse of a given number (e.g., input 1234 → output 4321).
n=1234
rev=0
while(n>0):
    num=n%10
    rev=rev*10+num
    n=n//10
print(rev)
# 5. Count the number of digits in a given integer using a loop.
n=123456789
count=0
while(n>0):
    num=n%10
    count+=1
    n//=10
print(count)
# 6. Write a program that prints all numbers from 1 to 100 that are divisible by both 3 and 5.
for i in range(1,100):
    if i%3==0 and i%5==0:
        print(i)
# 7. Without using multiplication, calculate a * b using addition and a loop.
a=5
b=4
result=0
for i in range(b):
    result+=a
print(result)
# 8. Print the sum of digits of a number entered by the user (e.g., 123 → 1+2+3 = 6).
n=123
sum=0
while(n>0):
    num=n%10
    sum+=num
    n=n//10
print(sum)
# 9. Write a loop to check if a number is a palindrome (number reads the same forwards and backwards).
n=333
original=n
rev=0
while(n>0):
    num=n%10
    rev=rev*10+num
    n=n//10
print(rev)
if rev==original:
    print("Its palindrome")
else:
    print("Not a palindrome")
# 10. Write a program to find the highest digit in a given number.
n=12349
high=0
while(n>0):
    num=n%10
    if num>high:
        high=num
    n=n//10
print(high)

#### 🔀 *Questions Involving Conditionals*

# 11. Write a program to check if a number is positive, negative, or zero.
n=30
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")
# 12. Write a program that takes a number and prints whether it is divisible by 2, 3, both, or neither.
n=30
if n%2==0 and n%3==0:
    print("it is divisible by both 2 and 3")
elif n%2==0:
    print("divisible by 2")
elif n%3==0:
    print('divisible by 3')
else:
    print("not divisible")
# 13. Check if a number is a three-digit number using conditionals.
n=12
count=0
while(n>0):
    num=n%10
    count+=1
    n=n//10
if count==3:
    print("its a 3 digit num")
else:
    print("not a 3 digit num")
# 14. Write a program to check whether a given number is a prime number.
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It's a prime number")
    else:
        print("Not a prime number")
# 15. Write a program to find the largest of three numbers entered by the user using nested if-else.
a=5
b=6
c=8
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")
# 16. Check if a year is a leap year or not.
year=2004
if (year%400==0) or(year%100!=0 and year%4==0):
    print("Its a leap year")
else:
    print("Not a leap year")
# 17. Take an integer input and determine if it is even and greater than 50.
n=78
if n>50 and n%2==0:
    print("its even and greater than 50")
# 18. Write a program to classify a number as:
#  Less than 0: "Negative"
# * 0 to 9: "Single Digit"
# * 10 to 99: "Two Digits"
# * 100 and above: "Three or More Digits"
n=12
count=0
while(n>0):
    num=n%10
    count+=1
    n=n//10
if count==0:
    print("its negative")
elif count==1:
    print("single digit")
elif count==2:
    print("Two digits")
else:
    print("three or more digits")
# 19. Write a program to check if the square of a number is greater than 1000, and if yes, print the square.
num=5
sq=num**2
print("Square",sq)
if sq>1000:
    print("greater than 1000")
else:
    print("not greater than 1000")
# 20. Take two integers as input and determine if one is a factor of the other.
a=6
b=36
if b%a==0:
    print(a,'is a  Factor of ',b)
else:
    print("Not")
