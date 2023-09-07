from tkinter import *
from tkinter import ttk
import cv2
import os 
import csv
from tkinter import filedialog

# Pillow Library
from PIL import Image, ImageTk

# Import MessageBox
from tkinter import messagebox

# import MySql
import mysql.connector


mydata=[]
class Attendance:
    # constructor
    def __init__(self,root):  # root is for root window
        self.root=root
        # setting geometry
        self.root.geometry("1530x790+0+0")   # 1530x790 is window size, both 0 is the coordinate of x and y i.e. start window from top-left
        self.root.title("Face Recognition System")

        # ============= Variables ======================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
    
        # 1st image
        img1 = Image.open(r"images\photos.jpg")
        img1=img1.resize((800,200),Image.Resampling.LANCZOS)
        self.background1=ImageTk.PhotoImage(img1)
        bg1_label=Label(self.root,image=self.background1)
        bg1_label.place(x=0,y=0,width=800,height=200)
        # 2nd image
        img2 = Image.open(r"images\attendance_bg.jpg")
        img2=img2.resize((800,200),Image.Resampling.LANCZOS)
        self.background2=ImageTk.PhotoImage(img2)
        bg2_label=Label(self.root,image=self.background2)
        bg2_label.place(x=800,y=0,width=800,height=200)

        # bg image
        img_bg = Image.open(r"images\student_bg.jpg")
        img_bg=img_bg.resize((1530,710),Image.Resampling.LANCZOS)
        self.background=ImageTk.PhotoImage(img_bg)
        bg_img=Label(self.root,image=self.background)
        bg_img.place(x=0,y=200,width=1530,height=710)

        # title
        title_label=Label(bg_img,text="STUDENT ATTENDANCE",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_label.place(x=0,y=0,width=1530,height=45)

        ######  FRAME  #######
        main_frame=Frame(bg_img,bd=2,bg="white")  # bd - border
        main_frame.place(x=20,y=50,width=1480,height=600)

        # LEFT LABEL FRAME
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details", font=('times new roman',12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=510)

        img_left_frame = Image.open(r"images\fr2.jpg")
        img_left_frame=img_left_frame.resize((750,130),Image.Resampling.LANCZOS)
        self.img_left=ImageTk.PhotoImage(img_left_frame)
        img_left_top=Label(left_frame,image=self.img_left)
        img_left_top.place(x=5,y=0,width=750,height=130)

        left_inside_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information", font=('times new roman',12,"bold"))
        left_inside_frame.place(x=10,y=135,width=740,height=350)

        # Attendance ID
        attendanceID_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,stick=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        # Roll
        attendanceID_label=Label(left_inside_frame,text="Roll:",font=("comicsansns",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=2,padx=4,pady=8)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("comicsansns",12,"bold"))
        attendanceID_entry.grid(row=0,column=3,pady=8)
        
        # Name
        attendanceID_label=Label(left_inside_frame,text="Name:",font=("comicsansns",12,"bold"),bg="white")
        attendanceID_label.grid(row=1,column=0)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font=("comicsansns",12,"bold"))
        attendanceID_entry.grid(row=1,column=1,pady=8)
        
        # Department
        attendanceID_label=Label(left_inside_frame,text="Department:",font=("comicsansns",12,"bold"),bg="white")
        attendanceID_label.grid(row=1,column=2)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("comicsansns",12,"bold"))
        attendanceID_entry.grid(row=1,column=3,pady=8)
        
        # Time
        attendanceID_label=Label(left_inside_frame,text="Time:",font=("comicsansns",12,"bold"),bg="white")
        attendanceID_label.grid(row=2,column=0)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("comicsansns",12,"bold"))
        attendanceID_entry.grid(row=2,column=1,pady=8)
        
        # Date
        attendanceID_label=Label(left_inside_frame,text="Date:",font=("comicsansns",12,"bold"),bg="white")
        attendanceID_label.grid(row=2,column=2)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("comicsansns",12,"bold"))
        attendanceID_entry.grid(row=2,column=3,pady=8)
        
        # Attendance
        attendanceID_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 12 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # Button's frame
        btn_frame1=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=270,width=730,height=40)

        # Import csv button
        import_csv=Button(btn_frame1,text="Import CSV",command=self.importCSV,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_csv.grid(row=0,column=0,padx=5,pady=2)
        
        # Export CSV button
        export_csv=Button(btn_frame1,text="Export CSV",command=self.exportCSV,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_csv.grid(row=0,column=1,padx=5,pady=2)
        
        # Update button
        update_btn=Button(btn_frame1,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2,padx=5,pady=2)
        
        # reset button
        reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=5,pady=2)

        # RIGHT FRAME LABEL
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Sheet", font=('times new roman',12,"bold"))
        right_frame.place(x=800,y=10,width=660,height=510)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=645,height=445)

        # ================= Scroll bar table =================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=120)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ================ Fetch Data =====================
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(('CSV files','*.csv'),('All files','*.*')),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(('CSV files','*.csv'),('All files','*.*')),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" Successfully!!")
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    def update_data(self):
        import subprocess
        # Specify the path to your CSV file
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(('CSV files','*.csv'),('All files','*.*')),parent=self.root)
        csv_file_path = fln  # Replace with the actual path to your CSV file

        try:
            # Use the 'start' command to open the CSV file in Excel (Windows)
            subprocess.Popen(['start', 'excel', csv_file_path], shell=True)
        except Exception as e:
            print(f"An error occurred: {e}")




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()