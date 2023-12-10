from array import array
from cProfile import label
from cgitb import text
from optparse import Values
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, LEFT, RIGHT, VERTICAL, Y, Button, Place, StringVar, ttk
from tkinter import messagebox,Label,RIDGE,TOP,Frame,LabelFrame,W,X,Entry,Tk,Text
import random
import time
import datetime
from tkinter import font
from tkinter.font import BOLD, Font
from tkinter.tix import COLUMN
from turtle import right, width
from unittest import TextTestResult
import mysql.connector

class Hospital:
    def __init__(self,root) -> None:
        self.root=root
        self.root.title("Hospital Patient Registration")
        self.root.geometry("1540x800+0+0")
        
        self.RefrenceNo=StringVar()
        self.PatientName=StringVar()
        self.ContactNumber=StringVar()
        self.PatientAge=StringVar()
        self.PatientWeight=StringVar()
        self.BloodPressure=StringVar()
        self.IllnessReason=StringVar()
        self.NameOfTablet=StringVar()
        self.Dose=StringVar()
        self.NumberOfTablet=StringVar()
        self.lot=StringVar()
        self.IssueDate=StringVar()
        self.SideEffects=StringVar()
        self.Precautions=StringVar()
        self.TotalAmount=StringVar()
        self.PaidAmount=StringVar()
        self.PaymentMode=StringVar()
        self.RemainingAmount=StringVar()
        
        lableTitle=Label(self.root,bd=15,relief=RIDGE,text="Hospital Patient Registration",fg="blue",bg='white',
                            font=("times new roman",30,BOLD))
        lableTitle.pack(side=TOP,fill=X)
   
        #============================ Making Dataframe for Patient Information ================================================#
        Dataframe=Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=('arial',12,"bold"),text='Patient Information')
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=15,padx=20,relief=RIDGE,font=('arial',12,"bold"),text='Prescription')
        DataframeRight.place(x=990,y=5,width=460,height=350)
        
        #============================Making Button Frame==============================================================#
        self.Buttonframe=Frame(self.root,bd=15,relief=RIDGE)
        self.Buttonframe.place(x=0,y=530,width=1530,height=70)

        #============================Making Detail Frame========================================================#
        Detailframe=Frame(self.root,bd=15,relief=RIDGE)
        Detailframe.place(x=0,y=600,width=1530,height=190)
        

        #==============DataframeLeft fields=================================================================#
        lblRefrenceNo=Label(DataframeLeft,font=('arial',12),text="Refrence No:",padx=2,pady=6)
        lblRefrenceNo.grid(row=0,column=0,sticky=W)
        txtRefrenceNo=Entry(DataframeLeft,textvariable=self.RefrenceNo,font=('arial',12),width=35)
        txtRefrenceNo.grid(row=0,column=1)

        lblPatientName=Label(DataframeLeft,font=('arial',12),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=1,column=0,sticky=W)
        txtPatientName=Entry(DataframeLeft,textvariable=self.PatientName,font=('arial',12),width=35)
        txtPatientName.grid(row=1,column=1)

        lblContactNumber=Label(DataframeLeft,font=('arial',12),text="Contact Number:",padx=2,pady=6)
        lblContactNumber.grid(row=2,column=0,sticky=W)
        txtContactNumber=Entry(DataframeLeft,textvariable=self.ContactNumber,font=('arial',12),width=35)
        txtContactNumber.grid(row=2,column=1)

        lblPatientAge=Label(DataframeLeft,font=('arial',12),text="Patient Age:",padx=2,pady=6)
        lblPatientAge.grid(row=3,column=0,sticky=W)
        txtPatientAge=Entry(DataframeLeft,textvariable=self.PatientAge,font=('arial',12),width=35)
        txtPatientAge.grid(row=3,column=1)

        lblPatientWeight=Label(DataframeLeft,font=('arial',12),text="Patient Weight:",padx=2,pady=6)
        lblPatientWeight.grid(row=4,column=0,sticky=W)
        txtPatientWeight=Entry(DataframeLeft,textvariable=self.PatientWeight,font=('arial',12),width=35)
        txtPatientWeight.grid(row=4,column=1)

        lblBloodPressure=Label(DataframeLeft,font=('arial',12),text="Blood Pressue:",padx=2,pady=6)
        lblBloodPressure.grid(row=5,column=0,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,textvariable=self.BloodPressure,font=('arial',12),width=35)
        txtBloodPressure.grid(row=5,column=1)

        lblIllnessReason=Label(DataframeLeft,font=('arial',12),text="Illness Reason:",padx=2,pady=6)
        lblIllnessReason.grid(row=6,column=0,sticky=W)
        txtIllnessReason=Entry(DataframeLeft,textvariable=self.IllnessReason,font=('arial',12),width=35)
        txtIllnessReason.grid(row=6,column=1)
        
        lblNameOfTablet=Label(DataframeLeft,font=("arial",12),text="Name of Tablet:",padx=2,pady=6)
        lblNameOfTablet.grid(row=7,column=0)
        listOfTablet=ttk.Combobox(DataframeLeft,textvariable=self.NameOfTablet,state="readonly",font=("arial",12),width=33)
        listOfTablet['value']=('Anacine','Bloffin','Paracetamol','Crocin','Quadridrum')
        listOfTablet.grid(row=7,column=1)

        lblDose=Label(DataframeLeft,font=('arial',12),text="Dose:",padx=2,pady=6)
        lblDose.grid(row=8,column=0,sticky=W)
        numOfDose=ttk.Combobox(DataframeLeft,textvariable=self.Dose,state="readonly",font=('arial',12),width=33)
        numOfDose['value']=('One time a day','Two times a day','Three times a day')
        numOfDose.grid(row=8,column=1)

        lblNumberOfTablet=Label(DataframeLeft,font=('arial',12),text="Number of Tablet:",padx=2,pady=6)
        lblNumberOfTablet.grid(row=0,column=2,sticky=W)
        txtNumberOfTablet=Entry(DataframeLeft,textvariable=self.NumberOfTablet,font=('arial',12),width=35)
        txtNumberOfTablet.grid(row=0,column=3)

        lbllot=Label(DataframeLeft,font=('arial',12),text="lot:",padx=2,pady=6)
        lbllot.grid(row=1,column=2,sticky=W)
        txtlot=Entry(DataframeLeft,textvariable=self.lot,font=('arial',12),width=35)
        txtlot.grid(row=1,column=3)

        lblIssueDate=Label(DataframeLeft,font=('arial',12),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=2,column=2,sticky=W)
        txtIssueDate=Entry(DataframeLeft,textvariable=self.IssueDate,font=('arial',12),width=35)
        txtIssueDate.grid(row=2,column=3)
        date=datetime.datetime.now()
        format_date=f"({date:%a, %b %d %Y %H:%M:%S})"
        txtIssueDate.insert(END,str(format_date))
        txtIssueDate.configure(state='disabled')

        lblSideEffects=Label(DataframeLeft,font=('arial',12),text="Side Effects:",padx=2,pady=6)
        lblSideEffects.grid(row=3,column=2,sticky=W)
        txtSideEffects=Entry(DataframeLeft,textvariable=self.SideEffects,font=('arial',12),width=35)
        txtSideEffects.grid(row=3,column=3)

        lblPrecautions=Label(DataframeLeft,font=('arial',12),text="Precautions:",padx=2,pady=6)
        lblPrecautions.grid(row=4,column=2,sticky=W)
        txtPrecautions=Entry(DataframeLeft,textvariable=self.Precautions,font=('arial',12),width=35)
        txtPrecautions.grid(row=4,column=3)

        lblTotalAmount=Label(DataframeLeft,font=('arial',12),text="Total Amount:",padx=2,pady=6)
        lblTotalAmount.grid(row=5,column=2,sticky=W)
        txtTotalAmount=Entry(DataframeLeft,textvariable=self.TotalAmount,font=('arial',12),width=35)
        txtTotalAmount.grid(row=5,column=3)

        lblPaidAmount=Label(DataframeLeft,font=('arial',12),text="Paid Amount:",padx=2,pady=6)
        lblPaidAmount.grid(row=6,column=2,sticky=W)
        txtPaidAmount=Entry(DataframeLeft,textvariable=self.PaidAmount,font=('arial',12),width=35)
        txtPaidAmount.grid(row=6,column=3)

        lblPaymentMode=Label(DataframeLeft,font=('arial',12),text="Payment Mode:",padx=2,pady=6)
        lblPaymentMode.grid(row=7,column=2,sticky=W)
        paymentMethod=ttk.Combobox(DataframeLeft,textvariable=self.PaymentMode,state="readonly",font=("arial",12),width=33)
        paymentMethod['value']=('Cash','ATM','Check','NEFT')
        paymentMethod.grid(row=7,column=3)
        

        lblRemainingAmount=Label(DataframeLeft,font=('arial',12),text="Remaining Amount:",padx=2,pady=6)
        lblRemainingAmount.grid(row=8,column=2,sticky=W)
        txtRemainingAmount=Entry(DataframeLeft,textvariable=self.RemainingAmount,font=('arial',12),width=35)
        txtRemainingAmount.grid(row=8,column=3)
        #=======================DataFrameRight fields=========================================#
        self.txtPrescription=Text(DataframeRight,font=('arial',12),width=48,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        
        scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailframe,columns=('RefrenceNo','PatientName','ContactNumber','PatientAge',
                                                              'PatientWeight','BloodPressure','IllnessReason','NameOfTablet',
                                                              'Dose','NumberOfTablet','lot','IssueDate','SideEffects','Precautions',
                                                              'TotalAmount','PaidAmount','PaymentMode','RemainingAmount'),
                                                               xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("RefrenceNo",text="Refrence No")
        self.hospital_table.heading("PatientName",text="Patient Name")
        self.hospital_table.heading("ContactNumber",text="Contact Number")
        self.hospital_table.heading("PatientAge",text="Patient Age")
        self.hospital_table.heading("PatientWeight",text="Patient Weight")
        self.hospital_table.heading("BloodPressure",text="Blood Pressure")
        self.hospital_table.heading("IllnessReason",text="Illness Reason")
        self.hospital_table.heading("NameOfTablet",text="Name Of Tablet")
        self.hospital_table.heading("Dose",text="Dose")
        self.hospital_table.heading("NumberOfTablet",text="Number Of Tablets")
        self.hospital_table.heading("lot",text="lot")
        self.hospital_table.heading("IssueDate",text="Issue Date")
        self.hospital_table.heading("SideEffects",text="Side Effects")
        self.hospital_table.heading("Precautions",text="Precautions")
        self.hospital_table.heading("TotalAmount",text="Total Amount")
        self.hospital_table.heading("PaidAmount",text="Paid Amount")
        self.hospital_table.heading("PaymentMode",text="Payment Mode")
        self.hospital_table.heading("RemainingAmount",text="Remaining Amount")
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("RefrenceNo",width=100)
        self.hospital_table.column("PatientName",width=100)
        self.hospital_table.column("ContactNumber",width=100)
        self.hospital_table.column("PatientAge",width=100)
        self.hospital_table.column("PatientWeight",width=100)
        self.hospital_table.column("BloodPressure",width=100)
        self.hospital_table.column("IllnessReason",width=100)
        self.hospital_table.column("NameOfTablet",width=100)
        self.hospital_table.column("Dose",width=100)
        self.hospital_table.column("NumberOfTablet",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("IssueDate",width=100)
        self.hospital_table.column("SideEffects",width=100)
        self.hospital_table.column("Precautions",width=100)
        self.hospital_table.column("TotalAmount",width=100)
        self.hospital_table.column("PaidAmount",width=100)
        self.hospital_table.column("PaymentMode",width=100)
        self.hospital_table.column("RemainingAmount",width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        
    def entry_details(self)->None:
        if(self.RefrenceNo.get()=="" or self.PatientName.get()==""):
            messagebox.showerror("Error 101:","All Fields are required")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='Test@123',database='Mydata')
            mycursor=conn.cursor()
            mycursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                         self.RefrenceNo.get(),
                                                                                                         self.PatientName.get(),
                                                                                                         self.ContactNumber.get(),
                                                                                                         self.PatientAge.get(),
                                                                                                         self.PatientWeight.get(),
                                                                                                         self.BloodPressure.get(),
                                                                                                         self.IllnessReason.get(),
                                                                                                         self.NameOfTablet.get(),
                                                                                                         self.Dose.get(),
                                                                                                         self.NumberOfTablet.get(),
                                                                                                         self.lot.get(),
                                                                                                         self.IssueDate.get(),
                                                                                                         self.SideEffects.get(),
                                                                                                         self.Precautions.get(),
                                                                                                         self.TotalAmount.get(),
                                                                                                         self.PaidAmount.get(),
                                                                                                         self.PaymentMode.get(),
                                                                                                         self.RemainingAmount.get()
                                                                                                         ))    
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")
    
    def fetch_data(self)->None:
        conn=mysql.connector.connect(host='localhost',user='root',password='Test@123',database='Mydata')
        mycursor=conn.cursor()
        mycursor.execute('select * from hospital')
        array=mycursor.fetchall()
        if array:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in array:
                self.hospital_table.insert("",END,values=row)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event)->None:
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.RefrenceNo.set(row[0])
        self.PatientName.set(row[1])
        self.ContactNumber.set(row[2])
        self.PatientAge.set(row[3])
        self.PatientWeight.set(row[4])
        self.BloodPressure.set(row[5])
        self.IllnessReason.set(row[6])
        self.NameOfTablet.set(row[7])
        self.Dose.set(row[8])
        self.NumberOfTablet.set(row[9])
        self.lot.set(row[10])
        self.IssueDate.set(row[11])
        self.SideEffects.set(row[12])
        self.Precautions.set(row[13])
        self.TotalAmount.set(row[14])
        self.PaidAmount.set(row[15])
        self.PaymentMode.set(row[16])
        self.RemainingAmount.set(row[17])
        
    def updateRecord(self)->None:
        conn=mysql.connector.connect(host='localhost',user='root',password='Test@123',database='Mydata')
        mycursor=conn.cursor()
        mycursor.execute("update hospital set PatientName=%s,ContactNumber=%s,PatientAge=%s,PatientWeight=%s,BloodPressure=%s,IllnessReason=%s,NameOfTablet=%s,Dose=%s,NumberOfTablet=%s,lot=%s,IssueDate=%s,SideEffects=%s,Precautions=%s,TotalAmount=%s,PaidAmount=%s,PaymentMode=%s,RemainingAmount=%s where RefrenceNo=%s",(
                                                    self.PatientName.get(),
                                                    self.ContactNumber.get(),
                                                    self.PatientAge.get(),
                                                    self.PatientWeight.get(),
                                                    self.BloodPressure.get(),
                                                    self.IllnessReason.get(),
                                                    self.NameOfTablet.get(),
                                                    self.Dose.get(),
                                                    self.NumberOfTablet.get(),
                                                    self.lot.get(),
                                                    self.IssueDate.get(),
                                                    self.SideEffects.get(),
                                                    self.Precautions.get(),
                                                    self.TotalAmount.get(),
                                                    self.PaidAmount.get(),
                                                    self.PaymentMode.get(),
                                                    self.RemainingAmount.get(),
                                                    self.RefrenceNo.get()
                                                    ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record has been Updated")
        
    def show_record(self)->None:
        self.txtPrescription.insert(END,"Refrence No:\t\t"+self.RefrenceNo.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"Contact Number:\t\t"+self.ContactNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Age:\t\t"+self.PatientAge.get()+"\n")
        self.txtPrescription.insert(END,"Patient Weight:\t\t"+self.PatientAge.get()+"\n")
        self.txtPrescription.insert(END,"Blood Pressure:\t\t"+self.BloodPressure.get()+"\n")
        self.txtPrescription.insert(END,"Illness Reason:\t\t"+self.IllnessReason.get()+"\n")
        self.txtPrescription.insert(END,"Name of tablet:\t\t"+self.NameOfTablet.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number Of Tablet:\t\t"+self.NumberOfTablet.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t"+self.lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date\t\t"+self.IssueDate.get()+"\n")
        self.txtPrescription.insert(END,"Side Effects:\t\t"+self.SideEffects.get()+"\n")
        self.txtPrescription.insert(END,"Precautions:\t\t"+self.Precautions.get()+"\n")
        self.txtPrescription.insert(END,"Total Amount:\t\t"+self.TotalAmount.get()+"\n")
        self.txtPrescription.insert(END,"Paid Amount:\t\t"+self.PaidAmount.get()+"\n")
        self.txtPrescription.insert(END,"Payment Mode:\t\t"+self.PaymentMode.get()+"\n")
        self.txtPrescription.insert(END,"Remaining Amount:\t\t"+self.RemainingAmount.get()+"\n")
        
    
    def record_delete(self)->None:
        conn=mysql.connector.connect(host='localhost',user='root',password='Test@123',database='Mydata')
        mycursor=conn.cursor()
        query="delete from hospital where RefrenceNo=%s"
        value=(self.RefrenceNo.get(),)  # value should be in proper tuple format otherwise error will happen
        mycursor.execute(query,value)
        conn.commit()
        conn.close()
        messagebox.showinfo('Delete','Patient has been deleted successfully')
        
    def clear_record(self)->None:
        self.RefrenceNo.set('')
        self.PatientName.set('')
        self.ContactNumber.set('')
        self.PatientAge.set('')
        self.PatientWeight.set('')
        self.BloodPressure.set('')
        self.IllnessReason.set('')
        self.NameOfTablet.set('')
        self.Dose.set('')
        self.NumberOfTablet.set('')
        self.lot.set('')
        self.IssueDate.set('')
        self.SideEffects.set('')
        self.Precautions.set('')
        self.TotalAmount.set('')
        self.PaidAmount.set('')
        self.PaymentMode.set('')
        self.RemainingAmount.set('')
        #Also erasing the prescription text preview
        self.txtPrescription.delete('1.0',"end")
    
    def exit_appilication(self)->None:
        yes_no=messagebox.askyesno("Hospital management","Confirm your choice")
        if yes_no>0:
            root.destroy()
            return
          
    def buttonClick(self)->None:
        btnPrescription=Button(self.Buttonframe,font=('arial',12),text='Prescription',
                               width=23,bg="green",fg="white",padx=2,pady=6,command=self.show_record)
        btnPrescription.pack(side="left")
        
        btnPrescriptionData=Button(self.Buttonframe,text='Prescription Data',bg="blue",fg="white",font=('arial',12,'bold'),
                                   width=23,padx=2,pady=6,command=self.entry_details)
        btnPrescriptionData.pack(side="left")
        
        btnUpdate=Button(self.Buttonframe,font=('arial',12),text='Update',
                               width=23,bg="pink",fg="white",padx=2,pady=6,command=self.updateRecord)
        btnUpdate.pack(side="left")
        
        btnDelete=Button(self.Buttonframe,font=('arial',12),text='Delete',
                               width=23,bg="Red",fg="white",padx=2,pady=6,command=self.record_delete)
        btnDelete.pack(side="left")
        
        btnClear=Button(self.Buttonframe,font=('arial',12),text='Clear',
                               width=23,bg="green",fg="white",padx=2,pady=6,command=self.clear_record)
        btnClear.pack(side="left")
        
        btnExit=Button(self.Buttonframe,font=('arial',12),text='Exit',
                               width=23,bg="blue",fg="white",padx=2,pady=6,command=self.exit_appilication)
        btnExit.pack(side="left")
        
        
        
        
        

if __name__=="__main__":
    root=Tk()
    obj=Hospital(root)
    obj.buttonClick()
    root.mainloop()