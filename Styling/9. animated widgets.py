import customtkinter as ctk

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, startPos, endPos):
        super().__init__(master = parent)

        # General attributes
        self.startPos = startPos # + 0.01 - For left side of screen
        self.endPos = endPos - 0.01
        self.width = abs(startPos - endPos)

        # animation logic
        self.pos = self.startPos
        self.inStartPos = True

        # Layout
        self.place(relx = self.startPos, rely = 0.05, relwidth = self.width, relheight = 0.9)


    def animate(self):
        if self.inStartPos:
            self.animateForward()
        else:
            self.animateBackward()
    
    def animateForward(self):
        if self.pos > self.endPos:
            self.pos -= 0.01 # animation speed
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
            self.after(10, self.animateForward)
        else:
            self.inStartPos = False
    
    def animateBackward(self):
        if self.pos < self.startPos:
            self.pos += 0.01 # animation speed
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
            self.after(10, self.animateBackward)
        else:
            self.inStartPos = True

# Create window
window = ctk.CTk()
window.title("Animated Widgets")
window.geometry("600x400")
# ctk.set_appearance_mode("light")

# DEBUG / TESTING
def moveButton():
    global buttonX
    buttonX += 0.001
    button.place(relx = buttonX, rely = 0.5, anchor = "center")

    if buttonX < 0.9:
        window.after(10, moveButton)

# Animated Widget
animatedPanel = SlidePanel(window, 1.0, 0.7) # left side of screen pos 0, -0.3
ctk.CTkLabel(animatedPanel, text = "Label #1").pack(expand = True, fill = "both", padx = 2, pady = 10)
ctk.CTkLabel(animatedPanel, text = "Label #2").pack(expand = True, fill = "both", padx = 2, pady = 10)
ctk.CTkButton(animatedPanel, text = "Button #1", corner_radius = 0).pack(expand = True, fill = "both", pady = 10)
ctk.CTkTextbox(animatedPanel, fg_color = ("#dbdbdb", "#2b2b2b")).pack(expand = True, fill = "both", pady = 10)

# Create widgets
buttonX = 0.5
button = ctk.CTkButton(window, text = "SideBar", command = animatedPanel.animate)
button.place(relx = buttonX, rely = 0.5, anchor = "center")

# Run window
window.mainloop()