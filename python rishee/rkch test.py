def count():
    c=0
    b=0
    f=open("counting.txt","r")
    while True:
        t=f.readline()
        m=t.split()
        for i in m:
            if(i=="the"):
                c=c+1
            elif(i=="is"):
                b=b+1
        if(len(t)<=0):
           break
    print("The no of time the ocur in text file==", c)
    print("The no of time to occur in the text file is==",b)
count()

            
