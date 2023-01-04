from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector
from PIL import Image, ImageTk

import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition")

        title__lbl=Label(self.root, text="FACE RECOGNITION", font=("Arial",25,"bold"), bg="red", fg="white")
        title__lbl.place(x=0,y=0,width=1530,height=30)

        # button
        b1_1=Button(self.root,text="Face detection",command=self.face_recog,cursor="hand2",font=("Arial",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=0,y=250,width=153,height=60)

        # ====================== Face recognition ==================
    
    def face_recog(self):
        os.system("python src/face_rec_cam.py")

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop() 