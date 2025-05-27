def fun(): #function definition
    print('hello')

fun() #function calling
def add(a,b):
    result=a+b
    print(result)
add(1,2)

def evenorodd(n):
    if n%2==0:
        return True
    else:
        return False
print(evenorodd(4))


def findmax(a,b,c):
   return max(a,b,c)
print(findmax(1,2,3))



def fact():
    fact=1
    for i in range(1,6):
        fact*=i
    return fact
print(fact())