import tkinter as tk
from tkinter import ttk
import os

# USES A BASIC DOWNLOADED THEME BUT IT IS NOT RECOMMENDED

# Create window
class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        
        # Main Window
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(600,600)

        # Theme
        self.tk.call("source", "Styling\\Azure\\azure.tcl") #window.tk.call("source", "Styling\\Azure\\azure.tcl")
        self.tk.call("set_theme", "dark")

        # Widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # Run window
        self.mainloop() 

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x = 0, y = 0, relwidth = 0.3, relheight = 1)

        self.createWidgets()

    def createWidgets(self):
        ### MENU WIDGETS ###
        # BUTTONS 
        menuButton1 = ttk.Button(
            self, 
            text = "Button #1")

        menuButton2 = ttk.Button(
            self, 
            text = "Button #2")

        menuButton3 = ttk.Button(
            self, 
            text = "Button #3")

        # SLIDERS
        menuSlider1 = ttk.Scale(
            self, 
            orient = "vertical")

        menuSlider2 = ttk.Scale(
            self, 
            orient = "vertical")

        # CHECK BOXES
        toggleFrame = ttk.Frame(self)
        
        menuToggle1 = ttk.Checkbutton(
            toggleFrame, 
            text = "Check #1")
        menuToggle2 = ttk.Checkbutton(
            toggleFrame, 
            text = "Check #2")

        # ENTRY
        entryWidget = ttk.Entry(self)

        ### MENU LAYOUT ###
        self.columnconfigure((0,1,2), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = "a")
        
        # Gridded Buttons
        menuButton1.grid(row = 0, column = 0, sticky = "nsew", columnspan = 2, padx = 4, pady = 4)
        menuButton2.grid(row = 0, column = 2, sticky = "nsew", padx = 4, pady = 4)
        menuButton3.grid(row = 1, column = 0, sticky = "nsew", columnspan = 3, padx = 4, pady = 4)
        
        # Gridded Sliders
        menuSlider1.grid(row = 2, column = 0, sticky = "ns", rowspan = 2, pady = 20)
        menuSlider2.grid(row = 2, column = 2, sticky = "ns", rowspan = 2, pady = 20)
        
        # Packed Toggles
        menuToggle1.pack(side = "left", expand = True)
        menuToggle2.pack(side = "left", expand = True)
        
        # Placed Entry
        entryWidget.place(relx = 0.5, rely = 0.95, relwidth = 0.9, anchor = "center")

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx = 0.3, y = 0, relwidth = 0.7, relheight = 1)

        Entry(self, "Entry #1", "Button #1", "green")
        Entry(self, "Entry #2", "Button #2", "blue")

class Entry(ttk.Frame):
    def __init__(self, parent, labelText, buttonText, labelBackground):
        super().__init__(parent)

        label = ttk.Label(self, text = labelText, background = labelBackground)
        button = ttk.Button(self, text = buttonText)

        label.pack(expand = True, fill = "both")
        button.pack(expand = True, fill = "both", pady = 10)

        self.pack(side = "left", expand = True, fill = "both", padx = 20, pady = 20)

# Run window
App("Theme Based App", (600,600))