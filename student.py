from tkinter import *
from tkinter import ttk

# Pillow Library
from PIL import Image, ImageTk

# Import MessageBox
from tkinter import messagebox

# import MySql
import mysql.connector

import cv2


class Student:
    # constructor
    def __init__(self,root):  # root is for root window
        self.root=root
        # setting geometry
        self.root.geometry("1530x790+0+0")   # 1530x790 is window size, both 0 is the coordinate of x and y i.e. start window from top-left
        self.root.title("Student Details")

        # ========================= Variables ========================= 
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #### Setting Background Image
        # width of window is 1530, for 3 img width will be 510 per img
        # 1st image
        img1 = Image.open(r"D:\Deep Learning\Student Attendance System\images\student_01.jpg")
        img1=img1.resize((510,130),Image.ANTIALIAS)
        self.background1=ImageTk.PhotoImage(img1)
        bg1_label=Label(self.root,image=self.background1)
        bg1_label.place(x=0,y=0,width=525,height=130)
        # 2nd image
        img2 = Image.open(r"D:\Deep Learning\Student Attendance System\images\student_02.jpg")
        img2=img2.resize((510,130),Image.ANTIALIAS)
        self.background2=ImageTk.PhotoImage(img2)
        bg2_label=Label(self.root,image=self.background2)
        bg2_label.place(x=510,y=0,width=510,height=130)
        # 3rd image
        img3 = Image.open(r"D:\Deep Learning\Student Attendance System\images\student_03.jpg")
        img3=img3.resize((510,130),Image.ANTIALIAS)
        self.background3=ImageTk.PhotoImage(img3)
        bg3_label=Label(self.root,image=self.background3)
        bg3_label.place(x=1020,y=0,width=510,height=130)

        # bg image
        img_bg = Image.open(r"D:\Deep Learning\Student Attendance System\images\student_bg.jpg")
        img_bg=img_bg.resize((1530,710),Image.ANTIALIAS)
        self.background=ImageTk.PhotoImage(img_bg)
        bg_img=Label(self.root,image=self.background)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # title
        title_label=Label(bg_img,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_label.place(x=0,y=0,width=1530,height=45)


        ######  FRAME  #######
        main_frame=Frame(bg_img,bd=2,bg="white")  # bd - border
        main_frame.place(x=20,y=50,width=1480,height=600)

        # LEFT LABEL FRAME
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=('times new roman',12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=580)

        img_left_frame = Image.open(r"D:\Deep Learning\Student Attendance System\images\student_left.jpg")
        img_left_frame=img_left_frame.resize((750,130),Image.ANTIALIAS)
        self.img_left=ImageTk.PhotoImage(img_left_frame)
        img_left_top=Label(left_frame,image=self.img_left)
        img_left_top.place(x=5,y=0,width=750,height=130)

        # Current Course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information", font=('times new roman',12,"bold"))
        current_course_frame.place(x=5,y=130,width=745,height=115)

        # department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12),state="readonly")
        dep_combo["values"]=("--Select-Department--","Computer Science","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,stick=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12),state="readonly",width=20)
        course_combo["values"]=("--Select-Course--","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,stick=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12),state="readonly",width=20)
        year_combo["values"]=("--Select-Year--","FE","SE","TE","BE")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,stick=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12),state="readonly",width=20)
        semester_combo["values"]=("--Select-Semester--","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        ###### Class Student Information
        class_stu_info_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information", font=('times new roman',12,"bold"))
        class_stu_info_frame.place(x=5,y=250,width=745,height=300)
        
        # Student ID
        studentID_label=Label(class_stu_info_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,stick=W)

        studentID_entry=ttk.Entry(class_stu_info_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        # Student name
        studentName_label=Label(class_stu_info_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,stick=W)

        studentName_entry=ttk.Entry(class_stu_info_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        # class division
        classDivision_label=Label(class_stu_info_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        classDivision_label.grid(row=1,column=0,padx=10,pady=5,stick=W)

        class_div_combo=ttk.Combobox(class_stu_info_frame,textvariable=self.var_div,font=("times new roman",12),state="readonly",width=18)
        class_div_combo["values"]=("--Select-Division--","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,sticky=W)
        
        # roll_no
        roll_no_label=Label(class_stu_info_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,stick=W)

        roll_no_entry=ttk.Entry(class_stu_info_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,sticky=W)
        
        # gender
        gender_label=Label(class_stu_info_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,stick=W)

        gender_combo=ttk.Combobox(class_stu_info_frame,textvariable=self.var_gender,font=("times new roman",12),state="readonly",width=18)
        gender_combo["values"]=("--Select-Gender--","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # dob
        dob_label=Label(class_stu_info_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,stick=W)

        dob_entry=ttk.Entry(class_stu_info_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # email
        email_label=Label(class_stu_info_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,stick=W)

        email_entry=ttk.Entry(class_stu_info_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        # phone
        phone_label=Label(class_stu_info_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,stick=W)

        phone_entry=ttk.Entry(class_stu_info_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        # address
        address_label=Label(class_stu_info_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,stick=W)

        address_entry=ttk.Entry(class_stu_info_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        # teacher
        teacher_label=Label(class_stu_info_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,stick=W)

        teacher_entry=ttk.Entry(class_stu_info_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio buttons
        self.var_radio=StringVar()
        radiobtn1=ttk.Radiobutton(class_stu_info_frame,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(class_stu_info_frame,variable=self.var_radio,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)

        # Button's frame
        btn_frame1=Frame(class_stu_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=200,width=730,height=40)

        # Save button
        save_btn=Button(btn_frame1,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=5,pady=2)
        
        # update button
        update_btn=Button(btn_frame1,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=2)
        
        # delete button
        delete_btn=Button(btn_frame1,text="Delete",command=self.delete_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=5,pady=2)
        
        # reset button
        reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=5,pady=2)
        
        btn_frame2=Frame(class_stu_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=5,y=235,width=730,height=40)

        # take photo button
        take_photo_btn=Button(btn_frame2,text="Take Photo Sample",command=self.generate_dataset,width=38,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=5,pady=2)
        
        # update photo button
        update_btn=Button(btn_frame2,text="Update Photo Sample",width=38,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=5,pady=2)

        
        # RIGHT FRAME LABEL
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=('times new roman',12,"bold"))
        right_frame.place(x=800,y=10,width=660,height=580)

        img_right = Image.open(r"D:\Deep Learning\Student Attendance System\images\student_01.jpg")
        img_right=img_right.resize((660,130),Image.ANTIALIAS)
        self.background1=ImageTk.PhotoImage(img_right)
        bg1_label=Label(right_frame,image=self.background1)
        bg1_label.place(x=5,y=0,width=650,height=130)

        # --------------- Search System -----------
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System", font=('times new roman',12,"bold"))
        search_frame.place(x=5,y=135,width=650,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,stick=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12),state="readonly",width=15)
        search_combo["values"]=("--Select--","Roll_No.","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=8,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5,pady=2)
        
        showAll_btn=Button(search_frame,text="Show All",width=8,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5,pady=2)

        # =========== Table Frame ===============
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()  # fetching data from database



    # ======================= FUNCTION DECLERATION =======================

    def add_data(self):
        if self.var_dep.get()=="--Select-department--" or self.var_std_id.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                # messagebox.showinfo("Sucess","Sucessfully Saved!")
                conn=mysql.connector.connect(host="localhost",username="root",password="2003",database="student_attendance_sys")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
            
    # =============================== Fetch Data ===========================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2003",database="student_attendance_sys")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ============================== Get Cursor ===================
    def get_cursor(self,event):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio.set(data[14])

    # =================== Update Function ========================
    def update_data(self):
        if self.var_dep.get()=="--Select-department--" or self.var_std_id.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="2003",database="student_attendance_sys")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Sucess","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
    # ======================== Delete Function ==========================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID is Empty!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="2003",database="student_attendance_sys")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully Deleted student details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)

    # ============================ RESET FUNCTION ===========================
    def reset_data(self):
        self.var_dep.set("--Select-Department--"),
        self.var_course.set("--Select-Course--"),
        self.var_year.set("--Select-Year--"),
        self.var_semester.set("--Select-Semester--"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("--Select-Division--"),
        self.var_roll.set(""),
        self.var_gender.set("--Select-Gender--"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio.set("")
    

    # ==================== Generate dataset or take photo samples =======================
    def generate_dataset(self):
        if self.var_dep.get()=="--Select-department--" or self.var_std_id.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="2003",database="student_attendance_sys")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio.get(),
                    self.var_std_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ===================== Load predefined data on face frontals from opencv ===========================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)  # scaling factor=1.3, minimum neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)   # 2->font scale, (0,255,0)->font color, 2->thickness
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:   # 13 for enter
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!")
            except Exception as e:
                messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
