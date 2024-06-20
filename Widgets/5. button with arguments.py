import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Button With Arguments")
window.geometry("600x400")

# Create widgets
def buttonFunction(entryWidgetVar):
    print("DEBUG : BUTTON PRESSED")
    print(entryWidgetVar.get())

entryWidgetVar = tk.StringVar(value = "ENTRY WIDGET")
entryWidget = ttk.Entry(
    window, 
    textvariable = entryWidgetVar)
entryWidget.pack()

standardButton = ttk.Button(
    window, 
    text = "BUTTON", 
    command = lambda: buttonFunction(entryWidgetVar))
standardButton.pack()



# Run window
window.mainloop()