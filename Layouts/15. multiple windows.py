import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# https://docs.python.org/3/library/tkinter.messagebox.html

# Create window
window = tk.Tk()
window.title("Multiple Windows")
window.geometry("600x400")

# CLASS FOR CREATEWINDOW
# class ExtraWindow(tk.Toplevel):
#     def __init__(self):
#         super().__init__()
#         self.title("Extra Window")
#         self.geometry("300x400")
# 
#         ttk.Label(self, text = "Label #1").pack()
#         ttk.Button(self, text = "Button #1").pack()
#         ttk.Label(self, text = "Label #2").pack(expand = True)

def askYesNo():
    # answer = messagebox.askquestion("Testing", "Test")
    # print("DEBUG :", answer)

    # messagebox.showinfo("INFO", "INFORMATION")

    messagebox.showerror("ERROR", "INFORMATION")

def createWindow():
    global extraWindow

    extraWindow = tk.Toplevel()
    extraWindow.title("Extra Window")
    extraWindow.geometry("300x400")

    ttk.Label(extraWindow, text = "Label #1").pack()
    ttk.Button(extraWindow, text = "Button #1").pack()
    ttk.Label(extraWindow, text = "Label #2").pack(expand = True)

def closeWindow():
    extraWindow.destroy()

# Create widgets
button1Widget = ttk.Button(window, text = "Open Main Window", command = createWindow)
button1Widget.pack(expand = True)

button2Widget = ttk.Button(window, text = "Close Main Window", command = closeWindow)
button2Widget.pack(expand = True)

button3Widget = ttk.Button(window, text = "Yes / No Window", command = askYesNo)
button3Widget.pack(expand = True)

# Run window
window.mainloop()