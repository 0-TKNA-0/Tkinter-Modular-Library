import tkinter as tk
from tkinter import ttk

# Create Window
window = tk.Tk()
window.geometry("600x400")
window.title("Canvas")

# Create Widget
canvasWidget = tk.Canvas(window, background = "gray")
canvasWidget.pack()

canvasWidget.create_rectangle(
    (50, 20, 100, 200), 
    fill = "white", 
    width = 3, 
    dash = (1,2), 
    outline = "pink")

canvasWidget.create_line(
    (200, 100, 100, 150), 
    fill = "blue")

canvasWidget.create_oval(
    (300, 0, 400, 100), 
    fill = "red")

canvasWidget.create_arc(
    (300, 0, 400, 100), 
    fill = "green", 
    start = 45, 
    extent = 180, 
    style = tk.ARC, 
    outline = "blue", 
    width = 5)


canvasWidget.create_polygon(
    (0, 0, 100, 200, 300, 50, 150, -50))


canvasWidget.create_text(
    (200, 200), 
    text = "TESTING", 
    fill = "Black", 
    width = 1)

canvasWidget.create_window(
    (50, 100), 
    window = ttk.Button(
        window, 
        text = "TESTING CANVAS"))


# HELPFUL EXERCISE
def drawOnCanvas(event):
    x = event.x
    y = event.y
    canvasWidget.create_oval((x - brushSize/2, y - brushSize/2, x + brushSize/2, y + brushSize/2), fill = "black")

def brushSizeAdjust(event):
    global brushSize
    if event.delta > 0:
        brushSize += 4
    else:
        brushSize -= 4

    brushSize = max(0, min(brushSize, 50))

brushSize = 2
canvasWidget.bind("<Motion>", drawOnCanvas)
canvasWidget.bind("<MouseWheel>", brushSizeAdjust)

# Run Window
window.mainloop()
