import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Colours")
window.geometry("400x300")

# Create widgets
ttk.Label(window, background = "red").pack(expand = True, fill = "both") # String colour
ttk.Label(window, background = "#08F").pack(expand = True, fill = "both") # 3 Hexadecimal colour
ttk.Label(window, background = "#4fc296").pack(expand = True, fill = "both") # 6 Hexadecimal colour

# White and Black
ttk.Label(window, background = "#000").pack(expand = True, fill = "both")
ttk.Label(window, background = "#FFF").pack(expand = True, fill = "both")
ttk.Label(window, background = "#888").pack(expand = True, fill = "both")

# Run window
window.mainloop()