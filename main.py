from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition System")

        #first imag
        img=Image.open("./college_image/SME.jpg")
        img=img.resize((450,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)

        #second imag
        img1=Image.open("./college_image/HUST.jpg")
        img1=img1.resize((450,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=130)

        #third imag
        img2=Image.open("./college_image/HUST1.png")
        img2=img2.resize((450,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=130)

        #bg imag
        img3=Image.open("./college_image/bg1.jpg")
        img3=img3.resize((1530,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title__lbl=Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE", font=("Arial",30,"bold"), bg="white", fg="red")
        title__lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open("./college_image/HUST.jpg")
        img4=img4.resize((180,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=300,y=50,width=180,height=220)

        b1_1=Button(bg_img,text="Thông tin sinh viên",command=self.student_details,cursor="hand2",font=("Arial",12,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=300,y=250,width=180,height=40)

        #Dectec button
        img5=Image.open("./college_image/HUST.jpg")
        img5=img5.resize((180,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=600,y=50,width=180,height=220)

        b1_1=Button(bg_img,text="Nhận diện",cursor="hand2",command=self.face_data,font=("Arial",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=600,y=250,width=180,height=40)

        #Attendance button
        img6=Image.open("./college_image/HUST.jpg")
        img6=img6.resize((180,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=900,y=50,width=180,height=220)

        b1_1=Button(bg_img,text="Điểm danh",cursor="hand2",font=("Arial",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=900,y=250,width=180,height=40)

        #Help button
        img7=Image.open("./college_image/HUST.jpg")
        img7=img7.resize((180,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=300,y=300,width=180,height=220)

        b1_1=Button(bg_img,text="Trợ giúp",cursor="hand2",font=("Arial",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=300,y=500,width=180,height=40)

        #Train button
        # img8=Image.open(r"college_image\HUST.jpg")
        # img8=img8.resize((180,220),Image.ANTIALIAS)
        # self.photoimg8=ImageTk.PhotoImage(img8)

        # b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        # b1.place(x=150,y=300,width=180,height=220)

        # b1_1=Button(bg_img,text="",cursor="hand2",command=self.train_data,font=("Arial",15,"bold"), bg="darkblue", fg="white")
        # b1_1.place(x=150,y=500,width=180,height=40)

        #Photo Data button
        # img9=Image.open(r"college_image\HUST.jpg")
        # img9=img9.resize((180,220),Image.ANTIALIAS)
        # self.photoimg9=ImageTk.PhotoImage(img9)

        # b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        # b1.place(x=450,y=300,width=180,height=220)

        # b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("Arial",15,"bold"), bg="darkblue", fg="white")
        # b1_1.place(x=450,y=500,width=180,height=40)

        #Developer button
        img10=Image.open("./college_image/HUST.jpg")
        img10=img10.resize((180,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=600,y=300,width=180,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("Arial",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=600,y=500,width=180,height=40)

        #Exit button
        img11=Image.open("./college_image/HUST.jpg")
        img11=img11.resize((180,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=900,y=300,width=180,height=220)

        b1_1=Button(bg_img,text="Thoát",cursor="hand2",font=("Arial",15,"bold"), bg="darkblue", fg="white")
        b1_1.place(x=900,y=500,width=180,height=40)

    def open_img(self):
        os.startfile("data")

    #================Function buttons===============

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()           