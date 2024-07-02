import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Griding")
window.geometry("600x400")

# Create widgets
label1Widget = ttk.Label(
    window, 
    text = "Label #1", 
    background = "red")

label2Widget = ttk.Label(
    window, 
    text = "Label #2", 
    background = "blue")

label3Widget = ttk.Label(
    window, 
    text = "Label #3", 
    background = "green")

label4Widget = ttk.Label(
    window, 
    text = "Label #4", 
    background = "yellow")

button1Widget = ttk.Button(
    window, 
    text = "Button #1")

button2Widget = ttk.Button(
    window, 
    text = "Button #2")

entryWidget = ttk.Entry(window)

# Create grid
window.columnconfigure((0,1,2), weight = 1, uniform = "a")
window.columnconfigure(3, weight = 10)

window.rowconfigure(0, weight = 1, uniform = "a")
window.rowconfigure((1,2), weight = 1, uniform = "a")
window.rowconfigure(3, weight = 3, uniform = "a")

# Grid the widgets
label1Widget.grid(row = 0, column = 0, sticky = "nsew")
label2Widget.grid(row = 1, column = 1, rowspan = 3, sticky = "nsew")
label3Widget.grid(row = 1, column = 0, columnspan = 3, sticky = "nsew", padx = 20, pady = 10)
label4Widget.grid(row = 3, column = 3, sticky = "se")

# HELPFUL EXERCISE
button1Widget.grid(row = 0, column = 3, sticky = "nsew")
button2Widget.grid(row = 2, column = 2, sticky = "nsew")
entryWidget.grid(row = 3, column = 3, sticky = "n")


# Run window
window.mainloop()