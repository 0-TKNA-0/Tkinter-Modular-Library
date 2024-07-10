import tkinter as tk
from tkinter import ttk
from random import randint, choice

# Create window
window = tk.Tk()
window.title("Scrolling")
window.geometry("600x400")

# Create widgets
canvasWidget = tk.Canvas(window, background = "white", scrollregion = (0,0,2000,5000)) # requires left, top, right, bottom coordinates
canvasWidget.create_line(0,0,2000,5000, fill = "green", width = 10)

# Randomly generates 100 squares and places them on the 2000x5000 canvas
for i in range(100):
    left = randint(0,2000)
    top = randint(0,5000)
    right = left + randint(10,500)
    bottom = top + randint(10,500)
    colour = choice(("red","green", "yellow", "orange", "blue"))

    canvasWidget.create_rectangle(left, top, right, bottom, fill = colour)
canvasWidget.pack(expand = True, fill = "both")

# Mousewheel scrolling
canvasWidget.bind("<MouseWheel>", lambda event: canvasWidget.yview_scroll(-int(event.delta / 60) , "units"))

# Scrollbar Widget
scrollBarWidget = ttk.Scrollbar(window, orient = "vertical", command = canvasWidget.yview)
canvasWidget.config(yscrollcommand = scrollBarWidget.set) # Updates the scrollbar UI
scrollBarWidget.place(relx= 1, rely= 0, relheight = 1, anchor = "ne")

# HELPFUL EXERCISE
NEWscrollBarWidget = ttk.Scrollbar(window, orient = "horizontal", command = canvasWidget.xview)
canvasWidget.config(xscrollcommand = NEWscrollBarWidget.set) # Updates the scrollbar UI
NEWscrollBarWidget.place(relx= 0, rely= 1, relwidth= 1, anchor = "sw")

# Mousewheel scrolling
canvasWidget.bind("<Control-MouseWheel>", lambda event: canvasWidget.xview_scroll(-int(event.delta / 60) , "units"))


##### Text Widget #####
# textWidget = tk.Text(window)
# for i in range(1, 200):
#     textWidget.insert(f"{i}.0", f"text: {i} \n") # 1 = starting line .0 is the character
# textWidget.pack(expand = True, fill = "both")
# 
# scrollBarText = ttk.Scrollbar(window, orient = "vertical", command = textWidget.yview)
# textWidget.config(yscrollcommand = scrollBarText.set) # Updates the scrollbar UI
# scrollBarText.place(relx= 1, rely= 0, relheight = 1, anchor = "ne")


##### TreeView Widget #####
# tableWidget = ttk.Treeview(window, columns = (1,2), show = "headings")
# tableWidget.heading(1, text = "First Name")
# tableWidget.heading(2, text = "Last Name")
# 
# # Data lists
# firstNames = ["Brody", "Matt", "Brinn", "Connor", "Joshua", "Bob", "Kerry", "Ella", "Todd", "Bianca"]
# lastNames = ["Jeanes", "Holden", "Hawes", "Williamson", "Edwards", "Smith", "Brown", "Sterchi", "Noetstaller"]
# 
# for i in range(100):
#     tableWidget.insert(parent = "", index = tk.END, values = (choice(firstNames), choice(lastNames)))
# tableWidget.pack(expand = True, fill = "both")
# 
# scrollBarTable = ttk.Scrollbar(window, orient = "vertical", command = tableWidget.yview)
# tableWidget.config(yscrollcommand = scrollBarTable.set) # Updates the scrollbar UI
# scrollBarTable.place(relx= 1, rely= 0, relheight = 1, anchor = "ne")

# Run window
window.mainloop()