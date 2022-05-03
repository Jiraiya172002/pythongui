def adtoresult(n):
    a=1
    b=1
    print(a,b)
    for i in range(n-2):
        c=a+b
        print(a,"+",b,"===",c)
        a=b
        b=c
n=int(input("Enter the integer"))
adtoresult(n)

