# Reverse a String Without Using [::-1]:
# Reverse a string using a loop or recursion.
def pali(str):
    duplicate=''
    for i in range(len(str)-1,-1,-1):
        duplicate+=str[i]
    return duplicate

a=pali("10kCoders")
print(a)
# Count Frequency of an Element in a List:
# Input a list and an element; count how many times the element appears.
def count(s,element):
    c=0
    for i in s:
        if i==element:
            c+=1
    print(c)
count([1,2,2],2)

# Print First N Prime Numbers:
# Take N as input and print the first N prime numbers.
# Take input from the user
n = int(input("Enter how many prime numbers you want: "))
count = 0
num = 2
while count < n:
    is_prime = True

    # Check if current number is prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1

# Remove Duplicates from a List:
# Given a list, return a new list without duplicates (maintain order).
l = [1, 2, 3, 4, 4]
unique_list = []

for item in l:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
# FizzBuzz:
# For numbers from 1 to N, print:
# “Fizz” if divisible by 3
# “Buzz” if divisible by 5
# “FizzBuzz” if divisible by both
# Else print the number itself.
for i in range(1,10):
    if i%2==0 and i%5==0:
        print("divisible by 3")
    elif i%5==0:
        print("divisible by 5")
    elif i%2==0:
        print("divisible by both")
    else:
        print(i)

