from tkinter import *
from tkinter import ttk
import cv2

# Pillow Library
from PIL import Image, ImageTk

# Import MessageBox
from tkinter import messagebox

# import MySql
import mysql.connector



class Developer:
    # constructor
    def __init__(self,root):  # root is for root window
        self.root=root
        # setting geometry
        self.root.geometry("1530x790+0+0")   # 1530x790 is window size, both 0 is the coordinate of x and y i.e. start window from top-left
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_label.place(x=0,y=0,width=1530,height=45)

        # bg-image
        bg_img = Image.open(r"images\developer.jpg")
        bg_img=bg_img.resize((1530,720),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(bg_img)
        bg_img=Label(self.root,image=self.bg_img)
        bg_img.place(x=0,y=55,width=1530,height=720)

        ######  FRAME  #######
        main_frame=Frame(bg_img,bd=2,bg="white")  # bd - border
        main_frame.place(x=900,y=0,width=600,height=600)


        self_img = Image.open(r"images\shivang.jpg")
        self_img=self_img.resize((200,200),Image.Resampling.LANCZOS)
        self.self_img=ImageTk.PhotoImage(self_img)
        self_img=Label(main_frame,image=self.self_img)
        self_img.place(x=380,y=0,width=200,height=200)

        # developer info
        dev_label=Label(main_frame,text="Hello! My name is Shivang",font=("times new roman",17,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="I am Machine Learning Enthusiast",font=("times new roman",17,"bold"),fg="yellow",bg="white")
        dev_label.place(x=0,y=50)
        dev_label=Label(main_frame,text="and Front-End Web Developer.",font=("times new roman",17,"bold"),fg="yellow",bg="white")
        dev_label.place(x=0,y=80)

        below_img = Image.open(r"images\student_bg.jpg")
        below_img=below_img.resize((570,370),Image.Resampling.LANCZOS)
        self.below_img=ImageTk.PhotoImage(below_img)
        below_img=Label(main_frame,image=self.below_img)
        below_img.place(x=10,y=215,width=570,height=370)



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()