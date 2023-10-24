# ==================imports===================
import sqlite3
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from tkinter.font import BOLD
import tkinter as tk
from datetime import date
from tkinter import scrolledtext as tkst
# ============================================

root = Tk()
root.geometry("1366x768")
root.title("ChurrasqueriaAPP")

#Definición de variables globales
user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()

#Se establece conexión a una base de datos SQLite
with sqlite3.connect("./Database/store.db") as db:
    cur = db.cursor()

def random_emp_id(stringLength):
    Digits = string.digits
    strr=''.join(random.choice(Digits) for i in range(stringLength-5))
    return ('E'+strr)

def valid_phone(phn):
    if re.match(r"[678]\d{7}$", phn):
        return True
    return False

def valid_ci(aad):
    if aad.isdigit() and len(aad)==8:
        return True
    return False

def salir():
            root.destroy()

class login_page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("ChurrasqueriaAPP(ADMIN)")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/admin_login.png")
        self.label1.configure(image=self.img)
        

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.373, rely=0.273, width=374, height=24)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=user)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.373, rely=0.384, width=374, height=24)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(textvariable=passwd)

        self.button1 = Button(root)
        self.button1.place(relx=0.366, rely=0.685, width=356, height=43)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="palevioletred")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#d46c91")
        self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Inicio de sesion""")
        self.button1.configure(command=self.login)


        self.button2 = Button(root)
        self.button2.place(relx=0.366, rely=0.785, width=356, height=43)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="palevioletred")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#d46c91")
        self.button2.configure(font="-family {Poppins SemiBold} -size 20")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Salir""")
        self.button2.configure(command=salir)

    def login(self, Event=None):
        username = user.get()
        password = passwd.get()

        with sqlite3.connect("./Database/store.db") as db:
            cur = db.cursor()
        find_user = "SELECT * FROM employee WHERE emp_id = ? and password = ?"
        cur.execute(find_user, [username, password])
        results = cur.fetchall()
        if results:
            if results[0][6]=="Admin":
                messagebox.showinfo("Inicio de Sesión", " Exitosa.")
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)

                root.withdraw()
                global adm
                global page2
                adm = Toplevel()
                page2 = Admin_Page(adm)
                #page2.time()
                adm.protocol("WM_DELETE_WINDOW", exitt)
                adm.mainloop()
            else:
                messagebox.showerror("Oops!!", "Error: Tú no eres Adm.")

        else:
            messagebox.showerror("Error", "Usuario y/o contraseña: Incorrecta.")
            page1.entry2.delete(0, END)

    
def exitt():
    sure = messagebox.askyesno("SALIDA","Estás seguro de salir?", parent=root)
    if sure == True:
        adm.destroy()
        root.destroy()

def inventory():
    adm.withdraw()
    global inv
    global page3
    inv = Toplevel()
    page3 = Inventory(inv)
    page3.time()
    inv.protocol("WM_DELETE_WINDOW", exitt)
    inv.mainloop()


def employee():
    adm.withdraw()
    global emp
    global page5
    emp = Toplevel()
    page5 = Employee(emp)
    page5.time()
    emp.protocol("WM_DELETE_WINDOW", exitt)
    emp.mainloop()


def invoices():
    adm.withdraw()
    global invoice
    invoice = Toplevel()
    page7 = Invoice(invoice)
    page7.time()
    invoice.protocol("WM_DELETE_WINDOW", exitt)
    invoice.mainloop()

def about():
    pass
#------funciones menu
def menu1 ():
    inv.destroy()
    employee()

def menu2():
    inv.destroy()
    invoices()

def menu3():
    emp.destroy()
    inventory()
    
def menu4():
    emp.destroy()
    invoices()

def menu5():
    invoice.destroy()
    inventory()
def menu6():
    invoice.destroy()
    employee()
    



class Admin_Page:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Modo: ADMIN")

        self.label1 = Label(adm)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/admin.png")
        self.label1.configure(image=self.img)

        self.message = Label(adm)
        self.message.place(relx=0.046, rely=0.056, width=62, height=30)
        self.message.configure(font="-family {Poppins} -size 12")
        self.message.configure(foreground="#ffffff")
        self.message.configure(background="#383c52")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.button1 = Button(adm)
        self.button1.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#d46c91")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Cerrar""")
        self.button1.configure(command=self.Logout)

        self.button2 = Button(adm)
        self.button2.place(relx=0.14, rely=0.508, width=146, height=63)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#ffffff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#333333")
        self.button2.configure(background="#ffffff")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Inventario""")
        self.button2.configure(command=inventory)

        self.button3 = Button(adm)
        self.button3.place(relx=0.338, rely=0.508, width=146, height=63)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#ffffff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#333333")
        self.button3.configure(background="#ffffff")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Personal""")
        self.button3.configure(command=employee)


        self.button4 = Button(adm)
        self.button4.place(relx=0.536, rely=0.508, width=146, height=63)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#ffffff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#333333")
        self.button4.configure(background="#ffffff")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Facturas""")
        self.button4.configure(command=invoices)


       

    def Logout(self):
        sure = messagebox.askyesno("Cerrar", "Estás seguro de salir?", parent=adm)
        if sure == True:
            adm.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class Inventory:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Inventario")

        self.label1 = Label(inv)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/inventory.png")
        self.label1.configure(image=self.img)

        self.message = Label(inv)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(inv)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(inv)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(inv)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="palevioletred")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#d46c91")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""BUSCAR""")
        self.button1.configure(command=self.search_product)

        self.button2 = Button(inv)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="palevioletred")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#d46c91")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Cerrar""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(inv)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="palevioletred")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#d46c91")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""AÑADIR""")
        self.button3.configure(command=self.add_product)

        self.button4 = Button(inv)
        self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="palevioletred")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#d46c91")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""ACTUALIZAR PRODUCTO""")
        self.button4.configure(command=self.update_product)

        self.button5 = Button(inv)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="palevioletred")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#d46c91")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""ELIMINAR PRODUCTO""")
        self.button5.configure(command=self.delete_product)

        self.button6 = Button(inv)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="palevioletred")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#d46c91")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Salir""")
        self.button6.configure(command=self.Exit)
         #---menu---
        self.menu1 = Button(inv)
        self.menu1.place(relx=0.0, rely=0.0, width=86, height=20)
        self.menu1.configure(relief="flat",overrelief="flat",activebackground="mistyrose",cursor="hand2",foreground="black",background="#d46c91",font=("-family {Poppins SemiBold} -size 10"))
        self.menu1.configure(borderwidth="2")
        self.menu1.configure(text="IMVENTARIO")
       


        self.menu2 = Button(inv)
        self.menu2.place(relx=0.065, rely=0.0, width=86, height=20)
        self.menu2.configure(relief="flat",overrelief="flat",activebackground="palevioletred",cursor="hand2",foreground="#ffffff",background="#d46c91",font=("-family {Poppins SemiBold} -size 10"))
        self.menu2.configure(borderwidth="2")
        self.menu2.configure(text="EMPLEADOS")
        self.menu2.configure(command=menu1)



        self.menu2 = Button(inv)
        self.menu2.place(relx=0.130, rely=0.0, width=86, height=20)
        self.menu2.configure(relief="flat",overrelief="flat",activebackground="palevioletred",cursor="hand2",foreground="#ffffff",background="#d46c91",font=("-family {Poppins SemiBold} -size 10"))
        self.menu2.configure(borderwidth="2")
        self.menu2.configure(text="""FACTURAS""")
        self.menu2.configure(command=menu2)



        #--------------------------------

        self.scrollbarx = Scrollbar(inv, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(inv, orient=VERTICAL)
        self.tree = ttk.Treeview(inv)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Product ID",
                "Name",
                "Category",
                "Sub-Category",
                "In Stock",
                "MRP",
                "Cost Price",
                "Vendor No.",
            )
        )

        self.tree.heading("Product ID", text="ID de Producto", anchor=W)
        self.tree.heading("Name", text="Nombre", anchor=W)
        self.tree.heading("Category", text="Categoría", anchor=W)
        self.tree.heading("Sub-Category", text="Sub-Categoría", anchor=W)
        self.tree.heading("In Stock", text="En Stock", anchor=W)
        self.tree.heading("MRP", text="P. de Compra", anchor=W)
        self.tree.heading("Cost Price", text="P. de Venta ", anchor=W)
        self.tree.heading("Vendor No.", text="Vendor No.", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)
        self.tree.column("#8", stretch=NO, minwidth=0, width=100)

        self.DisplayData()

    def DisplayData(self):
        cur.execute("SELECT * FROM raw_inventory")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    def search_product(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        try:
            to_search = int(self.entry1.get())
        except ValueError:
            messagebox.showerror("Oops!!", "ID de Producto invalidop.", parent=inv)
        else:
            for search in val:
                if search==to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Éxito!", "Product ID: {} encontrado.".format(self.entry1.get()), parent=inv)
                    break
            else: 
                messagebox.showerror("Oops!", "Product ID: {} no encontrado.".format(self.entry1.get()), parent=inv)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_product(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirmar", "Estás seguro de querer eliminar lo seleccionado?", parent=inv)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%8==0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    delete = "DELETE FROM raw_inventory WHERE product_id = ?"
                    cur.execute(delete, [k])
                    db.commit()

                messagebox.showinfo("Hecho", "Producto eliminado.", parent=inv)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
        else:
            messagebox.showerror("Error!!","Por favor selecciona un producto.", parent=inv)

    def update_product(self):
        if len(self.sel)==1:
            global p_update
            p_update = Toplevel()
            page9 = Update_Product(p_update)
            page9.time()
            p_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global valll
            valll = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    valll.append(j)

            page9.entry1.insert(0, valll[1])
            page9.entry2.insert(0, valll[2])
            page9.entry3.insert(0, valll[4])
            page9.entry4.insert(0, valll[5])
            page9.entry6.insert(0, valll[3])
            page9.entry7.insert(0, valll[6])
            page9.entry8.insert(0, valll[7])


        elif len(self.sel)==0:
            messagebox.showerror("Error","Selecciona un producto para actualizar", parent=inv)
        else:
            messagebox.showerror("Error","Solo puedes actualizar un producto a la vez.", parent=inv)

        p_update.mainloop()

    

    def add_product(self):
        global p_add
        global page4
        p_add = Toplevel()
        page4 = add_product(p_add)
        page4.time()
        p_add.mainloop()

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Salir","Estás sehuro de salir?", parent=inv)
        if sure == True:
            inv.destroy()
            adm.deiconify()

    def ex2(self):
        sure = messagebox.askyesno("Salir","Estás seguro de salir?", parent=p_update)
        if sure == True:
            p_update.destroy()
            inv.deiconify()



    def Logout(self):
        sure = messagebox.askyesno("Cerrar", "Estás seguro de cerrar sesión?")
        if sure == True:
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class add_product:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Añadir Producto")

        self.label1 = Label(p_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/add_product.png")
        self.label1.configure(image=self.img)

        self.clock = Label(p_add)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(p_add)
        self.entry1.place(relx=0.132, rely=0.296, width=996, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(p_add)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")

        self.r2 = p_add.register(self.testint)

        self.entry3 = Entry(p_add)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry4 = Entry(p_add)
        self.entry4.place(relx=0.132, rely=0.646, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
       

        self.entry6 = Entry(p_add)
        self.entry6.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
       

        self.entry7 = Entry(p_add)
        self.entry7.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry7.configure(font="-family {Poppins} -size 12")
        self.entry7.configure(relief="flat")
       

        self.entry8 = Entry(p_add)
        self.entry8.place(relx=0.527, rely=0.646, width=374, height=30)
        self.entry8.configure(font="-family {Poppins} -size 12")
        self.entry8.configure(relief="flat")
        self.entry8.configure(validate="key", validatecommand=(self.r2, "%P"))
       

        self.button1 = Button(p_add)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="palevioletred")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#d46c91")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""ADD""")
        self.button1.configure(command=self.add)

        self.button2 = Button(p_add)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="palevioletred")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#d46c91")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)

    def add(self):
        pqty = self.entry3.get()
        pcat = self.entry2.get()  
        pmrp = self.entry4.get()  
        pname = self.entry1.get()  
        psubcat = self.entry6.get()  
        pcp = self.entry7.get()  
        pvendor = self.entry8.get()  
       

        if pname.strip():
            if pcat.strip():
                if psubcat.strip():
                    if pqty:
                        if pcp:
                            try:
                                float(pcp)
                            except ValueError:
                                messagebox.showerror("Oops!", "Precio inválido.", parent=p_add)
                            else:
                                if pmrp:
                                    try:
                                        float(pmrp)
                                    except ValueError:
                                        messagebox.showerror("Oops!", "Inválido.", parent=p_add)
                                    else:
                                        if valid_phone(pvendor):
                                            with sqlite3.connect("./Database/store.db") as db:
                                                cur = db.cursor()
                                            insert = (
                                                        "INSERT INTO raw_inventory(product_name, product_cat, product_subcat, stock, mrp, cost_price, vendor_phn) VALUES(?,?,?,?,?,?,?)"
                                                    )
                                            cur.execute(insert, [pname, pcat, psubcat, int(pqty), float(pmrp), float(pcp), pvendor])
                                            db.commit()
                                            messagebox.showinfo("Hecho", "Producto añadido exitosamente.", parent=p_add)
                                            p_add.destroy()
                                            page3.tree.delete(*page3.tree.get_children())
                                            page3.DisplayData()
                                            p_add.destroy()
                                        else:
                                            messagebox.showerror("Oops!", "Numero de teléfono inválido.", parent=p_add)
                                else:
                                    messagebox.showerror("Oops!", "Introduzca un precio válido", parent=p_add)
                        else:
                            messagebox.showerror("Oops!", "Introduzca una cifra válida.", parent=p_add)
                    else:
                        messagebox.showerror("Oops!", "Introduzca una cantidad correcta.", parent=p_add)
                else:
                    messagebox.showerror("Oops!", "Introduzca sub-categoria.", parent=p_add)
            else:
                messagebox.showerror("Oops!", "Introduzca categoria del producto.", parent=p_add)
        else:
            messagebox.showerror("Oops!", "Introduzca el Nombre del Producto", parent=p_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


class Update_Product:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Añadir Producto")

        self.label1 = Label(p_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/update_product.png")
        self.label1.configure(image=self.img)

        self.clock = Label(p_update)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(p_update)
        self.entry1.place(relx=0.132, rely=0.296, width=996, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(p_update)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")

        self.r2 = p_update.register(self.testint)

        self.entry3 = Entry(p_update)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry4 = Entry(p_update)
        self.entry4.place(relx=0.132, rely=0.646, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
       

        self.entry6 = Entry(p_update)
        self.entry6.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
       

        self.entry7 = Entry(p_update)
        self.entry7.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry7.configure(font="-family {Poppins} -size 12")
        self.entry7.configure(relief="flat")
       

        self.entry8 = Entry(p_update)
        self.entry8.place(relx=0.527, rely=0.646, width=374, height=30)
        self.entry8.configure(font="-family {Poppins} -size 12")
        self.entry8.configure(relief="flat")
       

        self.button1 = Button(p_update)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="palevioletred")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#d46c91")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""ACTUALIZAR""")
        self.button1.configure(command=self.update)

        self.button2 = Button(p_update)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="palevioletred")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#d46c91")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""LIMPIAR""")
        self.button2.configure(command=self.clearr)

    def update(self):
        pqty = self.entry3.get()
        pcat = self.entry2.get()  
        pmrp = self.entry4.get()  
        pname = self.entry1.get()  
        psubcat = self.entry6.get()  
        pcp = self.entry7.get()  
        pvendor = self.entry8.get()  
       

        if pname.strip():
            if pcat.strip():
                if psubcat.strip():
                    if pqty:
                        if pcp:
                            try:
                                float(pcp)
                            except ValueError:
                                messagebox.showerror("Oops!", "Precio Inválido.", parent=p_update)
                            else:
                                if pmrp:
                                    try:
                                        float(pmrp)
                                    except ValueError:
                                        messagebox.showerror("Oops!", "Invalido.", parent=p_update)
                                    else:
                                        if valid_phone(pvendor):
                                            product_id = valll[0]
                                            with sqlite3.connect("./Database/store.db") as db:
                                                cur = db.cursor()
                                            update = (
                                            "UPDATE raw_inventory SET product_name = ?, product_cat = ?, product_subcat = ?, stock = ?, mrp = ?, cost_price = ?, vendor_phn = ? WHERE product_id = ?"
                                            )
                                            cur.execute(update, [pname, pcat, psubcat, int(pqty), float(pmrp), float(pcp), pvendor, product_id])
                                            db.commit()
                                            messagebox.showinfo("Exitosamente", "Producto actualizado.", parent=p_update)
                                            valll.clear()
                                            Inventory.sel.clear()
                                            page3.tree.delete(*page3.tree.get_children())
                                            page3.DisplayData()
                                            p_update.destroy()
                                        else:
                                            messagebox.showerror("Oops!", "Número de teléfono inválido.", parent=p_update)
                                else:
                                    messagebox.showerror("Oops!", "Introducza MRP.", parent=p_update)
                        else:
                            messagebox.showerror("Oops!", "Introduzca Precio Válido.", parent=p_update)
                    else:
                        messagebox.showerror("Oops!", "Introduzca cantidad de: Producto.", parent=p_update)
                else:
                    messagebox.showerror("Oops!", "Introduzca: sub-categoria.", parent=p_update)
            else:
                messagebox.showerror("Oops!", "Introduzca: Categoria.", parent=p_update)
        else:
            messagebox.showerror("Oops!", "Introduzca: Nombre del Producto", parent=p_update)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)
    


class Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Employee Management")

        self.label1 = Label(emp)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/employee.png")
        self.label1.configure(image=self.img)

        self.message = Label(emp)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(emp)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(emp)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(emp)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="palevioletred")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#d46c91")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Buscar""")
        self.button1.configure(command=self.search_emp)

        self.button2 = Button(emp)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="palevioletred")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#d46c91")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Cerrar""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(emp)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="palevioletred")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#d46c91")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""AGREGAR EMPLEADO""")
        self.button3.configure(command=self.add_emp)

        self.button4 = Button(emp)
        self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="palevioletred")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#d46c91")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""ACTUALIZAR EMPLEADO""")
        self.button4.configure(command=self.update_emp)

        self.button5 = Button(emp)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="palevioletred")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#d46c91")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""ELIMINAR EMPLEADO""")
        self.button5.configure(command=self.delete_emp)

        self.button6 = Button(emp)
        self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="palevioletred")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#d46c91")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""SALIR""")
        self.button6.configure(command=self.Exit)
        #---------------------menu---------------------
        
        #---menu---
        self.menu1 = Button(emp)
        self.menu1.place(relx=0.0, rely=0.0, width=86, height=20)
        self.menu1.configure(relief="flat",overrelief="flat",activebackground="palevioletred",cursor="hand2",foreground="#ffffff",background="#d46c91",font=("-family {Poppins SemiBold} -size 10"))
        self.menu1.configure(borderwidth="2")
        self.menu1.configure(text="IMVENTARIO")
        self.menu1.configure(command=menu3)
       


        self.menu2 = Button(emp)
        self.menu2.place(relx=0.065, rely=0.0, width=86, height=20)
        self.menu2.configure(relief="flat",overrelief="flat",activebackground="mistyrose",cursor="hand2",foreground="black",background="#d46c91",font=("-family {Poppins SemiBold} -size 10"))
        self.menu2.configure(borderwidth="2")
        self.menu2.configure(text="EMPLEADOS")
     



        self.menu3 = Button(emp)
        self.menu3.place(relx=0.130, rely=0.0, width=86, height=20)
        self.menu3.configure(relief="flat",overrelief="flat",activebackground="palevioletred",cursor="hand2",foreground="#ffffff",background="#d46c91",font=("-family {Poppins SemiBold} -size 10"))
        self.menu3.configure(borderwidth="2")
        self.menu3.configure(text="""FACTURAS""")
        self.menu3.configure(command=menu4)
      



        #--------------------------------
        #---------------------menu--------------------

        self.scrollbarx = Scrollbar(emp, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(emp, orient=VERTICAL)
        self.tree = ttk.Treeview(emp)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Employee ID",
                "Employee Name",
                "Contact No.",
                "Address",
                "Aadhar No.",
                "Password",
                "Designation"
            )
        )

        self.tree.heading("Employee ID", text="ID", anchor=W)
        self.tree.heading("Employee Name", text="Nombre", anchor=W)
        self.tree.heading("Contact No.", text="Número Contacto", anchor=W)
        self.tree.heading("Address", text="Dirección", anchor=W)
        self.tree.heading("Aadhar No.", text="CI", anchor=W)
        self.tree.heading("Password", text="Contraseña", anchor=W)
        self.tree.heading("Designation", text="Cargo", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=260)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=198)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)

        self.DisplayData()

    def DisplayData(self):
        cur.execute("SELECT * FROM employee")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    def search_emp(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Exito", " ID Personal: {} encontrado.".format(self.entry1.get()), parent=emp)
                break
        else: 
            messagebox.showerror("Oops!!", "ID personal: {} no encontrado.".format(self.entry1.get()), parent=emp)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_emp(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirmar", "Estás seguro de eliminar al personal seleccionados?", parent=emp)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%7==0:
                        to_delete.append(val[j])
                
                flag = 1

                for k in to_delete:
                    if k=="EMP0000":
                        flag = 0
                        break
                    else:
                        delete = "DELETE FROM employee WHERE emp_id = ?"
                        cur.execute(delete, [k])
                        db.commit()

                if flag==1:
                    messagebox.showinfo("Hecho", "Personal Eliminado.", parent=emp)
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())
                    self.DisplayData()
                else:
                    messagebox.showerror("Error!!","No puedes Eliminar al Administrador.")
        else:
            messagebox.showerror("Error!!","Selecciona al menos 1.", parent=emp)

    def update_emp(self):
        
        if len(self.sel)==1:
            global e_update
            e_update = Toplevel()
            page8 = Update_Employee(e_update)
            page8.time()
            e_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)
            
            page8.entry1.insert(0, vall[1])
            page8.entry2.insert(0, vall[2])
            page8.entry3.insert(0, vall[4])
            page8.entry4.insert(0, vall[6])
            page8.entry5.insert(0, vall[3])
            page8.entry6.insert(0, vall[5])
            e_update.mainloop()
        elif len(self.sel)==0:
            messagebox.showerror("Error","Selecciona para actualizar.")
        else:
            messagebox.showerror("Error","Solo puedes actualizar los datos: 1 a la vez.")

        


    def add_emp(self):
        global e_add
        e_add = Toplevel()
        page6 = add_employee(e_add)
        page6.time()
        e_add.protocol("WM_DELETE_WINDOW", self.ex)
        e_add.mainloop()


    def ex(self):
        e_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()   

    def ex2(self):
        e_update.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()  



    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Salir","Estás seguro de querer salir?", parent=emp)
        if sure == True:
            emp.destroy()
            adm.deiconify()


    def Logout(self):
        sure = messagebox.askyesno("Cerrar", "Estás seguro: cerrar sesión?")
        if sure == True:
            emp.destroy()
            root.deiconify()
            
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class add_employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Añadir Personal")

        self.label1 = Label(e_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/add_employee.png")
        self.label1.configure(image=self.img)

        self.clock = Label(e_add)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.r1 = e_add.register(self.testint)
        self.r2 = e_add.register(self.testchar)

        self.entry1 = Entry(e_add)
        self.entry1.place(relx=0.132, rely=0.296, width=374, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        

        self.entry2 = Entry(e_add)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_add)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(e_add)
        self.entry4.place(relx=0.527, rely=0.296, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry5 = Entry(e_add)
        self.entry5.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_add)
        self.entry6.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

        self.button1 = Button(e_add)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="palevioletred")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#d46c91")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""AGREGAR""")
        self.button1.configure(command=self.add)

        self.button2 = Button(e_add)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="palevioletred")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#d46c91")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""LIMPIAR""")
        self.button2.configure(command=self.clearr)



    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    
    def add(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()

        if ename.strip():
            if valid_phone(econtact):
                if valid_ci(eaddhar):
                    if edes:
                        if eadd:
                            if epass:
                                emp_id = random_emp_id(7)
                                insert = (
                                            "INSERT INTO employee(emp_id, name, contact_num, address, aadhar_num, password, designation) VALUES(?,?,?,?,?,?,?)"
                                        )
                                cur.execute(insert, [emp_id, ename, econtact, eadd, eaddhar, epass, edes])
                                db.commit()
                                messagebox.showinfo("Cuenta Creada", "ID de Empleado: {} añadido a la Base de Datos.".format(emp_id), parent=e_add)
                                self.clearr()
                            else:
                                messagebox.showerror("Oops!", "Introduzca; Contraseña.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Introduzca: Dirección.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Introduzca: Cargo.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Introduzca: CI.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Introduzca: Número de Teléfono.", parent=e_add)
        else:
            messagebox.showerror("Oops!", "Introduzca: Nombre del Personal.", parent=e_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)


class Update_Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Employee")

        self.label1 = Label(e_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/update_employee.png")
        self.label1.configure(image=self.img)

        self.clock = Label(e_update)
        self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.r1 = e_update.register(self.testint)
        self.r2 = e_update.register(self.testchar)

        self.entry1 = Entry(e_update)
        self.entry1.place(relx=0.132, rely=0.296, width=374, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        

        self.entry2 = Entry(e_update)
        self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_update)
        self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry4 = Entry(e_update)
        self.entry4.place(relx=0.527, rely=0.296, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

        self.entry5 = Entry(e_update)
        self.entry5.place(relx=0.527, rely=0.413, width=374, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_update)
        self.entry6.place(relx=0.527, rely=0.529, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

        self.button1 = Button(e_update)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="palevioletred")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#d46c91")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""UPDATE""")
        self.button1.configure(command=self.update)

        self.button2 = Button(e_update)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="palevioletred")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#d46c91")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""LIMPIAR""")
        self.button2.configure(command=self.clearr)

    def update(self):
        ename = self.entry1.get()
        econtact = self.entry2.get()
        eaddhar = self.entry3.get()
        edes = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()

        if ename.strip():
            if valid_phone(econtact):
                if valid_ci(eaddhar):
                    if edes:
                        if eadd:
                            if epass:
                                emp_id = vall[0]
                                update = (
                                            "UPDATE employee SET name = ?, contact_num = ?, address = ?, aadhar_num = ?, password = ?, designation = ? WHERE emp_id = ?"
                                        )
                                cur.execute(update, [ename, econtact, eadd, eaddhar, epass, edes, emp_id])
                                db.commit()
                                messagebox.showinfo("Success!!", "ID de empleado: {} correctamente subido a la base de datos.".format(emp_id), parent=e_update)
                                vall.clear()
                                page5.tree.delete(*page5.tree.get_children())
                                page5.DisplayData()
                                Employee.sel.clear()
                                e_update.destroy()
                            else:
                                messagebox.showerror("Oops!", "Please enter a password.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter address.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter designation.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Invalid Aadhar number.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_add)
        else:
            messagebox.showerror("Oops!", "Please enter employee name.", parent=e_add)


    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)



    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


        

class Invoice:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Invoices")

        self.label1 = Label(invoice)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/invoices.png")
        self.label1.configure(image=self.img)

        self.message = Label(invoice)
        self.message.place(relx=0.046, rely=0.055, width=136, height=30)
        self.message.configure(font="-family {Poppins} -size 10")
        self.message.configure(foreground="#000000")
        self.message.configure(background="#ffffff")
        self.message.configure(text="""ADMIN""")
        self.message.configure(anchor="w")

        self.clock = Label(invoice)
        self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#000000")
        self.clock.configure(background="#ffffff")

        self.entry1 = Entry(invoice)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(invoice)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="palevioletred")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#d46c91")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Buscar""")
        self.button1.configure(command=self.search_inv)

        self.button2 = Button(invoice)
        self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="palevioletred")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#d46c91")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)

        self.button3 = Button(invoice)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="palevioletred")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#d46c91")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""ELIMINAR FACTURA""")
        self.button3.configure(command=self.delete_invoice)

        self.button4 = Button(invoice)
        self.button4.place(relx=0.135, rely=0.885, width=76, height=23)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="palevioletred")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#d46c91")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""SALIR""")
        self.button4.configure(command=self.Exit)
         #------MENU-----
        #---menu---
        self.menu1 = Button(invoice)
        self.menu1.place(relx=0.0, rely=0.0, width=86, height=20)
        self.menu1.configure(relief="flat",overrelief="flat",activebackground="palevioletred",cursor="hand2",foreground="#ffffff",background="#d46c91",font=("-family {Poppins SemiBold} -size 10"))
        self.menu1.configure(borderwidth="2")
        self.menu1.configure(text="IMVENTARIO")
        self.menu1.configure(command=menu5)
       


        self.menu2 = Button(invoice)
        self.menu2.place(relx=0.065, rely=0.0, width=86, height=20)
        self.menu2.configure(relief="flat",overrelief="flat",activebackground="palevioletred",cursor="hand2",foreground="#ffffff",background="#d46c91",font=("-family {Poppins SemiBold} -size 10"))
        self.menu2.configure(borderwidth="2")
        self.menu2.configure(text="EMPLEADOS")
        self.menu2.configure(command=menu6)
     



        self.menu3 = Button(invoice)
        self.menu3.place(relx=0.130, rely=0.0, width=86, height=20)
        self.menu3.configure(relief="flat",overrelief="flat",activebackground="mistyrose",cursor="hand2",foreground="black",background="#d46c91",font=("-family {Poppins SemiBold} -size 10"))
        self.menu3.configure(borderwidth="2")
        self.menu3.configure(text="""FACTURAS""")



        #-------------------



        self.scrollbarx = Scrollbar(invoice, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(invoice, orient=VERTICAL)
        self.tree = ttk.Treeview(invoice)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.bind("<Double-1>", self.double_tap)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

        self.tree.configure(
            columns=(
                "Bill Number",
                "Date",
                "Customer Name",
                "Customer Phone No.",
            )
        )

        self.tree.heading("Bill Number", text="Número de factura", anchor=W)
        self.tree.heading("Date", text="Fecha", anchor=W)
        self.tree.heading("Customer Name", text="Nombre del cliente", anchor=W)
        self.tree.heading("Customer Phone No.", text="Número del cliente", anchor=W)
        

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=219)
        self.tree.column("#2", stretch=NO, minwidth=0, width=219)
        self.tree.column("#3", stretch=NO, minwidth=0, width=219)
        self.tree.column("#4", stretch=NO, minwidth=0, width=219)
        

        self.DisplayData()


    def DisplayData(self):
        cur.execute("SELECT * FROM bill")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def double_tap(self, Event):
        item = self.tree.identify('item', Event.x, Event.y)
        global bill_num
        bill_num = self.tree.item(item)['values'][0]
        

        global bill
        bill = Toplevel()
        pg = open_bill(bill)
        #bill.protocol("WM_DELETE_WINDOW", exitt)
        bill.mainloop()

        


    def delete_invoice(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Estás seguro que quieres eliminar la factura?", parent=invoice)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%5==0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    delete = "DELETE FROM bill WHERE bill_no = ?"
                    cur.execute(delete, [k])
                    db.commit()

                messagebox.showinfo("Success!!", "IFactura(s) eliminada de la Base de Datos.", parent=invoice)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select an invoice", parent=invoice)

    def search_inv(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Bill Number: {} found.".format(self.entry1.get()), parent=invoice)
                break
        else: 
            messagebox.showerror("Oops!!", "Bill NUmber: {} not found.".format(self.entry1.get()), parent=invoice)


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Seguro que quiere salir de la cuenta?")
        if sure == True:
            invoice.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Salir","Seguro que quieres salir?", parent=invoice)
        if sure == True:
            invoice.destroy()
            adm.deiconify()


class open_bill:
    def __init__(self, top=None):
        
        top.geometry("765x488")
        top.resizable(0, 0)
        top.title("Bill")

        self.label1 = Label(bill)
        self.label1.place(relx=0, rely=0, width=765, height=488)
        self.img = PhotoImage(file="./images/bill.png")
        self.label1.configure(image=self.img)
        
        self.name_message = Text(bill)
        self.name_message.place(relx=0.178, rely=0.205, width=176, height=30)
        self.name_message.configure(font="-family {Podkova} -size 10")
        self.name_message.configure(borderwidth=0)
        self.name_message.configure(background="#ffffff")

        self.num_message = Text(bill)
        self.num_message.place(relx=0.854, rely=0.205, width=90, height=30)
        self.num_message.configure(font="-family {Podkova} -size 10")
        self.num_message.configure(borderwidth=0)
        self.num_message.configure(background="#ffffff")

        self.bill_message = Text(bill)
        self.bill_message.place(relx=0.150, rely=0.243, width=176, height=26)
        self.bill_message.configure(font="-family {Podkova} -size 10")
        self.bill_message.configure(borderwidth=0)
        self.bill_message.configure(background="#ffffff")

        self.bill_date_message = Text(bill)
        self.bill_date_message.place(relx=0.780, rely=0.243, width=90, height=26)
        self.bill_date_message.configure(font="-family {Podkova} -size 10")
        self.bill_date_message.configure(borderwidth=0)
        self.bill_date_message.configure(background="#ffffff")


        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.044, rely=0.41, width=695, height=284)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
        self.Scrolledtext1.configure(state="disabled")

        find_bill = "SELECT * FROM bill WHERE bill_no = ?"
        cur.execute(find_bill, [bill_num])
        results = cur.fetchall()
        if results:
            self.name_message.insert(END, results[0][2])
            self.name_message.configure(state="disabled")
    
            self.num_message.insert(END, results[0][3])
            self.num_message.configure(state="disabled")
    
            self.bill_message.insert(END, results[0][0])
            self.bill_message.configure(state="disabled")

            self.bill_date_message.insert(END, results[0][1])
            self.bill_date_message.configure(state="disabled")

            self.Scrolledtext1.configure(state="normal")
            self.Scrolledtext1.insert(END, results[0][4])
            self.Scrolledtext1.configure(state="disabled")

page1 = login_page(root)
root.bind("<Return>", login_page.login)
root.mainloop()
