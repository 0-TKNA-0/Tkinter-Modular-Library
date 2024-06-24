import tkinter as tk
from tkinter import ttk
from random import choice

# Create Window
window = tk.Tk()
window.geometry("600x400")
window.title("Treeview Table")

# Data lists
firstNames = ["Brody", "Matt", "Brinn", "Connor", "Joshua", "Bob", "Kerry", "Ella", "Todd", "Bianca"]
lastNames = ["Jeanes", "Holden", "Hawes", "Williamson", "Edwards", "Smith", "Brown", "Sterchi", "Noetstaller"]

# Create Treeview Widget
tableWidget = ttk.Treeview(
    window, 
    columns = ("First", "Last", "Email"), 
    show = "headings")
tableWidget.heading("First", text = "First Name")
tableWidget.heading("Last", text = "Surname")
tableWidget.heading("Email", text = "Email")
tableWidget.pack(fill = "both", expand = True)

# Insert values into a treeview table
for integer in range(100):
    first = choice(firstNames)
    last = choice(lastNames)
    email = f"{first[0]}.{last}@email.com"
    appendedData = (first, last, email)
    tableWidget.insert(parent = "", index = 0, values = appendedData)

tableWidget.insert(parent = "", index = 2, values = ("HELLO", "TESTING", "HELLO@TEST"))


# event
def itemSelector(event):
    print(tableWidget.selection())
    for integer in tableWidget.selection():
        print(tableWidget.item(integer)["values"])

def itemDelete(event):
    for integer in tableWidget.selection():
        tableWidget.delete(integer)

tableWidget.bind("<<TreeviewSelect>>", itemSelector)
tableWidget.bind("<Delete>", itemDelete)

# item id 

# Run Window
window.mainloop()