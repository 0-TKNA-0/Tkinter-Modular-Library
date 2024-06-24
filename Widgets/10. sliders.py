import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


# Create Window
window = tk.Tk()
window.title("Sliders")

# Create Scale slider widgets
scaleWidgetFloat = tk.DoubleVar(value = 5)
scaleWidget = ttk.Scale(
    window, 
    command = lambda value: progressWidget.stop(), 
    from_ = 0, 
    to = 10,
    length = 300,
    orient = "horizontal",
    variable = scaleWidgetFloat)
scaleWidget.pack()

# Create Progress bar widget
progressWidget = ttk.Progressbar(
    window, 
    variable = scaleWidgetFloat, 
    maximum = 10,
    orient = "horizontal",
    mode = "indeterminate",
    length = 300)
progressWidget.pack()

#progressWidget.start(500)

# Create scrolled text widget
scrolledtextWidget = scrolledtext.ScrolledText(
    window, 
    width = 100, 
    height = 5)
scrolledtextWidget.pack()

# HELPFUL EXERCISE
NEWScaleWidgetInt = tk.IntVar()
NEWProgressWidget = ttk.Progressbar(
    window, 
    variable = NEWScaleWidgetInt, 
    maximum = 100, 
    orient = "vertical")
NEWProgressWidget.pack(pady=(10,0))
NEWProgressWidget.start()

labelWidget = ttk.Label(window, textvariable = NEWScaleWidgetInt)
labelWidget.pack()

NEWScaleWidget = ttk.Scale(
    window, 
    from_= 0, 
    to = 100, 
    variable = NEWScaleWidgetInt)
NEWScaleWidget.pack()

# Run window
window.mainloop()