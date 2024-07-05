import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Widget Sizes")
window.geometry("400x300")

# Create widgets
label1Widget = ttk.Label(
    window, 
    text = "Label #1", 
    background = "green")

label2Widget = ttk.Label(
    window, 
    text = "Label #2", 
    background = "red",
    width = 50
    )

# Pack Widgets
# label2Widget.pack(fill = "x")
# label1Widget.pack()

# Grid Widgets
window.columnconfigure((0,1), weight = 1, uniform = "a")
window.rowconfigure((0,1), weight = 1, uniform = "a")

label1Widget.grid(row = 0, column = 0)
label2Widget.grid(row = 1, column = 0, sticky = "nswe")

# Run window
window.mainloop()