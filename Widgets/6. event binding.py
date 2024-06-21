import tkinter as tk
from tkinter import ttk

# List of all events
# pythontutorial.net/tkinter/tkinter-event-binding


def getPosition(event):
    print(f"x: {event.x}, y: {event.y}")

# Create Window
window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

# Create Widgets
textWidget = tk.Text(window)
textWidget.pack()

entryWidget = ttk.Entry(window)
entryWidget.pack()

buttonWidget = ttk.Button(window, text = "BUTTON")
buttonWidget.pack()

# Create Events
window.bind("<Alt-KeyPress-a>", lambda event: print("DEBUG : EVENT"))
window.bind("<KeyPress>", lambda event: print(f"DEBUG : ({event.char}) BUTTOT WAS PRESSED"))
textWidget.bind("<Motion>", getPosition)

entryWidget.bind("<FocusIn>", lambda event: print("DEBUG : ENTRY WIDGET HAS BEEN SELECTED"))
entryWidget.bind("<FocusOut>", lambda event: print("DEBUG : ENTRY WIDGET HAS BEEN SELECTED"))


# HELPFUL EXERCISE
textWidget.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel"))

# Run Window
window.mainloop()