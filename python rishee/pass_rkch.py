def pas():
    c=0
    f=open("rishee.txt","r")
    while True:
        s = f.readline()
        l = s.split()
        for i in l:
            if(i == 'Chetan' or i == 'singh'):
                pass
            else:
                print(i)
        if(len(s) <= 0):
            break
    f.close()   
pas()        
            
