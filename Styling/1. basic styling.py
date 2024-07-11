import tkinter as tk
from tkinter import ttk, font

# Create window
window = tk.Tk()
window.title("Basic Styling")
window.geometry("400x300")

# Create style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use("classic")

#style.configure("TButton", foreground = "green", font = ("Arial", 20)) # Applies to all buttons
style.configure("new.TButton", foreground = "green", font = ("Arial", 20)) # Only applies to buttons with the bound styled variable
style.configure("TFrame", background = "pink")
style.map(
    "new.TButton", 
    foreground = [("pressed", "red"),("disabled", "yellow")],
    background = [("pressed", "green"),("active", "blue")])

# Create widgets
labelWidget = ttk.Label(
    window, 
    text = "Label #1\nNew Line", 
    background = "red", 
    foreground = "white", 
    font = ("Arial", 20), 
    justify = "center")
labelWidget.pack()

buttonWidget = ttk.Button(window, text = "Button #1", style = "new.TButton")
buttonWidget.pack()

frameWidget = ttk.Frame(window, style = "TFrame", width = 100, height = 100)
frameWidget.pack()

# Run window
window.mainloop()