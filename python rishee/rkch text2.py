def count():
    c=0
    p=0
    f=open("Article.txt","r")
    while True:
         t=f.readline()
         for i in t:
             if(t[0]=="t"):

                c=c+1
             elif(t[0]=="a"):

                 p=p+1
         if(len(t)<=0):
            break
    print("The no of lines with first letter t==",c)     
    print("The no of lines with first letter t==",p)     

count()

            
