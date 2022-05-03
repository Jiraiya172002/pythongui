def rkch():
    f=open("rkch.txt","r")
    p=open("send.txt","w")
    t=f.read()
    u = t[0 : 150]
    p.write(u)
    f.close()
    p.close()
    z=open("send.txt","r")
    x=z.read()
    print(x)
    
        
rkch()
