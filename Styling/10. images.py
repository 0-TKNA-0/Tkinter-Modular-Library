import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

# Create window
window = tk.Tk()
window.geometry("600x400")
window.title("Images")

# Gridded layout
window.columnconfigure((0,1,2,3), weight = 1, uniform = "a")
window.rowconfigure(0, weight = 1)

# Import images
imageOriginal = Image.open("Styling\\images\\raccoon.jpg")
imageOriginalRatio = imageOriginal.size[0] / imageOriginal.size[1]
imageOriginalTK = ImageTk.PhotoImage(imageOriginal)

pythonDark = Image.open("Styling\\images\\python_dark.png").resize((30,30))
pythonDarkTK = ImageTk.PhotoImage(pythonDark) 

# CTK way
imageCTK = ctk.CTkImage(
    light_image = Image.open("Styling\\images\\python_dark.png"), 
    dark_image = Image.open("Styling\\images\\python_light.png"))

# Create widgets
buttonFrame = ttk.Frame(window)

button = ttk.Button(buttonFrame, text = "   Button", image = pythonDarkTK, compound = "left")
button.pack(pady = 10)

# Cant use photoimage inside of CTK widgets
buttonCTK = ctk.CTkButton(buttonFrame, text = "   Button", image = imageCTK, compound = "left")
buttonCTK.pack(pady = 10)

buttonFrame.grid(column = 0, row = 0, sticky = "nsew")

#### Convert a canvas to an image ####

# NOT RECOMMENDED
def stretchImage(event):
    global resizeImageTK

    # Window size
    width = event.width
    height = event.height

    # Resize image
    resizeImage = imageOriginal.resize((width, height))
    resizeImageTK = ImageTk.PhotoImage(resizeImage)

    # Place on Canvas
    canvasWidget.create_image(0,0, image = resizeImageTK, anchor = "nw")

# Keep same aspect ratio of image when resizing
# RECOMMENDED IMPLEMENTATION
def fillImage(event):
    global resizeImageTK

    # current canvas ratio
    canvasRatio = event.width / event.height

    # Image Coordinates
    if canvasRatio > imageOriginalRatio: # canvas is wider that the image    
        width = int(event.width)
        height = int (width / imageOriginalRatio)
    else:  # Canvas is narrower than the image
        height = int (event.height)
        width = int(height * imageOriginalRatio)

    resizeImage = imageOriginal.resize((width, height))
    resizeImageTK = ImageTk.PhotoImage(resizeImage)

    canvasWidget.create_image(int(event.width / 2), int(event.height / 2), anchor = "center", image = resizeImageTK)

# NOT RECOMMENDED
def showFullImage(event):
    global resizeImageTK

    # current canvas ratio
    canvasRatio = event.width / event.height

    # Image Coordinates
    if canvasRatio > imageOriginalRatio: # canvas is wider that the image    
        width = int(event.height)
        height = int (height * imageOriginalRatio)
    else:  # Canvas is narrower than the image
        width = int(event.width)
        height = int (width / imageOriginalRatio)

    resizeImage = imageOriginal.resize((width, height))
    resizeImageTK = ImageTk.PhotoImage(resizeImage)

    canvasWidget.create_image(int(event.width / 2), int(event.height / 2), anchor = "center", image = resizeImageTK)

canvasWidget = tk.Canvas(window, bd = 0, highlightthickness = 0, relief = "ridge", background = "black")
canvasWidget.grid(column = 1, row = 0, columnspan = 3, sticky = "nsew")
canvasWidget.bind("<Configure>", fillImage)

# Run window
window.mainloop()