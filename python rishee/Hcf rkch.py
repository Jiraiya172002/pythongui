def bk(a,b):
    c=1
    for i in range(1,a+1):
        if(a%i==0 and b%i==0):
            c=i
    print("hcf of numbers",c)
x=int(input("Enter the number"))
y=int(input("enter the number"))
bk(x,y)
            
