# Assignment: Number-Based Challenges (Without Using Strings or Collections)

# 1. Armstrong Number Check
n = 153
hundreds = n // 100
tens = (n // 10) % 10
units = n % 10
armstrong = hundreds**3 + tens**3 + units**3
if n == armstrong:
    print("1. Armstrong Number: Yes")
else:
    print("1. Armstrong Number: No")

# 2. Prime Digit Count
def is_prime(d):
    if d < 2:
        return False
    for i in range(2, int(d**0.5) + 1):
        if d % i == 0:
            return False
    return True

def count_prime_digits(n):
    count = 0
    while n > 0:
        d = n % 10
        if is_prime(d):
            count += 1
        n = n // 10
    return count

print("2. Prime Digit Count:", count_prime_digits(23576))

# 3. Number Pyramid
n = 5
num = 1
print("3. Number Pyramid:")
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 4. Prime Numbers in Range
print("4. Prime Numbers from 1 to 50:")
for i in range(2, 51):
    prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i, end=" ")
print()

# 5. GCD and LCM
a, b = 12, 18
gcd = 1
for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i
lcm = (a * b) // gcd
print("5. GCD:", gcd, "LCM:", lcm)

# 6. Digit Alternation Check
def alternates_even_odd(n):
    prev = n % 10
    n = n // 10
    while n > 0:
        curr = n % 10
        if (prev % 2 == curr % 2):
            return False
        prev = curr
        n = n // 10
    return True

print("6. Alternates Even/Odd:", alternates_even_odd(2727))

# 7. Binary to Decimal
num = 1011
power = 0
decimal = 0
while num > 0:
    rem = num % 10
    decimal += rem * (2 ** power)
    power += 1
    num = num // 10
print("7. Binary to Decimal:", decimal)

# 8. Decimal to Binary
dec = 11
binary = 0
place = 1
while dec > 0:
    rem = dec % 2
    binary += rem * place
    place *= 10
    dec = dec // 2
print("8. Decimal to Binary:", binary)

# 9. Kaprekar Number
n = 45
sq = n * n
d = 1
while 10**d <= sq:
    d += 1
split = 10 ** (d // 2)
left = sq // split
right = sq % split
print("9. Kaprekar:", (left + right == n))

# 10. N-th Prime Number
n = 10
count = 0
i = 2
while True:
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        count += 1
        if count == n:
            print("10. 10th Prime:", i)
            break
    i += 1

# 12. Happy Number
n = 19
def is_happy(n):
    slow = n
    fast = n
    while True:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))
        if slow == 1 or fast == 1:
            return True
        if slow == fast:
            return False

def sum_of_squares(num):
    total = 0
    while num > 0:
        d = num % 10
        total += d * d
        num = num // 10
    return total

print("12. Happy Number:", is_happy(n))

# 13. Harshad Number
n = 18
sum_digits = 0
temp = n
while temp > 0:
    sum_digits += temp % 10
    temp = temp // 10
print("13. Harshad Number:", n % sum_digits == 0)

# 14. Number Reduction Game
n = 7
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1
print("14. Steps to 1:", steps)

# 15. Sum = Product of Digits
print("15. Digits where sum = product (1 to 1000):")
for i in range(1, 1001):
    temp = i
    s = 0
    p = 1
    while temp > 0:
        d = temp % 10
        s += d
        p *= d
        temp = temp // 10
    if s == p:
        print(i, end=" ")
print()

# 16. Magic Number
def is_magic(n):
    while n > 9:
        s = 0
        while n > 0:
            s += n % 10
            n = n // 10
        n = s
    return n == 1

print("16. Magic Number:", is_magic(1729))

# 17. Reverse and Prime Check
def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n = n // 10
    return rev

def both_prime(n):
    rev = reverse(n)
    return is_prime(n) and is_prime(rev)

print("17. Reverse and Prime:", both_prime(13))

# 18. Increasing/Decreasing Order
n = 54321
order = None
flag = True
prev = n % 10
n = n // 10
while n > 0:
    curr = n % 10
    if order is None:
        order = curr < prev
    elif (curr < prev) != order:
        flag = False
        break
    prev = curr
    n = n // 10
print("18. Strict Order:", flag)

# 19. Square Pattern (n=3)
n = 3
count = 1
print("19. Square Pattern:")
for i in range(n):
    for j in range(n):
        print(count, end=" ")
        count += 1
    print()

# 20. Smallest Number > N and its reverse divisible by 7
n = 100
while True:
    r = reverse(n)
    if n % 7 == 0 and r % 7 == 0:
        print("20. Smallest Number > N and reverse divisible by 7:", n)
        break
    n += 1
