from tkinter import *
from tkinter import messagebox, ttk, filedialog

from PIL import Image, ImageTk

import os
import csv
import numpy as np
from datetime import datetime

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("Attendance")

        # ==============Variable================#

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
        self.var_mail=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        self.attendances = []
        self.times = {}

         #bg imag
        img3=Image.open("./college_image/HUST.jpg")
        img3=img3.resize((1400,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=50,width=1400,height=700)

        title__lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Arial",25,"bold"), bg="red", fg="white")
        title__lbl.place(x=0,y=0,width=1400,height=30)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=30,width=1400,height=800)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=30,width=1400,height=800)

        Right_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student detail",font=("Arial",12,"bold"))
        Right_Frame.place(x=0,y=10,width=1400,height=500)

        #=================================================================#

        table_Frame=Frame(Right_Frame,bd=2,bg="white",relief=RIDGE)
        table_Frame.place(x=5,y=10,width=1350,height=400)

        Scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_Frame,column=("Atd","dep","course","year","sem","id","name", "div", "Roll", "gender", "dob","email","phone","address","teacher","photoSample"))

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Atd",text="Diem danh")
        self.student_table.heading("dep",text="Ngành")
        self.student_table.heading("course",text="Khóa")
        self.student_table.heading("year",text="Năm học")
        self.student_table.heading("sem",text="Kỳ học")
        self.student_table.heading("id",text="MSSV")
        self.student_table.heading("name",text="Tên")
        self.student_table.heading("div",text="Lớp")
        self.student_table.heading("Roll",text="STT")
        self.student_table.heading("gender",text="Giới tính")
        self.student_table.heading("dob",text="Ngày sinh")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="SĐT")
        self.student_table.heading("address",text="Địa chỉ")
        self.student_table.heading("teacher",text="Giảng viên")
        self.student_table.heading("photoSample",text="Ảnh")
        self.student_table["show"]="headings"

        self.student_table.column("Atd",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photoSample",width=100)

        self.student_table.pack(fill=BOTH,expand=1)

        #=========================================#

        import_btn=Button(main_frame,text="chon lop",width=22,font=("Arial",12,"bold"),bg="blue",fg="white", command=self.importClass)
        import_btn.place(x=0, y=500)

        report_btn=Button(main_frame,text="bao cao",width=11,font=("Arial",12,"bold"),bg="blue",fg="white", command=self.exportReport)
        report_btn.place(x=500, y=500)

    #========== import class function ========#
    def importClass(self):
        now = datetime.now()
        now = now.strftime("%d_%m_%Y")
        
        data_path = f"attendance/{now}/{now}.csv"
        
        self.times = {}
        self.attendances = []

        with open(data_path, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                self.attendances.append(row[1])
                self.times[row[1]] = row[0]

        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        if (len(fln) == 0): 
            return
        try:
            self.student_table.delete(*self.student_table.get_children())
            with open(fln, "r", newline='', encoding="utf-8") as f:
                csv_reader = csv.reader(f)
                line_count = 0
                for row in csv_reader:
                    if line_count != 0:
                        if row[4] in self.attendances:
                            row.insert(0, self.times[row[4]])
                        else:
                            row.insert(0, "Vắng")
                        self.student_table.insert("",END,values=row)
                    line_count += 1
            messagebox.showinfo("Success","class details has been add successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"due to :{str(es)}",parent=self.root)
        return     

    #========== export report function ========#  
    def exportReport(self):
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        if (len(fln) == 0): 
            return
        try:
            with open(fln, "w", newline='', encoding="utf-8") as f:
                f.write('\ufeff')
                writer = csv.writer(f)
                writer.writerows([("attend", "dep", "course", "year", 
                                    "semester", "studentID", "studentName", 
                                    "Division", "Roll", "gender", 
                                    "dob", "mail", "phone", 
                                    "address", "teacher", "photo")])
                line_count = 0
                writer = csv.writer(f)
                for line in self.student_table.get_children():
                    line_count += 1
                    data = self.student_table.item(line)["values"]
                    writer.writerows([(data[0], data[1], data[2],
                                        data[3], data[4], data[5],
                                        data[6], data[7], data[8],
                                        data[9], data[10], data[11],
                                        data[12], data[13], data[14], data[15])])
                now = datetime.now()
                now = now.strftime("%d/%m/%Y")
                writer.writerows([(f"Sĩ số ngày {now}: {len(self.attendances)} / {line_count}", "")])
                messagebox.showinfo("Success",f"Sĩ số ngày {now}: {len(self.attendances)} / {line_count}",parent=self.root)  
        except Exception as es:
            messagebox.showerror("Error",f"due to :{str(es)}",parent=self.root)
        return

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop() 