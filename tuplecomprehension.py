# l = 5200
# o /p: 10 500 notes 1 200 notes
n=5200
res=[]
tem=[500,200,100,50,20]
for x in tem:
    data=n//x
    if data>0:
        res.append(f'{data} {x} notes')
        n=n%x
print(res)
# 2. p = ["Python", "java", "c++"]   # print only python from the list using tuple comprehension
p = ["Python", "java", "c++"]
a=tuple(x for x in p if x=='Python')
print(a)
# 3. print prime numbers between 10 to 20 using tuple comprehension
primes = tuple(
    x for x in range(10, 21)
    if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
)
print(primes)

# 4. given a string "abcd" create a tuple of ASCII value of each character

str='abcd'
t=tuple(ord(ch) for ch in str )
print(t)
# 5.
# l = [1, 2, 3, 4, 5, 6]
# o / p: [[1, 2], [3, 4], [5, 6]]
l = [1, 2, 3, 4, 5, 6]
t=tuple([x,x+1] for x in range(1,6,2) )
print(t)
