def Desc_list (L):
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if(L[i]<L[j]):
                t=L[i]
                L[i]=L[j]
                L[j]=t
    print(L)
L=[]
for i in range(5):
    n=int(input("Enter no. for list:---->"))
    L.append(n)    
print(L)
Desc_list(L)
