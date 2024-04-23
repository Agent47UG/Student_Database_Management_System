import tkinter as tk
import mysql.connector

def Remove():
    top=tk.Tk()
    top.config(bg="#515a6e")
    top.geometry("1300x800")
    top.resizable(False, False)
    top.title("Remove Student")

    def f1():
        top.destroy()
    def delete():
        conn = mysql.connector.connect(host="localhost",user="Ujwal",password="12345",database="management_system")
        curr = conn.cursor()
        Uid = e1.get()

        sql = "select * from studentdata where uid = %s"
        curr.execute(sql,[(Uid)])
        results = curr.fetchall()

        if results:
            for i in results:
                curr.execute("DELETE FROM studentdata WHERE uid = " +str(e1.get()))
                conn.commit()
                l=tk.Label(main_frame,text="Student Removed Successfully!",font=("Typori",13),bg="#515a6e",fg="#cdff57").place(x=165,y=200)
        else:
            l=tk.Label(main_frame,text="Student Not Found!",font=("Typori",13),width=26,bg="#515a6e",fg="red").place(x=160,y=200)




    main_frame = tk.Frame(top,bd=5,bg="#515a6e",relief = tk.RIDGE)
    main_frame.place(x=350,y=150,width=600,height=400)

    l=tk.Label(main_frame,text="Please Enter A Correct UiD:",font=("Arial",17),bg="#515a6e",fg="white").place(x=150,y=50)
    e1=tk.Entry(main_frame)
    e1.place(x=190,y=120,width=210,height=26)
    b1=tk.Button(main_frame,text="Delete",font=("Ausion Personal Use",15),activebackground="#eb0000",activeforeground="white",command=delete).place(x=215,y=280,width=150,height=40)



    b1=tk.Button(top,text="Exit",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=f1).place(x=570,y=650,width=150,height=50)

    l=tk.Label(top,text="Remove Records!",font=("Lemon Milk",24),width=60,height=2,bg="#3b4252",fg="white").place(x=-35,y=0)

    top.mainloop()
