def  rkch():
    f=open("rkch.txt","r")
    while True:
        s = f.readline()
        t = s.split()
        for i in t:
            if(i[0] == 'a' or i[0] =='e' or i[0] =='i' or i[0] =='o' or i[0] =='u'):
                print(i)
        if(len(s)<= 0):
            break
rkch()
