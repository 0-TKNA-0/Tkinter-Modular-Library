import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Packing")
window.geometry("400x600")

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

buttonWidget = ttk.Button(
    window, 
    text = "Button")

label1Widget.pack(side = "top", expand = True, fill = "both", padx = 20, pady= 20)
label2Widget.pack(side = "left", expand = True, fill = "both")
label3Widget.pack(side = "top", expand = True, fill = "both")
buttonWidget.pack(side = "top", expand = True, fill = "both")

# Run Window
window.mainloop()