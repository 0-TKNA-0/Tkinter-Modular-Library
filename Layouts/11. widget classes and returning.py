import tkinter as tk
from tkinter import ttk


class Segment(ttk.Frame):
    def __init__(self, parent, labelText, buttonText):
        super().__init__(master = parent)

        # Gridded layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0,1,2), weight = 1, uniform = "a")
        ttk.Label(self, text = labelText).grid(row = 0, column = 0, sticky = "nsew")
        ttk.Button(self, text = buttonText).grid(row = 0, column = 1, sticky = "nsew")

        self.pack(expand = True, fill = "both", padx = 10, pady = 10)

# Create window
window = tk.Tk()
window.title("Widgets and Returning")
window.geometry("400x600")

# Widgets
Segment(window, "Label #1", "Button #1")
Segment(window, "Label #2", "Button #2")
Segment(window, "Label #3", "Button #3")
Segment(window, "Label #4", "Button #4")
Segment(window, "Label #5", "Button #5")

# Run window
window.mainloop()