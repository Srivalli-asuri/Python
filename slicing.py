# 1. Extract First 4 Characters
# Given a string s = "developer", slice and print only the first 4 characters.
s = "developer"
print(s[0:4])
# 2. Last 3 Characters
# Given a string s = "innovation", use negative indexing to print the last 3 characters.
a = "innovation"
print(a[-3:])
# 3. Middle Substring
# Print the substring "gram" from the string s = "programming" using slicing.
s = "programming"
print(s[3:7])
# 4. Reverse the String
# Reverse the string s = "python" using slicing.
s = "python"
print(s[-1:-7:-1])
# 5. Skip Characters
# Print every second character from the string s = "abcdefghijk".
s = "abcdefghijk"
print(s[0:len(s):2])
# 6. Remove First and Last Character
# Given s = "machine", print the string without the first and last characters.
s = "machine"
print(s[1:len(s)-1])
# 7. Last 5 Letters Using Negative Index
# Use negative indexing to get the last 5 characters of s = "Artificial".
s = "Artificial"
print(s[-1:-6:-1])
# 8. Reverse a Word Except First and Last Letter
# For string s = "example", reverse everything except the first and last characters.
s = "example"
print(s[-2:-7:-1])
# 9. Check Palindrome with Slicing
# Check if a given string s is a palindrome using slicing.
s="mamam"
print(len(s))
a=s[-1:-len(s)-1:-1]
print(a)
if a==s:
    print("its palindrome")
else:
    print("not a palindrome")
# 10. Substring From Middle to End
# Print the second half of the string s = "datastructure" using slicing.
s = "datastructure"
l=len(s)//2
print(l)
print(s[l:])
# 11. Even Indexed Characters
# From s = "abcdefgh", print only the characters at even indexes (0, 2, 4, ...).
s = "abcdefgh"
print(s[0:len(s):2])
# 12. Substring Excluding Middle Characters
# For s = "HelloWorld", remove the middle 4 characters using slicing.
s = "HelloWorld"
print(s[0:3]+s[7:10])
# 13. Replace Substring Using Slicing
# Given s = "hello123world", replace "123" with "ABC" using slicing.
s = "hello123world"
print(s[0:5]+"ABC"+s[8:])
# 14. Get String in Reverse Every 2nd Letter
# From s = "abcdefghij", print the string in reverse, skipping every second letter.
s="abcdefghij"
print(s[-1:-len(s)-1:-2])
# 15. Wrap Around Indexing
# Access the second character using a negative index in the string s = "index".
s = "index"
print(s[-4])