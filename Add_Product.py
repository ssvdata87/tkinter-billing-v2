import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from database import Database
db = Database('hotel.db')

def open_product_window():
    Product_window=tk.Tk()
    product_name=tk.StringVar()
    product_price=tk.DoubleVar()
    Product_window.title("Add Product")
    Product_window.geometry("500x500+0+0")
    Product_window.configure(bg="light green")
    product_name_label=Label(Product_window,text="Enter Product Name",bg="gray",fg="white",font=("Arial",12,"bold"))
    product_name_label.grid(row=0,column=0,padx=10,pady=10)    
    product_name_entry=Entry(Product_window,font=("Arial",12,"bold"),textvariable=product_name)
    product_name_entry.grid(row=0,column=1,padx=10,pady=10)
    product_price_label=Label(Product_window,text="Enter Product Price",bg="gray",fg="white",font=("Arial",12,"bold"))  
    product_price_label.grid(row=1,column=0,padx=10,pady=10)
    product_price_entry=Entry(Product_window,font=("Arial",12,"bold"),textvariable=product_price)
    product_price_entry.grid(row=1,column=1,padx=10,pady=10) 
    add_product_button=Button(Product_window,text="Add Product",bg="gray",fg="white",font=("Arial",12,"bold"),command=lambda:add_product())
    add_product_button.grid(row=2,column=1,padx=10,pady=10)
    
    def add_product():
        product_name1 = product_name_entry.get()
        product_price1 = product_price_entry.get()        
        if product_name_entry.get().strip() == "" or product_price_entry.get().strip() == 0.0:
            messagebox.showerror("Error", "All fields are required")
        else:
            
            print('pname :',product_name1,'price :',product_price1)
            db.add_product(product_name1, product_price1)
            messagebox.showinfo("Success", "Product added successfully")
            product_name_entry.delete(0, tk.END)
            product_price_entry.delete(0, tk.END)
