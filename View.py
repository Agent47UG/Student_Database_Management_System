import tkinter as tk
from tkinter import ttk
import mysql.connector

def View():
    top=tk.Tk()
    top.config(bg="#515a6e")
    top.geometry("1300x800")
    top.resizable(False, False)
    top.title("View Records")

    def fetch_data():
        conn = mysql.connector.connect(host="localhost",user="Ujwal",password="12345",database="management_system")
        curr = conn.cursor()
        curr.execute("SELECT * FROM studentdata")
        rows = curr.fetchall()
        if len(rows)!=0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('',tk.END,value=row)
                conn.commit()
            conn.close()

    def search_data():
        conn = mysql.connector.connect(host="localhost",user="Ujwal",password="12345",database="management_system")
        curr = conn.cursor()

        num = str(e1.get())
        if(num != ""):
            curr.execute("SELECT * FROM studentdata WHERE UID =" + str(e1.get()))
            rows=curr.fetchall()
            if len(rows)!=0:
                student_table.delete(*student_table.get_children())
                for row in rows:
                    student_table.insert('',tk.END,value=row)
                    conn.commit()
                conn.close()
        else:
            curr.execute("SELECT * FROM studentdata")
            rows = curr.fetchall()
            if len(rows)!=0:
                student_table.delete(*student_table.get_children())
                for row in rows:
                    student_table.insert('',tk.END,value=row)
                    conn.commit()
                conn.close()


    def f1():
        top.destroy()


    data_frame = tk.Frame(top,bd=12,bg="#515a6e",relief = tk.FLAT)
    data_frame.place(x=50,y=100,width=1200,height=600)

    Table_frame = tk.Frame(data_frame,bg="#515a6e",bd=1,relief=tk.FLAT)
    Table_frame.pack(fill=tk.BOTH,expand = True)

    y_scroll = tk.Scrollbar(Table_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(Table_frame,orient=tk.HORIZONTAL)

    student_table = ttk.Treeview(Table_frame, columns=("UID","First Name","Last Name","Email","Contact","Branch","Year"),yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command = student_table.yview)
    x_scroll.config(command = student_table.xview)
    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    student_table.heading("UID", text="UID")
    student_table.heading("First Name", text="First Name")
    student_table.heading("Last Name", text="Last Name")
    student_table.heading("Email", text="Email")
    student_table.heading("Contact", text="Contact")
    student_table.heading("Branch", text="Branch")
    student_table.heading("Year", text="Year")

    student_table['show'] = 'headings'

    student_table.column("UID",width=20)
    student_table.column("First Name", width=100)
    student_table.column("Last Name", width=100)
    student_table.column("Email", width=100)
    student_table.column("Contact", width=100)
    student_table.column("Branch", width=100)
    student_table.column("Year",width=100)
    student_table.pack(fill=tk.BOTH, expand = True)

    fetch_data()


    e1=tk.Entry(top)
    e1.place(x=500,y=735,width=210,height=30)
    l=tk.Label(top,text="Search By UID:",font=("Arial",14),bg="#515a6e",fg="white").place(x=350,y=738)
    l=tk.Label(top,text="View Records!",font=("Lemon Milk",24),width=60,height=2,bg="#3b4252",fg="white").place(x=-35,y=0)
    b1=tk.Button(top,text="Exit",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=f1).place(x=1090,y=730,width=150,height=40)
    b1=tk.Button(top,text="Search",font=("Ausion Personal Use",15),activebackground="#515a6e",activeforeground="white",command=search_data).place(x=870,y=730,width=150,height=40)

    top.mainloop()
