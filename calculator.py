##calculator
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("select operation:")
print("1.+")
print("2,-")
print("3./")
print("4.*")

choice=input("enter choice(1/2/3/4):")

if choice in ['1','2','3','4']:
    a=int(input("enter first number"))
    b=int(input("enter second number"))

    if choice=="1":
        print(int(a+b))

    elif choice=="2":
        print(int(a-b))

    elif choice=="3":
        print(int(a/b))
    elif choice=="4":
        print(int(a*b))

    else:
        print("invalid")

        
        









