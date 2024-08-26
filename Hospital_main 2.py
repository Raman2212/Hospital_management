from tkinter import*
from tkinter import ttk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvise=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.Patientname=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("Algerian",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ================================Dataframe=======================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        Dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",15,"bold"),text="Patient Information :")
        Dataframeleft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",15,"bold"),text="Prescription :")
        DataframeRight.place(x=990,y=5,width=500,height=350)

        # ================================Buttons frame=======================

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        # ================================Details frame=======================

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        # ================================DataframeLeft=======================

        lblNameTablet=Label(Dataframeleft,text="Name of Tablet:",font=("new times roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(Dataframeleft,textvariable=self.Nameoftablets,state="readonly",
                                   font=("new times roman",12,"bold"),
                                   width=33)
        comNametablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Allodipine","ativan")
        comNametablet.grid(row=0,column=1)

        lblref=Label(Dataframeleft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(Dataframeleft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(Dataframeleft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        noOfTabletsValues = [str(i) for i in range(1, 101)]  # You can modify the range as needed
        comNoOftablets = ttk.Combobox(Dataframeleft, textvariable=self.NumberofTablets, state="readonly",
                              font=("new times roman", 12, "bold"), width=33, values=noOfTabletsValues)
        comNoOftablets.grid(row=3, column=1)

        lblLot=Label(Dataframeleft,font=("arial",12,"bold"),text="Lots:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        self.calIssueDate = DateEntry(
            Dataframeleft,
            font=("arial", 13, "bold"),
            textvariable=self.Issuedate,
            width=33,
            date_pattern='dd-mm-yyyy'  # Format of the date
        )
        self.calIssueDate.grid(row=5, column=1)
        self.calIssueDate.set_date(date.today())

        lblExpDate=Label(Dataframeleft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        self.calExpDate = DateEntry(
            Dataframeleft,
            font=("arial", 13, "bold"),
            textvariable=self.ExpDate,
            width=33,
            date_pattern='dd-mm-yyyy'  # Format of the date
        )
        self.calExpDate.grid(row=6, column=1)
        self.calExpDate.set_date(date.today())

        lblDailyDose=Label(Dataframeleft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(Dataframeleft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.SideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(Dataframeleft,font=("arial",12,"bold"),text="Further Info:",padx=2,)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(Dataframeleft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(Dataframeleft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.StorageAdvise,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(Dataframeleft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(Dataframeleft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(Dataframeleft,font=("arial",12,"bold"),text="NHS Number",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.Patientname,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(Dataframeleft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        self.calDOB = DateEntry(
        Dataframeleft, 
        font=("arial", 13, "bold"), 
        textvariable=self.DateOfBirth, 
        width=33, 
        date_pattern='dd-mm-yyyy',  # Format of the date
        )
        self.calDOB.grid(row=7, column=3)
        self.calDOB.set_date(datetime.date.today())

        lblPatientAddress=Label(Dataframeleft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(Dataframeleft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

        # ================================Dataframeright=======================

        self.txtPresciption=Text(DataframeRight,font=("arial",12,"bold"),width=50,height=16,padx=2,pady=6)
        self.txtPresciption.grid(row=0,column=0)

        # ================================Buttons=======================


        btnPrescription=Button(Buttonframe,command=self.iPrescriptionDate,text="Add Presciption",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=0,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iprescription,text="Show Presciption Data",bg="green",fg="white",font=("arial",12,"bold"),width=25,height=0,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=25,height=0,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=24,height=0,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.iclear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=24,height=0,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iexit,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=21,height=0,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        # ================================Table=======================
        # ========================Scrollbar=======================

        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable", text="Name Of Tablet")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", lambda event: self.get_cursor(event))
        self.fetch_data()
        

    # ================================DataframeFunctionality=======================    
    def iPrescriptionDate(self):
        try:
            if self.Nameoftablets.get() == "" or self.ref.get() == "":
                messagebox.showerror("Error", "All fields are required")
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="Raman@7352#", database="mydata")
                if conn.is_connected():
                    print("SQL Connection established")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO hospital2(Nameoftablets,Reference_No,dose,Numbersoftablets,lot,issuedate,expdate,dailydose,storage,nhsnumber,patientname,DOB,patientaddress) value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvise.get(),
                    self.nhsNumber.get(),
                    self.Patientname.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")
        except mysql.connector.errors.IntegrityError as e:
            messagebox.showerror("Duplicate Entry", "This Reference No. already exists. Please use a different one.")
            print(f"Error: {e}")
    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Raman@7352#", database="mydata")
        if conn.is_connected():
         print("Update Connection established")
        my_cursor = conn.cursor()

        query = "UPDATE hospital2 SET Nameoftablets=%s, dose=%s, Numbersoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s WHERE Reference_No=%s"

        values = (
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvise.get(),
            self.nhsNumber.get(),
            self.Patientname.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get() 
        )

        my_cursor.execute(query, values)
        conn.commit()
        self.fetch_data()
        messagebox.showinfo("Success", "Record has been Successfully Updated")



    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Raman@7352#", database="mydata")
        if conn.is_connected():
            print("Fetch data Connection stablished")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from hospital2")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for item in rows:
                self.hospital_table.insert("", END, values=item)
            conn.commit()
        conn.close()
    

    def get_cursor(self, event):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvise.set(row[8])
        self.nhsNumber.set(row[9])
        self.Patientname.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iprescription(self):
       self.txtPresciption.delete(1.0, END)
       self.txtPresciption.insert(END,"Name of Tablets:\t\t\t" +self.Nameoftablets.get() +"\n")
       self.txtPresciption.insert(END,"Reference No:\t\t\t" + self.ref.get() +"\n")
       self.txtPresciption.insert(END,"Dose:\t\t\t" + self.Dose.get() +"\n")
       self.txtPresciption.insert(END,"Number Of Tablets:\t\t\t" + self.NumberofTablets.get() +"\n")
       self.txtPresciption.insert(END,"Lot:\t\t\t" + self.Lot.get() +"\n")
       self.txtPresciption.insert(END,"Issue Date:\t\t\t" +self.Issuedate.get() +"\n")
       self.txtPresciption.insert(END,"Exp Date:\t\t\t" + self.ExpDate.get() +"\n")
       self.txtPresciption.insert(END,"Daily DOse:\t\t\t" + self.DailyDose.get() +"\n")
       self.txtPresciption.insert(END,"Side Effects:\t\t\t" + self.SideEffect.get() +"\n")
       self.txtPresciption.insert(END,"Further Information:\t\t\t" +self.FurtherInformation.get() +"\n")
       self.txtPresciption.insert(END,"Storage Advice:\t\t\t" + self.StorageAdvise.get() +"\n")
       self.txtPresciption.insert(END,"Driving Using Machine:\t\t\t" + self.DrivingUsingMachine.get()+"\n")
       self.txtPresciption.insert(END,"PatientId:\t\t\t" + self.PatientId.get()+"\n")
       self.txtPresciption.insert(END,"NHSNumber:\t\t\t" + self.nhsNumber.get() +"\n")
       self.txtPresciption.insert(END,"Patient Name:\t\t\t" + self.Patientname.get() +"\n")
       self.txtPresciption.insert(END,"Date Of Birth\t\t\t" + self.DateOfBirth.get() +"\n")
       self.txtPresciption.insert(END,"Patient Address:\t\t\t" + self.PatientAddress.get()+"\n")

    def idelete(self):
       conn = mysql.connector.connect(host="localhost", username="root", password="Raman@7352#", database="mydata")
       if conn.is_connected():
            print("Delete Connection stablished")
            my_cursor = conn.cursor()
            query="delete from hospital2 where Reference_No=%s"
            value=(self.ref.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            conn.close()
            self.fetch_data()
            my_cursor.execute("Delete","Patient Has been Deleted")

    def iclear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvise.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.Patientname.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")

    def iexit(self):
        response = messagebox.askyesnocancel("Exit Confirmation", "Do you really want to exit?")

        if response is not None:
            if response:  
                self.root.destroy() 
            else: 
                messagebox.showinfo("Cancelled", "Exit cancelled.")
       





root = Tk()
ob = Hospital(root)
root.mainloop()