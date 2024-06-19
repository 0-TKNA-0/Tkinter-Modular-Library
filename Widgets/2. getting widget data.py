import tkinter as tk
from tkinter import ttk

def getEntryWidgetData():
    # Get the data from entryWidget
    entryWidgetText = entryWidget.get()

    # Update the labelWidget (2 different ways)
    labelWidget.config(text = entryWidgetText)
    labelWidget["text"] = entryWidgetText

    # Disable the entryWidget once the buttonWidget has been pressed
    entryWidget.config(state = "disabled")


# Create a window
window = tk.Tk()
window.geometry("500x500")
window.title("Getting Widget Data")

# Create widgets
labelWidget = ttk.Label(
    master = window, 
    text = "LABEL")
labelWidget.pack()

entryWidget = ttk.Entry(
    master = window)
entryWidget.pack()

buttonWidget = ttk.Button(
    master = window, 
    text = "BUTTON", 
    command = getEntryWidgetData)
buttonWidget.pack()


# HELPFUL EXERCISE
def undoFunction():
    # Renames the labelWidget back to its original name
    labelWidget.config(text = "LABEL")
    # Re-enables the entryWidget
    entryWidget.config(state = "enabled")

NEWButtonWidget = ttk.Button(
    master = window, 
    text = "UNDO", 
    command = undoFunction)
NEWButtonWidget.pack()

# Run window
window.mainloop()