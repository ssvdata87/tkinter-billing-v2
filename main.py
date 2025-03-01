import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from database import Database
from Add_Product import open_product_window
from Show_Product import open_Show_Product
db=Database('hotel.db')

def show_product():
    product_id=product_code_entry.get()
    product_details=db.get_product(product_id)
    if product_details:
        product_name_entry.delete(0,END)
        product_price_entry.delete(0,END)
        quantity_entry.delete(0,END)
        total_entry.delete(0,END)
        product_name_entry.insert(0,product_details[1])
        product_price_entry.insert(0,product_details[2])
        quantity=1
        quantity_entry.insert(0,quantity)
        pp=float(product_price_var.get())
        t=quantity*pp
        total_entry.insert(0,t)

def update_total():
    quantity=quantity_var.get()
    price=product_price_var.get()
    total=quantity*price
    total_entry.delete(0,END)
    total_entry.insert(0,total)

def save_order_details():
    product_code=product_code_entry.get()
    product_name=product_name_entry.get()
    product_price=product_price_entry.get()
    quantity=quantity_entry.get()
    total=total_entry.get()
    db.add_order_details(product_code,product_name,quantity,product_price,total)
    get_gtotal()
    product_tree_bind()



def get_gtotal():
    total=db.get_all_order_total()
    print(total)
    grand_total_entry.delete(0,END)
    grand_total_entry.insert(0,total)

def product_tree_bind():
    product_tree.delete(*product_tree.get_children())
    product_list=db.get_order_details()
    for i in product_list:
        product_tree.insert("",END,values=i)

def save_bill():
    db.save_order()
    product_tree.delete(*product_tree.get_children())
    grand_total_entry.delete(0,END)
    product_code_entry.delete(0,END)
    product_name_entry.delete(0,END)
    product_price_entry.delete(0,END)
    quantity_entry.delete(0,END)
    total_entry.delete(0,END)
    

    

root=tk.Tk()
product_code_var=StringVar()
product_name_var=StringVar()
product_price_var=DoubleVar()
quantity_var=IntVar()
total_var=DoubleVar()
gtotal=DoubleVar()
root.title("Hotel billing system")
root.state("zoomed")
root.configure(bg="green")
menu_bar=Menu(root)
root.config(menu=menu_bar)
file_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Add Product",command=lambda:open_product_window())
file_menu.add_separator()
file_menu.add_command(label="Show Product",command=lambda:open_Show_Product())
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#Entry Frame
entries_frame=Frame(root,bg="#e6e6e6")
entries_frame.pack(side=TOP,fill=X)
product_code_label=Label(entries_frame,text="Enter Product Code",bg="gray",fg="white",font=("Arial",12,"bold"))
product_code_label.grid(row=0,column=0,padx=10,pady=10)

product_code_entry=Entry(entries_frame,font=("Arial",12,"bold"),textvariable=product_code_var)
product_code_entry.grid(row=0,column=1,padx=10,pady=10)
product_code_entry.bind("<KeyRelease>",lambda e:show_product())

product_name_label=Label(entries_frame,text="Enter Product Name",bg="gray",fg="white",font=("Arial",11,"bold"))
product_name_label.grid(row=1,column=0,padx=10,pady=10)

product_name_entry=Entry(entries_frame,font=("Arial",11,"bold"),textvariable=product_name_var)
product_name_entry.grid(row=1,column=1,padx=10,pady=10)

product_price_label=Label(entries_frame,text="Enter Product Price",bg="gray",fg="white",font=("Arial",11,"bold"))
product_price_label.grid(row=1,column=2,padx=10,pady=10)

product_price_entry=Entry(entries_frame,font=("Arial",11,"bold"),textvariable=product_price_var)
product_price_entry.grid(row=1,column=3,padx=10,pady=10)

quantity_label=Label(entries_frame,text="Enter Quantity",bg="gray",fg="white",font=("Arial",10,"bold"))
quantity_label.grid(row=1,column=4,padx=10,pady=10)

quantity_entry=Entry(entries_frame,font=("Arial",10,"bold"),textvariable=quantity_var)
quantity_entry.grid(row=1,column=5,padx=10,pady=10)
quantity_entry.bind("<KeyRelease>",lambda e:update_total())


total_label=Label(entries_frame,text="Total",bg="gray",fg="white",font=("Arial",10,"bold"))
total_label.grid(row=1,column=6,padx=10,pady=10)

total_entry=Entry(entries_frame,font=("Arial",10,"bold"),textvariable=total_var)
total_entry.grid(row=1,column=7,padx=10,pady=10)

add_button=Button(entries_frame,text="Add Product",bg="green",fg="white",font=("Arial",12,"bold"),command=lambda:save_order_details())  
add_button.grid(row=1,column=8,padx=10,pady=10)


grand_total_entry = tk.Entry(entries_frame, textvariable=gtotal,font=('Ariel',16,'bold'), width=10,bg='#fff')
grand_total_entry.grid(row=2, column=7, padx=10, pady=10)
 
 
#table frame
table_frame=Frame(root,bg="white")
table_frame.place(x=0,y=180,width=800,height=200)
scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(table_frame,orient=VERTICAL)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("calbri",12,"bold"))
style.configure("mystyle.Treeview.Heading",font=("calbri",12,"bold"))
product_tree=ttk.Treeview(table_frame,columns=("product_name","product_price","quantity","total"),show='headings',style="mystyle.Treeview")
product_tree.heading("product_name",text="Product Name")
product_tree.heading("product_price",text="Product Price")  
product_tree.heading("quantity",text="Quantity")
product_tree.heading("total",text="Total")
product_tree.pack()

#buttom frame
bottom_frame=Frame(root,bg="gray")
bottom_frame.pack(side=BOTTOM,fill=X)
submit_button=Button(bottom_frame,text="Submit",bg="green",fg="white",font=("Arial",12,"bold"),width=20,height=2,command=lambda:save_bill()) 
submit_button.pack(side=LEFT,padx=10,pady=10)


root.mainloop()