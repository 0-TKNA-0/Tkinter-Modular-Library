import customtkinter as ctk

# Not required when using CTK
import tkinter as tk
from tkinter import ttk

# https://github.com/TomSchimansky/CustomTkinter
# https://customtkinter.tomschimansky.com/documentation/
# CTK VARIABLES ARE ESSENTIALLY THE SAME AS TK

# Create window
window = ctk.CTk()
window.title("CustomTkinter")
window.geometry("600x400")

# Create widgets
stringVar = ctk.StringVar(value = "CUSTOM STRING")
#CTK LABEL
labelWidget = ctk.CTkLabel(
    window, 
    text = "CTK Label #1", 
    fg_color = ("blue","red"), 
    text_color = ("black","white"),
    corner_radius = 10,
    textvariable = stringVar)
labelWidget.pack()

# CTK BUTTON
buttonWidget = ctk.CTkButton(
    window, 
    text = "CTK Button #1", 
    fg_color = "#FF0", 
    text_color = "#000", 
    hover_color = "#AA0",
    command = lambda: ctk.set_appearance_mode("light"))
buttonWidget.pack()

# CTK FRAME
frameWidget = ctk.CTkFrame(window, fg_color = "transparent")
frameWidget.pack()

# CTK SLIDER
sliderWidget = ctk.CTkSlider(frameWidget)
sliderWidget.pack(padx = 20, pady = 20)

# CTK SWITCH
NEWswitchWidget = ctk.CTkSwitch(
    window, 
    text = "SWITCH", 
    switch_height = 50, 
    switch_width = 100, 
    corner_radius = 2,
    progress_color = "pink",
    border_color = "blue",
    fg_color = "red",
    button_color = "green",
    button_hover_color = "yellow")
NEWswitchWidget.pack()


# Run window
window.mainloop()