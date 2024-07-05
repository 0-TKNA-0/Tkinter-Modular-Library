import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.title("Toggling Widgets")
window.geometry("600x400")

# TOGGLING USING PLACE
# def toggleLabelPlace():
#     global labelVisible
# 
#     if labelVisible:
#         labelWidget.place_forget()
#         labelVisible = False
#     else:
#         labelVisible = True
#         labelWidget.place(relx = 0.5, rely = 0.5, anchor = "center")
# 
# # Create Widgets
# buttonWidget = ttk.Button(
#     window, 
#     text = "Toggle Label", 
#     command = toggleLabelPlace)
# buttonWidget.place(x = 10, y = 10)
# 
# labelVisible = True
# labelWidget = ttk.Label(
#     window, 
#     text = "Label #1")
# labelWidget.place(relx = 0.5, rely = 0.5, anchor = "center") 


# TOGGLING USING GRID
# def toggleLabelGrid():
#     global labelVisible
# 
#     if labelVisible:
#         labelWidget.grid_forget()
#         labelVisible = False
#     else:
#         labelVisible = True
#         labelWidget.grid(column = 1, row = 0) 
#         
# window.columnconfigure((0,1), weight = 1, uniform = "a")
# window.rowconfigure(0, weight = 1, uniform = "a")
# 
# # Create Widgets
# buttonWidget = ttk.Button(
#     window, 
#     text = "Toggle Label", 
#     command = toggleLabelGrid)
# buttonWidget.grid(column = 0, row = 0)
#  
# labelVisible = True
# labelWidget = ttk.Label(
#     window, 
#     text = "Label #1")
# labelWidget.grid(column = 1, row = 0) 


# TOGGLING USING PACK
def toggleLabelPack():
    global labelVisible

    if labelVisible:
        labelWidget.pack_forget()
        labelVisible = False
        frame.pack(expand = True, before = buttonWidget)
    else:
        labelVisible = True
        frame.pack_forget()
        labelWidget.pack(expand = True, before = buttonWidget)
        
# Create Widgets
labelVisible = True
labelWidget = ttk.Label(
    window, 
    text = "Label #1")
labelWidget.pack(expand = True)

buttonWidget = ttk.Button(
    window, 
    text = "Toggle Label",
    command = toggleLabelPack)
buttonWidget.pack()

frame = ttk.Frame(window)

# Run window
window.mainloop()