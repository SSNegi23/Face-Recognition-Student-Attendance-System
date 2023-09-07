from tkinter import *
from tkinter import ttk
import cv2

# Pillow Library
from PIL import Image, ImageTk

# Import MessageBox
from tkinter import messagebox

# import MySql
import mysql.connector



class Help:
    # constructor
    def __init__(self,root):  # root is for root window
        self.root=root
        # setting geometry
        self.root.geometry("1530x790+0+0")   # 1530x790 is window size, both 0 is the coordinate of x and y i.e. start window from top-left
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_label.place(x=0,y=0,width=1530,height=45)

        # bg-image
        bg_img = Image.open(r"images\help.jpg")
        bg_img=bg_img.resize((1530,720),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(bg_img)
        bg_img=Label(self.root,image=self.bg_img)
        bg_img.place(x=0,y=55,width=1530,height=720)

        # Label
        dev_label=Label(bg_img,text="Email: negi1322003@gmail.com",font=("times new roman",17,"bold"),fg="blue",bg="yellow")
        dev_label.place(x=600,y=300)



if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()