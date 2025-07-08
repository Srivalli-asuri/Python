#1.sqrt
#userdefined
a=36
sqrt=a**0.5
print(sqrt)
#using modules
import math
print(math.sqrt(a))
#2.power
#userdefined
pow=2**3
print(pow)
#using modules
import math
print(math.pow(2,3))
#3.floor
#user defined
a=5.5//1
print(a)
#using modules
print(math.floor(5.5))
#4.ceil
a=5.5//1 +1
print(a)
#using modules
print(math.ceil(a))
#5.fabs
a=-20
if a<0:
    a=-a
    print(a)
#using modules
print(math.fabs(a))
#6.factorial
n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
#using modules
print(math.factorial(5))
#7.gcd
n1=10
n2=8
for i in range(2,max(n1,n2)):
    if n1%i==0 and n2%i==0:
        print(i)
#using modules
print(math.gcd(n1,n2))
#8.lcm
n1=10
n2=20
for i in range(max(n1,n2),n1*n2+1):
    if i%n1==0 and i%n2==0:
        print(i)
        break

#9.log
print(math.log(10,10))
