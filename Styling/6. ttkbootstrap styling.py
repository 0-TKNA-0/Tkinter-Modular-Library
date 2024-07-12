import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# https://ttkbootstrap.readthedocs.io/en/latest/

# Create window
# window = tk.Tk() DONT USE WHEN DEALING WITH TTKBOOTSTRAP
window = ttk.Window(themename = "journal") # 
window.title("ttkBootstrap Styling")
window.geometry("400x300")

labelWidget = ttk.Label(window, text = "Label #1")
labelWidget.pack(pady = 10)

button1Widget = ttk.Button(window, text = "Button #1", bootstyle = "danger")
button1Widget.pack(pady = 10)

button2Widget = ttk.Button(window, text = "Button #2", bootstyle = "warning")
button2Widget.pack(pady = 10)

button3Widget = ttk.Button(window, text = "Button #3", bootstyle = "success")
button3Widget.pack(pady = 10)

# Run window
window.mainloop()