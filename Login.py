import tkinter as tk
import mysql.connector
import Registration
import Home



def t1(event):
    Registration.registration()

def Login():
    top=tk.Tk()
    top.config(bg="#3b4252")
    top.geometry("400x400")
    top.resizable(False, False)
    top.title("Login Page")

    def log_in():
        mydb=mysql.connector.connect(host="localhost",user="Ujwal",password="12345",database="management_system")
        mycur=mydb.cursor()
        username = e1.get()
        passwrd = e2.get()
        sql = "select * from userdata where username = %s and password = %s"
        mycur.execute(sql,[(username),(passwrd)])
        results = mycur.fetchall()

        if results:
            for i in results:
                l=tk.Label(top,text="Login Successfull!",font=("Noto Sans",14),bg="#3b4252",fg="white").place(x=120,y=300)
                l=tk.Label(top,text="",width=50,font=("Noto Sans",10),bg="#3b4252",fg="white").place(x=60,y=330)
                Home.Home(username)

        else:
            l=tk.Label(top,text="Login Failed",font=("Noto Sans",14),bg="#3b4252",fg="red").place(x=140,y=300)
            l=tk.Label(top,text="Please Enter Correct Username or Password",font=("Noto Sans",10),bg="#3b4252",fg="red").place(x=60,y=330)

    l=tk.Label(top,text="Login",font=("Bitstream Charter",15,"bold"),width=33,bg="#2e3440",fg="white").place(x=0,y=0)
    l=tk.Label(top,text="Username :",font=("Fira Sans Compressed",14),bg="#3b4252",fg="white").place(x=160,y=70)
    e1=tk.Entry(top)
    e1.place(x=115,y=105,width=170,height=21)
    l=tk.Label(top,text="Password:",font=("Fira Sans Compressed",14),bg="#3b4252",fg="white").place(x=160,y=150)
    e2=tk.Entry(top)
    e2.place(x=115,y=185,width=170,height=21)

    b1=tk.Button(top,text="Login!",bg="#3b4252",activebackground="#4c566a",activeforeground="white",fg="white",command=log_in).place(x=145,y=240,width=100,height=25)
    l1=tk.Label(top,text="New Here? Create a Account",font=("ariel",9),bg="#3b4252",fg="#e3e3e3")
    l1.place(x=220,y=380)
    l1.bind("<Button>", t1)

    top.mainloop()

Login()
