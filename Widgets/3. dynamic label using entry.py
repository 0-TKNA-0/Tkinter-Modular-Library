import tkinter as tk
from tkinter import ttk

def buttonFunction():
    # Get the label string
    print(labelWidgetString_Var.get())


# Create window
window = tk.Tk()
window.geometry("500x500")
window.title("Dynamic Label Updating")

# tkinter dynamic variable
labelWidgetString_Var = tk.StringVar()
# labelWidgetString_Var = tk.StringVar(value = "STARTING VALUE")


# Create widgets
labelWidget = ttk.Label(
    master = window, 
    text = "placeholder", 
    textvariable = labelWidgetString_Var)
labelWidget.pack()

entryWidget = ttk.Entry(
    master = window, 
    textvariable = labelWidgetString_Var)
entryWidget.pack()

buttonWidget = ttk.Button(master = window, text = "Button", command = buttonFunction)
buttonWidget.pack()


# Run window
window.mainloop()