import mysql.connector
from tkinter import *
from tkinter import messagebox
import random
import welcomepage
mydb=mysql.connector.connect(host="localhost",user="root",
                             passwd="admin",
                             database="bookstore")
cur=mydb.cursor()

class new_user:
    def start(self):
        top=self.top=Tk()
        top.geometry("600x600+120+120")
        self.frame=Frame(top,bg="lightblue",width=600,height=600).pack()

        self.name=StringVar()
        self.mobile=StringVar()
        self.address=StringVar()
        self.number=StringVar()
        self.pwd=StringVar()

        Label(self.frame,text="NEW USER",bg='lightblue',font=('arial 13')).place(x=50,y=30)
        Label(self.frame,text="Name",bg='lightblue',font=('arial 10')).place(x=80,y=80)
        Label(self.frame,text="Mobile No.",bg='lightblue',font=('arial 10')).place(x=80,y=120)
        Label(self.frame,text="Password",bg='lightblue',font=('arial 10')).place(x=80,y=160)
        Label(self.frame,text="Address",bg='lightblue',font=('arial 10')).place(x=80,y=200)
        
        
        Entry(self.frame,textvariable=self.name).place(x=155,y=80)
        Entry(self.frame,textvariable=self.mobile).place(x=155,y=120)
        Entry(self.frame,show='*',textvariable=self.pwd).place(x=155,y=160)
        Entry(self.frame,textvariable=self.address).place(x=155,y=200)

        Button(self.frame, text="Add Data",command=self.insert,width=8,fg='green').place(x=140,y=250)
        Button(self.frame, text="New user",command=self.create_new,width=9).place(x=290,y=250)
        Button(self.frame, text="Back",command=self.back,width=6).place(x=500,y=500)
        top.mainloop()
    def create_new(self):
        self.stop()
        r=new_user()
        r.start()
        
    def back(self):
        self.stop()
        obj=welcomepage.welcomepage()

    def insert(self):
        self.userid=str(random.randint(10000,99999))
        suc='your user_id is %s'
        print(self.pwd.get())
        sqlformula="insert into user(user_id,name,address,phone,pwd) values(%s,%s,%s,%s,%s)"
        student1=[self.userid,self.name.get(),self.address.get(),self.mobile.get(),self.pwd.get()]
        cur.execute(sqlformula,student1)
        messagebox.showinfo("Success","your user_id is %s \n" %(self.userid))
        mydb.commit()
    def stop(self):
        self.top.destroy()
