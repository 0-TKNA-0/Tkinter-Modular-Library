import tkinter as tk
from tkinter import ttk

# https://www.tutorialspoint.com/python/tk_menu.htm

# Create Window
window = tk.Tk()
window.geometry("600x400")
window.title("Menus")

# Create Menu Widgets
mainMenu = tk.Menu(window)

# Create File Sub Menu
fileMenu = tk.Menu(mainMenu, tearoff = False)
fileMenu.add_command(label = "New", command = lambda : print("DEBUG : NEW FILE"))
fileMenu.add_command(label = "Open", command = lambda : print("DEBUG : OPEN FILE"))
fileMenu.add_separator()
mainMenu.add_cascade(label = "File", menu = fileMenu)


# Create Help Sub Menu
helpMenu = tk.Menu(mainMenu, tearoff = False)
helpMenu.add_command(label = "Help Entry", command = lambda : print(helpCheckString.get()))

helpCheckString = tk.StringVar()
helpMenu.add_checkbutton(label = "Check", onvalue = "on", offvalue = "off", variable = helpCheckString)
mainMenu.add_cascade(label = "Help", menu = helpMenu)

window.config(menu = mainMenu)

# Create Menu Button
menuButton = ttk.Menubutton(window, text = "Menu Button")
menuButton.pack()


buttonMenu = tk.Menu(menuButton, tearoff = False)
buttonMenu.add_command(label = "Entry #1", command = lambda : print ("DEBUG : MENU BUTTON"))
buttonMenu.add_checkbutton(label = "CHECK", command = lambda : print ("DEBUG : CHECK BUTTON"))
menuButton.config(menu = buttonMenu)



# HELPFUL EXERCISE (INCLUDES MENU NESTING)
NEWMenu = tk.Menu(mainMenu, tearoff = False)
NEWMenu.add_command(label = "TEST")
mainMenu.add_cascade(label = "TESTING", menu = NEWMenu)

NEWSubMenu = tk.Menu(mainMenu, tearoff = False)
NEWSubMenu.add_command(label = "TESTING AGAIN")
NEWMenu.add_cascade(label = "TESTING AGAIN", menu = NEWSubMenu)


# Run Window
window.mainloop()