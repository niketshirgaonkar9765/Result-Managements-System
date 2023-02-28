from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import re
class StudentClass:
    def __init__(self,root): 
        self.root=root
        self.root.title("Students Result Managemnt System")
        self.root.geometry("1200x480+150+150")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.resizable(False,False)
        
        #====title=====
        title=Label(self.root,text="Manage Student Details",padx=10,compound=LEFT,font=("callibri",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)
        
        #=====Variables=====
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        
        
        #=====widgets=====
        lbl_roll=Label(self.root,text="Roll No.:",font=("callibri",15,'bold'),bg='white').place(x=10,y=60)
        lbl_name=Label(self.root,text="Name:",font=("callibri",15,'bold'),bg='white').place(x=10,y=100)
        lbl_email=Label(self.root,text="Email ID:",font=("callibri",15,'bold'),bg='white').place(x=10,y=140)
        lbl_gender=Label(self.root,text="Gender:",font=("callibri",15,'bold'),bg='white').place(x=10,y=180)
        lbl_state=Label(self.root,text="State:",font=("callibri",15,'bold'),bg='white').place(x=10,y=220)
        lbl_address=Label(self.root,text="Address:",font=("callibri",15,'bold'),bg='white').place(x=10,y=260)
        lbl_dob=Label(self.root,text="D.O.B.:",font=("callibri",15,'bold'),bg='white').place(x=360,y=60)
        lbl_contact=Label(self.root,text="Contact:",font=("callibri",15,'bold'),bg='white').place(x=360,y=100)
        lbl_addmission=Label(self.root,text="Addmission:",font=("callibri",15,'bold'),bg='white').place(x=360,y=140)
        lbl_course=Label(self.root,text="Course:",font=("callibri",15,'bold'),bg='white').place(x=360,y=180)
        lbl_city=Label(self.root,text="City:",font=("callibri",15,'bold'),bg='white').place(x=270,y=220)
        lbl_pin=Label(self.root,text="Pincode:",font=("callibri",15,'bold'),bg='white').place(x=480,y=220)
        
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("callibri",15),bg='lightyellow')
        self.txt_roll.place(x=110,y=60,width=200)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=("callibri",15),bg='lightyellow')
        self.txt_name.place(x=110,y=100,width=230)
        self.txt_email=Entry(self.root,textvariable=self.var_email,font=("callibri",15),bg='lightyellow')
        self.txt_email.place(x=110,y=140,width=230)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Male","Female","Other"),font=("callibri",15),state='readonly',justify=CENTER)
        self.txt_gender.place(x=110,y=180,width=150)
        self.txt_gender.set("Select Gender")
        self.txt_state=ttk.Combobox(self.root,textvariable=self.var_state,values=("Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujrat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"),font=("callibri",15),state='readonly',justify=CENTER)
        self.txt_state.place(x=110,y=220,width=150)
        self.txt_state.set("Select State")
        self.txt_city=Entry(self.root,textvariable=self.var_city,font=("callibri",15),bg='lightyellow')
        self.txt_city.place(x=320,y=220,width=150)
        self.txt_pin=Entry(self.root,textvariable=self.var_pin,font=("callibri",15),bg='lightyellow')
        self.txt_pin.place(x=580,y=220,width=100)
        
        self.txt_dob=Entry(self.root,textvariable=self.var_dob,font=("callibri",15),bg='lightyellow')
        self.txt_dob.place(x=480,y=60,width=200)
        self.txt_contact=Entry(self.root,textvariable=self.var_contact,font=("callibri",15),bg='lightyellow')
        self.txt_contact.place(x=480,y=100,width=200)
        self.txt_addmission=Entry(self.root,textvariable=self.var_a_date,font=("callibri",15),bg='lightyellow')
        self.txt_addmission.place(x=480,y=140,width=200)
        self.txt_addmission=Entry(self.root,textvariable=self.var_a_date,font=("callibri",15),bg='lightyellow')
        self.txt_addmission.place(x=480,y=140,width=200)
        
        self.course_list=[]
        #function call to update list
        self.fetch_course()
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("callibri",15),state='readonly',justify=CENTER)
        self.txt_course.place(x=480,y=180,width=200)
        self.txt_course.set("Select Course")
        
        self.txt_address=Text(self.root,font=("callibri",15),bg='lightyellow')
        self.txt_address.place(x=110,y=260,width=565,height=100)
        
        
        #=====Buttons=====
        self.btn_add=Button(self.root,text="Save",font=("callibri",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="Update",font=("callibri",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="Delete",font=("callibri",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="Clear",font=("callibri",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)
        
        #=====Search Panel======
        self.var_search=StringVar()
        lbl_search_roll=Label(self.root,text="Roll No.:",font=("callibri",15,'bold'),bg='white').place(x=720,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("callibri",15),bg='lightyellow')
        txt_search_roll.place(x=870,y=60,width=180)
        
        btn_search=Button(self.root,text="Search",font=("callibri",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        btn_search.place(x=1070,y=60,width=120,height=28)
        
        #=====content=====
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)
        
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","email","gender","dob","contact","addmission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.heading("roll",text="Roll No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email ID")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B.")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("addmission",text="Addmission Date")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="Pincode")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]='headings'
        
        self.CourseTable.column("roll",width=60)
        self.CourseTable.column("name",width=180)
        self.CourseTable.column("email",width=180)
        self.CourseTable.column("gender",width=60)
        self.CourseTable.column("dob",width=80)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("addmission",width=80)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=80)
        self.CourseTable.column("address",width=200)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        
#===========================================================================
   
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select Course"),
        self.var_state.set("Select State"),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
        
    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required!",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select student from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
        
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])
        #print(row)
        '''self.var_roll.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        #self.var_course.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])'''
        
        
    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required!",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll Number already exist!",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,addmission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Student added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll Number should be required!",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,addmission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success","Student updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
            
    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            row=cur.fetchall()
            if len(row)>0:
                for row in row:
                    self.course_list.append(row[0])
            #print(v)                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            row=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in row:
                self.CourseTable.insert('',END,values=row)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
            
            
            
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    