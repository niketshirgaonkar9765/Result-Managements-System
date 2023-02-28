from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox
import sqlite3
import os

class RMS:
    def __init__(self,root): 
        self.root=root
        self.root.title("Students Result Management System | DEVELOPED BY NIKET")
        self.root.geometry("1910x1070+-6+-10")
        self.root.config(bg="white")
        
#====images=====   
        #self.logo_dash=ImageTk.PhotoImage(file="images/srmnew.png")
        
#====title=====
        title=Label(self.root,text="Sant Rawool Maharaj Mahavidyalay, Kudal\nStudents Result Management System",font=("callibri",30,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=100)
        
        '''r=PhotoImage(file="images/srmnew.png")
        lbl=Label(self.root,height="80",width="70",image=r)
        lbl.place(x=5,y=5)'''
        
        self.bg=ImageTk.PhotoImage(file="images/srmnew.png")
        bg=Label(self.root,image=self.bg).place(x=5,y=5,heigh=90)
#====menus=====
        M_frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_frame.place(x=10,y=100,width=1520,height=80)
        
#====Button====
        btn_course=Button(M_frame,text="Course",font=("callibri",18,"bold"),bg="#0b5377",fg="white",activebackground="blue",cursor="hand2",command=self.add_course).place(x=25,y=5,width=210,height=40)
        btn_student=Button(M_frame,text="Student",font=("callibri",18,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=270,y=5,width=210,height=40)
        btn_result=Button(M_frame,text="Result",font=("gcallibri",18,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=515,y=5,width=210,height=40)
        btn_view=Button(M_frame,text="View Student Result",font=("callibri",18,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=760,y=5,width=240,height=40)
        btn_logout=Button(M_frame,text="Logout",font=("callibri",18,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=1035,y=5,width=210,height=40)
        btn_exit=Button(M_frame,text="Exit",font=("callibri",18,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1280,y=5,width=210,height=40)
    
#=====content window=====
        self.bg_img=Image.open("images/bg1.jpeg")
        self.bg_img=self.bg_img.resize((900,450),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=550,y=210,width=900,height=450)
        
#=====update details======
        self.lbl_course=Label(self.root,text="Total Courses\n0",font=("callibri",20,"bold"),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=550,y=680,width=300,height=100)
        
        self.lbl_student=Label(self.root,text="Total Students\n0",font=("callibri",20,"bold"),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=860,y=680,width=300,height=100)
        
        self.lbl_result=Label(self.root,text="Total Results\n0",font=("callibri",20,"bold"),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1170,y=680,width=300,height=100)
     
#====footer=====
        footer=Label(self.root,text="Students Result Management System\nContact us for any technical issues: shirgaonkarniket14@gmail.com",font=("callibri",12,"bold"),bg="#262626",fg="white").pack(side=BOTTOM,fill=X) 
    
        self.update1()
        
        
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
        
        
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
        
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ResultClass(self.new_win)
        
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ReportClass(self.new_win)
        
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
            
    def exit_(self):
        oj=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if oj==True:
            self.root.destroy()


            
            
    def update1(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n{str(len(cr))}")  
            
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n{str(len(cr))}")
            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n{str(len(cr))}")
            
            self.lbl_course.after(10,self.update1)
            
                          
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
            
     
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
