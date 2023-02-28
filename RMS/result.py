from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class ResultClass:
    def __init__(self,root): 
        self.root=root
        self.root.title("Students Result Managemnt System")
        self.root.geometry("1200x480+150+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)
        
        #====title=====
        title=Label(self.root,text="Add Student Result",padx=10,compound=LEFT,font=("callibri",25,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)
        
        #======variables=====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        
        #=====labels======
        lbl_select=Label(self.root,text="Select student:",font=("callibri",16,'bold'),bg='white').place(x=50,y=100)
        lbl_name=Label(self.root,text="Name.:",font=("callibri",16,'bold'),bg='white').place(x=50,y=160)
        lbl_course=Label(self.root,text="Course:",font=("callibri",16,'bold'),bg='white').place(x=50,y=220)
        lbl_marks=Label(self.root,text="Marks Obtained:",font=("callibri",16,'bold'),bg='white').place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks:",font=("callibri",16,'bold'),bg='white').place(x=50,y=340)
        
        #=====Entries======
        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("callibri",16),state='readonly',justify=CENTER)
        self.txt_student.place(x=260,y=100,width=150)
        self.txt_student.set("Select")
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("callibri",16),bg='lightyellow',state='readonly')
        self.txt_name.place(x=260,y=160,width=280)
        self.txt_course=Entry(self.root,textvariable=self.var_course,font=("callibri",16),bg='lightyellow',state='readonly')
        self.txt_course.place(x=260,y=220,width=280)
        self.txt_marks=Entry(self.root,textvariable=self.var_marks,font=("callibri",16),bg='lightyellow')
        self.txt_marks.place(x=260,y=280,width=280)
        self.txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("callibri",16),bg='lightyellow')
        self.txt_full_marks.place(x=260,y=340,width=280)
        
        #=====Buttons=====
        self.btn_search=Button(self.root,text="Search",font=("callibri",16,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        self.btn_search.place(x=430,y=100,width=110,height=28)
        
        self.btn_submit=Button(self.root,text="Submit",font=("callibri",16,"bold"),bg="lightgreen",activebackground="#03a9f4",cursor="hand2",command=self.add)
        self.btn_submit.place(x=300,y=420,width=110,height=35)
        self.btn_clear=Button(self.root,text="Clear",font=("callibri",16,"bold"),bg="lightgray",activebackground="#03a9f4",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=430,y=420,width=110,height=35)
        
        #=====image=====
        self.bg_img=Image.open("images/result.jpeg")
        self.bg_img=self.bg_img.resize((520,320),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=620,y=100)
        
        #=====functions======
    def fetch_roll(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            row=cur.fetchall()
            if len(row)>0:
                for row in row:
                    self.roll_list.append(row[0])
            #print(v)                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student records!",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already exist!",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result(roll,name,course,marks_0b,full_marks,per) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Result added Successfully",parent=self.root)
                   
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),
    
        
        
if __name__=="__main__":
    root=Tk()
    obj=ResultClass(root)
    root.mainloop()