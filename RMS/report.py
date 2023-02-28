from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class ReportClass:
    def __init__(self,root): 
        self.root=root
        self.root.title("Students Result Managemnt System")
        self.root.geometry("1200x480+150+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)
        
        #====title=====
        title=Label(self.root,text="View Student Results",padx=10,compound=LEFT,font=("callibri",25,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)
        
        #=====search======
        self.var_search=StringVar()
        self.var_id=""
        
        lbl_select=Label(self.root,text="Search by Roll No.:",font=("callibri",20,'bold'),bg='white').place(x=270,y=100)
        self.txt_search=Entry(self.root,textvariable=self.var_search,font=("callibri",20),bg='lightyellow')
        self.txt_search.place(x=530,y=100,width=150)
        
        self.btn_search=Button(self.root,text="Search",font=("callibri",16,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        self.btn_search.place(x=700,y=100,width=110,height=35)
        self.btn_clear=Button(self.root,text="Clear",font=("callibri",16,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=820,y=100,width=110,height=35)
        
        #=====result table=====
        lbl_roll=Label(self.root,text="Roll No.",font=("callibri",15),bg='white',bd=2,relief=GROOVE).place(x=80,y=230,width=100,height=50)
        lbl_name=Label(self.root,text="Name",font=("callibri",15),bg='white',bd=2,relief=GROOVE).place(x=180,y=230,width=340,height=50)
        lbl_course=Label(self.root,text="Course",font=("callibri",15),bg='white',bd=2,relief=GROOVE).place(x=520,y=230,width=150,height=50)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("callibri",15),bg='white',bd=2,relief=GROOVE).place(x=670,y=230,width=150,height=50)
        lbl_full=Label(self.root,text="Total Marks",font=("callibri",15),bg='white',bd=2,relief=GROOVE).place(x=820,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("callibri",15),bg='white',bd=2,relief=GROOVE).place(x=970,y=230,width=150,height=50)
        
        self.lbl_roll=Label(self.root,font=("callibri",15),bg='white',bd=2,relief=GROOVE)
        self.lbl_roll.place(x=80,y=280,width=100,height=50)
        self.lbl_name=Label(self.root,font=("callibri",15),bg='white',bd=2,relief=GROOVE)
        self.lbl_name.place(x=180,y=280,width=340,height=50)
        self.lbl_course=Label(self.root,font=("callibri",15),bg='white',bd=2,relief=GROOVE)
        self.lbl_course.place(x=520,y=280,width=150,height=50)
        self.lbl_marks=Label(self.root,font=("callibri",15),bg='white',bd=2,relief=GROOVE)
        self.lbl_marks.place(x=670,y=280,width=150,height=50)
        self.lbl_full=Label(self.root,font=("callibri",15),bg='white',bd=2,relief=GROOVE)
        self.lbl_full.place(x=820,y=280,width=150,height=50)
        self.lbl_per=Label(self.root,font=("callibri",15),bg='white',bd=2,relief=GROOVE)
        self.lbl_per.place(x=970,y=280,width=150,height=50)
        
        self.btn_del=Button(self.root,text="Delete",font=("callibri",16,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete)
        self.btn_del.place(x=525,y=390,width=150,height=35)
        
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll Number should be required!",parent=self.root)
            else:               
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.lbl_roll.config(text=row[1])
                    self.lbl_name.config(text=row[2])
                    self.lbl_course.config(text=row[3])
                    self.lbl_marks.config(text=row[4])
                    self.lbl_full.config(text=row[5])
                    self.lbl_per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
    def clear(self):
        self.var_id=""
        self.lbl_roll.config(text="")
        self.lbl_name.config(text="")
        self.lbl_course.config(text="")
        self.lbl_marks.config(text="")
        self.lbl_full.config(text="")
        self.lbl_per.config(text="")
        self.var_search.set("")
        
        
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student result first",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
        
if __name__=="__main__":
    root=Tk()
    obj=ReportClass(root)
    root.mainloop()