def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "cant divide by zero"
    return a/b

def calculator():
    print("Simple Calculator")
    print("Choose operation")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")

    choice=int(input("enter the choice 1 |2|3 |4 "))
    if choice not in [1,2,3,4]:
        print("Invalid Choice")
        return

    a=float(input("enter the first number"))
    b=float(input("enter the second number"))

    if choice==1:
        print("Result",add(a,b))
    elif choice==2:
        print("Result",sub(a,b))
    elif choice==3:
        print("Result",mul(a,b))
    elif choice==4:
        print("Result",div(a,b))

calculator()



