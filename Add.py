import tkinter as tk
import mysql.connector

def Add():
    top=tk.Tk()
    top.config(bg="#515a6e")
    top.geometry("1300x800")
    top.resizable(False, False)
    top.title("Add Student")

    def f1():
        top.destroy()

    def clear_text():
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
            e5.delete(0, 'end')
            e6.delete(0, 'end')

    def add_student():
        f_name = e1.get()
        l_name = e2.get()
        email = e3.get()
        mobile = e4.get()
        branch = e5.get()
        year = e6.get()

        mydb=mysql.connector.connect(host="localhost",user="Ujwal",password="12345",database="management_system")
        mycur=mydb.cursor()
        insert="INSERT INTO studentdata(F_Name, L_Name, Email, Contact, Branch, Year) VALUES(%s,%s,%s,%s,%s,%s)"
        mycur.execute(insert,(f_name,l_name,email,mobile,branch,year))
        mydb.commit()
        l=tk.Label(top,text="Student Added Successfully!",font=("Typori",15),bg="#515a6e",fg="#cdff57").place(x=335,y=605)
        clear_text()

    l=tk.Label(top,text="Add Student!",font=("Lemon Milk",24),width=60,height=2,bg="#3b4252",fg="white").place(x=-35,y=0)

    l=tk.Label(top,text="First Name :",font=("Arial",18),bg="#515a6e",fg="white").place(x=200,y=200)
    l=tk.Label(top,text="Last Name :",font=("Arial",18),bg="#515a6e",fg="white").place(x=730,y=200)
    l=tk.Label(top,text="Email ID :",font=("Arial",18),bg="#515a6e",fg="white").place(x=200,y=300)
    l=tk.Label(top,text="Contact No. :",font=("Arial",18),bg="#515a6e",fg="white").place(x=730,y=300)
    l=tk.Label(top,text="Branch :",font=("Arial",18),bg="#515a6e",fg="white").place(x=200,y=400)
    l=tk.Label(top,text="Year :",font=("Arial",18),bg="#515a6e",fg="white").place(x=730,y=400)

    e1=tk.Entry(top)
    e1.place(x=365,y=203,width=210,height=26)
    e2=tk.Entry(top)
    e2.place(x=900,y=203,width=210,height=26)
    e3=tk.Entry(top)
    e3.place(x=365,y=303,width=210,height=26)
    e4=tk.Entry(top)
    e4.place(x=900,y=303,width=210,height=26)
    e5=tk.Entry(top)
    e5.place(x=365,y=403,width=210,height=26)
    e6=tk.Entry(top)
    e6.place(x=900,y=403,width=210,height=26)

    b1=tk.Button(top,text="Add",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=add_student).place(x=740,y=600,width=150,height=50)
    b1=tk.Button(top,text="Exit",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=f1).place(x=960,y=600,width=150,height=50)

    top.mainloop()
