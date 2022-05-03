def insrt_info(l):
    ch="y"
    while(ch=="y"):
        ro=int(input("Enter the rollno of the student"))
        na=input("enter the name of the student")
        z=(ro,na)
        l.append(z)
        ch=input("Do you want to store more data")
        if(ch=="n"):
            break
    print("Records in the file are","\n",l)
    print("\n","\n")
def delet(l):
    if(len(l)<=0):
        print("the list is empty")
    else:
        a=l.pop()
        print("The deleted record is","\n",a)
        print(l)
        print("\n","\n")
print("1: do you want to insert the information")
print("2:do you want to delete the information")
print("3: do you wnt to show the information")
b=[]    
ch='y'
while(ch=="y"):
    a=int(input("what do you want=====>"))
    if(a==1):
        insrt_info(b)
    elif(a==2):
        delet(b)
    elif(a==3):
        print(b)
        print("\n","\n")    
    else:
        break
print("thanks for visiting the software")
