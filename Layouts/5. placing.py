import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Placing")
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

# Place widgets
label1Widget.place(x = 300, y = 100, width = 100, height = 200)
label2Widget.place(relx = 0.2, rely = 0.1, relwidth = 0.4, relheight = 0.5)
label3Widget.place(x = 80, y = 60, width = 160, height = 300)
buttonWidget.place(relx = 1, rely = 1)

# Run window
window.mainloop()