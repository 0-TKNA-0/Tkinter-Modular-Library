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
buttonWidget.place(relx = 1, rely = 1, anchor = "se")


# Create frame
frameWidget = ttk.Frame(window)

labelFrame = ttk.Label(
    frameWidget, 
    text = "Label Inside of\n a Frame", 
    background = "yellow")

buttonFrame = ttk.Button(
    frameWidget, 
    text = "Button Inside of\n a Frame")

# Place Frame
frameWidget.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)
labelFrame.place(relx = 0, rely = 0, relwidth= 1, relheight = 0.5)
buttonFrame.place(relx = 0, rely = 0.5, relwidth= 1, relheight = 0.5)

# Helpful Exercise
NEWLabel = ttk.Label(
    window, 
    text = "NEW LABEL",
    background = "orange")

NEWLabel.place(relx = 0.5, rely = 0.5, relwidth = 0.5, height = 200, anchor = "center")
# Run window
window.mainloop()