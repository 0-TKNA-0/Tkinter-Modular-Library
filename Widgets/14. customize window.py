import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Customize window")
# window.geometry("600x400")
window.iconbitmap("Widgets\\python.ico") # Changes the icon 

# Add window sizes 
window.minsize(200, 100)
# window.maxsize(800, 700)
# window.resizable(True,False) # X, Y

# Centres the program to the USERS dead centre of their screen
windowWidth = 600
windowHeight = 400
displayWidth = window.winfo_screenwidth()
displayHeight = window.winfo_screenheight()

centreLeft = int(displayWidth / 2 - windowWidth / 2)
centreTop = int(displayHeight / 2 - windowHeight / 2)
window.geometry(f"{windowWidth}x{windowHeight}+{centreLeft}+{centreTop}")

# Add screen attributes
print(window.winfo_screenwidth()) # returns width of display screen
print(window.winfo_screenheight()) # returns height of display screen

# Add window attributes
window.attributes("-alpha", 1) # 0 - invisible | 1 - visible
# window.attributes("-topmost", True) # Pulls the program infront of every other program
# window.attributes("-disable", True) # Disables the window. Unable to interact with it
#window.attributes("-fullscreen", True) # There will be no title bar

# Add security event
window.bind("<Escape>", lambda event: window.quit())

# Edit title bar
window.overrideredirect(True) # Disables the title bar
grip = ttk.Sizegrip(window) # Adds a widget that allows the user to resize the window
grip.place(relx = 1.0, rely = 1.0, anchor = "se") 

# Run window
window.mainloop()