import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Packing with frames")
window.geometry("400x600")

# Create Top frame and widgets
topFrame = ttk.Frame(window)

label1Widget = ttk.Label(
    topFrame, 
    text = "Label #1", 
    background = "red")

label2Widget = ttk.Label(
    topFrame, 
    text = "Label #2", 
    background = "blue")

# Top frame layout
label1Widget.pack(side = "left", fill = "both", expand = True)
label2Widget.pack(side = "left", fill = "both", expand = True)
topFrame.pack(fill = "both", expand = True)


# Create widget in the middle
label3Widget = ttk.Label(
    window, 
    text = "Label #3", 
    background = "green")
label3Widget.pack(expand = True)


# Create bottom frame and widgets
bottomFrame = ttk.Frame(window)

label4Widget = ttk.Label(
    bottomFrame, 
    text = "Label #4", 
    background = "orange")

button1Widget = ttk.Button(
    bottomFrame, 
    text = "Button #1")

button2Widget = ttk.Button(
    bottomFrame, 
    text = "Button #2")

# Bottom frame layout
button1Widget.pack(side = "left", expand = True, fill = "both")
label4Widget.pack(side = "left", expand = True, fill = "both")
button2Widget.pack(side = "left", expand = True, fill = "both")
bottomFrame.pack(expand = True, fill = "both", padx = 20, pady=20)

# HELPFUL EXERCISE

# Create bottom right frame and widgets
bottomRightFrame = ttk.Frame(bottomFrame)

button3Widget = ttk.Button(
    bottomRightFrame, 
    text = "Button #3")

button4Widget = ttk.Button(
    bottomRightFrame, 
    text = "Button #4")

button5Widget = ttk.Button(
    bottomRightFrame, 
    text = "Button #5")

# Bottom right frame layout
button3Widget.pack(expand = True, fill = "both")
button4Widget.pack(expand = True, fill = "both")
button5Widget.pack(expand = True, fill = "both")
bottomRightFrame.pack(side = "left", expand = True, fill = "both")


# Run window
window.mainloop()