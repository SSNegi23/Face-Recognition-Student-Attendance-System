from tkinter import *
from tkinter import ttk
import os
from time import strftime
from datetime import datetime

# Pillow Library
from PIL import Image, ImageTk

# Import MessageBox
from tkinter import messagebox

# import MySql
import mysql.connector

import cv2
import numpy as np


class Face_Recognition:
    # constructor
    def __init__(self,root):  # root is for root window
        self.root=root
        # setting geometry
        self.root.geometry("1530x790+0+0")   # 1530x790 is window size, both 0 is the coordinate of x and y i.e. start window from top-left
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_label.place(x=0,y=0,width=1530,height=45)

        # left image
        img_left = Image.open(r"images\facial-recognition-bg2.jpg")
        img_left=img_left.resize((650,700),Image.Resampling.LANCZOS)
        self.img_left=ImageTk.PhotoImage(img_left)
        img_left=Label(self.root,image=self.img_left)
        img_left.place(x=0,y=55,width=650,height=700)

        # right image
        img_right = Image.open(r"images\facial-recognition-bg1.png")
        img_right=img_right.resize((950,700),Image.Resampling.LANCZOS)
        self.img_right=ImageTk.PhotoImage(img_right)
        img_right=Label(self.root,image=self.img_right)
        img_right.place(x=650,y=55,width=950,height=700)
        
        # button
        bt1_1=Button(img_right,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        bt1_1.place(x=365,y=620,width=200,height=40)

    # =================== Attendance =============================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry=line.split((","))
                nameList.append(entry[0])

            if((i not in nameList) and (r not in nameList) and (n not in nameList) and (d not in nameList)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # =================== face recognition ========================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="2003",database="student_attendance_sys")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"SID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Rool:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To VIT BHOPAL",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
