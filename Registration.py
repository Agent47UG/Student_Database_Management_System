import tkinter as tk
import mysql.connector

def registration():
    #---------------Tkinter Initialisation
    top=tk.Tk()
    top.config(bg="#3b4252")
    top.geometry("450x600")
    top.resizable(False, False)
    top.title("Registration Page")

    def register():
        username=e1.get()
        email=e2.get()
        contact=e3.get()
        passwrd=e4.get()
        #---------------Sql Initialisation
        mydb=mysql.connector.connect(host="localhost",user="Ujwal",password="12345",database="management_system")
        mycur=mydb.cursor()
        insert="INSERT INTO userdata VALUES(%s,%s,%s,%s)"
        mycur.execute(insert,(username,email,contact,passwrd))
        mydb.commit()
        l=tk.Label(top,text="Account Creation was Successfull!!",font=("ariel",8),bg="#3b4252",fg="white").place(x=130,y=500)

    #---------------GUI
    l=tk.Label(top,text="Registration Form",font=("Bitstream Charter",15,"bold"),width=38,bg="#2e3440",fg="white").place(x=0,y=0)
    l=tk.Label(top,text="Create a Account!",font=("Fira Sans",13,),bg="#3b4252",fg="white").place(x=160,y=50)
    l=tk.Label(top,text="Enter a Username :",font=("Fira Sans Compressed",14),bg="#3b4252",fg="white").place(x=160,y=110)
    e1=tk.Entry(top)
    e1.place(x=130,y=142,width=200,height=21)
    l=tk.Label(top,text="Enter a Email Address:",font=("Fira Sans Compressed",14),bg="#3b4252",fg="white").place(x=152,y=190)
    e2=tk.Entry(top)
    e2.place(x=130,y=222,width=200,height=21)
    l=tk.Label(top,text="Enter a Contact No.:",font=("Fira Sans Compressed",14),bg="#3b4252",fg="white").place(x=160,y=270)
    e3=tk.Entry(top)
    e3.place(x=130,y=302,width=200,height=21)
    l=tk.Label(top,text="Enter a Password :",font=("Fira Sans Compressed",14),bg="#3b4252",fg="white").place(x=165,y=350)
    e4=tk.Entry(top)
    e4.place(x=130,y=382,width=200,height=21)
    b1=tk.Button(top,text="Register!",bg="#3b4252",activebackground="#4c566a",activeforeground="white",fg="white",command=register).place(x=180,y=450,width=100,height=25)
    top.mainloop()
