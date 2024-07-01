from tkinter import *
from tkinter import ttk
from db import Database

db = Database("InventoryManagement.db")
root = Tk()
root.title("Textile Inventory Management")
root.geometry("1360x768+0+0")
root.config(bg="#3a4047")
root.state("zoomed")
# shrit
shirt = StringVar()
size = StringVar()
price = StringVar()
# pant
pant = StringVar()
psize = StringVar()
pprice = StringVar()

# choosing Frame shirt
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Textile Inventory Management", font=("Calibri", 18, "bold"), bg="#535c68",
              fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

labelshirt = Label(entries_frame, text="Shirt", font=("Calibri", 16), bg="#535c68", fg="white")
labelshirt.grid(row=1, column=0, padx=10, pady=10, sticky="w")
textshirt = Entry(entries_frame, textvariable=shirt, font=("Calibri", 16), width=30)
textshirt.grid(row=1, column=1, padx=10, pady=10, sticky="w")
comboshirt = ttk.Combobox(entries_frame, font=("Calibri", 16), width=30, textvariable=shirt, state="readonly")
comboshirt['values'] = ("Printed Shirt", "Formal Shirt", "Designer Shirt", "Checked Shirt")
comboshirt.grid(row=1, column=1, padx=10, sticky="w")

labelsize = Label(entries_frame, text="size", font=("Calibri", 16), bg="#535c68", fg="white")
labelsize.grid(row=1, column=2, padx=10, pady=10, sticky="w")
textsize = Entry(entries_frame, textvariable=size, font=("Calibri", 16), width=15)
textsize.grid(row=1, column=3, padx=10, pady=10, sticky="w")
combosize = ttk.Combobox(entries_frame, font=("Calibri", 16), width=15, textvariable=size, state="readonly")
combosize['values'] = ("S", "M", "L", "XL")
combosize.grid(row=1, column=3, padx=10, sticky="w")

labelprice = Label(entries_frame, text="price", font=("Calibri", 16), bg="#535c68", fg="white")
labelprice.grid(row=1, column=4, padx=10, pady=10, sticky="w")
textprice = Entry(entries_frame, textvariable=price, font=("Calibri", 16), width=15)
textprice.grid(row=1, column=5, padx=10, pady=10, sticky="w")

# choosing Frame pant
labelpant = Label(entries_frame, text="Pant", font=("Calibri", 16), bg="#535c68", fg="white")
labelpant.grid(row=2, column=0, padx=10, pady=10, sticky="w")
textpant = Entry(entries_frame, textvariable=pant, font=("Calibri", 16), width=30)
textpant.grid(row=2, column=1, padx=10, pady=10, sticky="w")
combopant = ttk.Combobox(entries_frame, font=("Calibri", 16), width=30, textvariable=pant, state="readonly")
combopant['values'] = ("Baggy Pant", "Formal Pant", "Denim Pant", "Chinos")
combopant.grid(row=2, column=1, padx=10, sticky="w")

labelpsize = Label(entries_frame, text="size", font=("Calibri", 16), bg="#535c68", fg="white")
labelpsize.grid(row=2, column=2, padx=10, pady=10, sticky="w")
textpsize = Entry(entries_frame, textvariable=psize, font=("Calibri", 16), width=15)
textpsize.grid(row=2, column=3, padx=10, pady=10, sticky="w")
combopsize = ttk.Combobox(entries_frame, font=("Calibri", 16), width=15, textvariable=psize, state="readonly")
combopsize['values'] = ("S", "M", "L", "XL")
combopsize.grid(row=2, column=3, padx=10, sticky="w")

labelpprice = Label(entries_frame, text="price", font=("Calibri", 16), bg="#535c68", fg="white")
labelpprice.grid(row=2, column=4, padx=10, pady=10, sticky="w")
textpprice = Entry(entries_frame, textvariable=pprice, font=("Calibri", 16), width=15)
textpprice.grid(row=2, column=5, padx=10, pady=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    shirt.set(row[1])
    size.set(row[2])
    price.set(row[3])
    pant.set(row[4])
    psize.set(row[5])
    pprice.set(row[6])

def showAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

# button Frame
def add_items():
    db.insert(textshirt.get(), textsize.get(), textprice.get(), textpant.get(), textpsize.get(),
              textpprice.get())
    clearAll()
    showAll()


def update_items():
    db.update(row[0], textshirt.get(), textsize.get(), textprice.get(), textpant.get(), textpsize.get(), textpprice.get())
    clearAll()
    showAll()

def delete_items():
    db.remove(row[0])
    clearAll()
    showAll()

def clearAll():
    shirt.set("")
    size.set("")
    price.set("")
    pant.set("")
    psize.set("")
    pprice.set("")



btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_items, text="Add Items", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#db6f5c", bd=2).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_items, text="Update Items", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#f7db5e", bd=2).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_items, text="Delete Items", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#79e36b", bd=2).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear", width=15, font=("Calibri", 16, "bold"),
                  fg="white", bg="#243d57", bd=2).grid(row=0, column=3, padx=10)
# Table Frame
tbl_frame = Frame(root, bg="#ecf0f1")
tbl_frame.place(x=0, y=300, width=1360, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tbl_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.heading("2", text="Shirt")
tv.heading("3", text="Size")
tv.heading("4", text="Price")
tv.heading("5", text="Pant")
tv.heading("6", text="size")
tv.heading("7", text="price")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

showAll()
root.mainloop()