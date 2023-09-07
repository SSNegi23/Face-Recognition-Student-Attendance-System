import tkinter
from tkinter import *
from tkinter import ttk
import os
from time import strftime

# Pillow Library
from PIL import Image, ImageTk

# Importing components
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_recognition_System:
    # constructor
    def __init__(self,root):  # root is for root window
        self.root=root
        # setting geometry
        self.root.geometry("1530x790+0+0")   # 1530x790 is window size, both 0 is the coordinate of x and y i.e. start window from top-left
        self.root.title("Face Recognition System")

        #### Setting Background Image
        # width of window is 1530, for 3 img width will be 510 per img
        # 1st image
        img1 = Image.open(r"images\background_01.jpg")
        img1=img1.resize((510,130),Image.Resampling.LANCZOS)
        self.background1=ImageTk.PhotoImage(img1)
        bg1_label=Label(self.root,image=self.background1)
        bg1_label.place(x=0,y=0,width=525,height=130)
        # 2nd image
        img2 = Image.open(r"images\background_02.jpg")
        img2=img2.resize((510,130),Image.Resampling.LANCZOS)
        self.background2=ImageTk.PhotoImage(img2)
        bg2_label=Label(self.root,image=self.background2)
        bg2_label.place(x=510,y=0,width=510,height=130)
        # 3rd image
        img3 = Image.open(r"images\background_03.jpg")
        img3=img3.resize((510,130),Image.Resampling.LANCZOS)
        self.background3=ImageTk.PhotoImage(img3)
        bg3_label=Label(self.root,image=self.background3)
        bg3_label.place(x=1020,y=0,width=510,height=130)

        # bg image
        img_bg = Image.open(r"images\background.jpg")
        img_bg=img_bg.resize((1530,710),Image.Resampling.LANCZOS)
        self.background=ImageTk.PhotoImage(img_bg)
        bg_img=Label(self.root,image=self.background)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # title
        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        # ============== TIME ======================
        def time():
            string=strftime('%H:%M:%S')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(bg_img,font=('time new roman',14,'bold'),background="white",foreground="blue")
        lbl.place(x=1400,y=40,width=110,height=50)
        time()

        # student button
        bt_img_student = Image.open(r"images\student_button.jpg")
        bt_img_student=bt_img_student.resize((220,220),Image.Resampling.LANCZOS)
        self.bt1_img=ImageTk.PhotoImage(bt_img_student)
        bt1=Button(bg_img,image=self.bt1_img,command=self.student_details,cursor="hand2")
        bt1.place(x=200,y=100,width=220,height=220)
        bt1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bt1_1.place(x=200,y=300,width=220,height=40)
        
        # detect face button
        bt_img_face_decetor = Image.open(r"images\face_recognition.jpg")
        bt_img_face_decetor=bt_img_face_decetor.resize((220,220),Image.Resampling.LANCZOS)
        self.bt2_img=ImageTk.PhotoImage(bt_img_face_decetor)
        bt2=Button(bg_img,image=self.bt2_img,cursor="hand2",command=self.face_data)
        bt2.place(x=500,y=100,width=220,height=220)
        bt2_2=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bt2_2.place(x=500,y=300,width=220,height=40)

        # attendance
        bt_img_attendance = Image.open(r"images\student_01.jpg")
        bt_img_attendance=bt_img_attendance.resize((220,220),Image.Resampling.LANCZOS)
        self.bt3_img=ImageTk.PhotoImage(bt_img_attendance)
        bt3=Button(bg_img,image=self.bt3_img,cursor="hand2",command=self.attendance_data)
        bt3.place(x=800,y=100,width=220,height=220)
        bt3_3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bt3_3.place(x=800,y=300,width=220,height=40)
        
        # help
        bt_img_help = Image.open(r"images\help.jpg")
        bt_img_help=bt_img_help.resize((220,220),Image.Resampling.LANCZOS)
        self.bt4_img=ImageTk.PhotoImage(bt_img_help)
        bt4=Button(bg_img,image=self.bt4_img,cursor="hand2",command=self.help_data)
        bt4.place(x=1100,y=100,width=220,height=220)
        bt4_4=Button(bg_img,text="Help",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bt4_4.place(x=1100,y=300,width=220,height=40)
        
        # train face button
        bt_img_train_face = Image.open(r"images\train_face.jpg")
        bt_img_train_face=bt_img_train_face.resize((220,220),Image.Resampling.LANCZOS)
        self.bt5_img=ImageTk.PhotoImage(bt_img_train_face)
        bt5=Button(bg_img,image=self.bt5_img,cursor="hand2",command=self.train_data)
        bt5.place(x=200,y=380,width=220,height=220)
        bt5_5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bt5_5.place(x=200,y=580,width=220,height=40)
        
        # photo button
        bt_img_photo = Image.open(r"images\collage-of-student-photo.jpg")
        bt_img_photo=bt_img_photo.resize((220,220),Image.Resampling.LANCZOS)
        self.bt6_img=ImageTk.PhotoImage(bt_img_photo)
        bt6=Button(bg_img,image=self.bt6_img,cursor="hand2",command=self.open_img)
        bt6.place(x=500,y=380,width=220,height=220)
        bt6_6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bt6_6.place(x=500,y=580,width=220,height=40)

        # developer
        bt_img_developer = Image.open(r"images\developer.jpg")
        bt_img_developer=bt_img_developer.resize((220,220),Image.Resampling.LANCZOS)
        self.bt7_img=ImageTk.PhotoImage(bt_img_developer)
        bt7=Button(bg_img,image=self.bt7_img,cursor="hand2",command=self.developer_data)
        bt7.place(x=800,y=380,width=220,height=220)
        bt7_7=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bt7_7.place(x=800,y=580,width=220,height=40)
        
        # exit
        bt_img_exit = Image.open(r"images\exit.jpg")
        bt_img_exit=bt_img_exit.resize((220,220),Image.Resampling.LANCZOS)
        self.bt8_img=ImageTk.PhotoImage(bt_img_exit)
        bt8=Button(bg_img,image=self.bt8_img,cursor="hand2",command=self.exit)
        bt8.place(x=1100,y=380,width=220,height=220)
        bt8_8=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bt8_8.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    # ====================== FUNCTION BUTTONS ==========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recodnition System","Dou you wnat to Quit?")
        if self.exit>0:
            self.root.destroy()
        else:
            return
        


if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
