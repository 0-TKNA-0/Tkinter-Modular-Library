import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Basic Layouts")
window.geometry("600x400")

# Create widgets
label1Widget = ttk.Label(window, text = "Label #1", background = "red")
label2Widget = ttk.Label(window, text = "Label #2", background = "blue")

# Packing
# label1Widget.pack(side = "left", expand = True, fill = "x") # fill - x, y, both
# label2Widget.pack(side = "right", expand = True, fill = "both")

# ------------------------------------------------------------------------

# Gridding
# window.columnconfigure(0, weight = 1)
# window.columnconfigure(1, weight = 1)
# window.columnconfigure(2, weight = 2)
# window.rowconfigure(0, weight = 1)
# window.rowconfigure(1, weight = 1)

# label1Widget.grid(row = 0, column = 1, sticky = "nsew") # sticky - cardinal directions
# label2Widget.grid(row = 1, column = 1, columnspan = 2, sticky = "nsew")

# ------------------------------------------------------------------------

# Placing
label1Widget.place(x = 100, y = 200, width = 200, height = 100)
label2Widget.place(relx = 0.5, rely = 0.5, relwidth = 1, anchor = "center") # resizing the program move the widget

# Run window
window.mainloop()