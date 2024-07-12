import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame # required if using scrollable frame
from ttkbootstrap.toast import ToastNotification # required if using toast
from ttkbootstrap.tooltip import ToolTip # required if using tooltip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter # required if using calendar or Floodgauge or Meter

# Create window
window = ttk.Window(themename = "darkly")
window.title("ttkBootstrap Extra Widgets")
window.geometry("600x600")

# Create widgets

# scrollable frame (not very customisable)
scrollFrame = ScrolledFrame(window)
scrollFrame.pack(expand = True, fill = "both")
# creates buttons and labels that are inserted into the scrollable frame
for i in range(100):
    frame = ttk.Frame(scrollFrame)
    ttk.Label(frame, text = f"Label: {i}").pack(fill = "x", side = "left")
    ttk.Button(frame, text = f"Button: {i}").pack(fill = "x", side = "left")
    frame.pack(expand = True, fill = "x")

# Toast / Notification
toast = ToastNotification(
    title = "TITLE", 
    message = "MESSAGE",
    duration = 2000, # in ms
    bootstyle = "dark",
    position = (50, 100,"ne")) # x padding - px, y padding - px, start pos - "NSWE" 

# toast.show_toast() # BUGGED IF USED BY ITSELF - USE WITH A BUTTON
ttk.Button(window, text = "TOAST", command = toast.show_toast).pack(pady = 10)


# Tooltip
button = ttk.Button(window, text = "TOOLTIP", bootstyle = "warning")
button.pack(pady = 10)
ToolTip(button, text = "TOOLTIP", bootstyle = "danger-inverse")

# Calendar
calendar = DateEntry(window)
calendar.pack(pady = 10)

ttk.Button(window, text = "Get Calendar Date", command = lambda: print(calendar.entry.get())).pack()

# Progress Bar --- floodgauge
progressInt = ttk.IntVar(value = 50)
progress = ttk.Floodgauge(
    window, 
    text = "Progress", 
    variable = progressInt,
    bootstyle = "danger",
    mask = "Mask Text - {}%")
progress.pack(pady = 10, fill = "x")

ttk.Scale(window, from_ = 0, to = 100, variable = progressInt).pack()

# meter 
# NOT WORKING ON MY MACHINE BECAUSE OF A PILLOW ERROR

# Exception has occurred: AttributeError
# module 'PIL.Image' has no attribute 'CUBIC'
# AttributeError: module 'PIL.Image' has no attribute 'CUBIC'

# meter = ttk.Meter(
# 	window,
# 	amounttotal = 100,
# 	amountused = 10,
# 	interactive = True,
# 	metertype = "semi",
# 	subtext = "Text",
# 	bootstyle = "danger"
# 	)
# meter.pack()


# Run window
window.mainloop()