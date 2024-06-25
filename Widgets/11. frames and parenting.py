import tkinter as tk
from tkinter import ttk

# Create Window
window = tk.Tk()
window.geometry("600x400")
window.title("Frames and Parenting")

# Create Frame widget
frameWidget = ttk.Frame(
    window, 
    width = 100, 
    height = 200, 
    borderwidth = 10, 
    relief = tk.GROOVE)
frameWidget.pack_propagate(False) # sets the size of the frame from its children
frameWidget.pack(side = "left")

# Master Settings
labelWidget = ttk.Label(
    frameWidget, 
    text = "Label")
labelWidget.pack()

buttonWidget = ttk.Button(
    frameWidget, 
    text = "Button")
buttonWidget.pack()

label2Widget = ttk.Label(
    window, 
    text = "Hello")
label2Widget.pack()

# HELPFUL EXERCISE
NEWFrameWidget = ttk.Frame(
    window, 
    width = 100, 
    height = 200, 
    borderwidth = 10, 
    relief = tk.GROOVE)
NEWFrameWidget.pack(side = "left")

NEWLabelWidget = ttk.Label(NEWFrameWidget, text = "NEW LABEL")
NEWFrameWidget.pack()

NEWButtonWidget = ttk.Button(NEWFrameWidget, text = "NEW BUTTON")
NEWButtonWidget.pack()

NEWEntryWidget = ttk.Entry(NEWFrameWidget)
NEWEntryWidget.pack()


# Run window
window.mainloop()