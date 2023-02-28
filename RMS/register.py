from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1920x1080+-6+0")
        self.root.config(bg="white")
#======bg======        
        self.bg=ImageTk.PhotoImage(file="images/back.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
#=====register frame=====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=420,y=170,width=700,height=500)
        
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=50,y=30)
        
        fname=Label(frame1,text="First Name:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("callibri",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        lname=Label(frame1,text="Last Name:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=400,y=100)
        self.txt_lname=Entry(frame1,font=("callibri",15),bg="lightgray")
        self.txt_lname.place(x=400,y=130,width=250)
        
        contact=Label(frame1,text="Contact:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=50,y=175)
        self.txt_contact=Entry(frame1,font=("callibri",15),bg="lightgray")
        self.txt_contact.place(x=50,y=205,width=250)
        
        email=Label(frame1,text="Email ID:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=400,y=175)
        self.txt_email=Entry(frame1,font=("callibri",15),bg="lightgray")
        self.txt_email.place(x=400,y=205,width=250)
        
        self.var_sec=StringVar()
        self.sec=Label(frame1,text="Security Question:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=50,y=250)
        self.sec=ttk.Combobox(frame1,textvariable=self.var_sec,values=("Email ID","Birth year","Any Word"),font=("callibri",15),state='readonly',justify=CENTER)
        self.sec.place(x=50,y=280,width=250)
        self.sec.set("Select Question")
        
        ans=Label(frame1,text="Answer:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=400,y=250)
        self.txt_ans=Entry(frame1,font=("callibri",15),bg="lightgray")
        self.txt_ans.place(x=400,y=280,width=250)
        
        passw=Label(frame1,text="Password:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=50,y=325)
        self.txt_passw=Entry(frame1,font=("callibri",15),bg="lightgray",show="*")
        self.txt_passw.place(x=50,y=355,width=250)
        
        conpass=Label(frame1,text="Confirm Password:",font=("callibri",15,"bold"),bg="white",fg="black").place(x=400,y=325)
        self.txt_conpass=Entry(frame1,font=("callibri",15),bg="lightgray",show="*")
        self.txt_conpass.place(x=400,y=355,width=250)
        
        #=======================================================
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("callibri",11)).place(x=50,y=400)
        
        
        btn_reg=Button(frame1,text="Register",font=("callibri",16,"bold"),bg="green",fg="white",cursor="hand2",command=self.register_data)
        btn_reg.place(x=50,y=450,width=200,height=45)
        
        btn_sign=Button(self.root,text="Sign In",font=("callibri",16,"bold"),bg="blue",fg="white",cursor="hand2",command=self.sign_win)
        btn_sign.place(x=1300,y=30,width=200,height=45)
        
    def sign_win(self):
        self.root.destroy()
        os.system("python login.py")
        
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_ans.delete(0,END)
        self.txt_passw.delete(0,END)
        self.txt_conpass.delete(0,END)
        self.sec.current("Select Question")
        
    def register_data(self):
        if self.txt_fname.get()=="":
            messagebox.showerror("Error","First Name is required!",parent=self.root)
        elif self.txt_lname.get()=="":
            messagebox.showerror("Error","Last Name is required!",parent=self.root)
        elif self.txt_contact.get()=="":
            messagebox.showerror("Error","Contact Number is required!",parent=self.root)
        elif self.txt_email.get()=="":
            messagebox.showerror("Error","Email ID is required!",parent=self.root)
        elif self.sec.get()=="Select Question":
            messagebox.showerror("Error","Security question is required!",parent=self.root)
        elif self.txt_ans.get()=="":
            messagebox.showerror("Error","Answer is required!",parent=self.root)
        elif self.txt_passw.get()=="":
            messagebox.showerror("Error","Password is required!",parent=self.root)
        elif self.txt_conpass.get()=="":
            messagebox.showerror("Error","Please confirm your password!",parent=self.root)
        elif self.txt_passw.get()!=self.txt_conpass.get():
            messagebox.showerror("Error","Password and Confirm Password should be same!",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showinfo("Error","Please Agree our Terms & Conditions!",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showinfo("Error","User already exist, please try with another email ID",parent=self.root)
                else:               
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                                (
                                    self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.sec.get(),
                                    self.txt_ans.get(),
                                    self.txt_passw.get()
                                    )
                                
                                )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered Successfully!",parent=self.root)
                    self.clear()
                    self.sign_win()
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
          
    
root=Tk()
obj=Register(root)
root.mainloop()

