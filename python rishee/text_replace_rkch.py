def rkch():
    f=open("rishee.txt","r+")
    while True:
        t=f.readline()
        s=t.split()
        print(t ,end="_")
        for i in s:
            if(i=="RKCH"):
                i="rishee"
                print(i ,end="_")
            else:
                print(i,end="_")
        if(len(s)<=0):
            break
    f.close()
rkch()


