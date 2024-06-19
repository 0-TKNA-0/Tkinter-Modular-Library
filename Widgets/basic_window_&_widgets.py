import tkinter as tk
from tkinter import ttk

def buttonFunction():
    print("DEBUG : Button was pressed")

# Create a window
window = tk.Tk()
window.title("Basic Window & Widgets")
window.geometry("800x500")

# Create (ttk) label widget
labelWidget = ttk.Label(
    master = window,
    text = "TESTING")
labelWidget.pack()

# Create (tk) text widget 
textWidget = tk.Text(
    master = window)
textWidget.pack()

# Create (ttk) entry widget
entryWidget = ttk.Entry(
    master = window)
entryWidget.pack()

# Create (ttk) button widget
buttonWidget = ttk.Button(
    master = window,
    text = "Button",
    command = buttonFunction)
buttonWidget.pack()

# HELPFUL EXERCISE
NEWLabelWidget = ttk.Label(
    master = window,
    text = "MY LABEL")
NEWLabelWidget.pack()

NEWButtonWidget = ttk.Button(
    master = window, 
    text = "NEW BUTTON", 
    command = lambda: print("Hello"))
NEWButtonWidget.pack()

# Run window
window.mainloop()