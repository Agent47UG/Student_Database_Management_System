import tkinter as tk
import mysql.connector

def Update():

    top=tk.Toplevel()
    top.config(bg="#515a6e")
    top.geometry("1300x800")
    top.resizable(False, False)
    top.title("Update Student")

    #------------------Variables
    fname1 = tk.StringVar()
    lname1 = tk.StringVar()
    email1 = tk.StringVar()
    contact1 = tk.StringVar()
    branch1 = tk.StringVar()
    year1 = tk.StringVar()

    def f1():
        top.destroy()
    def find():
        conn = mysql.connector.connect(host="localhost",user="Ujwal",password="12345",database="management_system")
        curr = conn.cursor()
        Uid = e.get()

        sql = "select * from studentdata where uid = %s"
        curr.execute(sql,[(Uid)])
        results = curr.fetchall()

        if results:
            for i in results:
                curr.execute("SELECT * FROM studentdata WHERE UID =" + str(e.get()))
                rows = curr.fetchall()

                for row in rows:
                    fname1.set(row[1])
                    lname1.set(row[2])
                    email1.set(row[3])
                    contact1.set(row[4])
                    branch1.set(row[5])
                    year1.set(row[6])
                l=tk.Label(top,text="Student Found!",font=("Typori",13),width=26,bg="#515a6e",fg="#cdff57").place(x=535,y=350)

        else:
            l=tk.Label(top,text="Student Not Found!",font=("Typori",13),width=26,bg="#515a6e",fg="red").place(x=535,y=350)
            fname1.set("")
            lname1.set("")
            email1.set("")
            contact1.set("")
            branch1.set("")
            year1.set("")

        conn.close()

    def update_data():
        conn = mysql.connector.connect(host="localhost",user="Ujwal",password="12345",database="management_system")
        curr = conn.cursor()
        Uid = e.get()

        f_name = e1.get()
        l_name = e2.get()
        email = e3.get()
        mobile = e4.get()
        branch = e5.get()
        year = e6.get()

        curr.execute("update studentdata set F_Name=%s, L_Name=%s, Email=%s, Contact=%s, Branch=%s, Year=%s where uid=%s",(f_name,l_name,email,mobile,branch,year,Uid))
        conn.commit()
        conn.close()
        l=tk.Label(main_frame,text="Student Updated Successfully!",font=("Typori",12),bg="#515a6e",fg="#cdff57").place(x=520,y=290)

    l=tk.Label(top,text="Please Enter A Correct UiD:",font=("Arial",17),bg="#515a6e",fg="white").place(x=520,y=130)
    e=tk.Entry(top)
    e.place(x=560,y=190,width=210,height=26)
    b1=tk.Button(top,text="Find!",font=("Ausion Personal Use",14),activebackground="#515a6e",activeforeground="white",command=find).place(x=590,y=280,width=150,height=33)

    #---------------------Main Frame
    main_frame = tk.Frame(top,bd=5,bg="#515a6e",relief = tk.RIDGE)
    main_frame.place(x=10,y=380,width=1280,height=410)
    l=tk.Label(main_frame,text="First Name :",font=("Arial",17),bg="#515a6e",fg="white").place(x=100,y=80)
    l=tk.Label(main_frame,text="Last Name :",font=("Arial",17),bg="#515a6e",fg="white").place(x=760,y=80)
    l=tk.Label(main_frame,text="Email ID :",font=("Arial",17),bg="#515a6e",fg="white").place(x=100,y=150)
    l=tk.Label(main_frame,text="Contact No. :",font=("Arial",17),bg="#515a6e",fg="white").place(x=760,y=150)
    l=tk.Label(main_frame,text="Branch :",font=("Arial",17),bg="#515a6e",fg="white").place(x=100,y=220)
    l=tk.Label(main_frame,text="Year :",font=("Arial",17),bg="#515a6e",fg="white").place(x=760,y=220)

    e1=tk.Entry(main_frame,textvariable = fname1)
    e1.place(x=270,y=86,width=210,height=26)
    e2=tk.Entry(main_frame,textvariable = lname1)
    e2.place(x=950,y=86,width=210,height=26)
    e3=tk.Entry(main_frame,textvariable = email1)
    e3.place(x=270,y=150,width=210,height=26)
    e4=tk.Entry(main_frame,textvariable = contact1)
    e4.place(x=950,y=150,width=210,height=26)
    e5=tk.Entry(main_frame,textvariable = branch1)
    e5.place(x=270,y=220,width=210,height=26)
    e6=tk.Entry(main_frame,textvariable = year1)
    e6.place(x=950,y=220,width=210,height=26)

    b1=tk.Button(main_frame,text="Update",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=update_data).place(x=470,y=330,width=130,height=40)
    b1=tk.Button(main_frame,text="Exit",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=f1).place(x=690,y=330,width=130,height=40)



    l=tk.Label(top,text="Update Records!",font=("Lemon Milk",24),width=60,height=2,bg="#3b4252",fg="white").place(x=-35,y=0)
    top.mainloop()
