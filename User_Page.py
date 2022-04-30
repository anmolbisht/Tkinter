from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import welcomepage
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",
                             passwd="admin",
                             database="bookstore")
cur=mydb.cursor()

class User_Page:
    def start(self,userid):
        arr=0
        key,name,address,mobile,password=0,0,0,0,0
        top=self.top=Tk()
        self.user=userid
        top.geometry("500x400+120+120")
        self.frame=Frame(top,bg="lightgreen",width=500,height=400).pack()
        self.id=StringVar()

        statement="select * from user where user_id= '" +userid+"' "
        cur.execute(statement)
        arr=cur.fetchall()
        (key,name,address,mobile,password)=arr[0]
        
        Label(self.frame,text='USER DETAILS',bg="lightgreen",font=('arial 13'), fg='Black').place(x=75,y=50)
        Label(self.frame, text='User_Id',bg="lightgreen", font=('arial 10'), fg='Black').place(x=50, y=100)
        Label(self.frame, text='Name',bg="lightgreen", font=('arial 10'), fg='Black').place(x=50, y=150)
        Label(self.frame, text='Address',bg="lightgreen", font=('arial 10'), fg='Black').place(x=50, y=200)
        Label(self.frame, text='Mobile no.',bg="lightgreen", font=('arial 10'), fg='Black').place(x=50, y=250)

        Label(self.frame, text=key, font=('arial 12'), fg='Black',bg="lightgreen").place(x=150, y=100)
        Label(self.frame, text=name, font=('arial 12'), fg='Black',bg="lightgreen").place(x=150, y=150)
        Label(self.frame, text=address, font=('arial 12'), fg='Black',bg="lightgreen").place(x=150, y=200)
        Label(self.frame,text=mobile, font=('arial 12'), fg='Black',bg="lightgreen").place(x=150,y=250)

        Button(self.frame,text="logout",width=8,command=self.logout).place(x=150,y=300)
    def logout(self):
        self.top.destroy()
        x=welcomepage.welcomepage()

        
                
