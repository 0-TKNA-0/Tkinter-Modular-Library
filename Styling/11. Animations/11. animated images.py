import customtkinter as ctk
from PIL import Image
from os import walk

# Open this Animation folder in vs code, not the repository folder as it probably wont work correctly. 
# The paths are not dynamically set as they use walk()

# Create window
window = ctk.CTk()
window.title("Image Animation")
window.geometry("300x200")

# Create widgets

# Class for the button
class AnimatedButton(ctk.CTkButton):
    def __init__(self, parent, lightPath, darkPath):

        # Animation logic setup
        self.frames = self.importFolders(lightPath, darkPath)
        self.frameIndex = 0
        self.animationLength = len(self.frames) - 1
        self.animationStatus = ctk.StringVar(value = "start")

        self.animationStatus.trace("w", self.animate)

        super().__init__(master = parent, text = "Button Animation", image = self.frames[self.frameIndex], command = self.triggerAnimation) # command = self.infiniteAnimate

        self.pack(expand = True)

    # function for importing folders
    def importFolders(self, lightPath, darkPath):
	    imagePaths = []
	    for path in (lightPath, darkPath):
		    for folder, subFolder, imageData in walk(path):
			    sorted_data = sorted(
					imageData, 
					key = lambda item: int(item.split('.')[0][-5:]))
				
			    fullPathData = [path + '/' + item for item in sorted_data]
			    imagePaths.append(fullPathData)
	    imagePaths = zip(*imagePaths)

	    ctkImages = []
	    for image_path in imagePaths:
	    	ctkImage = ctk.CTkImage(
	    		light_image = Image.open(image_path[0]), 
	    		dark_image = Image.open(image_path[1]))
	    	ctkImages.append(ctkImage)  
	    return ctkImages

    # function for triggering the animation (state)
    def triggerAnimation(self):
        if self.animationStatus.get() == "start":
            self.frameIndex = 0
            self.animationStatus.set("forward")
        if self.animationStatus.get() == "end":
            self.frameIndex = self.animationLength
            self.animationStatus.set("backward")

    # function for the animation
    def animate(self, *args):
        if self.animationStatus.get() == "forward":
            self.frameIndex += 1
            self.configure(image = self.frames[self.frameIndex])

            if self.frameIndex < self.animationLength:
                self.after(20, self.animate)
            else:
                self.animationStatus.set("end")
                
        if self.animationStatus.get() == "backward":
            self.frameIndex -= 1
            self.configure(image = self.frames[self.frameIndex])

            if self.frameIndex > 0:
                self.after(20, self.animate)
            else:
                self.animationStatus.set("start")

    # extra function to make the animation play infintily
    def infiniteAnimate(self):
        self.frameIndex += 1
        self.frameIndex = 0 if self.frameIndex > self.animationLength else self.frameIndex
        self.configure(image = self.frames[self.frameIndex])
        self.after(20, self.infiniteAnimate)

AnimatedButton(window, "black", "yellow") # dark, light

# Run window
window.mainloop()