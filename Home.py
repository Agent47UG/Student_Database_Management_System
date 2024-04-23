import tkinter as tk
import Add
import View
import Update
import Remove


def Home(user):
    top=tk.Tk()
    top.config(bg="#515a6e")
    top.geometry("900x600")
    top.resizable(False, False)
    top.title("Student Database Management System")

    def f1():
        Add.Add()
    def f2():
        View.View()
    def f3():
        Update.Update()
    def f4():
        Remove.Remove()
    def f5():
        top.destroy()



    l=tk.Label(top,text="Student Database Management System",font=("Lemon Milk",24),width=50,height=2,bg="#3b4252",fg="white").place(x=-100,y=0)
    l=tk.Label(top,text="Welcome "+user+"!",font=("Typori",13),bg="#515a6e",fg="#cdff57").place(x=380,y=120)

    b1=tk.Button(top,text="Add Records",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=f1).place(x=190,y=210,width=150,height=50)
    b1=tk.Button(top,text="View Records",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=f2).place(x=560,y=210,width=150,height=50)
    b1=tk.Button(top,text="Update Records",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=f3).place(x=190,y=350,width=150,height=50)
    b1=tk.Button(top,text="Remove Records",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=f4).place(x=560,y=350,width=150,height=50)
    b1=tk.Button(top,text="Log Out!",font=("Ausion Personal Use",15),activebackground="#eb0000",activeforeground="white",command=f5).place(x=377,y=460,width=150,height=50)

    l=tk.Label(top,text="By Ujwal Ghodeswar",font=("Typori",13),bg="#515a6e",fg="white").place(x=730,y=576)



    top.mainloop()
