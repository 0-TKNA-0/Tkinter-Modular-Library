import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Combining Layouts")
window.geometry("600x600")
window.minsize(600,600)

# Create main widgets
### Main 'Place' Widgets + Layout ###
mainFrame = ttk.Frame(window)
entryFrame1 = ttk.Frame(mainFrame)
entryFrame2 = ttk.Frame(mainFrame)

mainFrame.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)
entryFrame1.pack(side = "left", expand = True, fill = "both", padx = 20, pady = 20)
entryFrame2.pack(side = "left", expand = True, fill = "both", padx = 20, pady = 20)

# BUTTONS
mainButton1 = ttk.Button(
    entryFrame1, 
    text = "Button #1")

mainButton2 = ttk.Button(
    entryFrame2, 
    text = "Button #2")

# LABELS
mainLabel1 = ttk.Label(
    entryFrame1, 
    text = "Label #1", 
    background = "red")

mainLabel2 = ttk.Label(
    entryFrame2, 
    text = "Label #2", 
    background = "blue")

mainLabel1.pack(expand = True, fill = "both")
mainButton1.pack(expand = True, fill = "both", pady = 10)

mainLabel2.pack(expand = True, fill = "both")
mainButton2.pack(expand = True, fill = "both", pady = 10)

### Menu 'Place' Widgets + Layout ###
menuFrame = ttk.Frame(window)
toggleFrame = ttk.Frame(menuFrame)

menuFrame.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)
toggleFrame.grid(row = 4, column = 0, columnspan = 3, sticky = "nswe")

# BUTTONS 
menuButton1 = ttk.Button(
    menuFrame, 
    text = "Button #1")

menuButton2 = ttk.Button(
    menuFrame, 
    text = "Button #2")

menuButton3 = ttk.Button(
    menuFrame, 
    text = "Button #3")

# SLIDERS
menuSlider1 = ttk.Scale(
    menuFrame, 
    orient = "vertical")

menuSlider2 = ttk.Scale(
    menuFrame, 
    orient = "vertical")

# CHECK BOXES
menuToggle1 = ttk.Checkbutton(
    toggleFrame, 
    text = "Check #1")
menuToggle2 = ttk.Checkbutton(
    toggleFrame, 
    text = "Check #2")


# ENTRY
entryWidget = ttk.Entry(menuFrame)

# Menu Layout
menuFrame.columnconfigure((0,1,2), weight = 1, uniform = "a")
menuFrame.rowconfigure((0,1,2,3,4), weight = 1, uniform = "a")

# Gridded Buttons
menuButton1.grid(row = 0, column = 0, sticky = "nsew", columnspan = 2)
menuButton2.grid(row = 0, column = 2, sticky = "nsew")
menuButton3.grid(row = 1, column = 0, sticky = "nsew", columnspan = 3)

# Gridded Sliders
menuSlider1.grid(row = 2, column = 0, sticky = "nsew", rowspan = 2, pady = 20)
menuSlider2.grid(row = 2, column = 2, sticky = "nsew", rowspan = 2, pady = 20)

# Packed Toggles
menuToggle1.pack(side = "left", expand = True)
menuToggle2.pack(side = "left", expand = True)

# Placed Entry
entryWidget.place(relx = 0.5, rely = 0.95, relwidth = 0.9, anchor = "center")

# Run window
window.mainloop()