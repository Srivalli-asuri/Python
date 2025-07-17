import math
import random as r
print(r.random())

val=r.random()
print(val)
print(math.ceil(val))
print(val*10)
print(math.floor(val*10))
a=10.9

digits=4
otp=""
for i in range(digits):
    num=math.floor(r.random()*10)
    otp+=str(num)
print(otp)

print(r.randint(1,20))
print(r.uniform(2,5))
print(r.choice(["abcdefghijklmnopqrstuvwxyz"]))
a=r.shuffle(['duke' , 'r15' ,'x'])
print(a)

import random

a = ['duke', 'r15', 'x']
r.shuffle(a)
print(a)
r.randrange(start,stop,step)
print(r.randrange(10,50,2))

print(r.getrandbits())
