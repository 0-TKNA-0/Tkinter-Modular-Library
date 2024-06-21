import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.geometry("600x400")
window.title("ComboBox & SpinBox")

# Create ComboBox Widgets
listOfMonths = ("January", "Feburary", "March")
monthStringVar = tk.StringVar(value = listOfMonths[0])

comboBoxWidget = ttk.Combobox(
    window, 
    textvariable = monthStringVar)
#comboBoxWidget["values"] = listOfMonths
comboBoxWidget.config(values = listOfMonths)
comboBoxWidget.pack()

# ComboBox Events
comboBoxWidget.bind("<<ComboboxSelected>>", lambda event: comboBoxLabel.config(text = f"Selected Month : {monthStringVar.get()}"))

comboBoxLabel = ttk.Label(window, text = "MONTH")
comboBoxLabel.pack()


# Create SpinBox Widget
spinBoxWidgetInt = tk.IntVar(value = 1)
spinBoxWidget = ttk.Spinbox(
    window,
    from_ = 1,
    to = 10, 
    increment = 2, 
    command = lambda: print(spinBoxWidgetInt.get()),
    textvariable = spinBoxWidgetInt)
spinBoxWidget.bind("<<Increment>>", lambda event: print("DEBUG : UP ARROW WAS PRESSED"))
spinBoxWidget.bind("<<Decrement>>", lambda event: print("DEBUG : DOWN ARROW WAS PRESSED"))
#spinBoxWidget.config(values = (1, 2, 3, 4, 5))
spinBoxWidget.pack(pady=(30,0))


# HELPFUL EXERCISE
listOfLetters = ("A", "B", "C", "D", "E")
NEWSpinBoxWidgetVar = tk.StringVar(value = listOfLetters[0])

NEWSpinBoxWidget = ttk.Spinbox(
    window, 
    textvariable = NEWSpinBoxWidgetVar,
    values = listOfLetters)
NEWSpinBoxWidget.bind("<<Decrement>>", lambda event: print(NEWSpinBoxWidgetVar.get()))
NEWSpinBoxWidget.pack()


# Run Window
window.mainloop()