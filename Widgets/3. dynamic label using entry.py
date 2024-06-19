import tkinter as tk
from tkinter import ttk

def buttonFunction():
    # Get the label string
    print(labelWidgetString_Var.get())

    # Set the label and entry widget string 
    labelWidgetString_Var.set("BUTTON PRESSED")


# Create window
window = tk.Tk()
window.geometry("500x500")
window.title("Dynamic Label Updating")

# tkinter dynamic variable
labelWidgetString_Var = tk.StringVar()
# labelWidgetString_Var = tk.StringVar(value = "STARTING VALUE")
NEWLabelWidgetString_Var = tk.StringVar(value = "START")



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

buttonWidget = ttk.Button(
    master = window, 
    text = "Button", 
    command = buttonFunction)
buttonWidget.pack(pady=30)

# HELPFUL EXERCISE
NEWLabelWidget = ttk.Label(
    master = window, 
    text = "PLACEHOLDER",
    textvariable = NEWLabelWidgetString_Var)
NEWLabelWidget.pack()

NEWEntryWidget = ttk.Entry(
    master = window, 
    textvariable = NEWLabelWidgetString_Var )
NEWEntryWidget.pack()

OTHEREntryWidget = ttk.Entry(
    master = window, 
    textvariable = NEWLabelWidgetString_Var)
OTHEREntryWidget.pack()

# Run window
window.mainloop()