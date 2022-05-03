def change(l):
    l1=[]
    for i in l:
        if(i not in l1):
            l1.append(i)
    return l1
l=[]
for i in range(5):
    n=int(input("Enter the number"))
    l.append(n)
print(l)
p=change(l)
print("the list after functioning===>",p)
 
    
