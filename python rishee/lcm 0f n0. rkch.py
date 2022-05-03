def fun(n):
    if(n == 0):
        return 1
    elif(n %2 == 0):
        print(n)
    fun(n -1)
        
x=int(input("Enter the no. for lcm:------"))
fun(x)

