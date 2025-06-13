1. Print First and Last Character of a String

s = "srivalli"
print("First:", s[0])
print("Last:", s[-1])
 2. Reverse a String

s = "python"
rev = ""
for i in range(len(s)-1, -1, -1):
    rev += s[i]
print("Reversed:", rev)
3. Count Vowels in a String

s = "communication"
vowels = 'aeiou'
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel Count:", count)
4. Check if a String is Palindrome

s = "madam"
is_palindrome = True
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        is_palindrome = False
        break
print("Palindrome:", is_palindrome)
 5. Remove Spaces from a String

s = "I love coding"
result = ""
for ch in s:
    if ch != " ":
        result += ch
print("Without spaces:", result)
6. Count Occurrences of 'a' in a String

s = "banana"
count = 0
for ch in s:
    if ch == 'a':
        count += 1
print("Count of 'a':", count)
7. Convert String to Uppercase Without Using .upper()

s = "hello"
result = ""
for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch
print("Uppercase:", result)
8. Replace "is" with "si" Without Using .replace()
s = "This is a test"
result = ""
i = 0
while i < len(s):
    if s[i:i+2] == "is":
        result += "si"
        i += 2
    else:
        result += s[i]
        i += 1
print("Modified:", result)
9. Find Length of String Without Using len()
s = "developer"
length = 0
for _ in s:
    length += 1
print("Length:", length)

