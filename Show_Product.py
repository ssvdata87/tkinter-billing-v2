import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from database import Database
db=Database('hotel.db')

def open_Show_Product():
    get_product=db.show_product()
    Show_Product_window=tk.Tk()
    Show_Product_window.title("Show Product")
    Show_Product_window.geometry("700x500+0+0")
    Show_Product_window.configure(bg="light green")

    style=ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
    style.configure("Treeview", font=("Arial", 12))

    _ptree=ttk.Treeview(Show_Product_window, column=("column1", "column2", "column3"), show='headings',style="Treeview")
    _ptree.heading("#1", text="Product Code")
    _ptree.heading("#2", text="Product Name")
    _ptree.heading("#3", text="Product Price")


    _ptree.place(x=10, y=10, width=680, height=300)


    for i in get_product:
        _ptree.insert("", "end", values
        =(i[0], i[1], i[2]))


    
    


