from tkinter import *
import welcomepage
from tkinter import messagebox
import mysql.connector
from tkinter import Entry
mydb=mysql.connector.connect(host="localhost",user="root",
                             passwd="admin",
                             database="bookstore")
cur=mydb.cursor()        
class Help(Exception):
    pass
class Admin_Page:
    def start(self):
        top=self.top=Tk()
        top.configure(bg="#e3e3e3")
        top.geometry("600x600+120+120")
        top.resizable(False,False)

        self.left=Frame(top,width=600,height=720,bg="#e3e3e3").pack(side=LEFT)


        self.userid=StringVar()
        self.name=StringVar()
        self.phone=StringVar()
        self.pwd=StringVar()
        self.address=StringVar()

        Label(self.left,text="ADMINISTRATOR LOGIN",font=('arial 30 bold'),fg='Black',bg="#e3e3e3").place(x=40,y=5)

        Label(self.left, text="User ID", font=('arial 12'), fg='blue', bg='#e3e3e3').place(x=60,y=80)
        Entry(self.left,textvariable=self.userid,width=25).place(x=145,y=80)
        Button(self.left,text="search",width=6,command=self.searching).place(x=180,y=110)

        top.mainloop()

    def searching(self):
        self.input=[self.userid.get()]
        try:
            sql="select * from user where user_id=%s"
            cur.execute(sql,self.input)
            self.res=cur.fetchone()
            if(self.res is None):
                raise Help

            self.q=StringVar()
            self.w=StringVar()
            self.e=StringVar()
            self.r=StringVar()

            Label(self.left, text="User_id", font=('arial 10'), fg='black', bg='#e3e3e3').place(x=60,y=150)
            self.ent1=Entry(self.left,textvariable=self.r,width=25).place(x=145,y=150)
            self.r.set(self.res[0])

            Label(self.left, text="Name", font=('arial 10'), fg='black', bg='#e3e3e3').place(x=60,y=180)
            self.ent2=Entry(self.left,textvariable=self.q,width=25).place(x=145,y=180)
            self.q.set(self.res[1])


            Label(self.left, text="Address", font=('arial 10'), fg='black', bg='#e3e3e3').place(x=60,y=210)
            self.ent3=Entry(self.left,textvariable=self.w,width=25).place(x=145,y=210)
            self.w.set(self.res[2])

            Label(self.left, text="Phone NO.", font=('arial 10'), fg='black', bg='#e3e3e3').place(x=60,y=240)
            self.ent4=Entry(self.left,textvariable=self.e,width=25).place(x=145,y=240)
            self.e.set(self.res[3])


            Button(self.left,text="Update",width=6,fg="green",command=self.update).place(x=200,y=280)
            Button(self.left,text="Delete",width=6,fg="Red",command=self.delete).place(x=80,y=280)
            Button(self.left,text="logout",width=6,fg="blue",command=self.logout).place(x=520,y=280)
        except Help:
            messagebox.showerror("Invalid","User_id you entered is wrong")
            self.userid.set('')
    def update(self):
        query="update user set user_id=%s,name=%s,address=%s,phone=%s where user_id=%s"
        element=[self.r.get(),self.q.get(),self.w.get(),self.e.get(),self.userid.get()]
        cur.execute(query,element)
        mydb.commit()
        messagebox.showinfo("Success","Value update successfully")
        
    def logout(self):
        self.stop()
        a=welcomepage.welcomepage()
    def delete(self):
        query="delete from user where user_id=%s"
        cur.execute(query,self.input)
        mydb.commit()
        messagebox.showinfo("Success","Successfully deleted the row")
        self.stop()
        x=Admin_Page()
        x.start()

    def stop(self):
        self.top.destroy()
        
