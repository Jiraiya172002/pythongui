import math
def mersenne(n):
    c=1
    for i in range(c,n+1):
        a=math.pow(2,i-1)
        print(a-1)
i=int(input("Enter the no"))
mersenne(i)
