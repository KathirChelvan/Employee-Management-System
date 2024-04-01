from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database


db=Database("Employee.db")
root=Tk()
root.title("Employee Management System")
root.geometry("1366x768+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
desig=StringVar()
salary=StringVar()
email=StringVar()
gender=StringVar()
contact=StringVar()


#entries frame
entries_frame = Frame(root, bg="#000080")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=("Calibri",18,"bold"),bg="#000080",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20,sticky="w")
#name
lblName=Label(entries_frame,text="Name",font=("Calibri",16), bg="#000080", fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(entries_frame,textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")
#desig
lbldesig=Label(entries_frame,text="Designation",font=("Calibri",16), bg="#000080", fg="white")
lbldesig.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtdesig=Entry(entries_frame,textvariable=desig,font=("Calibri",16),width=30)
txtdesig.grid(row=1,column=3,padx=10,pady=10,sticky="w")
#sal
lblsal=Label(entries_frame,text="Salary",font=("Calibri",16), bg="#000080", fg="white")
lblsal.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtsal=Entry(entries_frame,textvariable=salary,font=("Calibri",16),width=30)
txtsal.grid(row=2,column=1,padx=10,pady=10,sticky="w")
#email
lblEmail=Label(entries_frame,text="Email",font=("Calibri",16), bg="#000080", fg="white")
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtEmail=Entry(entries_frame,textvariable=email,font=("Calibri",16),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky="w")
#gender
lblGender=Label(entries_frame,text="Gender",font=("Calibri",16), bg="#000080", fg="white")
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entries_frame,font=("calibri",16),width=28,textvariable=gender,state="readonly")
comboGender['values']=("Male", "Female")
comboGender.grid(row=3,column=1,padx=10,pady=10,sticky="w")
#contact
lblcontact=Label(entries_frame,text="Contact No",font=("Calibri",16), bg="#000080", fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtcontact=Entry(entries_frame,textvariable=contact,font=("Calibri",16),width=30)
txtcontact.grid(row=3,column=3,padx=10,pady=10,sticky="w")
#address
lblAddress=Label(entries_frame,text="Address",font=("Calibri",16),bg="#000080", fg="white")
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky="w")

txtAddress=Text(entries_frame,width=85,height=5,font=("calibri",16))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    #print(row)
    name.set(row[1])
    desig.set(row[2])
    salary.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0,END)
    txtAddress.insert(END, row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtName.get()=="" or txtdesig.get()=="" or txtsal.get()==""or txtEmail.get()=="" or comboGender.get()=="" or txtcontact.get()=="" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("error in Input","Please Fill All the Details")
        return
    db.insert(txtName.get(),txtdesig.get(),txtsal.get(),txtEmail.get(),comboGender.get(),txtcontact.get(),txtAddress.get(1.0, END))
    messagebox.showinfo("Success","Record Inserted")
    clearAll()
    displayAll()


def update_employee():
    if txtName.get() == "" or txtdesig.get() == "" or txtsal.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtcontact.get() == "" or txtAddress.get(1.0, END) == "":
        messagebox.showerror("error in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtdesig.get(), txtsal.get(), txtEmail.get(), comboGender.get(), txtcontact.get(),txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    displayAll()

def delete_employee():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():
    name.set("")
    desig.set("")
    salary.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)

btn_frame=Frame(entries_frame,bg="#000080")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")

btnAdd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=("Calibri",16,"bold"), bg="#16a085",bd=0, fg="white").grid(row=0,column=0)

btnEdit=Button(btn_frame,command=update_employee,text="Update Details",width=15,font=("Calibri",16,"bold"), bg="#ffa500",bd=0, fg="white").grid(row=0,column=1,padx=10)

btnDelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=("Calibri",16,"bold"), bg="#003300",bd=0, fg="white").grid(row=0,column=2,padx=10)

btnClear=Button(btn_frame,command=clearAll,text="Clear Details",width=15,font=("Calibri",16,"bold"), bg="red",bd=0, fg="white").grid(row=0,column=3,padx=10)


#tableframe
tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=480,width=1366,height=300)
style=ttk.Style()
style.configure("mystyle.Treeview", font=('calibri',18),rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('calibri',18),rowheight=50)

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=50)
tv.heading("2",text="Name")
tv.column("2",width=200)
tv.heading("3",text="Deisgnation")
tv.column("3",width=200)
tv.heading("4",text="Salary")
tv.column("4",width=150)
tv.heading("5",text="Email")
tv.column("5",width=200)
tv.heading("6",text="Gender")
tv.column("6",width=150)
tv.heading("7",text="Contact")
tv.column("7",width=150)
tv.heading("8",text="Address")
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)
#Table frame
displayAll()
root.mainloop()
