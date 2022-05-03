def find():
    f=open("abc.txt","r")
    while True:
        s = f.readline()
        t = s.split()
        for i in t:
            if(i[0] == 'm' or i[0] =='M'):
                print(i, end=' & ')
        if(len(s) <= 0):
            break
        

find()
