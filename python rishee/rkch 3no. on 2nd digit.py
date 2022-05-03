def rkch(l):
    
    for i in l:
        if( i[-2] == "3"):
            print(i)
        else:
            print("nothing")
a=[]
for i in range(5):
    n=input("Enter the two digit no:-------->>")
    a.append(n)
print(a)
rkch(a)

