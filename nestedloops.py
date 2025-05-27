# 1..Sum of Rows in a 2D List
# Given a 2D list, use nested loops to print the sum of each row.
l=[[1,2] ,[1,3] ,[1,4] ]
for i in l:
    sum=0
    for j in i:
        sum+=j
    print(sum)
# 2..Count Vowels in Multiple Words
# Ask the user to enter 3 words. Use a nested loop to count the number of vowels in each word and print it.
vowels='aeiouAEIOU'
for i in range(3):
    words=input("enter 3 words")
    count=0
    for char in words:
        if char in vowels:
            count+=1
    print(f"Vowels in word '{words}' : {count}")
# 3..Common Elements in Two Lists
# Use nested loops to find and print all common elements between two lists.
common=set()
l1=['sri','valli',3]
l2=['sri','valli',5]
for i in l1:
    for j in l2:
        if i==j:
           common.add(i)
print("common elements are",list(common))
# 4.Multiplication Table from 1 to 5
# Use nested loops to print multiplication results of numbers 1 through 5 in table form (but not as a pattern).
for i in range(1,6):
    for j in range(1,11):
        print(i*j)
# 5. Check Prime Numbers in a Range
# Ask the user for a range (e.g., 1 to 20), then use nested loops to check and print all prime numbers in that range.
start=int(input("enter the start range"))
end=int(input("enter the end range"))
for num in range(start,end+1):
    if num<2:
        continue
    isprime=True
    for i in range(2,num):
        if num%i==0:
            isprime=False
            break
    if isprime:
        print(num)

# 7.Word Search in Sentence
# Ask the user for a sentence and 3 words. Use nested loops to check if each word is present in the sentence.
sentence='enter your name'
words=[]
for i in range(3):
    word=input("enter 3 words")
    words.append(word)
for word in words:
    if word in sentence:
        print(word,"present in the sentence")
    else:
        print(word,"not present in the sentence")

# 8.Find Duplicates in a List
# Given a list of numbers, use nested loops to find and print all duplicate values.
l=[1,2,3,3,8,8,8,9,9]
duplicates=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j] and l[i] not in duplicates:
            duplicates.append(l[i])
print(duplicates)

# 9.Simulate a Simple Grading System
# Ask for marks of 3 students, each with 3 subjects. Use nested loops to input and calculate each student’s total and average.
num_students = 3
num_subjects = 3

for student in range(1, num_students + 1):
    total = 0
    print(f"\nEnter marks for Student {student}:")

    for subject in range(1, num_subjects + 1):
        mark = int(input(f"  Subject {subject} marks: "))
        total += mark

    average = total / num_subjects
    print(f"Total marks for Student {student}: {total}")
    print(f"Average marks for Student {student}: {average:.2f}")

# 10.All Pairs of Even and Odd Numbers
# Given a list of even numbers and a list of odd numbers, use nested loops to print all possible even-odd pairs.

even_numbers = [2, 4, 6]
odd_numbers = [1, 3, 5]

print("All possible even-odd pairs:")

for even in even_numbers:
    for odd in odd_numbers:
        print(f"({even}, {odd})")
