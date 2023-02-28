from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os
#import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1080+-6+0")
        self.root.config(bg="white")
#======bg======        
        self.bg=ImageTk.PhotoImage(file="images/2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        
#=====login frame=====
        frame1=Frame(self.root,bg="white",borderwidth=5,relief="ridge")
        frame1.place(x=480,y=170,width=750,height=500)
        
        self.bg1=ImageTk.PhotoImage(file="images/3.jpg")
        bg=Label(self.root,image=self.bg1).place(x=290,y=235)
        
        title=Label(frame1,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="blue").place(x=190,y=50)
        
        fname=Label(frame1,text="EMAIL ADDRESS:",font=("callibri",20,"bold"),bg="white",fg="black").place(x=190,y=130)
        self.txt_email=Entry(frame1,font=("callibri",20),bg="lightgray")
        self.txt_email.place(x=190,y=170,width=400)
        
        fname=Label(frame1,text="PASSWORD:",font=("callibri",20,"bold"),bg="white",fg="black").place(x=190,y=240)
        self.txt_pass=Entry(frame1,font=("callibri",20),show="*",bg="lightgray")
        self.txt_pass.place(x=190,y=280,width=400)
        
        
        btn_reg=Button(frame1,text="Register new Account?",font=("callibri",16,"bold"),borderwidth=0,bg="white",fg="black",cursor="hand2",command=self.register_win)
        btn_reg.place(x=190,y=340)
        
        btn_forget=Button(frame1,text="Forget Password?",font=("callibri",16,"bold"),borderwidth=0,bg="white",fg="black",cursor="hand2",command=self.forget_pass)
        btn_forget.place(x=480,y=340)
        
        btn_login=Button(frame1,text="Login",font=("callibri",20,"bold"),bg="Green",fg="White",cursor="hand2",command=self.login)
        btn_login.place(x=190,y=400,width=150,height=40)
        
        
    def reset(self):
        self.sec.current(0)
        self.txt_newpass.delete(0,END)
        self.txt_ans.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_email.delete(0,END)
        
        
    def forget(self):
        if self.sec.get()=="Select Question" or self.txt_ans.get()=="" or self.txt_newpass.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.txt_email.get(),self.sec.get(),self.txt_ans.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select the correct security question / Enter Answer!",parent=self.root2)
                        
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_newpass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your Password has been reset, Please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
    
    def forget_pass(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password!",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","User not found!",parent=self.root)
                    
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Reset Password")
                    self.root2.geometry("560x450+450+150")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.config(bg="white")
                    
                    t=Label(self.root2,text="Reset Password",font=("callibri",20,"bold"),bg="white",fg="blue").place(x=0,y=10,relwidth=1)
                    
                    self.var_sec=StringVar()
                    self.sec=Label(self.root2,text="Security Question:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=50,y=80)
                    self.sec=ttk.Combobox(self.root2,textvariable=self.var_sec,values=("Email ID","Birth year","Any Word"),font=("callibri",15),state='readonly',justify=CENTER)
                    self.sec.place(x=50,y=120,width=400)
                    self.sec.set("Select Question")
                    
                    ans=Label(self.root2,text="Answer:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=50,y=180)
                    self.txt_ans=Entry(self.root2,font=("callibri",15),bg="lightgray")
                    self.txt_ans.place(x=50,y=220,width=400)
                    
                    passw=Label(self.root2,text="Set New Password:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=50,y=280)
                    self.txt_newpass=Entry(self.root2,font=("callibri",15),bg="lightgray")
                    self.txt_newpass.place(x=50,y=320,width=400)
                    
                    btn_changepass=Button(self.root2,text="Change Password",font=("callibri",15,"bold"),bg="Green",fg="White",cursor="hand2",command=self.forget)
                    btn_changepass.place(x=170,y=380,width=200,height=40)
                    
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
                        
        
    def register_win(self):
        self.root.destroy()
        import register
                    
                    
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password!",parent=self.root)
                    
                else:
                    messagebox.showinfo("Success",f"Welcome, {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")#import dashboard
                con.close()
                    
                    
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        
        
    
root=Tk()
obj=Register(root)
root.mainloop()
