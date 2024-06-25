import tkinter as tk
from tkinter import ttk

# Create Window
window = tk.Tk()
window.geometry("600x400")
window.title("Tabs")

# Create Notebook Tab Widget
notebookWidget = ttk.Notebook(window)

# Tab 1 Widgets
tab1 = ttk.Frame(notebookWidget)
label1Widget = ttk.Label(
    tab1, 
    text = "Label")
label1Widget.pack()

button1Widget = ttk.Button(
    tab1, 
    text = "Button")
button1Widget.pack()

# Tab 2 Widgets
tab2 = ttk.Frame(notebookWidget)
label2Widget = ttk.Label(
    tab2, 
    text = "LABEL 2")
label2Widget.pack()
entry2Widget = ttk.Entry(tab2)
entry2Widget.pack()

notebookWidget.add(tab1, text = "TAB 1")
notebookWidget.add(tab2, text = "TAB 2")
notebookWidget.pack()

# HELPFUL EXERCISE TAB
tab3 = ttk.Frame(notebookWidget)

label3Widget = ttk.Label(
    tab3, 
    text = "Label 3")
label3Widget.pack()

button31Widget = ttk.Button(
    tab3, 
    text = "Button 3.2")
button31Widget.pack()

button32Widget = ttk.Button(
    tab3, 
    text = "Button 3.2")
button32Widget.pack()

notebookWidget.add(tab3, text = "TAB 3")




# Run Window
window.mainloop()