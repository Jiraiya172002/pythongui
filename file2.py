from tkinter import *
import mysql.connector as m
from tkinter import messagebox
root=Tk()
root.geometry("1350x700+0+0")
root.title("Details of Game registery.")
root.configure(background="black")

bg_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\A1Y5u83elyS.png")
user_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\icons8-cloud-account-login-male-100.png")
id_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\icons8-login-as-user-30.png")
pass_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\icons8-password-24.png")

a = StringVar()
b = StringVar()
a.set("Rkch")

b.set("94100")

def sign_in():
    global a
    global b

    username = a.get()
    password = b.get()
    import mysql.connector

    conn=m.connect(host='localhost',user='root',database='game_resistery',password='rkch172002')
    cur=conn.cursor()
    cur.execute("select user_name from new_account")
    result=cur.fetchall()
    r=str(result)

    conn1=m.connect(host='localhost',user='root',database='game_resistery',password='rkch172002')
    cur1=conn1.cursor()
    cur1.execute("select create_password from new_account")
    result1=cur1.fetchall()
    p=str(result1)

    if(username ==''  and password ==''):
        messagebox.showinfo("sign_in","ALL FIELDS ARE REQUIRED.")

    elif(username ==''  or  password ==''):
        messagebox.showinfo("sign_in","ALL FIELDS ARE REQUIRED.")

    elif((username in r) and (password in p)):
        messagebox.showinfo("sign_in","Sign_in is successfully")

        root.destroy()
        
        root1=Tk()
        root1.geometry("1350x700+0+0")
        root1.title("Details of Game registery.")
        root1.configure(background="black")


        bg_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\A1Y5u83elyS.png")
            
        a=IntVar()
        b=StringVar()
        c=StringVar()
        d=StringVar()
        e=IntVar()
        z=StringVar()
        a.set("1")
        b.set("GOD OF WAR")
        c.set("Santa Monica Stu.")
        d.set("KRATOS")
        e.set("DATE")
   
        def E(event):
            b1.config(bg="grey",fg="white")

        def F(event):
            b1.config(bg="white",fg="black")

        def E1(event):
            b2.config(bg="grey",fg="white")
        
        def F1(event):
            b2.config(bg="white",fg="black")

        def E2(event):
            b3.config(bg="grey",fg="white")

        def F2(event):
            b3.config(bg="white",fg="black")
        
        def E3(event):
            b4.config(bg="grey",fg="white")

        def F3(event):
            b4.config(bg="white",fg="black")

        def E4(event):
            b5.config(bg="grey",fg="white")

        def F4(event):
            b5.config(bg="white",fg="black")
                
        def Sumit():
            import mysql.connector
            conn = m.connect(host='localhost', user ='root', database='game_resistery', password='rkch172002')
            cur = conn.cursor()
            serial_no = a.get()
            name_of_game = b.get()
            created_by = c.get()
            main_charector = d.get()
            date_of_release = e.get()
            sq="insert into game_info values({}, '{}', '{}', '{}', {})".format( serial_no , name_of_game , created_by , main_charector , date_of_release)
            cur.execute(sq)
            conn.commit()
            messagebox.showinfo("Data","Our data is saved successfully")
            conn.close()


        def Back():
            messagebox.showinfo("SORRY!!!!","Not WORKING PROPERLY........")          

        def Reset():
            messagebox.showinfo("Reset","Want To Reset.")
            a.set("")
            b.set("")
            c.set("")
            d.set("")
            e.set("")

        def Exit():
            messagebox.showinfo("Exit","Are you sure")
            root1.destroy()
         
        def show():
            z.delete(0.0,END)
            conn=m.connect(host='localhost',user='root',database='game_resistery',password='rkch172002')
            cur=conn.cursor()
            cur.execute("select * from game_info")
            r=cur.fetchall()
            z.insert(END, "serial_no"+'\t\t'+"name_of_game"+'\t\t'+"created_by"+'\t\t'+"main_charector"+'\t\t'+"date_of_release"+'\n')
            z.insert(END,"\n","     ")
            for i in r:
                for j in i:
                    z.insert(END,str(j) +'\t\t')
                z.insert(END, "\n")
            

        L0=Label(root1,image=bg_photo)
        L0.pack()
        L1=Label(root1, text="GAME REGISTERY",font=("National Cartoon",30, "bold","underline"),fg="white",bg="black",bd=10,relief=GROOVE)
        L1.place(x=0,y=0,relwidth=1)
        L2=Label(root1, text="Serial no.",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
        L2.place(x=40,y=150)
        L3=Label(root1, text="Name of Game",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
        L3.place(x=40,y=250)
        L4=Label(root1, text="Created by",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
        L4.place(x=40,y=350)
        L5=Label(root1, text="Main charector",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
        L5.place(x=40,y=450)
        L6=Label(root1, text="Date of Release",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
        L6.place(x=40,y=550)
        L7=Label(root1, text="Please DONOT enter any space or any symbole b/w the date.",font=("mv boli",7,"underline"),fg="white",bg="black")
        L7.place(x=40,y=590)

        e1=Entry(root1,font=("papyrus",15),textvariable=a ,bd=5,relief=GROOVE)
        e1.place(x=350,y=150)
        e2=Entry(root1,font=("papyrus",15),textvariable=b ,bd=5,relief=GROOVE)
        e2.place(x=350,y=250)
        e3=Entry(root1,font=("papyrus",15),textvariable=c ,bd=5,relief=GROOVE)
        e3.place(x=350,y=350)
        e4=Entry(root1,font=("papyrus",15),textvariable=d ,bd=5,relief=GROOVE)
        e4.place(x=350,y=450)
        e5=Entry(root1,font=("papyrus",15),textvariable=e ,bd=5,relief=GROOVE)
        e5.place(x=350,y=550)

        b1=Button(root1,text="Sumit",font=("papyrus",10),bd=6,command=Sumit)
        b1.place(x=300,y=610)
        b1.bind("<Enter>",E)
        b1.bind("<Leave>",F)
        b2=Button(root1,text="Back",font=("papyrus",10),bd=6,command=Back)
        b2.place(x=400,y=610)
        b2.bind("<Enter>",E1)
        b2.bind("<Leave>",F1)
        b3=Button(root1,text="Reset",font=("papyrus",10),bd=6,command=Reset)
        b3.place(x=500,y=610)
        b3.bind("<Enter>",E2)
        b3.bind("<Leave>",F2)
        b4=Button(root1,text="Exit",font=("papyrus",10),bd=6,command=Exit)
        b4.place(x=600,y=610)
        b4.bind("<Enter>",E3)
        b4.bind("<Leave>",F3)
        b5=Button(root1,text="Display resistries",font=("papyrus",10),command=show,bd=6)
        b5.place(x=950,y=100)
        b5.bind("<Enter>",E4)
        b5.bind("<Leave>",F4)

        z= Text(height=30,width=80,font=("calibri light",10),bd=7,relief=GROOVE)
        z.place(x=750,y=140)
        

        root1.mainloop()
        
    else:
        messagebox.showinfo("sign_in","Sign in is not successfully")

def E(event):
    b1.config(bg="grey",fg="white")

def F(event):
    b1.config(bg="white",fg="black")

def E1(event):
    b2.config(bg="grey",fg="white")

def F1(event):
    b2.config(bg="white",fg="black")

def E2(event):
    b3.config(bg="grey",fg="white")

def F2(event):
    b3.config(bg="white",fg="black")
    
def E3(event):
    b4.config(bg="grey",fg="white")

def F3(event):
    b4.config(bg="white",fg="black")

def E4(event):
    b5.config(bg="grey",fg="white")

def F4(event):
    b5.config(bg="white",fg="black")

def E5(event):
    b6.config(bg="grey",fg="white")

def F5(event):
    b6.config(bg="white",fg="black")

def Forgot_pass():
    root.destroy()
    root2=Tk()
    root2.geometry("1350x700+0+0")
    root2.title("Details of Game registery.")
    root2.configure(background="black")

    def E(event):
        b1.config(bg="grey",fg="white")

    def F(event):
        b1.config(bg="white",fg="black")

    def E1(event):
        b2.config(bg="grey",fg="white")
    
    def F1(event):
        b2.config(bg="white",fg="black")

    def E2(event):
        b3.config(bg="grey",fg="white")

    def F2(event):
        b3.config(bg="white",fg="black")
    
    def E3(event):
        b4.config(bg="grey",fg="white")

    def F3(event):
        b4.config(bg="white",fg="black")

    bg_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\A1Y5u83elyS.png")
    user_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\icons8-cloud-account-login-male-100.png")
    id_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\icons8-login-as-user-24.png")
    pass_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\icons8-login-as-user-16.png")

    p =StringVar()
    pas =StringVar()

    def Next():

        name=p.get()
        user_name=pas.get()
        import mysql.connector

        conn=m.connect(host='localhost',user='root',database='game_resistery',password='rkch172002')
        cur=conn.cursor()
        cur.execute("select name from new_account")
        result=cur.fetchall()
        pr=str(result)
        

        conn1=m.connect(host='localhost',user='root',database='game_resistery',password='rkch172002')
        cur1=conn1.cursor()
        cur1.execute("select user_name from new_account")
        result1=cur1.fetchall()
        pa=str(result1)

        
        if(name ==''  and user_name ==''):
            messagebox.showinfo("Sign_in","ALL FIELDS ARE REQUIRED.")

        elif(name ==''  or  user_name ==''):
            messagebox.showinfo("Sign_in","ALL FIELDS ARE REQUIRED.")

        elif((name in pr) and (user_name in pa)):
            messagebox.showinfo("Sign_in","Sign_in is successfully")
            root2.destroy()
            
            root1=Tk()
            root1.geometry("1350x700+0+0")
            root1.title("Details of Game registery.")
            root1.configure(background="black")

            def E(event):
                b1.config(bg="grey",fg="white")

            def F(event):
                b1.config(bg="white",fg="black")

            def E1(event):
                b2.config(bg="grey",fg="white")

            def F1(event):
                b2.config(bg="white",fg="black")

            def E2(event):
                b3.config(bg="grey",fg="white")

            def F2(event):
                b3.config(bg="white",fg="black")
                
            def E3(event):
                b4.config(bg="grey",fg="white")

            def F3(event):
                b4.config(bg="white",fg="black")

            def E4(event):
                b5.config(bg="grey",fg="white")
            bg_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\A1Y5u83elyS.png")

            def F4(event):
                b5.config(bg="white",fg="black")

            a=IntVar()
            b=StringVar()
            c=StringVar()
            d=StringVar()
            e=IntVar()
            a.set("1")
            b.set("GOD OF WAR")
            c.set("Santa Monica Stu.")
            d.set("KRATOS")
            e.set("DATE")


            def Sumit():
                import mysql.connector
                conn = m.connect(host='localhost', user ='root', database='game_resistery', password='rkch172002')
                cur = conn.cursor()
                serial_no = a.get()
                name_of_game = b.get()
                created_by = c.get()
                main_charector = d.get()
                date_of_release = e.get()
                sq="insert into game_info values({}, '{}', '{}', '{}', {})".format( serial_no , name_of_game , created_by , main_charector , date_of_release)
                cur.execute(sq)
                conn.commit()
                messagebox.showinfo("Data","Our data is saved successfully")
                print("data is saved successfully...........")
                conn.close()
            def Back():
                messagebox.showinfo("SORRY!!!!","Not WORKING PROPERLY........")

            def Reset():
                messagebox.showinfo("Reset","Want To Reset.")
                a.set("")
                b.set("")
                c.set("")
                d.set("")
                e.set("")

            def Exit():
                messagebox.showinfo("Exit","Are you sure")
                root1.destroy()
                 
            def show():
                z.delete(0.0,END)
                conn=m.connect(host='localhost',user='root',database='game_resistery',password='rkch172002')
                cur=conn.cursor()
                cur.execute("select * from game_info")
                r=cur.fetchall()
                z.insert(END, "serial_no"+'\t\t'+"name_of_game"+'\t\t'+"created_by"+'\t\t'+"main_charector"+'\t\t'+"date_of_release"+'\n')
                z.insert(END,"\n","     ")
                for i in r:
                    for j in i:
                        z.insert(END,str(j) +'\t\t')
                    z.insert(END, "\n")
                z.config(state="disabled")

            L0=Label(root1,image=bg_photo)
            L0.pack()
            L1=Label(root1, text="GAME REGISTERY",font=("National Cartoon",30, "bold","underline"),fg="white",bg="black",bd=10,relief=GROOVE)
            L1.place(x=0,y=0,relwidth=1)
            L2=Label(root1, text="Serial no.",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
            L2.place(x=40,y=150)
            L3=Label(root1, text="Name of Game",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
            L3.place(x=40,y=250)
            L4=Label(root1, text="Created by",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
            L4.place(x=40,y=350)
            L5=Label(root1, text="Main charector",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
            L5.place(x=40,y=450)
            L6=Label(root1, text="Date of Release",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
            L6.place(x=40,y=550)
            L7=Label(root1, text="Please DONOT enter any space or any symbole b/w the date.",font=("mv boli",7,"underline"),fg="white",bg="black")
            L7.place(x=40,y=590)

            e1=Entry(root1,font=("papyrus",15),textvariable=a ,bd=5,relief=GROOVE)
            e1.place(x=350,y=150)
            e2=Entry(root1,font=("papyrus",15),textvariable=b ,bd=5,relief=GROOVE)
            e2.place(x=350,y=250)
            e3=Entry(root1,font=("papyrus",15),textvariable=c ,bd=5,relief=GROOVE)
            e3.place(x=350,y=350)
            e4=Entry(root1,font=("papyrus",15),textvariable=d ,bd=5,relief=GROOVE)
            e4.place(x=350,y=450)
            e5=Entry(root1,font=("papyrus",15),textvariable=e ,bd=5,relief=GROOVE)
            e5.place(x=350,y=550)

            b1=Button(root1,text="Sumit",font=("papyrus",10),bd=6,command=Sumit)
            b1.place(x=300,y=610)
            b1.bind("<Enter>",E)
            b1.bind("<Leave>",F)
            b2=Button(root1,text="Back",font=("papyrus",10),bd=6,command=Back)
            b2.place(x=400,y=610)
            b2.bind("<Enter>",E1)
            b2.bind("<Leave>",F1)
            b3=Button(root1,text="Reset",font=("papyrus",10),bd=6,command=Reset)
            b3.place(x=500,y=610)
            b3.bind("<Enter>",E2)
            b3.bind("<Leave>",F2)
            b4=Button(root1,text="Exit",font=("papyrus",10),bd=6,command=Exit)
            b4.place(x=600,y=610)
            b4.bind("<Enter>",E3)
            b4.bind("<Leave>",F3)
            b5=Button(root1,text="Display resistries",font=("papyrus",10),command=show,bd=6)
            b5.place(x=950,y=100)
            b5.bind("<Enter>",E4)
            b5.bind("<Leave>",F4)

            z= Text(height=30,width=80,font=("calibri light",10),bd=7,relief=GROOVE)
            z.place(x=750,y=140)

            root1.mainloop()
   
        else:
            messagebox.showinfo("Incorrect","Username is incorrect.")

    def Previous():
        messagebox.showinfo("SORRY!!!!","Not WORKING PROPERLY........")
    
    def Reset():
        messagebox.showinfo("Reset","Want To Reset.")
        p.set("")
        pas.set("")

    def Exit():
        messagebox.showinfo("Exit","Are you sure")
        root2.destroy()

    L0=Label(root2,image=bg_photo)
    L0.pack()
    L1=Label(root2,text="GAME REGISTERY",font=("National Cartoon",30,"underline"),bg="black",fg="white",bd=10,relief=GROOVE)
    L1.place(x=0,y=0,relwidth=1)
    login_frame=Frame(root2,bg="white")
    login_frame.place(x=540,y=100)
    L2=Label(login_frame,image=user_photo,bg="white",fg="black")
    L2.grid(row=0,columnspan=3,pady=20)
    L3=Label(login_frame,text="Name",image=id_photo,compound=LEFT,font=("Times New Roman",15,"underline"),bg="white",fg="black")
    L3.grid(row=1,column=0,pady=20)
    L4=Label(login_frame,text="Pre User Name",image=pass_photo,compound=LEFT,font=("Times New Roman",15,"underline"),bg="white",fg="black")
    L4.grid(row=2,column=0,padx=20,pady=10)

    e1=Entry(login_frame,font=("papyrus",10),textvariable=p ,bd=5,relief=GROOVE)
    e1.grid(row=1,column=2,padx=20,pady=10)
    e2=Entry(login_frame,font=("papyrus",10),textvariable=pas ,bd=5,relief=GROOVE,show='*')
    e2.grid(row=2,column=2,padx=20,pady=10)

    b1=Button(login_frame,text="Next",font=("papyrus",10),bd=6,command=Next)
    b1.grid(row=3,column=0,padx=20,pady=10)
    b1.bind("<Enter>",E)
    b1.bind("<Leave>",F)
    b2=Button(login_frame,text="Previous",font=("papyrus",10),bd=6,command=Previous)
    b2.grid(row=3,column=2,padx=20,pady=10)
    b2.bind("<Enter>",E1)
    b2.bind("<Leave>",F1)
    b3=Button(root2,text="Reset",font=("papyrus",10),bd=6,command=Reset)
    b3.place(x=602,y=450)
    b3.bind("<Enter>",E2)
    b3.bind("<Leave>",F2)
    b4=Button(root2,text="Exit",font=("papyrus",10),bd=6,command=Exit)
    b4.place(x=795,y=450)
    b4.bind("<Enter>",E3)
    b4.bind("<Leave>",F3)

    root2.mainloop()

def sign_up():
    messagebox.showinfo("Sign Up","Are you want to sign_up.")
    root.destroy()

    root3=Tk()
    root3.geometry("1350x700+0+0")
    root3.title("Details of Game registery.")
    root3.configure(background="black")

    a=StringVar()
    b=StringVar()
    us=StringVar()
    crpass=IntVar()
    copass=IntVar()
    z=StringVar()

    a.set("Chetan")
    b.set("Singh")
    us.set("Rkch")
    crpass.set("*********")
    copass.set("Conform Password")

    

    def E(event):
        b1.config(bg="grey",fg="white")

    def F(event):
        b1.config(bg="white",fg="black")

    def E1(event):
        b2.config(bg="grey",fg="white")

    def F1(event):
        b2.config(bg="white",fg="black")

    def E2(event):
        b3.config(bg="grey",fg="white")

    def F2(event):
        b3.config(bg="white",fg="black")
    
    def E3(event):
        b4.config(bg="grey",fg="white")

    def F3(event):
        b4.config(bg="white",fg="black")

    def E4(event):
        b5.config(bg="grey",fg="white")

    def F4(event):
        b5.config(bg="white",fg="black")

    def sign_up1():
        import mysql.connector
        conn = m.connect(host='localhost', user ='root', database='game_resistery', password='rkch172002')
        cur = conn.cursor()
        name = a.get()
        last_name = b.get()
        username = us.get()
        create_password = crpass.get()
        conform_password = copass.get()
        if(create_password == conform_password):
            sq="insert into new_account values('{}', '{}', '{}', {}, {})".format( name , last_name , username , create_password , conform_password)
            cur.execute(sq)
            conn.commit()
            messagebox.showinfo("sign up","sign up successfully")
            conn.close()
        
        else:
            messagebox.showinfo("ERROR","Please enter password correctly")

    def Back():
        messagebox.showinfo("SORRY!!!!","Not WORKING PROPERLY........")

    def Reset():
        messagebox.showinfo("Reset","Want To Reset.")
        a.set("")
        b.set("")
        us.set("")
        crpass.set("")
        copass.set("")

    def Exit():
        messagebox.showinfo("Exit","Are you sure")
        root3.destroy()
    bg_photo=PhotoImage(file="F:\\pythongui\\final pro1\\photos\\A1Y5u83elyS.png")

    def show():
        z.delete(0.0,END)
        conn=m.connect(host='localhost',user='root',database='game_resistery',password='rkch172002')
        cur=conn.cursor()
        cur.execute("select name,last_name,user_name from new_account")
        r=cur.fetchall()
        z.insert(END, "NAME"+'\t\t'+"LAST NAME"+'\t\t'+"USER NAME"+'\n')
        z.insert(END,"\n","     ")
        for i in r:
            for j in i:
                z.insert(END,str(j) +'\t\t')
            z.insert(END, "\n")
        z.config(state="disabled")


    L0=Label(root3,image=bg_photo)
    L0.pack()
    L1=Label(root3, text="GAME REGISTERY",font=("National Cartoon",30, "bold","underline"),fg="white",bg="black",bd=10,relief=GROOVE)
    L1.place(x=0,y=0,relwidth=1)
    L2=Label(root3, text="Name",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
    L2.place(x=40,y=150)
    L3=Label(root3, text="Last Name",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
    L3.place(x=40,y=250)
    L4=Label(root3, text="User Name",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
    L4.place(x=40,y=350)
    L5=Label(root3, text="Create Password",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
    L5.place(x=40,y=450)
    L6=Label(root3, text="Conform Password",font=("Planet Kosmos",15, "bold","underline"),fg="black",bg="#F5F5F5")
    L6.place(x=40,y=550)

    e1=Entry(root3,font=("papyrus",15),textvariable=a ,bd=5,relief=GROOVE)
    e1.place(x=350,y=150)
    e2=Entry(root3,font=("papyrus",15),textvariable=b ,bd=5,relief=GROOVE)
    e2.place(x=350,y=250)
    e3=Entry(root3,font=("papyrus",15),textvariable=us ,bd=5,relief=GROOVE)
    e3.place(x=350,y=350)
    e4=Entry(root3,font=("papyrus",15),textvariable=crpass ,bd=5,relief=GROOVE,show='*')
    e4.place(x=350,y=450)
    e5=Entry(root3,font=("papyrus",15),textvariable=copass ,bd=5,relief=GROOVE)
    e5.place(x=350,y=550)

    b1=Button(root3,text="Sign up",font=("papyrus",10),bd=6,command=sign_up1)
    b1.place(x=300,y=610)
    b1.bind("<Enter>",E)
    b1.bind("<Leave>",F)
    b2=Button(root3,text="Back",font=("papyrus",10),bd=6,command=Back)
    b2.place(x=400,y=610)
    b2.bind("<Enter>",E)
    b2.bind("<Leave>",F1)
    b3=Button(root3,text="Reset",font=("papyrus",10),bd=6,command=Reset)
    b3.place(x=500,y=610)
    b3.bind("<Enter>",E2)
    b3.bind("<Leave>",F2)
    b4=Button(root3,text="Exit",font=("papyrus",10),bd=6, command=Exit)
    b4.place(x=600,y=610)
    b4.bind("<Enter>",E3)
    b4.bind("<Leave>",F3)
    bg_photo1=PhotoImage(file="photos\A1Y5u83elyS.png")
    b5=Button(root3,text="Dislay Pre Entry",font=("papyrus",10),bd=6, command=show)
    b5.place(x=1020,y=100)
    b5.bind("<Enter>",E4)
    b5.bind("<Leave>",F4)

    z= Text(height=30,width=50,font=("calibri light",10),bd=7,relief=GROOVE)
    z.place(x=900,y=140)

    root3.mainloop()

def Disc():
    root.destroy()
    root4=Tk()
    root4.geometry("1350x700+0+0")
    root4.title("Details of Game registery.")

    L0=Label(root4,image=bg_photo1)
    L0.pack()

    L1=Label(root4, text="GAME REGISTERY",font=("National Cartoon",30, "bold","underline"),fg="white",bg="black",bd=10,relief=GROOVE)
    L1.place(x=0,y=0,relwidth=1)
    L2=Label(root4, text="A  Small  Try  By  Making  a  Small  Gameing  Database. ",font=("Zanzabar",20,"bold","underline"),fg="#00ff00",bg="#F5F5F5")
    L2.place(x=350,y=380)
    L3=Label(root4, text="thank you.....",font=("American Kestrel Straight Laser",25,"underline"),fg="#FF4500",bg="#F5F5F5")
    L3.place(x=600,y=480)
    L4=Label(root4, text="created by :-",font=("American Kestrel Straight Exp",20),fg="#DC143C",bg="#F5F5F5")
    L4.place(x=1000,y=540)
    L5=Label(root4, text="Rishee kumar and grp.",font=("American Kestrel Straight 3D",12,"underline"),fg="#000080",bg="#F5F5F5")
    L5.place(x=1100,y=590)
    L6=Label(root4, text=" B-TECH EE ",font=("American Kestrel Straight 3D",10,"underline"),fg="#000080",bg="#F5F5F5")
    L6.place(x=1180,y=630)

    root4.mainloop()

def Reset():
    messagebox.showinfo("Reset","Want To Reset.")
    a.set("")
    b.set("")

def Exit():
    messagebox.showinfo("Exit","Are you sure")
    root.destroy()


L0=Label(root,image=bg_photo)
L0.pack()
L1=Label(root,text="GAME REGISTERY",font=("National Cartoon",30,"underline"),bg="black",fg="white",bd=10,relief=GROOVE)
L1.place(x=0,y=0,relwidth=1)
login_frame=Frame(root,bg="white")
login_frame.place(x=520,y=100)
L2=Label(login_frame,image=user_photo,bg="white",fg="black")
L2.grid(row=0,columnspan=3,pady=20)
L3=Label(login_frame,text="USER NAME",image=id_photo,compound=LEFT,font=("Times New Roman",15),bg="white",fg="black")
L3.grid(row=1,column=0,pady=20)
L4=Label(login_frame,text="PASSWORD",image=pass_photo,compound=LEFT,font=("Times New Roman",15),fg="black",bg="white")
L4.grid(row=2,column=0,padx=20,pady=10)


e1=Entry(login_frame,font=("papyrus",10), textvariable= a,bd=5,relief=GROOVE)
e1.grid(row=1,column=1,padx=20,pady=10)
e2=Entry(login_frame,font=("papyrus",10), textvariable= b ,bd=5,relief=GROOVE,show='*')
e2.grid(row=2,column=1,padx=20,pady=10)

b1=Button(login_frame,text="Sign in",font=("papyrus",10),bd=6,command=sign_in)
b1.grid(row=3,column=1,padx=20,pady=10)
b1.bind("<Enter>",E)
b1.bind("<Leave>",F)
b2=Button(login_frame,text="Forgoten Password",font=("papyrus",10),bd=6,command=Forgot_pass)
b2.grid(row=3,column=0,padx=20,pady=10)
b2.bind("<Enter>",E1)
b2.bind("<Leave>",F1)
b3=Button(root,text="Reset",font=("papyrus",10),bd=6,command=Reset)
b3.place(x=583,y=440)
b3.bind("<Enter>",E2)
b3.bind("<Leave>",F2)
b4=Button(root,text="Exit",font=("papyrus",10),bd=6,command=Exit)
b4.place(x=920,y=440)
b4.bind("<Enter>",E3)
b4.bind("<Leave>",F3)
b5=Button(login_frame,text="Sign up",font=("papyrus",10),bd=6,command=sign_up)
b5.grid(row=3,column=2,padx=20,pady=10)
b5.bind("<Enter>",E4)
b5.bind("<Leave>",F4)
b6=Button(root,text="Discripstion",font=("papyrus",10),bd=6,command=Disc)
b6.place(x=749,y=440)
b6.bind("<Enter>",E5)
b6.bind("<Leave>",F5)

root.mainloop()
