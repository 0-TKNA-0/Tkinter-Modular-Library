import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Stacking Widgets")
window.geometry("400x400")

# Create Widgets
label1Widget = ttk.Label(
    window, 
    text = "Label #1", 
    background = "green")

label2Widget = ttk.Label(
    window, 
    text = "Label #2", 
    background = "red")

label3Widget = ttk.Label(
    window, 
    text = "Label #3", 
    background = "blue")

# label1Widget.lift()
# label2Widget.lower()

# label1Widget.tkraise()
# label2Widget.tklower()

button1Widget = ttk.Button(
    window, 
    text = "Raise Label #1",
    command = lambda: label1Widget.lift(aboveThis = label2Widget)) # label 1 cannot be above label 3 unless its ontop of label 2

button2Widget = ttk.Button(
    window, 
    text = "Raise Label #2",
    command = lambda: label2Widget.lift())

button3Widget = ttk.Button(
    window, 
    text = "Raise Label #3",
    command = lambda: label3Widget.lift())

# Place Widgets
label1Widget.place(x = 50, y = 100, width = 200, height = 150)
label2Widget.place(x = 150, y = 60, width = 140, height = 100)
label3Widget.place(x = 20, y = 80, width = 180, height = 100)

button1Widget.place(relx = 0.8, rely = 1, anchor = "se")
button2Widget.place(relx= 1, rely = 1, anchor = "se")
button3Widget.place(relx= 0.6, rely = 1, anchor = "se")

# Run window
window.mainloop()