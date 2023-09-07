from tkinter import *
from tkinter import ttk
import os

# Pillow Library
from PIL import Image, ImageTk

# Import MessageBox
from tkinter import messagebox

# import MySql
import mysql.connector

import cv2
import numpy as np


class Train:
    # constructor
    def __init__(self,root):  # root is for root window
        self.root=root
        # setting geometry
        self.root.geometry("1530x790+0+0")   # 1530x790 is window size, both 0 is the coordinate of x and y i.e. start window from top-left
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        # top-image
        img_top = Image.open(r"images\train_face_recognition.jpg")
        img_top=img_top.resize((1530,325),Image.Resampling.LANCZOS)
        self.img_top=ImageTk.PhotoImage(img_top)
        img_top=Label(self.root,image=self.img_top)
        img_top.place(x=0,y=55,width=1530,height=325)

        # button
        bt1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",35,"bold"),bg="red",fg="white")
        bt1_1.place(x=0,y=380,width=1530,height=60)
        
        # bottom-image
        img_bottom = Image.open(r"images\photos.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.Resampling.LANCZOS)
        self.img_bottom=ImageTk.PhotoImage(img_bottom)
        img_bottom=Label(self.root,image=self.img_bottom)
        img_bottom.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   # L -> convert to gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        # ========================= Train the classifier and Save ===================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        clf.write("classifier.xlsx")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets COMPLETED!!")


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
