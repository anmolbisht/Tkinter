from tkinter import *
from new_user import *
import mysql.connector
from tkinter.font import Font
from tkinter import messagebox
from Admin_Page import *
from User_Page import User_Page
mydb=mysql.connector.connect(host="localhost",user="root",
                             passwd="admin",
                             database="bookstore")
cur=mydb.cursor()        


class welcomepage:
    def __init__(self):
        top=self.top=Tk()
        top.title('BOOKSTORE')
        top.geometry("500x500+120+120")


        self.left=Frame(top,width=250,height=500,bg="lightpink").pack(side=LEFT)
        self.right=Frame(top,width=250,height=500,bg="lightblue").pack(side=RIGHT)



        Label(self.left,text="USER LOGIN",font=('arial 13'),bg="lightpink").place(x=50,y=10)
        Label(self.left,text="USER ID",bg="lightpink").place(x=20,y=60)
        Label(self.left,text="password",bg="lightpink").place(x=20,y=120)

        self.userid=StringVar()
        self.userpwd=StringVar()

        Entry(self.left,textvariable=self.userid,width=15).place(x=125,y=60)
        Entry(self.left,show='*',textvariable=self.userpwd,width=15).place(x=125,y=120)

        Button(self.left,text="LOGIN",command=self.user_login).place(x=110,y=150)
        
        Label(self.left,text="NEW USER",bg="lightpink").place(x=20,y=210)
        Button(self.left,text="new user",command=self.new_login).place(x=125,y=230)

        Label(self.right, text="ADMIN LOGIN", font=('arial 13'), bg='lightblue').place(x=290, y=10)
        Label(self.right, text="Admin ID", bg='lightblue').place(x=260, y=60)
        Label(self.right, text="Password", bg='lightblue').place(x=260, y=120)

        Button(self.right, text="LOGIN",command=self.admin_login).place(x=345, y=180)
        
        self.adminid=StringVar()
        self.adminpwd=StringVar()
        Entry(self.right, textvariable=self.adminid, width=15).place(x=360, y=60)
        Entry(self.right,show='*', textvariable=self.adminpwd, width=15).place(x=360, y=120)
        top.mainloop()

    def admin_login(self):
        if self.adminid.get()=='admin' and self.adminpwd.get()=="Anmol":
            self.stop()
            m=Admin_Page()
            m.start()
        else:
            messagebox.showerror('Error',"Invalid admin name or password")
                
    def stop(self):
        self.top.destroy()
    def user_login(self):
        statement="select * from user where user_id=%s and pwd=%s"
        cur.execute(statement,(self.userid.get(),self.userpwd.get()))
        a=cur.fetchall()
        if len(a)==0:
            messagebox.showerror("Error","Invalid user name or password")
        else:
            self.stop()
            g=User_Page()
            g.start(self.userid.get())
    def new_login(self):
        self.stop()
        a=new_user()
        a.start()
   
welcomepage()
